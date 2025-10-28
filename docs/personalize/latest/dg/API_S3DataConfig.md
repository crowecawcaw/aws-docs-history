# S3DataConfig

The configuration details of an Amazon S3 input or output bucket.

## Contents

**path**

The file path of the Amazon S3 bucket.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `(s3|http|https)://.+`

Required: Yes

**kmsKeyArn**

The Amazon Resource Name (ARN) of the AWS Key Management Service (KMS) key that Amazon Personalize uses to
encrypt or decrypt the input and output files.

Type: String

Length Constraints: Maximum length of 2048.

Pattern: `arn:aws.*:kms:.*:[0-9]{12}:key/.*`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/S3DataConfig.md "../../../goto/SdkForCpp/personalize-2018-05-22/S3DataConfig.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/S3DataConfig.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/S3DataConfig.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/S3DataConfig.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/S3DataConfig.md")
