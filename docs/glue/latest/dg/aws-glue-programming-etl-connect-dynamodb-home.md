# DynamoDB connections

You can use AWS Glue for Spark to read from and write to tables in DynamoDB in AWS Glue. You connect to DynamoDB using
IAM permissions attached to your AWS Glue job. AWS Glue supports writing data into another AWS
account's DynamoDB table. For more information, see [Cross-account cross-Region access to DynamoDB tables](aws-glue-programming-etl-dynamo-db-cross-account.md "aws-glue-programming-etl-dynamo-db-cross-account.md").

In addition to the AWS Glue DynamoDB ETL connector, you can read from DynamoDB using the DynamoDB export
connector, that invokes a DynamoDB `ExportTableToPointInTime` request and stores it in an Amazon S3 location
you supply, in the format of [DynamoDB
JSON](../../../amazondynamodb/latest/developerguide/DataExport.md "../../../amazondynamodb/latest/developerguide/DataExport.md"). AWS Glue then creates a DynamicFrame object by reading the data from the Amazon S3 export
location.

The DynamoDB writer is available in AWS Glue version 1.0 or later versions. The
AWS Glue DynamoDB export connector is available in AWS Glue version
2.0 or later versions.

For more information about DynamoDB, consult [Amazon DynamoDB](../../../amazondynamodb/latest/developerguide.md "../../../amazondynamodb/latest/developerguide.md") documentation.

###### Note

The DynamoDB ETL reader does not support filters or pushdown predicates.

## Configuring DynamoDB connections

To connect to DynamoDB from AWS Glue, grant the IAM role associated with your AWS Glue job permission to interact
with DynamoDB. For more information about permissions necessary to read or write from DynamoDB, consult [Actions,
resources, and condition keys for DynamoDB](../../../service-authorization/latest/reference/list_amazondynamodb.md "../../../service-authorization/latest/reference/list_amazondynamodb.md") in the IAM documentation.

In the following situations, you may need additional configuration:

- When using the DynamoDB export connector, you will need to configure IAM so your job can request
  DynamoDB table exports. Additionally, you will need to identify an Amazon S3 bucket for the export and
  provide appropriate permissions in IAM for DynamoDB to write to it, and for your AWS Glue job to read
  from it. For more information, consult [Request a table export in
  DynamoDB](../../../amazondynamodb/latest/developerguide/S3DataExport_Requesting.md "../../../amazondynamodb/latest/developerguide/S3DataExport_Requesting.md").
- If your AWS Glue job has specific Amazon VPC connectivity requirements, use the `NETWORK` AWS Glue
  connection type to provide network options. Since access to DynamoDB is authorized by IAM, there is
  no need for a AWS Glue DynamoDB connection type.

## Reading from and writing to

DynamoDB

The following code examples show how to read from (via the ETL connector) and write to DynamoDB tables. They
demonstrate reading from one table and writing to another table.

Python

```
import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
glue_context= GlueContext(SparkContext.getOrCreate())
job = Job(glue_context)
job.init(args["JOB_NAME"], args)

dyf = glue_context.create_dynamic_frame.from_options(
    connection_type="dynamodb",
    connection_options={"dynamodb.input.tableName": `test_source`,
        "dynamodb.throughput.read.percent": "1.0",
        "dynamodb.splits": "100"
    }
)
print(dyf.getNumPartitions())

glue_context.write_dynamic_frame_from_options(
    frame=dyf,
    connection_type="dynamodb",
    connection_options={"dynamodb.output.tableName": `test_sink`,
        "dynamodb.throughput.write.percent": "1.0"
    }
)

job.commit()

```

Scala

```
import com.amazonaws.services.glue.GlueContext
import com.amazonaws.services.glue.util.GlueArgParser
import com.amazonaws.services.glue.util.Job
import com.amazonaws.services.glue.util.JsonOptions
import com.amazonaws.services.glue.DynamoDbDataSink
import org.apache.spark.SparkContext
import scala.collection.JavaConverters._


object GlueApp {

  def main(sysArgs: Array[String]): Unit = {
    val glueContext = new GlueContext(SparkContext.getOrCreate())
    val args = GlueArgParser.getResolvedOptions(sysArgs, Seq("JOB_NAME").toArray)
    Job.init(args("JOB_NAME"), glueContext, args.asJava)

    val dynamicFrame = glueContext.getSourceWithFormat(
      connectionType = "dynamodb",
      options = JsonOptions(Map(
        "dynamodb.input.tableName" -> `test_source`,
        "dynamodb.throughput.read.percent" -> "1.0",
        "dynamodb.splits" -> "100"
      ))
    ).getDynamicFrame()

    print(dynamicFrame.getNumPartitions())

    val dynamoDbSink: DynamoDbDataSink =  glueContext.getSinkWithFormat(
      connectionType = "dynamodb",
      options = JsonOptions(Map(
        "dynamodb.output.tableName" -> `test_sink`,
        "dynamodb.throughput.write.percent" -> "1.0"
      ))
    ).asInstanceOf[DynamoDbDataSink]

    dynamoDbSink.writeDynamicFrame(dynamicFrame)

    Job.commit()
  }

}
```

## Using the DynamoDB export connector

The export connector performs better than the ETL connector when the DynamoDB table size is larger than 80 GB. In
addition, given that the export request is conducted outside from the Spark processes in an AWS Glue
job, you can enable [auto scaling of
AWS Glue jobs](auto-scaling.md "auto-scaling.md") to save DPU usage during the export request. With the export connector, you also do not need
to configure the number of splits for Spark executor parallelism or DynamoDB throughput read percentage.

###### Note

DynamoDB has specific requirements to invoke the `ExportTableToPointInTime` requests. For
more information, see [Requesting a table export in DynamoDB](../../../amazondynamodb/latest/developerguide/DataExport.md "../../../amazondynamodb/latest/developerguide/DataExport.md"). For example, Point-in-Time-Restore (PITR) needs to be
enabled on the table to use this connector. The DynamoDB connector also supports AWS KMS encryption for
DynamoDB exports to Amazon S3. Supplying your security configuration in the AWS Glue job configuration enables
AWS KMS encryption for a DynamoDB export. The KMS key must be in the same Region as the Amazon S3
bucket.

Note that additional charges for DynamoDB export and Amazon S3 storage costs apply. Exported data in Amazon S3
persists after a job run finishes so you can reuse it without additional DynamoDB exports. A
requirement for using this connector is that point-in-time recovery (PITR) is enabled for the
table.

The DynamoDB ETL connector or export connector do not support filters or pushdown predicates to be
applied at the DynamoDB source.

The following code examples show how to read from (via the export connector) and print the number of
partitions.

Python

```
import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
glue_context= GlueContext(SparkContext.getOrCreate())
job = Job(glue_context)
job.init(args["JOB_NAME"], args)

dyf = glue_context.create_dynamic_frame.from_options(
    connection_type="dynamodb",
    connection_options={
        "dynamodb.export": "ddb",
        "dynamodb.tableArn": `test_source`,
        "dynamodb.s3.bucket": `bucket_name`,
        "dynamodb.s3.prefix": `bucket_prefix`,
        "dynamodb.s3.bucketOwner": `account_id_of_bucket`,
    }
)
print(dyf.getNumPartitions())

job.commit()
```

Scala

```
import com.amazonaws.services.glue.GlueContext
import com.amazonaws.services.glue.util.GlueArgParser
import com.amazonaws.services.glue.util.Job
import com.amazonaws.services.glue.util.JsonOptions
import com.amazonaws.services.glue.DynamoDbDataSink
import org.apache.spark.SparkContext
import scala.collection.JavaConverters._


object GlueApp {

  def main(sysArgs: Array[String]): Unit = {
    val glueContext = new GlueContext(SparkContext.getOrCreate())
    val args = GlueArgParser.getResolvedOptions(sysArgs, Seq("JOB_NAME").toArray)
    Job.init(args("JOB_NAME"), glueContext, args.asJava)

    val dynamicFrame = glueContext.getSourceWithFormat(
      connectionType = "dynamodb",
      options = JsonOptions(Map(
        "dynamodb.export" -> "ddb",
        "dynamodb.tableArn" -> `test_source`,
        "dynamodb.s3.bucket" -> `bucket_name`,
        "dynamodb.s3.prefix" -> `bucket_prefix`,
        "dynamodb.s3.bucketOwner" -> `account_id_of_bucket`,
      ))
    ).getDynamicFrame()

    print(dynamicFrame.getNumPartitions())

    Job.commit()
  }

}
```

These examples show how to do the read from (via the export connector) and print the number of partitions
from an AWS Glue Data Catalog table that has a `dynamodb` classification:

Python

```
import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
glue_context= GlueContext(SparkContext.getOrCreate())
job = Job(glue_context)
job.init(args["JOB_NAME"], args)

dynamicFrame = glue_context.create_dynamic_frame.from_catalog(
        database=`catalog_database`,
        table_name=`catalog_table_name`,
        additional_options={
            "dynamodb.export": "ddb",
            "dynamodb.s3.bucket": `s3_bucket`,
            "dynamodb.s3.prefix": `s3_bucket_prefix`
        }
    )
print(dynamicFrame.getNumPartitions())

job.commit()
```

Scala

```
import com.amazonaws.services.glue.GlueContext
import com.amazonaws.services.glue.util.GlueArgParser
import com.amazonaws.services.glue.util.Job
import com.amazonaws.services.glue.util.JsonOptions
import com.amazonaws.services.glue.DynamoDbDataSink
import org.apache.spark.SparkContext
import scala.collection.JavaConverters._


object GlueApp {

  def main(sysArgs: Array[String]): Unit = {
    val glueContext = new GlueContext(SparkContext.getOrCreate())
    val args = GlueArgParser.getResolvedOptions(sysArgs, Seq("JOB_NAME").toArray)
    Job.init(args("JOB_NAME"), glueContext, args.asJava)

    val dynamicFrame = glueContext.getCatalogSource(
        database = `catalog_database`,
        tableName = `catalog_table_name`,
        additionalOptions = JsonOptions(Map(
            "dynamodb.export" -> "ddb",
            "dynamodb.s3.bucket" -> `s3_bucket`,
            "dynamodb.s3.prefix" -> `s3_bucket_prefix`
        ))
    ).getDynamicFrame()
    print(dynamicFrame.getNumPartitions())
)
```

## Simplifying usage of DynamoDB export JSON

The DynamoDB exports with the AWS Glue DynamoDB export connector results in JSON files of
specific nested structures. For more information, see [Data objects](../../../amazondynamodb/latest/developerguide/S3DataExport.md "../../../amazondynamodb/latest/developerguide/S3DataExport.md"). AWS Glue supplies a DynamicFrame transformation, which can unnest
such structures into an easier-to-use form for downstream applications.

The transform can be invoked in one of two ways. You can set the connection option
`"dynamodb.simplifyDDBJson"` with the value `"true"` when calling a method to read
from DynamoDB. You can also call the transform as a method independently available in the AWS Glue library.

Consider the following schema generated by a DynamoDB export:

```
root
|-- Item: struct
|    |-- parentMap: struct
|    |    |-- M: struct
|    |    |    |-- childMap: struct
|    |    |    |    |-- M: struct
|    |    |    |    |    |-- appName: struct
|    |    |    |    |    |    |-- S: string
|    |    |    |    |    |-- packageName: struct
|    |    |    |    |    |    |-- S: string
|    |    |    |    |    |-- updatedAt: struct
|    |    |    |    |    |    |-- N: string
|    |-- strings: struct
|    |    |-- SS: array
|    |    |    |-- element: string
|    |-- numbers: struct
|    |    |-- NS: array
|    |    |    |-- element: string
|    |-- binaries: struct
|    |    |-- BS: array
|    |    |    |-- element: string
|    |-- isDDBJson: struct
|    |    |-- BOOL: boolean
|    |-- nullValue: struct
|    |    |-- NULL: boolean
```

The `simplifyDDBJson` transform will simplify this to:

```
root
|-- parentMap: struct
|    |-- childMap: struct
|    |    |-- appName: string
|    |    |-- packageName: string
|    |    |-- updatedAt: string
|-- strings: array
|    |-- element: string
|-- numbers: array
|    |-- element: string
|-- binaries: array
|    |-- element: string
|-- isDDBJson: boolean
|-- nullValue: null
```

###### Note

`simplifyDDBJson` is available in AWS Glue 3.0 and later versions. The
`unnestDDBJson` transform is also available to simplify DynamoDB export JSON. We encourage users
to transition to `simplifyDDBJson` from `unnestDDBJson`.

## Configuring paralleism in DynamoDB operations

To improve performance, you can tune certain parameters available for the DynamoDB connector. Your goal when
tuning paralleism parameters is to maximize the use of the provisioned AWS Glue workers. Then, if you need more
performance, we recommend you to scale out your job by increasing the number of DPUs.

You can alter the parallelism in a DynamoDB read operation using the `dynamodb.splits` parameter
when using the ETL connector. When reading with the export connector, you do not need to configure the
number of splits for Spark executor parallelism. You can alter the parallelism in a DynamoDB write operation
with `dynamodb.output.numParallelTasks`.

**Reading with the DynamoDB ETL connector**

We recommend you to calculate `dynamodb.splits` based on the maximum number of workers set in
your job configuration and the following `numSlots` calculation. If autoscaling, the actual
number of workers available may change under that cap. For more information about setting the maximum number
of workers, see **Number of workers** (`NumberOfWorkers`) in [Configuring job properties for Spark jobs in AWS Glue](add-job.md "add-job.md").

- `numExecutors = NumberOfWorkers - 1`

For context, one executor is reserved for the Spark driver; other executors are used to process
data.

- `numSlotsPerExecutor =`

AWS Glue 3.0 and later versions

    + `4` if `WorkerType` is
     `G.1X`
    + `8` if `WorkerType` is
     `G.2X`
    + `16` if `WorkerType` is
     `G.4X`
    + `32` if `WorkerType` is
     `G.8X`

AWS Glue 2.0 and legacy versions

    + `8` if `WorkerType` is
     `G.1X`
    + `16` if `WorkerType` is
     `G.2X`

- `numSlots = numSlotsPerExecutor * numExecutors`

We recommend you set `dynamodb.splits` to the number of slots available, `numSlots`.

**Writing to DynamoDB**

The `dynamodb.output.numParallelTasks` parameter is used to determine WCU per Spark task, using the following calculation:

`permittedWcuPerTask = ( TableWCU * dynamodb.throughput.write.percent ) /
 dynamodb.output.numParallelTasks`

The DynamoDB writer will function best if configuration accurately represents the number of Spark tasks
writing to DynamoDB. In some cases, you may need to override the default calculation to improve write
performance. If you do not specify this parameter, the permitted WCU per Spark task will be automatically
calculated by the following formula:

- - `numPartitions = dynamicframe.getNumPartitions()`
  - `numSlots` (as defined previously in this section)
  - `numParallelTasks = min(numPartitions, numSlots)`
- Example 1. DPU=10, WorkerType=Standard. Input DynamicFrame has 100 RDD
  partitions.
  - `numPartitions = 100`
  - `numExecutors = (10 - 1) * 2 - 1 = 17`
  - `numSlots = 4 * 17 = 68`
  - `numParallelTasks = min(100, 68) = 68`

- Example 2. DPU=10, WorkerType=Standard. Input DynamicFrame has 20 RDD
  partitions.
  - `numPartitions = 20`
  - `numExecutors = (10 - 1) * 2 - 1 = 17`
  - `numSlots = 4 * 17 = 68`
  - `numParallelTasks = min(20, 68) = 20`

###### Note

Jobs on legacy AWS Glue versions and those using Standard workers require different methods to calculate
the number of slots. If you need to performance tune these jobs, we recommend you transition to
supported AWS Glue versions.

## DynamoDB connection option reference

Designates a connection to Amazon DynamoDB.

Connection options differ for a source connection and a sink connection.

### "connectionType": "dynamodb" with the ETL connector as

source

Use the following connection options with `"connectionType": "dynamodb"` as a source, when
using the AWS Glue DynamoDB ETL connector:

- `"dynamodb.input.tableName"`: (Required) The DynamoDB table to read from.
- `"dynamodb.throughput.read.percent"`: (Optional) The percentage of read capacity
  units (RCU) to use. The default is set to "0.5". Acceptable values are from "0.1" to "1.5",
  inclusive.
  - `0.5` represents the default read rate, meaning that AWS Glue
    will attempt to consume half of the read capacity of the table. If you increase the
    value above `0.5`, AWS Glue increases the request rate;
    decreasing the value below `0.5` decreases the read request rate. (The actual
    read rate will vary, depending on factors such as whether there is a uniform key
    distribution in the DynamoDB table.)
  - When the DynamoDB table is in on-demand mode, AWS Glue handles the read
    capacity of the table as 40000. For exporting a large table, we recommend switching your
    DynamoDB table to on-demand mode.

- `"dynamodb.splits"`: (Optional) Defines how many splits we partition this DynamoDB
  table into while reading. The default is set to "1". Acceptable values are from "1" to
  "1,000,000", inclusive.

`1` represents there is no parallelism. We highly recommend that you specify a
larger value for better performance by using the below formula. For more information on
appropriately setting a value, see [Configuring paralleism in DynamoDB operations](#aws-glue-programming-etl-connect-dynamodb-parallelism "#aws-glue-programming-etl-connect-dynamodb-parallelism").

- `"dynamodb.sts.roleArn"`: (Optional) The IAM role ARN to be assumed for
  cross-account access. This parameter is available in AWS Glue 1.0 or later.
- `"dynamodb.sts.roleSessionName"`: (Optional) STS session name. The default is set
  to "glue-dynamodb-read-sts-session". This parameter is available in AWS Glue 1.0 or
  later.

### "connectionType": "dynamodb" with the

AWS Glue DynamoDB export connector as source

Use the following connection options with "connectionType": "dynamodb" as a source, when using the
AWS Glue DynamoDB export connector, which is available only for AWS Glue version
2.0 onwards:

- `"dynamodb.export"`: (Required) A string value:
  - If set to `ddb` enables the AWS Glue DynamoDB export connector
    where a new `ExportTableToPointInTimeRequest` will be invoked during the
    AWS Glue job. A new export will be generated with the location passed from
    `dynamodb.s3.bucket` and `dynamodb.s3.prefix`.
  - If set to `s3` enables the AWS Glue DynamoDB export connector but
    skips the creation of a new DynamoDB export and instead uses the
    `dynamodb.s3.bucket` and `dynamodb.s3.prefix` as the Amazon S3 location
    of a past export of that table.

- `"dynamodb.tableArn"`: (Required) The DynamoDB table to read from.
- `"dynamodb.unnestDDBJson"`: (Optional) Default: false. Valid values: boolean. If set to true,
  performs an unnest transformation of the DynamoDB JSON structure that is present in exports. It is an error to set
  `"dynamodb.unnestDDBJson"` and `"dynamodb.simplifyDDBJson"` to true at the same time.
  In AWS Glue 3.0 and later versions, we recommend you use `"dynamodb.simplifyDDBJson"` for better
  behavior when simplifying DynamoDB Map types. For more information, see [Simplifying usage of DynamoDB export JSON](#etl-connect-dynamodb-traversing-structure "#etl-connect-dynamodb-traversing-structure").
- `"dynamodb.simplifyDDBJson"`: (Optional) Default: false. Valid values: boolean. If
  set to true, performs a transformation to simplify the schema of the DynamoDB JSON structure that
  is present in exports. This has the same purpose as the `"dynamodb.unnestDDBJson"`
  option but provides better support for DynamoDB Map types or even nested Map types in your DynamoDB
  table. This option is available in AWS Glue 3.0 and later versions. It is an error to set
  `"dynamodb.unnestDDBJson"` and `"dynamodb.simplifyDDBJson"` to true at the
  same time. For more information, see [Simplifying usage of DynamoDB export JSON](#etl-connect-dynamodb-traversing-structure "#etl-connect-dynamodb-traversing-structure").
- `"dynamodb.s3.bucket"`: (Optional) Indicates the Amazon S3 bucket location in which the
  DynamoDB `ExportTableToPointInTime` process is to be conducted. The file format for the
  export is DynamoDB JSON.
  - `"dynamodb.s3.prefix"`: (Optional) Indicates the Amazon S3 prefix location
    inside the Amazon S3 bucket in which the DynamoDB `ExportTableToPointInTime` loads
    are to be stored. If neither `dynamodb.s3.prefix` nor
    `dynamodb.s3.bucket` are specified, these values will default to the
    Temporary Directory location specified in the AWS Glue job configuration.
    For more information, see [Special Parameters Used by AWS Glue](aws-glue-programming-etl-glue-arguments.md "aws-glue-programming-etl-glue-arguments.md").
  - `"dynamodb.s3.bucketOwner"`: Indicates the bucket owner needed for
    cross-account Amazon S3 access.

- `"dynamodb.sts.roleArn"`: (Optional) The IAM role ARN to be assumed for
  cross-account access and/or cross-Region access for the DynamoDB table. Note: The same IAM role
  ARN will be used to access the Amazon S3 location specified for the
  `ExportTableToPointInTime` request.
- `"dynamodb.sts.roleSessionName"`: (Optional) STS session name. The default is set
  to "glue-dynamodb-read-sts-session".
- `"dynamodb.exportTime"` (Optional) Valid values: strings representing ISO-8601 instants. A point-in-time at which the export should be made.
- `"dynamodb.sts.region"`: (Required if making a cross-region call using a regional endpoint) The region hosting the DynamoDB table you want to read.

### "connectionType": "dynamodb" with the ETL connector as

sink

Use the following connection options with `"connectionType": "dynamodb"` as a sink:

- `"dynamodb.output.tableName"`: (Required) The DynamoDB table to write to.
- `"dynamodb.throughput.write.percent"`: (Optional) The percentage of write capacity
  units (WCU) to use. The default is set to "0.5". Acceptable values are from "0.1" to "1.5",
  inclusive.
  - `0.5` represents the default write rate, meaning that AWS Glue
    will attempt to consume half of the write capacity of the table. If you increase the
    value above 0.5, AWS Glue increases the request rate; decreasing the value
    below 0.5 decreases the write request rate. (The actual write rate will vary, depending
    on factors such as whether there is a uniform key distribution in the DynamoDB
    table).
  - When the DynamoDB table is in on-demand mode, AWS Glue handles the write
    capacity of the table as `40000`. For importing a large table, we recommend
    switching your DynamoDB table to on-demand mode.

- `"dynamodb.output.numParallelTasks"`: (Optional) Defines how many parallel tasks
  write into DynamoDB at the same time. Used to calculate permissive WCU per Spark task. In most cases, AWS Glue will calculate a
  reasonable default for this value. For more information, see [Configuring paralleism in DynamoDB operations](#aws-glue-programming-etl-connect-dynamodb-parallelism "#aws-glue-programming-etl-connect-dynamodb-parallelism").
- `"dynamodb.output.retry"`: (Optional) Defines how many retries we perform when
  there is a `ProvisionedThroughputExceededException` from DynamoDB. The default is set to
  "10".
- `"dynamodb.sts.roleArn"`: (Optional) The IAM role ARN to be assumed for
  cross-account access.
- `"dynamodb.sts.roleSessionName"`: (Optional) STS session name. The default is set
  to "glue-dynamodb-write-sts-session".
