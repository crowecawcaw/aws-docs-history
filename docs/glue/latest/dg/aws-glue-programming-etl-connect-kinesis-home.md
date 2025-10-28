# Kinesis connections

You can use a Kinesis connection to read and write to Amazon Kinesis data streams using information stored in a Data Catalog table, or by providing
information to directly access the data stream. You can read information from Kinesis into a Spark DataFrame, then
convert it to a AWS Glue DynamicFrame. You can write DynamicFrames to Kinesis in a JSON format. If you directly access the data stream, use
these options to provide the information about how to access the data stream.

If you use `getCatalogSource` or `create_data_frame_from_catalog` to
consume records from a Kinesis streaming source, the job has the Data Catalog database and table name
information, and can use that to obtain some basic parameters for reading from the Kinesis
streaming source. If you use `getSource`, `getSourceWithFormat`, `createDataFrameFromOptions` or
`create_data_frame_from_options`, you must specify these basic parameters using
the connection options described here.

You can specify the connection options for Kinesis using the following arguments for the
specified methods in the `GlueContext` class.

- Scala
  - `connectionOptions`: Use with `getSource`, `createDataFrameFromOptions`, `getSink`
  - `additionalOptions`: Use with `getCatalogSource`, `getCatalogSink`
  - `options`: Use with `getSourceWithFormat`, `getSinkWithFormat`

- Python
  - `connection_options`: Use with
    `create_data_frame_from_options`, `write_dynamic_frame_from_options`
  - `additional_options`: Use with
    `create_data_frame_from_catalog`, `write_dynamic_frame_from_catalog`
  - `options`: Use with `getSource`, `getSink`

For notes and restrictions about Streaming ETL jobs, consult [Streaming ETL notes and
restrictions](add-job-streaming.md#create-job-streaming-restrictions "add-job-streaming.md#create-job-streaming-restrictions").

## Configure Kinesis

To connect to a Kinesis data stream in an AWS Glue Spark job, you will need some prerequisites:

- If reading, the AWS Glue job must have Read access level IAM permissions to the Kinesis data stream.
- If writing, the AWS Glue job must have Write access level IAM permissions to the Kinesis data stream.

In certain cases, you will need to configure additional prerequisites:

- If your AWS Glue job is configured with **Additional network connections** (typically to
  connect to other datasets) and one of those connections provides Amazon VPC **Network options**,
  this will direct your job to communicate over Amazon VPC. In this case you will also need to configure your Kinesis
  data stream to communicate over Amazon VPC. You can do this by creating an interface VPC endpoint between your
  Amazon VPC and Kinesis data stream. For more information, see [Using Kinesis Data Streams with Interface VPC Endpoints](../../../streams/latest/dev/vpc.md "../../../streams/latest/dev/vpc.md").
- When specifying Amazon Kinesis Data Streams in another account, you must setup the roles and policies to allow
  cross-account access. For more information, see [Example: Read From a
  Kinesis Stream in a Different Account](../../../kinesisanalytics/latest/java/examples-cross.md "../../../kinesisanalytics/latest/java/examples-cross.md").

For more information about Streaming ETL job prerequisites, consult [Streaming ETL jobs in AWS Glue](add-job-streaming.md "add-job-streaming.md").

## Example: Reading from Kinesis streams

### Example: Reading from Kinesis streams

Used in conjunction with [forEachBatch](aws-glue-api-crawler-pyspark-extensions-glue-context.md#aws-glue-api-crawler-pyspark-extensions-glue-context-forEachBatch "aws-glue-api-crawler-pyspark-extensions-glue-context.md#aws-glue-api-crawler-pyspark-extensions-glue-context-forEachBatch").

Example for Amazon Kinesis streaming source:

```
kinesis_options =
   { "streamARN": "arn:aws:kinesis:us-east-2:777788889999:stream/fromOptionsStream",
     "startingPosition": "TRIM_HORIZON",
     "inferSchema": "true",
     "classification": "json"
   }
data_frame_datasource0 = glueContext.create_data_frame.from_options(connection_type="kinesis", connection_options=kinesis_options)
```

## Example: Writing to Kinesis streams

### Example: Reading from Kinesis streams

Used in conjunction with [forEachBatch](aws-glue-api-crawler-pyspark-extensions-glue-context.md#aws-glue-api-crawler-pyspark-extensions-glue-context-forEachBatch "aws-glue-api-crawler-pyspark-extensions-glue-context.md#aws-glue-api-crawler-pyspark-extensions-glue-context-forEachBatch").

Example for Amazon Kinesis streaming source:

```
kinesis_options =
   { "streamARN": "arn:aws:kinesis:us-east-2:777788889999:stream/fromOptionsStream",
     "startingPosition": "TRIM_HORIZON",
     "inferSchema": "true",
     "classification": "json"
   }
data_frame_datasource0 = glueContext.create_data_frame.from_options(connection_type="kinesis", connection_options=kinesis_options)
```

## Kinesis connection option reference

Designates connection options for Amazon Kinesis Data Streams.

Use the following connection options for Kinesis streaming data sources:

- `"streamARN"` (Required) Used for Read/Write. The ARN of the Kinesis data stream.
- `"classification"` (Required for read) Used for Read. The file format used by the data in the record.
  Required unless provided through the Data Catalog.
- `"streamName"` – (Optional) Used for Read. The name of a Kinesis data stream to read from. Used with `endpointUrl`.
- `"endpointUrl"` – (Optional) Used for Read. Default: "https://kinesis.us-east-1.amazonaws.com". The AWS endpoint of the Kinesis stream. You do not
  need to change this unless you are connecting to a special region.
- `"partitionKey"` – (Optional) Used for Write. The Kinesis partition key used when producing records.
- `"delimiter"` (Optional) Used for Read. The value separator used when
  `classification` is CSV. Default is "`,`."
- `"startingPosition"`: (Optional) Used for Read. The starting position in the Kinesis data stream
  to read data from. The possible values are `"latest"`, `"trim_horizon"`,
  `"earliest"`, or a Timestamp string in UTC format in the pattern `yyyy-mm-ddTHH:MM:SSZ`
  (where `Z` represents a UTC timezone offset with a +/-. For example "2023-04-04T08:00:00-04:00").
  The default value is `"latest"`. Note: the Timestamp string in UTC Format for
  `"startingPosition"` is supported only for AWS Glue version 4.0 or later.
- `"failOnDataLoss"`: (Optional) Fail the job if any active shard is missing or expired. The default value is `"false"`.
- `"awsSTSRoleARN"`: (Optional) Used for Read/Write. The Amazon Resource Name (ARN) of the role
  to assume using AWS Security Token Service (AWS STS). This role must have permissions for describe or read record operations for
  the Kinesis data stream. You must use this parameter when accessing a data stream in a different account. Used in
  conjunction with `"awsSTSSessionName"`.
- `"awsSTSSessionName"`: (Optional) Used for Read/Write. An identifier for the session assuming
  the role using AWS STS. You must use this parameter when accessing a data stream in a different account. Used in
  conjunction with `"awsSTSRoleARN"`.
- `"awsSTSEndpoint"`: (Optional) The AWS STS endpoint to use when connecting to Kinesis with an assumed role.
  This allows using the regional AWS STS endpoint in a VPC, which is not possible with the default global endpoint.
- `"maxFetchTimeInMs"`: (Optional) Used for Read. The maximum time spent for the job executor to read records for the current batch from the Kinesis data stream, specified in milliseconds (ms). Multiple `GetRecords` API calls may be made within this time. The default value is `1000`.
- `"maxFetchRecordsPerShard"`: (Optional) Used for Read. The maximum number of records to fetch per shard in the Kinesis data stream per microbatch. Note: The client can exceed this limit if the streaming job has already read extra records from Kinesis (in the same get-records call). If `maxFetchRecordsPerShard` needs to be strict then it needs to be a multiple of `maxRecordPerRead`. The default value is `100000`.
- `"maxRecordPerRead"`: (Optional) Used for Read. The maximum number of records to fetch from the
  Kinesis data stream in each `getRecords` operation. The default value is `10000`.
- `"addIdleTimeBetweenReads"`: (Optional) Used for Read. Adds a time delay between two
  consecutive `getRecords` operations. The default value is `"False"`. This option is only
  configurable for Glue version 2.0 and above.
- `"idleTimeBetweenReadsInMs"`: (Optional) Used for Read. The minimum time delay between two
  consecutive `getRecords` operations, specified in ms. The default value is `1000`. This
  option is only configurable for Glue version 2.0 and above.
- `"describeShardInterval"`: (Optional) Used for Read. The minimum time interval between two
  `ListShards` API calls for your script to consider resharding. For more information, see [Strategies
  for Resharding](../../../streams/latest/dev/kinesis-using-sdk-java-resharding-strategies.md "../../../streams/latest/dev/kinesis-using-sdk-java-resharding-strategies.md") in _Amazon Kinesis Data Streams Developer Guide_. The default value is
  `1s`.
- `"numRetries"`: (Optional) Used for Read. The maximum number of retries for Kinesis Data Streams API requests.
  The default value is `3`.
- `"retryIntervalMs"`: (Optional) Used for Read. The cool-off time period (specified in ms)
  before retrying the Kinesis Data Streams API call. The default value is `1000`.
- `"maxRetryIntervalMs"`: (Optional) Used for Read. The maximum cool-off time period (specified
  in ms) between two retries of a Kinesis Data Streams API call. The default value is `10000`.
- `"avoidEmptyBatches"`: (Optional) Used for Read. Avoids creating an empty microbatch job by
  checking for unread data in the Kinesis data stream before the batch is started. The default value is
  `"False"`.
- `"schema"`: (Required when inferSchema set to false) Used for Read. The schema to use to
  process the payload. If classification is `avro` the provided schema must be in the Avro schema
  format. If the classification is not `avro` the provided schema must be in the DDL schema
  format.

The following are schema examples.

Example in DDL schema format

```
`column1` INT, `column2` STRING , `column3` FLOAT
```

Example in Avro schema format

```
{
  "type":"array",
  "items":
  {
    "type":"record",
    "name":"test",
    "fields":
    [
      {
        "name":"_id",
        "type":"string"
      },
      {
        "name":"index",
        "type":
        [
          "int",
          "string",
          "float"
        ]
      }
    ]
  }
}
```

- `"inferSchema"`: (Optional) Used for Read. The default value is 'false'. If set to 'true', the
  schema will be detected at runtime from the payload within `foreachbatch`.
- `"avroSchema"`: (Deprecated) Used for Read. Parameter used to specify a schema of Avro data
  when Avro format is used. This parameter is now deprecated. Use the `schema` parameter.
- `"addRecordTimestamp"`: (Optional) Used for Read. When this option is set to 'true', the data
  output will contain an additional column named "\_\_src_timestamp" that indicates the time when the
  corresponding record received by the stream. The default value is 'false'. This option is supported in
  AWS Glue version 4.0 or later.
- `"emitConsumerLagMetrics"`: (Optional) Used for Read. When the option is set to 'true', for
  each batch, it will emit the metrics for the duration between the oldest record received by the stream and the
  time it arrives in AWS Glue to CloudWatch. The metric's name is
  "glue.driver.streaming.maxConsumerLagInMs". The default value is 'false'. This option is supported in
  AWS Glue version 4.0 or later.
- `"fanoutConsumerARN"`: (Optional) Used for Read. The ARN of a Kinesis stream consumer for the
  stream specified in `streamARN`. Used to enable enhanced fan-out mode for your Kinesis connection. For
  more information on consuming a Kinesis stream with enhanced fan-out, see [Using enhanced fan-out in Kinesis streaming jobs](aws-glue-programming-etl-connect-kinesis-efo.md "aws-glue-programming-etl-connect-kinesis-efo.md").
- `"recordMaxBufferedTime"` – (Optional) Used for Write. Default: 1000 (ms). Maximum time
  a record is buffered while waiting to be written.
- `"aggregationEnabled"` – (Optional) Used for Write. Default: true. Specifies if records
  should be aggregated before sending them to Kinesis.
- `"aggregationMaxSize"` – (Optional) Used for Write. Default: 51200 (bytes). If a record
  is larger than this limit, it will bypass the aggregator. Note Kinesis enforces a limit of 50KB on record size.
  If you set this beyond 50KB, oversize records will be rejected by Kinesis.
- `"aggregationMaxCount"` – (Optional) Used for Write. Default: 4294967295. Maximum number
  of items to pack into an aggregated record.
- `"producerRateLimit"` – (Optional) Used for Write. Default: 150 (%). Limits per-shard
  throughput sent from a single producer (such as your job), as a percentage of the backend limit.
- `"collectionMaxCount"` – (Optional) Used for Write. Default: 500. Maximum number of
  items to pack into an PutRecords request.
- `"collectionMaxSize"` – (Optional) Used for Write. Default: 5242880 (bytes). Maximum
  amount of data to send with a PutRecords request.
