# GetItem

The `GetItem` request lets you tell the AWS AppSync DynamoDB function to make a
`GetItem` request to DynamoDB, and enables you to specify:

- The key of the item in DynamoDB
- Whether to use a consistent read or not
  The `GetItem` request has the following structure:

```
type DynamoDBGetItem = {
  operation: 'GetItem';
  key: { [key: string]: any };
  consistentRead?: ConsistentRead;
  projection?: {
    expression: string;
    expressionNames?: { [key: string]: string };
  };
};
```

The fields are defined as follows:

## GetItem fields

**`operation`**

The DynamoDB operation to perform. To perform the `GetItem`
DynamoDB operation, this must be set to `GetItem`. This value
is required.

**`key`**

The key of the item in DynamoDB. DynamoDB items may have a single hash key,
or a hash key and sort key, depending on the table structure. For more
information about how to specify a “typed value”, see [Type system (request mapping)](js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-typed-values-request "js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-typed-values-request"). This value is required.

**`consistentRead`**

Whether or not to perform a strongly consistent read with DynamoDB. This
is optional, and defaults to `false`.

**`projection`**

A projection that's used to specify the attributes to return from the
DynamoDB operation. For more information about projections, see [Projections](js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-projections "js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-projections"). This field is optional.

The item returned from DynamoDB is automatically converted into GraphQL and JSON primitive
types, and is available in the context result (`context.result`).

For more information about DynamoDB type conversion, see [Type system (response mapping)](js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-typed-values-responses "js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-typed-values-responses").

For more information about JavaScript resolvers, see [JavaScript resolvers
overview](resolver-reference-overview-js.md "resolver-reference-overview-js.md").

## Example

The following example is a function request handler for a GraphQL query
`getThing(foo: String!, bar: String!)`:

```
export function request(ctx) {
  const {foo, bar} = ctx.args
  return {
    operation : "GetItem",
    key : util.dynamodb.toMapValues({foo, bar}),
    consistentRead : true
  }
}
```

For more information about the DynamoDB `GetItem` API, see the [DynamoDB
API documentation](../../../amazondynamodb/latest/APIReference/API_GetItem.md "../../../amazondynamodb/latest/APIReference/API_GetItem.md").
