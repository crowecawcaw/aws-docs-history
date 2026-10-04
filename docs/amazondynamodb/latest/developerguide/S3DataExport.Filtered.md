

# Filtering a table export
<a name="S3DataExport.Filtered"></a>

Instead of exporting an entire table, you can export only the items and attributes that you need. DynamoDB exports only the data that matches the expressions you provide. Filtered export works with both full exports and incremental exports.

For an incremental export, DynamoDB evaluates the filter against the latest image of each changed item. For a deleted item, DynamoDB evaluates the filter against the old image of the item, because the new image doesn't exist.

You control what a filtered export returns with three types of expressions. You can provide one of them or combine them in a single export request:
+ A **key condition expression** selects items by their primary key, using the same syntax and rules as a DynamoDB `Query` key condition expression. A key condition expression specifies a single partition key value with an equality comparison, and an optional condition on the sort key. It can't reference non-key attributes, and it can't specify more than one partition key value. Because a key condition expression limits the export to a single partition key value, it reduces the amount of data that DynamoDB reads for the export. For more information, see [Key condition expressions for the Query operation in DynamoDB](Query.KeyConditionExpressions.md).
+ A **filter expression** can apply conditions to both key and non-key attributes, using the same syntax and rules as a filter expression in a `Scan` operation. Filter expressions support comparisons such as equals, not equals, and `OR`, along with the `contains`, `IN`, `begins_with`, `BETWEEN`, `attribute_exists`, and `size` functions. DynamoDB applies a filter expression after it reads the data, so the filter doesn't reduce the amount of data that DynamoDB processes for the export. For more information about filter expressions and their syntax, see [Syntax for filter and condition expressions](Expressions.OperatorsAndFunctions.md#Expressions.OperatorsAndFunctions.Syntax).
+ A **projection expression** identifies the specific attributes that you want in the export output, using the same syntax and rules as a projection expression in other DynamoDB operations. For more information, see [Using projection expressions in DynamoDB](Expressions.ProjectionExpressions.md).

**Note**  
Whether a key attribute can appear in the filter expression depends on whether you also provide a key condition expression. If you provide a key condition expression, the key attribute can't also appear in the filter expression. If you provide only a filter expression, key attributes can appear in the filter expression.

Each expression is subject to the following limits:
+ An expression can be up to 4 KB in size.
+ Attribute names can be up to 250 bytes.
+ Attribute values can be up to 2 MB.
+ An expression can contain at most 300 operators.