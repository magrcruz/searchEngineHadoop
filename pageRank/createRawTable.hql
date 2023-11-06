CREATE TABLE raw_pages (
    url STRING,
    titulo STRING,
    contenido STRING,
    snipet STRING,
    enlaces_salientes ARRAY<STRING>
)
ROW FORMAT SERDE 'org.apache.hive.hcatalog.data.JsonSerDe';

DESCRIBE raw_pages;