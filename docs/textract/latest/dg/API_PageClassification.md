# PageClassification

The class assigned to a Page object detected in an input document.
Contains information regarding the predicted type/class of a document's page and the
page number that the Page object was detected on.

## Contents

**PageNumber**

The page number the value was detected on, relative to Amazon Textract's starting position.

Type: Array of [Prediction](API_Prediction.md "API_Prediction.md") objects

Required: Yes

**PageType**

The class, or document type, assigned to a detected Page object. The class, or document type,
assigned to a detected Page object.

Type: Array of [Prediction](API_Prediction.md "API_Prediction.md") objects

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/textract-2018-06-27/PageClassification.md "../../../goto/SdkForCpp/textract-2018-06-27/PageClassification.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/textract-2018-06-27/PageClassification.md "../../../goto/SdkForJavaV2/textract-2018-06-27/PageClassification.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/textract-2018-06-27/PageClassification.md "../../../goto/SdkForRubyV3/textract-2018-06-27/PageClassification.md")
