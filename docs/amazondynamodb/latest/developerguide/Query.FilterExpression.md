

# Filter expressions for the Query operation in DynamoDB
<a name="Query.FilterExpression"></a>

If you need to further refine the `Query` results, you can optionally provide a filter expression. A *filter expression* determines which items within the `Query` results should be returned to you. All of the other results are discarded.

A filter expression is applied after a `Query` finishes, but before the results are returned. Therefore, a `Query` consumes the same amount of read capacity, regardless of whether a filter expression is present.

A `Query` operation can retrieve a maximum of 1 MB of data. This limit applies before the filter expression is evaluated.

A filter expression cannot contain partition key or sort key attributes. You need to specify those attributes in the key condition expression, not the filter expression.

The syntax for a filter expression is similar to that of a key condition expression. Filter expressions can use the same comparators, functions, and logical operators as a key condition expression. In addition, filter expressions can use the not-equals operator (`<>`), the `OR` operator, the `CONTAINS` operator, the `IN` operator, the `BEGINS_WITH` operator, the `BETWEEN` operator, the `EXISTS` operator, and the `SIZE` operator. For more information, see [Key condition expressions for the Query operation in DynamoDB](Query.KeyConditionExpressions.md) and [Syntax for filter and condition expressions](Expressions.OperatorsAndFunctions.md#Expressions.OperatorsAndFunctions.Syntax).

**Example**  
The following AWS CLI example queries the `Thread` table for a particular `ForumName` (partition key) and `Subject` (sort key). Of the items that are found, only the most popular discussion threads are returned—in other words, only those threads with more than a certain number of `Views`.  

```
aws dynamodb query \
    --table-name Thread \
    --key-condition-expression "ForumName = :fn and Subject begins_with :sub" \
    --filter-expression "#v >= :num" \
    --expression-attribute-names '{"#v": "Views"}' \
    --expression-attribute-values file://values.json
```
The arguments for `--expression-attribute-values` are stored in the `values.json` file.  

```
{
    ":fn":{"S":"Amazon DynamoDB"},
    ":sub":{"S":"DynamoDB Thread 1"},
    ":num":{"N":"3"}
}
```
Note that `Views` is a reserved word in DynamoDB (see [Reserved words in DynamoDB](ReservedWords.md)), so this example uses `#v` as a placeholder. For more information, see [Expression attribute names (aliases) in DynamoDB](Expressions.ExpressionAttributeNames.md).

**Note**  
A filter expression removes items from the `Query` result set. If possible, avoid using `Query` where you expect to retrieve a large number of items but also need to discard most of those items.