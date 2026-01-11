# ScanFilter (legacy)

###### Note

We recommend that you use the new expression parameters instead of these legacy parameters whenever possible.
For more information, see [Using expressions in DynamoDB](Expressions.md "Expressions.md").
For specific information on the new parameter replacing this one,
[use FilterExpression instead.](#FilterExpression2.instead "#FilterExpression2.instead").

In a `Scan` operation, the legacy conditional parameter `ScanFilter` is a
condition that evaluates the scan results and returns only the desired
values.

###### Note

This parameter does not support attributes of type List or Map.

If you specify more than one condition in the `ScanFilter` map,
then by default all of the conditions must evaluate to true. In other words, the
conditions are ANDed together. (You can use the
[ConditionalOperator (legacy)](LegacyConditionalParameters.md "LegacyConditionalParameters.md") parameter to OR the conditions instead.
If you do this, then at least one of the conditions must evaluate to true, rather
than all of them.)

Each `ScanFilter` element consists of an attribute name to
compare, along with the following:

- `AttributeValueList` - One or more values to evaluate
  against the supplied attribute. The number of values in the list depends on
  the operator specified in `ComparisonOperator` .

For type Number, value comparisons are numeric.

String value comparisons for greater than, equals, or less than are based
on UTF-8 binary encoding. For example, `a` is greater than
`A`, and `a` is greater than
`B`.

For Binary, DynamoDB treats each byte of the binary data as unsigned when
it compares binary values.

For information on specifying data types in JSON, see [DynamoDB low-level API](Programming.md "Programming.md").

- `ComparisonOperator` - A comparator for evaluating attributes. For
  example: equals, greater than, and less than.

The following comparison operators are available:

`EQ | NE | LE | LT | GE | GT | NOT_NULL | NULL | CONTAINS |
 NOT_CONTAINS | BEGINS_WITH | IN | BETWEEN`

## Use _FilterExpression_ instead – Example

Suppose you wanted to scan the _Music_ table and apply a
condition to the matching items. You could use a
`Scan` request with a `ScanFilter` parameter, as in this
AWS CLI example:

```
aws dynamodb scan \
    --table-name Music \
    --scan-filter '{
        "Genre":{
            "AttributeValueList":[ {"S":"Rock"} ],
            "ComparisonOperator": "EQ"
        }
    }'
```

You can use a `FilterExpression` instead:

```
aws dynamodb scan \
    --table-name Music \
    --filter-expression 'Genre = :g' \
    --expression-attribute-values '{
        ":g": {"S":"Rock"}
    }'

```
