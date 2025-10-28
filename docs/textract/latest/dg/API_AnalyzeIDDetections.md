# AnalyzeIDDetections

Used to contain the information detected by an AnalyzeID operation.

## Contents

**Text**

Text of either the normalized field or value associated with it.

Type: String

Required: Yes

**Confidence**

The confidence score of the detected text.

Type: Float

Valid Range: Minimum value of 0. Maximum value of 100.

Required: No

**NormalizedValue**

Only returned for dates, returns the type of value detected and the date
written in a more machine readable way.

Type: [NormalizedValue](API_NormalizedValue.md "API_NormalizedValue.md") object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/textract-2018-06-27/AnalyzeIDDetections.md "../../../goto/SdkForCpp/textract-2018-06-27/AnalyzeIDDetections.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/textract-2018-06-27/AnalyzeIDDetections.md "../../../goto/SdkForJavaV2/textract-2018-06-27/AnalyzeIDDetections.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/textract-2018-06-27/AnalyzeIDDetections.md "../../../goto/SdkForRubyV3/textract-2018-06-27/AnalyzeIDDetections.md")
