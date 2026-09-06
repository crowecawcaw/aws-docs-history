

# Configuration guidelines
<a name="rds-proxy-best-practices.configuration"></a>

This section describes the settings available in RDS Proxy and provides best practices for aligning configuration across the application stack. These are combined guidelines for using RDS Proxy with Amazon RDS and Amazon Aurora. RDS-specific and Aurora-specific notes are called out where applicable.

Unless noted otherwise, the terms "database" or "target" refer to an Aurora cluster, an Amazon RDS Multi-AZ DB cluster, or an Amazon RDS instance.

**Topics**
+ [Settings for RDS Proxy](#rds-proxy-best-practices.configuration-settings)
+ [Aligning application, proxy, and database configuration](#rds-proxy-best-practices.configuration.alignment)
+ [Database configuration](#rds-proxy-best-practices.configuration.alignment.database)
+ [Application configuration](#rds-proxy-best-practices.configuration.alignment.application)

## Settings for RDS Proxy
<a name="rds-proxy-best-practices.configuration-settings"></a>

### MaxConnectionsPercent
<a name="rds-proxy-best-practices.configuration.maxconnectionspercent"></a>


| Minimum value | Maximum value | Default value | 
| --- | --- | --- | 
| lesser of (1, MaxIdleConnectionsPercent) | 100 | 100 | 

For more information, see [MaxConnectionsPercent](rds-proxy-connections.md#rds-proxy-connection-pooling-tuning.maxconnectionspercent).

This setting limits the number of connections that RDS Proxy can establish with the target database, as a percentage of the maximum number of connections allowed by the database. The proxy opens back-end connections as needed, so the actual number of connections at any given time might be lower than the configured maximum.

Given that the `MaxConnectionsPercent` setting is a percentage of the database connection limit, the proxy's connection pool size automatically follows database configuration. This means you don't need to reconfigure your proxies whenever you resize your database instances or make configuration changes. It also means you need to be aware of the scenarios when the database settings might change, whether implicitly or explicitly:
+ If you did not explicitly set the connection limit (such as the `max_connections` parameter) in your database's parameter group, Amazon RDS and Aurora calculate it automatically based on the database instance class. As a result, the implicit connection limit can change when you scale your database instances, thus influencing the maximum pool size in the proxy. For more information, see [Maximum number of database connections](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Limits.html#RDS_Limits.MaxConnections) in the *Amazon RDS User Guide*, [Maximum connections to an Aurora MySQL DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Managing.Performance.html#AuroraMySQL.Managing.MaxConnections), and [Maximum connections to an Aurora PostgreSQL DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Managing.html#AuroraPostgreSQL.Managing.MaxConnections) in the *Amazon Aurora User Guide*.
+ Aurora Serverless v2 database instances determine their connection limit based on the database's maximum ACU configuration. For details, see [Maximum connections for Aurora Serverless v2](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.setting-capacity.html#aurora-serverless-v2.max-connections) in the *Amazon Aurora User Guide*.

Best practices:
+ The default setting of 100 percent is suitable for databases that receive all of their traffic through the proxy and don't need any headroom for administrative access or other clients.
+ Reduce this setting when the database also receives traffic directly from applications (bypassing the proxy) and you don't want the proxy to consume all the connections, or when you want to set a certain number of connections aside for other purposes such as direct access by database administrators.
+ When using RDS Proxy with Aurora Global Database clusters and Write Forwarding is enabled, reduce your proxy's `MaxConnectionsPercent` value by the quota that's allotted for write forwarding. For details, see configuration parameters for write forwarding in [Aurora MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-write-forwarding-ams.html#aurora-global-database-write-forwarding-params-ams) and [Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-write-forwarding-apg.html#aurora-global-database-write-forwarding-params-apg) in the *Amazon Aurora User Guide*. This recommendation applies whether the proxy is serving a cluster in the primary or a secondary Region of the global database. Secondary clusters can be promoted to the primary role, so it's a good practice to keep proxy settings consistent across the entire global topology. You *can* use asymmetric settings for proxies serving primary versus secondary regions, but you'll need to adjust those settings after each global failover or switchover.
+ If the target serves multiple proxies, the combined value of `MaxConnectionsPercent` across all those proxies must not exceed 100 so that the database doesn't become oversubscribed. We recommend using a single proxy per target to simplify configuration and management. In particular, you don't need to use multiple proxies per database for redundancy. For more information, see [Using multiple proxies with one target](rds-proxy-best-practices.usage-scenarios.md#rds-proxy-best-practices.multiple-proxies).

Whether you're using the default `MaxConnectionsPercent` setting or a custom value, keep at least a 30% headroom between the number of connections allowed and the maximum number of client connections expected during peak periods. For example:
+ If you believe the proxy will need up to 50% of the connection limit configured for the database, use a `MaxConnectionsPercent` setting of at least `1.3 * 50% = 65%`.
+ When using the default `MaxConnectionsPercent` setting of 100, make sure the database limit itself provides enough headroom.

This additional headroom improves client experience during unexpected workload spikes and helps RDS Proxy redistribute connections across its internal infrastructure for heat management and other purposes.

Although you can set `MaxConnectionsPercent` to a value as low as 1, we recommend the following minimums based on instance type:
+ db.t3.small: 100
+ db.t3.medium: 55
+ db.t3.large: 35
+ db.r3.large or above: 20

### MaxIdleConnectionsPercent
<a name="rds-proxy-best-practices.configuration.maxidleconnectionspercent"></a>


| Minimum value | Maximum value | Default value (SQL Server) | Default value (other engines) | 
| --- | --- | --- | --- | 
| (zero) | MaxConnectionsPercent | 5% of MaxConnectionsPercent | 50% of MaxConnectionsPercent | 

For more information, see [MaxIdleConnectionsPercent](rds-proxy-connections.md#rds-proxy-connection-pooling-tuning.maxidleconnectionspercent).

This setting limits the number of idle database connections that RDS Proxy keeps in the connection pool, as a percentage of the maximum number of connections allowed by the database. A database (back-end) connection is considered to be idle when there's been no activity on the connection for five minutes. This setting applies to connections between the proxy and the back-end database.

Note the following:
+ This setting limits the number of idle connections in the pool, but doesn't force the proxy to retain a given number of idle connections. If the client activity is very low, the actual number of back-end database connections can be lower than `MaxIdleConnectionsPercent`.
+ Connections count as idle when they are available for reuse in the proxy's connection pool. Pinned connections are not available for reuse by other clients, and therefore don't count as idle for the purposes of enforcing `MaxIdleConnectionsPercent`. For more information about pinning, see [Avoiding pinning an RDS Proxy](rds-proxy-pinning.md).
+ The number of idle connections reported by database metadata is typically higher than the number of idle connections recorded by RDS Proxy metrics. This can be due to direct client connections bypassing the proxy as well as internal connections used by Amazon RDS and Aurora automation.

**Note**  
The connection idle time observed and enforced at the proxy layer might be different than the idle time reported by database tools such as the MySQL process list or the activity statistics tables in PostgreSQL. RDS Proxy pings back-end connections occasionally, which resets the database idle timers even though the connection remains idle in terms of client activity.

Best practices:

The default setting of 50 is suitable and recommended for most workloads. Changing the setting has the following effect:
+ When you raise `MaxIdleConnectionsPercent`, the database observes a larger number of idle connections which can increase database resource consumption outside of peak hours. On the other hand, connection spikes handled through the proxy experience lower borrow latency because there are more connections readily available in the pool.
+ When you lower `MaxIdleConnectionsPercent`, the proxy closes idle connections more aggressively, potentially reducing the contention and resource consumption caused by those connections. However, connection spikes passing through the proxy might experience longer borrow times. As there are fewer connections available in the pool, the proxy needs to spend additional time opening new back-end connections during a spike.

Resource consumption by idle connections might not be a material concern in databases using provisioned instance types, but Aurora databases using the Serverless v2 instance type might prefer to optimize idle resource consumption to reduce cost.

### IdleClientTimeout
<a name="rds-proxy-best-practices.configuration.idleclienttimeout"></a>


| Minimum value | Maximum value | Default value | 
| --- | --- | --- | 
| 1 minute | 8 hours | 30 minutes | 

For more information, see [IdleClientTimeout](rds-proxy-connections.md#rds-proxy-connection-pooling-tuning.idleclienttimeout).

This setting determines how long a client connection can remain idle before the proxy closes it. Note that RDS Proxy enforces a maximum connection lifetime of 24 hours, regardless of whether the connection is idle. For example, if you configure `IdleClientTimeout` to 30 minutes (default) and ping the database every minute, the connection never exceeds the idle timeout, but it doesn't remain open indefinitely. RDS Proxy closes the connection after 24 hours even if it doesn't qualify as idle.

The `IdleClientTimeout` setting applies to the connection between a client (applications or interactive users) and RDS Proxy. To understand idle behavior of back-end connections between RDS Proxy and the database, see [MaxIdleConnectionsPercent](#rds-proxy-best-practices.configuration.maxidleconnectionspercent).

Best practices:
+ The idle timeout must be long enough to accommodate normal pauses in SQL activity inside of a client connection or transaction. It must not be so long as to allow a client to hold on to resources that it reasonably no longer needs, but that might be needed by other clients. This is particularly important if you observe connection pinning because a connection pinned by one client can't be reused by other clients.
+ For RDS Proxy to correctly enforce the timeout, the client connection must be truly idle without sending any queries (even simple health checks such as `SELECT 1;`) or protocol pings (such as `COM_PING` in MySQL). If you observe connections not being closed despite exceeding the timeout, check the connection logic of your application drivers. Application-level connection pools are particularly likely to perform their own liveness checks interfering with `IdleClientTimeout`.

### ConnectionBorrowTimeout
<a name="rds-proxy-best-practices.configuration.connectionborrowtimeout"></a>


| Minimum value | Maximum value | Default value | 
| --- | --- | --- | 
| (zero) | 5 minutes | 2 minutes | 

For more information, see [ConnectionBorrowTimeout](rds-proxy-connections.md#rds-proxy-connection-pooling-tuning.connectionborrowtimeout).

When a client connects to RDS Proxy, the proxy must either borrow an existing available connection from the pool or open a new database connection. This setting defines how long RDS Proxy waits for a connection to be borrowed or opened before returning an error.

Note the following:
+ A `ConnectionBorrowTimeout` of zero results in timeout errors when the connection pool doesn't already contain an available connection. This is true even if the pool is below maximum capacity and could open a new back-end connection.
+ Even with `MaxIdleConnectionsPercent` equal to `MaxConnectionsPercent`, the actual number of connections in the pool can be lower than the configured maximum. In other words, `MaxIdleConnectionsPercent` limits the amount of idle connections but doesn't force connections to remain open.

It is normal for a connection pool to run below maximum capacity. In this situation, using a `ConnectionBorrowTimeout` setting of zero can prevent the pool from growing because the pool isn't allowed to wait for a new connection to be opened. As a result, you should use non-zero `ConnectionBorrowTimeout` values for all workloads unless the previously described behavior is preferred.

**Note**  
This setting also applies when the database is not ready to accept connections, such as during offline maintenance operations and failovers. The logic for enforcing the `ConnectionBorrowTimeout` is the same whether the database is up or down.

### Initialization queries and pinning filters
<a name="rds-proxy-best-practices.configuration.pinning-filters"></a>

RDS Proxy supports additional features that can reduce connection pinning and improve multiplexing efficiency as a result.

An **initialization query** is one or more statements run each time the proxy sets up a new back-end database connection. If your clients use identical statements to set up session parameters, you can move those statements to the proxy's initialization query. This helps reduce the probability of pinning and it also improves efficiency: a particular back-end database connection runs its initialization query once during setup but it might be reused later by many clients. Keep in mind that putting SQL statements in the initialization query does not filter them out from client traffic. You still need to remove those statements from the application code so that they don't interfere with multiplexing.

**Session pinning filters** are a configuration property that prevents the proxy from pinning certain session states. The only filter option currently available, `EXCLUDE_VARIABLE_SETS`, instructs the proxy to ignore all `SET` statements when determining whether a session should be pinned. The `SET` statements are still passed on to the database and can affect session state, which means this option is only safe in the following situations:

1. The `SET` statements are no-ops, such as setting a system variable to a value identical with the server default.

1. The `SET` statements and subsequent queries are part of the same transaction, and every transaction sets up its own state fully independently so that it's not affected by variables set by other transactions.

**Note**  
The `EXCLUDE_VARIABLE_SETS` pinning filter is an all-or-nothing setting and you cannot selectively choose which `SET` statements to ignore. Do not use this filter as a blanket solution for pinning unless your use case falls under one of the categories discussed in the preceding list.

For best results, remove unnecessary statements from application code where possible, and only using filters if application modifications are not possible. This promotes a less noisy and more predictable client-server environment as opposed to applying special treatment to statements that aren't needed in the first place.

**Important**  
Neither initialization queries nor pinning filters cause RDS Proxy to alter the client-server query traffic. Statements arriving from the clients are still passed on to the database regardless of the init query or pinning filter configuration.

For more information, see:
+ [Creating a proxy](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-creating.html) and [Modifying a proxy](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-modifying-proxy.html) for Amazon RDS.
+ [Creating a proxy](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-proxy-creating.html) and [Modifying a proxy](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-proxy-modifying-proxy.html) for Amazon Aurora.

For PostgreSQL connections, you can also put supported connection parameters in the startup message exchanged between the client driver and the proxy. This avoids sending separate `SET` commands, both reducing round-trips and avoiding connection pinning caused by explicit `SET` statements. For more information, see [Considerations for connecting to PostgreSQL](rds-proxy-connecting.md#rds-proxy-connecting-postgresql).

## Aligning application, proxy, and database configuration
<a name="rds-proxy-best-practices.configuration.alignment"></a>

As discussed in the preceding section, RDS Proxy supports a range of parameters to help you align the proxy behavior with your application needs. However, choosing the right configuration values is a task that cuts across all layers of the stack: the application, the proxy, and the database itself. The settings of all those components must be aligned with the following goals in mind:

1. Provide the expected level of performance and scalability during normal operations.

1. Promote clarity and ease of troubleshooting during workload issues.

1. Help the stack deal with unexpected events (such as workload surges) with minimal impact to the application.

When choosing and tuning settings in a multi-layered environment, try to align configuration values such that the limits and timeouts at a lower layer are equal to or higher than the corresponding limits and timeouts at a higher layer. In other words, treat settings from one layer as an envelope that fits into the next configuration envelope further down the stack.

For example, assume that your application is the top layer, the proxy is a middle layer, and the database is the lower layer. If the timeouts and limits at the proxy level are lower than the limits at the application level, proxy limits preempt application limits. The application is unable to exercise its settings and it experiences behaviors that can't be explained by its own configuration.

Consider the `IdleClientTimeout` proxy setting as an example. If your application drivers or client pools enforce their own idle timeouts, the proxy's idle timeout is a safety net on top of the application settings. This means the `IdleClientTimeout` must be at least equal to any application-level idle timeouts to prevent confusion:
+ When the application idle timeout is lower than the proxy timeout, you expect the application to close its connections as configured. If the application fails to close idle connections in a timely manner, the proxy acts as a backstop.
+ When the application idle timeout is longer than the proxy timeout, the application might experience connection closures that are considered premature. This can lead to confusion on the application side.

The same logic applies to other settings such as connection limits: each layer's settings should fit inside of the envelope defined by the next layer's configuration.

For best results, configuration settings should include some padding between one layer and the next. For example, you can make the proxy timeout a few seconds longer than the application timeout to avoid sporadic errors due to client/server clock drift, or in case the client needs additional time to gracefully close the connection.

In other words, align your settings like this:

`client timeout < proxy timeout < database timeout`

Instead of doing this:

`client timeout = proxy timeout = database timeout`

And avoid this:

`client timeout > proxy timeout > database timeout`

## Database configuration
<a name="rds-proxy-best-practices.configuration.alignment.database"></a>

### Connection limits
<a name="rds-proxy-database-connection-limits"></a>

RDS Proxy uses the `MaxConnectionsPercent` setting to determine the maximum size of its connection pool, which means the proxy's connection pool size is relative to the database's connection limit. When you change the database's connection limit, the proxy's pool size follows automatically. If you want the database to reserve a portion of connection limit for non-proxy users, you should do that by lowering the `MaxConnectionsPercent` setting in the proxy rather than by increasing the database limit.

RDS Proxy doesn't eliminate the need for proper configuration of database connection limits. A single proxy connection isn't inherently lighter than a single direct client connection, so don't increase database limits solely because you're using a proxy. A proxy doesn't reduce the amount of work the database must perform to handle queries, but it helps the database handle the same workload using fewer connections.

### Idle timeouts
<a name="rds-proxy-database-idle-timeouts"></a>

Databases can enforce their own idle timeouts, for example, using the `wait_timeout` and `interactive_timeout` settings in MySQL or the `transaction_timeout` and `idle_in_transaction_session_timeout` settings in PostgreSQL. Default values for those settings are unlikely to interfere with proxy configuration, but if you use custom database-level timeouts, make sure they're at least as long as the corresponding proxy timeouts or otherwise the proxy experiences connection errors due to premature timeouts.

The same logic applies to database environments using connection killers, which are scripts or processes that monitor session state and actively terminate connections based on certain criteria. If your environment uses such techniques, ensure that the connection termination logic aligns with proxy settings.

Databases that handle all their workload through the proxy can typically depend on the proxy configuration for idle timeouts, and leave the database-level settings at their default values.

## Application configuration
<a name="rds-proxy-best-practices.configuration.alignment.application"></a>

### Managing session state
<a name="rds-proxy-managing-session-state"></a>

Many database drivers, application frameworks, and object-relational mapping (ORM) tools use session variables or `SET` statements to set up connections before sending query traffic. The use of connection and transaction initialization statements might not be obvious when looking at the application code alone, and there can be several layers of abstraction between the database itself and the SQL statements and application logic. You can use the RDS Proxy enhanced logging feature to record reasons for connection pinning, and database query logs can provide further information about all statements sent over your database connections.

Consider the following best practices:

1. Set connection parameters only when they're different from database defaults and the client session must deviate from those defaults. Removing unnecessary initialization statements not only helps with multiplexing, but it also reduces the number of client-server round trips for each new database connection.

1. Set variables and configuration settings consistently across all connections.

1. Avoid session configuration that can also be applied at query runtime. For example, if different clients need to see data in different time zones, consider using time zone conversion functions at the query level instead of setting the time zone at the session level.

1. If possible, move session configuration statements to the proxy layer using the initialization query feature. For more details, see [Initialization queries and pinning filters](#rds-proxy-best-practices.configuration.pinning-filters).

### Liveness checks
<a name="rds-proxy-best-practices.configuration.alignment.healthchecks"></a>

If your application uses connection pooling or advanced drivers, look for configuration related to liveness checks such as protocol pings, health check statements, or keep-alive queries. RDS Proxy treats all client requests equally, so even though a `SELECT 1;` query or a `COM_PING` request is a no-op from the application perspective, it prevents the proxy from enforcing idle client timeouts and managing the connection pool size according to `MaxIdleConnectionsPercent`.

**Note**  
RDS Proxy enforces a maximum connection lifetime of 24 hours regardless of the activity on the connection.

In most cases, it might be appropriate to disable client-side liveness checks to reduce protocol noise and help RDS Proxy manage idle connections. There are edge cases when you might want to run those health checks regardless:
+ You deliberately want to prevent certain connections from timing out in the proxy layer.
+ You want to allow the application driver or pool to proactively detect when a connection is dropped by the proxy. For example, pinned back-end connections might be closed due to a database restart and client connections might exceed the 24 hour maximum lifetime.

Consider disabling liveness checks on the application side, or only perform them for the specific connections that you want to keep from timing out.

### Session state tracking
<a name="rds-proxy-best-practices.configuration.alignment.statetracking"></a>

Some MySQL database drivers, such as the MariaDB driver, use `session_track_*` variables to enable tracking of session state. With this feature enabled, whenever the client makes a session state change that the server can track, the server includes the state change information in its response packets. This allows the driver to be advised about session state by the server.

This manner of session state tracking can be meaningful when the client interacts with the server directly and implements its own session management features, such as session migration in multi-server environments. RDS Proxy implements its own state tracking mechanisms and doesn't use the information enabled by `session_track_*` variables, however setting those variables causes session pinning.

If your database driver sets those variables, you can look for ways to disable the tracking functionality in the driver, switch to a different driver, or use session pinning filters to ignore the statements if it's safe to do so. For more details, see [Initialization queries and pinning filters](#rds-proxy-best-practices.configuration.pinning-filters).