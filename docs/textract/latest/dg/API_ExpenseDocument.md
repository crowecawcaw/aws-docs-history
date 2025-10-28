# ExpenseDocument

The structure holding all the information returned by AnalyzeExpense

## Contents

**Blocks**

This is a block object, the same as reported when DetectDocumentText is run on a document.
It provides word level recognition of text.

Type: Array of [Block](API_Block.md "API_Block.md") objects

Required: No

**ExpenseIndex**

Denotes which invoice or receipt in the document the information is coming from.
First document will be 1, the second 2, and so on.

Type: Integer

Valid Range: Minimum value of 0.

Required: No

**LineItemGroups**

Information detected on each table of a document, seperated into `LineItems`.

Type: Array of [LineItemGroup](API_LineItemGroup.md "API_LineItemGroup.md") objects

Required: No

**SummaryFields**

Any information found outside of a table by Amazon Textract.

Type: Array of [ExpenseField](API_ExpenseField.md "API_ExpenseField.md") objects

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/textract-2018-06-27/ExpenseDocument.md "../../../goto/SdkForCpp/textract-2018-06-27/ExpenseDocument.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/textract-2018-06-27/ExpenseDocument.md "../../../goto/SdkForJavaV2/textract-2018-06-27/ExpenseDocument.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/textract-2018-06-27/ExpenseDocument.md "../../../goto/SdkForRubyV3/textract-2018-06-27/ExpenseDocument.md")
