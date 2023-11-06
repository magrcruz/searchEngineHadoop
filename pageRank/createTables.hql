-- Crea tabla de enlaces fuente y destino
DROP TABLE IF EXISTS links;

CREATE TABLE links AS
SELECT
  url AS source,
  enlace AS dest
FROM
  raw_pages
LATERAL VIEW explode(enlaces_salientes) enlaces AS enlace;


-- Tabla temporal para almacenar los valores iniciales de PageRank
DROP TABLE IF EXISTS pagerank_temp;

CREATE TABLE pagerank_temp AS
SELECT DISTINCT
  source,
  1.0 AS pagerank
FROM
  links;

SHOW TABLES;