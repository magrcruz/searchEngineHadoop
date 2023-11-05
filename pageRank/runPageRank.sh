#not working
#!/bin/bash

hive -f createLinkTable.hql
hive -f createTables.hql

# Número de veces que deseas ejecutar el archivo HQL
n=10

# Nombre del archivo HQL a ejecutar
hql_file="pageRank.hql"

# Bucle para ejecutar el archivo HQL n veces
for ((i=1; i<=n; i++))
do
  echo "Ejecutando $i de $n..."
  hive -f $hql_file
done

echo "Todas las ejecuciones completadas."
