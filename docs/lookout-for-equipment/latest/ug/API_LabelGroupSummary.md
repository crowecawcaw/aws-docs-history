On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# LabelGroupSummary

Contains information about the label group.

## Contents

**CreatedAt**

The time at which the label group was created.

Type: Timestamp

Required: No

**LabelGroupArn**

The Amazon Resource Name (ARN) of the label group.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Pattern: `arn:aws(-[^:]+)?:lookoutequipment:[a-zA-Z0-9\-]*:[0-9]{12}:label-group\/.+`

Required: No

**LabelGroupName**

The name of the label group.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 200.

Pattern: `^[0-9a-zA-Z_-]{1,200}$`

Required: No

**UpdatedAt**

The time at which the label group was updated.

Type: Timestamp

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/lookoutequipment-2020-12-15/LabelGroupSummary.md "../../../goto/SdkForCpp/lookoutequipment-2020-12-15/LabelGroupSummary.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/LabelGroupSummary.md "../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/LabelGroupSummary.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/LabelGroupSummary.md "../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/LabelGroupSummary.md")
