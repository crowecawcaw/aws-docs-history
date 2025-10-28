# BatchPutItem

The `BatchPutItem` request object lets you tell the AWS AppSync DynamoDB function to
make a `BatchWriteItem` request to DynamoDB to put multiple items, potentially
across multiple tables. For this request object, you must specify the following:

- The table names where to put the items in
- The full items to put in each table
  The DynamoDB `BatchWriteItem` limits apply and **no
  condition expression** can be provided.

The `BatchPutItem` request object has the following structure:

```
type DynamoDBBatchPutItemRequest = {
  operation: 'BatchPutItem';
  tables: {
    [tableName: string]: { [key: string]: any}[];
  };
};
```

The fields are defined as follows:

## BatchPutItem fields

**`operation`**

The DynamoDB operation to perform. To perform the
`BatchPutItem` DynamoDB operation, this must be set to
`BatchPutItem`. This value is required.

**`tables`**

The DynamoDB tables to put the items in. Each table entry represents a
list of DynamoDB items to insert for this specific table. At least one table
must be provided. This value is required.

Things to remember:

- The fully inserted items are returned in the response, if successful.
- If an item hasn’t been inserted in the table, a _null_ element is displayed in the data block for that table.
- The inserted items are sorted per table, based on the order in which they were
  provided inside the request object.
- Each `Put` command inside a `BatchPutItem` is atomic,
  however, a batch can be partially processed. If a batch is partially processed due to
  an error, the unprocessed keys are returned as part of the invocation result inside
  the _unprocessedKeys_ block.
- `BatchPutItem` is limited to 25 items.
- This operation **is not** supported when used with
  conflict detection. Using both at the same time may result in an error.
  For the following example function request handler:

```
import { util } from '@aws-appsync/utils';

export function request(ctx) {
  const { authorId, postId, name, title } = ctx.args;
  return {
    operation: 'BatchPutItem',
    tables: {
      authors: [util.dynamodb.toMapValues({ authorId, name })],
      posts: [util.dynamodb.toMapValues({ authorId, postId, title })],
    },
  };
}
```

The invocation result available in `ctx.result` is as follows:

```
{
   "data": {
     "authors": [
         null
     ],
     "posts": [
        // Was inserted
        {
          "authorId": "a1",
          "postId": "p2",
          "title": "title"
        }
     ]
   },
   "unprocessedItems": {
     "authors": [
        // This item was not processed due to an error
        {
          "authorId": "a1",
          "name": "a1_name"
        }
      ],
     "posts": []
   }
}
```

The `ctx.error` contains details about the error. The keys **data**, **unprocessedItems**, and each
table key that was provided in the request object are guaranteed to be present in the
invocation result. Items that have been inserted are in the **data** block. Items that haven’t been processed are marked as _null_ inside the data block and are placed inside the
**unprocessedItems** block.
