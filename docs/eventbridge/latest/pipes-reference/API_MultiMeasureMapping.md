# MultiMeasureMapping

Maps multiple measures from the source event to the same Timestream for
LiveAnalytics record.

For more information, see [Amazon Timestream for LiveAnalytics concepts](../../../timestream/latest/developerguide/concepts.md "../../../timestream/latest/developerguide/concepts.md")

## Contents

**MultiMeasureAttributeMappings**

Mappings that represent multiple source event fields mapped to measures in the same
Timestream for LiveAnalytics record.

Type: Array of [MultiMeasureAttributeMapping](API_MultiMeasureAttributeMapping.md "API_MultiMeasureAttributeMapping.md") objects

Array Members: Minimum number of 1 item. Maximum number of 256 items.

Required: Yes

**MultiMeasureName**

The name of the multiple measurements per record (multi-measure).

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/pipes-2015-10-07/MultiMeasureMapping.md "../../../goto/SdkForCpp/pipes-2015-10-07/MultiMeasureMapping.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/pipes-2015-10-07/MultiMeasureMapping.md "../../../goto/SdkForJavaV2/pipes-2015-10-07/MultiMeasureMapping.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/pipes-2015-10-07/MultiMeasureMapping.md "../../../goto/SdkForRubyV3/pipes-2015-10-07/MultiMeasureMapping.md")
