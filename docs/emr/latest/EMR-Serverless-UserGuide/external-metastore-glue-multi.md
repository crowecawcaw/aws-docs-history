# Working with AWS Glue multi-catalog hierarchy on EMR Serverless

You can configure your EMR Serverless applications to work with the AWS Glue multi-catalog hierarchy. The following example shows how to use EMR-S
Spark with the AWS Glue multi-catalog hierarchy.

To learn more about multi-catalog hierarchy,
refer to [Working with a multi-catalog hierarchy in AWS Glue Data Catalog with Spark on Amazon EMR](../ReleaseGuide/emr-multi-catalog.md "../ReleaseGuide/emr-multi-catalog.md").

## Using Redshift Managed Storage (RMS) with Iceberg and AWS Glue Data Catalog

The following demonstrates how to configure Spark for integration with an AWS Glue Data Catalog with Iceberg:

```
aws emr-serverless start-job-run \
    --application-id application-id \
    --execution-role-arn job-role-arn \
    --job-driver '{
        "sparkSubmit": {
            "entryPoint": "s3://amzn-s3-demo-bucket/myscript.py",
            "sparkSubmitParameters": "--conf spark.sql.catalog.nfgac_rms = org.apache.iceberg.spark.SparkCatalog
             --conf spark.sql.catalog.rms.type=glue
             --conf spark.sql.catalog.rms.glue.id=`Glue RMS catalog ID`
             --conf spark.sql.defaultCatalog=rms
             --conf spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions"
        }
    }'
```

A sample query from a table in the catalog, following integration:

```
SELECT * FROM my_rms_schema.my_table
```

## Using Redshift Managed Storage (RMS) with Iceberg REST API and AWS Glue Data Catalog

The following demonstrates how to configure Spark to work with Iceberg REST catalog:

```
aws emr-serverless start-job-run \
--application-id application-id \
--execution-role-arn job-role-arn \
--job-driver '{
"sparkSubmit": {
"entryPoint": "s3://amzn-s3-demo-bucket/myscript.py",
    "sparkSubmitParameters": "
    --conf spark.sql.catalog.rms=org.apache.iceberg.spark.SparkCatalog
    --conf spark.sql.catalog.rms.type=rest
    --conf spark.sql.catalog.rms.warehouse=`Glue RMS catalog ID`
    --conf spark.sql.catalog.rms.uri=`Glue endpoint URI/iceberg`
    --conf spark.sql.catalog.rms.rest.sigv4-enabled=true
    --conf spark.sql.catalog.rms.rest.signing-name=glue
    --conf spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions"
    }
  }'
```

A sample query from a table in the catalog:

```
SELECT * FROM my_rms_schema.my_table
```
