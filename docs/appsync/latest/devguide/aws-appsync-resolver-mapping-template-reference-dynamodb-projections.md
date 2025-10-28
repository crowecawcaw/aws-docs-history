# Projections

When reading objects in DynamoDB using the `GetItem`, `Scan`, `Query`,
`BatchGetItem`, and `TransactGetItems` operations, you can optionally specify a
projection that identifies the attributes that you want. The projection has the following structure, which is
similar to filters:

```
"projection" : {
    "expression" : "projection expression"
    "expressionNames" : {
        "#name" : "name",
    }
}
```

The fields are defined as follows:

**`expression`**

The projection expression, which is a string. To retrieve a single attribute, specify its name. For
multiple attributes, the names must be comma-separated values. For more information on writing
projection expressions, see the [DynamoDB projection
expressions](../../../amazondynamodb/latest/developerguide/Expressions.md "../../../amazondynamodb/latest/developerguide/Expressions.md") documentation. This field is required.

**`expressionNames`**

The substitutions for expression attribute _name_ placeholders in
the form of key-value pairs. The key corresponds to a name placeholder used in the
`expression`. The value must be a string that corresponds to the attribute name of the
item in DynamoDB. This field is optional and should only be populated with substitutions for expression
attribute name placeholders used in the `expression`. For more information about
`expressionNames`, see the [DynamoDB
documentation](../../../amazondynamodb/latest/developerguide/Expressions.md "../../../amazondynamodb/latest/developerguide/Expressions.md").

## Example 1

The following example is a projection section for a VTL mapping template in which only the attributes
`author` and `id` are returned from DynamoDB:

```
"projection" : {
    "expression" : "#author, id",
    "expressionNames" : {
        "#author" : "author"
    }
}
```

###### Tip

You can access your GraphQL request selection set using [$context.info.selectionSetList](resolver-context-reference.md#aws-appsync-resolver-context-reference-info "resolver-context-reference.md#aws-appsync-resolver-context-reference-info"). This field allows you to frame your projection expression
dynamically according to your requirements.

###### Note

While using projection expressions with the `Query` and `Scan` operations, the
value for `select` must be `SPECIFIC_ATTRIBUTES`. For more information, see the
[DynamoDB
documentation](../../../amazondynamodb/latest/APIReference/API_Query.md#DDB-Query-request-Select "../../../amazondynamodb/latest/APIReference/API_Query.md#DDB-Query-request-Select").
