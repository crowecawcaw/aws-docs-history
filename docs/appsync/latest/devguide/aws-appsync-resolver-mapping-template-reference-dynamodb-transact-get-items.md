# TransactGetItems

The `TransactGetItems` request mapping document lets you to tell the AWS AppSync DynamoDB resolver to
make a `TransactGetItems` request to DynamoDB to retrieve multiple items, potentially across multiple
tables. For this request template, you must specify the following:

- The table name of each request item where to retrieve the item from
- The key of each request item to retrieve from each table
  The DynamoDB `TransactGetItems` limits apply and **no condition
  expression** can be provided.

The `TransactGetItems` mapping document has the following structure:

```
{
    "version": "2018-05-29",
    "operation": "TransactGetItems",
    "transactItems": [
       ## First request item
       {
           "table": "table1",
           "key": {
               "foo": ... typed value,
               "bar": ... typed value
           },
           "projection" : {
                ...
           }
       },
       ## Second request item
       {
           "table": "table2",
           "key": {
               "foo": ... typed value,
               "bar": ... typed value
           },
           "projection" : {
                ...
           }
       }
    ]
}
```

The fields are defined as follows:

## TransactGetItems fields

**`version`**

The template definition version. Only `2018-05-29` is supported. This value is
required.

**`operation`**

The DynamoDB operation to perform. To perform the `TransactGetItems` DynamoDB
operation, this must be set to `TransactGetItems`. This value is required.

**`transactItems`**

The request items to include. The value is an array of request items. At least one request
item must be provided. This `transactItems` value is required.

**`table`**

The DynamoDB table to retrieve the item from. The value is a string of the table
name. This `table` value is required.

**`key`**

The DynamoDB key representing the primary key of the item to
retrieve. DynamoDB items may have a single hash key, or a hash key
and sort key, depending on the table structure. For more
information about how to specify a “typed value”, see [Type system (request mapping)](aws-appsync-resolver-mapping-template-reference-dynamodb-typed-values-request.md "aws-appsync-resolver-mapping-template-reference-dynamodb-typed-values-request.md").

**`projection`**

A projection that's used to specify the attributes to return
from the DynamoDB operation. For more information about
projections, see [Projections](resolver-mapping-template-reference-dynamodb.md#aws-appsync-resolver-mapping-template-reference-dynamodb-projections "resolver-mapping-template-reference-dynamodb.md#aws-appsync-resolver-mapping-template-reference-dynamodb-projections"). This field is optional.

Things to remember:

- If a transaction succeeds, the order of retrieved items in the `items` block will be the
  same as the order of request items.
- Transactions are performed in an all-or-nothing way. If any request item causes an error, the whole
  transaction will not be performed and error details will be returned.
- A request item being unable to be retrieved is not an error. Instead, a _null_ element appears in the _items_ block in the corresponding position.
- If the error of a transaction is _TransactionCanceledException_, the `cancellationReasons` block will be
  populated. The order of cancellation reasons in `cancellationReasons` block will be the same
  as the order of request items.
- `TransactGetItems` is limited to 100 request items.
  For the following example request mapping template:

```
{
    "version": "2018-05-29",
    "operation": "TransactGetItems",
    "transactItems": [
       ## First request item
       {
           "table": "posts",
           "key": {
               "post_id": {
                 "S": "p1"
               }
           }
       },
       ## Second request item
       {
           "table": "authors",
           "key": {
               "author_id": {
                 "S": a1
               }
           }
       }
    ]
}
```

If the transaction succeeds and only the first requested item is retrieved, the invocation result available
in `$ctx.result` is as follows:

```
{
    "items": [
       {
           // Attributes of the first requested item
           "post_id": "p1",
           "post_title": "title",
           "post_description": "description"
       },
       // Could not retrieve the second requested item
       null,
    ],
    "cancellationReasons": null
}
```

If the transaction fails due to _TransactionCanceledException_
caused by the first request item, the invocation result available in `$ctx.result` is as
follows:

```
{
    "items": null,
    "cancellationReasons": [
       {
           "type":"Sample error type",
           "message":"Sample error message"
       },
       {
           "type":"None",
           "message":"None"
       }
    ]
}
```

The `$ctx.error` contains details about the error. The keys **items** and **cancellationReasons** are guaranteed to be present in
`$ctx.result`.

For a more complete example, follow the DynamoDB Transaction tutorial with AppSync here
[Tutorial: DynamoDB transaction
resolvers](tutorial-dynamodb-transact.md#aws-appsync-tutorial-dynamodb-transact "tutorial-dynamodb-transact.md#aws-appsync-tutorial-dynamodb-transact").
