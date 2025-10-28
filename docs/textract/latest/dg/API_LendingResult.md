# LendingResult

Contains the detections for each page analyzed through the Analyze Lending API.

## Contents

**Extractions**

An array of Extraction to hold structured data. e.g. normalized key value pairs instead of raw OCR detections .

Type: Array of [Extraction](API_Extraction.md "API_Extraction.md") objects

Required: No

**Page**

The page number for a page, with regard to whole submission.

Type: Integer

Valid Range: Minimum value of 0.

Required: No

**PageClassification**

The classifier result for a given page.

Type: [PageClassification](API_PageClassification.md "API_PageClassification.md") object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/textract-2018-06-27/LendingResult.md "../../../goto/SdkForCpp/textract-2018-06-27/LendingResult.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/textract-2018-06-27/LendingResult.md "../../../goto/SdkForJavaV2/textract-2018-06-27/LendingResult.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/textract-2018-06-27/LendingResult.md "../../../goto/SdkForRubyV3/textract-2018-06-27/LendingResult.md")
