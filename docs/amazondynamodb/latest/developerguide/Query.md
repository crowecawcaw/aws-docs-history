# Key condition expressions for the Query

operation in DynamoDB

You can use any attribute name in a key condition expression, provided that the first
character is `a-z` or `A-Z` and the rest of the characters
(starting from the second character, if present) are `a-z`, `A-Z`,
or `0-9`. In addition, the attribute name must not be a DynamoDB reserved word.
(For a complete list of these, see [Reserved words in DynamoDB](ReservedWords.md "ReservedWords.md").) If an attribute name does not meet these
requirements, you must define an expression attribute name as a placeholder. For more
information, see [Expression attribute names (aliases)
in DynamoDB](Expressions.md "Expressions.md").

For items with a given partition key value, DynamoDB stores these items close together,
in sorted order by sort key value. In a `Query` operation, DynamoDB retrieves
the items in sorted order, and then processes the items using
`KeyConditionExpression` and any `FilterExpression` that might
be present. Only then are the `Query` results sent back to the client.

A `Query` operation always returns a result set. If no matching items are
found, the result set is empty.

`Query` results are always sorted by the sort key value. If the data type
of the sort key is `Number`, the results are returned in numeric order.
Otherwise, the results are returned in order of UTF-8 bytes. By default, the sort order
is ascending. To reverse the order, set the `ScanIndexForward` parameter to
`false`.

A single `Query` operation can retrieve a maximum of 1 MB of
data. This limit applies before any `FilterExpression` or
`ProjectionExpression` is applied to the results. If
`LastEvaluatedKey` is present in the response and is non-null, you must
paginate the result set (see [Paginating table query results in DynamoDB](Query.md "Query.md")).

## Key condition expression

examples

To specify the search criteria, you use a _key condition
expression_—a string that determines the items to be read from
the table or index.

You must specify the partition key name and value as an equality condition. You
cannot use a non-key attribute in a key condition expression.

You can optionally provide a second condition for the sort key (if present). The
sort key condition must use one of the following comparison operators:

- ``a` = `b``
  — true if the attribute `a` is equal to the
  value `b`
- ``a` <
`b`` — true if
  `a` is less than
  `b`
- ``a` <=
`b`` — true if
  `a` is less than or equal to
  `b`
- ``a` >
`b`` — true if
  `a` is greater than
  `b`
- ``a` >=
`b`` — true if
  `a` is greater than or equal to
  `b`
- ``a` BETWEEN `b`
AND `c`` — true if
  `a` is greater than or equal to
  `b`, and less than or equal to
  `c`.

The following function is also supported:

- `begins_with (`a`,
`substr`)`— true if the value
  of attribute `a` begins with a
  particular substring.

The following AWS Command Line Interface (AWS CLI) examples demonstrate the use of key condition
expressions. These expressions use placeholders (such as `:name` and
`:sub`) instead of actual values. For more information, see [Expression attribute names (aliases)
in DynamoDB](Expressions.md "Expressions.md") and [Using expression attribute
values in DynamoDB](Expressions.md "Expressions.md").

###### Example

Query the `Thread` table for a particular `ForumName`
(partition key). All of the items with that `ForumName` value are
read by the query because the sort key (`Subject`) is not included in
`KeyConditionExpression`.

```
aws dynamodb query \
    --table-name Thread \
    --key-condition-expression "ForumName = :name" \
    --expression-attribute-values  '{":name":{"S":"Amazon DynamoDB"}}'
```

###### Example

Query the `Thread` table for a particular `ForumName`
(partition key), but this time return only the items with a given
`Subject` (sort key).

```
aws dynamodb query \
    --table-name Thread \
    --key-condition-expression "ForumName = :name and Subject = :sub" \
    --expression-attribute-values  file://values.json
```

The arguments for `--expression-attribute-values` are stored in the
`values.json` file.

```
{
    ":name":{"S":"Amazon DynamoDB"},
    ":sub":{"S":"DynamoDB Thread 1"}
}
```

###### Example

Query the `Reply` table for a particular `Id` (partition
key), but return only those items whose `ReplyDateTime` (sort key)
begins with certain characters.

```
aws dynamodb query \
    --table-name Reply \
    --key-condition-expression "Id = :id and begins_with(ReplyDateTime, :dt)" \
    --expression-attribute-values  file://values.json
```

The arguments for `--expression-attribute-values` are stored in the
`values.json` file.

```
{
    ":id":{"S":"Amazon DynamoDB#DynamoDB Thread 1"},
    ":dt":{"S":"2015-09"}
}
```
