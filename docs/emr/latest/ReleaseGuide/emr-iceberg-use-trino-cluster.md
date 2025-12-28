# Use an Iceberg cluster with Trino

Starting with Amazon EMR version 6.6.0, you can use Iceberg with your Trino cluster.

In this tutorial, you use the AWS CLI to work with Iceberg on an Amazon EMR Trino
cluster. To use the console to create a cluster with Iceberg installed, follow the
steps in [Build an Apache Iceberg data lake using Amazon Athena, Amazon EMR, and
AWS Glue](https://aws.amazon.com/blogs//big-data/build-an-apache-iceberg-data-lake-using-amazon-athena-amazon-emr-and-aws-glue/ "https://aws.amazon.com/blogs//big-data/build-an-apache-iceberg-data-lake-using-amazon-athena-amazon-emr-and-aws-glue/").

## Create an Iceberg

cluster

To use Iceberg on Amazon EMR with the AWS CLI, first create a cluster with the
following steps. For information on specifying the Iceberg classification
using the AWS CLI, see [Supply a configuration using
the AWS CLI when you create a cluster](emr-configure-apps-create-cluster.md#emr-configure-apps-create-cluster-cli "emr-configure-apps-create-cluster.md#emr-configure-apps-create-cluster-cli") or [Supply a configuration using
the Java SDK when you create a cluster](emr-configure-apps-create-cluster.md#emr-configure-apps-create-cluster-sdk "emr-configure-apps-create-cluster.md#emr-configure-apps-create-cluster-sdk").

1. Create an `configurations.json` file with the following
   content. For example, if you want to use the Hive
   metastore as your catalog, your file should have the following
   content.

```
[
  {
    "Classification": "trino-connector-iceberg",
    "Properties": {
      "connector.name": "iceberg",
      "hive.metastore.uri": "thrift://localhost:9083"
    }
  }
]
```

If you want to use the AWS Glue Data Catalog as your store, your file should
have the following content.

```
[
  {
    "Classification": "trino-connector-iceberg",
    "Properties": {
      "connector.name": "iceberg",
      "iceberg.catalog.type": "glue"
    }
  }
]
```

Starting with Amazon EMR 7.7.0, include the property `fs.native-s3.enabled=true`

```
[
  {
    "Classification": "trino-connector-iceberg",
    "Properties": {
      "connector.name": "iceberg",
      "iceberg.catalog.type": "glue",
      "fs.native-s3.enabled": "true"
    }
  }
]
```

2. Create a cluster with the following configuration, replacing the
   example Amazon S3 bucket path and key name with your own.

```
aws emr create-cluster --release-label emr-6.7.0 \
--applications Name=Trino \
--region us-east-1 \
--name My_Trino_Iceberg_Cluster \
--log-uri s3://`amzn-s3-demo-bucket` \
--configurations file://configurations.json \
--instance-groups InstanceGroupType=MASTER,InstanceCount=1,InstanceType=c3.4xlarge InstanceGroupType=CORE,InstanceCount=3,InstanceType=c3.4xlarge \
--use-default-roles \
--ec2-attributes KeyName=`<key-name>`
```

## Initialize a Trino session for

Iceberg

To initialize a Trino session, run the following command.

```
trino-cli --catalog iceberg
```

## Write to an Iceberg

table

Create and write to your table with the following SQL commands.

```
trino> SHOW SCHEMAS;
trino> CREATE TABLE default.iceberg_table (
            id int,
            data varchar,
            category varchar)
       WITH (
            format = 'PARQUET',
            partitioning = ARRAY['category', 'bucket(id, 16)'],
            location = 's3://`amzn-s3-demo-bucket`/<prefix>')

trino> INSERT INTO default.iceberg_table VALUES (1,'a','c1'), (2,'b','c2'), (3,'c','c3');
```

## Read from a table for

Iceberg

To read from your Iceberg table, run the following command.

```
trino> SELECT * from default.iceberg_table;
```

## Considerations for using Iceberg with

Trino

- Amazon EMR 6.5 does not offer Trino Iceberg Catalog support for Iceberg
  natively. Trino needs Iceberg v0.11, so we recommend launching an Amazon EMR
  cluster for Trino separate from the Spark cluster and including Iceberg
  v0.11 on that cluster.
- When using AWS Glue as a catalog for Iceberg, make sure that the database
  in which you are creating a table exists in AWS Glue. If you are using services
  such as AWS Lake Formation and you're unable to load the catalog, make sure you have
  proper access to the service to execute the command.
- Iceberg Glue integration does not work with the Redshift Managed Storage catalog.
