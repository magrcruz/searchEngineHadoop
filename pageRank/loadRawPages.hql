
LOAD DATA INPATH 's3://hive-bucket-bigdata/rawPages/paginas0000-0199.txt' INTO TABLE raw_pages;
LOAD DATA INPATH 's3://hive-bucket-bigdata/rawPages/paginas0200-0399.txt' INTO TABLE raw_pages;
LOAD DATA INPATH 's3://hive-bucket-bigdata/rawPages/paginas0400-0599.txt' INTO TABLE raw_pages;
LOAD DATA INPATH 's3://hive-bucket-bigdata/rawPages/paginas0600-0799.txt' INTO TABLE raw_pages;
LOAD DATA INPATH 's3://hive-bucket-bigdata/rawPages/paginas0800-0999.txt' INTO TABLE raw_pages;
LOAD DATA INPATH 's3://hive-bucket-bigdata/rawPages/paginas1000-1199.txt' INTO TABLE raw_pages;
LOAD DATA INPATH 's3://hive-bucket-bigdata/rawPages/paginas1200-1399.txt' INTO TABLE raw_pages;
LOAD DATA INPATH 's3://hive-bucket-bigdata/rawPages/paginas1400-1599.txt' INTO TABLE raw_pages;
LOAD DATA INPATH 's3://hive-bucket-bigdata/rawPages/paginas1600-1799.txt' INTO TABLE raw_pages;
LOAD DATA INPATH 's3://hive-bucket-bigdata/rawPages/paginas1800-1999.txt' INTO TABLE raw_pages;

SELECT COUNT(*) AS total_elementos FROM raw_pages;
SELECT * FROM raw_pages
LIMIT 10;
