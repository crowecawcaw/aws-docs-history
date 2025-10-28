# Use a Delta Lake cluster with Spark and

AWS Glue

To use the AWS Glue Catalog as the Metastore for Delta Lake tables, create a cluster
with following steps. For information on specifying the Delta Lake classification using
AWS Command Line Interface, see [Supply a configuration using the AWS Command Line Interface when you create a cluster](emr-configure-apps-create-cluster.md#emr-configure-apps-create-cluster-cli "emr-configure-apps-create-cluster.md#emr-configure-apps-create-cluster-cli")
or [Supply a configuration using the Java SDK when you create a
cluster](emr-configure-apps-create-cluster.md#emr-configure-apps-create-cluster-sdk "emr-configure-apps-create-cluster.md#emr-configure-apps-create-cluster-sdk").

###### Create a Delta Lake cluster

1. Create a file, `configurations.json`, with the
   following content:

```

[{"Classification":"delta-defaults",
"Properties":{"delta.enabled":"true"}},
{"Classification":"spark-hive-site",
"Properties":{"hive.metastore.client.factory.class":"com.amazonaws.glue.catalog.metastore.AWSGlueDataCatalogHiveClientFactory"}}]
```

2. Create a cluster with the following configuration, replacing the
   `example Amazon S3 bucket path` and the
   `subnet ID` with your own.

```

aws emr create-cluster
    --release-label  emr-6.9.0
    --applications Name=Spark
    --configurations file://delta_configurations.json
    --region us-east-1
    --name My_Spark_Delta_Cluster
    --log-uri  `s3://amzn-s3-demo-bucket/`
    --instance-type m5.xlarge
    --instance-count 2
    --service-role EMR_DefaultRole_V2
    --ec2-attributes  InstanceProfile=EMR_EC2_DefaultRole,SubnetId=`subnet-1234567890abcdef0`
```
