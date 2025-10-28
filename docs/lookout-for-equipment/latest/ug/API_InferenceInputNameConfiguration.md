On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# InferenceInputNameConfiguration

Specifies configuration information for the input data for the inference, including
timestamp format and delimiter.

## Contents

**ComponentTimestampDelimiter**

Indicates the delimiter character used between items in the data.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 1.

Pattern: `^(\-|\_|\s)?$`

Required: No

**TimestampFormat**

The format of the timestamp, whether Epoch time, or standard, with or without hyphens
(-).

Type: String

Pattern: `^EPOCH|yyyy-MM-dd-HH-mm-ss|yyyyMMddHHmmss$`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/lookoutequipment-2020-12-15/InferenceInputNameConfiguration.md "../../../goto/SdkForCpp/lookoutequipment-2020-12-15/InferenceInputNameConfiguration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/InferenceInputNameConfiguration.md "../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/InferenceInputNameConfiguration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/InferenceInputNameConfiguration.md "../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/InferenceInputNameConfiguration.md")
