# Using Apache Iceberg with EMR Serverless

This section describes how to use Apache Iceberg with EMR Serverless applications. Apache Iceberg is a table format that
helps working with large data sets in data lakes.

###### To use Apache Iceberg with EMR Serverless applications

1. Set the required Spark properties in the corresponding Spark job run.

```
spark.jars=/usr/share/aws/iceberg/lib/iceberg-spark3-runtime.jar
```

2. Designate either the AWS Glue Data Catalog as your metastore or configure an external
   metastore. To learn more about setting up your metastore, refer to [Metastore configuration for EMR Serverless](metastore-config.md "metastore-config.md").

Configure the metastore properties that you want to use for Iceberg. For
example, if you want to use the AWS Glue Data Catalog, set the following properties in the
application configuration.

```
spark.sql.catalog.dev.warehouse=s3://`amzn-s3-demo-bucket`/`EXAMPLE-PREFIX`/
spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions
spark.sql.catalog.dev=org.apache.iceberg.spark.SparkCatalog
spark.sql.catalog.dev.catalog-impl=org.apache.iceberg.aws.glue.GlueCatalog
spark.hadoop.hive.metastore.client.factory.class=com.amazonaws.glue.catalog.metastore.AWSGlueDataCatalogHiveClientFactory
```

When you use the AWS Glue Data Catalog as your metastore, specify the following
configuration properties for your Iceberg job.

```
--conf spark.jars=/usr/share/aws/iceberg/lib/iceberg-spark3-runtime.jar,
--conf spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions,
--conf spark.sql.catalog.dev=org.apache.iceberg.spark.SparkCatalog,
--conf spark.sql.catalog.dev.catalog-impl=org.apache.iceberg.aws.glue.GlueCatalog,
--conf spark.sql.catalog.dev.warehouse=s3://`amzn-s3-demo-bucket`/`EXAMPLE-PREFIX`/
--conf spark.hadoop.hive.metastore.client.factory.class=com.amazonaws.glue.catalog.metastore.AWSGlueDataCatalogHiveClientFactory
```

To learn more about Apache Iceberg releases of Amazon EMR, refer to [Iceberg release
history](../ReleaseGuide/Iceberg-release-history.md "../ReleaseGuide/Iceberg-release-history.md").
