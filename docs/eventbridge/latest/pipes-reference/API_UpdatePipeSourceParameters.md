

# UpdatePipeSourceParameters
<a name="API_UpdatePipeSourceParameters"></a>

The parameters required to set up a source for your pipe.

## Contents
<a name="API_UpdatePipeSourceParameters_Contents"></a>

 ** ActiveMQBrokerParameters **   <a name="eventbridge-Type-UpdatePipeSourceParameters-ActiveMQBrokerParameters"></a>
The parameters for using an Active MQ broker as a source.  
Type: [UpdatePipeSourceActiveMQBrokerParameters](API_UpdatePipeSourceActiveMQBrokerParameters.md) object  
Required: No

 ** DynamoDBStreamParameters **   <a name="eventbridge-Type-UpdatePipeSourceParameters-DynamoDBStreamParameters"></a>
The parameters for using a DynamoDB stream as a source.  
Type: [UpdatePipeSourceDynamoDBStreamParameters](API_UpdatePipeSourceDynamoDBStreamParameters.md) object  
Required: No

 ** FilterCriteria **   <a name="eventbridge-Type-UpdatePipeSourceParameters-FilterCriteria"></a>
The collection of event patterns used to filter events.  
To remove a filter, specify a `FilterCriteria` object with an empty array of `Filter` objects.  
For more information, see [Events and Event Patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-and-event-patterns.html) in the *Amazon EventBridge User Guide*.  
Type: [FilterCriteria](API_FilterCriteria.md) object  
Required: No

 ** KinesisStreamParameters **   <a name="eventbridge-Type-UpdatePipeSourceParameters-KinesisStreamParameters"></a>
The parameters for using a Kinesis stream as a source.  
Type: [UpdatePipeSourceKinesisStreamParameters](API_UpdatePipeSourceKinesisStreamParameters.md) object  
Required: No

 ** ManagedStreamingKafkaParameters **   <a name="eventbridge-Type-UpdatePipeSourceParameters-ManagedStreamingKafkaParameters"></a>
The parameters for using an MSK stream as a source.  
Type: [UpdatePipeSourceManagedStreamingKafkaParameters](API_UpdatePipeSourceManagedStreamingKafkaParameters.md) object  
Required: No

 ** RabbitMQBrokerParameters **   <a name="eventbridge-Type-UpdatePipeSourceParameters-RabbitMQBrokerParameters"></a>
The parameters for using a Rabbit MQ broker as a source.  
Type: [UpdatePipeSourceRabbitMQBrokerParameters](API_UpdatePipeSourceRabbitMQBrokerParameters.md) object  
Required: No

 ** SelfManagedKafkaParameters **   <a name="eventbridge-Type-UpdatePipeSourceParameters-SelfManagedKafkaParameters"></a>
The parameters for using a self-managed Apache Kafka stream as a source.  
A *self managed* cluster refers to any Apache Kafka cluster not hosted by AWS. This includes both clusters you manage yourself, as well as those hosted by a third-party provider, such as [Confluent Cloud](https://www.confluent.io/), [CloudKarafka](https://www.cloudkarafka.com/), or [Redpanda](https://redpanda.com/). For more information, see [Apache Kafka streams as a source](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-kafka.html) in the *Amazon EventBridge User Guide*.  
Type: [UpdatePipeSourceSelfManagedKafkaParameters](API_UpdatePipeSourceSelfManagedKafkaParameters.md) object  
Required: No

 ** SqsQueueParameters **   <a name="eventbridge-Type-UpdatePipeSourceParameters-SqsQueueParameters"></a>
The parameters for using a Amazon SQS stream as a source.  
Type: [UpdatePipeSourceSqsQueueParameters](API_UpdatePipeSourceSqsQueueParameters.md) object  
Required: No

## See Also
<a name="API_UpdatePipeSourceParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pipes-2015-10-07/UpdatePipeSourceParameters) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pipes-2015-10-07/UpdatePipeSourceParameters) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pipes-2015-10-07/UpdatePipeSourceParameters) 