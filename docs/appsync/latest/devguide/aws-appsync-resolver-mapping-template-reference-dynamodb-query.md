# Query

The `Query` request mapping document lets you tell the AWS AppSync DynamoDB resolver to make a
`Query` request to DynamoDB, and enables you to specify the following:

- Key expression
- Which index to use
- Any additional filter
- How many items to return
- Whether to use consistent reads
- query direction (forward or backward)
- Pagination token
  The `Query` mapping document has the following structure:

```
{
    "version" : "2017-02-28",
    "operation" : "Query",
    "query" : {
        "expression" : "some expression",
        "expressionNames" : {
            "#foo" : "foo"
        },
        "expressionValues" : {
            ":bar" : ... typed value
        }
    },
    "index" : "fooIndex",
    "nextToken" : "a pagination token",
    "limit" : 10,
    "scanIndexForward" : true,
    "consistentRead" : false,
    "select" : "ALL_ATTRIBUTES" | "ALL_PROJECTED_ATTRIBUTES" | "SPECIFIC_ATTRIBUTES",
    "filter" : {
        ...
    },
    "projection" : {
        ...
    }
}
```

The fields are defined as follows:

## Query fields

**`version`**

The template definition version. `2017-02-28` and `2018-05-29` are
currently supported. This value is required.

**`operation`**

The DynamoDB operation to perform. To perform the `Query` DynamoDB operation, this
must be set to `Query`. This value is required.

**`query`**

The `query` section lets you specify a key condition expression that describes
which items to retrieve from DynamoDB. For more information about how to write key condition
expressions, see the [DynamoDB KeyConditions documentation](../../../amazondynamodb/latest/developerguide/LegacyConditionalParameters.md "../../../amazondynamodb/latest/developerguide/LegacyConditionalParameters.md") . This section must be specified.

**`expression`**

The query expression. This field must be specified.

**`expressionNames`**

The substitutions for expression attribute _name_
placeholders, in the form of key-value pairs. The key corresponds to a name
placeholder used in the `expression`, and the value must be a string
corresponding to the attribute name of the item in DynamoDB. This field is optional,
and should only be populated with substitutions for expression attribute name
placeholders used in the `expression`.

**`expressionValues`**

The substitutions for expression attribute
_value_ placeholders, in the form of
key-value pairs. The key corresponds to a value placeholder used
in the `expression`, and the value must be a typed
value. For more information about how to specify a “typed
value”, see [Type system (request mapping)](aws-appsync-resolver-mapping-template-reference-dynamodb-typed-values-request.md "aws-appsync-resolver-mapping-template-reference-dynamodb-typed-values-request.md"). This value is
required. This field is optional, and should only be populated
with substitutions for expression attribute value placeholders
used in the `expression`.

**`filter`**

An additional filter that can be used to filter the results from DynamoDB before they are
returned. For more information about filters, see [Filters](aws-appsync-resolver-mapping-template-reference-dynamodb-filter.md "aws-appsync-resolver-mapping-template-reference-dynamodb-filter.md").
This field is optional.

**`index`**

The name of the index to query. The DynamoDB query operation allows you to scan on Local
Secondary Indexes and Global Secondary Indexes in addition to the primary key index for a
hash key. If specified, this tells DynamoDB to query the specified index. If omitted, the
primary key index is queried.

**`nextToken`**

The pagination token to continue a previous query. This would have been obtained from a
previous query. This field is optional.

**`limit`**

The maximum number of items to evaluate (not necessarily the number of matching items).
This field is optional.

**`scanIndexForward`**

A boolean indicating whether to query forwards or backwards. This field is optional, and
defaults to `true`.

**`consistentRead`**

A boolean indicating whether to use consistent reads when querying DynamoDB. This field is
optional, and defaults to `false`.

**`select`**

By default, the AWS AppSync DynamoDB resolver only returns attributes that are projected into the
index. If more attributes are required, you can set this field. This field is optional. The
supported values are:

**`ALL_ATTRIBUTES`**

Returns all of the item attributes from the specified table or index. If you
query a local secondary index, DynamoDB fetches the entire item from the parent table
for each matching item in the index. If the index is configured to project all item
attributes, all of the data can be obtained from the local secondary index and no
fetching is required.

**`ALL_PROJECTED_ATTRIBUTES`**

Allowed only when querying an index. Retrieves all attributes that have been
projected into the index. If the index is configured to project all attributes, this
return value is equivalent to specifying `ALL_ATTRIBUTES`.

**`SPECIFIC_ATTRIBUTES`**

Returns only the attributes listed in the `projection`'s
`expression`. This return value is equivalent to specifying the
`projection`'s `expression` without specifying any value
for `Select`.

**`projection`**

A projection that's used to specify the attributes to return from the
DynamoDB operation. For more information about projections, see [Projections](resolver-mapping-template-reference-dynamodb.md#aws-appsync-resolver-mapping-template-reference-dynamodb-projections "resolver-mapping-template-reference-dynamodb.md#aws-appsync-resolver-mapping-template-reference-dynamodb-projections"). This field is optional.

The results from DynamoDB are automatically converted into GraphQL and JSON primitive types and are available
in the mapping context (`$context.result`).

For more information about DynamoDB type conversion, see [Type system (response mapping)](aws-appsync-resolver-mapping-template-reference-dynamodb-typed-values-responses.md "aws-appsync-resolver-mapping-template-reference-dynamodb-typed-values-responses.md").

For more information about response mapping templates, see [Resolver mapping
template overview](resolver-mapping-template-reference-overview.md#aws-appsync-resolver-mapping-template-reference-overview "resolver-mapping-template-reference-overview.md#aws-appsync-resolver-mapping-template-reference-overview").

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

If there might be more results, `nextToken` contains a pagination token that you can use
in another request. Note that AWS AppSync encrypts and obfuscates the pagination token returned from
DynamoDB. This prevents your table data from being inadvertently leaked to the caller. Also note that
these pagination tokens cannot be used across different resolvers.

**`scannedCount`**

The number of items that matched the query condition expression, before a filter expression (if
present) was applied.

## Example

The following example is a mapping template for a GraphQL query `getPosts(owner:
 ID!)`.

In this example, a global secondary index on a table is queried to return all posts owned by the
specified ID.

```
{
    "version" : "2017-02-28",
    "operation" : "Query",
    "query" : {
        "expression" : "ownerId = :ownerId",
        "expressionValues" : {
            ":ownerId" : $util.dynamodb.toDynamoDBJson($context.arguments.owner)
        }
    },
    "index" : "owner-index"
}
```

For more information about the DynamoDB `Query` API, see the [DynamoDB API
documentation](../../../amazondynamodb/latest/APIReference/API_Query.md "../../../amazondynamodb/latest/APIReference/API_Query.md").
