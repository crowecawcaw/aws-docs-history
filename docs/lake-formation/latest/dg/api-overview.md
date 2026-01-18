# Lake Formation workflow for application integration API

operations

The following is the work flow for application integration API operations:

1. A user submits a query or request for data using an integrated third-party query
   engine. The query engine assumes an IAM role that represents the user or a group of
   users, and retrieves trusted credentials to be used when calling the application
   integration API operations.
2. The query engine calls `GetUnfilteredTableMetadata`, and if it is a
   partitioned table, the query engine calls `GetUnfilteredPartitionsMetadata`
   to retrieve metadata and policy information from the Data Catalog.
3. Lake Formation performs authorization for the request. If the user doesn't have appropriate
   permissions on the table, then _AccessDeniedException_ is thrown.
4. As part of the request, the query engine sends the filtering it supports. There are
   two flags that can be sent within an array: _COLUMN_PERMISSIONS_ and _CELL_FILTER_PERMISSION_. If the query engine doesn't support any of these
   features, and a policy exists on the table for the feature, then a _PermissionTypeMismatchException_ is thrown and the query
   fails. This is to avoid data leakage.
5. The returned response contains the following:
   - The entire schema for the table so that query engines can use it to parse the
     data from storage.
   - A list of authorized columns that the user has access. If the authorized column list is empty, it
     indicates that the user has `DESCRIBE` permissions, but does not have `SELECT`
     permissions, and the query fails.
   - A flag, `IsRegisteredWithLakeFormation`, which indicates if Lake Formation can
     vend credentials to this resources data. If this returns false, then the customers'
     credentials should be used to access Amazon S3.
   - A list of `CellFilters` if any that should be applied to rows of
     data. This list contains columns and an expression to evaluate each row. This should
     only be populated if _CELL_FILTER_PERMISSION_ is
     sent as part of the request and there is a data filter against the table for the
     calling user.

6. After the metadata is retrieved, the query engine calls
   `GetTemporaryGlueTableCredentials` or
   `GetTemporaryGluePartitionCredentials` to get AWS credentials to retrieve
   data from the Amazon S3 location.
7. The query engine reads relevant objects from Amazon S3, filters the data based on the
   policies it received in step 2, and returns the results to the user.
   The application integration API operations for Lake Formation contain additional
   content for configuring integration with third-party query engines. You can see the
   operation details in the [Credential vending API operations section.](aws-lake-formation-api-credential-vending.md "aws-lake-formation-api-credential-vending.md")

The `QuerySessionContext` is a structure that query engines can additionally send
to Lake Formation for these application integration API operations.
It allows Lake Formation to store and utilize additional context for a given query.
The following provides an example of how [QuerySessionContext](../../../glue/latest/webapi/API_QuerySessionContext.md "../../../glue/latest/webapi/API_QuerySessionContext.md") should be used:

1. The query engine makes a `GetInternalUnfilteredMetadata` call, passing in
   a QSC structure containing a unique query id in the request:

```
{
    "QuerySessionContext": {
        "QueryId": "your-unique-identifier-here"
    }
}
```

2. The `GetInternalUnfilteredMetadata` call will have returned a
   `QueryAuthorizationId` string in the response. On the next (and any subsequent) query call
   that accepts a QSC structure in the input, the query engine passes the same QSC structure that now also
   contains the `QueryAuthorizationId` returned by Lake Formation.
   Suppose this next call is `GetTemporaryGlueTableCredentials`; the request will contain:

```
{
    "QuerySessionContext": {
        "QueryAuthorizationId": "lf-returned-query-authz-id-here",
        "QueryId": "your-unique-identifier-here"
    },
}
```
