

# PipeSourceManagedStreamingKafkaParameters
<a name="API_PipeSourceManagedStreamingKafkaParameters"></a>

The parameters for using an MSK stream as a source.

## Contents
<a name="API_PipeSourceManagedStreamingKafkaParameters_Contents"></a>

 ** TopicName **   <a name="eventbridge-Type-PipeSourceManagedStreamingKafkaParameters-TopicName"></a>
The name of the topic that the pipe will read from.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 249.  
Pattern: `[^.]([a-zA-Z0-9\-_.]+)`   
Required: Yes

 ** BatchSize **   <a name="eventbridge-Type-PipeSourceManagedStreamingKafkaParameters-BatchSize"></a>
The maximum number of records to include in each batch.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 10000.  
Required: No

 ** ConsumerGroupID **   <a name="eventbridge-Type-PipeSourceManagedStreamingKafkaParameters-ConsumerGroupID"></a>
The name of the destination queue to consume.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `[a-zA-Z0-9-\/*:_+=.@-]*`   
Required: No

 ** Credentials **   <a name="eventbridge-Type-PipeSourceManagedStreamingKafkaParameters-Credentials"></a>
The credentials needed to access the resource.  
Type: [MSKAccessCredentials](API_MSKAccessCredentials.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** MaximumBatchingWindowInSeconds **   <a name="eventbridge-Type-PipeSourceManagedStreamingKafkaParameters-MaximumBatchingWindowInSeconds"></a>
The maximum length of a time to wait for events.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 300.  
Required: No

 ** StartingPosition **   <a name="eventbridge-Type-PipeSourceManagedStreamingKafkaParameters-StartingPosition"></a>
The position in a stream from which to start reading.  
Type: String  
Valid Values: `TRIM_HORIZON | LATEST`   
Required: No

## See Also
<a name="API_PipeSourceManagedStreamingKafkaParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pipes-2015-10-07/PipeSourceManagedStreamingKafkaParameters) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pipes-2015-10-07/PipeSourceManagedStreamingKafkaParameters) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pipes-2015-10-07/PipeSourceManagedStreamingKafkaParameters) 