

# What is Amazon Kinesis Data Streams?

You can use Amazon Kinesis Data Streams to collect and process large [streams](https://aws.amazon.com/streaming-data/) of data records in real time. You can create data-processing applications, known as *consumers*. A consumer reads data from a *data stream* as data records. You can send the processed records to dashboards, use them to generate alerts, dynamically change pricing and advertising strategies, or send data to a variety of other AWS services.

A consumer is either a *stream consumer*, which reads the stream directly, or a *queue consumer*, which consumes the stream through a queue. The two suit different kinds of processing.

A *stream consumer* reads the records of a shard in order, which suits *stateful* processing, where processing one record depends on the records before it, for use cases such as live analytics, personalization, and anomaly and pattern detection. Each shard is processed by one stream consumer instance at a time, which preserves the order of the records in that shard so that the stream consumer can keep an accurate state.

A *queue consumer* receives each record independently, which suits *stateless* processing, for use cases such as microservice integration, order processing, and per-record inference. Queue consumer instances do not lease shards, so you add instances to process more records in parallel. A queue delivers each record at least once and does not necessarily deliver records in the order that producers wrote them to the stream, so design your queue consumer to be idempotent, so that processing the same record more than once is safe. One record that fails does not hold up the ones behind it.

A stream and its queues carry the same records, so both kinds of consumer can process the same data at the same time. You can also have Kinesis Data Streams deliver the data for you, without running a consumer, to streaming tables on Apache Iceberg or to Amazon S3. For more information, see [Read data from Kinesis data streams](building-consumers.md), [Consume records from a stream with queues](consuming-with-queues.md), and [Streaming tables and S3 delivery for Amazon Kinesis Data Streams](data-delivery.md).

For information about Kinesis Data Streams features and pricing, see [Amazon Kinesis Data Streams](https://aws.amazon.com/kinesis/streams/).

Kinesis Data Streams is part of the Kinesis streaming data platform, along with [Firehose](https://docs.aws.amazon.com/firehose/latest/dev/), [Kinesis Video Streams](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/), and [Managed Service for Apache Flink](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/).

For more information about AWS big data solutions, see [Big Data on AWS](https://aws.amazon.com/big-data/). For more information about AWS streaming data solutions, see [What is Streaming Data?](https://aws.amazon.com/streaming-data/).

**Topics**
+ [What can I do with Kinesis Data Streams?](#use-service-for-what)
+ [Benefits of using Kinesis Data Streams](#using-the-service)
+ [Related services](#related-services)

## What can I do with Kinesis Data Streams?
<a name="use-service-for-what"></a>

You can use Kinesis Data Streams for rapid and continuous data intake and aggregation. The type of data used can include IT infrastructure log data, application logs, social media, market data feeds, web clickstream data, and business events such as orders, payments, and sign-ups. Records are available to consumers within a second of being written, so you can process them in real time.

The following are typical scenarios for using Kinesis Data Streams:

Accelerated log and data feed intake and processing  
You can have producers push data directly into a stream. For example, push system and application logs and they are available for processing in seconds. This prevents the log data from being lost if the front end or application server fails. Kinesis Data Streams provides accelerated data feed intake because you don't batch the data on the servers before you submit it for intake.

Real-time metrics and reporting  
You can use data collected into Kinesis Data Streams for simple data analysis and reporting in real time. For example, your data-processing application can work on metrics and reporting for system and application logs as the data is streaming in, rather than wait to receive batches of data.

Real-time data analytics  
This combines the power of parallel processing with the value of real-time data. For example, process website clickstreams in real time, and then analyze site usability engagement using multiple different consumers running in parallel.

Complex stream processing  
You can create Directed Acyclic Graphs (DAGs) of consumers and data streams. This typically involves putting data from multiple consumers into another stream for downstream processing by a different consumer.

Work distribution and background processing  
You can consume a stream through a queue to distribute records as units of work across many workers. For example, handle each record as an order to fulfill, a background job to run, or a notification to send. A record that a worker cannot process does not hold up the records behind it.

Continuous delivery to a data lake  
You can have Kinesis Data Streams deliver records to streaming tables on Apache Iceberg or to general purpose Amazon S3 buckets, with no consumer to run and no infrastructure to manage. For example, land card transactions as queryable Iceberg tables for later analysis while a consumer processes the same records in real time.

## Benefits of using Kinesis Data Streams
<a name="using-the-service"></a>

Kinesis Data Streams durably stores the records your producers write and makes them available for consumption in real time. The delay between the time a record is put into the stream and the time it can be retrieved is typically less than 1 second. In other words, a consumer can start processing the data almost immediately after it is added, whether it reads the stream directly or receives the records through a queue. The managed service aspect of Kinesis Data Streams relieves you of the operational burden of creating and running a data intake pipeline. The elasticity of Kinesis Data Streams enables you to scale the stream up or down, so that you never lose data records before they expire.

Multiple consumers can consume the same records, so that multiple actions can take place concurrently and independently, and managed data delivery can land the same records in streaming tables or Amazon S3. For example, for a stream of customer orders, a stream consumer can read the stream directly to calculate running revenue aggregates, which depend on the sequence of the records, and update an Amazon DynamoDB table that a dashboard reads for up-to-the-minute reports. At the same time, a queue consumer can receive the same orders through a queue and fulfill each one independently, while managed data delivery lands the same orders as queryable Iceberg tables for later analysis.

The Kinesis Client Library enables fault-tolerant consumption of data from streams and provides scaling support for stream consumers. For more information, see [Use Kinesis Client Library](kcl.md).

When you consume through a queue, you don't need to use the Kinesis Client Library. The queue tracks the delivery state of each record on the server, so a queue consumer does not coordinate work across its instances, and you add instances to process more records in parallel. For more information, see [Consume records from a stream with queues](consuming-with-queues.md).

## Related services
<a name="related-services"></a>

For information about using Amazon EMR clusters to read and process Kinesis data streams directly, see [Kinesis Connector](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-kinesis.html).