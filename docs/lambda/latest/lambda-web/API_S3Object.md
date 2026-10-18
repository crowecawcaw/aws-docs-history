

# S3Object
<a name="API_S3Object"></a>

The Amazon S3 location of a deployment artifact.

## Contents
<a name="API_S3Object_Contents"></a>

 ** bucket **   <a name="lambdaweb-Type-S3Object-bucket"></a>
The name of the Amazon S3 bucket.  
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 63.  
Pattern: `([a-z0-9][a-z0-9\.\-]{1,61}[a-z0-9])`   
Required: Yes

 ** key **   <a name="lambdaweb-Type-S3Object-key"></a>
The Amazon S3 object key.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Required: Yes

 ** versionId **   <a name="lambdaweb-Type-S3Object-versionId"></a>
The version ID of the Amazon S3 object.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Required: No

## See Also
<a name="API_S3Object_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-web-2025-03-07/S3Object) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-web-2025-03-07/S3Object) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-web-2025-03-07/S3Object) 