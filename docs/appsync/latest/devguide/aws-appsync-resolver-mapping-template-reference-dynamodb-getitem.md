# GetItem

The `GetItem` request mapping document lets you tell the AWS AppSync DynamoDB resolver to make a
`GetItem` request to DynamoDB, and enables you to specify:

- The key of the item in DynamoDB
- Whether to use a consistent read or not
  The `GetItem` mapping document has the following structure:

```
{
    "version" : "2017-02-28",
    "operation" : "GetItem",
    "key" : {
        "foo" : ... typed value,
        "bar" : ... typed value
    },
    "consistentRead" : true,
    "projection" : {
        ...
    }
}
```

The fields are defined as follows:

## GetItem fields

**`version`**

The template definition version. `2017-02-28` and
`2018-05-29` are currently supported. This value is
required.

**`operation`**

The DynamoDB operation to perform. To perform the `GetItem`
DynamoDB operation, this must be set to `GetItem`. This value
is required.

**`key`**

The key of the item in DynamoDB. DynamoDB items may have a single hash key,
or a hash key and sort key, depending on the table structure. For more
information about how to specify a “typed value”, see [Type system (request mapping)](aws-appsync-resolver-mapping-template-reference-dynamodb-typed-values-request.md "aws-appsync-resolver-mapping-template-reference-dynamodb-typed-values-request.md"). This value is required.

**`consistentRead`**

Whether or not to perform a strongly consistent read with DynamoDB. This
is optional, and defaults to `false`.

**`projection`**

A projection that's used to specify the attributes to return from the
DynamoDB operation. For more information about projections, see [Projections](resolver-mapping-template-reference-dynamodb.md#aws-appsync-resolver-mapping-template-reference-dynamodb-projections "resolver-mapping-template-reference-dynamodb.md#aws-appsync-resolver-mapping-template-reference-dynamodb-projections"). This field is optional.

The item returned from DynamoDB is automatically converted into GraphQL and JSON primitive types, and is
available in the mapping context (`$context.result`).

For more information about DynamoDB type conversion, see [Type system (response mapping)](aws-appsync-resolver-mapping-template-reference-dynamodb-typed-values-responses.md "aws-appsync-resolver-mapping-template-reference-dynamodb-typed-values-responses.md").

For more information about response mapping templates, see [Resolver mapping
template overview](resolver-mapping-template-reference-overview.md#aws-appsync-resolver-mapping-template-reference-overview "resolver-mapping-template-reference-overview.md#aws-appsync-resolver-mapping-template-reference-overview").

## Example

The following example is a mapping template for a GraphQL query `getThing(foo:
 String!, bar: String!)`:

```
{
    "version" : "2017-02-28",
    "operation" : "GetItem",
    "key" : {
        "foo" : $util.dynamodb.toDynamoDBJson($ctx.args.foo),
        "bar" : $util.dynamodb.toDynamoDBJson($ctx.args.bar)
    },
    "consistentRead" : true
}
```

For more information about the DynamoDB `GetItem` API, see the [DynamoDB API
documentation](../../../amazondynamodb/latest/APIReference/API_GetItem.md "../../../amazondynamodb/latest/APIReference/API_GetItem.md").
