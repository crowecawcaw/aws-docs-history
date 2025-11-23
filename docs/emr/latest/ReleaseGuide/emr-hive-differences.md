# Differences and considerations for Hive on Amazon EMR

## Differences between Apache Hive on Amazon EMR and Apache Hive

This section describes the differences between Hive on Amazon EMR and the default
versions of Hive available at [http://svn.apache.org/viewvc/hive/branches/](http://svn.apache.org/viewvc/hive/branches/ "http://svn.apache.org/viewvc/hive/branches/").

### Hive authorization

Amazon EMR supports [Hive authorization](https://cwiki.apache.org/confluence/display/Hive/LanguageManual+Authorization "https://cwiki.apache.org/confluence/display/Hive/LanguageManual+Authorization") for HDFS but not for EMRFS and Amazon S3. Amazon EMR clusters run
with authorization disabled by default.

### Hive file merge behavior with Amazon S3

Apache Hive merges small files at the end of a map-only job if
`hive.merge.mapfiles` is true and the merge is triggered only if the average
output size of the job is less than the `hive.merge.smallfiles.avgsize`
setting. Amazon EMR Hive has exactly the same behavior if the final output path is in HDFS. If the output path is in Amazon S3, the `hive.merge.smallfiles.avgsize` parameter is ignored. In that situation, the merge task is always triggered if
`hive.merge.mapfiles` is set to `true`.

### ACID transactions and Amazon S3

Amazon EMR 6.1.0 and later supports Hive ACID (Atomicity, Consistency, Isolation, Durability) transactions so it complies with the ACID properties of a database. With this feature, you can run INSERT, UPDATE, DELETE, and MERGE operations in Hive managed tables with data in Amazon Simple Storage Service (Amazon S3).

### Hive Live Long and Process (LLAP)

[LLAP
functionality](https://cwiki.apache.org/confluence/display/Hive/LLAP "https://cwiki.apache.org/confluence/display/Hive/LLAP") added in version 2.0 of default Apache Hive is not
supported in Hive 2.1.0 on Amazon EMR release 5.0.

Amazon EMR version 6.0.0 and later supports the Live Long and Process (LLAP) functionality for
Hive. For more information, see [Using
Hive LLAP](emr-hive-llap.md "emr-hive-llap.md").

## Differences in Hive between Amazon EMR release version 4.x and 5.x

This section covers differences to consider before you migrate a Hive implementation from Hive version 1.0.0 on Amazon EMR release 4.x to Hive 2.x on Amazon EMR release 5.x.

### Operational differences and considerations

- **Support added for [ACID (atomicity, consistency, isolation, and durability) transactions](https://cwiki.apache.org/confluence/display/Hive/Hive+Transactions "https://cwiki.apache.org/confluence/display/Hive/Hive+Transactions"):** This difference between Hive 1.0.0 on
  Amazon EMR 4.x and default Apache Hive has been eliminated.
- **Direct writes to Amazon S3 eliminated:** This difference between
  Hive 1.0.0 on Amazon EMR and the default Apache Hive has been eliminated. Hive 2.1.0 on Amazon EMR release 5.x
  now creates, reads from, and writes to temporary files stored in Amazon S3. As a result, to
  read from and write to the same table you no longer have to create a
  temporary table in the cluster's local HDFS file system as a
  workaround. If you use versioned buckets, be sure to manage these temporary files as described below.
- **Manage temp files when using Amazon S3 versioned buckets:** When you run
  Hive queries where the destination of generated data is Amazon S3, many temporary
  files and directories are created. This is new behavior as described earlier. If you use versioned S3 buckets, these
  temp files clutter Amazon S3 and incur cost if they're not deleted. Adjust your
  lifecycle rules so that data with a `/_tmp` prefix is deleted after
  a short period, such as five days. See [Specifying a lifecycle configuration](../../../AmazonS3/latest/userguide/how-to-set-lifecycle-configuration-intro.md "../../../AmazonS3/latest/userguide/how-to-set-lifecycle-configuration-intro.md") for more information.
- **Log4j updated to log4j 2:** If you use log4j, you may need to
  change your logging configuration because of this upgrade. See [Apache log4j 2](http://logging.apache.org/log4j/2.x/ "http://logging.apache.org/log4j/2.x/") for
  details.

### Performance differences and considerations

- **Performance differences with Tez:** With Amazon EMR release 5.x , Tez is the default execution engine for Hive instead of MapReduce. Tez provides improved performance for most workflows.
- **Tables with many partitions:** Queries that generate a large number of dynamic partitions may fail, and queries that select from tables with many partitions may take longer than expected to execute. For example, a select from 100,000 partitions may take 10 minutes or more.

## Additional features of Hive on Amazon EMR

Amazon EMR extends Hive with new features that support Hive integration with other AWS services,
such as the ability to read from and write to Amazon Simple Storage Service (Amazon S3) and DynamoDB.

### Variables in Hive

You can include variables in your scripts by using the dollar sign and curly braces.

```

add jar ${LIB}/jsonserde.jar

```

You pass the values of these variables to Hive on the command line using the
`-d` parameter, as in the following example:

```

-d LIB=s3://elasticmapreduce/samples/hive-ads/lib

```

You can also pass the values into steps that execute Hive scripts.

###### To pass variable values into Hive steps using the console

1. Open the Amazon EMR console at
   [https://console.aws.amazon.com/emr](https://console.aws.amazon.com/emr/ "https://console.aws.amazon.com/emr/").
2. Choose **Create cluster**.
3. In the **Steps** section, for **Add Step**,
   choose **Hive Program** from the list and **Configure
   and add**.
4. In the **Add Step** dialog, specify the parameters using the
   following table as a guide, and then choose **Add**.

| Field                | Action                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Script S3 location\* | Specify the URI where your script resides in Amazon S3. The value<br>must be in the form<br>`BucketName`/`path`/`ScriptName`.<br>For example:<br>`s3://elasticmapreduce/samples/hive-ads/libs/response-time-stats.q`.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Input S3 location    | Optionally, specify the URI where your input files reside in<br>Amazon S3. The value must be in the form<br>`BucketName`/`path`/.<br>If specified, this will be passed to the Hive script as a<br>parameter named `INPUT`. For example:<br>`s3://elasticmapreduce/samples/hive-ads/tables/`.                                                                                                                                                                                                                                                                                                                                                                     |
| Output S3 location   | Optionally, specify the URI where you want the output stored<br>in Amazon S3. The value must be in the form<br>`BucketName`/`path`.<br>If specified, this will be passed to the Hive script as a<br>parameter named `OUTPUT`. For example:<br>`s3://amzn-s3-demo-bucket/hive-ads/output/`.                                                                                                                                                                                                                                                                                                                                                                       |
| Arguments            | Optionally, enter a list of arguments (space-separated<br>strings) to pass to Hive. If you defined a path variable in your<br>Hive script named ${SAMPLE}, for<br>example:<br>```<br>CREATE EXTERNAL TABLE logs (requestBeginTime STRING, requestEndTime STRING, hostname STRING) PARTITIONED BY (dt STRING) \<br>ROW FORMAT serde 'com.amazon.elasticmapreduce.JsonSerde'<br>WITH SERDEPROPERTIES ( 'paths'='requestBeginTime, requestEndTime, hostname' ) LOCATION '${SAMPLE}/tables/impressions';<br>```<br>To<br>pass a value for the variable, type the following in the<br>**Arguments**<br>window:`-d<br>SAMPLE=s3://elasticmapreduce/samples/hive-ads/`. |
| Action on Failure    | This determines what the cluster does in response to any<br>errors. The possible values for this setting are:<br>• **Terminate cluster**: If the<br>step fails, terminate the cluster. If the cluster<br>has termination protection enabled AND keep alive<br>enabled, it will not terminate.<br>• **Cancel and wait**: If the<br>step fails, cancel the remaining steps. If the<br>cluster has keep alive enabled, the cluster will<br>not terminate.<br>• **Continue**: If the step<br>fails, continue to the next step.                                                                                                                                       |

5. Select values as necessary and choose **Create
   cluster**.

###### To pass variable values into Hive steps using the AWS CLI

To pass variable values into Hive steps using the AWS CLI, use the
`--steps` parameter and include an arguments list.

- ###### Note

Linux line continuation characters (\) are included for readability. They can be removed or used in Linux commands. For Windows, remove them or replace with a caret (^).

```
aws emr create-cluster --name "`Test cluster`" --release-label `emr-7.12.0` \
--applications Name=`Hive` Name=`Pig` --use-default-roles --ec2-attributes KeyName=`myKey` --instance-type `m5.xlarge` --instance-count `3` \
--steps Type=`Hive`,Name="`Hive Program`",ActionOnFailure=`CONTINUE`,Args=[-f,`s3://elasticmapreduce/samples/hive-ads/libs/response-time-stats.q`,-d,INPUT=`s3://elasticmapreduce/samples/hive-ads/tables`,-d,OUTPUT=`s3://amzn-s3-demo-bucket/hive-ads/output/`,-d,`SAMPLE`=`s3://elasticmapreduce/samples/hive-ads/`]
```

For more information on using Amazon EMR commands in the AWS CLI, see [https://docs.aws.amazon.com/cli/latest/reference/emr](../../../cli/latest/reference/emr.md "../../../cli/latest/reference/emr.md").

###### To pass variable values into Hive steps using the Java SDK

- The following example demonstrates how to pass variables into steps using the SDK. For more information, see
  [Class StepFactory](../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/elasticmapreduce/util/StepFactory.md "../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/elasticmapreduce/util/StepFactory.md") in the _AWS SDK for Java API Reference_.

```
StepFactory stepFactory = new StepFactory();

   StepConfig runHive = new StepConfig()
     .withName("Run Hive Script")
     .withActionOnFailure("TERMINATE_JOB_FLOW")
     .withHadoopJarStep(stepFactory.newRunHiveScriptStep(“s3://amzn-s3-demo-bucket/script.q”,
      Lists.newArrayList(“-d”,”LIB= s3://elasticmapreduce/samples/hive-ads/lib”));

```

### Amazon EMR Hive queries to accommodate partial DynamoDB

schemas

Amazon EMR Hive provides maximum flexibility when querying DynamoDB tables by allowing you to
specify a subset of columns on which you can filter data, rather than requiring your
query to include all columns. This partial schema query technique is effective when you
have a sparse database schema and want to filter records based on a few columns, such as
filtering on time stamps.

The following example shows how to use a Hive query to:

- Create a DynamoDB table.
- Select a subset of items (rows) in DynamoDB and further narrow the data to
  certain columns.
- Copy the resulting data to Amazon S3.

```
DROP TABLE dynamodb;
DROP TABLE s3;

CREATE EXTERNAL TABLE dynamodb(hashKey STRING, recordTimeStamp BIGINT, fullColumn map<String, String>)
    STORED BY 'org.apache.hadoop.hive.dynamodb.DynamoDBStorageHandler'
    TBLPROPERTIES (
     "dynamodb.table.name" = "myTable",
     "dynamodb.throughput.read.percent" = ".1000",
     "dynamodb.column.mapping" = "hashKey:HashKey,recordTimeStamp:RangeKey");

CREATE EXTERNAL TABLE s3(map<String, String>)
     ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
     LOCATION 's3://bucketname/path/subpath/';

INSERT OVERWRITE TABLE s3 SELECT item fullColumn FROM dynamodb WHERE recordTimeStamp < "2012-01-01";
```

The following table shows the query syntax for selecting any combination of items from
DynamoDB.

| Query example                                                                                                       | Result description                                                                                             |
| ------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| SELECT \<br>• FROM `table_name`;                                                                                    | Selects all items (rows) from a given table and includes data from<br>all columns available for those items.   |
| SELECT \<br>• FROM `table_name` WHERE<br>`field_name`<br>=`value`;                                                  | Selects some items (rows) from a given table and includes data from<br>all columns available for those items.  |
| SELECT `column1_name`,<br>`column2_name`,<br>`column3_name` FROM<br>`table_name`;                                   | Selects all items (rows) from a given table and includes data from<br>some columns available for those items.  |
| SELECT `column1_name`,<br>`column2_name`,<br>`column3_name` FROM<br>`table_name` WHERE<br>`field_name`<br>=`value`; | Selects some items (rows) from a given table and includes data from<br>some columns available for those items. |

### Copy data between DynamoDB tables in different

AWS Regions

Amazon EMR Hive provides a `dynamodb.region` property you can set per DynamoDB
table. When `dynamodb.region` is set differently on two tables, any data you
copy between the tables automatically occurs between the specified regions.

The following example shows you how to create a DynamoDB table with a Hive script that
sets the `dynamodb.region` property:

###### Note

Per-table region properties override the global Hive properties.

```
CREATE EXTERNAL TABLE dynamodb(hashKey STRING, recordTimeStamp BIGINT, map<String, String> fullColumn)
    STORED BY 'org.apache.hadoop.hive.dynamodb.DynamoDBStorageHandler'
    TBLPROPERTIES (
     "dynamodb.table.name" = "myTable",
     "dynamodb.region" = "eu-west-1",
     "dynamodb.throughput.read.percent" = ".1000",
     "dynamodb.column.mapping" = "hashKey:HashKey,recordTimeStamp:RangeKey");
```

### Set DynamoDB throughput values per table

Amazon EMR Hive enables you to set the DynamoDB readThroughputPercent and
writeThroughputPercent settings on a per table basis in the table definition. The
following Amazon EMR Hive script shows how to set the throughput values. For more information
about DynamoDB throughput values, see [Specifying read and write requirements for tables](../../../amazondynamodb/latest/developerguide/WorkingWithDDTables.md#ProvisionedThroughput "../../../amazondynamodb/latest/developerguide/WorkingWithDDTables.md#ProvisionedThroughput").

```
CREATE EXTERNAL TABLE dynamodb(hashKey STRING, recordTimeStamp BIGINT, map<String, String> fullColumn)
    STORED BY 'org.apache.hadoop.hive.dynamodb.DynamoDBStorageHandler'
    TBLPROPERTIES (
     "dynamodb.table.name" = "myTable",
     "dynamodb.throughput.read.percent" = ".4",
     "dynamodb.throughput.write.percent" = "1.0",
     "dynamodb.column.mapping" = "hashKey:HashKey,recordTimeStamp:RangeKey");
```
