

# Troubleshooting issues in Aurora DSQL
<a name="troubleshooting"></a>

**Note**  
The following topics provide troubleshooting advice for errors and issues that you might encounter when using Aurora DSQL. If you find an issue that is not listed here, reach out to AWS support

**Topics**
+ [Troubleshooting connection errors](#troubleshooting-connections)
+ [Troubleshooting authentication errors](#troubleshooting-authentication)
+ [Troubleshooting authorization errors](#troubleshooting-authorization)
+ [Troubleshooting SQL errors](#troubleshooting-sql)
+ [Troubleshooting concurrency control responses](#troubleshooting-occ)
+ [Troubleshooting SSL/TLS connections](#troubleshooting-ssl-tls)
+ [Troubleshooting missing metrics from the Amazon CloudWatch Database Insights console](#troubleshooting-database-insights)

## Troubleshooting connection errors
<a name="troubleshooting-connections"></a>

**error: unrecognized SSL error code: 6** or **unable to accept connection, sni was not received**

You might be using a psql version earlier than [version 14](https://www.postgresql.org/docs/release/14.0/), which doesn't support Server Name Indication (SNI). The SNI is required when connecting to Aurora DSQL.

You can check your client version with `psql --version`.

**error: NetworkUnreachable**

A `NetworkUnreachable` error during connection attempts might indicate that your client doesn't support IPv6 connections, rather than signaling an actual network problem. This error commonly occurs on IPv4-only instances because of how PostgreSQL clients handle dual-stack connections. When a server supports dual-stack mode, these clients first resolve hostnames to both IPv4 and IPv6 addresses. They attempt an IPv4 connection first, then try IPv6 if the initial connection fails. If your system doesn't support IPv6, you'll see a general `NetworkUnreachable` error instead of a clear "IPv6 not supported" message.

## Troubleshooting authentication errors
<a name="troubleshooting-authentication"></a>

**IAM authentication failed for user "..."**

When you generate an Aurora DSQL IAM authentication token, the maximum duration you can set is 1 week. After one week, you can't authenticate with that token.

Additionally, Aurora DSQL rejects your connection request if your assumed role has expired. For example, if you try to connect with a temporary IAM role even if your authentication token hasn't expired, Aurora DSQL will reject the connection request.

To learn more about how IAM works with Aurora DSQL, see [ Understanding authentication and authorization for Aurora DSQL ](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/authentication-authorization.html) and [AWS Identity and Access Management in Aurora DSQL](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/security-iam.html).

** An error occurred (InvalidAccessKeyId) when calling the GetObject operation: The AWS Access Key ID you provided does not exist in our records**

IAM rejected your request. For more information, see [ Why requests are signed](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html#why-requests-are-signed).

**IAM role <role> does not exist**

Aurora DSQL couldn't find your IAM role. For more information, see [IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html).

**IAM role must look like an IAM ARN**

See [ IAM Identifiers - IAM ARNs](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-arns) for more information.

**Wrong user to action mapping**

This error occurs when the authentication token type does not match the database role. Aurora DSQL uses two token types: `DbConnectAdmin` for the `admin` role and `DbConnect` for custom database roles.
+ If you see `Wrong user to action mapping. user: admin, action: DbConnect`, use `generate-db-connect-admin-auth-token` instead of `generate-db-connect-auth-token`.
+ If you see `Wrong user to action mapping. user: {{myusername}}, action: DbConnectAdmin`, use `generate-db-connect-auth-token` instead of `generate-db-connect-admin-auth-token`.

## Troubleshooting authorization errors
<a name="troubleshooting-authorization"></a>

**Role <role> not supported**

Aurora DSQL doesn't support the `GRANT` operation. See [Supported subsets of SQL commands in Aurora DSQL](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/working-with-postgresql-compatibility-supported-sql-subsets.html).

**Cannot establish trust with role <role>**

Aurora DSQL doesn't support the `GRANT` operation. See [Supported subsets of SQL commands in Aurora DSQL](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/working-with-postgresql-compatibility-supported-sql-subsets.html).

**Role <role> does not exist**

Aurora DSQL couldn't find specified database user. See [ Authorize custom database roles to connect to a cluster](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/using-database-and-iam-roles.html#using-database-and-iam-roles-custom-database-roles).

**ERROR: permission denied to grant IAM trust with role <role>**

To grant access to a database role, you must be connected to your cluster with the admin role. To learn more, see [ Authorize database roles to use SQL in a database](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/using-database-and-iam-roles.html#using-database-and-iam-roles-custom-database-roles-sql).

**ERROR: role <role> must have the LOGIN attribute**

Any database roles you create must have the `LOGIN` permission.

To address this error, make sure that you've created the PostgreSQL Role with the `LOGIN` permission. For more information, see [CREATE ROLE](https://www.postgresql.org/docs/current/sql-createrole.html) and [ALTER ROLE](https://www.postgresql.org/docs/current/sql-alterrole.html) in the PostgreSQL documentation.

**ERROR: role <role> cannot be dropped because some objects depend on it**

Aurora DSQL returns an error if you drop a database role with an IAM relationship until you revoke the relationship using `AWS IAM REVOKE`. To learn more, see [Revoking authorization](authentication-authorization.md#authentication-authorization-revoke).

## Troubleshooting SQL errors
<a name="troubleshooting-sql"></a>

**Error: Not supported**

Aurora DSQL doesn't support all PostgreSQL-based dialect. To learn about what is supported, see [ Supported PostgreSQL features in Aurora DSQL ](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/working-with-postgresql-compatibility-supported-sql-features.html).

**Error: use `CREATE INDEX ASYNC` instead**

To create an index on a table with existing rows, you must use the `CREATE INDEX ASYNC` command. To learn more, see [ Creating indexes asynchronously in Aurora DSQL](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/working-with-create-index-async.html).

## Troubleshooting concurrency control responses
<a name="troubleshooting-occ"></a>

**OC000 "ERROR: change conflicts with another transaction (OC000)"**

This transaction attempted to modify the same tuples as another concurrent transaction. This indicates contention on the modified tuples. To learn more, refer to [ Concurrency control in Aurora DSQL ](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/working-with-concurrency-control.html).

**OC001 "ERROR: schema has been updated by another transaction (OC001)"**

Your session had a cached copy of the schema catalog at version V1, loaded at time T1.

A separate transaction updated the catalog to version V2 at time T2.

At time T3, when your session runs a query, it detects that it's behind and attempts to rebase onto the new catalog changes. In some situations the rebase can't succeed, and Aurora DSQL returns a `40001` OC001 response. The time between T2 and T3 can range from milliseconds to minutes, because query processors discover catalog changes reactively rather than receiving proactive updates.

When you retry from the same session, Aurora DSQL refreshes the catalog cache. The retried transaction uses catalog V2 and succeeds as long as no further catalog changes have occurred since T2.

## Troubleshooting SSL/TLS connections
<a name="troubleshooting-ssl-tls"></a>

**SSL error: certificate verify failed**

This error indicates that the client cannot verify the server's certificate. Ensure that:

1. The Amazon Root CA 1 certificate is properly installed. See [Configuring SSL/TLS certificates for Aurora DSQL connections](configure-root-certificates.md) for instructions on how to validate and install this certificate. 

1. The `PGSSLROOTCERT` environment variable points to the correct certificate file.

1. The certificate file has the correct permissions.

**Unrecognized SSL error code: 6**

This error occurs with PostgreSQL clients below version 14. Upgrade your PostgreSQL client to version 17 to resolve this issue.

**SSL error: unregistered scheme (Windows)**

This is a known issue with the Windows psql client when using system certificates. Use the downloaded certificate file method described in the [Connecting from Windows](configure-root-certificates.md#connect-windows) instructions.

## Troubleshooting missing metrics from the Amazon CloudWatch Database Insights console
<a name="troubleshooting-database-insights"></a>

### Aurora DSQL cluster not appearing in the Amazon CloudWatch Database Insights console
<a name="troubleshooting-database-insights-symptom"></a>

Amazon CloudWatch Database Insights populates its cluster selector using activity data from Aurora DSQL database insights. For more information about Aurora DSQL database insights, see [Monitoring Aurora DSQL clusters with Aurora DSQL Database Insights](dsql-db-insights.md). A cluster becomes visible in Database Insights only after the cluster has generated load within the last eight days that was captured by Aurora DSQL active session history (DASH) sampler.

DASH uses 1-second sampling, which might miss fast, infrequent transactions that complete in milliseconds.

Use the following steps to confirm whether this explains what you're seeing:

1. Confirm that you have run transactions on the cluster within the last eight days. A cluster that has been idle longer than that doesn't appear in Database Insights regardless of how you used it previously. To check for recent activity, view the `TotalTransactions` metric for your cluster in CloudWatch. For more information about this metric, see [Observability and performance](cloudwatch-monitoring.md#observability-performance).

1. Run a sustained workload against the cluster so that at least one session stays active. Examples include a load-testing script, a batch of inserts, or a long-running query. Because DASH samples once per second, a brief workload might not be captured, so the more continuous the activity, the more likely it is to appear.

1. Wait a few minutes after running that workload, then refresh the Database Insights console.

1. Verify that you're viewing the same AWS Region and account where the cluster was created. Selecting the wrong Region or account is a common reason a cluster appears to be missing.