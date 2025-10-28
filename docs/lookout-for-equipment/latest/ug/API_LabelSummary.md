On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# LabelSummary

Information about the label.

## Contents

**CreatedAt**

The time at which the label was created.

Type: Timestamp

Required: No

**EndTime**

The timestamp indicating the end of the label.

Type: Timestamp

Required: No

**Equipment**

Indicates that a label pertains to a particular piece of equipment.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 200.

Pattern: `[\P{M}\p{M}]{1,200}`

Required: No

**FaultCode**

Indicates the type of anomaly associated with the label.

Data in this field will be retained for service usage. Follow best practices for the
security of your data.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `[\P{M}\p{M}]{1,100}`

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

**LabelId**

The ID of the label.

Type: String

Length Constraints: Maximum length of 32.

Pattern: `[A-Fa-f0-9]{0,32}`

Required: No

**Rating**

Indicates whether a labeled event represents an anomaly.

Type: String

Valid Values: `ANOMALY | NO_ANOMALY | NEUTRAL`

Required: No

**StartTime**

The timestamp indicating the start of the label.

Type: Timestamp

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/lookoutequipment-2020-12-15/LabelSummary.md "../../../goto/SdkForCpp/lookoutequipment-2020-12-15/LabelSummary.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/LabelSummary.md "../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/LabelSummary.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/LabelSummary.md "../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/LabelSummary.md")
