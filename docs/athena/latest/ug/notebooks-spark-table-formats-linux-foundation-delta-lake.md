# Use Linux Foundation Delta Lake tables in Athena for Spark

[Linux Foundation Delta Lake](https://delta.io/ "https://delta.io/") is a table format
that you can use for big data analytics. You can use Athena for Spark to read Delta Lake
tables stored in Amazon S3 directly.

To use Delta Lake tables in Athena for Spark, configure the following Spark properties.
These properties are configured for you by default in the Athena for Spark console when
you choose Delta Lake as the table format. For steps, see [Step 4: Edit session details](notebooks-spark-getting-started.md#notebooks-spark-getting-started-editing-session-details "notebooks-spark-getting-started.md#notebooks-spark-getting-started-editing-session-details") or [Step 7: Create your own notebook](notebooks-spark-getting-started.md#notebooks-spark-getting-started-creating-your-own-notebook "notebooks-spark-getting-started.md#notebooks-spark-getting-started-creating-your-own-notebook").

```
"spark.sql.catalog.spark_catalog" : "org.apache.spark.sql.delta.catalog.DeltaCatalog",
"spark.sql.extensions" : "io.delta.sql.DeltaSparkSessionExtension"
```

The following procedure shows you how to use a Delta Lake table in an Athena for Spark
notebook. Run each step in a new cell in the notebook.

###### To use a Delta Lake table in Athena for Spark

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

4. Create an empty Delta Lake table.

```
spark.sql("""
CREATE TABLE {}.{} (
  language string,
  users_count int
) USING DELTA
""".format(`DB_NAME`, `TABLE_NAME`))
```

5. Insert a row of data into the table.

```
spark.sql("""INSERT INTO {}.{} VALUES ('Golang', 3000)""".format(`DB_NAME`, `TABLE_NAME`))
```

6. Confirm that you can query the new table.

```
spark.sql("SELECT * FROM {}.{}".format(`DB_NAME, TABLE_NAME`)).show()
```
