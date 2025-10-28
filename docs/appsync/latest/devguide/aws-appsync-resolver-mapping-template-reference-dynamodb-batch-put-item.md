# BatchPutItem

The `BatchPutItem` request mapping document lets you tell the AWS AppSync DynamoDB resolver to make a
`BatchWriteItem` request to DynamoDB to put multiple items, potentially across multiple tables. For
this request template, you must specify the following:

- The table names where to put the items in
- The full items to put in each table
  The DynamoDB `BatchWriteItem` limits apply and **no
  condition expression** can be provided.

The `BatchPutItem` mapping document has the following structure:

```
{
    "version" : "2018-05-29",
    "operation" : "BatchPutItem",
    "tables" : {
        "table1": [
        ## Item to put
        {
             "foo" : ... typed value,
             "bar" : ... typed value
        },
        ## Item2 to put
        {
             "foo" : ... typed value,
             "bar" : ... typed value
        }],
        "table2": [
        ## Item3 to put
        {
             "foo" : ... typed value,
             "bar" : ... typed value
        },
        ## Item4 to put
        {
             "foo" : ... typed value,
             "bar" : ... typed value
        }],
    }
}
```

The fields are defined as follows:

## BatchPutItem fields

**`version`**

The template definition version. Only `2018-05-29` is supported. This value is
required.

**`operation`**

The DynamoDB operation to perform. To perform the `BatchPutItem` DynamoDB
operation, this must be set to `BatchPutItem`. This value is required.

**`tables`**

The DynamoDB tables to put the items in. Each table entry represents a list of DynamoDB items to
insert for this specific table. At least one table must be provided. This value is
required.

Things to remember:

- The fully inserted items are returned in the response, if successful.
- If an item hasn’t been inserted in the table, a _null_
  element is displayed in the data block for that table.
- The inserted items are sorted per table, based on the order in which they were
  provided inside the request mapping template.
- Each `Put` command inside a `BatchPutItem` is atomic,
  however, a batch can be partially processed. If a batch is partially processed due to
  an error, the unprocessed keys are returned as part of the invocation result inside
  the _unprocessedKeys_ block.
- `BatchPutItem` is limited to 25 items.
- This operation **is not** supported when used with
  conflict detection. Using both at the same time may result in an error.
  For the following example request mapping template:

```
{
  "version": "2018-05-29",
  "operation": "BatchPutItem",
  "tables": {
    "authors": [
        {
          "author_id": {
            "S": "a1"
          },
          "author_name": {
            "S": "a1_name"
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
          },
          "post_title": {
            "S": "title"
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
     "authors": [
         null
     ],
     "posts": [
        # Was inserted
        {
          "author_id": "a1",
          "post_id": "p2",
          "post_title": "title"
        }
     ]
   },
   "unprocessedItems": {
     "authors": [
        # This item was not processed due to an error
        {
          "author_id": "a1",
          "author_name": "a1_name"
        }
      ],
     "posts": []
   }
}
```

The `$ctx.error` contains details about the error. The keys **data**, **unprocessedItems**, and each table key that was provided in
the request mapping template are guaranteed to be present in the invocation result. Items that have been
inserted are in the **data** block. Items that haven’t been processed are marked
as _null_ inside the data block and are placed inside the **unprocessedItems** block.

For a more complete example, follow the DynamoDB Batch tutorial with AppSync here [Tutorial: DynamoDB batch
resolvers](tutorial-dynamodb-batch.md#aws-appsync-tutorial-dynamodb-batch "tutorial-dynamodb-batch.md#aws-appsync-tutorial-dynamodb-batch").
