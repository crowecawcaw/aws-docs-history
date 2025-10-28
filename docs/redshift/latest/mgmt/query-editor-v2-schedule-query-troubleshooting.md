Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Troubleshooting set up

of scheduling a query

Consider the following if you have issues scheduling a query.

**Queries not running**

Check if the IAM role used in the schedule has permission to get the
temporary cluster credentials. The permission for provisioned clusters is
`redshift:GetClusterCredentialsWithIAM`. The permission for
Redshift Serverless workgroups is `redshift-serverless:GetCredentials`.

**Scheduled history not displaying**

The IAM user or IAM role used to log in to the AWS console was not
added into the trust policy of the IAM role used to schedule the
query.

When using AWS Secrets Manager for the scheduled query to connect, confirm the
secret is tagged with the key `RedshiftDataFullAccess`.

If the scheduled query is using an AWS Secrets Manager connection, the IAM role
used to schedule the query must have the equivalent of managed policy
`SecretsManagerReadWrite` attached to the role.

**Query history status is `Failed`**

View the SYS_QUERY_HISTORY system view for details about why the query
failed. A common issue is that the database user or role that was used to
run the query might not have the required privilege to run the SQL. For more
information, see [Authenticating a
scheduled query](query-editor-v2-schedule-query-authentication.md "query-editor-v2-schedule-query-authentication.md").

The following SQL queries the SYS_QUERY_HISTORY view to return failed
queries.

```
SELECT user_id, query_id, transaction_id, session_id, database_name, query_type, status, error_message, query_text
FROM sys_query_history
WHERE status = 'failed';
```

To find out details for a specific failing scheduled query, see [Viewing the
results of a scheduled query with AWS CloudShell](query-editor-v2-schedule-query-troubleshooting-cloudshell.md "query-editor-v2-schedule-query-troubleshooting-cloudshell.md").
