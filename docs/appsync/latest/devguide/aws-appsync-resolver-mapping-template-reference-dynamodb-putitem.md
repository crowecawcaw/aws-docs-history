# PutItem

The `PutItem` request mapping document lets you tell the AWS AppSync DynamoDB
resolver to make a `PutItem` request to DynamoDB, and enables you to specify the
following:

- The key of the item in DynamoDB
- The full contents of the item (composed of `key` and
  `attributeValues`)
- Conditions for the operation to succeed
  The `PutItem` mapping document has the following structure:

```
{
    "version" : "2018-05-29",
    "operation" : "PutItem",
    "customPartitionKey" : "foo",
    "populateIndexFields" : boolean value,
    "key": {
        "foo" : ... typed value,
        "bar" : ... typed value
    },
    "attributeValues" : {
        "baz" : ... typed value
    },
    "condition" : {
       ...
    },
    "_version" : 1
}
```

The fields are defined as follows:

## PutItem fields

**`version`**

The template definition version. `2017-02-28` and
`2018-05-29` are currently supported. This value is
required.

**`operation`**

The DynamoDB operation to perform. To perform the `PutItem`
DynamoDB operation, this must be set to `PutItem`. This value
is required.

**`key`**

The key of the item in DynamoDB. DynamoDB items may have a single hash key,
or a hash key and sort key, depending on the table structure. For more
information about how to specify a “typed value”, see [Type system (request mapping)](aws-appsync-resolver-mapping-template-reference-dynamodb-typed-values-request.md "aws-appsync-resolver-mapping-template-reference-dynamodb-typed-values-request.md"). This value is required.

**`attributeValues`**

The rest of the attributes of the item to be put into DynamoDB. For
more information about how to specify a “typed value”, see [Type system (request mapping)](aws-appsync-resolver-mapping-template-reference-dynamodb-typed-values-request.md "aws-appsync-resolver-mapping-template-reference-dynamodb-typed-values-request.md"). This field is optional.

**`condition`**

A condition to determine if the request should succeed or not, based
on the state of the object already in DynamoDB. If no condition is
specified, the `PutItem` request overwrites any existing entry
for that item. For more information about conditions, see [Condition expressions](aws-appsync-resolver-mapping-template-reference-dynamodb-condition-expressions.md "aws-appsync-resolver-mapping-template-reference-dynamodb-condition-expressions.md"). This value is optional.

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

The item written to DynamoDB is automatically converted into GraphQL and JSON primitive
types and is available in the mapping context (`$context.result`).

For more information about DynamoDB type conversion, see [Type system (response mapping)](aws-appsync-resolver-mapping-template-reference-dynamodb-typed-values-responses.md "aws-appsync-resolver-mapping-template-reference-dynamodb-typed-values-responses.md").

For more information about response mapping templates, see [Resolver mapping
template overview](resolver-mapping-template-reference-overview.md#aws-appsync-resolver-mapping-template-reference-overview "resolver-mapping-template-reference-overview.md#aws-appsync-resolver-mapping-template-reference-overview").

## Example 1

The following example is a mapping template for a GraphQL mutation
`updateThing(foo: String!, bar: String!, name: String!, version:
 Int!)`.

If no item with the specified key exists, it’s created. If an item already exists
with the specified key, it’s overwritten.

```
{
    "version" : "2017-02-28",
    "operation" : "PutItem",
    "key": {
        "foo" : $util.dynamodb.toDynamoDBJson($ctx.args.foo),
        "bar" : $util.dynamodb.toDynamoDBJson($ctx.args.bar)
    },
    "attributeValues" : {
        "name"    : $util.dynamodb.toDynamoDBJson($ctx.args.name),
        "version" : $util.dynamodb.toDynamoDBJson($ctx.args.version)
    }
}
```

## Example 2

The following example is a mapping template for a GraphQL mutation
`updateThing(foo: String!, bar: String!, name: String!, expectedVersion:
 Int!)`.

This example checks to be sure the item currently in DynamoDB has the
`version` field set to `expectedVersion`.

```
{
    "version" : "2017-02-28",
    "operation" : "PutItem",
    "key": {
        "foo" : $util.dynamodb.toDynamoDBJson($ctx.args.foo),
        "bar" : $util.dynamodb.toDynamoDBJson($ctx.args.bar)
    },
    "attributeValues" : {
        "name"    : $util.dynamodb.toDynamoDBJson($ctx.args.name),
        #set( $newVersion = $context.arguments.expectedVersion + 1 )
        "version" : $util.dynamodb.toDynamoDBJson($newVersion)
    },
    "condition" : {
        "expression" : "version = :expectedVersion",
        "expressionValues" : {
            ":expectedVersion" : $util.dynamodb.toDynamoDBJson($expectedVersion)
        }
    }
}
```

For more information about the DynamoDB `PutItem` API, see the [DynamoDB
API documentation](../../../amazondynamodb/latest/APIReference/API_PutItem.md "../../../amazondynamodb/latest/APIReference/API_PutItem.md").
