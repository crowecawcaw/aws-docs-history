# BatchGetItem

The `BatchGetItem` request mapping document lets you tell the AWS AppSync DynamoDB resolver to make a
`BatchGetItem` request to DynamoDB to retrieve multiple items, potentially across multiple tables.
For this request template, you must specify the following:

- The table names where to retrieve the items from
- The keys of the items to retrieve from each table
  The DynamoDB `BatchGetItem` limits apply and **no condition
  expression** can be provided.

The `BatchGetItem` mapping document has the following structure:

```
{
    "version" : "2018-05-29",
    "operation" : "BatchGetItem",
    "tables" : {
        "table1": {
           "keys": [
              ## Item to retrieve Key
              {
                   "foo" : ... typed value,
                   "bar" : ... typed value
              },
              ## Item2 to retrieve Key
              {
                   "foo" : ... typed value,
                   "bar" : ... typed value
              }
            ],
            "consistentRead": true|false,
            "projection" : {
                 ...
            }
        },
        "table2": {
           "keys": [
              ## Item3 to retrieve Key
              {
                   "foo" : ... typed value,
                   "bar" : ... typed value
              },
              ## Item4 to retrieve Key
              {
                   "foo" : ... typed value,
                   "bar" : ... typed value
              }
            ],
            "consistentRead": true|false,
            "projection" : {
                 ...
            }
        }
    }
}
```

The fields are defined as follows:

## BatchGetItem fields

**`version`**

The template definition version. Only `2018-05-29` is supported. This value is
required.

**`operation`**

The DynamoDB operation to perform. To perform the `BatchGetItem` DynamoDB operation,
this must be set to `BatchGetItem`. This value is required.

**`tables`**

The DynamoDB tables to retrieve the items from. The value is a map where table names are
specified as the keys of the map. At least one table must be provided. This
`tables` value is required.

**`keys`**

List of DynamoDB keys representing the primary key of the items
to retrieve. DynamoDB items may have a single hash key, or a hash
key and sort key, depending on the table structure. For more
information about how to specify a “typed value”, see [Type system (request mapping)](aws-appsync-resolver-mapping-template-reference-dynamodb-typed-values-request.md "aws-appsync-resolver-mapping-template-reference-dynamodb-typed-values-request.md").

**`consistentRead`**

Whether to use a consistent read when executing a _GetItem_ operation. This value is optional and
defaults to _false_.

**`projection`**

A projection that's used to specify the attributes to return
from the DynamoDB operation. For more information about
projections, see [Projections](resolver-mapping-template-reference-dynamodb.md#aws-appsync-resolver-mapping-template-reference-dynamodb-projections "resolver-mapping-template-reference-dynamodb.md#aws-appsync-resolver-mapping-template-reference-dynamodb-projections"). This field is optional.

Things to remember:

- If an item has not been retrieved from the table, a _null_
  element appears in the data block for that table.
- Invocation results are sorted per table, based on the order in which they were
  provided inside the request mapping template.
- Each `Get` command inside a `BatchGetItem` is atomic,
  however, a batch can be partially processed. If a batch is partially processed due to
  an error, the unprocessed keys are returned as part of the invocation result inside
  the _unprocessedKeys_ block.
- `BatchGetItem` is limited to 100 keys.
  For the following example request mapping template:

```
{
  "version": "2018-05-29",
  "operation": "BatchGetItem",
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
        # Was retrieved
        {
          "author_id": "a1",
          "post_id": "p2",
          "post_title": "title",
          "post_description": "description",
        }
     ]
   },
   "unprocessedKeys": {
     "authors": [
        # This item was not processed due to an error
        {
          "author_id": "a1"
        }
      ],
     "posts": []
   }
}
```

The `$ctx.error` contains details about the error. The keys **data**, **unprocessedKeys**, and each table key that was provided in the
request mapping template are guaranteed to be present in the invocation result. Items that have been deleted
appear in the **data** block. Items that haven’t been processed are marked as
_null_ inside the data block and are placed inside the **unprocessedKeys** block.

For a more complete example, follow the DynamoDB Batch tutorial with AppSync here [Tutorial: DynamoDB batch
resolvers](tutorial-dynamodb-batch.md#aws-appsync-tutorial-dynamodb-batch "tutorial-dynamodb-batch.md#aws-appsync-tutorial-dynamodb-batch").
