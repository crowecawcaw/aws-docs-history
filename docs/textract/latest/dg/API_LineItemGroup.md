# LineItemGroup

A grouping of tables which contain LineItems, with each table identified by the table's `LineItemGroupIndex`.

## Contents

**LineItemGroupIndex**

The number used to identify a specific table in a document. The first table encountered will have a LineItemGroupIndex of 1, the second 2, etc.

Type: Integer

Valid Range: Minimum value of 0.

Required: No

**LineItems**

The breakdown of information on a particular line of a table.

Type: Array of [LineItemFields](API_LineItemFields.md "API_LineItemFields.md") objects

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/textract-2018-06-27/LineItemGroup.md "../../../goto/SdkForCpp/textract-2018-06-27/LineItemGroup.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/textract-2018-06-27/LineItemGroup.md "../../../goto/SdkForJavaV2/textract-2018-06-27/LineItemGroup.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/textract-2018-06-27/LineItemGroup.md "../../../goto/SdkForRubyV3/textract-2018-06-27/LineItemGroup.md")
