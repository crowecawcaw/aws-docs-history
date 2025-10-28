# DynamoDB Streams and Apache Flink

You can consume Amazon DynamoDB Streams records with Apache Flink. With [Amazon Managed Service for Apache Flink](https://aws.amazon.com/managed-service-apache-flink/ "https://aws.amazon.com/managed-service-apache-flink/"), you can
transform and analyze streaming data in real time using Apache Flink. Apache Flink is an
open-source stream processing framework for processing real-time data. The Amazon DynamoDB Streams
connector for Apache Flink simplifies building and managing Apache Flink workloads and
allows you to integrate applications with other AWS services.

Amazon Managed Service for Apache Flink helps you to quickly build end-to-end stream processing applications for log
analytics, clickstream analytics, Internet of Things (IoT), ad tech, gaming, and more. The
four most common use cases are streaming extract-transform-load (ETL), event driven
applications, responsive real-time analytics, and interactive querying of data streams. For
more information on writing to Apache Flink from Amazon DynamoDB Streams, see [Amazon DynamoDB Streams Connector](https://nightlies.apache.org/flink/flink-docs-master/docs/connectors/datastream/dynamodb/ "https://nightlies.apache.org/flink/flink-docs-master/docs/connectors/datastream/dynamodb/").

## Using the ShardFilter parameter with DynamoDB Streams

connector for Apache Flink

Amazon DynamoDB Streams supports the `ShardFilter` parameter in the
`DescribeStream` API to find a subset of shards. By specifying a parent
shard in the request, DynamoDB Streams will return its immediate child shards. You can use the
`ShardFilter` parameter to quickly discover child shards after a parent
shard has been closed, making your stream processing applications more responsive and
cost-effective.

Amazon Managed Service for Apache Flink supports the `ShardFilter` parameter when reading from DynamoDB Streams. To
use this feature, you must request access to a special version of the Flink connector
that includes `ShardFilter` support. To get started, open a support case in
the AWS Support Center and request access to these binaries. For more information about
using DynamoDB Streams with Apache Flink, see [Reading and processing a stream](Streams.md#Streams.Processing "Streams.md#Streams.Processing") in the DynamoDB
Developer Guide.
