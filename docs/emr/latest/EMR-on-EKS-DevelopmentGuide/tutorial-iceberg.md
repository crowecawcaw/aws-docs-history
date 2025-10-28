# Using Apache Iceberg with Amazon EMR on EKS

The runtime JAR for Iceberg contains the necessary Iceberg classes for Spark runtime support. The following procedure shows how to start a
job run using the Iceberg spark runtime.

###### To use Apache Iceberg with Amazon EMR on EKS applications

1. When you start a job run to submit a Spark job in the application configuration,
   include the Iceberg spark runtime JAR file:

```
--job-driver '{"sparkSubmitJobDriver" : {"sparkSubmitParameters" : "--jars local:///usr/share/aws/iceberg/lib/iceberg-spark3-runtime.jar"}}'
```

2. Include Iceberg additional configuration:

```
--configuration-overrides '{
    "applicationConfiguration": [
    "classification" : "spark-defaults",
    "properties" : {
        "spark.sql.catalog.dev.warehouse" : "s3://amzn-s3-demo-bucket/EXAMPLE-PREFIX/ ",
        "spark.sql.extensions ":" org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions ",
        "spark.sql.catalog.dev" : "org.apache.iceberg.spark.SparkCatalog",
        "spark.sql.catalog.dev.catalog-impl" : "org.apache.iceberg.aws.glue.GlueCatalog",
        "spark.sql.catalog.dev.io-impl": "org.apache.iceberg.aws.s3.S3FileIO"
        }
    ]
}'

```

To learn more about Apache Iceberg release versions of EMR, see [Iceberg
release history](../ReleaseGuide/Iceberg-release-history.md "../ReleaseGuide/Iceberg-release-history.md").

## Spark session configurations for catalog integration

### Spark session configurations for Iceberg AWS Glue catalog integration

This sample shows how to integrate Iceberg with the AWS Glue crawler:

```
spark-sql \
  --conf spark.sql.catalog.rms = org.apache.iceberg.spark.SparkCatalog \
  --conf spark.sql.catalog.rms.type = glue \
  --conf spark.sql.catalog.rms.glue.id = `glue RMS catalog ID` \
  --conf spark.sql.catalog.rms.glue.account-id = `AWS account ID` \

  --conf spark.sql.extensions=
    org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions
```

The following shows a sample query:

```
SELECT * FROM rms.rmsdb.table1
```

### Spark session configurations for Iceberg REST AWS Glue catalog integration

This sample shows how to integrate Iceberg REST with the AWS Glue crawler:

```
spark-sql \
  --conf spark.sql.catalog.rms = org.apache.iceberg.spark.SparkCatalog \
  --conf spark.sql.catalog.rms.type = rest \
  --conf spark.sql.catalog.rms.warehouse = `glue RMS catalog ID` \
  --conf spark.sql.catalog.rms.uri = `glue endpoint URI`/iceberg \
  --conf spark.sql.catalog.rms.rest.sigv4-enabled = true \
  --conf spark.sql.catalog.rms.rest.signing-name = glue \

  --conf spark.sql.extensions=
    org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions
```

The following shows a sample query:

```
SELECT * FROM rms.rmsdb.table1
```

This configuration works for Redshift Managed Storage only. FGAC for Amazon S3 isn't supported.
