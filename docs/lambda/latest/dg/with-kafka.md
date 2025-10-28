# Using Lambda with self-managed Apache Kafka

This topic describes how to use Lambda with a self-managed Kafka cluster. In AWS terminology, a self-managed
cluster includes non-AWS hosted Kafka clusters. For example, you can host your Kafka cluster with a cloud provider
such as [Confluent Cloud](https://www.confluent.io/confluent-cloud/ "https://www.confluent.io/confluent-cloud/").

Apache Kafka as an event source operates similarly to using Amazon Simple Queue Service (Amazon SQS) or Amazon Kinesis. Lambda internally polls for
new messages from the event source and then synchronously invokes the target Lambda function. Lambda reads the
messages in batches and provides these to your function as an event payload. The maximum batch size is configurable
(the default is 100 messages). For more information, see [Batching behavior](invocation-eventsourcemapping.md#invocation-eventsourcemapping-batching "invocation-eventsourcemapping.md#invocation-eventsourcemapping-batching").

To optimize the throughput of your self-managed Apache Kafka event source mapping, configure provisioned mode. In provisioned
mode, you can define the minimum and maximum number of event pollers allocated to your event source mapping.
This can improve the ability of your event source mapping to handle unexpected message spikes. For more
information, see [provisioned mode](with-kafka-process.md#services-kafka-provisioned-mode "with-kafka-process.md#services-kafka-provisioned-mode").

###### Warning

Lambda event source mappings process each event at least once, and duplicate processing of records can occur. To avoid potential issues
related to duplicate events, we strongly recommend that you make your function code idempotent. To learn more, see [How do I make my Lambda function idempotent](https://repost.aws/knowledge-center/lambda-function-idempotent "https://repost.aws/knowledge-center/lambda-function-idempotent")
in the AWS Knowledge Center.

For Kafka-based event sources, Lambda supports processing control parameters, such as batching windows
and batch size. For more information, see [Batching behavior](invocation-eventsourcemapping.md#invocation-eventsourcemapping-batching "invocation-eventsourcemapping.md#invocation-eventsourcemapping-batching").

For an example of how to use self-managed Kafka as an event source, see [Using self-hosted Apache Kafka as an
event source for AWS Lambda](https://aws.amazon.com/blogs/compute/using-self-hosted-apache-kafka-as-an-event-source-for-aws-lambda/ "https://aws.amazon.com/blogs/compute/using-self-hosted-apache-kafka-as-an-event-source-for-aws-lambda/") on the AWS Compute Blog.

###### Topics

- [Example event](#smaa-sample-event "#smaa-sample-event")
- [Configuring self-managed Apache Kafka event sources for Lambda](with-kafka-configure.md "with-kafka-configure.md")
- [Processing self-managed Apache Kafka messages with Lambda](with-kafka-process.md "with-kafka-process.md")
- [Using event filtering with a self-managed Apache Kafka event source](with-kafka-filtering.md "with-kafka-filtering.md")
- [Capturing discarded batches for a self-managed Apache Kafka event source](with-kafka-on-failure.md "with-kafka-on-failure.md")
- [Troubleshooting self-managed Apache Kafka event source mapping errors](with-kafka-troubleshoot.md "with-kafka-troubleshoot.md")

## Example event

Lambda sends the batch of messages in the event parameter when it invokes your Lambda function. The event payload
contains an array of messages. Each array item contains details of the Kafka topic and Kafka partition identifier,
together with a timestamp and a base64-encoded message.

```
{
   "eventSource": "SelfManagedKafka",
   "bootstrapServers":"b-2.demo-cluster-1.a1bcde.c1.kafka.us-east-1.amazonaws.com:9092,b-1.demo-cluster-1.a1bcde.c1.kafka.us-east-1.amazonaws.com:9092",
   "records":{
      "mytopic-0":[
         {
            "topic":"mytopic",
            "partition":0,
            "offset":15,
            "timestamp":1545084650987,
            "timestampType":"CREATE_TIME",
            "key":"abcDEFghiJKLmnoPQRstuVWXyz1234==",
            "value":"SGVsbG8sIHRoaXMgaXMgYSB0ZXN0Lg==",
            "headers":[
               {
                  "headerKey":[
                     104,
                     101,
                     97,
                     100,
                     101,
                     114,
                     86,
                     97,
                     108,
                     117,
                     101
                  ]
               }
            ]
         }
      ]
   }
}
```
