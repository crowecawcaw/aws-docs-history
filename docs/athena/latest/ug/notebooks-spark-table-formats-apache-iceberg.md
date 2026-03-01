# Use Apache Iceberg tables in Athena for Spark

[Apache Iceberg](https://iceberg.apache.org/ "https://iceberg.apache.org/") is an open table
format for large datasets in Amazon Simple Storage Service (Amazon S3). It provides you with fast query
performance over large tables, atomic commits, concurrent writes, and SQL-compatible
table evolution.

To use Apache Iceberg tables in Athena for Spark, configure the following Spark
properties. These properties are configured for you by default in the Athena for Spark
console when you choose Apache Iceberg as the table format. For steps, see [Step 4: Edit session details](notebooks-spark-getting-started.md#notebooks-spark-getting-started-editing-session-details "notebooks-spark-getting-started.md#notebooks-spark-getting-started-editing-session-details") or [Step 7: Create your own notebook](notebooks-spark-getting-started.md#notebooks-spark-getting-started-creating-your-own-notebook "notebooks-spark-getting-started.md#notebooks-spark-getting-started-creating-your-own-notebook").

```
"spark.sql.catalog.spark_catalog": "org.apache.iceberg.spark.SparkSessionCatalog",
"spark.sql.catalog.spark_catalog.catalog-impl": "org.apache.iceberg.aws.glue.GlueCatalog",
"spark.sql.catalog.spark_catalog.io-impl": "org.apache.iceberg.aws.s3.S3FileIO",
"spark.sql.extensions": "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions"
```

The following procedure shows you how to use an Apache Iceberg table in an Athena for
Spark notebook. Run each step in a new cell in the notebook.

###### To use an Apache Iceberg table in Athena for Spark

1. Define the constants to use in the notebook.

```
DB_NAME = "`NEW_DB_NAME`"
TABLE_NAME = "`NEW_TABLE_NAME`"
TABLE_S3_LOCATION = "s3://amzn-s3-demo-bucket"
```

2. Create an Apache Spark [DataFrame](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/dataframe.html "https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/dataframe.html").

```
columns = ["language","users_count"]
data = [("Golang", 3000)]
df = spark.createDataFrame(data, columns)
```

3. Create a database.

```
spark.sql("CREATE DATABASE {} LOCATION '{}'".format(`DB_NAME`, `TABLE_S3_LOCATION`))
```

4. Create an empty Apache Iceberg table.

```
spark.sql("""
CREATE TABLE {}.{} (
language string,
users_count int
) USING ICEBERG
""".format(`DB_NAME`, `TABLE_NAME`))
```

5. Insert a row of data into the table.

```
spark.sql("""INSERT INTO {}.{} VALUES ('Golang', 3000)""".format(`DB_NAME`, `TABLE_NAME`))
```

6. Confirm that you can query the new table.

```
spark.sql("SELECT * FROM {}.{}".format(`DB_NAME`, `TABLE_NAME`)).show()
```

For more information and examples on working with Spark DataFrames and Iceberg tables,
see [Spark
Queries](https://iceberg.apache.org/docs/latest/spark-queries/ "https://iceberg.apache.org/docs/latest/spark-queries/") in the Apache Iceberg documentation.
