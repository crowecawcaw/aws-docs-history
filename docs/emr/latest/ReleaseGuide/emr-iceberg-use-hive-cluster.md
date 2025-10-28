# Use an Iceberg cluster with Hive

With Amazon EMR releases 6.9.0 and higher, you can use Iceberg with a Hive cluster
without having to perform the setup steps that are required for Open Source Iceberg
Hive Integration. For Amazon EMR versions 6.8.0 and earlier, you can use a bootstrap
action to install `iceberg-hive-runtime` jar for configuring Hive for
Iceberg support.

Amazon EMR 6.9.0 includes all features for [Hive 3.1.3 integration with
Iceberg 0.14.1](https://iceberg.apache.org/releases/#0140-release "https://iceberg.apache.org/releases/#0140-release") and also includes Amazon EMR added features such as auto
selection of supported execution engines at runtime (Amazon EMR on EKS 6.9.0).

## Create an Iceberg cluster

You can create a cluster with Iceberg installed using the AWS Management Console, the
AWS CLI or the Amazon EMR API. In this tutorial, you use the AWS CLI to work with
Iceberg on an Amazon EMR cluster. To use the console to create a cluster with
Iceberg installed, follow the steps in [Build an Iceberg data lake using Amazon Athena, Amazon EMR, and
AWS Glue](https://aws.amazon.com/blogs/big-data/build-an-apache-iceberg-data-lake-using-amazon-athena-amazon-emr-and-aws-glue/ "https://aws.amazon.com/blogs/big-data/build-an-apache-iceberg-data-lake-using-amazon-athena-amazon-emr-and-aws-glue/").

To use Iceberg on Amazon EMR with the AWS CLI, first create a cluster using the
steps below. For information on specifying the Iceberg classification using
the AWS CLI or the Java SDK, see [Supply a configuration using
the AWS CLI when you create a cluster](emr-configure-apps-create-cluster.md#emr-configure-apps-create-cluster-cli "emr-configure-apps-create-cluster.md#emr-configure-apps-create-cluster-cli") or [Supply a configuration using
the Java SDK when you create a cluster](emr-configure-apps-create-cluster.md#emr-configure-apps-create-cluster-sdk "emr-configure-apps-create-cluster.md#emr-configure-apps-create-cluster-sdk"). Create a file named
`configurations.json` with the following content:

```
[{
    "Classification":"iceberg-defaults",
    "Properties":{"iceberg.enabled":"true"}
}]
```

Next, create a cluster with the following configuration, replacing the example
Amazon S3 bucket path and the subnet ID with your own:

```
aws emr create-cluster --release-label emr-6.9.0 \
--applications Name=Hive \
--configurations file://iceberg_configurations.json \
--region us-east-1 \
--name My_hive_Iceberg_Cluster \
--log-uri s3://`amzn-s3-demo-bucket`/ \
--instance-type m5.xlarge \
--instance-count 2 \
--service-role EMR_DefaultRole \
--ec2-attributes InstanceProfile=EMR_EC2_DefaultRole,SubnetId=`subnet-1234567890abcdef`
```

A Hive Iceberg cluster does the following things:

- Loads the Iceberg Hive runtime jar in Hive and enables
  Iceberg-related configuration for the Hive engine.
- Enables Amazon EMR Hive’s dynamic execution engine selection to prevent
  users from setting supported execution engine for Iceberg
  compatibility.

###### Note

Hive Iceberg clusters do not currently support AWS Glue Data Catalog. The default
Iceberg catalog is `HiveCatalog`, which corresponds to the
metastore configured for the Hive environment. For more information on
catalog management, see [Using HCatalog](https://cwiki.apache.org/confluence/display/Hive/HCatalog+UsingHCat#HCatalogUsingHCat-UsingHCatalog "https://cwiki.apache.org/confluence/display/Hive/HCatalog+UsingHCat#HCatalogUsingHCat-UsingHCatalog") in the [Apache Hive
documentation](https://cwiki.apache.org/confluence/display/HIVE "https://cwiki.apache.org/confluence/display/HIVE").

## Feature support

Amazon EMR 6.9.0 supports Hive 3.1.3 and Iceberg 0.14.1. The feature support is
limited to Iceberg-compatible features for Hive 3.1.2 and 3.1.3. The following
commands are supported:

- With Amazon EMR releases 6.9.0 to 6.12.x, you must include the
  `libfb303` jar in the Hive `auxlib` directory.
  Use the following command to include it:

```
sudo /usr/bin/ln -sf /usr/lib/hive/lib/libfb303-*.jar /usr/lib/hive/auxlib/libfb303.jar
```

With Amazon EMR releases 6.13 and higher, the `libfb303` jar is
automatically symlinked to the Hive `auxlib` directory.

- **Creating a table**
  - **Non-partitioned table**
    – External tables in Hive can be created by providing the
    storage handler as follows:

  ```
  CREATE EXTERNAL TABLE x (i int) STORED BY 'org.apache.iceberg.mr.hive.HiveIcebergStorageHandler'
  ```

  - **Partitioned table** –
    External partitioned tables in Hive can be created as
    follows:

  ```
  CREATE EXTERNAL TABLE x (i int) PARTITIONED BY (j int) STORED BY 'org.apache.iceberg.mr.hive.HiveIcebergStorageHandler'
  ```

###### Note

The `STORED AS` file format of ORC/AVRO/PARQUET is not
supported in Hive 3. The default and only option is Parquet.

- **Dropping a table** – The
  `DROP TABLE` command is used to drop tables, such as in
  the following example:

```
DROP TABLE [IF EXISTS] table_name [PURGE];
```

- **Reading a table** –
  `SELECT` statements can be used to read Iceberg tables
  in Hive, such as in the following example. Supported execution engines
  are MR and Tez.

```
SELECT * FROM table_name
```

For information on Hive’s select syntax, see [LanguageManual Select](https://cwiki.apache.org/confluence/display/Hive/LanguageManual+Select "https://cwiki.apache.org/confluence/display/Hive/LanguageManual+Select"). For information on select statements
with Iceberg tables in Hive, see [Apache
Iceberg Select](https://iceberg.apache.org/docs/latest/hive/#select "https://iceberg.apache.org/docs/latest/hive/#select").

- **Inserting into a table** –
  HiveQL‘s `INSERT INTO` statement works on Iceberg tables
  with support for the Map Reduce execution engine only. Amazon EMR users don’t
  need to explicitly set the execution engine because Amazon EMR Hive selects
  the engine for Iceberg Tables at runtime.
  - **Single table insert into**
    – Example:

  ```
  INSERT INTO table_name VALUES ('a', 1);
  INSERT INTO table_name SELECT...;
  ```

  - **Multi-table insert into**
    – Non-atomic multi-table insert into statements are
    supported. Example:

  ```
  FROM source
   INSERT INTO table_1 SELECT a, b
   INSERT INTO table_2 SELECT c,d;
  ```

Starting with Amazon EMR 7.3.0, Hive with Iceberg supports the AWS Glue Data Catalog as a metastore. To use
the AWS Glue Data Catalog as the metastore, set the following property.

```
SET iceberg.catalog.<catalog_name>.catalog-impl=org.apache.iceberg.aws.glue.GlueCatalog;
```

Alternatively, you can also set the following property.

```
SET iceberg.catalog.<catalog_name>.type=glue;
```

You can then create a table using the following example.

```
CREATE EXTERNAL TABLE table_name (col1 type1, col2 type2,..)
ROW FORMAT SERDE 'org.apache.iceberg.mr.hive.HiveIcebergSerDe'
STORED BY 'org.apache.iceberg.mr.hive.HiveIcebergStorageHandler'
location '<location>'
TBLPROPERTIES ('table_type'='iceberg', 'iceberg.catalog'='<catalog_name>');
```

## Considerations for using Iceberg with

Hive

- Iceberg supports the following query types:
  - Create table
  - Drop table
  - Insert into table
  - Read table

- Only the MR (MapReduce) execution engine is supported for DML (data
  manipulation language) operations, and MR is deprecated in Hive
  3.1.3.

- For Amazon EMR prior to 7.3.0, AWS Glue Data Catalog is not currently supported for Iceberg with Hive.

- Error handling is insufficiently robust. In cases of misconfiguration,
  inserts into queries might complete successfully. However, failure to update
  metadata can result in data loss.
- Iceberg Glue integration does not work with the Redshift Managed Storage catalog.
