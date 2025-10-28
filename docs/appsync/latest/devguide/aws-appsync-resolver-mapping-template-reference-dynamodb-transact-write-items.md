# TransactWriteItems

The `TransactWriteItems` request mapping document lets you tell the AWS AppSync DynamoDB resolver to make
a `TransactWriteItems` request to DynamoDB to write multiple items, potentially to multiple tables. For
this request template, you must specify the following:

- The destination table name of each request item
- The operation of each request item to perform. There are four types of operations that are supported:
  _PutItem_, _UpdateItem_, _DeleteItem_, and _ConditionCheck_
- The key of each request item to write
  The DynamoDB `TransactWriteItems` limits apply.

The `TransactWriteItems` mapping document has the following structure:

```
{
    "version": "2018-05-29",
    "operation": "TransactWriteItems",
    "transactItems": [
       {
           "table": "table1",
           "operation": "PutItem",
           "key": {
               "foo": ... typed value,
               "bar": ... typed value
           },
           "attributeValues": {
               "baz": ... typed value
           },
           "condition": {
               "expression": "someExpression",
               "expressionNames": {
                   "#foo": "foo"
               },
               "expressionValues": {
                   ":bar": ... typed value
               },
               "returnValuesOnConditionCheckFailure": true|false
           }
       },
       {
           "table":"table2",
           "operation": "UpdateItem",
           "key": {
               "foo": ... typed value,
               "bar": ... typed value
           },
           "update": {
               "expression": "someExpression",
               "expressionNames": {
                   "#foo": "foo"
               },
               "expressionValues": {
                   ":bar": ... typed value
               }
           },
           "condition": {
               "expression": "someExpression",
               "expressionNames": {
                   "#foo":"foo"
               },
               "expressionValues": {
                   ":bar": ... typed value
               },
               "returnValuesOnConditionCheckFailure": true|false
           }
       },
       {
           "table": "table3",
           "operation": "DeleteItem",
           "key":{
               "foo": ... typed value,
               "bar": ... typed value
           },
           "condition":{
               "expression": "someExpression",
               "expressionNames": {
                   "#foo": "foo"
               },
               "expressionValues": {
                   ":bar": ... typed value
               },
               "returnValuesOnConditionCheckFailure": true|false
           }
       },
       {
           "table": "table4",
           "operation": "ConditionCheck",
           "key":{
               "foo": ... typed value,
               "bar": ... typed value
           },
           "condition":{
               "expression": "someExpression",
               "expressionNames": {
                   "#foo": "foo"
               },
               "expressionValues": {
                   ":bar": ... typed value
               },
               "returnValuesOnConditionCheckFailure": true|false
           }
       }
    ]
}
```

## TransactWriteItems fields

**The fields are defined as follows:**

**`version`**

The template definition version. Only `2018-05-29` is supported. This
value is required.

**`operation`**

The DynamoDB operation to perform. To perform the `TransactWriteItems`
DynamoDB operation, this must be set to `TransactWriteItems`. This value
is required.

**`transactItems`**

The request items to include. The value is an array of request items. At least
one request item must be provided. This `transactItems` value is
required.

For `PutItem`, the fields are defined as follows:

**`table`**

The destination DynamoDB table. The value is a string of the table name.
This `table` value is required.

**`operation`**

The DynamoDB operation to perform. To perform the `PutItem`
DynamoDB operation, this must be set to `PutItem`. This value is
required.

**`key`**

The DynamoDB key representing the primary key of the
item to put. DynamoDB items may have a single hash key, or
a hash key and sort key, depending on the table
structure. For more information about how to specify a
“typed value”, see [Type system (request mapping)](aws-appsync-resolver-mapping-template-reference-dynamodb-typed-values-request.md "aws-appsync-resolver-mapping-template-reference-dynamodb-typed-values-request.md"). This value is
required.

**`attributeValues`**

The rest of the attributes of the item to be put
into DynamoDB. For more information about how to
specify a “typed value”, see [Type system (request mapping)](aws-appsync-resolver-mapping-template-reference-dynamodb-typed-values-request.md "aws-appsync-resolver-mapping-template-reference-dynamodb-typed-values-request.md"). This field is
optional.

**`condition`**

A condition to determine if the request should
succeed or not, based on the state of the object
already in DynamoDB. If no condition is specified, the
`PutItem` request overwrites any existing
entry for that item. You can specify whether to
retrieve the existing item back when condition check
fails. For more information about transactional
conditions, see [Transaction condition expressions](aws-appsync-resolver-mapping-template-reference-dynamodb-transaction-condition-expressions.md "aws-appsync-resolver-mapping-template-reference-dynamodb-transaction-condition-expressions.md"). This
value is optional.

For `UpdateItem`, the fields are defined as follows:

**`table`**

The DynamoDB table to update. The value is a string of the table name. This
`table` value is required.

**`operation`**

The DynamoDB operation to perform. To perform the `UpdateItem`
DynamoDB operation, this must be set to `UpdateItem`. This value
is required.

**`key`**

The DynamoDB key representing the primary key of the
item to update. DynamoDB items may have a single hash key,
or a hash key and sort key, depending on the table
structure. For more information about how to specify a
“typed value”, see [Type system (request mapping)](aws-appsync-resolver-mapping-template-reference-dynamodb-typed-values-request.md "aws-appsync-resolver-mapping-template-reference-dynamodb-typed-values-request.md"). This value is
required.

**`update`**

The `update` section lets you specify an update expression
that describes how to update the item in DynamoDB. For more information about
how to write update expressions, see the [DynamoDB UpdateExpressions documentation](../../../amazondynamodb/latest/developerguide/Expressions.md "../../../amazondynamodb/latest/developerguide/Expressions.md"). This section is
required.

**`condition`**

A condition to determine if the request should
succeed or not, based on the state of the object
already in DynamoDB. If no condition is specified, the
`UpdateItem` request updates the existing
entry regardless of its current state. You can specify
whether to retrieve the existing item back when
condition check fails. For more information about
transactional conditions, see [Transaction condition expressions](aws-appsync-resolver-mapping-template-reference-dynamodb-transaction-condition-expressions.md "aws-appsync-resolver-mapping-template-reference-dynamodb-transaction-condition-expressions.md"). This
value is optional.

For `DeleteItem`, the fields are defined as follows:

**`table`**

The DynamoDB table in which to delete the item. The value is a string of
the table name. This `table` value is required.

**`operation`**

The DynamoDB operation to perform. To perform the `DeleteItem`
DynamoDB operation, this must be set to `DeleteItem`. This value
is required.

**`key`**

The DynamoDB key representing the primary key of the
item to delete. DynamoDB items may have a single hash key,
or a hash key and sort key, depending on the table
structure. For more information about how to specify a
“typed value”, see [Type system (request mapping)](aws-appsync-resolver-mapping-template-reference-dynamodb-typed-values-request.md "aws-appsync-resolver-mapping-template-reference-dynamodb-typed-values-request.md"). This value is
required.

**`condition`**

A condition to determine if the request should
succeed or not, based on the state of the object
already in DynamoDB. If no condition is specified, the
`DeleteItem` request deletes an item
regardless of its current state. You can specify
whether to retrieve the existing item back when
condition check fails. For more information about
transactional conditions, see [Transaction condition expressions](aws-appsync-resolver-mapping-template-reference-dynamodb-transaction-condition-expressions.md "aws-appsync-resolver-mapping-template-reference-dynamodb-transaction-condition-expressions.md"). This
value is optional.

For `ConditionCheck`, the fields are defined as follows:

**`table`**

The DynamoDB table in which to check the condition. The value is a string
of the table name. This `table` value is required.

**`operation`**

The DynamoDB operation to perform. To perform the
`ConditionCheck` DynamoDB operation, this must be set to
`ConditionCheck`. This value is required.

**`key`**

The DynamoDB key representing the primary key of the
item to condition check. DynamoDB items may have a single
hash key, or a hash key and sort key, depending on the
table structure. For more information about how to
specify a “typed value”, see [Type system (request mapping)](aws-appsync-resolver-mapping-template-reference-dynamodb-typed-values-request.md "aws-appsync-resolver-mapping-template-reference-dynamodb-typed-values-request.md"). This value is
required.

**`condition`**

A condition to determine if the request should
succeed or not, based on the state of the object
already in DynamoDB. You can specify whether to retrieve
the existing item back when condition check fails. For
more information about transactional conditions, see
[Transaction condition expressions](aws-appsync-resolver-mapping-template-reference-dynamodb-transaction-condition-expressions.md "aws-appsync-resolver-mapping-template-reference-dynamodb-transaction-condition-expressions.md"). This
value is required.

Things to remember:

- Only keys of request items are returned in the response, if successful. The order of keys will be the
  same as the order of request items.
- Transactions are performed in an all-or-nothing way. If any request item causes an error, the whole
  transaction will not be performed and error details will be returned.
- No two request items can target the same item. Otherwise they will cause _TransactionCanceledException_ error.
- If the error of a transaction is _TransactionCanceledException_, the `cancellationReasons` block will be
  populated. If a request item’s condition check fails **and** you did not
  specify `returnValuesOnConditionCheckFailure` to be `false`, the item existing in
  the table will be retrieved and stored in `item` at the corresponding position of
  `cancellationReasons` block.
- `TransactWriteItems` is limited to 100 request items.
- This operation **is not** supported when used with
  conflict detection. Using both at the same time may result in an error.
  For the following example request mapping template:

```
{
    "version": "2018-05-29",
    "operation": "TransactWriteItems",
    "transactItems": [
       {
           "table": "posts",
           "operation": "PutItem",
           "key": {
               "post_id": {
                   "S": "p1"
               }
           },
           "attributeValues": {
               "post_title": {
                   "S": "New title"
               },
               "post_description": {
                   "S": "New description"
               }
           },
           "condition": {
               "expression": "post_title = :post_title",
               "expressionValues": {
                   ":post_title": {
                       "S": "Expected old title"
                   }
               }
           }
       },
       {
           "table":"authors",
           "operation": "UpdateItem",
           "key": {
               "author_id": {
                   "S": "a1"
               },
           },
           "update": {
               "expression": "SET author_name = :author_name",
               "expressionValues": {
                   ":author_name": {
                       "S": "New name"
                   }
               }
           },
       }
    ]
}
```

If the transaction succeeds, the invocation result available in `$ctx.result` is as
follows:

```
{
    "keys": [
       // Key of the PutItem request
       {
           "post_id": "p1",
       },
       // Key of the UpdateItem request
       {
           "author_id": "a1"
       }
    ],
    "cancellationReasons": null
}
```

If the transaction fails due to condition check failure of the `PutItem`
request, the invocation result available in `$ctx.result` is as follows:

```
{
    "keys": null,
    "cancellationReasons": [
       {
           "item": {
               "post_id": "p1",
               "post_title": "Actual old title",
               "post_description": "Old description"
           },
           "type": "ConditionCheckFailed",
           "message": "The condition check failed."
       },
       {
           "type": "None",
           "message": "None"
       }
    ]
}
```

The `$ctx.error` contains details about the error. The keys **keys**
and **cancellationReasons** are guaranteed to be present in
`$ctx.result`.

For a more complete example, follow the DynamoDB Transaction tutorial with AppSync here
[Tutorial: DynamoDB transaction
resolvers](tutorial-dynamodb-transact.md#aws-appsync-tutorial-dynamodb-transact "tutorial-dynamodb-transact.md#aws-appsync-tutorial-dynamodb-transact").
