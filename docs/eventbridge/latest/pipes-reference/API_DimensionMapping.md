# DimensionMapping

Maps source data to a dimension in the target Timestream for LiveAnalytics
table.

For more information, see [Amazon Timestream for LiveAnalytics concepts](../../../timestream/latest/developerguide/concepts.md "../../../timestream/latest/developerguide/concepts.md")

## Contents

**DimensionName**

The metadata attributes of the time series. For example, the name and Availability Zone
of an Amazon EC2 instance or the name of the manufacturer of a wind turbine are
dimensions.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Required: Yes

**DimensionValue**

Dynamic path to the dimension value in the source event.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2048.

Required: Yes

**DimensionValueType**

The data type of the dimension for the time-series data.

Type: String

Valid Values: `VARCHAR`

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/pipes-2015-10-07/DimensionMapping.md "../../../goto/SdkForCpp/pipes-2015-10-07/DimensionMapping.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/pipes-2015-10-07/DimensionMapping.md "../../../goto/SdkForJavaV2/pipes-2015-10-07/DimensionMapping.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/pipes-2015-10-07/DimensionMapping.md "../../../goto/SdkForRubyV3/pipes-2015-10-07/DimensionMapping.md")
