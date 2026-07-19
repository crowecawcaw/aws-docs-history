# Use Apache Flink connectors with Managed Service for Apache Flink

Apache Flink connectors are software components that move data into and out of an
Amazon Managed Service for Apache Flink application. Connectors are flexible integrations that let you read from
files and directories. Connectors consist of complete modules for interacting with Amazon
services and third-party systems.

Types of connectors include the following:

- **Sources:** Provide data to your application from a Kinesis data
  stream, file, Apache Kafka topic, file, or other data sources.
- **Sinks:** Send data from your application to a Kinesis
  data stream, Firehose stream, Apache Kafka topic, or other data destinations.
- **Asynchronous I/O:** Provides asynchronous access to
  a data source such as a database to enrich streams.
  Apache Flink connectors are stored in their own source repositories. The version and
  artifact for Apache Flink connectors changes depending on the Apache Flink version you are
  using, and whether you are using the DataStream, Table, or SQL API.

Amazon Managed Service for Apache Flink supports over 40 pre-built Apache Flink source and sink connectors. The
following table provides a summary of the most popular connectors and their associated
versions. You can also build custom sinks using the Async-sink framework. For more
information, see [The Generic Asynchronous Base Sink](https://flink.apache.org/2022/03/16/the-generic-asynchronous-base-sink/ "https://flink.apache.org/2022/03/16/the-generic-asynchronous-base-sink/") in the Apache Flink documentation.

To access the repository for Apache Flink AWS connectors, see [flink-connector-aws](https://github.com/apache/flink-connector-aws "https://github.com/apache/flink-connector-aws").

## Connectors for Flink 2.0+

When upgrading to Flink 2.x, you need to update your connector dependencies to
versions that are compatible with the Flink 2.x runtime. Flink connectors are released
independently from the Flink runtime, and not all connectors have a Flink
2.x-compatible release yet. The following table summarizes the availability of commonly
used connectors in Amazon Managed Service for Apache Flink as of this writing:

Connectors for Flink 2.0+| Connector | Flink 2.2 Version | Flink 2.3 Version |
| --- | --- | --- |
| Apache Kafka | flink-connector-kafka 4.0.0-2.0 | flink-connector-kafka 4.0.0-2.0 |
| Kinesis Data Streams (source) | flink-connector-aws-kinesis-streams 6.0.1-2.0 | flink-connector-aws-kinesis-streams 6.0.1-2.0 |
| Kinesis Data Streams (sink) | flink-connector-aws-kinesis-streams 6.0.1-2.0 | flink-connector-aws-kinesis-streams 6.0.1-2.0 |
| FileSystem (S3, HDFS) | Bundled with Flink | Bundled with Flink |
| JDBC | flink-connector-jdbc-core 4.0.0-2.0 | flink-connector-jdbc-core 4.0.0-2.0 |
| OpenSearch | Not yet released for 2.x | Not yet released for 2.x |
| Elasticsearch | flink-connector-elasticsearch7 4.0.0-2.0 | flink-connector-elasticsearch7 4.0.0-2.0 |
| Amazon Managed Service for Prometheus | Not yet released for 2.x | Not yet released for 2.x |

If your application depends on a connector that does not yet have a Flink 2.x
release, you have two options: wait for the connector to release a compatible version,
or evaluate whether you can replace it with an alternative (for example, using the JDBC
catalog or a custom sink).

###### Note

Starting with version 4.0.0-2.0, the JDBC connector is modularized. The
monolithic `flink-connector-jdbc` artifact is replaced by a core
artifact (`flink-connector-jdbc-core`) and database-specific artifacts
such as `flink-connector-jdbc-postgres` and
`flink-connector-jdbc-mysql`. Update your Maven or Gradle dependencies
accordingly when upgrading to Flink 2.x.

**Known issues**

- Applications using the `KinesisStreamsSource` with EFO
  (Enhanced Fan-Out / SubscribeToShard) path introduced in connector v5.0.0 and
  v6.0.0 may fail when Kinesis streams undergo resharding. This is a known issue
  in the community. For more information, see [FLINK-37648](https://issues.apache.org/jira/browse/FLINK-37648 "https://issues.apache.org/jira/browse/FLINK-37648").
- Applications using the `KinesisStreamsSource` with EFO
  (Enhanced Fan-Out / SubscribeToShard) path introduced in connector v5.0.0 and
  v6.0.0 together with `KinesisStreamsSink` may experience deadlocks
  if the Flink application is under backpressure, resulting in a complete stop of
  data processing in one or more TaskManagers. A force stop operation and a start
  app operation are needed to recover the app. This is a sub-case of the known
  issue in the community: [FLINK-34071](https://issues.apache.org/jira/browse/FLINK-34071 "https://issues.apache.org/jira/browse/FLINK-34071").

## Connectors for older Flink versions

Connectors for older Flink versions| Connector | Flink version 1.15 | Flink version 1.18 | Flink versions 1.19 | Flink versions 1.20 |
| --- | --- | --- | --- | --- |
| Kinesis Data Stream<br>• Source<br>• DataStream and Table API | flink-connector-kinesis, 1.15.4 | flink-connector-kinesis, 4.3.0-1.18 | flink-connector-kinesis, 5.0.0-1.19 | flink-connector-kinesis, 5.0.0-1.20 |
| Kinesis Data Stream<br>• Sink<br>• DataStream and Table API | flink-connector-aws-kinesis-streams, 1.15.4 | flink-connector-aws-kinesis-streams, 4.3.0-1.18 | flink-connector-aws-kinesis-streams, 5.0.0-1.19 | flink-connector-aws-kinesis-streams, 5.0.0-1.20 |
| Kinesis Data Streams<br>• Source/Sink<br>• SQL | flink-sql-connector-kinesis, 1.15.4 | flink-sql-connector-kinesis, 4.3.0-1.18 | flink-sql-connector-kinesis, 5.0.0-1.19 | flink-sql-connector-kinesis-streams, 5.0.0-1.20 |
| Kafka<br>• DataStream and Table API | flink-connector-kafka, 1.15.4 | flink-connector-kafka, 3.2.0-1.18 | flink-connector-kafka, 3.3.0-1.19 | flink-connector-kafka, 3.3.0-1.20 |
| Kafka<br>• SQL | flink-sql-connector-kafka, 1.15.4 | flink-sql-connector-kafka, 3.2.0-1.18 | flink-sql-connector-kafka, 3.3.0-1.19 | flink-sql-connector-kafka, 3.3.0-1.20 |
| Firehose<br>• DataStream and Table API | flink-connector-aws-kinesis-firehose, 1.15.4 | flink-connector-aws-firehose, 4.3.0-1.18 | flink-connector-aws-firehose, 5.0.0-1.19 | flink-connector-aws-firehose, 5.0.0-1.20 |
| Firehose<br>• SQL | flink-sql-connector-aws-kinesis-firehose, 1.15.4 | flink-sql-connector-aws-firehose, 4.3.0-1.18 | flink-sql-connector-aws-firehose, 5.0.0-1.19 | flink-sql-connector-aws-firehose, 5.0.0-1.20 |
| DynamoDB<br>• DataStream and Table API | flink-connector-dynamodb, 3.0.0-1.15 | flink-connector-dynamodb, 4.3.0-1.18 | flink-connector-dynamodb, 5.0.0-1.19 | flink-connector-dynamodb, 5.0.0-1.20 |
| DynamoDB<br>• SQL | flink-sql-connector-dynamodb, 3.0.0-1.15 | flink-sql-connector-dynamodb, 4.3.0-1.18 | flink-sql-connector-dynamodb, 5.0.0-1.19 | flink-sql-connector-dynamodb, 5.0.0-1.20 |
| OpenSearch<br>• DataStream and Table API | - | flink-connector-opensearch, 1.2.0-1.18 | flink-connector-opensearch, 1.2.0-1.19 | flink-connector-opensearch, 1.2.0-1.19 |
| OpenSearch<br>• SQL | - | flink-sql-connector-opensearch, 1.2.0-1.18 | flink-sql-connector-opensearch, 1.2.0-1.19 | flink-sql-connector-opensearch, 1.2.0-1.19 |
| Amazon Managed Service for Prometheus DataStream | - | flink-sql-connector-opensearch, 1.2.0-1.18 | flink-connector-prometheus, 1.0.0-1.19 | flink-connector-prometheus, 1.0.0-1.20 |
| Amazon SQS DataStream and Table API | - | flink-sql-connector-opensearch, 1.2.0-1.18 | flink-connector-sqs, 5.0.0-1.19 | flink-connector-sqs, 5.0.0-1.20 |

To learn more about connectors in Amazon Managed Service for Apache Flink, see:

- [DataStream API connectors](how-connectors.md "how-connectors.md")
- [Table API connectors](how-table-connectors.md "how-table-connectors.md")

### Known issues

There is a known open source Apache Flink issue with the Apache Kafka connector in
Apache Flink 1.15. This issue is resolved in later versions of Apache Flink.

For more information, see [Known issues](flink-1-15-2.md#flink-1-15-known-issues "flink-1-15-2.md#flink-1-15-known-issues").
