# Amazon EventBridge Pipes sources

EventBridge Pipes receives event data from a variety of sources, applies optional filters and
enrichments to that data, and sends it to a destination.

If a source enforces order to the events sent to EventBridge Pipes, that order is maintained throughout the entire process to the destination.

The following AWS services can be specified as sources for EventBridge Pipes:

- [Amazon DynamoDB stream](eb-pipes-dynamodb.md "eb-pipes-dynamodb.md")
- [Amazon Kinesis stream](eb-pipes-kinesis.md "eb-pipes-kinesis.md")
- [Amazon MQ broker](eb-pipes-mq.md "eb-pipes-mq.md")
- [Amazon MSK stream](eb-pipes-msk.md "eb-pipes-msk.md")
- [Amazon SQS queue](eb-pipes-sqs.md "eb-pipes-sqs.md")
- [Apache Kafka stream](eb-pipes-kafka.md "eb-pipes-kafka.md")

When you specify an Apache Kafka stream as a pipe source, you can specify an Apache Kafka
stream that you manage yourself, or one managed by a third-party provider such as:

    + [Confluent Cloud](https://www.confluent.io/ "https://www.confluent.io/")
    + [CloudKarafka](https://www.cloudkarafka.com/ "https://www.cloudkarafka.com/")
    + [Redpanda](https://redpanda.com/ "https://redpanda.com/")
