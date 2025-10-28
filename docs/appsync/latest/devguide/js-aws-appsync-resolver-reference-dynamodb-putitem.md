# PutItem

The `PutItem` request mapping document lets you tell the AWS AppSync DynamoDB
function to make a `PutItem` request to DynamoDB, and enables you to specify the
following:

- The key of the item in DynamoDB
- The full contents of the item (composed of `key` and
  `attributeValues`)
- Conditions for the operation to succeed
  The `PutItem` request has the following structure:

```
type DynamoDBPutItemRequest = {
  operation: 'PutItem';
  key: { [key: string]: any };
  attributeValues: { [key: string]: any};
  condition?: ConditionCheckExpression;
  customPartitionKey?: string;
  populateIndexFields?: boolean;
  _version?: number;
};
```

The fields are defined as follows:

## PutItem fields

**`operation`**

The DynamoDB operation to perform. To perform the `PutItem`
DynamoDB operation, this must be set to `PutItem`. This value
is required.

**`key`**

The key of the item in DynamoDB. DynamoDB items may have a single hash key,
or a hash key and sort key, depending on the table structure. For more
information about how to specify a “typed value”, see [Type system (request mapping)](js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-typed-values-request "js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-typed-values-request"). This value is required.

**`attributeValues`**

The rest of the attributes of the item to be put into DynamoDB. For
more information about how to specify a “typed value”, see [Type system (request mapping)](js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-typed-values-request "js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-typed-values-request"). This field is optional.

**`condition`**

A condition to determine if the request should succeed or not, based
on the state of the object already in DynamoDB. If no condition is
specified, the `PutItem` request overwrites any existing entry
for that item. For more information about conditions, see [Condition expressions](js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-condition-expressions "js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-condition-expressions"). This value is optional.

**`_version`**

A numeric value that represents the latest known version of an item.
This value is optional. This field is used for _Conflict Detection_ and is only
supported on versioned data sources.

**`customPartitionKey`**

When enabled, this string value modifies the format of the
`ds_sk` and `ds_pk` records used by the delta
sync table when versioning has been enabled (for more information, see
[Conflict detection and sync](conflict-detection-and-sync.md "conflict-detection-and-sync.md") in the
_AWS AppSync Developer Guide_). When enabled, the processing of
the `populateIndexFields` entry is also enabled. This field is
optional.

**`populateIndexFields`**

A boolean value that, when enabled **along with
the `customPartitionKey`**, creates new entries
for each record in the delta sync table, specifically in the
`gsi_ds_pk` and `gsi_ds_sk` columns. For more
information, see [Conflict detection and sync](conflict-detection-and-sync.md "conflict-detection-and-sync.md") in the
_AWS AppSync Developer Guide_. This field is optional.

The item written to DynamoDB is automatically converted to GraphQL and
JSON primitive types and is available in the context result
(`context.result`).

The item written to DynamoDB is automatically converted into GraphQL and JSON primitive
types and is available in the context result (`context.result`).

For more information about DynamoDB type conversion, see [Type system (response mapping)](js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-typed-values-responses "js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-typed-values-responses").

For more information about JavaScript resolvers, see [JavaScript
resolvers overview](resolver-reference-overview-js.md "resolver-reference-overview-js.md").

## Example 1

The following example is a function request handler for a GraphQL mutation
`updateThing(foo: String!, bar: String!, name: String!, version:
 Int!)`.

If no item with the specified key exists, it’s created. If an item already exists
with the specified key, it’s overwritten.

```
import { util } from '@aws-appsync/utils';
export function request(ctx) {
  const { foo, bar, ...values} = ctx.args
  return {
    operation: 'PutItem',
    key: util.dynamodb.toMapValues({foo, bar}),
    attributeValues: util.dynamodb.toMapValues(values),
  };
}
```

## Example 2

The following example is a function request handler for a GraphQL mutation
`updateThing(foo: String!, bar: String!, name: String!, expectedVersion:
 Int!)`.

This example verifies that the item currently in DynamoDB has the `version`
field set to `expectedVersion`.

```
import { util } from '@aws-appsync/utils';
export function request(ctx) {
  const { foo, bar, name, expectedVersion } = ctx.args;
  const values = { name, version: expectedVersion + 1 };
  let condition = util.transform.toDynamoDBConditionExpression({
    version: { eq: expectedVersion },
  });

  return {
    operation: 'PutItem',
    key: util.dynamodb.toMapValues({ foo, bar }),
    attributeValues: util.dynamodb.toMapValues(values),
    condition,
  };
}
```

For more information about the DynamoDB `PutItem` API, see the [DynamoDB
API documentation](../../../amazondynamodb/latest/APIReference/API_PutItem.md "../../../amazondynamodb/latest/APIReference/API_PutItem.md").
