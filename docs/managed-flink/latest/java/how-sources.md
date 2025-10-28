Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Add streaming data sources to Managed Service for Apache Flink

Apache Flink provides connectors for reading from files, sockets, collections, and
custom sources. In your application code, you use an [Apache Flink source](https://nightlies.apache.org/flink/flink-docs-release-1.15/dev/datastream_api.html#data-sources "https://nightlies.apache.org/flink/flink-docs-release-1.15/dev/datastream_api.html#data-sources") to receive data from a stream. This section describes
the sources that are available for Amazon services.

## Use Kinesis data streams

The `KinesisStreamsSource` provides streaming data to your application
from an Amazon Kinesis data stream.

### Create a

`KinesisStreamsSource`

The following code example demonstrates creating a
`KinesisStreamsSource`:

```
// Configure the KinesisStreamsSource
Configuration sourceConfig = new Configuration();
sourceConfig.set(KinesisSourceConfigOptions.STREAM_INITIAL_POSITION, KinesisSourceConfigOptions.InitialPosition.TRIM_HORIZON); // This is optional, by default connector will read from LATEST

// Create a new KinesisStreamsSource to read from specified Kinesis Stream.
KinesisStreamsSource<String> kdsSource =
        KinesisStreamsSource.<String>builder()
                .setStreamArn("arn:aws:kinesis:us-east-1:123456789012:stream/test-stream")
                .setSourceConfig(sourceConfig)
                .setDeserializationSchema(new SimpleStringSchema())
                .setKinesisShardAssigner(ShardAssignerFactory.uniformShardAssigner()) // This is optional, by default uniformShardAssigner will be used.
                .build();
```

For more information about using a `KinesisStreamsSource`, see
[Amazon Kinesis Data Streams Connector](https://nightlies.apache.org/flink/flink-docs-stable/docs/connectors/datastream/kinesis/ "https://nightlies.apache.org/flink/flink-docs-stable/docs/connectors/datastream/kinesis/") in the Apache Flink
documentation and [our public KinesisConnectors example on Github](https://github.com/aws-samples/amazon-managed-service-for-apache-flink-examples/tree/main/java/KinesisConnectors "https://github.com/aws-samples/amazon-managed-service-for-apache-flink-examples/tree/main/java/KinesisConnectors").

### Create a `KinesisStreamsSource` that uses an EFO

consumer

The `KinesisStreamsSource` now supports [Enhanced Fan-Out (EFO)](https://ci.apache.org/projects/flink/flink-docs-release-1.13/docs/connectors/datastream/kinesis/ "https://ci.apache.org/projects/flink/flink-docs-release-1.13/docs/connectors/datastream/kinesis/").

If a Kinesis consumer uses EFO, the Kinesis Data Streams service gives it its own dedicated bandwidth, rather than having the consumer
share the fixed bandwidth of the stream with the other consumers reading from the stream.

For more information about using EFO with the Kinesis consumer, see [FLIP-128: Enhanced Fan Out for AWS Kinesis Consumers](https://cwiki.apache.org/confluence/display/FLINK/FLIP-128%3A+Enhanced+Fan+Out+for+AWS+Kinesis+Consumers "https://cwiki.apache.org/confluence/display/FLINK/FLIP-128%3A+Enhanced+Fan+Out+for+AWS+Kinesis+Consumers").

You enable the EFO consumer by setting the following parameters on the Kinesis consumer:

- **READER_TYPE:** Set this parameter to **EFO** for your application to use an EFO consumer to
  access the Kinesis Data Stream data.
- **EFO_CONSUMER_NAME:** Set this parameter to a string value that
  is unique among the consumers of this stream. Re-using a consumer name
  in the same Kinesis Data Stream will cause the previous consumer using that
  name to be terminated.

To configure a `KinesisStreamsSource` to use EFO, add the following
parameters to the consumer:

```
sourceConfig.set(KinesisSourceConfigOptions.READER_TYPE, KinesisSourceConfigOptions.ReaderType.EFO);
sourceConfig.set(KinesisSourceConfigOptions.EFO_CONSUMER_NAME, "my-flink-efo-consumer");
```

For an example of a Managed Service for Apache Flink application that uses an EFO consumer, see
[our public Kinesis Connectors example on Github](https://github.com/aws-samples/amazon-managed-service-for-apache-flink-examples/tree/main/java/KinesisConnectors "https://github.com/aws-samples/amazon-managed-service-for-apache-flink-examples/tree/main/java/KinesisConnectors").

## Use Amazon MSK

The `KafkaSource` source provides streaming data to your
application from an Amazon MSK topic.

### Create a `KafkaSource`

The following code example demonstrates creating a
`KafkaSource`:

```
KafkaSource<String> source = KafkaSource.<String>builder()
    .setBootstrapServers(brokers)
    .setTopics("input-topic")
    .setGroupId("my-group")
    .setStartingOffsets(OffsetsInitializer.earliest())
    .setValueOnlyDeserializer(new SimpleStringSchema())
    .build();

env.fromSource(source, WatermarkStrategy.noWatermarks(), "Kafka Source");
```

For more information about using a `KafkaSource`, see
[MSK Replication](earlier.md#example-msk "earlier.md#example-msk").
