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
