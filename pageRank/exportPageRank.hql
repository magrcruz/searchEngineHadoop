INSERT OVERWRITE DIRECTORY 's3://hive-bucket-bigdata/pageRank/out' 
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
SELECT * FROM pagerank_temp;
