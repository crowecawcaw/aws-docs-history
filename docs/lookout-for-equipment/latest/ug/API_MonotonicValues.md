On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# MonotonicValues

Entity that comprises information on monotonic values in the data.

## Contents

**Status**

Indicates whether there is a potential data issue related to having monotonic values.

Type: String

Valid Values: `POTENTIAL_ISSUE_DETECTED | NO_ISSUE_DETECTED`

Required: Yes

**Monotonicity**

Indicates the monotonicity of values. Can be INCREASING, DECREASING, or STATIC.

Type: String

Valid Values: `DECREASING | INCREASING | STATIC`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/lookoutequipment-2020-12-15/MonotonicValues.md "../../../goto/SdkForCpp/lookoutequipment-2020-12-15/MonotonicValues.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/MonotonicValues.md "../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/MonotonicValues.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/MonotonicValues.md "../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/MonotonicValues.md")
