# AWS AppSync JavaScript resolver function

reference for DynamoDB

The AWS AppSync DynamoDB function allows you to use [GraphQL](https://graphql.org "https://graphql.org") to store and retrieve data in existing Amazon DynamoDB tables in your account by
mapping an incoming GraphQL request into a DynamoDB call, and then mapping the DynamoDB response
back to GraphQL. This section describes the request and response handlers for supported DynamoDB
operations:

- [GetItem](js-aws-appsync-resolver-reference-dynamodb-getitem.md "js-aws-appsync-resolver-reference-dynamodb-getitem.md") - The GetItem request lets you tell the DynamoDB function to make a
  GetItem request to DynamoDB, and enables you to specify the key of the item in DynamoDB
  and whether to use a consistent read or not.
- [PutItem](js-aws-appsync-resolver-reference-dynamodb-putitem.md "js-aws-appsync-resolver-reference-dynamodb-putitem.md") - The PutItem request mapping document lets you tell the DynamoDB
  function to make a PutItem request to DynamoDB, and enables you to specify the key of
  the item in DynamoDB, the full contents of the item (composed of key and
  attributeValues), and conditions for the operation to succeed.
- [UpdateItem](js-aws-appsync-resolver-reference-dynamodb-updateitem.md "js-aws-appsync-resolver-reference-dynamodb-updateitem.md") - The UpdateItem request enables you to tell the DynamoDB
  function to make a UpdateItem request to DynamoDB and allows you to specify the key of
  the item in DynamoDB, an update expression describing how to update the item in
  DynamoDB, and conditions for the operation to succeed.
- [DeleteItem](js-aws-appsync-resolver-reference-dynamodb-deleteitem.md "js-aws-appsync-resolver-reference-dynamodb-deleteitem.md") - The DeleteItem request lets you tell the DynamoDB function to
  make a DeleteItem request to DynamoDB, and enables you to specify the key of the item in
  DynamoDB and conditions for the operation to succeed.
- [Query](js-aws-appsync-resolver-reference-dynamodb-query.md "js-aws-appsync-resolver-reference-dynamodb-query.md") - The Query request object lets you tell the DynamoDB resolver to make
  a Query request to DynamoDB, and enables you to specify the key expression, which index
  to use, additional filters, how many items to return, whether to use consistent reads,
  query direction (forward or backward), and pagination tokens.
- [Scan](js-aws-appsync-resolver-reference-dynamodb-scan.md "js-aws-appsync-resolver-reference-dynamodb-scan.md") - The Scan request lets you tell the DynamoDB function to make a Scan
  request to DynamoDB, and enables you to specify a filter to exclude results, which index
  to use, how many items to return, whether to use consistent reads, pagination tokens,
  and parallel scans.
- [Sync](js-aws-appsync-resolver-reference-dynamodb-sync.md "js-aws-appsync-resolver-reference-dynamodb-sync.md") - The Sync request object lets you retrieve all the results from a
  DynamoDB table and then receive only the data altered since your last query (the delta
  updates). Sync requests can only be made to versioned DynamoDB data sources. You can
  specify a filter to exclude results, how many items to return, pagination Tokens, and
  when your last Sync operation was started.
- [BatchGetItem](js-aws-appsync-resolver-reference-dynamodb-batch-get-item.md "js-aws-appsync-resolver-reference-dynamodb-batch-get-item.md") - The BatchGetItem request object lets you tell the DynamoDB
  function to make a BatchGetItem request to DynamoDB to retrieve multiple items,
  potentially across multiple tables. For this request object, you must specify the table
  names to retrieve the items from and the keys of the items to retrieve from each
  table.
- [BatchDeleteItem](js-aws-appsync-resolver-reference-dynamodb-batch-delete-item.md "js-aws-appsync-resolver-reference-dynamodb-batch-delete-item.md") - The BatchDeleteItem request object lets you tell the
  DynamoDB function to make a BatchWriteItem request to DynamoDB to delete multiple items,
  potentially across multiple tables. For this request object, you must specify the table
  names to delete the items from and the keys of the items to delete from each
  table.
- [BatchPutItem](js-aws-appsync-resolver-reference-dynamodb-batch-put-item.md "js-aws-appsync-resolver-reference-dynamodb-batch-put-item.md") - The BatchPutItem request object lets you tell the DynamoDB
  function to make a BatchWriteItem request to DynamoDB to put multiple items, potentially
  across multiple tables. For this request object, you must specify the table names to put
  the items in and the full items to put in each table.
- [TransactGetItems](js-aws-appsync-resolver-reference-dynamodb-transact-get-items.md "js-aws-appsync-resolver-reference-dynamodb-transact-get-items.md") - The TransactGetItems request object lets you to tell
  the DynamoDB function to make a TransactGetItems request to DynamoDB to retrieve
  multiple items, potentially across multiple tables. For this request object, you must
  specify the table name of each request item to retrieve the item from and the key of
  each request item to retrieve from each table.
- [TransactWriteItems](js-aws-appsync-resolver-reference-dynamodb-transact-write-items.md "js-aws-appsync-resolver-reference-dynamodb-transact-write-items.md") - The TransactWriteItems request object lets you tell
  the DynamoDB function to make a TransactWriteItems request to DynamoDB to write multiple
  items, potentially to multiple tables. For this request object, you must specify the
  destination table name of each request item, the operation of each request item to
  perform, and the key of each request item to write.
- [Type system (request mapping)](js-aws-appsync-resolver-reference-dynamodb-typed-values-request.md "js-aws-appsync-resolver-reference-dynamodb-typed-values-request.md") - Learn more about how DynamoDB typing is
  integrated into AWS AppSync requests.
- [Type system (response mapping)](js-aws-appsync-resolver-reference-dynamodb-typed-values-responses.md "js-aws-appsync-resolver-reference-dynamodb-typed-values-responses.md") - Learn more about how DynamoDB types are
  converted automatically to GraphQL or JSON in a response payload.
- [Filters](js-aws-appsync-resolver-reference-dynamodb-filter.md "js-aws-appsync-resolver-reference-dynamodb-filter.md") - Learn more about filters for query and scan operations.
- [Condition expressions](js-aws-appsync-resolver-reference-dynamodb-condition-expressions.md "js-aws-appsync-resolver-reference-dynamodb-condition-expressions.md") - Learn more about condition expressions for
  PutItem, UpdateItem, and DeleteItem operations.
- [Transaction condition expressions](js-aws-appsync-resolver-reference-dynamodb-transaction-condition-expressions.md "js-aws-appsync-resolver-reference-dynamodb-transaction-condition-expressions.md") - Learn more about condition expressions
  for TransactWriteItems operations.
- [Projections](js-aws-appsync-resolver-reference-dynamodb-projections.md "js-aws-appsync-resolver-reference-dynamodb-projections.md") - Learn more about how to specify attributes in read
  operations.
