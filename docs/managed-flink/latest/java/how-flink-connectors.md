Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

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

| Connectors for Flink versions                                 | Connector                                        | Flink version 1.15                              | Flink version 1.18                              | Flink versions 1.19                             | Flink versions 1.20 |
| ------------------------------------------------------------- | ------------------------------------------------ | ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- | ------------------- |
| Kinesis Data Stream<br>• Source<br>• DataStream and Table API | flink-connector-kinesis, 1.15.4                  | flink-connector-kinesis, 4.3.0-1.18             | flink-connector-kinesis, 5.0.0-1.19             | flink-connector-kinesis, 5.0.0-1.20             |
| Kinesis Data Stream<br>• Sink<br>• DataStream and Table API   | flink-connector-aws-kinesis-streams, 1.15.4      | flink-connector-aws-kinesis-streams, 4.3.0-1.18 | flink-connector-aws-kinesis-streams, 5.0.0-1.19 | flink-connector-aws-kinesis-streams, 5.0.0-1.20 |
| Kinesis Data Streams<br>• Source/Sink<br>• SQL                | flink-sql-connector-kinesis, 1.15.4              | flink-sql-connector-kinesis, 4.3.0-1.18         | flink-sql-connector-kinesis, 5.0.0-1.19         | flink-sql-connector-kinesis-streams, 5.0.0-1.20 |
| Kafka<br>• DataStream and Table API                           | flink-connector-kafka, 1.15.4                    | flink-connector-kafka, 3.2.0-1.18               | flink-connector-kafka, 3.3.0-1.19               | flink-connector-kafka, 3.3.0-1.20               |
| Kafka<br>• SQL                                                | flink-sql-connector-kafka, 1.15.4                | flink-sql-connector-kafka, 3.2.0-1.18           | flink-sql-connector-kafka, 3.3.0-1.19           | flink-sql-connector-kafka, 3.3.0-1.20           |
| Firehose<br>• DataStream and Table API                        | flink-connector-aws-kinesis-firehose, 1.15.4     | flink-connector-aws-firehose, 4.3.0-1.18        | flink-connector-aws-firehose, 5.0.0-1.19        | flink-connector-aws-firehose, 5.0.0-1.20        |
| Firehose<br>• SQL                                             | flink-sql-connector-aws-kinesis-firehose, 1.15.4 | flink-sql-connector-aws-firehose, 4.3.0-1.18    | flink-sql-connector-aws-firehose, 5.0.0-1.19    | flink-sql-connector-aws-firehose, 5.0.0-1.20    |
| DynamoDB<br>• DataStream and Table API                        | flink-connector-dynamodb, 3.0.0-1.15             | flink-connector-dynamodb, 4.3.0-1.18            | flink-connector-dynamodb, 5.0.0-1.19            | flink-connector-dynamodb, 5.0.0-1.20            |
| DynamoDB<br>• SQL                                             | flink-sql-connector-dynamodb, 3.0.0-1.15         | flink-sql-connector-dynamodb, 4.3.0-1.18        | flink-sql-connector-dynamodb, 5.0.0-1.19        | flink-sql-connector-dynamodb, 5.0.0-1.20        |
| OpenSearch<br>• DataStream and Table API                      | -                                                | flink-connector-opensearch, 1.2.0-1.18          | flink-connector-opensearch, 1.2.0-1.19          | flink-connector-opensearch, 1.2.0-1.19          |
| OpenSearch<br>• SQL                                           | -                                                | flink-sql-connector-opensearch, 1.2.0-1.18      | flink-sql-connector-opensearch, 1.2.0-1.19      | flink-sql-connector-opensearch, 1.2.0-1.19      |
| Amazon Managed Service for Prometheus DataStream              | -                                                | flink-sql-connector-opensearch, 1.2.0-1.18      | flink-connector-prometheus, 1.0.0-1.19          | flink-connector-prometheus, 1.0.0-1.20          |
| Amazon SQS DataStream and Table API                           | -                                                | flink-sql-connector-opensearch, 1.2.0-1.18      | flink-connector-sqs, 5.0.0-1.19                 | flink-connector-sqs, 5.0.0-1.20                 |

To learn more about connectors in Amazon Managed Service for Apache Flink, see:

- [DataStream API connectors](how-connectors.md "how-connectors.md")
- [Table API connectors](how-table-connectors.md "how-table-connectors.md")

## Known issues

There is a known open source Apache Flink issue with the Apache Kafka connector in
Apache Flink 1.15. This issue is resolved in later versions of Apache Flink.

For more information, see [Known issues](flink-1-15-2.md#flink-1-15-known-issues "flink-1-15-2.md#flink-1-15-known-issues").
