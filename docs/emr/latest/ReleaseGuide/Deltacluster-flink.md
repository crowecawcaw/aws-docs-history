# Use a Delta Lake cluster with Flink

With Amazon EMR release 6.11 and higher, you can use Delta Lake with your Flink cluster.
The following examples use the AWS CLI to work with Delta Lake on an Amazon EMR Flink
cluster.

###### Note

Amazon EMR supports the Flink DataStream API when you use Delta Lake with a Flink
cluster.

## Create a Delta Lake

cluster

1. Create a file, `delta_configurations.json`, with the
   following content:

```
[{"Classification":"delta-defaults",
    "Properties":{"delta.enabled":"true"}}]
```

2. Create a cluster with the following configuration. Replace the
   `example Amazon S3 bucket path` and the `subnet ID`
   with your own.

```
aws emr create-cluster
--release-label emr-6.11.0
--applications Name=Flink
--configurations file://delta_configurations.json
--region us-east-1  --name My_Spark_Delta_Cluster
--log-uri  s3://amzn-s3-demo-bucket/
--instance-type m5.xlarge
--instance-count 3
--service-role EMR_DefaultRole_V2
--ec2-attributes  InstanceProfile=EMR_EC2_DefaultRole,SubnetId=subnet-1234567890abcdef0
```

## Initialize a Flink yarn

session

To initialize a Flink yarn session, run the following command:

```
flink-yarn-session -d
```

## Build a Flink job with

Delta Lake

The following examples show how to use sbt or Maven to build your Flink job
with Delta Lake.

sbt
[sbt](https://www.scala-sbt.org/1.x/docs/index.html "https://www.scala-sbt.org/1.x/docs/index.html") is a build tool for Scala that you can use with
little to no configuration when you have small projects.

```
libraryDependencies ++= Seq(
  "io.delta" %% "delta-flink" % `deltaConnectorsVersion` % "provided",
  "io.delta" %% "delta-standalone" % `deltaConnectorsVersion` % "provided",
  "org.apache.flink" %% "flink-clients" % `flinkVersion` % "provided",
  "org.apache.flink" %% "flink-parquet" % `flinkVersion` % "provided",
  "org.apache.hadoop" % "hadoop-client" % `hadoopVersion` % "provided",
  "org.apache.flink" % "flink-table-common" % `flinkVersion` % "provided",
  "org.apache.flink" %% "flink-table-runtime" % `flinkVersion` % "provided")
```

Maven
[Maven](https://maven.apache.org "https://maven.apache.org") is an
open-source build automation tool from the Apache Software
Foundation. With Maven, you can build, publish, and deploy a Flink
job with Delta Lake on Amazon EMR.

```
<project>
<properties>
    <scala.main.version>2.12</scala.main.version>
    <delta-connectors-version>0.6.0</delta-connectors-version>
    <flink-version>1.16.1</flink-version>
    <hadoop-version>3.1.0</hadoop-version>
</properties>

<dependencies>
    <dependency>
        <groupId>io.delta</groupId>
        <artifactId>delta-flink</artifactId>
        <version>$`delta-connectors-version`</version>
        <scope>provided</scope>
    </dependency>
    <dependency>
        <groupId>io.delta</groupId>
        <artifactId>delta-standalone_$`scala-main-version`</artifactId>
        <version>$`delta-connectors-version`</version>
        <scope>provided</scope>
    </dependency>
    <dependency>
        <groupId>org.apache.flink</groupId>
        <artifactId>flink-clients</artifactId>
        <version>$`flink-version`</version>
        <scope>provided</scope>
    </dependency>
    <dependency>
        <groupId>org.apache.flink</groupId>
        <artifactId>flink-parquet</artifactId>
        <version>$`flink-version`</version>
        <scope>provided</scope>
    </dependency>
    <dependency>
        <groupId>org.apache.hadoop</groupId>
        <artifactId>hadoop-client</artifactId>
        <version>$`hadoop-version`</version>
        <scope>provided</scope>
    </dependency>
    <dependency>
        <groupId>org.apache.flink</groupId>
        <artifactId>flink-table-common</artifactId>
        <version>$`flink-version`</version>
        <scope>provided</scope>
    </dependency>
    <dependency>
        <groupId>org.apache.flink</groupId>
        <artifactId>flink-table-runtime</artifactId>
        <version>$`flink-version`</version>
        <scope>provided</scope>
    </dependency>
</dependencies>
```

## Write to

a Delta table with Flink Datastream API

Use the following example to create a DeltaSink to write to the table with a
`deltaTablePath:`

```
public static DataStream<RowData> createDeltaSink(
        DataStream<RowData> stream,
        String deltaTablePath,
        RowType rowType) {
    Configuration configuration = new Configuration();
    DeltaSink<RowData> deltaSink = DeltaSink
            .forRowData(
                    new org.apache.flink.core.fs.Path(deltaTablePath),
                    configuration,
                    rowType)
            .build();
    stream.sinkTo(deltaSink);
    return stream;
}
```

## Read from

a Delta table with Flink Datastream API

Use the following example to create a bounded DeltaSource to read from the
table with a `deltaTablePath:`

```
public static DataStream<RowData> createBoundedDeltaSourceAllColumns(
        StreamExecutionEnvironment env,
        String deltaTablePath) {
    Configuration configuration = new Configuration();
    DeltaSource<RowData> deltaSource = DeltaSource
            .forBoundedRowData(
                    new org.apache.flink.core.fs.Path(`deltaTablePath`),
                    configuration)
            .build();

    return env.fromSource(deltaSource, WatermarkStrategy.noWatermarks(), "delta-source");
}
```

## Sink creation with

multi-cluster support for Delta Lake standalone

Use the following example to create a DeltaSink to write to table with a
`deltaTablePath` and [multi cluster support](https://docs.delta.io/latest/delta-standalone.html#multi-cluster-setup "https://docs.delta.io/latest/delta-standalone.html#multi-cluster-setup"):

```
public DataStream<RowData> createDeltaSink(
        DataStream<RowData> stream,
        String deltaTablePath) {
    Configuration configuration = new Configuration();
    configuration.set("spark.delta.logStore.s3.impl", "io.delta.storage.S3DynamoDBLogStore");
    configuration.set("spark.io.delta.storage.S3DynamoDBLogStore.ddb.tableName", "`delta_log`");
    configuration.set("spark.io.delta.storage.S3DynamoDBLogStore.ddb.region", "`us-east-1`");

    DeltaSink<RowData> deltaSink = DeltaSink
        .forRowData(
            new Path(deltaTablePath),
            configuration,
            rowType)
        .build();
    stream.sinkTo(deltaSink);
    return stream;
}
```

## Run the Flink job

Use the following command to run your job:

```
flink run FlinkJob.jar
```
