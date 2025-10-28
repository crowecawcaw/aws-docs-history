On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# LargeTimestampGaps

Entity that comprises information on large gaps between consecutive timestamps in data.

## Contents

**Status**

Indicates whether there is a potential data issue related to large gaps in timestamps.

Type: String

Valid Values: `POTENTIAL_ISSUE_DETECTED | NO_ISSUE_DETECTED`

Required: Yes

**MaxTimestampGapInDays**

Indicates the size of the largest timestamp gap, in days.

Type: Integer

Required: No

**NumberOfLargeTimestampGaps**

Indicates the number of large timestamp gaps, if there are any.

Type: Integer

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/lookoutequipment-2020-12-15/LargeTimestampGaps.md "../../../goto/SdkForCpp/lookoutequipment-2020-12-15/LargeTimestampGaps.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/LargeTimestampGaps.md "../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/LargeTimestampGaps.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/LargeTimestampGaps.md "../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/LargeTimestampGaps.md")
