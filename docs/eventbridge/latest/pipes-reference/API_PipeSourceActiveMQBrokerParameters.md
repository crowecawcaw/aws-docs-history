

# PipeSourceActiveMQBrokerParameters
<a name="API_PipeSourceActiveMQBrokerParameters"></a>

The parameters for using an Active MQ broker as a source.

## Contents
<a name="API_PipeSourceActiveMQBrokerParameters_Contents"></a>

 ** Credentials **   <a name="eventbridge-Type-PipeSourceActiveMQBrokerParameters-Credentials"></a>
The credentials needed to access the resource.  
Type: [MQBrokerAccessCredentials](API_MQBrokerAccessCredentials.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** QueueName **   <a name="eventbridge-Type-PipeSourceActiveMQBrokerParameters-QueueName"></a>
The name of the destination queue to consume.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1000.  
Pattern: `[\s\S]*`   
Required: Yes

 ** BatchSize **   <a name="eventbridge-Type-PipeSourceActiveMQBrokerParameters-BatchSize"></a>
The maximum number of records to include in each batch.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 10000.  
Required: No

 ** MaximumBatchingWindowInSeconds **   <a name="eventbridge-Type-PipeSourceActiveMQBrokerParameters-MaximumBatchingWindowInSeconds"></a>
The maximum length of a time to wait for events.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 300.  
Required: No

## See Also
<a name="API_PipeSourceActiveMQBrokerParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pipes-2015-10-07/PipeSourceActiveMQBrokerParameters) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pipes-2015-10-07/PipeSourceActiveMQBrokerParameters) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pipes-2015-10-07/PipeSourceActiveMQBrokerParameters) 