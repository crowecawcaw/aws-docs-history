

# UpdatePipeSourceSelfManagedKafkaParameters
<a name="API_UpdatePipeSourceSelfManagedKafkaParameters"></a>

The parameters for using a self-managed Apache Kafka stream as a source.

A *self managed* cluster refers to any Apache Kafka cluster not hosted by AWS. This includes both clusters you manage yourself, as well as those hosted by a third-party provider, such as [Confluent Cloud](https://www.confluent.io/), [CloudKarafka](https://www.cloudkarafka.com/), or [Redpanda](https://redpanda.com/). For more information, see [Apache Kafka streams as a source](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-kafka.html) in the *Amazon EventBridge User Guide*.

## Contents
<a name="API_UpdatePipeSourceSelfManagedKafkaParameters_Contents"></a>

 ** BatchSize **   <a name="eventbridge-Type-UpdatePipeSourceSelfManagedKafkaParameters-BatchSize"></a>
The maximum number of records to include in each batch.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 10000.  
Required: No

 ** Credentials **   <a name="eventbridge-Type-UpdatePipeSourceSelfManagedKafkaParameters-Credentials"></a>
The credentials needed to access the resource.  
Type: [SelfManagedKafkaAccessConfigurationCredentials](API_SelfManagedKafkaAccessConfigurationCredentials.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** MaximumBatchingWindowInSeconds **   <a name="eventbridge-Type-UpdatePipeSourceSelfManagedKafkaParameters-MaximumBatchingWindowInSeconds"></a>
The maximum length of a time to wait for events.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 300.  
Required: No

 ** ServerRootCaCertificate **   <a name="eventbridge-Type-UpdatePipeSourceSelfManagedKafkaParameters-ServerRootCaCertificate"></a>
The ARN of the Secrets Manager secret used for certification.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1600.  
Pattern: `(^arn:aws([a-z]|\-)*:secretsmanager:([a-z]{2,4}((-gov)|(-de)|(-iso([a-z]?)))?-[a-z]+(-\d{1})?):(\d{12}):secret:.+)`   
Required: No

 ** Vpc **   <a name="eventbridge-Type-UpdatePipeSourceSelfManagedKafkaParameters-Vpc"></a>
This structure specifies the VPC subnets and security groups for the stream, and whether a public IP address is to be used.  
Type: [SelfManagedKafkaAccessConfigurationVpc](API_SelfManagedKafkaAccessConfigurationVpc.md) object  
Required: No

## See Also
<a name="API_UpdatePipeSourceSelfManagedKafkaParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pipes-2015-10-07/UpdatePipeSourceSelfManagedKafkaParameters) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pipes-2015-10-07/UpdatePipeSourceSelfManagedKafkaParameters) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pipes-2015-10-07/UpdatePipeSourceSelfManagedKafkaParameters) 