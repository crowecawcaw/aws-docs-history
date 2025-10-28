# BatchDeleteItem

The `BatchDeleteItem` request mapping document lets you tell the AWS AppSync DynamoDB resolver to make a
`BatchWriteItem` request to DynamoDB to delete multiple items, potentially across multiple tables.
For this request template, you must specify the following:

- The table names where to delete the items from
- The keys of the items to delete from each table
  The DynamoDB `BatchWriteItem` limits apply and **no
  condition expression** can be provided.

The `BatchDeleteItem` mapping document has the following structure:

```
{
    "version" : "2018-05-29",
    "operation" : "BatchDeleteItem",
    "tables" : {
        "table1": [
        ## Item to delete Key
        {
             "foo" : ... typed value,
             "bar" : ... typed value
        },
        ## Item2 to delete Key
        {
             "foo" : ... typed value,
             "bar" : ... typed value
        }],
        "table2": [
        ## Item3 to delete Key
        {
             "foo" : ... typed value,
             "bar" : ... typed value
        },
        ## Item4 to delete Key
        {
             "foo" : ... typed value,
             "bar" : ... typed value
        }],
    }
}
```

The fields are defined as follows:

## BatchDeleteItem fields

**`version`**

The template definition version. Only `2018-05-29` is supported. This value is
required.

**`operation`**

The DynamoDB operation to perform. To perform the `BatchDeleteItem` DynamoDB
operation, this must be set to `BatchDeleteItem`. This value is required.

**`tables`**

The DynamoDB tables to delete the items from. Each table is a list of
DynamoDB keys representing the primary key of the items to delete. DynamoDB
items may have a single hash key, or a hash key and sort key, depending
on the table structure. For more information about how to specify a
“typed value”, see [Type system (request mapping)](aws-appsync-resolver-mapping-template-reference-dynamodb-typed-values-request.md "aws-appsync-resolver-mapping-template-reference-dynamodb-typed-values-request.md"). At least one table must be
provided. The `tables` value is required.

Things to remember:

- Contrary to the `DeleteItem` operation, the fully deleted item isn’t returned in the
  response. Only the passed key is returned.
- If an item has not been deleted from the table, a _null_
  element appears in the data block for that table.
- Invocation results are sorted per table, based on the order in which they were
  provided inside the request mapping template.
- Each `Delete` command inside a `BatchDeleteItem` is atomic.
  However a batch can be partially processed. If a batch is partially processed due to
  an error, the unprocessed keys are returned as part of the invocation result inside
  the _unprocessedKeys_ block.
- `BatchDeleteItem` is limited to 25 keys.
- This operation **is not** supported when used with
  conflict detection. Using both at the same time may result in an error.
  For the following example request mapping template:

```
{
  "version": "2018-05-29",
  "operation": "BatchDeleteItem",
  "tables": {
    "authors": [
        {
          "author_id": {
            "S": "a1"
          }
        },
    ],
    "posts": [
        {
          "author_id": {
            "S": "a1"
          },
          "post_id": {
            "S": "p2"
          }
        }
    ],
  }
}
```

The invocation result available in `$ctx.result` is as follows:

```
{
   "data": {
     "authors": [null],
     "posts": [
        # Was deleted
        {
          "author_id": "a1",
          "post_id": "p2"
        }
     ]
   },
   "unprocessedKeys": {
     "authors": [
        # This key was not processed due to an error
        {
          "author_id": "a1"
        }
      ],
     "posts": []
   }
}
```

The `$ctx.error` contains details about the error. The keys **data**, **unprocessedKeys**, and each
table key that was provided in the request mapping template are guaranteed to be present in
the invocation result. Items that have been deleted are present in the **data** block. Items that haven’t been processed are marked as
_null_ inside the data block and are placed inside the
**unprocessedKeys** block.

For a more complete example, follow the DynamoDB Batch tutorial with AppSync here [Tutorial: DynamoDB batch
resolvers](tutorial-dynamodb-batch.md#aws-appsync-tutorial-dynamodb-batch "tutorial-dynamodb-batch.md#aws-appsync-tutorial-dynamodb-batch").
