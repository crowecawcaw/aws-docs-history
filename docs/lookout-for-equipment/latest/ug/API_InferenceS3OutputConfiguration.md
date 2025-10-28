On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# InferenceS3OutputConfiguration

Specifies configuration information for the output results from the inference,
including output S3 location.

## Contents

**Bucket**

The bucket containing the output results from the inference

Type: String

Length Constraints: Minimum length of 3. Maximum length of 63.

Pattern: `^[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9]$`

Required: Yes

**Prefix**

The prefix for the S3 bucket used for the output results from the inference.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 1024.

Pattern: `(^$)|([\u0009\u000A\u000D\u0020-\u00FF]{1,1023}/$)`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/lookoutequipment-2020-12-15/InferenceS3OutputConfiguration.md "../../../goto/SdkForCpp/lookoutequipment-2020-12-15/InferenceS3OutputConfiguration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/InferenceS3OutputConfiguration.md "../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/InferenceS3OutputConfiguration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/InferenceS3OutputConfiguration.md "../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/InferenceS3OutputConfiguration.md")
