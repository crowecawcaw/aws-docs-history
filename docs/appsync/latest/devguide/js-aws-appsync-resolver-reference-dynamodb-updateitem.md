# UpdateItem

The `UpdateItem` request enables you to tell the AWS AppSync DynamoDB function to
make a `UpdateItem` request to DynamoDB and allows you to specify the
following:

- The key of the item in DynamoDB
- An update expression describing how to update the item in DynamoDB
- Conditions for the operation to succeed
  The `UpdateItem` request has the following structure:

```
type DynamoDBUpdateItemRequest = {
  operation: 'UpdateItem';
  key: { [key: string]: any };
  update: {
    expression: string;
    expressionNames?: { [key: string]: string };
    expressionValues?: { [key: string]: any };
  };
  condition?: ConditionCheckExpression;
  customPartitionKey?: string;
  populateIndexFields?: boolean;
  _version?: number;
};
```

The fields are defined as follows:

## UpdateItem fields

**`operation`**

The DynamoDB operation to perform. To perform the `UpdateItem`
DynamoDB operation, this must be set to `UpdateItem`. This
value is required.

**`key`**

The key of the item in DynamoDB. DynamoDB items may have a single hash key,
or a hash key and sort key, depending on the table structure. For more
information about specifying a “typed value”, see [Type system (request mapping)](js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-typed-values-request "js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-typed-values-request"). This value is required.

**`update`**

The `update` section lets you specify an update expression
that describes how to update the item in DynamoDB. For more information
about how to write update expressions, see the [DynamoDB UpdateExpressions documentation](../../../amazondynamodb/latest/developerguide/Expressions.md "../../../amazondynamodb/latest/developerguide/Expressions.md"). This section is
required.

The `update` section has three components:

**`expression`**

The update expression. This value is required.

**`expressionNames`**

The substitutions for expression attribute
_name_ placeholders, in the form of
key-value pairs. The key corresponds to a name placeholder used
in the `expression`, and the value must be a string
corresponding to the attribute name of the item in DynamoDB. This
field is optional, and should only be populated with
substitutions for expression attribute name placeholders used in
the `expression`.

**`expressionValues`**

The substitutions for expression attribute
_value_ placeholders, in the form of
key-value pairs. The key corresponds to a value placeholder used
in the `expression`, and the value must be a typed
value. For more information about how to specify a “typed
value”, see [Type system (request mapping)](js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-typed-values-request "js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-typed-values-request"). This must be
specified. This field is optional, and should only be populated
with substitutions for expression attribute value placeholders
used in the `expression`.

**`condition`**

A condition to determine if the request should succeed or not, based
on the state of the object already in DynamoDB. If no condition is
specified, the `UpdateItem` request updates the existing entry
regardless of its current state. For more information about conditions,
see [Condition expressions](js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-condition-expressions "js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-condition-expressions"). This value is optional.

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

The item updated in DynamoDB is automatically converted into GraphQL and JSON primitive
types and is available in the context result (`context.result`).

For more information about DynamoDB type conversion, see [Type system (response mapping)](js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-typed-values-responses "js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-typed-values-responses").

For more information about JavaScript resolvers, see [JavaScript resolvers
overview](resolver-reference-overview-js.md "resolver-reference-overview-js.md").

## Example 1

The following example is a function request handler for the GraphQL mutation
`upvote(id: ID!)`.

In this example, an item in DynamoDB has its `upvotes` and
`version` fields incremented by 1.

```
import { util } from '@aws-appsync/utils';
export function request(ctx) {
  const { id } = ctx.args;
  return {
    operation: 'UpdateItem',
    key: util.dynamodb.toMapValues({ id }),
    update: {
      expression: 'ADD #votefield :plusOne, version :plusOne',
      expressionNames: { '#votefield': 'upvotes' },
      expressionValues: { ':plusOne': { N: 1 } },
    },
  };
}
```

## Example 2

The following example is a function request handler for a GraphQL mutation
`updateItem(id: ID!, title: String, author: String, expectedVersion:
 Int!)`.

This is a complex example that inspects the arguments and dynamically generates the
update expression that only includes the arguments that have been provided by the
client. For example, if `title` and `author` are omitted, they are
not updated. If an argument is specified but its value is `null`, then that
field is deleted from the object in DynamoDB. Finally, the operation has a condition, which
verifies whether the item currently in DynamoDB has the `version` field set to
`expectedVersion`:

```
import { util } from '@aws-appsync/utils';
export function request(ctx) {
  const { args: { input: { id, ...values } } } = ctx;

  const condition = {
    id: { attributeExists: true },
    version: { eq: values.expectedVersion },
  };
  values.expectedVersion += 1;
  return dynamodbUpdateRequest({ keys: { id }, values, condition });
}


/**
 * Helper function to update an item
 * @returns an UpdateItem request
 */
function dynamodbUpdateRequest(params) {
  const { keys, values, condition: inCondObj } = params;

  const sets = [];
  const removes = [];
  const expressionNames = {};
  const expValues = {};

  // Iterate through the keys of the values
  for (const [key, value] of Object.entries(values)) {
    expressionNames[`#${key}`] = key;
    if (value) {
      sets.push(`#${key} = :${key}`);
      expValues[`:${key}`] = value;
    } else {
      removes.push(`#${key}`);
    }
  }

  let expression = sets.length ? `SET ${sets.join(', ')}` : '';
  expression += removes.length ? ` REMOVE ${removes.join(', ')}` : '';

  const condition = JSON.parse(
    util.transform.toDynamoDBConditionExpression(inCondObj)
  );

  return {
    operation: 'UpdateItem',
    key: util.dynamodb.toMapValues(keys),
    condition,
    update: {
      expression,
      expressionNames,
      expressionValues: util.dynamodb.toMapValues(expValues),
    },
  };
}
```

For more information about the DynamoDB `UpdateItem` API, see the [DynamoDB
API documentation](../../../amazondynamodb/latest/APIReference/API_UpdateItem.md "../../../amazondynamodb/latest/APIReference/API_UpdateItem.md").
