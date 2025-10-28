# DeleteItem

The `DeleteItem` request lets you tell the AWS AppSync DynamoDB function to make a
`DeleteItem` request to DynamoDB, and enables you to specify the
following:

- The key of the item in DynamoDB
- Conditions for the operation to succeed
  The `DeleteItem` request has the following structure:

```
type DynamoDBDeleteItemRequest = {
  operation: 'DeleteItem';
  key: { [key: string]: any };
  condition?: ConditionCheckExpression;
  customPartitionKey?: string;
  populateIndexFields?: boolean;
  _version?: number;
};
```

The fields are defined as follows:

## DeleteItem fields

**`operation`**

The DynamoDB operation to perform. To perform the `DeleteItem`
DynamoDB operation, this must be set to `DeleteItem`. This
value is required.

**`key`**

The key of the item in DynamoDB. DynamoDB items may have a single hash key,
or a hash key and sort key, depending on the table structure. For more
information about specifying a “typed value”, see [Type system (request mapping)](js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-typed-values-request "js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-typed-values-request"). This value is required.

**`condition`**

A condition to determine if the request should succeed or not, based
on the state of the object already in DynamoDB. If no condition is
specified, the `DeleteItem` request deletes an item regardless
of its current state. For more information about conditions, see [Condition expressions](js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-condition-expressions "js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-condition-expressions"). This value is optional.

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

The item deleted from DynamoDB is automatically converted into GraphQL and JSON primitive
types and is available in the context result (`context.result`).

For more information about DynamoDB type conversion, see [Type system (response mapping)](js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-typed-values-responses "js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-typed-values-responses").

For more information about JavaScript resolvers, see [JavaScript resolvers
overview](resolver-reference-overview-js.md "resolver-reference-overview-js.md").

## Example 1

The following example is a function request handler for a GraphQL mutation
`deleteItem(id: ID!)`. If an item exists with this ID, it’s
deleted.

```
import { util } from '@aws-appsync/utils';
export function request(ctx) {
  return {
    operation: 'DeleteItem',
    key: util.dynamodb.toMapValues({ id: ctx.args.id }),
  };
}
```

## Example 2

The following example is a function request handler for a GraphQL mutation
`deleteItem(id: ID!, expectedVersion: Int!)`. If an item exists with this
ID, it’s deleted, but only if its `version` field set to
`expectedVersion`:

```
import { util } from '@aws-appsync/utils';

export function request(ctx) {
  const { id, expectedVersion } = ctx.args;
  const condition = {
    id: { attributeExists: true },
    version: { eq: expectedVersion },
  };
  return {
    operation: 'DeleteItem',
    key: util.dynamodb.toMapValues({ id }),
    condition: util.transform.toDynamoDBConditionExpression(condition),
  };
}
```

For more information about the DynamoDB `DeleteItem` API, see the [DynamoDB
API documentation](../../../amazondynamodb/latest/APIReference/API_DeleteItem.md "../../../amazondynamodb/latest/APIReference/API_DeleteItem.md").
