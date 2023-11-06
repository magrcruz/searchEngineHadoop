LOAD DATA INPATH 's3://hive-bucket-bigdata/rawPages/toydata.txt' INTO TABLE raw_pages;

SELECT COUNT(*) AS total_elementos FROM raw_pages;
SELECT * FROM raw_pages
LIMIT 10;
SELECT
    url,
    size(enlaces_salientes) AS cantidad_enlaces_salientes
FROM raw_pages
LIMIT 10;


DROP TABLE IF EXISTS raw_pages;

CREATE TABLE raw_pages (
    url STRING,
    titulo STRING,
    contenido STRING,
    snipet STRING,
    enlaces_salientes ARRAY<STRING>
)
ROW FORMAT SERDE 'org.apache.hive.hcatalog.data.JsonSerDe';

DESCRIBE raw_pages;