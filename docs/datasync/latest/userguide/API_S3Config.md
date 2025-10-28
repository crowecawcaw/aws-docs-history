# S3Config

Specifies the Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that DataSync uses to access your S3 bucket.

For more information, see [Providing
DataSync access to S3 buckets](create-s3-location.md#create-s3-location-access "create-s3-location.md#create-s3-location-access").

## Contents

**BucketAccessRoleArn**

Specifies the ARN of the IAM role that DataSync uses to access
your S3 bucket.

Type: String

Length Constraints: Maximum length of 2048.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):iam::[0-9]{12}:role/.*$`

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/S3Config.md "../../../goto/SdkForCpp/datasync-2018-11-09/S3Config.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/S3Config.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/S3Config.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/S3Config.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/S3Config.md")
