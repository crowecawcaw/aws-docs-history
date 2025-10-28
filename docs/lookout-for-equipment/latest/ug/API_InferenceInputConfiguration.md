On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# InferenceInputConfiguration

Specifies configuration information for the input data for the inference, including
Amazon S3 location of input data..

## Contents

**InferenceInputNameConfiguration**

Specifies configuration information for the input data for the inference, including
timestamp format and delimiter.

Type: [InferenceInputNameConfiguration](API_InferenceInputNameConfiguration.md "API_InferenceInputNameConfiguration.md") object

Required: No

**InputTimeZoneOffset**

Indicates the difference between your time zone and Coordinated Universal Time
(UTC).

Type: String

Pattern: `^(\+|\-)[0-9]{2}\:[0-9]{2}$`

Required: No

**S3InputConfiguration**

Specifies configuration information for the input data for the inference, including
Amazon S3 location of input data.

Type: [InferenceS3InputConfiguration](API_InferenceS3InputConfiguration.md "API_InferenceS3InputConfiguration.md") object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/lookoutequipment-2020-12-15/InferenceInputConfiguration.md "../../../goto/SdkForCpp/lookoutequipment-2020-12-15/InferenceInputConfiguration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/InferenceInputConfiguration.md "../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/InferenceInputConfiguration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/InferenceInputConfiguration.md "../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/InferenceInputConfiguration.md")
