# LendingDetection

The results extracted for a lending document.

## Contents

**Confidence**

The confidence level for the text of a detected value in a lending document.

Type: Float

Valid Range: Minimum value of 0. Maximum value of 100.

Required: No

**Geometry**

Information about where the following items are located on a document page: detected
page, text, key-value pairs, tables, table cells, and selection elements.

Type: [Geometry](API_Geometry.md "API_Geometry.md") object

Required: No

**SelectionStatus**

The selection status of a selection element, such as an option button or check box.

Type: String

Valid Values: `SELECTED | NOT_SELECTED`

Required: No

**Text**

The text extracted for a detected value in a lending document.

Type: String

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/textract-2018-06-27/LendingDetection.md "../../../goto/SdkForCpp/textract-2018-06-27/LendingDetection.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/textract-2018-06-27/LendingDetection.md "../../../goto/SdkForJavaV2/textract-2018-06-27/LendingDetection.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/textract-2018-06-27/LendingDetection.md "../../../goto/SdkForRubyV3/textract-2018-06-27/LendingDetection.md")
