Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Use connectors to move data in Managed Service for Apache Flink with the

DataStream API

In the Amazon Managed Service for Apache Flink DataStream API, _connectors_ are software
components that move data into and out of a Managed Service for Apache Flink application. Connectors are flexible integrations
that let you read from files and directories. Connectors consist of complete modules for
interacting with Amazon services and third-party systems.

Types of connectors include the following:

- [Add streaming data sources](how-sources.md "how-sources.md"): Provide data to your
  application from a Kinesis data stream, file, or other data source.
- [Write data using sinks](how-sinks.md "how-sinks.md"): Send data from your application
  to a Kinesis data stream, Firehose stream, or other data destination.
- [Use Asynchronous I/O](how-async.md "how-async.md"): Provides asynchronous access to a data source (such as a database) to enrich stream events.

## Available connectors

The Apache Flink framework contains connectors for accessing data from a variety of sources. For information about connectors available in the Apache Flink framework, see [Connectors](https://nightlies.apache.org/flink/flink-docs-release-1.15/dev/connectors/ "https://nightlies.apache.org/flink/flink-docs-release-1.15/dev/connectors/") in the [Apache Flink documentation](https://nightlies.apache.org/flink/flink-docs-release-1.15/ "https://nightlies.apache.org/flink/flink-docs-release-1.15/").

###### Warning

If you have applications running on Flink 1.6, 1.8, 1.11 or 1.13 and would like to run in
Middle East (UAE), Asia Pacific (Hyderabad), Israel (Tel Aviv),
Europe (Zurich), Middle East (UAE), Asia Pacific (Melbourne) or
Asia Pacific (Jakarta) Regions, you might have to rebuild your application archive
with an updated connector or upgrade to Flink 1.18.

Apache Flink connectors are stored in their own open source repositories. If
you're upgrading to version 1.18 or later, you must update your dependencies. To
access the repository for Apache Flink AWS connectors, see [flink-connector-aws](https://github.com/apache/flink-connector-aws "https://github.com/apache/flink-connector-aws").

The former Kinesis source
`org.apache.flink.streaming.connectors.kinesis.FlinkKinesisConsumer`
is discontinued and might be removed with a future release of Flink. Use [Kinesis Source](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/datastream/kinesis/#kinesis-streams-source "https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/datastream/kinesis/#kinesis-streams-source") instead.

There is no state compatibility between the `FlinkKinesisConsumer` and
`KinesisStreamsSource`. For details, see [Migrating existing jobs to new Kinesis Streams Source](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/datastream/kinesis/#migrating-existing-jobs-to-new-kinesis-streams-source-from-kinesis-consumer "https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/datastream/kinesis/#migrating-existing-jobs-to-new-kinesis-streams-source-from-kinesis-consumer") in the Apache
Flink documentation.

Following are the recommended guidelines:

| Connector upgrades | Flink version                              | Connector used                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Resolution |
| ------------------ | ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| 1.19, 1.20         | Kinesis Source                             | When upgrading to Managed Service for Apache Flink version 1.19 and 1.20, make sure that you are using the most recent Kinesis Data Streams source connector. That must be any version 5.0.0 or later. For more information, see [Amazon Kinesis Data Streams Connector](https://nightlies.apache.org/flink/flink-docs-stable/docs/connectors/datastream/kinesis/ "https://nightlies.apache.org/flink/flink-docs-stable/docs/connectors/datastream/kinesis/").                                    |
| 1.19, 1.20         | Kinesis Sink                               | When upgrading to Managed Service for Apache Flink version 1.19 and 1.20, make sure that you are using the most recent Kinesis Data Streams sink connector. That must be any version 5.0.0 or later. For more information, see [Kinesis Streams Sink](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/datastream/kinesis/#kinesis-streams-sink "https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/datastream/kinesis/#kinesis-streams-sink"). |
| 1.19, 1.20         | DynamoDB Streams Source                    | When upgrading to Managed Service for Apache Flink version 1.19 and 1.20, make sure that you are using the most recent DynamoDB Streams source connector. That must be any version 5.0.0 or later. For more information, see [Amazon DynamoDB Connector](https://nightlies.apache.org/flink/flink-docs-stable/docs/connectors/datastream/dynamodb/ "https://nightlies.apache.org/flink/flink-docs-stable/docs/connectors/datastream/dynamodb/").                                                  |
| 1.19, 1.20         | DynamoDB Sink                              | When upgrading to Managed Service for Apache Flink version 1.19 and 1.20, make sure that you are using the most recent DynamoDB sink connector. That must be any version 5.0.0 or later. For more information, see [Amazon DynamoDB Connector](https://nightlies.apache.org/flink/flink-docs-stable/docs/connectors/datastream/dynamodb/ "https://nightlies.apache.org/flink/flink-docs-stable/docs/connectors/datastream/dynamodb/").                                                            |
| 1.19, 1.20         | Amazon SQS Sink                            | When upgrading to Managed Service for Apache Flink version 1.19 and 1.20, make sure that you are using the most recent Amazon SQS sink connector. That must be any version 5.0.0 or later. For more information, see [Amazon SQS Sink](https://nightlies.apache.org/flink/flink-docs-stable/docs/connectors/datastream/sqs/ "https://nightlies.apache.org/flink/flink-docs-stable/docs/connectors/datastream/sqs/").                                                                              |
| 1.19, 1.20         | Amazon Managed Service for Prometheus Sink | When upgrading to Managed Service for Apache Flink version 1.19 and 1.20, make sure that you are using the most recent Amazon Managed Service for Prometheus sink connector. That must be any version 1.0.0 or later. For more information, see [Prometheus Sink](https://nightlies.apache.org/flink/flink-docs-stable/docs/connectors/datastream/prometheus/ "https://nightlies.apache.org/flink/flink-docs-stable/docs/connectors/datastream/prometheus/").                                     |
