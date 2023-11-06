--Nota poner todo el contenido de un json en una linea y no poner como un arr d jsons
--Create table
CREATE TABLE crawling (
    url STRING,
    titulo STRING,
    contenido STRING,
    snipet STRING,
    enlaces_salientes ARRAY<STRING>
)
ROW FORMAT SERDE 'org.apache.hive.hcatalog.data.JsonSerDe';

DROP TABLE crawling;
LOAD DATA LOCAL INPATH '/home/magr/Universidad/searchEngineHadoop/out/data.json' INTO TABLE crawling;
SELECT * FROM crawling;

SELECT
    url,
    size(enlaces_salientes) AS cantidad_enlaces_salientes
FROM crawling;