# DocumentGroup

Summary information about documents grouped by the same document type.

## Contents

**DetectedSignatures**

A list of the detected signatures found in a document group.

Type: Array of [DetectedSignature](API_DetectedSignature.md "API_DetectedSignature.md") objects

Required: No

**SplitDocuments**

An array that contains information about the pages of a document, defined by logical boundary.

Type: Array of [SplitDocument](API_SplitDocument.md "API_SplitDocument.md") objects

Required: No

**Type**

The type of document that Amazon Textract has detected. See [Analyze Lending Response Objects](lending-response-objects.md "lending-response-objects.md") for a list of all types returned by Textract.

Type: String

Pattern: `.*\S.*`

Required: No

**UndetectedSignatures**

A list of any expected signatures not found in a document group.

Type: Array of [UndetectedSignature](API_UndetectedSignature.md "API_UndetectedSignature.md") objects

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/textract-2018-06-27/DocumentGroup.md "../../../goto/SdkForCpp/textract-2018-06-27/DocumentGroup.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/textract-2018-06-27/DocumentGroup.md "../../../goto/SdkForJavaV2/textract-2018-06-27/DocumentGroup.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/textract-2018-06-27/DocumentGroup.md "../../../goto/SdkForRubyV3/textract-2018-06-27/DocumentGroup.md")
