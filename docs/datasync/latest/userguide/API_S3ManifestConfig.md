# S3ManifestConfig

Specifies the S3 bucket where you're hosting the manifest that you want AWS DataSync to use. For more information and configuration examples, see [Specifying what DataSync transfers by using a manifest](transferring-with-manifest.md "transferring-with-manifest.md").

## Contents

**BucketAccessRoleArn**

Specifies the AWS Identity and Access Management (IAM) role that allows DataSync to access your manifest. For more information, see [Providing DataSync access to your manifest](transferring-with-manifest.md#transferring-with-manifest-access "transferring-with-manifest.md#transferring-with-manifest-access").

Type: String

Length Constraints: Maximum length of 2048.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):iam::[0-9]{12}:role/.*$`

Required: Yes

**ManifestObjectPath**

Specifies the Amazon S3 object key of your manifest. This can include a prefix
(for example, `prefix/my-manifest.csv`).

Type: String

Length Constraints: Maximum length of 4096.

Pattern: `^[a-zA-Z0-9_\-\+\./\(\)\p{Zs}]*$`

Required: Yes

**S3BucketArn**

Specifies the Amazon Resource Name (ARN) of the S3 bucket where you're hosting your
manifest.

Type: String

Length Constraints: Maximum length of 268.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):s3:[a-z\-0-9]*:[0-9]{12}:accesspoint[/:][a-zA-Z0-9\-.]{1,63}$|^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):s3-outposts:[a-z\-0-9]+:[0-9]{12}:outpost[/:][a-zA-Z0-9\-]{1,63}[/:]accesspoint[/:][a-zA-Z0-9\-]{1,63}$|^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):s3:::[a-zA-Z0-9.\-_]{1,255}$`

Required: Yes

**ManifestObjectVersionId**

Specifies the object version ID of the manifest that you want DataSync to use.
If you don't set this, DataSync uses the latest version of the object.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^.+$`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/S3ManifestConfig.md "../../../goto/SdkForCpp/datasync-2018-11-09/S3ManifestConfig.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/S3ManifestConfig.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/S3ManifestConfig.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/S3ManifestConfig.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/S3ManifestConfig.md")
