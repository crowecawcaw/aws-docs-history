# Using Apache Hudi with EMR Serverless

This section describes using Apache Hudi with EMR Serverless applications. Hudi is a data-management framework that makes data processing more simple.

###### To use Apache Hudi with EMR Serverless applications

1. Set the required Spark properties in the corresponding Spark job run.

```
spark.jars=/usr/lib/hudi/hudi-spark-bundle.jar,/usr/lib/hudi/hudi-utilities-bundle.jar,/usr/lib/hudi/hudi-aws-bundle.jar
spark.serializer=org.apache.spark.serializer.KryoSerializer
```

2. To sync a Hudi table to the configured catalog, designate either the AWS Glue Data Catalog
   as your metastore, or configure an external metastore. EMR Serverless supports
   `hms` as the sync mode for Hive tables for Hudi workloads.
   EMR Serverless activates this property as a default. To learn more about how to set
   up your metastore, refer to [Metastore configuration for EMR Serverless](metastore-config.md "metastore-config.md").

###### Important

EMR Serverless doesn't support `HIVEQL` or `JDBC` as
sync mode options for Hive tables to handle Hudi workloads. To learn more, refer to
[Sync modes](https://hudi.apache.org/docs/next/syncing_metastore/#sync-modes "https://hudi.apache.org/docs/next/syncing_metastore/#sync-modes").

When you use the AWS Glue Data Catalog as your metastore, specify the following
configuration properties for your Hudi job.

```
--conf spark.jars=/usr/lib/hudi/hudi-spark-bundle.jar,
--conf spark.serializer=org.apache.spark.serializer.KryoSerializer,
--conf spark.hadoop.hive.metastore.client.factory.class=com.amazonaws.glue.catalog.metastore.AWSGlueDataCatalogHiveClientFactory
```

To learn more about Apache Hudi releases of Amazon EMR, refer to [Hudi release
history](../ReleaseGuide/Hudi-release-history.md "../ReleaseGuide/Hudi-release-history.md").
