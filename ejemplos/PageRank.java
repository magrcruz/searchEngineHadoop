import java.io.IOException;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class PageRank {
    public static class PageRankMapper extends Mapper<Object, Text, Text, Text> {
        @Override
        protected void map(Object key, Text value, Context context) throws IOException, InterruptedException {
            String[] parts = value.toString().split("\t");
            String page = parts[0];
            String links = parts[1];

            String[] linkArray = links.split(" ");
            double pageRank = 1.0 / linkArray.length;

            for (String link : linkArray) {
                context.write(new Text(link), new Text(String.valueOf(pageRank)));
            }

            context.write(new Text(page), new Text("!" + links));
        }
    }

    public static class PageRankReducer extends Reducer<Text, Text, Text, Text> {
        @Override
        protected void reduce(Text key, Iterable<Text> values, Context context) throws IOException, InterruptedException {
            double newPageRank = 0.0;
            String links = "";
            
            for (Text value : values) {
                String val = value.toString();
                if (val.startsWith("!")) {
                    links = val.substring(1);
                } else {
                    newPageRank += Double.parseDouble(val);
                }
            }

            double dampingFactor = 0.85;
            double finalPageRank = (1.0 - dampingFactor) + dampingFactor * newPageRank;

            context.write(key, new Text(finalPageRank + "\t" + links));
        }
    }

    public static void main(String[] args) throws Exception {
        Configuration conf = new Configuration();
        Job job = Job.getInstance(conf, "PageRank");

        job.setJarByClass(PageRank.class);
        job.setMapperClass(PageRankMapper.class);
        job.setReducerClass(PageRankReducer.class);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(Text.class);

        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));

        for (int i = 0; i < 100; i++) {
            job.waitForCompletion(true);
        }
    }
}
