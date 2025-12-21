# Kafka connections

You can use a Kafka connection to read and write to Kafka data streams using information stored in a Data Catalog table, or by providing
information to directly access the data stream. The connection supports a Kafka cluster or an Amazon Managed Streaming for Apache Kafka cluster. You can read information from Kafka into a Spark DataFrame, then
convert it to a AWS Glue DynamicFrame. You can write DynamicFrames to Kafka in a JSON format. If you directly access the data stream, use
these options to provide the information about how to access the data stream.

If you use `getCatalogSource` or `create_data_frame_from_catalog` to
consume records from a Kafka streaming source, or `getCatalogSink` or `write_dynamic_frame_from_catalog` to write records to Kafka, and the job has the Data Catalog database and table name
information, and can use that to obtain some basic parameters for reading from the Kafka
streaming source. If you use `getSource`, `getCatalogSink`, `getSourceWithFormat`, `getSinkWithFormat`, `createDataFrameFromOptions` or
`create_data_frame_from_options`, or `write_dynamic_frame_from_catalog`, you must specify these basic parameters using
the connection options described here.

You can specify the connection options for Kafka using the following arguments for the
specified methods in the `GlueContext` class.

- Scala
  - `connectionOptions`: Use with `getSource`, `createDataFrameFromOptions`, `getSink`
  - `additionalOptions`: Use with `getCatalogSource`, `getCatalogSink`
  - `options`: Use with `getSourceWithFormat`, `getSinkWithFormat`

- Python

      + `connection_options`: Use with
       `create_data_frame_from_options`, `write_dynamic_frame_from_options`
      + `additional_options`: Use with
       `create_data_frame_from_catalog`, `write_dynamic_frame_from_catalog`
      + `options`: Use with `getSource`, `getSink`

  For notes and restrictions about streaming ETL jobs, consult [Streaming ETL notes and
  restrictions](add-job-streaming.md#create-job-streaming-restrictions "add-job-streaming.md#create-job-streaming-restrictions").

###### Topics

- [Configure Kafka](#aws-glue-programming-etl-connect-kafka-configure "#aws-glue-programming-etl-connect-kafka-configure")
- [Example: Reading from Kafka streams](#aws-glue-programming-etl-connect-kafka-read "#aws-glue-programming-etl-connect-kafka-read")
- [Example: Writing to Kafka streams](#aws-glue-programming-etl-connect-kafka-write "#aws-glue-programming-etl-connect-kafka-write")
- [Kafka connection option reference](#aws-glue-programming-etl-connect-kafka "#aws-glue-programming-etl-connect-kafka")

## Configure Kafka

There are no AWS prerequisites to connecting to Kafka streams available through the internet.

You can create a AWS Glue Kafka connection to manage your connection credentials. For more
information, see [Creating an AWS Glue connection for an Apache Kafka
data stream](add-job-streaming.md#create-conn-streaming "add-job-streaming.md#create-conn-streaming"). In your AWS Glue job configuration, provide
`connectionName` as an **Additional network connection**, then, in your method
call, provide `connectionName` to the `connectionName` parameter.

In certain cases, you will need to configure additional prerequisites:

- If using Amazon Managed Streaming for Apache Kafka with IAM authentication, you will need appropriate IAM configuration.
- If using Amazon Managed Streaming for Apache Kafka within an Amazon VPC, you will need appropriate Amazon VPC configuration. You will need
  to create a AWS Glue connection that provides Amazon VPC connection information. You will need your job configuration
  to include the AWS Glue connection as an **Additional network connection**.

For more information about Streaming ETL job prerequisites, consult [Streaming ETL jobs in AWS Glue](add-job-streaming.md "add-job-streaming.md").

## Example: Reading from Kafka streams

Used in conjunction with [forEachBatch](aws-glue-api-crawler-pyspark-extensions-glue-context.md#aws-glue-api-crawler-pyspark-extensions-glue-context-forEachBatch "aws-glue-api-crawler-pyspark-extensions-glue-context.md#aws-glue-api-crawler-pyspark-extensions-glue-context-forEachBatch").

Example for Kafka streaming source:

```
kafka_options =
    { "connectionName": "ConfluentKafka",
      "topicName": "kafka-auth-topic",
      "startingOffsets": "earliest",
      "inferSchema": "true",
      "classification": "json"
    }
data_frame_datasource0 = glueContext.create_data_frame.from_options(connection_type="kafka", connection_options=kafka_options)
```

## Example: Writing to Kafka streams

Examples for writing to Kafka:

Example with the `getSink` method:

```
data_frame_datasource0 =
glueContext.getSink(
	connectionType="kafka",
	connectionOptions={
		JsonOptions("""{
			"connectionName": "ConfluentKafka",
			"classification": "json",
			"topic": "kafka-auth-topic",
			"typeOfData": "kafka"}
		""")},
	transformationContext="dataframe_ApacheKafka_node1711729173428")
	.getDataFrame()
```

Example with the `write_dynamic_frame.from_options` method:

```
kafka_options =
    { "connectionName": "ConfluentKafka",
      "topicName": "kafka-auth-topic",
      "classification": "json"
    }
data_frame_datasource0 = glueContext.write_dynamic_frame.from_options(connection_type="kafka", connection_options=kafka_options)
```

## Kafka connection option reference

When reading, use the following connection options with `"connectionType": "kafka"`:

- `"bootstrap.servers"` (Required) A list of bootstrap server URLs, for
  example, as `b-1.vpc-test-2.o4q88o.c6.kafka.us-east-1.amazonaws.com:9094`. This
  option must be specified in the API call or defined in the table metadata in the
  Data Catalog.
- `"security.protocol"` (Required) The protocol used to
  communicate with brokers. The possible values are `"SSL"` or
  `"PLAINTEXT"`.
- `"topicName"` (Required) A comma-separated list of topics to subscribe to. You must specify one and only one of `"topicName"`, `"assign"` or `"subscribePattern"`.
- `"assign"`: (Required) A JSON string specifying the specific `TopicPartitions` to consume. You must specify one and only one of `"topicName"`, `"assign"` or `"subscribePattern"`.

Example: '{"topicA":[0,1],"topicB":[2,4]}'

- `"subscribePattern"`: (Required) A Java regex string that identifies the topic list to subscribe to. You must specify one and only one of `"topicName"`, `"assign"` or `"subscribePattern"`.

Example: 'topic.\*'

- `"classification"` (Required) The file format used by the data in the record. Required unless provided through the Data Catalog.
- `"delimiter"` (Optional) The value separator used when `classification` is CSV. Default is "`,`."
- `"startingOffsets"`: (Optional) The starting position in the Kafka topic to
  read data from. The possible values are `"earliest"` or `"latest"`.
  The default value is `"latest"`.
- `"startingTimestamp"`: (Optional, supported only for AWS Glue version 4.0 or later) The Timestamp of the record in the Kafka topic to read data from. The possible value is a Timestamp string in UTC format in the pattern `yyyy-mm-ddTHH:MM:SSZ` (where `Z` represents a UTC timezone offset with a +/-. For example: "2023-04-04T08:00:00-04:00").

Note: Only one of 'startingOffsets' or 'startingTimestamp' can be present in the Connection Options list of the AWS Glue streaming script, including both these properties will result in job failure.

- `"endingOffsets"`: (Optional) The end point when a batch query is ended.
  Possible values are either `"latest"` or a JSON string that specifies an ending
  offset for each `TopicPartition`.

For the JSON string, the format is
`{"topicA":{"0":23,"1":-1},"topicB":{"0":-1}}`. The value `-1` as
an offset represents `"latest"`.

- `"pollTimeoutMs"`: (Optional) The timeout in milliseconds to poll data from
  Kafka in Spark job executors. The default value is `600000`.
- `"numRetries"`: (Optional) The number of times to retry before failing to
  fetch Kafka offsets. The default value is `3`.
- `"retryIntervalMs"`: (Optional) The time in milliseconds to wait before
  retrying to fetch Kafka offsets. The default value is `10`.
- `"maxOffsetsPerTrigger"`: (Optional) The rate limit on the maximum number
  of offsets that are processed per trigger interval. The specified total number of offsets
  is proportionally split across `topicPartitions` of different volumes. The
  default value is null, which means that the consumer reads all offsets until the known
  latest offset.
- `"minPartitions"`: (Optional) The desired minimum number of partitions to
  read from Kafka. The default value is null, which means that the number of spark
  partitions is equal to the number of Kafka partitions.
- `"includeHeaders"`: (Optional) Whether to include the Kafka headers.
  When the option is set to "true", the data output will contain an additional column named "glue_streaming_kafka_headers"
  with type `Array[Struct(key: String, value: String)]`. The default value is "false".
  This option is available in AWS Glue version 3.0 or later.
- `"schema"`: (Required when inferSchema set to false) The schema to use to process the payload. If classification is `avro` the provided schema must be in the Avro schema format. If the classification is not `avro` the provided schema must be in the DDL schema format.

The following are schema examples.

Example in DDL schema format

```
'column1' INT, 'column2' STRING , 'column3' FLOAT
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

- `"inferSchema"`: (Optional) The default value is 'false'. If set to 'true', the schema will be detected at runtime from the payload within `foreachbatch`.
- `"avroSchema"`: (Deprecated) Parameter used to specify a schema of Avro data when Avro format is used. This parameter is now deprecated. Use the `schema` parameter.
- `"addRecordTimestamp"`: (Optional) When this option is set to 'true', the data output will contain an additional column named "\_\_src_timestamp" that indicates the time when the corresponding record received by the topic. The default value is 'false'. This option is supported in AWS Glue version 4.0 or later.
- `"emitConsumerLagMetrics"`: (Optional) When the option is set to 'true', for each batch, it will emit the metrics for the duration between the oldest record received by the topic and the time it arrives in AWS Glue to CloudWatch. The metric's name is "glue.driver.streaming.maxConsumerLagInMs". The default value is 'false'. This option is supported in AWS Glue version 4.0 or later.

When writing, use the following connection options with `"connectionType": "kafka"`:

- `"connectionName"` (Required) Name of the AWS Glue connection used to connect to the Kafka cluster (similar to Kafka source).
- `"topic"` (Required) If a topic column exists then its value is used as the topic when writing the given row to Kafka, unless the topic configuration option is set. That is, the `topic` configuration option overrides the topic column.
- `"partition"` (Optional) If a valid partition number is specified, that `partition` will be used when sending the record.

If no partition is specified but a `key` is present, a partition will be chosen using a hash of the key.

If neither `key` nor `partition` is present, a partition will be chosen based on sticky partitioning those changes when at least batch.size bytes are produced to the partition.

- `"key"` (Optional) Used for partitioning if `partition` is null.
- `"classification"` (Optional) The file format used by the data in the record. We only support JSON, CSV and Avro.

With Avro format, we can provide a custom avroSchema to serialize with, but note that this needs to be provided on the source for deserializing as well. Else, by default it uses the Apache AvroSchema for serializing.

Additionally, you can fine-tune the Kafka sink as required by updating the [Kafka producer configuration parameters](https://kafka.apache.org/documentation/#producerconfigs "https://kafka.apache.org/documentation/#producerconfigs"). Note that there is no allow listing on connection options, all the key-value pairs are persisted on the sink as is.

However, there is a small deny list of options that will not take effect. For more information, see [Kafka specific configurations](https://spark.apache.org/docs/latest/structured-streaming-kafka-integration.html "https://spark.apache.org/docs/latest/structured-streaming-kafka-integration.html").
