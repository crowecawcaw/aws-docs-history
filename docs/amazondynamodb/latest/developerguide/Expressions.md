# Using expressions in DynamoDB

In Amazon DynamoDB, you can use _expressions_ to specify which attributes to
read from an item, write data when a condition is met, specify how to update an item, define
queries and filter the results of a query.

This table describes the basic expression grammar and the available kinds of
expressions.

| Expression type          | Description                                                                                                                                                               |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Projection expression    | A projection expression identifies the attributes that you want to<br>retrieve from an item when you use operations such as GetItem, Query, or<br>Scan.                   |
| Condition expression     | A condition expression determines which items should be modified when you<br>use the PutItem, UpdateItem, and DeleteItem operations.                                      |
| Update expression        | An update expression specifies how UpdateItem will modify the attributes<br>of an item— for example, setting a scalar value or removing elements from a<br>list or a map. |
| Key condition expression | A key condition expression determines which items a query will read from<br>a table or index.                                                                             |
| Filter expression        | A filter expression determines which items among the Query results should<br>be returned to you. All the other results are discarded.                                     |

For information about expression syntax and more detailed information about each type of
expression, see the following sections.

###### Topics

- [Referring to item attributes when using
  expressions in DynamoDB](Expressions.md "Expressions.md")
- [Expression attribute names (aliases)
  in DynamoDB](Expressions.md "Expressions.md")
- [Using expression attribute
  values in DynamoDB](Expressions.md "Expressions.md")
- [Using projection expressions in
  DynamoDB](Expressions.md "Expressions.md")
- [Using update expressions in DynamoDB](Expressions.md "Expressions.md")
- [Condition and filter expressions,
  operators, and functions in DynamoDB](Expressions.md "Expressions.md")
- [DynamoDB condition expression CLI example](Expressions.md "Expressions.md")

###### Note

For backward compatibility, DynamoDB also supports conditional parameters that do not use
expressions. For more information, see [Legacy DynamoDB conditional parameters](LegacyConditionalParameters.md "LegacyConditionalParameters.md").

New applications should use expressions rather than the legacy parameters.
