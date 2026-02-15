# Using expression attribute

values in DynamoDB

_Expression attribute values_ in Amazon DynamoDB act as variables.
They're substitutes for the actual values that you want to compare—values that you
might not know until runtime. An expression attribute value must begin with a colon
(`:`) and be followed by one or more alphanumeric characters.

For example, suppose that you wanted to return all of the `ProductCatalog`
items that are available in `Black` and cost `500` or less. You
could use a `Scan` operation with a filter expression, as in this AWS Command Line Interface
(AWS CLI) example.

```
aws dynamodb scan \
    --table-name ProductCatalog \
    --filter-expression "contains(Color, :c) and Price <= :p" \
    --expression-attribute-values file://values.json
```

The arguments for `--expression-attribute-values` are stored in the
`values.json` file.

```
{
    ":c": { "S": "Black" },
    ":p": { "N": "500" }
}
```

If you define an expression attribute value, you must use it consistently throughout
the entire expression. Also, you can't omit the `:` symbol.

Expression attribute values are used with key condition expressions, condition
expressions, update expressions, and filter expressions.
