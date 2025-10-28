# Using Delta Lake with Amazon EMR on EKS

Delta Lake is an open-source storage framework for building a Lakehouse architecture. The following shows how to set it up for use.

###### To use [Delta Lake](https://delta.io/ "https://delta.io/") with Amazon EMR on EKS

applications

1. When you start a job run to submit a Spark job in the application configuration,
   include the Delta Lake JAR files:

```
--job-driver '{"sparkSubmitJobDriver" : {
      "sparkSubmitParameters" : "--jars local:///usr/share/aws/delta/lib/delta-core.jar,local:///usr/share/aws/delta/lib/delta-storage.jar,local:///usr/share/aws/delta/lib/delta-storage-s3-dynamodb.jar"}}'
```

###### Note

Amazon EMR releases 7.0.0 and higher uses Delta Lake 3.0, which renames `delta-core.jar`
to `delta-spark.jar`. If you use Amazon EMR releases 7.0.0 or higher, be sure to use the correct
file name, such as in the following example:

```
--jars local:///usr/share/aws/delta/lib/delta-spark.jar
```

2. Include Delta Lake additional configuration and use AWS Glue Data Catalog as your
   metastore.

```
--configuration-overrides '{
        "applicationConfiguration": [
        {
          "classification" : "spark-defaults",
          "properties" : {
            "spark.sql.extensions" : "io.delta.sql.DeltaSparkSessionExtension",
            "spark.sql.catalog.spark_catalog":"org.apache.spark.sql.delta.catalog.DeltaCatalog",
"spark.hadoop.hive.metastore.client.factory.class":"com.amazonaws.glue.catalog.metastore.AWSGlueDataCatalogHiveClientFactory"
           }
        }]}'
```
