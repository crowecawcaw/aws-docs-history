# Work with query results and recent queries

Amazon Athena automatically stores query results and query execution result metadata for each
query that runs in a _query result location_ that you can specify in
Amazon S3. If necessary, you can access the files in this location to work with them. You can
also download query result files directly from the Athena console.

Athena now offers you two options for managing query results; you can either use a
customer-owned S3 bucket or opt for the managed query results feature. With your own bucket,
you maintain complete control over storage, permissions, lifecycle policies, and retention,
providing maximum flexibility but require more management. Alternatively, when you choose
the managed query results option, the service automatically handles storage and lifecycle
management, eliminating your need to configure a separate results bucket and automatically
cleaning up results after a predetermined retention period. For more information, see [Managed query results](managed-results.md "managed-results.md").

To set up an Amazon S3 query result location for the first time, see [Specify a query result location using the Athena console](query-results-specify-location-console.md "query-results-specify-location-console.md").

Output files are saved automatically for every query that runs. To access and view query
output files using the Athena console, IAM principals (users and roles) need permission to
the Amazon S3 [GetObject](../../../AmazonS3/latest/API/API_GetObject.md "../../../AmazonS3/latest/API/API_GetObject.md") action for the query result location, as well as permission for the
Athena [GetQueryResults](../APIReference/API_GetQueryResults.md "../APIReference/API_GetQueryResults.md") action. The query result location can be encrypted. If the
location is encrypted, users must have the appropriate key permissions to encrypt and
decrypt the query result location.

###### Important

IAM principals with permission to the Amazon S3 `GetObject` action for the query
result location are able to retrieve query results from Amazon S3 even if permission to the
Athena `GetQueryResults` action is denied.

###### Note

- In the case of canceled or failed queries, Athena may have
  already written partial results to Amazon S3. In such cases, Athena
  does not delete partial results from the Amazon S3 prefix where
  results are stored. You must remove the Amazon S3 prefix with partial
  results. Athena uses Amazon S3 multipart uploads to write data Amazon S3.
  We recommend that you set the bucket lifecycle policy to end
  multipart uploads in cases when queries fail. For more
  information, see [Aborting incomplete multipart uploads using a bucket
  lifecycle policy](../../../AmazonS3/latest/userguide/mpuoverview.md#mpu-abort-incomplete-mpu-lifecycle-config "../../../AmazonS3/latest/userguide/mpuoverview.md#mpu-abort-incomplete-mpu-lifecycle-config") in the
  _Amazon Simple Storage Service User Guide_.
- Under certain conditions, Athena may automatically retry query
  executions. In most cases, these queries are able to complete
  successfully and the query ID is marked as
  `Completed`. These queries might have written
  partial results during the initial attempts and may generate
  incomplete multipart uploads.

###### Topics

- [Managed query results](managed-results.md "managed-results.md")
- [Specify a query result location](query-results-specify-location.md "query-results-specify-location.md")
- [Download query results files using the Athena console](saving-query-results.md "saving-query-results.md")
- [View recent queries in the Athena console](queries-viewing-history.md "queries-viewing-history.md")
- [Download multiple recent queries to a CSV file](queries-downloading-multiple-recent-queries-to-csv.md "queries-downloading-multiple-recent-queries-to-csv.md")
- [Configure recent query display options](queries-recent-queries-configuring-options.md "queries-recent-queries-configuring-options.md")
- [Keep your query history longer than 45 days](querying-keeping-query-history.md "querying-keeping-query-history.md")
- [Find query output files in Amazon S3](querying-finding-output-files.md "querying-finding-output-files.md")
