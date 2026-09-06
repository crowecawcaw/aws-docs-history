

# Encryption
<a name="API_Encryption"></a>

Defines the encryption configuration for S3 Table integrations, including the encryption algorithm and KMS key settings.

## Contents
<a name="API_Encryption_Contents"></a>

 ** SseAlgorithm **   <a name="cwoa-Type-Encryption-SseAlgorithm"></a>
The server-side encryption algorithm used for encrypting data in the S3 Table integration.  
Type: String  
Valid Values: `aws:kms | AES256`   
Required: Yes

 ** KmsKeyArn **   <a name="cwoa-Type-Encryption-KmsKeyArn"></a>
The Amazon Resource Name (ARN) of the KMS key used for encryption when using customer-managed keys.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1011.  
Pattern: `arn:aws([a-z0-9\-]+)?:([a-zA-Z0-9\-]+):([a-z0-9\-]+)?:([0-9]{12})?:(.+)`   
Required: No

## See Also
<a name="API_Encryption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/Encryption) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/Encryption) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/Encryption) 