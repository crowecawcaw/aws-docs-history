# BatchDeleteItem

The `BatchDeleteItem` request object lets you tell the AWS AppSync DynamoDB function
to make a `BatchWriteItem` request to DynamoDB to delete multiple items,
potentially across multiple tables. For this request object, you must specify the
following:

- The table names where to delete the items from
- The keys of the items to delete from each table
  The DynamoDB `BatchWriteItem` limits apply and **no
  condition expression** can be provided.

The `BatchDeleteItem` request object has the following structure:

```
type DynamoDBBatchDeleteItemRequest = {
  operation: 'BatchDeleteItem';
  tables: {
    [tableName: string]: { [key: string]: any }[];
  };
};
```

The fields are defined as follows:

## BatchDeleteItem fields

**`operation`**

The DynamoDB operation to perform. To perform the
`BatchDeleteItem` DynamoDB operation, this must be set to
`BatchDeleteItem`. This value is required.

**`tables`**

The DynamoDB tables to delete the items from. Each table is a list of
DynamoDB keys representing the primary key of the items to delete. DynamoDB
items may have a single hash key, or a hash key and sort key, depending
on the table structure. For more information about how to specify a
“typed value”, see [Type system (request mapping)](js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-typed-values-request "js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-typed-values-request"). At least one table must be
provided. The `tables` value is required.

Things to remember:

- Contrary to the `DeleteItem` operation, the fully deleted item isn’t
  returned in the response. Only the passed key is returned.
- If an item has not been deleted from the table, a _null_ element appears in the data block for that table.
- Invocation results are sorted per table, based on the order in which they were
  provided inside the request object.
- Each `Delete` command inside a `BatchDeleteItem` is atomic.
  However a batch can be partially processed. If a batch is partially processed due to
  an error, the unprocessed keys are returned as part of the invocation result inside
  the _unprocessedKeys_ block.
- `BatchDeleteItem` is limited to 25 keys.
- This operation **is not** supported when used with
  conflict detection. Using both at the same time may result in an error.
  For the following example function request handler:

```
import { util } from '@aws-appsync/utils';

export function request(ctx) {
  const { authorId, postId } = ctx.args;
  return {
    operation: 'BatchDeleteItem',
    tables: {
      authors: [util.dynamodb.toMapValues({ authorId })],
      posts: [util.dynamodb.toMapValues({ authorId, postId })],
    },
  };
}
```

The invocation result available in `ctx.result` is as follows:

```
{
   "data": {
     "authors": [null],
     "posts": [
        // Was deleted
        {
          "authorId": "a1",
          "postId": "p2"
        }
     ]
   },
   "unprocessedKeys": {
     "authors": [
        // This key was not processed due to an error
        {
          "authorId": "a1"
        }
      ],
     "posts": []
   }
}
```

The `ctx.error` contains details about the error. The keys **data**, **unprocessedKeys**, and each
table key that was provided in the function request object are guaranteed to be present in
the invocation result. Items that have been deleted are present in the **data** block. Items that haven’t been processed are marked as
_null_ inside the data block and are placed inside the
**unprocessedKeys** block.
