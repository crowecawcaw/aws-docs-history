# Query

The `Query` request object lets you tell the AWS AppSync DynamoDB resolver to make a
`Query` request to DynamoDB, and enables you to specify the following:

- Key expression
- Which index to use
- Any additional filter
- How many items to return
- Whether to use consistent reads
- query direction (forward or backward)
- Pagination token
  The `Query` request object has the following structure:

```
type DynamoDBQueryRequest = {
  operation: 'Query';
  query: {
    expression: string;
    expressionNames?: { [key: string]: string };
    expressionValues?: { [key: string]: any };
  };
  index?: string;
  nextToken?: string;
  limit?: number;
  scanIndexForward?: boolean;
  consistentRead?: boolean;
  select?: 'ALL_ATTRIBUTES' | 'ALL_PROJECTED_ATTRIBUTES' | 'SPECIFIC_ATTRIBUTES';
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

## Query fields

**`operation`**

The DynamoDB operation to perform. To perform the `Query`
DynamoDB operation, this must be set to `Query`. This value is
required.

**`query`**

The `query` section lets you specify a key condition
expression that describes which items to retrieve from DynamoDB. For more
information about how to write key condition expressions, see the [DynamoDB KeyConditions documentation](../../../amazondynamodb/latest/developerguide/LegacyConditionalParameters.md "../../../amazondynamodb/latest/developerguide/LegacyConditionalParameters.md") . This section must be
specified.

**`expression`**

The query expression. This field must be specified.

**`expressionNames`**

The substitutions for expression attribute
_name_ placeholders, in the form of
key-value pairs. The key corresponds to a name placeholder used
in the `expression`, and the value must be a string
corresponding to the attribute name of the item in DynamoDB. This
field is optional, and should only be populated with
substitutions for expression attribute name placeholders used in
the `expression`.

**`expressionValues`**

The substitutions for expression attribute
_value_ placeholders, in the form of
key-value pairs. The key corresponds to a value placeholder used
in the `expression`, and the value must be a typed
value. For more information about how to specify a “typed
value”, see [Type system (request mapping)](js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-typed-values-request "js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-typed-values-request"). This value is
required. This field is optional, and should only be populated
with substitutions for expression attribute value placeholders
used in the `expression`.

**`filter`**

An additional filter that can be used to filter the results from
DynamoDB before they are returned. For more information about filters,
see [Filters](js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-filter "js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-filter"). This field is optional.

**`index`**

The name of the index to query. The DynamoDB query operation allows you
to scan on Local Secondary Indexes and Global Secondary Indexes in
addition to the primary key index for a hash key. If specified, this
tells DynamoDB to query the specified index. If omitted, the primary key
index is queried.

**`nextToken`**

The pagination token to continue a previous query. This would have
been obtained from a previous query. This field is optional.

**`limit`**

The maximum number of items to evaluate (not necessarily the number of
matching items). This field is optional.

**`scanIndexForward`**

A boolean indicating whether to query forwards or backwards. This
field is optional, and defaults to `true`.

**`consistentRead`**

A boolean indicating whether to use consistent reads when querying
DynamoDB. This field is optional, and defaults to `false`.

**`select`**

By default, the AWS AppSync DynamoDB resolver only returns attributes that are
projected into the index. If more attributes are required, you can set
this field. This field is optional. The supported values are:

**`ALL_ATTRIBUTES`**

Returns all of the item attributes from the specified table
or index. If you query a local secondary index, DynamoDB fetches
the entire item from the parent table for each matching item in
the index. If the index is configured to project all item
attributes, all of the data can be obtained from the local
secondary index and no fetching is required.

**`ALL_PROJECTED_ATTRIBUTES`**

Allowed only when querying an index. Retrieves all attributes
that have been projected into the index. If the index is
configured to project all attributes, this return value is
equivalent to specifying `ALL_ATTRIBUTES`.

**`SPECIFIC_ATTRIBUTES`**

Returns only the attributes listed in the
`projection`'s `expression`. This
return value is equivalent to specifying the
`projection`'s `expression` without
specifying any value for `Select`.

**`projection`**

A projection that's used to specify the attributes to return from the
DynamoDB operation. For more information about projections, see [Projections](js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-projections "js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-projections"). This field is optional.

The results from DynamoDB are automatically converted into GraphQL and JSON primitive types
and are available in the context result (`context.result`).

For more information about DynamoDB type conversion, see [Type system (response mapping)](js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-typed-values-responses "js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-typed-values-responses").

For more information about JavaScript resolvers, see [JavaScript resolvers
overview](resolver-reference-overview-js.md "resolver-reference-overview-js.md").

The results have the following structure:

```
{
    items = [ ... ],
    nextToken = "a pagination token",
    scannedCount = 10
}
```

The fields are defined as follows:

**`items`**

A list containing the items returned by the DynamoDB query.

**`nextToken`**

If there might be more results, `nextToken` contains a pagination
token that you can use in another request. Note that AWS AppSync encrypts and
obfuscates the pagination token returned from DynamoDB. This prevents your table data
from being inadvertently leaked to the caller. Also note that these pagination
tokens cannot be used across different functions or resolvers.

**`scannedCount`**

The number of items that matched the query condition expression, before a
filter expression (if present) was applied.

## Example

The following example is a function request handler for a GraphQL query
`getPosts(owner: ID!)`.

In this example, a global secondary index on a table is queried to return all posts
owned by the specified ID.

```
import { util } from '@aws-appsync/utils';

export function request(ctx) {
  const { owner } = ctx.args;
  return {
    operation: 'Query',
    query: {
      expression: 'ownerId = :ownerId',
      expressionValues: util.dynamodb.toMapValues({ ':ownerId': owner }),
    },
    index: 'owner-index',
  };
}
```

For more information about the DynamoDB `Query` API, see the [DynamoDB API
documentation](../../../amazondynamodb/latest/APIReference/API_Query.md "../../../amazondynamodb/latest/APIReference/API_Query.md").
