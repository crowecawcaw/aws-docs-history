

# RevisionConfig
<a name="API_RevisionConfig"></a>

The configuration for a web function revision, including code build settings and service configuration.

## Contents
<a name="API_RevisionConfig_Contents"></a>

 ** buildConfig **   <a name="lambdaweb-Type-RevisionConfig-buildConfig"></a>
The build configuration for the revision.  
Type: [BuildConfig](API_BuildConfig.md) object  
Required: Yes

 ** serviceConfig **   <a name="lambdaweb-Type-RevisionConfig-serviceConfig"></a>
The service configuration for the revision.  
Type: [ServiceConfig](API_ServiceConfig.md) object  
Required: Yes

 ** description **   <a name="lambdaweb-Type-RevisionConfig-description"></a>
A description of the revision.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Required: No

 ** kmsKeyArn **   <a name="lambdaweb-Type-RevisionConfig-kmsKeyArn"></a>
The Amazon Resource Name (ARN) of the AWS Key Management Service (AWS KMS) key used to encrypt the revision's code and environment variables.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:(aws[a-z-]*):kms:[a-z0-9-]+:[0-9]{12}:key/[a-z0-9-]+`   
Required: No

## See Also
<a name="API_RevisionConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-web-2025-03-07/RevisionConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-web-2025-03-07/RevisionConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-web-2025-03-07/RevisionConfig) 