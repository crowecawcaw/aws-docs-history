# Reading and writing from and to

Amazon Redshift

The following code examples use PySpark to read and write sample data from and to
an Amazon Redshift database with data source API and using SparkSQL.

Data source API
Use PySpark to read and write sample data from and to an Amazon Redshift
database with data source API.

```
import boto3
from pyspark.sql import SQLContext

sc = # existing SparkContext
sql_context = SQLContext(sc)

url = "jdbc:redshift:iam://redshifthost:5439/database"
aws_iam_role_arn = "arn:aws:iam::`accountID`:role/`roleName`"

df = sql_context.read \
    .format("io.github.spark_redshift_community.spark.redshift") \
    .option("url", `url`) \
    .option("dbtable", "`tableName`") \
    .option("tempdir", "`s3://path/for/temp/data`") \
    .option("aws_iam_role", "`aws_iam_role_arn`") \
    .load()

df.write \
    .format("io.github.spark_redshift_community.spark.redshift") \
    .option("url", `url`) \
    .option("dbtable", "`tableName_copy`") \
    .option("tempdir", "`s3://path/for/temp/data`") \
    .option("aws_iam_role", "`aws_iam_role_arn`") \
    .mode("error") \
    .save()

```

SparkSQL
Use PySpark to read and write sample data from and to an Amazon Redshift
database with SparkSQL.

```
import boto3
import json
import sys
import os
from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .enableHiveSupport() \
    .getOrCreate()

url = "jdbc:redshift:iam://redshifthost:5439/database"
aws_iam_role_arn = "arn:aws:iam::`accountID`:role/`roleName`"

bucket = "s3://`path/for/temp/data`"
tableName = "`tableName`" # Redshift table name

s = f"""CREATE TABLE IF NOT EXISTS {`tableName`} (country string, data string)
    USING io.github.spark_redshift_community.spark.redshift
    OPTIONS (dbtable '{`tableName`}', tempdir '{`bucket`}', url '{`url`}', aws_iam_role '{`aws_iam_role_arn`}' ); """

spark.sql(s)

columns = ["country" ,"data"]
data = [("`test-country`","`test-data`")]
df = spark.sparkContext.parallelize(data).toDF(columns)

# Insert data into table
df.write.insertInto(`tableName`, overwrite=False)
df = spark.sql(f"SELECT * FROM {`tableName`}")
df.show()
```
