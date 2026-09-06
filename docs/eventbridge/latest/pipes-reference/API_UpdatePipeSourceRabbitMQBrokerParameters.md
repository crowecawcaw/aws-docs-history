

# UpdatePipeSourceRabbitMQBrokerParameters
<a name="API_UpdatePipeSourceRabbitMQBrokerParameters"></a>

The parameters for using a Rabbit MQ broker as a source.

## Contents
<a name="API_UpdatePipeSourceRabbitMQBrokerParameters_Contents"></a>

 ** Credentials **   <a name="eventbridge-Type-UpdatePipeSourceRabbitMQBrokerParameters-Credentials"></a>
The credentials needed to access the resource.  
Type: [MQBrokerAccessCredentials](API_MQBrokerAccessCredentials.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** BatchSize **   <a name="eventbridge-Type-UpdatePipeSourceRabbitMQBrokerParameters-BatchSize"></a>
The maximum number of records to include in each batch.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 10000.  
Required: No

 ** MaximumBatchingWindowInSeconds **   <a name="eventbridge-Type-UpdatePipeSourceRabbitMQBrokerParameters-MaximumBatchingWindowInSeconds"></a>
The maximum length of a time to wait for events.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 300.  
Required: No

## See Also
<a name="API_UpdatePipeSourceRabbitMQBrokerParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pipes-2015-10-07/UpdatePipeSourceRabbitMQBrokerParameters) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pipes-2015-10-07/UpdatePipeSourceRabbitMQBrokerParameters) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pipes-2015-10-07/UpdatePipeSourceRabbitMQBrokerParameters) 