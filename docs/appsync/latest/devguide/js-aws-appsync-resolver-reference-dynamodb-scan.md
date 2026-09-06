

# Scan
<a name="js-aws-appsync-resolver-reference-dynamodb-scan"></a>

The `Scan` request lets you tell the AWS AppSync DynamoDB function to make a `Scan` request to DynamoDB, and enables you to specify the following:
+ A filter to exclude results
+ Which index to use
+ How many items to return
+ Whether to use consistent reads
+ Pagination token
+ Parallel scans

The `Scan` request object has the following structure:

```
type DynamoDBScanRequest = {
  operation: 'Scan';
  index?: string;
  limit?: number;
  consistentRead?: boolean;
  nextToken?: string;
  totalSegments?: number;
  segment?: number;
  filter?: {
    expression: string;
    expressionNames?: { [key: string]: string };
    expressionValues?: { [key: string]: any };
  };
  projection?: {
    expression: string;
    expressionNames?: { [key: string]: string };
  };
};
```

The fields are defined as follows:

## Scan fields
<a name="js-scan-list"></a>

### Scan fields list
<a name="js-scan-list-col"></a>

** `operation` **  
The DynamoDB operation to perform. To perform the `Scan` DynamoDB operation, this must be set to `Scan`. This value is required.

** `filter` **  
A filter that can be used to filter the results from DynamoDB before they are returned. For more information about filters, see [Filters](https://docs.aws.amazon.com/appsync/latest/devguide/js-resolver-reference-dynamodb.html#js-aws-appsync-resolver-reference-dynamodb-filter). This field is optional.

** `index` **  
The name of the index to query. The DynamoDB query operation allows you to scan on Local Secondary Indexes and Global Secondary Indexes in addition to the primary key index for a hash key. If specified, this tells DynamoDB to query the specified index. If omitted, the primary key index is queried.

** `limit` **  
The maximum number of items to evaluate at a single time. This field is optional.

** `consistentRead` **  
A Boolean that indicates whether to use consistent reads when querying DynamoDB. This field is optional, and defaults to `false`.

** `nextToken` **  
The pagination token to continue a previous query. This would have been obtained from a previous query. This field is optional.

** `select` **  
By default, the AWS AppSync DynamoDB function only returns whatever attributes are projected into the index. If more attributes are required, then this field can be set. This field is optional. The supported values are:    
** `ALL_ATTRIBUTES` **  
Returns all of the item attributes from the specified table or index. If you query a local secondary index, DynamoDB fetches the entire item from the parent table for each matching item in the index. If the index is configured to project all item attributes, all of the data can be obtained from the local secondary index and no fetching is required.  
** `ALL_PROJECTED_ATTRIBUTES` **  
Allowed only when querying an index. Retrieves all attributes that have been projected into the index. If the index is configured to project all attributes, this return value is equivalent to specifying `ALL_ATTRIBUTES`.  
**`SPECIFIC_ATTRIBUTES`**  
Returns only the attributes listed in the `projection`'s `expression`. This return value is equivalent to specifying the `projection`'s `expression` without specifying any value for `Select`.

** `totalSegments` **  
The number of segments to partition the table by when performing a parallel scan. This field is optional, but must be specified if `segment` is specified.

** `segment` **  
The table segment in this operation when performing a parallel scan. This field is optional, but must be specified if `totalSegments` is specified.

**`projection`**  
A projection that's used to specify the attributes to return from the DynamoDB operation. For more information about projections, see [Projections](https://docs.aws.amazon.com/appsync/latest/devguide/js-resolver-reference-dynamodb.html#js-aws-appsync-resolver-reference-dynamodb-projections). This field is optional.

The results returned by the DynamoDB scan are automatically converted into GraphQL and JSON primitive types and is available in the context result (`context.result`).

For more information about DynamoDB type conversion, see [Type system (response mapping)](https://docs.aws.amazon.com/appsync/latest/devguide/js-resolver-reference-dynamodb.html#js-aws-appsync-resolver-reference-dynamodb-typed-values-responses).

For more information about JavaScript resolvers, see [JavaScript resolvers overview](https://docs.aws.amazon.com/appsync/latest/devguide/resolver-reference-overview-js.html).

The results have the following structure:

```
{
    items = [ ... ],
    nextToken = "a pagination token",
    scannedCount = 10
}
```

The fields are defined as follows:

** `items` **  
A list containing the items returned by the DynamoDB scan.

** `nextToken` **  
If there might be more results, `nextToken` contains a pagination token that you can use in another request. AWS AppSync encrypts and obfuscates the pagination token returned from DynamoDB. This prevents your table data from being inadvertently leaked to the caller. Also, these pagination tokens can’t be used across different functions or resolvers.

** `scannedCount` **  
The number of items that were retrieved by DynamoDB before a filter expression (if present) was applied.

## Example 1
<a name="js-id11"></a>

The following example is a function request handler for the GraphQL query: `allPosts`.

In this example, all entries in the table are returned.

```
export function request(ctx) {
  return { operation: 'Scan' };
}
```

## Example 2
<a name="js-id12"></a>

The following example is a function request handler for the GraphQL query: `postsMatching(title: String!)`.

In this example, all entries in the table are returned where the title starts with the `title` argument.

```
export function request(ctx) {
  const { title } = ctx.args;
  const filter = { filter: { beginsWith: title } };
  return {
    operation: 'Scan',
    filter: JSON.parse(util.transform.toDynamoDBFilterExpression(filter)),
  };
}
```

For more information about the DynamoDB `Scan` API, see the [DynamoDB API documentation](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Scan.html).