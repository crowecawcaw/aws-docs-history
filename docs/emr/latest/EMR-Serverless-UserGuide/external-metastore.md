# Using an external Hive metastore

You can configure your EMR Serverless Spark and Hive jobs to connect to an external
Hive metastore, such as Amazon Aurora or Amazon RDS for MySQL. This section describes how to set up an
Amazon RDS Hive metastore, configure your VPC, and configure your EMR Serverless jobs to use an
external metastore.

## Create an external Hive metastore

1. Create an Amazon Virtual Private Cloud (Amazon VPC) with private subnets by following the instructions in
   [Create a VPC](../../../vpc/latest/userguide/working-with-vpcs.md#Create-VPC "../../../vpc/latest/userguide/working-with-vpcs.md#Create-VPC").
2. Create your EMR Serverless application with your new Amazon VPC and private subnets.
   When you configure your EMR Serverless application with a VPC, it first provisions an
   elastic network interface for each subnet that you specify. It then attaches your
   specified security group to that network interface. This gives your application access
   control. For more details about how to set up your VPC, refer to [Configuring VPC access for EMR Serverless applications to connect to data](vpc-access.md "vpc-access.md").
3. Create a MySQL or Aurora PostgreSQL database in a private subnet in your Amazon VPC. For
   information about how to create an Amazon RDS database, refer to [Creating an Amazon RDS DB
   instance](../../../AmazonRDS/latest/UserGuide/USER_CreateDBInstance.md "../../../AmazonRDS/latest/UserGuide/USER_CreateDBInstance.md").
4. Modify the security group of your MySQL or Aurora database to allow JDBC
   connections from your EMR Serverless security group by following the steps in [Modifying an
   Amazon RDS DB instance](../../../AmazonRDS/latest/UserGuide/Overview.DBInstance.md "../../../AmazonRDS/latest/UserGuide/Overview.DBInstance.md"). Add a rule for inbound traffic to the RDS security group
   from one of your EMR Serverless security groups.

| Type    | Protocol | Port range | Source                          |
| ------- | -------- | ---------- | ------------------------------- |
| All TCP | TCP      | 3306       | `emr-serverless-security-group` |

## Configure Spark options

**Using JDBC**

To configure your EMR Serverless Spark application to connect to a Hive metastore
based on an Amazon RDS for MySQL or Amazon Aurora MySQL instance, use a JDBC connection. Pass the
`mariadb-connector-java.jar` with `--jars` in the
`spark-submit` parameters of your job run.

```
aws emr-serverless start-job-run \
  --application-id "`application-id`" \
  --execution-role-arn "`job-role-arn`" \
  --job-driver '{
        "sparkSubmit": {
            "entryPoint": "s3://`amzn-s3-demo-bucket`/scripts/spark-jdbc.py",
            "sparkSubmitParameters": "--jars s3://`amzn-s3-demo-bucket`/mariadb-connector-java.jar
            --conf spark.hadoop.javax.jdo.option.ConnectionDriverName=org.mariadb.jdbc.Driver
            --conf spark.hadoop.javax.jdo.option.ConnectionUserName=<connection-user-name>
            --conf spark.hadoop.javax.jdo.option.ConnectionPassword=<connection-password>
            --conf spark.hadoop.javax.jdo.option.ConnectionURL=<JDBC-Connection-string>
            --conf spark.driver.cores=2
            --conf spark.executor.memory=10G
            --conf spark.driver.memory=6G
            --conf spark.executor.cores=4"
        }
    }' \
    --configuration-overrides '{
        "monitoringConfiguration": {
        "s3MonitoringConfiguration": {
            "logUri": "s3://`amzn-s3-demo-bucket`/spark/logs/"
        }
    }
}'
```

The following code example is a Spark entrypoint script that interacts with a Hive
metastore on Amazon RDS.

```
from os.path import expanduser, join, abspath
from pyspark.sql import SparkSession
from pyspark.sql import Row
# warehouse_location points to the default location for managed databases and tables
warehouse_location = abspath('spark-warehouse')
spark = SparkSession \
    .builder \
    .config("spark.sql.warehouse.dir", warehouse_location) \
    .enableHiveSupport() \
    .getOrCreate()
spark.sql("SHOW DATABASES").show()
spark.sql("CREATE EXTERNAL TABLE `sampledb`.`sparknyctaxi`(`dispatching_base_num` string, `pickup_datetime` string, `dropoff_datetime` string, `pulocationid` bigint, `dolocationid` bigint, `sr_flag` bigint) STORED AS PARQUET LOCATION 's3://<s3 prefix>/nyctaxi_parquet/'")
spark.sql("SELECT count(*) FROM sampledb.sparknyctaxi").show()
spark.stop()
```

**Using the thrift service**

You can configure your EMR Serverless Hive application to connect to a Hive metastore
based on an Amazon RDS for MySQL or Amazon Aurora MySQL instance. To do this, run a thrift server on
the primary node of an existing Amazon EMR cluster. This option is ideal if you already have an
Amazon EMR cluster with a thrift server that you want to use to simplify your EMR Serverless
job configurations.

```
aws emr-serverless start-job-run \
  --application-id "`application-id`" \
  --execution-role-arn "`job-role-arn`" \
  --job-driver '{
        "sparkSubmit": {
            "entryPoint": "s3://`amzn-s3-demo-bucket`/thriftscript.py",
            "sparkSubmitParameters": "--jars s3://`amzn-s3-demo-bucket`/mariadb-connector-java.jar
            --conf spark.driver.cores=2
            --conf spark.executor.memory=10G
            --conf spark.driver.memory=6G
            --conf spark.executor.cores=4"
        }
    }' \
    --configuration-overrides '{
        "monitoringConfiguration": {
        "s3MonitoringConfiguration": {
            "logUri": "s3://`amzn-s3-demo-bucket`/spark/logs/"
        }
    }
}'
```

The following code example is an entrypoint script (`thriftscript.py`) that
uses thrift protocol to connect to a Hive metastore. Note that the
`hive.metastore.uris` property needs to be set to read from an external Hive
metastore.

```
from os.path import expanduser, join, abspath
from pyspark.sql import SparkSession
from pyspark.sql import Row
# warehouse_location points to the default location for managed databases and tables
warehouse_location = abspath('spark-warehouse')
spark = SparkSession \
    .builder \
    .config("spark.sql.warehouse.dir", warehouse_location) \
    .config("hive.metastore.uris","thrift://`thrift-server-host`:`thift-server-port`") \
    .enableHiveSupport() \
    .getOrCreate()
spark.sql("SHOW DATABASES").show()
spark.sql("CREATE EXTERNAL TABLE sampledb.`sparknyctaxi`( `dispatching_base_num` string, `pickup_datetime` string, `dropoff_datetime` string, `pulocationid` bigint, `dolocationid` bigint, `sr_flag` bigint) STORED AS PARQUET LOCATION 's3://<s3 prefix>/nyctaxi_parquet/'")
spark.sql("SELECT * FROM sampledb.sparknyctaxi").show()
spark.stop()
```

## Configure Hive options

**Using JDBC**

If you want to specify an external Hive database location on either an Amazon RDS MySQL or
Amazon Aurora instance, you can override the default metastore configuration.

###### Note

In Hive, you can perform multiple writes to metastore tables at the same time. If
you share metastore information between two jobs, make sure that you don't write to the
same metastore table simultaneously unless you write to different partitions of the same
metastore table.

Set the following configurations in the `hive-site` classification to
activate the external Hive metastore.

```
{
    "classification": "hive-site",
    "properties": {
        "hive.metastore.client.factory.class": "org.apache.hadoop.hive.ql.metadata.SessionHiveMetaStoreClientFactory",
        "javax.jdo.option.ConnectionDriverName": "org.mariadb.jdbc.Driver",
        "javax.jdo.option.ConnectionURL": "jdbc:mysql://`db-host`:`db-port`/`db-name`",
        "javax.jdo.option.ConnectionUserName": "`username`",
        "javax.jdo.option.ConnectionPassword": "`password`"
    }
}
```

**Using a thrift server**

You can configure your EMR Serverless Hive application to connect to a Hive metastore
based on an Amazon RDS for MySQL or Amazon Aurora MySQLinstance. To do this, run a thrift server on
the main node of an existing Amazon EMR cluster. This option is ideal if you already have an
Amazon EMR cluster that runs a thrift server and you want to use your EMR Serverless job
configurations.

Set the following configurations in the `hive-site` classification so that
EMR Serverless can access the remote thrift metastore. Note that you must set the
`hive.metastore.uris` property to read from an external Hive metastore.

```
{
    "classification": "hive-site",
    "properties": {
        "hive.metastore.client.factory.class": "org.apache.hadoop.hive.ql.metadata.SessionHiveMetaStoreClientFactory",
        "hive.metastore.uris": "thrift://`thrift-server-host`:`thirft-server-port`"
    }
}
```
