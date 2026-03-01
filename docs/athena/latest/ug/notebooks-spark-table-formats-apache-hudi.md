# Use Apache Hudi tables in Athena for Spark

[**Apache
Hudi**](https://hudi.apache.org/ "https://hudi.apache.org/") is an open-source data management framework
that simplifies incremental data processing. Record-level insert, update, upsert, and
delete actions are processed with greater precision, which reduces overhead.

To use Apache Hudi tables in Athena for Spark, configure the following Spark
properties. These properties are configured for you by default in the Athena for Spark
console when you choose Apache Hudi as the table format. For steps, see [Step 4: Edit session details](notebooks-spark-getting-started.md#notebooks-spark-getting-started-editing-session-details "notebooks-spark-getting-started.md#notebooks-spark-getting-started-editing-session-details") or [Step 7: Create your own notebook](notebooks-spark-getting-started.md#notebooks-spark-getting-started-creating-your-own-notebook "notebooks-spark-getting-started.md#notebooks-spark-getting-started-creating-your-own-notebook").

```
"spark.sql.catalog.spark_catalog": "org.apache.spark.sql.hudi.catalog.HoodieCatalog",
"spark.serializer": "org.apache.spark.serializer.KryoSerializer",
"spark.sql.extensions": "org.apache.spark.sql.hudi.HoodieSparkSessionExtension"
```

The following procedure shows you how to use an Apache Hudi table in an Athena for
Spark notebook. Run each step in a new cell in the notebook.

###### To use an Apache Hudi table in Athena for Spark

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

4. Create an empty Apache Hudi table.

```
spark.sql("""
CREATE TABLE {}.{} (
language string,
users_count int
) USING HUDI
TBLPROPERTIES (
primaryKey = 'language',
type = 'mor'
);
""".format(`DB_NAME`, `TABLE_NAME`))
```

5. Insert a row of data into the table.

```
spark.sql("""INSERT INTO {}.{} VALUES ('Golang', 3000)""".format(`DB_NAME`,`TABLE_NAME`))
```

6. Confirm that you can query the new table.

```
spark.sql("SELECT * FROM {}.{}".format(`DB_NAME`, `TABLE_NAME`)).show()
```
