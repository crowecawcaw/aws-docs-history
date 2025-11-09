# RDS Proxy concepts and terminology

You can simplify connection management for your Amazon RDS DB instances
by using RDS Proxy.

RDS Proxy handles the network traffic between the client application and the database. It does so in an active
way first by understanding the database protocol. It then adjusts its behavior based on the SQL operations
from your application and the result sets from the database.

RDS Proxy reduces the memory and CPU overhead for connection management on your database. The database needs
less memory and CPU resources when applications open many simultaneous connections. It also doesn't
require logic in your applications to close and reopen connections that stay idle for a long time. Similarly,
it requires less application logic to reestablish connections in case of a database problem.

The infrastructure for RDS Proxy is highly available and deployed over multiple
Availability Zones (AZs). The computation, memory, and storage for RDS Proxy are independent of
your RDS DB instance. This separation helps lower overhead on your database servers, so that
they can devote their resources to serving database workloads. The RDS Proxy compute resources
are serverless, automatically scaling based on your database workload.

###### Topics

- [Overview of RDS Proxy concepts](#rds-proxy-overview "#rds-proxy-overview")
- [Connection pooling](#rds-proxy-connection-pooling "#rds-proxy-connection-pooling")
- [RDS Proxy security](#rds-proxy-security "#rds-proxy-security")
- [Failover](#rds-proxy-failover "#rds-proxy-failover")
- [Transactions](#rds-proxy-transactions "#rds-proxy-transactions")

## Overview of RDS Proxy concepts

RDS Proxy handles the infrastructure to perform connection pooling and the other features described in the sections that follow.
You see the proxies represented in the RDS console on the **Proxies** page.

Each proxy handles connections to a single RDS DB
instance. The proxy
automatically determines the current writer instance for RDS
Multi-AZ DB instance or cluster.

The connections that a proxy keeps open and available for your database applications to use make up the
_connection pool_.

By default, RDS Proxy can reuse a connection after each transaction in your session. This transaction-level
reuse is called _multiplexing_. When RDS Proxy temporarily removes a connection from the
connection pool to reuse it, that operation is called _borrowing_ the connection.
When it's safe to do so, RDS Proxy returns that connection to the connection pool.

In some cases, RDS Proxy can't be sure that it's safe to reuse a database connection outside of the
current session. In these cases, it keeps the session on the same connection until the session ends. This fallback
behavior is called _pinning_.

A proxy has a default endpoint. You connect to this endpoint when you work with an
Amazon RDS DB instance.
You do so instead of connecting to the read/write endpoint
that connects directly to the instance
. For RDS DB clusters,
you can also create additional read/write and read-only endpoints. For more information, see [Overview of proxy endpoints](rds-proxy-endpoints.md#rds-proxy-endpoints-overview "rds-proxy-endpoints.md#rds-proxy-endpoints-overview").

For example, you can still connect to the cluster endpoint for read/write connections
without connection pooling. You can still connect to the reader endpoint for load-balanced
read-only connections. You can still connect to the instance endpoints for diagnosis and
troubleshooting of specific DB instances within a cluster. If you use other AWS
services such as AWS Lambda to connect to RDS databases, change their connection settings to
use the proxy endpoint. For example, you specify the proxy endpoint to allow Lambda functions
to access your database while taking advantage of RDS Proxy functionality.

Each proxy contains a target group. This _target
group_ embodies the RDS DB
instance that the proxy can
connect to.
The RDS DB instance associated with a proxy are called the _targets_ of
that proxy. For convenience, when you create a proxy through the console, RDS Proxy also
creates the corresponding target group and registers the associated targets automatically.

An _engine family_ is a related set of database engines that use the same DB protocol.
You choose the engine family for each proxy that you create.

## Connection pooling

Each proxy performs connection pooling separately for the writer and reader instance of its associated RDS database
. _Connection pooling_ is an optimization
that reduces the overhead associated with opening and closing connections and with keeping
many connections open simultaneously. This overhead includes memory needed to handle each
new connection. It also involves CPU overhead to close each connection and open a new one.
Examples include Transport Layer Security/Secure Sockets Layer (TLS/SSL) handshaking,
authentication, negotiating capabilities, and so on. Connection pooling simplifies your
application logic. You don't need to write application code to minimize the number of
simultaneous open connections.

Each proxy also performs connection multiplexing, also known as connection reuse. With
_multiplexing_, RDS Proxy performs all the operations for a transaction
using one underlying database connection. RDS then can use a different connection for the
next transaction. You can open many simultaneous connections to the proxy, and the proxy
keeps a smaller number of connections open to the DB instance or cluster. Doing so further
minimizes the memory overhead for connections on the database server. This technique also
reduces the chance of "too many connections" errors.

## RDS Proxy security

RDS Proxy uses the existing RDS security mechanisms such as TLS/SSL and AWS Identity and Access Management
(IAM). For general information about those security features, see [Security in Amazon RDS](UsingWithRDS.md "UsingWithRDS.md"). Also, make sure to familiarize
yourself with how RDS
work with authentication, authorization, and other areas of
security.

RDS Proxy can act as an additional layer of security between client applications and the
underlying database. For example, you can connect to the proxy using TLS 1.3, even if the
underlying DB instance supports an older version of TLS. You can connect to the proxy using
an IAM role even if the proxy connects to the database using the database user
and password authentication method. By using this technique, you can enforce strong
authentication requirements for database applications without a costly migration effort for
the DB instances themselves.

You can use the following methods of authentication with RDS Proxy:

- **Database credentials**
- **Standard IAM authentication**
- **End-to-end IAM authentication**

### Using IAM with RDS Proxy

RDS Proxy offers two methods of IAM authentication:

- **Standard IAM authentication**: Enforce IAM authentication for connections to
  your proxy while the proxy connects to the database using credentials stored in Secrets Manager.
  This enforces IAM authentication for database access even if the databases use native password authentication.
  The proxy retrieves the database credentials from Secrets Manager and handles the authentication to the database on behalf of your application.
- **End-to-end IAM authentication**: Enforces IAM authentication for connections directly from
  your applications to your database through the proxy. End-to-end IAM authentication simplifies your security configuration and
  avoids database credential management in Secrets Manager. This additional layer of security enforces IAM-based access
  control from the client application to the database.

To use standard IAM authentication, configure your proxy to use Secrets Manager secrets for authentication and enable IAM authentication for client connections.
Your applications authenticate to the proxy using IAM, while the proxy authenticates to the database using the credentials retrieved from Secrets Manager.

To use end-to-end IAM authentication, configure your proxy to use IAM authentication when setting the default authentication scheme
when creating or modifying your proxy.

For end-to-end IAM authentication, you must update the IAM role associated with the proxy to grant the `rds-db:connect` permission.
With end-to-end IAM authentication, this eliminates the need to register individual database users with the proxy through Secrets Manager secrets.

### Using TLS/SSL with RDS Proxy

You can connect to RDS Proxy using the TLS/SSL protocol.

###### Note

RDS Proxy uses certificates from the AWS Certificate Manager (ACM). If you are using RDS Proxy, you don't need
to download Amazon RDS certificates or update applications that use RDS Proxy connections.

To enforce TLS for all connections between the proxy and your database, you can
specify a setting **Require Transport Layer Security** when you create or
modify a proxy in the AWS Management Console.

RDS Proxy can also ensure that your session uses TLS/SSL between your client and the
RDS Proxy endpoint. To have RDS Proxy do so, specify the requirement on the client side. SSL
session variables are not set for SSL connections to a database using RDS Proxy.

- For RDS for MySQL, specify the requirement on the client side with the
  `--ssl-mode` parameter when you run the `mysql` command.
- For Amazon RDS PostgreSQL, specify `sslmode=require` as part of the
  `conninfo` string when you run the `psql` command.

RDS Proxy supports TLS protocol version 1.0, 1.1, 1.2, and 1.3. You can connect to the
proxy using a higher version of TLS than you use in the underlying database.

By default, client programs establish an encrypted connection with RDS Proxy, with
further control available through the `--ssl-mode` option. From the client
side, RDS Proxy supports all SSL modes.

For the client, the SSL modes are the following:

**PREFERRED**

SSL is the first choice, but it isn't required.

**DISABLED**

No SSL is allowed.

**REQUIRED**

Enforce SSL.

**VERIFY_CA**

Enforce SSL and verify the certificate authority (CA).

**VERIFY_IDENTITY**

Enforce SSL and verify the CA and CA hostname.

When using a client with `--ssl-mode`
`VERIFY_CA` or `VERIFY_IDENTITY`, specify the `--ssl-ca`
option pointing to a CA in `.pem` format. For the `.pem` file to
use, download all root CA PEMs from [Amazon Trust Services](https://www.amazontrust.com/repository/ "https://www.amazontrust.com/repository/") and place them into a single `.pem`
file.

RDS Proxy uses wildcard certificates, which apply to both a domain and its subdomains. If you use the
`mysql` client to connect with SSL mode `VERIFY_IDENTITY`, currently you must use
the MySQL 8.0-compatible `mysql` command.

## Failover

_Failover_ is a high-availability feature that replaces a
database instance with another one when the original instance becomes unavailable. A
failover might happen because of a problem with a database instance. It might also be part
of normal maintenance procedures, such as during a database upgrade. Failover applies to RDS
DB instances in a Multi-AZ configuration.

Connecting through a proxy makes your applications more resilient to database failovers. When the original DB
instance becomes unavailable, RDS Proxy connects to the standby database without dropping idle application
connections. This helps speed up and simplify the failover process. This is less disruptive to your application
than a typical reboot or database problem.

Without RDS Proxy, a failover involves a brief outage. During the outage, you can't
perform write operations on the database in failover. Any existing database connections are disrupted,
and your application must reopen them. The database becomes available for new connections
and write operations when a read-only DB instance is promoted in place of one that's
unavailable.

During DB failovers, RDS Proxy continues to accept connections at the same IP address and automatically
directs connections to the new primary DB instance. Clients connecting through RDS Proxy are not susceptible to the
following:

- Domain Name System (DNS) propagation delays on failover.
- Local DNS caching.
- Connection timeouts.
- Uncertainty about which DB instance is the current writer.
- Waiting for a query response from a former writer that became unavailable without closing connections.

For applications that maintain their own connection pool, going through RDS Proxy means that most connections
stay alive during failovers or other disruptions. Only connections that are in the middle of a transaction
or SQL statement are canceled. RDS Proxy immediately accepts new connections. When the database writer is
unavailable, RDS Proxy queues up incoming requests.

For applications that don't maintain their own connection pools, RDS Proxy offers faster connection rates
and more open connections. It offloads the expensive overhead of frequent reconnects from the database. It
does so by reusing database connections maintained in the RDS Proxy connection pool. This approach is
particularly important for TLS connections, where setup costs are significant.

## Transactions

All the statements within a single transaction always use the same underlying database connection. The
connection becomes available for use by a different session when the transaction ends. Using the transaction
as the unit of granularity has the following consequences:

- Connection reuse can happen after each individual statement when the RDS for MySQL
  `autocommit` setting is turned on.
- Conversely, when the `autocommit` setting is turned off, the first
  statement you issue in a session begins a new transaction. For example, suppose that you
  enter a sequence of `SELECT`, `INSERT`, `UPDATE`, and
  other data manipulation language (DML) statements. In this case, connection reuse
  doesn't happen until you issue a `COMMIT`, `ROLLBACK`, or
  otherwise end the transaction.
- Entering a data definition language (DDL) statement causes the transaction to end after that statement
  completes.

RDS Proxy detects when a transaction ends through the network protocol used by the database client
application. Transaction detection doesn't rely on keywords such as `COMMIT` or
`ROLLBACK` appearing in the text of the SQL statement.

In some cases, RDS Proxy might detect a database request that makes it impractical to move your session to a
different connection. In these cases, it turns off multiplexing for that connection the remainder of your
session. The same rule applies if RDS Proxy can't be certain that multiplexing is practical for the
session. This operation is called _pinning_. For ways to detect and
minimize pinning, see [Avoiding pinning an RDS Proxy](rds-proxy-pinning.md "rds-proxy-pinning.md").
