Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Java examples for Managed Service for Apache Flink

The following examples demonstrate how to create applications written in Java.

###### Note

Most of the examples are designed to run both locally, on your development machine
and your IDE of choice, and on Amazon Managed Service for Apache Flink. They demonstrate the mechanisms that you
can use to pass application parameters, and how to set the dependency correctly to
run the application in both environments with no changes.

This example illustrates how to define custom TypeInfo on your record or state
object to prevent serialization falling back to the less efficient Kryo
serialization. This is required, for example, when your objects contain a
`List` or `Map`. For more information, see [Data Types & Serialization](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/dev/datastream/fault-tolerance/serialization/types_serialization/#data-types--serialization "https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/dev/datastream/fault-tolerance/serialization/types_serialization/#data-types--serialization") in the Apache Flink documentation.
The example also shows how to test whether the serialization of your object
falls back to the less efficient Kryo serialization.

Code example: [CustomTypeInfo](https://github.com/aws-samples/amazon-managed-service-for-apache-flink-examples/tree/main/java/Serialization/CustomTypeInfo "https://github.com/aws-samples/amazon-managed-service-for-apache-flink-examples/tree/main/java/Serialization/CustomTypeInfo")

This example shows a simple application, reading from a Kinesis data stream and
writing to another Kinesis data stream, using the `DataStream` API. The
example demonstrates how to set up the file with the correct dependencies, build
the uber-JAR, and then parse the configuration parameters, so you can run the
application both locally, in your IDE, and on Amazon Managed Service for Apache Flink.

Code example: [GettingStarted](https://github.com/aws-samples/amazon-managed-service-for-apache-flink-examples/tree/main/java/GettingStarted "https://github.com/aws-samples/amazon-managed-service-for-apache-flink-examples/tree/main/java/GettingStarted")

This example shows a simple application using the `Table` API and
SQL. It demonstrates how to integrate the `DataStream` API with the
`Table` API or SQL in the same Java application. It also
demonstrates how to use the `DataGen` connector to generate random
test data from within the Flink application itself, not requiring an external
data generator.

Complete example: [GettingStartedTable](https://github.com/aws-samples/amazon-managed-service-for-apache-flink-examples/tree/main/java/GettingStartedTable "https://github.com/aws-samples/amazon-managed-service-for-apache-flink-examples/tree/main/java/GettingStartedTable")

This example demonstrates how to use the `DataStream` API's
`FileSink` to write JSON files to an S3 bucket.

Code example: [S3Sink](https://github.com/aws-samples/amazon-managed-service-for-apache-flink-examples/tree/main/java/S3Sink "https://github.com/aws-samples/amazon-managed-service-for-apache-flink-examples/tree/main/java/S3Sink")

This example demonstrates how to configure a source consuming from a Kinesis data stream, either using the standard consumer or EFO, and how
to set up a sink to the Kinesis data stream.

Code example: [KinesisConnectors](https://github.com/aws-samples/amazon-managed-service-for-apache-flink-examples/tree/main/java/KinesisConnectors "https://github.com/aws-samples/amazon-managed-service-for-apache-flink-examples/tree/main/java/KinesisConnectors")

This example shows how to send data to Amazon Data Firehose (formerly known as Kinesis Data Firehose).

Code example: [KinesisFirehoseSink](https://github.com/aws-samples/amazon-managed-service-for-apache-flink-examples/tree/main/java/KinesisFirehoseSink "https://github.com/aws-samples/amazon-managed-service-for-apache-flink-examples/tree/main/java/KinesisFirehoseSink")

This example demonstrates the use of the [Prometheus sink connector](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/datastream/prometheus/ "https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/datastream/prometheus/") to write time-series data to
Prometheus.

Code example: [PrometheusSink](https://github.com/aws-samples/amazon-managed-service-for-apache-flink-examples/tree/main/java/PrometheusSink "https://github.com/aws-samples/amazon-managed-service-for-apache-flink-examples/tree/main/java/PrometheusSink")

This example demonstrates four types of the windowing aggregation in the
`DataStream` API.

1. Sliding Window based on processing time
2. Sliding Window based on event time
3. Tumbling Window based on processing time
4. Tumbling Window based on event time
   Code example: [Windowing](https://github.com/aws-samples/amazon-managed-service-for-apache-flink-examples/tree/main/java/Windowing "https://github.com/aws-samples/amazon-managed-service-for-apache-flink-examples/tree/main/java/Windowing")

This example shows how to add custom metrics to your Flink application and
send them to CloudWatch metrics.

Code example: [CustomMetrics](https://github.com/dzikosc/amazon-managed-service-for-apache-flink-examples/tree/main/java/CustomMetrics "https://github.com/dzikosc/amazon-managed-service-for-apache-flink-examples/tree/main/java/CustomMetrics")

This example illustrates how you can use Kafka Configuration Providers to set
up a custom keystore and truststore with certificates for mTLS authentication
for the Kafka connector. This technique lets you load the required custom
certificates from Amazon S3 and the secrets from AWS Secrets Manager when the
application starts.

Code example: [Kafka-mTLS-Keystore-ConfigProviders](https://github.com/aws-samples/amazon-managed-service-for-apache-flink-examples/tree/main/java/KafkaConfigProviders/Kafka-mTLS-Keystore-ConfigProviders "https://github.com/aws-samples/amazon-managed-service-for-apache-flink-examples/tree/main/java/KafkaConfigProviders/Kafka-mTLS-Keystore-ConfigProviders")

This example illustrates how you can use Kafka Configuration Providers to
fetch credentials from AWS Secrets Manager and download the truststore from
Amazon S3 to set up SASL/SCRAM authentication on a Kafka connector. This
technique lets you load the required custom certificates from Amazon S3
and the secrets from AWS Secrets Manager when the application starts.

Code example: [Kafka-SASL_SSL-ConfigProviders](https://github.com/aws-samples/amazon-managed-service-for-apache-flink-examples/tree/main/java/KafkaConfigProviders/Kafka-SASL_SSL-ConfigProviders "https://github.com/aws-samples/amazon-managed-service-for-apache-flink-examples/tree/main/java/KafkaConfigProviders/Kafka-SASL_SSL-ConfigProviders")

This example illustrates how you can use Kafka Configuration Providers in
Table API /SQL to set up a custom keystore and truststore with certificates for
mTLS authentication for the Kafka connector. This technique lets you load the
required custom certificates from Amazon S3 and the secrets from AWS Secrets Manager when
the application starts.

Code example: [Kafka-mTLS-Keystore-Sql-ConfigProviders](https://github.com/aws-samples/amazon-managed-service-for-apache-flink-examples/tree/main/java/KafkaConfigProviders/Kafka-mTLS-Keystore-Sql-ConfigProviders "https://github.com/aws-samples/amazon-managed-service-for-apache-flink-examples/tree/main/java/KafkaConfigProviders/Kafka-mTLS-Keystore-Sql-ConfigProviders")

This example illustrates how to leverage [Side Outputs](https://nightlies.apache.org/flink/flink-docs-master/docs/dev/datastream/side_output/ "https://nightlies.apache.org/flink/flink-docs-master/docs/dev/datastream/side_output/") in Apache Flink for splitting a stream on specified
attributes. This pattern is particularly useful when trying to implement the
concept of Dead Letter Queues (DLQ) in streaming applications.

Code example: [SideOutputs](https://github.com/aws-samples/amazon-managed-service-for-apache-flink-examples/tree/main/java/SideOutputs "https://github.com/aws-samples/amazon-managed-service-for-apache-flink-examples/tree/main/java/SideOutputs")

This example illustrates how to use [Apache Flink Async I/O](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/dev/datastream/operators/asyncio/ "https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/dev/datastream/operators/asyncio/") to call an external endpoint in a
non-blocking way, with retries on recoverable errors.

Code example: [AsyncIO](https://github.com/aws-samples/amazon-managed-service-for-apache-flink-examples/tree/main/java/AsyncIO "https://github.com/aws-samples/amazon-managed-service-for-apache-flink-examples/tree/main/java/AsyncIO")
