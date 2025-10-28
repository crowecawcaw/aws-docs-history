On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# LabelsInputConfiguration

Contains the configuration information for the S3 location being used to hold label
data.

## Contents

**LabelGroupName**

The name of the label group to be used for label data.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 200.

Pattern: `^[0-9a-zA-Z_-]{1,200}$`

Required: No

**S3InputConfiguration**

Contains location information for the S3 location being used for label data.

Type: [LabelsS3InputConfiguration](API_LabelsS3InputConfiguration.md "API_LabelsS3InputConfiguration.md") object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/lookoutequipment-2020-12-15/LabelsInputConfiguration.md "../../../goto/SdkForCpp/lookoutequipment-2020-12-15/LabelsInputConfiguration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/LabelsInputConfiguration.md "../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/LabelsInputConfiguration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/LabelsInputConfiguration.md "../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/LabelsInputConfiguration.md")
