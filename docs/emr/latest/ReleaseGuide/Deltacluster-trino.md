# Use a Delta Lake cluster with Trino

With Amazon EMR releases 6.9.0 and higher, you can use Delta Lake with your Trino
cluster.

In this tutorial, we will use the AWS CLI to work with Delta Lake on Amazon EMR Trino
cluster.

##

###### Create a Delta Lake cluster

1. Create a file, `delta_configurations.json`, and set
   values for your chosen catalog. For example, if you want to use the Hive
   metastore as your catalog, your file should have the following
   content:

```
[{"Classification":"delta-defaults",
    "Properties":{"delta.enabled":"true"}},
    {"Classification":"trino-connector-delta",
    "Properties":{"hive.metastore.uri":"thrift://localhost:9083"}}]
```

If you want to use the AWS Glue Catalog as your store, your file
should have the following content:

```
[{"Classification":"delta-defaults",
    "Properties":{"delta.enabled":"true"}},
    {"Classification":"trino-connector-delta",
    "Properties":{"hive.metastore":"glue"}}]
```

2. Create a cluster with the following configuration, replacing the
   `example Amazon S3 bucket path` and the
   `subnet ID` with your own.

```
aws emr create-cluster
    --release-label emr-6.9.0
    --applications Name=Trino
    --configurations file://delta_configurations.json
    --region us-east-1  --name My_Spark_Delta_Cluster
    --log-uri  `s3://amzn-s3-demo-bucket/`
    --instance-type m5.xlarge
    --instance-count 2
    --service-role EMR_DefaultRole_V2
    --ec2-attributes  InstanceProfile=EMR_EC2_DefaultRole,SubnetId=`subnet-1234567890abcdef0`
```

## Initialize Trino session for

Delta Lake

To initialize Trino session, run the following command

```

trino-cli --catalog delta
```

## Write to a Delta Lake table

Create and write to your table with the following SQL commands:

```
SHOW SCHEMAS;

CREATE TABLE default.delta_table (id  int, data varchar, category varchar) WITH
( location =  `'s3://amzn-s3-demo-bucket/<prefix>'`);

INSERT INTO default.delta_table VALUES  (1,'a','c1'), (2,'b','c2'), (3,'c','c3');

```

## Read from a Delta Lake table

Read from your table with the following SQL command:

```

SELECT * from default.delta_table;
```
