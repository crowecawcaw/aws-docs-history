# Troubleshooting connection issues for Aurora MySQL databases

Ensuring reliable connectivity between your applications and your RDS DB instance is crucial for
the smooth operation of your workloads. However, connectivity issues can arise because of
various factors, such as network configurations, authentication problems, or resource
constraints. This guide aims to provide a comprehensive approach to troubleshooting
connectivity issues with Aurora MySQL.

###### Contents

- [Identifying database connectivity issues for Aurora MySQL](mysql-troubleshooting-dbconn.md#mysql-dbconn-identify "mysql-troubleshooting-dbconn.md#mysql-dbconn-identify")
- [Gathering data on connectivity issues for Aurora MySQL](mysql-troubleshooting-dbconn.md#mysql-dbconn-gather "mysql-troubleshooting-dbconn.md#mysql-dbconn-gather")
- [Monitoring database connections for Aurora MySQL](mysql-troubleshooting-dbconn.md#mysql-dbconn-monitor "mysql-troubleshooting-dbconn.md#mysql-dbconn-monitor")
  - [Additional monitoring for Aurora MySQL](mysql-troubleshooting-dbconn.md#mysql-dbconn-monitor-ams "mysql-troubleshooting-dbconn.md#mysql-dbconn-monitor-ams")

- [Connectivity error codes for Aurora MySQL](mysql-troubleshooting-dbconn.md#mysql-dbconn-errors "mysql-troubleshooting-dbconn.md#mysql-dbconn-errors")
- [Parameter tuning recommendations for Aurora MySQL](mysql-troubleshooting-dbconn.md#mysql-dbconn-params "mysql-troubleshooting-dbconn.md#mysql-dbconn-params")
- [Examples of troubleshooting database connection issues for Aurora MySQL](mysql-troubleshooting-dbconn.md#mysql-dbconn-examples "mysql-troubleshooting-dbconn.md#mysql-dbconn-examples")
  - [Example 1: Troubleshooting failed connection attempts](mysql-troubleshooting-dbconn.md#mysql-dbconn-example1 "mysql-troubleshooting-dbconn.md#mysql-dbconn-example1")
  - [Example 2: Troubleshooting abnormal client disconnects](mysql-troubleshooting-dbconn.md#mysql-dbconn-example2 "mysql-troubleshooting-dbconn.md#mysql-dbconn-example2")

## Identifying database connectivity issues for Aurora MySQL

Identifying the specific category of the connectivity issue can help narrow down the potential causes and guide the troubleshooting process. Each
category might require different approaches and techniques for diagnosis and resolution. Database connectivity issues can broadly be classified into
the following categories.

**Connection errors and exceptions**

Connection errors and exceptions can occur for various reasons, such as
incorrect connection strings, authentication failures, network disruptions,
or database server issues. Causes can include misconfigured connection
parameters, invalid credentials, network outages, or database server crashes
or restarts. Misconfigured security groups, virtual private cloud (VPC)
settings, network Access Control Lists (ACLs), and route tables associated
with subnets can also lead to connection issues.

**Connection limit reached**

This issue arises when the number of concurrent connections to the database server exceeds the maximum allowed limit. Database servers
typically have a configurable maximum connection limit defined by the parameter max_connections in the clusters and instance parameter
groups. By imposing a connection limit, the database server ensures that it has sufficient resources (for example, memory, CPU, and file
handles) to handle the existing connections efficiently and provide acceptable performance. Causes can include connection leaks in the
application, inefficient connection pooling, or an unexpected surge in connection requests.

**Connection timeouts**

Connection timeouts occur when the client application is unable to establish a connection with the database server within a specified
timeout period. Common causes include network issues, server overload, firewall rules, and misconfigured connection settings.

**Idle connection timeouts**

Idle connections that remain inactive for a prolonged period might be closed automatically by the database server to conserve
resources. This timeout is typically configurable using the `wait_timeout` and `interactive_timeout parameters`,
and should be adjusted based on the application's connection usage patterns. Causes can include application logic that leaves
connections idle for extended periods, or improper connection management.

**Intermittent disconnect of existing connections**

This class of errors refers to a scenario where established connections between a client application and the database are unexpectedly
terminated or disconnected at irregular intervals, despite being active and in use. These disconnections occur intermittently, meaning
they happen at irregular intervals and not consistently. The causes can include the following:

- Database server issues such as restarts or failovers
- Improper application connection handling
- Load balancing and proxy issues
- Network instability
- Problems with third-party components or middleware involved in the connection path
- Query execution timeouts
- Resource constraints on the server or client side

Identifying the root cause through comprehensive monitoring, logging, and analysis is crucial, while implementing proper error
handling, connection pooling, and retry mechanisms can help mitigate the impact of these intermittent disconnections on the
application's functionality and user experience.

## Gathering data on connectivity issues for Aurora MySQL

Gathering comprehensive data related to the application, database, network, and infrastructure components is crucial for effectively
troubleshooting connectivity issues between an application and an Aurora MySQL database. By collecting relevant logs, configurations, and diagnostic information, you gain valuable insights that can help
identify the root cause of the connectivity problems and guide you towards an appropriate resolution.

Network logs and configurations, such as security group rules, VPC settings, and route tables, are essential for identifying potential
network-related bottlenecks or misconfigurations that could be preventing the application from establishing a successful connection with the
database. By analyzing these network components, you can make sure that the necessary ports are open, IP addresses are allowed, and routing
configurations are set up correctly.

**Timestamps**

Record the exact timestamps when the connectivity issues occur. This can help identify patterns or correlate the issues with other
events or activities.

**DB engine logs**

In addition to the general database logs, review the database engine logs (for example, the MySQL error log and slow query log) for
any relevant information or errors that might be related to the intermittent connectivity issues. For more information, see [Logging for Aurora MySQL databases](aurora-mysql-troubleshooting-logging.md "aurora-mysql-troubleshooting-logging.md").

**Client application logs**

Collect detailed logs from the client applications that connect to the database. Application logs provide visibility into the
connection attempts, errors, and any relevant information from the application's perspective, which can reveal issues related to
connection strings, authentication credentials, or application-level connection handling.

Database logs, on the other hand, offer insights into database-side errors, slow queries, or events that might be contributing to the
connectivity issues. For more information, see [Logging for Aurora MySQL databases](aurora-mysql-troubleshooting-logging.md "aurora-mysql-troubleshooting-logging.md").

**Client environment variables**

Check whether any environment variables or configuration settings on the client side might be affecting the database connection, such
as proxy settings, SSL/TLS settings, or any other relevant variables.

**Client library versions**

Make sure that the client is using the latest versions of any database drivers, libraries, or frameworks used for database
connectivity. Outdated versions can have known issues or compatibility problems.

**Client network capture**

Perform a network capture on the client side using a tool such as Wireshark or `tcpdump` during the times when connectivity
issues occur. This can help identify any network-related issues or anomalies on the client side.

**Client network topology**

Understand the client's network topology, including any firewalls, load balancers, or other components such as RDS Proxy or Proxy SQL
that are making connections to the database instead of the client directly making connections.

**Client operating system settings**

Check the client's operating system settings that might affect network connectivity, such as firewall rules, network adapter settings,
and any other relevant settings.

**Connection pooling configuration**

If you're using a connection pooling mechanism in your application, review the configuration settings and monitor the pool metrics
(for example, active connections, idle connections, and connection timeouts) to ensure that the pool is functioning correctly. Also
review the pool settings, such as the maximum pool size, minimum pool size, and connection validation settings, to ensure that they are
configured correctly.

**Connection string**

The connection string typically includes parameters such as the hostname or endpoint, port number, database name, and authentication
credentials. Analyzing the connection string can help identify potential misconfigurations or incorrect settings that may be causing
connectivity problems. For example, an incorrect hostname or port number can prevent the client from reaching the database instance,
while invalid authentication credentials can lead to authentication failures and connection rejections. Additionally, the connection
string can reveal issues related to connection pooling, timeouts, or other connection-specific settings that could contribute to
connectivity issues. Providing the complete connection string used by the client application can help pinpoint any misconfigurations on
the client.

**Database metrics**

Monitor database metrics such as CPU usage, memory usage, and disk I/O during the times when connectivity issues occur. These can help
identify whether the DB instance is experiencing resource contention or performance issues.

**DB engine version**

Note the Aurora MySQL DB engine version. AWS
regularly releases updates addressing known issues, security vulnerabilities, and introducing performance enhancements. Therefore, we
highly recommend that you upgrade to the latest available versions, as these updates often include bug fixes and improvements
specifically related to connectivity, performance, and stability. Providing the database version information, along with the other
collected details, can assist Support in effectively diagnosing and resolving connectivity issues.

**Network metrics**

Collect network metrics such as latency, packet loss, and throughput during the times when connectivity issues occur. Tools such as
`ping`, `traceroute`, and network monitoring tools can help gather this data.

**Source and client details**

Determine the IP addresses of the application servers, load balancers, or any other components that are initiating the database
connections. This could be a single IP address or a range of IP addresses (CIDR notation). If the source is an Amazon EC2 instance, it also
helps to review the instance type, Availability Zone, subnet ID , and security groups associated with the instance, and network
interface details such as private IP address and public IP address.

By thoroughly analyzing the gathered data, you can identify misconfigurations, resource constraints, network disruptions, or other underlying
issues that are causing the intermittent or persistent connectivity problems. This information allows you to take targeted actions, such as
adjusting configurations, resolving network issues, or addressing application-level connection handling.

## Monitoring database connections for Aurora MySQL

To monitor and troubleshoot connectivity issues, you can use the following metrics and features.

**CloudWatch metrics**

- `CPUUtilization` – High CPU usage on the DB instance can lead to slow query execution, which can result in
  connection timeouts or rejections.
- `DatabaseConnections` – Monitor the number of active connections to the DB instance. A high number of connections
  close to the configured maximum can indicate potential connectivity issues or connection pool exhaustion.
- `FreeableMemory` – Low available memory can
  cause performance issues and connectivity problems because of
  resource constraints.
- `NetworkReceiveThroughput` and `NetworkTransmitThroughput` – Unusual spikes or drops in network
  throughput can indicate connectivity issues or network bottlenecks.

**Performance Insights metrics**

To troubleshoot connectivity issues in Aurora MySQL
using Performance Insights, analyze Database metrics such as the following:

- Aborted_clients
- Aborted_connects
- Connections
- max_connections
- Threads_connected
- Threads_created
- Threads_running

These metrics can help you to identify connection bottlenecks, detect network or authentication problems, optimize connection pooling,
and ensure efficient thread management. For more information, see [Performance Insights counters for Aurora MySQL](USER_PerfInsights_Counters.md#USER_PerfInsights_Counters.Aurora_MySQL "USER_PerfInsights_Counters.md#USER_PerfInsights_Counters.Aurora_MySQL").

**Performance Insights features**

- **Database Load** – Visualize the database load over time and correlate it with
  connectivity issues or performance degradation.
- **SQL Statistics** – Analyze SQL statistics to identify inefficient queries or database
  operations that might contribute to connectivity problems.
- **Top Queries** – Identify and analyze the most resource-intensive queries, which can help
  identify potential performance bottlenecks or long-running queries that may be causing connectivity issues.

By monitoring these metrics and leveraging Performance Insights, you can gain visibility into the database instance's performance, resource usage, and potential
bottlenecks that might be causing connectivity issues. For example:

- High `DatabaseConnections` close to the maximum limit can indicate connection pool exhaustion or improper connection handling,
  leading to connectivity problems.
- High `CPUUtilization` or low `FreeableMemory` can indicate resource constraints, which may cause slow query
  execution and connection timeouts or rejections.
- Analyzing the **Top Queries** and **SQL Statistics** can help identify inefficient or resource-intensive
  queries that may be contributing to connectivity issues.

Additionally, monitoring CloudWatch Logs and setting up alarms can help you proactively identify and respond to connectivity problems before they
escalate.

It's important to note that while these metrics and tools can provide valuable insights, they should be used in conjunction with other
troubleshooting steps. By also reviewing network configurations, security group rules, and application-level connection handling, you can
comprehensively diagnose and resolve connectivity issues with Aurora MySQL DB instances.

### Additional monitoring for Aurora MySQL

**CloudWatch metrics**

- `AbortedClients` – Tracks the number of client connections that have not been closed properly.
- `AuroraSlowConnectionHandleCount` – Tracks the number of slow connection handle operations, indicating
  potential connectivity issues or performance bottlenecks.
- `AuroraSlowHandshakeCount` – Measures the number of slow handshake operations, which can also be an indicator
  of connectivity problems.
- `ConnectionAttempts` – Measures the number of connection attempts made to the Aurora MySQL DB instance.

**Global status variables**

`Aurora_external_connection_count` – Shows the number of database connections to the DB instance, excluding RDS
service connections used for database health checks.

By monitoring these metrics and global status variables you can gain visibility into the connection patterns, errors, and potential
bottlenecks that may be causing connectivity issues with your Amazon Aurora MySQL instance.

For example, a high number of `AbortedClients` or `AuroraSlowConnectionHandleCount` can indicate connectivity
problems.

Additionally, setting up CloudWatch alarms and notifications can help you proactively identify and respond to connectivity issues before they
escalate and impact your application's performance.

## Connectivity error codes for Aurora MySQL

The following are some common connectivity errors for Aurora MySQL databases, along with their error codes and explanations.

**Error Code 1040: Too many connections**

This error occurs when the client tries to establish more connections than the maximum allowed by the database server. Possible causes
include the following:

- Connection pooling misconfiguration – If using a connection pooling mechanism, ensure that the maximum pool size is not
  set too high, and that connections are being properly released back to the pool.
- Database instance configuration – Verify the maximum allowed connections setting for the database instance and adjust
  it if necessary by setting the `max_connections` parameter.
- High concurrency – If multiple clients or applications are connecting to the database simultaneously, the maximum
  allowed connections limit may be reached.

**Error Code 1045: Access denied for user '...'@'...' (using password: YES/NO)**

This error indicates an authentication failure when attempting to connect to the database. Possible causes include the
following:

- Authentication plugin compatibility – Check whether the authentication plugin used by the client is compatible with the
  database server's authentication mechanism.
- Incorrect username or password – Verify that the correct username and password are being used in the connection string
  or authentication mechanism.
- User permissions – Make sure that the user has the necessary permissions to connect to the database instance from the
  specified host or network.

**Error Code 1049: Unknown database '...'**

This error indicates that the client is attempting to connect to a database that does not exist on the server. Possible causes include
the following:

- Database not created – Make sure that the specified database has been created on the database server.
- Incorrect database name – Double-check the database name used in the connection string or query for accuracy.
- User permissions – Verify that the user has the necessary permissions to access the specified database.

**Error Code 1153: Got a packet bigger than 'max_allowed_packet' bytes**

This error occurs when the client attempts to send or receive data that exceeds the maximum packet size allowed by the database
server. Possible causes include the following:

- Large queries or result sets – If executing queries that involve large amounts of data, the packet size limit may be
  exceeded.
- Misconfigured packet size settings – Check the `max_allowed_packet` setting on the database server and
  adjust it if necessary.
- Network configuration issues – Make sure that the network configuration (for example, MTU size) allows for the required
  packet sizes.

**Error Code 1226: User '...' has exceeded the 'max_user_connections' resource (current value: ...)**

This error indicates that the user has exceeded the maximum number of concurrent connections allowed by the database server. Possible
causes include the following::

- Connection pooling misconfiguration – If using a connection pooling mechanism, ensure that the maximum pool size is not
  set too high for the user's connection limit.
- Database instance configuration – Verify the `max_user_connections` setting for the database instance and
  adjust it if necessary.
- High concurrency – If multiple clients or applications are connecting to the database simultaneously using the same
  user, the user-specific connection limit may be reached.

**Error Code 2003: Can't connect to MySQL server on '...' (10061)**

This error typically occurs when the client is unable to establish a TCP/IP connection with the database server. It can be caused by
various issues, such as the following:

- Database instance status – Make sure that the database instance is in the `available` state, and not
  undergoing any maintenance or backup operations.
- Firewall rules – Check whether any firewalls (operating system, network, or security group) are blocking the connection
  on the specified port (usually 3306 for MySQL).
- Incorrect hostname or endpoint – Make sure that the hostname or endpoint used in the connection string is correct and
  matches the database instance.
- Network connectivity issues – Verify that the client machine can reach the database instance over the network. Check
  for any network outages, routing issues, or VPC or subnet misconfigurations.

**Error Code 2005: Unknown MySQL server host '...' (11001)**

This error occurs when the client is unable to resolve the hostname or endpoint of the database server to an IP address. Possible
causes include the following:

- DNS resolution issues – Verify that the client machine can resolve the hostname correctly using DNS. Check the DNS
  settings, DNS cache, and try using the IP address instead of the hostname.
- Incorrect hostname or endpoint – Double-check the hostname or endpoint used in the connection string for accuracy.
- Network configuration issues – Make sure that the client's network configuration (for example, VPC, subnet, and route
  tables) allows DNS resolution and connectivity to the database instance.

**Error Code 2026: SSL connection error**

This error occurs when there is an issue with the SSL/TLS configuration or certificate validation during the connection attempt.
Possible causes include the following:

- Certificate expiration – Check whether the SSL/TLS certificate used by the server has expired and needs to be
  renewed.
- Certificate validation issues – Verify that the client is able to validate the server's SSL/TLS certificate correctly, and that
  the certificate is trusted.
- Network configuration issues – Make sure that the network configuration allows for SSL/TLS connections and doesn't
  block or interfere with the SSL/TLS handshake process.
- SSL/TLS configuration mismatch – Make sure that the SSL/TLS settings (for example, cipher suites and protocol versions)
  on the client and server are compatible.

By understanding the detailed explanations and potential causes for each error code, you can better troubleshoot and resolve connectivity issues
when working with Aurora MySQL databases.

## Parameter tuning recommendations for Aurora MySQL

**Maximum connections**

Adjusting these parameters can help prevent connection issues caused by reaching the maximum allowed connections limit. Make sure that
these values are set appropriately based on your application's concurrency requirements and resource constraints.

- `max_connections` – This parameter specifies the maximum number of concurrent connections allowed to the
  DB instance.
- `max_user_connections` – This parameter can be specified during user creation and modification, and sets the maximum
  number of concurrent connections allowed for a specific user account.

**Network buffer size**

Increasing these values can improve network performance, especially for workloads involving large data transfers or result sets.
However, be cautious as larger buffer sizes can consume more memory.

- `net_buffer_length` – This parameter sets the initial size for client connection and result buffers,
  balancing memory usage with query performance.
- `max_allowed_packet` – This parameter specifies the maximum size of a single network packet that can be sent
  or received by the DB instance.

**Network compression (client side)**

Enabling network compression can reduce network bandwidth usage, but it can increase CPU overhead on both the client and server
sides.

- `compress` – This parameter enables or disables network compression for client/server communication.
- `compress_protocol` – This parameter specifies the compression protocol to use for network
  communication.

**Network performance tuning**

Adjusting these timeouts can help manage idle connections and prevent resource exhaustion, but be cautious as low values can cause
premature connection terminations.

- `interactive_timeout` – This parameter specifies the number of seconds the server waits for activity on an
  interactive connection before closing it.
- `wait_timeout` – This parameter determines the number of seconds the server waits for activity on a
  noninteractive connection before closing it.

**Network timeout settings**

Adjusting these timeouts can help address issues related to slow or unresponsive connections. But be careful not to set them too low,
as it can cause premature connection failures.

- `net_read_timeout` – This parameter specifies the number of seconds to wait for more data from a connection before
  ending the read operation.
- `net_write_timeout` – This parameter determines the number of seconds to wait for a block to be written to a
  connection before ending the write operation.

## Examples of troubleshooting database connection issues for Aurora MySQL

The following examples show how to identify and troubleshoot database connection issues for Aurora MySQL.

### Example 1: Troubleshooting failed connection attempts

Connection attempts can fail for several reasons, including authentication failures, SSL/TLS handshake failures, `max_connections`
limit reached, and resource constraints on the DB instance.

You can track the number of failed connections either from Performance Insights or by using the following command.

```
mysql> show global status like 'aborted_connects';
+------------------+-------+
| Variable_name    | Value |
+------------------+-------+
| Aborted_connects | 7     |
+------------------+-------+
1 row in set (0.00 sec)
```

If the number of `Aborted_connects` increases over time, then the application could be having intermittent connectivity
issues.

You can use [Aurora Advanced Auditing](AuroraMySQL.md "AuroraMySQL.md") to log the connects and disconnects from the client
connections. You can do this by setting the following parameters in the DB cluster parameter group:

- `server_audit_logging` = `1`
- `server_audit_events` = `CONNECT`

The following is an extract from the audit logs for a failed login.

```
1728498527380921,auora-mysql-node1,user_1,172.31.49.222,147189,0,FAILED_CONNECT,,,1045
1728498527380940,auora-mysql-node1,user_1,172.31.49.222,147189,0,DISCONNECT,,,0
```

Where:

- `1728498527380921` – The epoch timestamp of when the failed login occurred
- `aurora-mysql-node1` – The instance identifier of the node of the Aurora MySQL cluster on which the connection
  failed
- `user_1` – The name of the database user for which the login failed
- `172.31.49.222` – The private IP address of the client from which the connection was established
- `147189` – The connection ID of the failed login
- `FAILED_CONNECT` – Indicates that the connection failed.
- `1045` – The return code. A nonzero value indicates an error. In this case, `1045` corresponds to access
  denied.

For more information, see [Server error codes](https://dev.mysql.com/doc/mysql-errors/5.7/en/server-error-reference.html "https://dev.mysql.com/doc/mysql-errors/5.7/en/server-error-reference.html")
and [Client error codes](https://dev.mysql.com/doc/mysql-errors/5.7/en/client-error-reference.html "https://dev.mysql.com/doc/mysql-errors/5.7/en/client-error-reference.html") in the MySQL
documentation.

You can also examine the Aurora MySQL error logs for any related error messages, for example:

```
2024-10-09T19:26:59.310443Z 220 [Note] [MY-010926] [Server] Access denied for user 'user_1'@'172.31.49.222' (using password: YES) (sql_authentication.cc:1502)
```

### Example 2: Troubleshooting abnormal client disconnects

You can track the number of abnormal client disconnects either from Performance Insights or by using the following command.

```
mysql> show global status like 'aborted_clients';
+-----------------+-------+
| Variable_name   | Value |
+-----------------+-------+
| Aborted_clients | 9     |
+-----------------+-------+
1 row in set (0.01 sec)
```

If the number of `Aborted_clients` increases over time, then the application isn't closing the connections to the database
correctly. If connections aren't closed properly, it can lead to resource leaks and potential performance issues. Leaving connections open
unnecessarily can consume system resources, such as memory and file descriptors, which can eventually cause the application or server to become
unresponsive or restart.

You can use the following query to identify accounts that aren't closing connections properly. It retrieves the user account name, the host
from which the user is connecting, the number of connections not closed, and the percentage of connections not closed.

```
SELECT
    ess.user,
    ess.host,
    (a.total_connections - a.current_connections) - ess.count_star AS not_closed,
    (((a.total_connections - a.current_connections) - ess.count_star) * 100) / (a.total_connections - a.current_connections) AS pct_not_closed
FROM
    performance_schema.events_statements_summary_by_account_by_event_name AS ess
    JOIN performance_schema.accounts AS a ON (ess.user = a.user AND ess.host = a.host)
WHERE
    ess.event_name = 'statement/com/quit'
    AND (a.total_connections - a.current_connections) > ess.count_star;

+----------+---------------+------------+----------------+
| user     | host          | not_closed | pct_not_closed |
+----------+---------------+------------+----------------+
| user1    | 172.31.49.222 |          1 |        33.3333 |
| user1    | 172.31.93.250 |       1024 |        12.1021 |
| user2    | 172.31.93.250 |         10 |        12.8551 |
+----------+---------------+------------+----------------+
3 rows in set (0.00 sec)
```

After you identify the user accounts and hosts from which the connections aren't closed, you can proceed to check the code that isn't closing
the connections gracefully.

For example, with the MySQL connector in Python, use the `close()` method of the connection object to close connections. Here's an
example function that establishes a connection to a database, performs a query, and closes the connection:

```
import mysql.connector

def execute_query(query):
    # Establish a connection to the database
    connection = mysql.connector.connect(
        host="your_host",
        user="your_username",
        password="your_password",
        database="your_database"
    )

    try:
        # Create a cursor object
        cursor = connection.cursor()

        # Execute the query
        cursor.execute(query)

        # Fetch and process the results
        results = cursor.fetchall()
        for row in results:
            print(row)

    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()
```

In this example, the `connection.close()` method is called in the `finally` block to make sure that the connection is
closed, whether or not an exception occurs.
