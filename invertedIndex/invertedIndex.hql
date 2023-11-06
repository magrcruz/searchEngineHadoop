CREATE EXTERNAL TABLE IF NOT EXISTS indice_invertido (
  termino STRING,
  documento_ids ARRAY<STRING>
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
COLLECTION ITEMS TERMINATED BY '|'
STORED AS TEXTFILE
LOCATION 's3://hive-bucket-bigdata/output/';

INSERT OVERWRITE TABLE indice_invertido
SELECT palabra, collect_set(url) as documento_ids
FROM (
  SELECT url, LOWER(regexp_replace(palabra, '[^a-zA-Z0-9]', '')) as palabra
  FROM raw_pages
  LATERAL VIEW explode(split(regexp_replace(contenido, '[^a-zA-Z0-9 ]', ' '), '\\s+')) lview AS palabra
) t
GROUP BY palabra;
