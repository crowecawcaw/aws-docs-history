# Sync

The `Sync` request mapping document lets you retrieve all the results from a DynamoDB table and then
receive only the data altered since your last query (the delta updates). `Sync` requests can only be
made to versioned DynamoDB data sources. You can specify the following:

- A filter to exclude results
- How many items to return
- Pagination Token
- When your last `Sync` operation was started
  The `Sync` mapping document has the following structure:

```
{
    "version" : "2018-05-29",
    "operation" : "Sync",
    "basePartitionKey": "Base Tables PartitionKey",
    "deltaIndexName": "delta-index-name",
    "limit" : 10,
    "nextToken" : "aPaginationToken",
    "lastSync" :  1550000000000,
    "filter" : {
        ...
    }
}
```

The fields are defined as follows:

## Sync fields

**`version`**

The template definition version. Only `2018-05-29` is currently supported. This
value is required.

**`operation`**

The DynamoDB operation to perform. To perform the `Sync` operation, this must be
set to `Sync`. This value is required.

**`filter`**

A filter that can be used to filter the results from DynamoDB before they are returned. For
more information about filters, see [Filters](aws-appsync-resolver-mapping-template-reference-dynamodb-filter.md "aws-appsync-resolver-mapping-template-reference-dynamodb-filter.md").
This field is optional.

**`limit`**

The maximum number of items to evaluate at a single time. This field is optional. If
omitted, the default limit will be set to `100` items. The maximum value for this
field is `1000` items.

**`nextToken`**

The pagination token to continue a previous query. This would have been obtained from a
previous query. This field is optional.

**`lastSync`**

The moment, in epoch milliseconds, when the last successful `Sync` operation
started. If specified, only items that have changed after `lastSync` are returned.
This field is optional, and should only be populated after retrieving all pages from an
initial `Sync` operation. If omitted, results from the _Base_ table will be returned, otherwise, results from the
_Delta_ table will be returned.

**`basePartitionKey`**

The partition key of the _Base_ table used when performing a
`Sync` operation. This field allows a `Sync` operation to be
performed when the table utilizes a custom partition key. This is an optional field.

**`deltaIndexName`**

The index used for the `Sync` operation. This index is required to enable a
`Sync` operation on the whole delta store table when the table uses a custom
partition key. The `Sync` operation will be performed on the GSI (created on
`gsi_ds_pk` and `gsi_ds_sk`). This field is optional.

The results returned by the DynamoDB sync are automatically converted into GraphQL and JSON primitive types and
are available in the mapping context (`$context.result`).

For more information about DynamoDB type conversion, see [Type system (response mapping)](aws-appsync-resolver-mapping-template-reference-dynamodb-typed-values-responses.md "aws-appsync-resolver-mapping-template-reference-dynamodb-typed-values-responses.md").

For more information about response mapping templates, see [Resolver mapping
template overview](resolver-mapping-template-reference-overview.md#aws-appsync-resolver-mapping-template-reference-overview "resolver-mapping-template-reference-overview.md#aws-appsync-resolver-mapping-template-reference-overview").

The results have the following structure:

```
{
    items = [ ... ],
    nextToken = "a pagination token",
    scannedCount = 10,
    startedAt = 1550000000000
}
```

The fields are defined as follows:

**`items`**

A list containing the items returned by the sync.

**`nextToken`**

If there might be more results, `nextToken` contains a pagination token that you can use
in another request. AWS AppSync encrypts and obfuscates the pagination token returned from DynamoDB. This
prevents your table data from being inadvertently leaked to the caller. Also, these pagination tokens
can’t be used across different resolvers.

**`scannedCount`**

The number of items that were retrieved by DynamoDB before a filter expression (if present) was
applied.

**`startedAt`**

The moment, in epoch milliseconds, when the sync operation started that you can store locally and
use in another request as your `lastSync` argument. If a pagination token was included in
the request, this value will be the same as the one returned by the request for the first page of
results.

## Example

The following example is a mapping template for the GraphQL query:
`syncPosts(nextToken: String, lastSync: AWSTimestamp)`.

In this example, if `lastSync` is omitted, all entries in the base table are returned. If
`lastSync` is supplied, only the entries in the delta sync table that have changed since
`lastSync` are returned.

```
{
    "version" : "2018-05-29",
    "operation" : "Sync",
    "limit": 100,
    "nextToken": $util.toJson($util.defaultIfNull($ctx.args.nextToken, null)),
    "lastSync": $util.toJson($util.defaultIfNull($ctx.args.lastSync, null))
}
```
