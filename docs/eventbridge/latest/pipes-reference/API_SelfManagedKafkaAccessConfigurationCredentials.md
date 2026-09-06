

# SelfManagedKafkaAccessConfigurationCredentials
<a name="API_SelfManagedKafkaAccessConfigurationCredentials"></a>

The AWS Secrets Manager secret that stores your stream credentials.

## Contents
<a name="API_SelfManagedKafkaAccessConfigurationCredentials_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** BasicAuth **   <a name="eventbridge-Type-SelfManagedKafkaAccessConfigurationCredentials-BasicAuth"></a>
The ARN of the Secrets Manager secret.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1600.  
Pattern: `(^arn:aws([a-z]|\-)*:secretsmanager:([a-z]{2,4}((-gov)|(-de)|(-iso([a-z]?)))?-[a-z]+(-\d{1})?):(\d{12}):secret:.+)`   
Required: No

 ** ClientCertificateTlsAuth **   <a name="eventbridge-Type-SelfManagedKafkaAccessConfigurationCredentials-ClientCertificateTlsAuth"></a>
The ARN of the Secrets Manager secret.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1600.  
Pattern: `(^arn:aws([a-z]|\-)*:secretsmanager:([a-z]{2,4}((-gov)|(-de)|(-iso([a-z]?)))?-[a-z]+(-\d{1})?):(\d{12}):secret:.+)`   
Required: No

 ** SaslScram256Auth **   <a name="eventbridge-Type-SelfManagedKafkaAccessConfigurationCredentials-SaslScram256Auth"></a>
The ARN of the Secrets Manager secret.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1600.  
Pattern: `(^arn:aws([a-z]|\-)*:secretsmanager:([a-z]{2,4}((-gov)|(-de)|(-iso([a-z]?)))?-[a-z]+(-\d{1})?):(\d{12}):secret:.+)`   
Required: No

 ** SaslScram512Auth **   <a name="eventbridge-Type-SelfManagedKafkaAccessConfigurationCredentials-SaslScram512Auth"></a>
The ARN of the Secrets Manager secret.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1600.  
Pattern: `(^arn:aws([a-z]|\-)*:secretsmanager:([a-z]{2,4}((-gov)|(-de)|(-iso([a-z]?)))?-[a-z]+(-\d{1})?):(\d{12}):secret:.+)`   
Required: No

## See Also
<a name="API_SelfManagedKafkaAccessConfigurationCredentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pipes-2015-10-07/SelfManagedKafkaAccessConfigurationCredentials) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pipes-2015-10-07/SelfManagedKafkaAccessConfigurationCredentials) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pipes-2015-10-07/SelfManagedKafkaAccessConfigurationCredentials) 