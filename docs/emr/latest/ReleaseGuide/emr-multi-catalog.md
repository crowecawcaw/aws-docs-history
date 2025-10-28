# Working with a multi-catalog hierarchy in AWS Glue Data Catalog with Spark on Amazon EMR

You can register your Amazon EMR cluster to access the AWS Glue Data Catalog, which makes tables and other catalog resources available to
various consumers. AWS Glue Data Catalog supports a multi-catalog hierarchy, which unifies your data across Amazon S3 data lakes. It also provides both a Hive metastore API and an
open-source Apache Iceberg REST API for accessing the data. These features are available to Amazon EMR and other services like Amazon Athena and Amazon Redshift.

## How catalog resources are organized

When you create
resources in the AWS Glue Data Catalog, you can access them from any SQL engine that supports the Apache Iceberg REST API or Hive metastore. AWS Lake Formation manages
permissions.

In AWS Glue Data Catalog, data is organized in a logical hierarchy of catalogs, databases and tables:

- **Catalog** – A logical container that holds objects from a data store, such as schemas or tables.
- **Catalog to store Redshift Managed Storage (RMS) tables** – When you manage catalogs to store RMS tables, you can access
  these tables using Iceberg.
- **Database** – Organizes data objects such as tables and views in a catalog.
- **Tables and views** – Data objects in a database that provide an abstraction layer with an understandable schema. They provide a layer to access underlying data, which
  can be in various formats and in different locations.

## Configuring a data catalog for use with Amazon EMR

To get started, you configure the catalog to support Amazon EMR tools. The AWS Glue Data Catalog provides Hive metastore compatibility and Iceberg REST compatible APIs.

**Configuring Amazon EMR with a Hive metastore**

For information about how to set this up,
see [AWS Glue Data Catalog support for Spark jobs](../../../glue/latest/dg/aws-glue-programming-etl-glue-data-catalog-hive.md "../../../glue/latest/dg/aws-glue-programming-etl-glue-data-catalog-hive.md") in the AWS Glue User Guide. This topic describes
how to configure AWS Glue Data Catalog as a Hive metastore and make it available as an endpoint. Additionally, there is Amazon EMR documentation available that shows you
how to specify AWS Glue Data Catalog as a Spark metastore,
in [Use the AWS Glue Data Catalog as the Apache Hive metastore for Spark](emr-spark-glue.md "emr-spark-glue.md").

## Permissions for accessing resources in AWS Glue Data Catalog

This section describes the IAM policy requirements for using Amazon EMR tools with catalog data.

After you register your cluster with the AWS Glue Data Catalog, you need the following permissions to discover the creation of and changes to the subsequently created data catalog:

- **glue:GetCatalog**
- **glue:GetCatalogs**
- **sts:AssumeRole**
- **sts:TagSession**
- **sts:SetContext**
- **sts:SetSourceIdentity**

In most cases, when you assign permissions, we
recommend creating an IAM role and assigning permissions to it.

Additionally, to query catalog data, you must set permissions for the data catalog using AWS Lake Formation. For more information on setting permissions for data catalogs in AWS Lake Formation,
see [Granting and revoking permissions on Data Catalog resources](../../../lake-formation/latest/dg/granting-catalog-permissions.md "../../../lake-formation/latest/dg/granting-catalog-permissions.md").

After you create and configure your cluster, and set permissions on your catalog objects, you can submit jobs to query and process data.

## Configure Spark to access a multi-catalog hierarchy in AWS Glue Data Catalog

With EMR 7.5, you can configure Spark to use AWS Glue's multi-catalog heirarchy. A multi-catalog hierarchy allows you to:

- Bring your Redshift Managed Storage (RMS) data, such as tables, views, and materialized views from existing Amazon Redshift data warehouses to AWS Glue Data Catalog. You can query these objects
  using EMR on EC2 and EMR Serverless.
- Create RMS catalogs, AWS Glue Data Catalog and store data in RMS using ZeroETL and query the data with Iceberg-compatible query engines.
- Create managed Iceberg tables in AWS Glue Data Catalog with full-featured storage management that includes compaction, snapshots, and retention.

### Connecting to multi-catalog when you initialize a Spark

session

The following examples demonstrate how to use interactive Spark shell, Spark submit, or Amazon EMR Notebooks to work with AWS Glue’s multi-catalog hierarchy.

spark-shell

1. Connect to the master node using SSH. For more
   information, see [Connect to the master node using SSH](../ManagementGuide/emr-connect-master-node-ssh.md "../ManagementGuide/emr-connect-master-node-ssh.md") in the
   _Amazon EMR Management
   Guide_.
2. Enter the following command to launch the Spark shell. To
   use the PySpark shell, replace `spark-shell` with
   `pyspark`.

```
spark-shell \
    --conf spark.sql.catalog.my_catalog=org.apache.iceberg.spark.SparkCatalog \
    --conf spark.sql.catalog.my_catalog.warehouse=s3://`amzn-s3-demo-bucket`/`prefix`/
    --conf spark.sql.catalog.my_catalog.type=glue \
    --conf spark.sql.catalog.my_catalog.glue.id=`Glue RMS catalog ID` \
    --conf spark.sql.defaultCatalog=my_catalog \
    --conf spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions
```

spark-submit

1. Connect to the master node using SSH. For more
   information, see [Connect to the master node using SSH](../ManagementGuide/emr-connect-master-node-ssh.md "../ManagementGuide/emr-connect-master-node-ssh.md") in the
   _Amazon EMR Management
   Guide_.
2. Enter the following command to launch the Spark session
   for Spark.

```
spark-submit \
--conf spark.sql.catalog.my_catalog=org.apache.iceberg.spark.SparkCatalog \
--conf spark.sql.catalog.my_catalog.warehouse=s3://`amzn-s3-demo-bucket1`/`prefix` \
--conf spark.sql.catalog.my_catalog.type=glue \
--conf spark.sql.catalog.my_catalog.glue.id=`Glue RMS catalog ID` \
--conf spark.sql.defaultCatalog=my_catalog \
--conf spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions
```

EMR Studio notebooks
To initialize a Spark session using EMR Studio notebooks,
configure your Spark session using the `%%configure`
magic command in your Amazon EMR notebook, as in the following example.
For more information, see [Use EMR Notebooks magics](../ManagementGuide/emr-studio-magics.md#emr-magics "../ManagementGuide/emr-studio-magics.md#emr-magics") in the
_Amazon EMR Management Guide_.

```
%%configure -f{
"conf":{
    "spark.sql.catalog.my_catalog":"org.apache.iceberg.spark.SparkCatalog",
    "spark.sql.catalog.my_catalog.type":"glue",
    "spark.sql.catalog.my_catalog.glue.id":"`Glue RMS catalog ID`",
    "spark.sql.catalog.my_catalog.warehouse":"s3://`amzn-s3-demo-bucket1`/`prefix`/",
    "spark.sql.defaultCatalog", "my_catalog",
    "spark.sql.extensions":"org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions"
    }
}
```

CLI
To initialize a Spark session using the CLI, run the following sample. For more information about
specifying a configuration classification using the AWS CLI and Amazon EMR API, see [Configure applications](emr-configure-apps.md "emr-configure-apps.md").

```
[
  {
    "Classification": "spark-defaults",
    "Properties": {
      "spark.sql.catalog.my_catalog":"org.apache.iceberg.spark.SparkCatalog",
      "spark.sql.catalog.my_catalog.type":"glue",
      "spark.sql.catalog.my_catalog.glue.id":"`Glue RMS catalog ID`",
      "spark.sql.catalog.my_catalog.warehouse":"s3://`amzn-s3-demo-bucket1`/`prefix`/",
      "spark.sql.defaultCatalog", "my_catalog",
      "spark.sql.extensions":"org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions"
    }
  }
]
```

#### Initialize a Spark session to Redshift Managed Storage with AWS Glue Data Catalog

The following sample command initializes a Spark session with the AWS Glue Data Catalog.

```
spark-sql \
  --conf spark.sql.catalog.rms=org.apache.iceberg.spark.SparkCatalog \
  --conf spark.sql.catalog.rms.type=glue \
  --conf spark.sql.catalog.rms.glue.id=`Glue RMS catalog ID` \
  --conf spark.sql.defaultCatalog=rms
  --conf spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions
```

The following sample initializes a Spark session using the Iceberg REST API and Redshift Managed Storage with AWS Glue Data Catalog.

```
spark-sql \
  --conf spark.sql.catalog.rms=org.apache.iceberg.spark.SparkCatalog \
  --conf spark.sql.catalog.rms.type=rest \
  --conf spark.sql.catalog.rms.warehouse=`glue RMS catalog ID` \
  --conf spark.sql.catalog.rms.uri=`Glue endpoint URI`/iceberg \
  --conf spark.sql.catalog.rms.rest.sigv4-enabled=true \
  --conf spark.sql.catalog.rms.rest.signing-name=glue \
  --conf spark.sql.defaultCatalog=rms \
  --conf spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions
```

For more information about using an AWS Glue multi-catalog hierarchy with Spark Iceberg,
see [Use an Iceberg cluster with Spark](emr-iceberg-use-spark-cluster.md "emr-iceberg-use-spark-cluster.md").

## Considerations and limitations for a multi-catalog configuration

- Using a multi-catalog hierarchy with Apache Hive metastore is not supported.
- Using a multi-catalog hierarchy with Apache Iceberg cannot support fallback to Apache Hive metastore, when
  using `SparkSessionCatalog`.
- EMR on EC2 clusters with Runtime role don't support multi-catalog hierarchy.
- EMR on EC2 clusters enabled with AWS Lake Formation don't support multi-catalog hierarchy.
