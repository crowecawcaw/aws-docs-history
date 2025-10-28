# SingleMeasureMapping

Maps a single source data field to a single record in the specified Timestream
for LiveAnalytics table.

For more information, see [Amazon Timestream for LiveAnalytics concepts](../../../timestream/latest/developerguide/concepts.md "../../../timestream/latest/developerguide/concepts.md")

## Contents

**MeasureName**

Target measure name for the measurement attribute in the Timestream table.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1024.

Required: Yes

**MeasureValue**

Dynamic path of the source field to map to the measure in the record.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2048.

Required: Yes

**MeasureValueType**

Data type of the source field.

Type: String

Valid Values: `DOUBLE | BIGINT | VARCHAR | BOOLEAN | TIMESTAMP`

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/pipes-2015-10-07/SingleMeasureMapping.md "../../../goto/SdkForCpp/pipes-2015-10-07/SingleMeasureMapping.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/pipes-2015-10-07/SingleMeasureMapping.md "../../../goto/SdkForJavaV2/pipes-2015-10-07/SingleMeasureMapping.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/pipes-2015-10-07/SingleMeasureMapping.md "../../../goto/SdkForRubyV3/pipes-2015-10-07/SingleMeasureMapping.md")
