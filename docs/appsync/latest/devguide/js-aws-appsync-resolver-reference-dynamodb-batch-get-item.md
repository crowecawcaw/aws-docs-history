# BatchGetItem

The `BatchGetItem` request object lets you tell the AWS AppSync DynamoDB function to
make a `BatchGetItem` request to DynamoDB to retrieve multiple items, potentially
across multiple tables. For this request object, you must specify the following:

- The table names where to retrieve the items from
- The keys of the items to retrieve from each table
  The DynamoDB `BatchGetItem` limits apply and **no condition
  expression** can be provided.

The `BatchGetItem` request object has the following structure:

```
type DynamoDBBatchGetItemRequest = {
  operation: 'BatchGetItem';
  tables: {
    [tableName: string]: {
      keys: { [key: string]: any }[];
      consistentRead?: boolean;
      projection?: {
        expression: string;
        expressionNames?: { [key: string]: string };
      };
    };
  };
};
```

The fields are defined as follows:

## BatchGetItem fields

**`operation`**

The DynamoDB operation to perform. To perform the
`BatchGetItem` DynamoDB operation, this must be set to
`BatchGetItem`. This value is required.

**`tables`**

The DynamoDB tables to retrieve the items from. The value is a map where
table names are specified as the keys of the map. At least one table must
be provided. This `tables` value is required.

**`keys`**

List of DynamoDB keys representing the primary key of the items
to retrieve. DynamoDB items may have a single hash key, or a hash
key and sort key, depending on the table structure. For more
information about how to specify a “typed value”, see [Type system (request mapping)](js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-typed-values-request "js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-typed-values-request").

**`consistentRead`**

Whether to use a consistent read when executing a _GetItem_ operation. This
value is optional and defaults to _false_.

**`projection`**

A projection that's used to specify the attributes to return
from the DynamoDB operation. For more information about
projections, see [Projections](js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-projections "js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-projections"). This field is optional.

Things to remember:

- If an item has not been retrieved from the table, a _null_ element appears in the data block for that
  table.
- Invocation results are sorted per table, based on the order in which they were
  provided inside the request object.
- Each `Get` command inside a `BatchGetItem` is atomic,
  however, a batch can be partially processed. If a batch is partially processed due to
  an error, the unprocessed keys are returned as part of the invocation result inside
  the _unprocessedKeys_ block.
- `BatchGetItem` is limited to 100 keys.
  For the following example function request handler:

```
import { util } from '@aws-appsync/utils';

export function request(ctx) {
  const { authorId, postId } = ctx.args;
  return {
    operation: 'BatchGetItem',
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
        // Was retrieved
        {
          "authorId": "a1",
          "postId": "p2",
          "postTitle": "title",
          "postDescription": "description",
        }
     ]
   },
   "unprocessedKeys": {
     "authors": [
        // This item was not processed due to an error
        {
          "authorId": "a1"
        }
      ],
     "posts": []
   }
}
```

The `ctx.error` contains details about the error. The keys **data**, **unprocessedKeys**, and each
table key that was provided in the result in the function request object are guaranteed to
be present in the invocation result. Items that have been deleted appear in the **data** block. Items that haven’t been processed are marked as
_null_ inside the data block and are placed
inside the **unprocessedKeys** block.
