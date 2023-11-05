-- Crea tabla de enlaces fuente y destino
CREATE TABLE IF NOT EXISTS links AS
SELECT
  url AS source,
  enlace AS dest
FROM
  temp
LATERAL VIEW explode(enlaces_salientes) enlaces AS enlace;
