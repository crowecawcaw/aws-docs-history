# MultiMeasureAttributeMapping

A mapping of a source event data field to a measure in a Timestream for
LiveAnalytics record.

## Contents

**MeasureValue**

Dynamic path to the measurement attribute in the source event.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2048.

Required: Yes

**MeasureValueType**

Data type of the measurement attribute in the source event.

Type: String

Valid Values: `DOUBLE | BIGINT | VARCHAR | BOOLEAN | TIMESTAMP`

Required: Yes

**MultiMeasureAttributeName**

Target measure name to be used.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/pipes-2015-10-07/MultiMeasureAttributeMapping.md "../../../goto/SdkForCpp/pipes-2015-10-07/MultiMeasureAttributeMapping.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/pipes-2015-10-07/MultiMeasureAttributeMapping.md "../../../goto/SdkForJavaV2/pipes-2015-10-07/MultiMeasureAttributeMapping.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/pipes-2015-10-07/MultiMeasureAttributeMapping.md "../../../goto/SdkForRubyV3/pipes-2015-10-07/MultiMeasureAttributeMapping.md")
