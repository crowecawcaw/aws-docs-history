# NotificationConfiguration

A container for specifying the notification configuration of the bucket. If this element is empty,
 notifications are turned off for the bucket.


## Contents





**EventBridgeConfiguration** 


Enables delivery of events to Amazon EventBridge.


Type: [EventBridgeConfiguration](API_EventBridgeConfiguration.md "API_EventBridgeConfiguration.md") data type


Required: No




**LambdaFunctionConfigurations** 


Describes the AWS Lambda functions to invoke and the events for which to invoke them.


Type: Array of [LambdaFunctionConfiguration](API_LambdaFunctionConfiguration.md "API_LambdaFunctionConfiguration.md") data types


Required: No




**QueueConfigurations** 


The Amazon Simple Queue Service queues to publish messages to and the events for which to publish
 messages.


Type: Array of [QueueConfiguration](API_QueueConfiguration.md "API_QueueConfiguration.md") data types


Required: No




**TopicConfigurations** 


The topic to which notifications are sent and the events for which notifications are
 generated.


Type: Array of [TopicConfiguration](API_TopicConfiguration.md "API_TopicConfiguration.md") data types


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/NotificationConfiguration "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/NotificationConfiguration")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/NotificationConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/NotificationConfiguration")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/NotificationConfiguration "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/NotificationConfiguration")
