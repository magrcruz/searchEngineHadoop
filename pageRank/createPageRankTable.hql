-- Tabla temporal para almacenar los valores iniciales de PageRank

DROP TABLE IF EXISTS pagerank_temp;

CREATE TABLE pagerank_temp AS
SELECT DISTINCT
  source,
  1.0 AS pagerank
FROM
  links;
