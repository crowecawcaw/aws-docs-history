# RDS Proxy connection considerations

## Configuring connection settings

To adjust RDS Proxy's connection pooling, you can modify the following
settings:

- [IdleClientTimeout](#rds-proxy-connection-pooling-tuning.idleclienttimeout "#rds-proxy-connection-pooling-tuning.idleclienttimeout")
- [MaxConnectionsPercent](#rds-proxy-connection-pooling-tuning.maxconnectionspercent "#rds-proxy-connection-pooling-tuning.maxconnectionspercent")
- [MaxIdleConnectionsPercent](#rds-proxy-connection-pooling-tuning.maxidleconnectionspercent "#rds-proxy-connection-pooling-tuning.maxidleconnectionspercent")
- [ConnectionBorrowTimeout](#rds-proxy-connection-pooling-tuning.connectionborrowtimeout "#rds-proxy-connection-pooling-tuning.connectionborrowtimeout")

### IdleClientTimeout

You can specify how long a client connection can be idle before the proxy closes
it. The default is 1,800 seconds (30 minutes).

A client connection is considered _idle_ when the
application doesn't submit a new request within the specified time after the previous
request completed. The underlying database connection stays open and is returned to the
connection pool. Thus, it's available to be reused for new client connections. If you
want the proxy to proactively remove stale connections, then lowering the idle client
connection timeout. If your workload establishes frequent connections with the proxy,
then raise the idle client connection timeout to save the cost of establishing
connections.

This setting is represented by the **Idle client connection timeout**
field in the RDS console and the `IdleClientTimeout` setting in the AWS CLI and
the API. To learn how to change the value of the **Idle client connection
timeout** field in the RDS console, see [AWS Management Console](rds-proxy-modifying-proxy.md#rds-proxy-modifying-proxy.console "rds-proxy-modifying-proxy.md#rds-proxy-modifying-proxy.console"). To learn how to change the value of
the `IdleClientTimeout` setting, see the CLI command [modify-db-proxy](../../../cli/latest/reference/rds/modify-db-proxy.md "../../../cli/latest/reference/rds/modify-db-proxy.md") or the API operation [ModifyDBProxy](../APIReference/API_ModifyDBProxy.md "../APIReference/API_ModifyDBProxy.md").

### MaxConnectionsPercent

You can limit the number of connections that an RDS Proxy can establish with the
target database. You specify the limit as a percentage of the maximum connections available for your database.
This setting is represented by the **Connection pool maximum
connections** field in the RDS console and the `MaxConnectionsPercent` setting in the AWS CLI and the API.

The `MaxConnectionsPercent` value is expressed as a percentage of the `max_connections` setting for
the RDS DB instance used by the target group.
The proxy doesn't create all of these connections in
advance. This setting allows the proxy to establish these connections as the workload needs them.

For example, for a registered database target with `max_connections` set to 1000,
and `MaxConnectionsPercent` set to 95, RDS Proxy sets 950 connections as the
upper limit for concurrent connections to that database target.

A common side-effect of your workload reaching the maximum number of allowed database connections is an increase in overall query latency,
along with an increase in the `DatabaseConnectionsBorrowLatency` metric.
You can monitor currently used and total allowed database connections by
comparing the `DatabaseConnections` and `MaxDatabaseConnectionsAllowed` metrics.

When setting this parameter, note the following best practices:

- Allow sufficient connection headroom for changes in workload pattern.
  It is recommended to set the parameter at least 30% above your maximum recent monitored usage.
  As RDS Proxy redistributes database connection quotas across multiple nodes,
  internal capacity changes might require at least 30% headroom for additional connections to avoid increased borrow latencies.
- RDS Proxy reserves a certain number of connections for active monitoring to support fast failover, traffic routing and internal operations.
  The `MaxDatabaseConnectionsAllowed` metric does not include these reserved connections.
  It represents the number of connections available to serve the workload,
  and can be lower than the value derived from the `MaxConnectionsPercent` setting.

Minimal recommended `MaxConnectionsPercent` values

    + db.t3.small: 30
    + db.t3.medium or above: 20

To learn how to change the value of the **Connection pool maximum connections** field in
the RDS console, see [AWS Management Console](rds-proxy-modifying-proxy.md#rds-proxy-modifying-proxy.console "rds-proxy-modifying-proxy.md#rds-proxy-modifying-proxy.console"). To learn how to change the value of
the `MaxConnectionsPercent` setting, see the CLI command [modify-db-proxy-target-group](../../../cli/latest/reference/rds/modify-db-proxy-target-group.md "../../../cli/latest/reference/rds/modify-db-proxy-target-group.md") or the API operation [ModifyDBProxyTargetGroup](../APIReference/API_ModifyDBProxyTargetGroup.md "../APIReference/API_ModifyDBProxyTargetGroup.md").

For information on database connection limits, see [Maximum number of database connections](CHAP_Limits.md#RDS_Limits.MaxConnections "CHAP_Limits.md#RDS_Limits.MaxConnections").

### MaxIdleConnectionsPercent

You can control the number of idle database connections that RDS Proxy can keep in the
connection pool. By default, RDS Proxy considers a database connection in its pool to be _idle_ when there's been no activity on the connection for five
minutes.

The `MaxIdleConnectionsPercent` value is expressed as a
percentage of the `max_connections` setting for the RDS DB instance target group.
The default value is 50 percent of `MaxConnectionsPercent`, and the
upper limit is the value of `MaxConnectionsPercent`. For example, if
`MaxConnectionsPercent`, is 80, then the default value of
`MaxIdleConnectionsPercent` is 40.
If the value of
`MaxConnectionsPercent` isn’t specified, then for RDS for SQL Server,
`MaxIdleConnectionsPercent` is 5, and for all other engines, the default is 50.

With a high value, the proxy leaves a high percentage of idle database connections
open. With a low value, the proxy closes a high percentage of idle database connections.
If your workloads are unpredictable, consider setting a high value for
`MaxIdleConnectionsPercent`. Doing so means that RDS Proxy can accommodate
surges in activity without opening a lot of new database connections.

This setting is represented by the
`MaxIdleConnectionsPercent`
setting of `DBProxyTargetGroup` in the AWS CLI and the API.
To
learn how to change the value of the `MaxIdleConnectionsPercent` setting, see
the CLI command [modify-db-proxy-target-group](../../../cli/latest/reference/rds/modify-db-proxy-target-group.md "../../../cli/latest/reference/rds/modify-db-proxy-target-group.md") or the API operation [ModifyDBProxyTargetGroup](../APIReference/API_ModifyDBProxyTargetGroup.md "../APIReference/API_ModifyDBProxyTargetGroup.md").

For information on database connection limits, see [Maximum number of database connections](CHAP_Limits.md#RDS_Limits.MaxConnections "CHAP_Limits.md#RDS_Limits.MaxConnections").

### ConnectionBorrowTimeout

You can choose how long RDS Proxy waits for a database connection in the connection pool to become available for use
before returning a timeout error. The default is 120 seconds. This setting applies when the number of connections is at the maximum, and
so no connections are available in the connection pool. It also applies when no appropriate
database instance is available to handle the request, such as when a failover
operation is in process. Using this setting, you can set the best wait period for your
application without changing the query timeout in your application code.

This setting is represented by the **Connection borrow timeout**
field in the RDS console or the `ConnectionBorrowTimeout` setting of
`DBProxyTargetGroup` in the AWS CLI or API. To learn how to change the value of
the **Connection borrow timeout** field in the RDS console, see [AWS Management Console](rds-proxy-modifying-proxy.md#rds-proxy-modifying-proxy.console "rds-proxy-modifying-proxy.md#rds-proxy-modifying-proxy.console"). To learn how to change the value of
the `ConnectionBorrowTimeout` setting, see the CLI command [modify-db-proxy-target-group](../../../cli/latest/reference/rds/modify-db-proxy-target-group.md "../../../cli/latest/reference/rds/modify-db-proxy-target-group.md") or the API operation [ModifyDBProxyTargetGroup](../APIReference/API_ModifyDBProxyTargetGroup.md "../APIReference/API_ModifyDBProxyTargetGroup.md").

## Client and database connections

Connections from your application to RDS Proxy are known as client connections.
Connections from a proxy to the database are database connections.
When using RDS Proxy, client connections terminate
at the proxy while database connections are managed within RDS Proxy.

Application-side connection pooling can provide the benefit of reducing
recurring connection establishment between your application and RDS Proxy.

Consider the following configuration aspects before implementing an application-side connection pool:

- Client connection max life: RDS Proxy enforces a maximum life of client connections of 24 hours.
  This value is not configurable. Configure your pool with a maximum connection life less than 24 hours
  to avoid unexpected client connection drops.
- Client connection idle timeout: RDS Proxy enforces a maximum idle time for client connections.
  Configure your pool with an idle connection timeout of a value lower than your client connection
  idle timeout setting for RDS Proxy to avoid unexpected connection drops.

The maximum number of client connections configured in your application-side connection pool
does not have to be limited to the **max_connections** setting for RDS Proxy.

Client connection pooling results in a longer client connection life. If your connections
experience pinning, then pooling client connections might reduce multiplexing efficiency.
Client connections that are pinned but idle in the application-side connection pool continue to hold
on to a database connection and prevent the database connection to be reused by other client connections.
Review your proxy logs to check whether your connections experience pinning.

###### Note

RDS Proxy closes database connections some time after 24 hours when they are no longer
in use. The proxy performs this action regardless of the value of the maximum idle
connections setting.
