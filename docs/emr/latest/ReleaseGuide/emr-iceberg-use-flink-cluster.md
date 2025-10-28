# Use an Iceberg cluster with Flink

Starting with Amazon EMR version 6.9.0, you can use Iceberg with a Flink cluster
without the setup steps required when using the open source Iceberg Flink
Integration.

## Creating an Iceberg

cluster

You can create a cluster with Iceberg installed using the AWS Management Console, the
AWS CLI, or the Amazon EMR API. In this tutorial, you use the AWS CLI to work with
Iceberg on an Amazon EMR cluster. To use the console to create a cluster with
Iceberg installed, follow the steps in [Build an Apache Iceberg data lake using Amazon Athena, Amazon EMR, and
AWS Glue](https://aws.amazon.com/blogs/big-data/build-an-apache-iceberg-data-lake-using-amazon-athena-amazon-emr-and-aws-glue/ "https://aws.amazon.com/blogs/big-data/build-an-apache-iceberg-data-lake-using-amazon-athena-amazon-emr-and-aws-glue/").

To use Iceberg on Amazon EMR with the AWS CLI, first create a cluster with the
following steps. For information on specifying the Iceberg classification
using the AWS CLI, see [Supply a configuration using
the AWS CLI when you create a cluster](emr-configure-apps-create-cluster.md#emr-configure-apps-create-cluster-cli "emr-configure-apps-create-cluster.md#emr-configure-apps-create-cluster-cli") or [Supply a configuration using
the Java SDK when you create a cluster](emr-configure-apps-create-cluster.md#emr-configure-apps-create-cluster-sdk "emr-configure-apps-create-cluster.md#emr-configure-apps-create-cluster-sdk"). Create a file
called `configurations.json` with the following content:

```
[{
"Classification":"iceberg-defaults",
    "Properties":{"iceberg.enabled":"true"}
}]
```

Next, create a cluster with the following configuration, replacing the example
Amazon S3 bucket path and subnet ID with your own values:

```
aws emr create-cluster --release-label emr-6.9.0 \
--applications Name=Flink \
--configurations file://iceberg_configurations.json \
--region us-east-1 \
--name My_flink_Iceberg_Cluster \
--log-uri s3://amzn-s3-demo-bucket/ \
--instance-type m5.xlarge \
--instance-count 2 \
--service-role EMR_DefaultRole \
--ec2-attributes InstanceProfile=EMR_EC2_DefaultRole,SubnetId=subnet-1234567890abcdef
```

Alternatively, you can create an Amazon EMR 6.9.0 cluster with a Flink application
in it and use the file
`/usr/share/aws/iceberg/lib/iceberg-flink-runtime.jar` as a JAR
dependency in a Flink job.

## Using the Flink SQL Client

The SQL Client script is located under `/usr/lib/flink/bin`. You
can run the script with the following command:

```
flink-yarn-session -d # starting the Flink YARN Session in detached mode
./sql-client.sh
```

This launches a Flink SQL Shell.

## Flink examples

### Create an Iceberg table

**Flink SQL**

```
CREATE CATALOG glue_catalog WITH (
   'type'='iceberg',
   'warehouse'='<WAREHOUSE>',
   'catalog-impl'='org.apache.iceberg.aws.glue.GlueCatalog',
    'io-impl'='org.apache.iceberg.aws.s3.S3FileIO'
 );

USE CATALOG  glue_catalog;

CREATE DATABASE IF NOT EXISTS <DB>;

USE <DB>;

CREATE TABLE IF NOT EXISTS `glue_catalog`.`<DB>`.`sample` (id int, data string);
```

**Table API**

```
EnvironmentSettings settings =
                EnvironmentSettings.newInstance().inBatchMode().build();

TableEnvironment tEnv = TableEnvironment.create(settings);

String warehouse = "<WAREHOUSE>";
String db = "<DB>";

tEnv.executeSql(
                "CREATE CATALOG glue_catalog WITH (\n"
                        + "   'type'='iceberg',\n"
                        + "   'warehouse'='"
                        + warehouse
                        + "',\n"
                        + "   'catalog-impl'='org.apache.iceberg.aws.glue.GlueCatalog',\n"
                        + "   'io-impl'='org.apache.iceberg.aws.s3.S3FileIO'\n"
                        + " );");

tEnv.executeSql("USE CATALOG  glue_catalog;");
tEnv.executeSql("CREATE DATABASE IF NOT EXISTS " + db + ";");
tEnv.executeSql("USE " + db + ";");
tEnv.executeSql(
        "CREATE TABLE `glue_catalog`.`" + db + "`.`sample` (id bigint, data string);");
```

### Write to an Iceberg table

**Flink SQL**

```
INSERT INTO `glue_catalog`.`<DB>`.`sample` values (1, 'a'),(2,'b'),(3,'c');
```

**Table API**

```
tEnv.executeSql(
        "INSERT INTO `glue_catalog`.`"
                + db
                + "`.`sample` values (1, 'a'),(2,'b'),(3,'c');");
```

**Datastream API**

```
final StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();

final StreamTableEnvironment tableEnv = StreamTableEnvironment.create(env);

String db = "<DB Name>";

String warehouse = "<Warehouse Path>";

GenericRowData rowData1 = new GenericRowData(2);
rowData1.setField(0, 1L);
rowData1.setField(1, StringData.fromString("a"));

DataStream<RowData> input = env.fromElements(rowData1);

Map<String, String> props = new HashMap<();
props.put("type", "iceberg");
props.put("warehouse", warehouse);
props.put("io-impl", "org.apache.iceberg.aws.s3.S3FileIO");

CatalogLoader glueCatlogLoader =
        CatalogLoader.custom(
                "glue",
                props,
                new Configuration(),
                "org.apache.iceberg.aws.glue.GlueCatalog");

TableLoader tableLoader =
        TableLoader.fromCatalog(glueCatlogLoader, TableIdentifier.of(db, "sample"));

DataStreamSink<Void> dataStreamSink =
        FlinkSink.forRowData(input).tableLoader(tableLoader).append();

env.execute("Datastream Write");

```

### Read from an Iceberg

table

**Flink SQL**

```
SELECT * FROM `glue_catalog`.`<DB>`.`sample`;
```

**Table API**

```
Table result = tEnv.sqlQuery("select * from `glue_catalog`.`" + db + "`.`sample`;");
```

**Datastream API**

```
final StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();

final StreamTableEnvironment tableEnv = StreamTableEnvironment.create(env);

String db = "<DB Name>";

String warehouse = "<Warehouse Path>";

Map<String, String> props = new HashMap<>();
props.put("type", "iceberg");
props.put("warehouse", warehouse);
props.put("io-impl", "org.apache.iceberg.aws.s3.S3FileIO");

CatalogLoader glueCatlogLoader =
        CatalogLoader.custom(
                "glue",
                props,
                new Configuration(),
                "org.apache.iceberg.aws.glue.GlueCatalog");

TableLoader tableLoader =
        TableLoader.fromCatalog(glueCatlogLoader, TableIdentifier.of(db, "sample"));

DataStream<RowData> batch =
                FlinkSource.forRowData().env(env).tableLoader(tableLoader).streaming(false).build();

batch.print().name("print-sink");
```

## Using the Hive catalog

Make sure the Flink and Hive dependencies are resolved as described in [Configure Flink with Hive Metastore and Glue
Catalog](flink-configure.md#flink-configure-hive "flink-configure.md#flink-configure-hive").

## Running a Flink Job

One way to submit a job to Flink is to use a per job Flink YARN session. This
can be launched with the following command:

```
sudo flink run -m yarn-cluster -p 4 -yjm 1024m -ytm 4096m $JAR_FILE_NAME
```

## Considerations for using Iceberg with

Flink

- When using AWS Glue as a catalog for Iceberg, make sure the database in which you
  are creating a table exists in AWS Glue. If you are using services such as AWS Lake Formation and
  you're unable to load the catalog, make sure you have proper access to the service
  to execute the command.
- Iceberg Glue integration does not work with the Redshift Managed Storage catalog.
