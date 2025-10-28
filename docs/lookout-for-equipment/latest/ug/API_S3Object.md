On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# S3Object

Contains information about an S3 bucket.

## Contents

**Bucket**

The name of the specific S3 bucket.

Type: String

Length Constraints: Minimum length of 3. Maximum length of 63.

Pattern: `^[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9]$`

Required: Yes

**Key**

The AWS Key Management Service (AWS KMS key) key being used to encrypt the S3 object.
Without this key, data in the bucket is not accessible.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1024.

Pattern: `[\P{M}\p{M}]{1,1024}[^/]$`

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/lookoutequipment-2020-12-15/S3Object.md "../../../goto/SdkForCpp/lookoutequipment-2020-12-15/S3Object.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/S3Object.md "../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/S3Object.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/S3Object.md "../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/S3Object.md")
