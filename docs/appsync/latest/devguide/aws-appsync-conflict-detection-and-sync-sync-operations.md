# Using DynamoDB

sync operations on versioned data sources in AWS AppSync

Versioned data sources support `Sync` operations that allow you to retrieve
all the results from a DynamoDB table and then receive only the data altered since your last
query (the delta updates). When AWS AppSync receives a request for a `Sync`
operation, it uses the fields specified in the request to determine if the _Base_ table or the _Delta_ table should be accessed.

- If the `lastSync` field is not specified, a `Scan` on the
  _Base_ table is performed.
- If the `lastSync` field is specified, but the value is before the
  `current moment - DeltaSyncTTL`, a `Scan` on the _Base_ table is performed.
- If the `lastSync` field is specified, and the value is on or after the
  `current moment - DeltaSyncTTL`, a `Query` on the _Delta_ table is performed.
  AWS AppSync returns the `startedAt` field to the response mapping template for
  all `Sync` operations. The `startedAt` field is the moment, in epoch
  milliseconds, when the `Sync` operation started that you can store locally and
  use in another request. If a pagination token was included in the request, this value will
  be the same as the one returned by the request for the first page of results.

For information about the format for `Sync` mapping templates, see [the mapping
template reference](aws-appsync-resolver-mapping-template-reference-dynamodb-sync.md "aws-appsync-resolver-mapping-template-reference-dynamodb-sync.md").
