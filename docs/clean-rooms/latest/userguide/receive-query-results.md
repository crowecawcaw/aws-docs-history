# Receiving and using analysis results

[Members
who can receive results](glossary.md#glossary-member-who-can-receive-results "glossary.md#glossary-member-who-can-receive-results")
can
review the query results in either the AWS Clean Rooms console or in the Amazon S3
buckets
that they specified when they joined the collaboration.

###### Note

For encrypted data tables only, the member who can receive results decrypts the query
results by running the C3R encryption client in the [decrypt](glossary.md#glossary-decryption "glossary.md#glossary-decryption") mode.

If you are using the Spark analytics engine, the **Results destination in
Amazon S3** can't be within the same S3 bucket as any data source.

The following topics explain how to receive analysis results using the AWS Clean Rooms console.

###### Topics

- [Receiving query results](receive-results.md "receive-results.md")
- [Receiving job results](receive-job-results.md "receive-job-results.md")
- [Editing default values for query results
  settings](edit-query-results-settings.md "edit-query-results-settings.md")
- [Editing default values for job results
  settings](edit-job-results-settings.md "edit-job-results-settings.md")
- [Using query output in other AWS services](using-query-output.md "using-query-output.md")
  For information about how to query data or view queries by calling the AWS Clean Rooms API
  directly or by using the AWS SDKs, see the [AWS Clean Rooms API Reference](../apireference/Welcome.md "../apireference/Welcome.md").

For information about query logging, see [Analysis logging in AWS Clean Rooms](query-logs.md "query-logs.md").

###### Note

If you run a query on encrypted data tables, the results from the encrypted columns are
encrypted.
