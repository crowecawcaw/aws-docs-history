# Troubleshooting Amazon RDS Data API

Use the following sections, titled with common error messages, to help troubleshoot
problems that you have with the Amazon RDS Data API (Data API).

###### Topics

- [Transaction
  <transaction_ID> isn't found](#data-api.troubleshooting.tran-id-not-found "#data-api.troubleshooting.tran-id-not-found")
- [Packet for query is too
  large](#data-api.troubleshooting.packet-too-large "#data-api.troubleshooting.packet-too-large")
- [Database response exceeded size limit](#data-api.troubleshooting.response-size-too-large "#data-api.troubleshooting.response-size-too-large")
- [HttpEndpoint
  isn't enabled for cluster <cluster_ID>](#data-api.troubleshooting.http-endpoint-not-enabled "#data-api.troubleshooting.http-endpoint-not-enabled")
- [DatabaseErrorException: Transaction is still running a query](#data-api.troubleshooting.txn-concurrent-requests-rejected "#data-api.troubleshooting.txn-concurrent-requests-rejected")
- [Unsupported result exception](#data-api.troubleshooting.unsupported-result "#data-api.troubleshooting.unsupported-result")
- [Multi-statements aren't supported](#data-api.troubleshooting.multi-statements "#data-api.troubleshooting.multi-statements")
- [Schema parameter isn't supported](#data-api.troubleshooting.schema-parameter "#data-api.troubleshooting.schema-parameter")
- [IPv6 connectivity issues](#data-api.troubleshooting.ipv6-connectivity "#data-api.troubleshooting.ipv6-connectivity")

## Transaction

<transaction_ID> isn't found

In this case, the transaction ID specified in a Data API call wasn't found. The cause for this issue is appended
to the error message, and is one of the following:

- **`Transaction may be expired.`**

Make sure that each transactional call runs within three minutes of the previous one.

It's also possible that the specified transaction ID wasn't created by a [BeginTransaction](../../../rdsdataservice/latest/APIReference/API_BeginTransaction.md "../../../rdsdataservice/latest/APIReference/API_BeginTransaction.md") call. Make sure that your call has a
valid transaction ID.

- **`One previous call resulted in a termination of your transaction.`**

The transaction was already ended by your `CommitTransaction` or `RollbackTransaction`
call.

- **`Transaction has been aborted due to an error from a previous call.`**

Check whether your previous calls have thrown any exceptions.

For information about running transactions, see [Calling the Amazon RDS Data API](data-api.md "data-api.md").

## Packet for query is too

large

In this case, the result set returned for a row was too large. The Data API
size limit is 64 KB per row in the result set returned by the database.

To solve this issue, make sure that each row in a result set is 64 KB or less.

## Database response exceeded size limit

In this case, the size of the result set returned by the database was too large. The Data API limit is 1 MiB in the result set returned by the database.

To solve this issue, make sure that calls to Data API return 1 MiB of data
or less. If you need to return more than 1 MiB, you can use multiple
[`ExecuteStatement`](../../../rdsdataservice/latest/APIReference/API_ExecuteStatement.md "../../../rdsdataservice/latest/APIReference/API_ExecuteStatement.md") calls
with the `LIMIT` clause in your query.

For more information about the `LIMIT` clause, see
[SELECT syntax](https://dev.mysql.com/doc/refman/8.0/en/select.html "https://dev.mysql.com/doc/refman/8.0/en/select.html")
in the MySQL documentation.

## HttpEndpoint

isn't enabled for cluster <cluster_ID>

Check the following potential causes for this issue:

- The Aurora DB cluster doesn't support Data API.
  For information about the types of DB clusters RDS Data API supports,
  see [Region and version availability for the Amazon RDS Data API](data-api.md "data-api.md").
- Data API isn't enabled for the Aurora DB cluster. To use Data API
  with an Aurora DB cluster, Data API must be enabled for the DB cluster. For
  information about enabling Data API, see [Enabling the Amazon RDS Data API](data-api.md "data-api.md").
- The DB cluster was renamed after Data API was enabled for it. In that
  case, turn off Data API for that cluster and then enable it again.
- The ARN you specified doesn't precisely match the ARN of the cluster.
  Check that the ARN returned from another source or constructed by program logic matches the
  ARN of the cluster exactly. For example, make sure that the ARN you use
  has the correct letter case for all alphabetic characters.

## DatabaseErrorException: Transaction is still running a query

If your application sends a request with a transaction ID and that transaction is currently processing another
request, Data API returns this error to your application immediately. This condition might arise if your
application makes asynchronous requests, using a mechanism such as "promises" in Javascript.

To solve this issue, wait until the previous request finishes and then retry the request. You can keep retrying until
the error no longer occurs, or the application receives some different kind of error.

This condition can happen with Data API for Aurora Serverless v2 and provisioned instances.
In Data API for Aurora Serverless v1, subsequent requests for the same transaction ID automatically
wait for the previous request to finish. However, that older behavior potentially could encounter timeouts
due to the previous request taking too long. If you are porting an older Data API application that
makes concurrent requests, modify your exception handling logic to account for this new kind
of error.

## Unsupported result exception

The Data API doesn't support all data types. This error occurs when you execute a
query that returns an unsupported data type.

To work around this issue, cast the unsupported data type to `TEXT`.
For example:

```
SELECT custom_type::TEXT FROM my_table;
-- OR
SELECT CAST(custom_type AS TEXT) FROM my_table;
```

## Multi-statements aren't supported

Multi-statements are not supported in the Data API for Aurora Serverless v2 and
provisioned clusters. Attempting to execute multiple statements in a single API call
results in this error.

To execute multiple statements, use separate `ExecuteStatement` API
calls or use the `BatchExecuteStatement` API for batch processing.

## Schema parameter isn't supported

Aurora Serverless v1 silently ignores the schema parameter. However, Aurora
Serverless v2 and provisioned clusters explicitly reject API calls that include the
schema parameter.

To solve this issue, remove the schema parameter from all calls to the Data API
when you use Aurora Serverless v2 or provisioned clusters.

## IPv6 connectivity issues

If you experience issues when connecting to Data API using IPv6 endpoints, check the following potential causes:

- **Network doesn't support IPv6**: Verify that your network infrastructure supports IPv6 and that IPv6 routing is configured correctly.
- **DNS resolution issues**: Ensure that your DNS resolver can resolve AAAA records for the dual-stack endpoints (e.g., `rds-data.us-east-1.api.aws`).
- **Security group configuration**: Update security group rules to allow IPv6 traffic on port 443 (HTTPS). Add rules for IPv6 CIDR blocks (e.g., `::/0` for all IPv6 addresses).
- **Network ACL configuration**: Ensure that network ACLs allow IPv6 traffic on the required ports.
- **Client library compatibility**: Verify that your HTTP client libraries and AWS SDKs support IPv6 and dual-stack connectivity.
- **VPC endpoint configuration**: If using PrivateLink, ensure that your VPC endpoint is configured to support IPv6 and that the associated subnets have IPv6 CIDR blocks assigned.

To troubleshoot IPv6 connectivity issues:

1. Test connectivity using the IPv4-only endpoints (`.amazonaws.com`) to verify that the issue is specific to IPv6.
2. Use network diagnostic tools to verify IPv6 connectivity to the dual-stack endpoints.
3. Check CloudTrail logs for any authentication or authorization errors when using IPv6 endpoints.
4. Verify that your application is correctly configured to use the new dual-stack endpoint URLs.
