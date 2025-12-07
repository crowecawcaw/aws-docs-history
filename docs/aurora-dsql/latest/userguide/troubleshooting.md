# Troubleshooting issues in Aurora DSQL

###### Note

The following topics provide troubleshooting advice for errors and issues that you might
encounter when using Aurora DSQL. If you find an issue that is not listed here, reach out to AWS
support

###### Topics

- [Troubleshooting connection errors](#troubleshooting-connections "#troubleshooting-connections")
- [Troubleshooting authentication errors](#troubleshooting-authentication "#troubleshooting-authentication")
- [Troubleshooting authorization errors](#troubleshooting-authorization "#troubleshooting-authorization")
- [Troubleshooting SQL errors](#troubleshooting-sql "#troubleshooting-sql")
- [Troubleshooting OCC errors](#troubleshooting-occ "#troubleshooting-occ")
- [Troubleshooting SSL/TLS connections](#troubleshooting-ssl-tls "#troubleshooting-ssl-tls")

## Troubleshooting connection errors

**error: unrecognized SSL error code: 6**
or **unable to accept connection, sni was not received**

You might be using a psql version earlier than [version 14](https://www.postgresql.org/docs/release/14.0/ "https://www.postgresql.org/docs/release/14.0/"), which doesn't support
Server Name Indication (SNI).
The SNI is required when connecting to Aurora DSQL.

You can check your client version with `psql --version`.

**error: NetworkUnreachable**

A `NetworkUnreachable` error during connection attempts might indicate that your client
doesn't support IPv6 connections, rather than signaling an actual network problem. This error
commonly occurs on IPv4-only instances because of how PostgreSQL clients handle dual-stack
connections. When a server supports dual-stack mode, these clients first resolve hostnames to
both IPv4 and IPv6 addresses. They attempt an IPv4 connection first, then try IPv6 if the initial
connection fails. If your system doesn't support IPv6, you'll see a general `NetworkUnreachable`
error instead of a clear "IPv6 not supported" message.

## Troubleshooting authentication errors

**IAM authentication failed for user "..."**

When you generate an Aurora DSQL IAM authentication token, the maximum duration you can set is
1 week. After one week, you can't authenticate with that token.

Additionally, Aurora DSQL rejects your connection request if your assumed role has expired. For
example, if you try to connect with a temporary IAM role even if your authentication token
hasn't expired, Aurora DSQL will reject the connection request.

To learn more about how IAM works with Aurora DSQL, see [Understanding
authentication and authorization for Aurora DSQL](authentication-authorization.md "authentication-authorization.md") and [AWS Identity and Access Management in Aurora DSQL](security-iam.md "security-iam.md").

**An error occurred (InvalidAccessKeyId) when calling the GetObject
operation: The AWS Access Key ID you provided does not exist in our records**

IAM rejected your request. For more information, see [Why requests are
signed](../../../IAM/latest/UserGuide/reference_sigv.md#why-requests-are-signed "../../../IAM/latest/UserGuide/reference_sigv.md#why-requests-are-signed").

**IAM role <role> does not exist**

Aurora DSQL couldn't find your IAM role. For more information, see [IAM roles](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md").

**IAM role must look like an IAM ARN**

See [IAM Identifiers -
IAM ARNs](../../../IAM/latest/UserGuide/reference_identifiers.md#identifiers-arns "../../../IAM/latest/UserGuide/reference_identifiers.md#identifiers-arns") for more information.

## Troubleshooting authorization errors

**Role <role> not supported**

Aurora DSQL doesn't support the `GRANT` operation. See [Supported subsets of PostgreSQL commands in Aurora DSQL](working-with-postgresql-compatibility-supported-sql-subsets.md "working-with-postgresql-compatibility-supported-sql-subsets.md").

**Cannot establish trust with role <role>**

Aurora DSQL doesn't support the `GRANT` operation. See [Supported subsets of PostgreSQL commands in Aurora DSQL](working-with-postgresql-compatibility-supported-sql-subsets.md "working-with-postgresql-compatibility-supported-sql-subsets.md").

**Role <role> does not exist**

Aurora DSQL couldn't find specified database user. See [Authorize custom database roles to connect to a cluster](using-database-and-iam-roles.md#using-database-and-iam-roles-custom-database-roles "using-database-and-iam-roles.md#using-database-and-iam-roles-custom-database-roles").

**ERROR: permission denied to grant IAM trust with role
<role>**

To grant access to a database role, you must be connected to your cluster with the admin
role. To learn more, see [Authorize database roles to use SQL in a database](using-database-and-iam-roles.md#using-database-and-iam-roles-custom-database-roles-sql "using-database-and-iam-roles.md#using-database-and-iam-roles-custom-database-roles-sql").

**ERROR: role <role> must have the LOGIN
attribute**

Any database roles you create must have the `LOGIN` permission.

To address this error, make sure that you’ve created the PostgreSQL Role with the
`LOGIN` permission. For more information, see [CREATE ROLE](https://www.postgresql.org/docs/current/sql-createrole.html "https://www.postgresql.org/docs/current/sql-createrole.html") and [ALTER ROLE](https://www.postgresql.org/docs/current/sql-alterrole.html "https://www.postgresql.org/docs/current/sql-alterrole.html") in the
PostgreSQL documentation.

**ERROR: role <role> cannot be dropped because some objects depend
on it**

Aurora DSQL returns an error if you drop a database role with an IAM relationship until you
revoke the relationship using `AWS IAM REVOKE`. To learn more, see [Revoking authorization](authentication-authorization.md#authentication-authorization-revoke "authentication-authorization.md#authentication-authorization-revoke").

## Troubleshooting SQL errors

**Error: Not supported**

Aurora DSQL doesn't support all PostgreSQL-based dialect. To learn about what is supported, see
[Supported PostgreSQL features in Aurora DSQL](working-with-postgresql-compatibility-supported-sql-features.md "working-with-postgresql-compatibility-supported-sql-features.md") .

**Error: use `CREATE INDEX ASYNC` instead**

To create an index on a table with existing rows, you must use the `CREATE INDEX
 ASYNC` command. To learn more, see [Creating indexes
asynchronously in Aurora DSQL](working-with-create-index-async.md "working-with-create-index-async.md").

## Troubleshooting OCC errors

**OC000 “ERROR: mutation conflicts with another transaction, retry as
needed”**

This transaction attempted to modify the same tuples as another, concurrent, transaction.
This indicates contention on the modified tuples. To learn more, please
refer to [Concurrency control in Aurora DSQL](working-with-concurrency-control.md "working-with-concurrency-control.md")

**OC001 “ERROR: schema has been updated by another transaction, retry as
needed”**

Your PostgreSQL session had a cached copy of the schema catalog. That cached copy was valid
at the time was loaded. Let’s call the time T1 and the version V1.

Another transaction updates the catalog at time T2. Let’s call this V2.

When the original session attempts to read from storage at time T2 it’s still using catalog
version V1. Aurora DSQL’s storage layer rejects the request because the latest catalog version at T2
is V2.

When you retry at time T3 from the original session, Aurora DSQL refreshes the catalog cache. The
transaction at T3 is using catalog V2. Aurora DSQL will finish the transaction as long as no other
catalog changes came through since time T2.

## Troubleshooting SSL/TLS connections

**SSL error: certificate verify failed**

This error indicates that the client cannot verify the server's certificate. Ensure that:

1. The Amazon Root CA 1 certificate is properly installed. See [Configuring SSL/TLS certificates for Aurora DSQL connections](configure-root-certificates.md "configure-root-certificates.md") for instructions on how to validate and install this certificate.
2. The `PGSSLROOTCERT` environment variable points to the correct
   certificate file.
3. The certificate file has the correct permissions.

**Unrecognized SSL error code: 6**

This error occurs with PostgreSQL clients below version 14. Upgrade your PostgreSQL
client to version 17 to resolve this issue.

**SSL error: unregistered scheme (Windows)**

This is a known issue with the Windows psql client when using system certificates.
Use the downloaded certificate file method described in the [Connecting from Windows](configure-root-certificates.md#connect-windows "configure-root-certificates.md#connect-windows") instructions.
