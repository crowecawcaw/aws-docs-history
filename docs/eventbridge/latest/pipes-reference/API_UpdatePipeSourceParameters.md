# UpdatePipeSourceParameters

The parameters required to set up a source for your pipe.

## Contents

**ActiveMQBrokerParameters**

The parameters for using an Active MQ broker as a source.

Type: [UpdatePipeSourceActiveMQBrokerParameters](API_UpdatePipeSourceActiveMQBrokerParameters.md "API_UpdatePipeSourceActiveMQBrokerParameters.md") object

Required: No

**DynamoDBStreamParameters**

The parameters for using a DynamoDB stream as a source.

Type: [UpdatePipeSourceDynamoDBStreamParameters](API_UpdatePipeSourceDynamoDBStreamParameters.md "API_UpdatePipeSourceDynamoDBStreamParameters.md") object

Required: No

**FilterCriteria**

The collection of event patterns used to filter events.

To remove a filter, specify a `FilterCriteria` object with an empty array of `Filter` objects.

For more information, see [Events and Event
Patterns](../userguide/eventbridge-and-event-patterns.md "../userguide/eventbridge-and-event-patterns.md") in the _Amazon EventBridge User Guide_.

Type: [FilterCriteria](API_FilterCriteria.md "API_FilterCriteria.md") object

Required: No

**KinesisStreamParameters**

The parameters for using a Kinesis stream as a source.

Type: [UpdatePipeSourceKinesisStreamParameters](API_UpdatePipeSourceKinesisStreamParameters.md "API_UpdatePipeSourceKinesisStreamParameters.md") object

Required: No

**ManagedStreamingKafkaParameters**

The parameters for using an MSK stream as a source.

Type: [UpdatePipeSourceManagedStreamingKafkaParameters](API_UpdatePipeSourceManagedStreamingKafkaParameters.md "API_UpdatePipeSourceManagedStreamingKafkaParameters.md") object

Required: No

**RabbitMQBrokerParameters**

The parameters for using a Rabbit MQ broker as a source.

Type: [UpdatePipeSourceRabbitMQBrokerParameters](API_UpdatePipeSourceRabbitMQBrokerParameters.md "API_UpdatePipeSourceRabbitMQBrokerParameters.md") object

Required: No

**SelfManagedKafkaParameters**

The parameters for using a self-managed Apache Kafka stream as a source.

A _self managed_ cluster refers to any Apache Kafka cluster not hosted by AWS.
This includes both clusters you manage yourself, as well as those hosted by a third-party
provider, such as [Confluent
Cloud](https://www.confluent.io/ "https://www.confluent.io/"), [CloudKarafka](https://www.cloudkarafka.com/ "https://www.cloudkarafka.com/"), or [Redpanda](https://redpanda.com/ "https://redpanda.com/"). For more information, see [Apache Kafka streams as a source](../userguide/eb-pipes-kafka.md "../userguide/eb-pipes-kafka.md") in the _Amazon EventBridge User Guide_.

Type: [UpdatePipeSourceSelfManagedKafkaParameters](API_UpdatePipeSourceSelfManagedKafkaParameters.md "API_UpdatePipeSourceSelfManagedKafkaParameters.md") object

Required: No

**SqsQueueParameters**

The parameters for using a Amazon SQS stream as a source.

Type: [UpdatePipeSourceSqsQueueParameters](API_UpdatePipeSourceSqsQueueParameters.md "API_UpdatePipeSourceSqsQueueParameters.md") object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/pipes-2015-10-07/UpdatePipeSourceParameters.md "../../../goto/SdkForCpp/pipes-2015-10-07/UpdatePipeSourceParameters.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/pipes-2015-10-07/UpdatePipeSourceParameters.md "../../../goto/SdkForJavaV2/pipes-2015-10-07/UpdatePipeSourceParameters.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/pipes-2015-10-07/UpdatePipeSourceParameters.md "../../../goto/SdkForRubyV3/pipes-2015-10-07/UpdatePipeSourceParameters.md")
