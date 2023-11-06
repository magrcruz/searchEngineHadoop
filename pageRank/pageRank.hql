-- Número de iteraciones
SET hivevar:num_iterations=1;

--Realiza una onda del pageRank sin normalizar
DROP TABLE IF EXISTS pagerank_contribuciones;

CREATE TABLE pagerank_contribuciones AS
SELECT
  link.dest AS source,
  --Suma los pesos que entran a la pagina
  SUM(pr.pagerank / num_links) AS contribucion
FROM
  links link
  JOIN pagerank_temp pr ON link.source = pr.source
  JOIN (
    --Calcula el numero de enlaces salientes
    SELECT
      source,
      COUNT(1) AS num_links
    FROM
      links
    GROUP BY
      source
  ) link_counts ON link.source = link_counts.source
GROUP BY
  link.dest;

-- Damping Factor
-- Calcula el nuevo PageRank para cada página
DROP TABLE IF EXISTS pagerank_temp;

CREATE TABLE pagerank_temp AS
SELECT
  source,
  0.15 + 0.85 * pc.contribucion AS pagerank
FROM
  pagerank_contribuciones pc;


SELECT * from pagerank_temp
LIMIT 10;