# IdentityDocument

The structure that lists each document processed in an AnalyzeID operation.

## Contents

**Blocks**

Individual word recognition, as returned by document detection.

Type: Array of [Block](API_Block.md "API_Block.md") objects

Required: No

**DocumentIndex**

Denotes the placement of a document in the IdentityDocument list. The first document
is marked 1, the second 2 and so on.

Type: Integer

Valid Range: Minimum value of 0.

Required: No

**IdentityDocumentFields**

The structure used to record information extracted from identity documents.
Contains both normalized field and value of the extracted text.

Type: Array of [IdentityDocumentField](API_IdentityDocumentField.md "API_IdentityDocumentField.md") objects

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/textract-2018-06-27/IdentityDocument.md "../../../goto/SdkForCpp/textract-2018-06-27/IdentityDocument.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/textract-2018-06-27/IdentityDocument.md "../../../goto/SdkForJavaV2/textract-2018-06-27/IdentityDocument.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/textract-2018-06-27/IdentityDocument.md "../../../goto/SdkForRubyV3/textract-2018-06-27/IdentityDocument.md")
