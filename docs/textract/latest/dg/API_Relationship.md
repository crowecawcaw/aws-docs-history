# Relationship

Information about how blocks are related to each other. A `Block` object
contains 0 or more `Relation` objects in a list, `Relationships`. For
more information, see [Block](API_Block.md "API_Block.md").

The `Type` element provides the type of the relationship for all blocks in
the `IDs` array.

## Contents

**Ids**

An
array of IDs for related blocks. You can get the type of the relationship from the
`Type` element.

Type: Array of strings

Pattern: `.*\S.*`

Required: No

**Type**

The type of relationship between the blocks in the IDs array and the current block. The
following list describes the relationship types that can be returned.

- _VALUE_ - A list that contains the ID of the VALUE block that's associated with the
  KEY of a key-value pair.
- _CHILD_ - A list of IDs that identify blocks found within the
  current block object. For example, WORD blocks have a CHILD relationship to the LINE
  block type.
- _MERGED_CELL_ - A list of IDs that identify each of the
  MERGED_CELL block types in a table.
- _ANSWER_ - A list that contains the ID of the QUERY_RESULT
  block that’s associated with the corresponding QUERY block.
- _TABLE_ - A list of IDs that identify associated TABLE block
  types.
- _TABLE_TITLE_ - A list that contains the ID for the TABLE_TITLE
  block type in a table.
- _TABLE_FOOTER_ - A list of IDs that identify the TABLE_FOOTER
  block types in a table.

Type: String

Valid Values: `VALUE | CHILD | COMPLEX_FEATURES | MERGED_CELL | TITLE | ANSWER | TABLE | TABLE_TITLE | TABLE_FOOTER`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/textract-2018-06-27/Relationship.md "../../../goto/SdkForCpp/textract-2018-06-27/Relationship.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/textract-2018-06-27/Relationship.md "../../../goto/SdkForJavaV2/textract-2018-06-27/Relationship.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/textract-2018-06-27/Relationship.md "../../../goto/SdkForRubyV3/textract-2018-06-27/Relationship.md")
