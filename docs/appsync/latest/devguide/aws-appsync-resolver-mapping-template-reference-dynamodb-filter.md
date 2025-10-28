# Filters

When querying objects in DynamoDB using the `Query` and `Scan` operations, you can
optionally specify a `filter` that evaluates the results and returns only the desired values.

The filter mapping section of a `Query` or `Scan` mapping document has the following
structure:

```
"filter" : {
    "expression" : "filter expression"
    "expressionNames" : {
        "#name" : "name",
    },
    "expressionValues" : {
        ":value" : ... typed value
    },
}
```

The fields are defined as follows:

**`expression`**

The query expression. For more information about how to write filter expressions, see the [DynamoDB QueryFilter](../../../amazondynamodb/latest/developerguide/LegacyConditionalParameters.md "../../../amazondynamodb/latest/developerguide/LegacyConditionalParameters.md") and [DynamoDB ScanFilter](../../../amazondynamodb/latest/developerguide/LegacyConditionalParameters.md "../../../amazondynamodb/latest/developerguide/LegacyConditionalParameters.md") documentation. This field must be specified.

**`expressionNames`**

The substitutions for expression attribute _name_ placeholders, in the form of
key-value pairs. The key corresponds to a name placeholder used in the `expression`. The
value must be a string that corresponds to the attribute name of the item in DynamoDB. This field is
optional, and should only be populated with substitutions for expression attribute name placeholders
used in the `expression`.

**`expressionValues`**

The substitutions for expression attribute _value_ placeholders, in the form of
key-value pairs. The key corresponds to a value placeholder used in the `expression`, and
the value must be a typed value. For more information about how to specify a “typed value”, see [Type System
(Request Mapping)](aws-appsync-resolver-mapping-template-reference-dynamodb-typed-values-request.md "aws-appsync-resolver-mapping-template-reference-dynamodb-typed-values-request.md"). This must be specified. This field is optional, and should only be
populated with substitutions for expression attribute value placeholders used in the
`expression`.

## Example

The following example is a filter section for a mapping template, where entries
retrieved from DynamoDB are only returned if the title starts with the `title`
argument.

```
"filter" : {
    "expression" : "begins_with(#title, :title)",
    "expressionNames" : {
        "#title" : "title"
    },
    "expressionValues" : {
        ":title" : $util.dynamodb.toDynamoDBJson($context.arguments.title)
    }
}
```
