

# Application and workload considerations
<a name="rds-proxy-best-practices.workload-considerations"></a>

**Topics**
+ [Multi-tenant and multi-user environments](#rds-proxy-best-practices.multi-tenant)
+ [Databases serving multiple applications or software stacks](#rds-proxy-best-practices.multiple-applications)
+ [Using application-level pooling and advanced drivers with RDS Proxy](#rds-proxy-best-practices.application-pooling)

## Multi-tenant and multi-user environments
<a name="rds-proxy-best-practices.multi-tenant"></a>

 When it comes to scalability and improving connection management, the benefits of using RDS Proxy depend on its ability to perform connection pooling and, to a much greater extent, connection multiplexing. Connection pooling reduces the overhead associated with opening and closing connections. Connection multiplexing allows the proxy to reuse a back-end database connection after a transaction. For more information, see [RDS Proxy concepts and terminology](rds-proxy.howitworks.md). 

 When a connection can't be multiplexed, the proxy falls back to a behavior called *connection pinning*. Pinning is a situation where a client is forced to use the same underlying proxy connection for its entire session. The proxy connection is reserved for that one client, so it's not available for reuse by other clients. In other words, pinning creates an exclusive 1:1 association between a client-proxy connection and a proxy-database connection. Avoiding pinning is important in all scenarios where RDS Proxy is used mainly for scalability and efficiency reasons. For the most current pinning behavior, see [Avoiding pinning an RDS Proxy](rds-proxy-pinning.md). 

 As a general rule, connections can be multiplexed when they have identical state. Connections can't be multiplexed when they contain custom session-specific state information. One of the aspects defining session state is the database user name associated with a connection. When you connect to the proxy as "user\_A", the proxy needs to open a back-end database connection as "user\_A" as well. The proxy can potentially pool and reuse this back-end connection for other clients that log in as "user\_A", but not for clients using a different user name. 

 This behavior can significantly reduce pooling and multiplexing efficiency in multi-user environments with a large number of unique database accounts. This is particularly true in architectures using database-level or schema-level multi-tenancy. If the database contains a thousand schemas (one per tenant) and each tenant connects to the database with a different user name, the connection pool becomes fragmented into user-specific micro-pools, reducing overall efficiency. 

 Additionally, aspects specific to the database engine might further affect pooling efficiency and the proxy's ability to multiplex connections: 

1.  In Amazon RDS and Aurora PostgreSQL, multi-tenancy is often implemented by using one database per tenant. However, in PostgreSQL, connections are database-specific: a connection opened against one database can't access data from other databases. Therefore, database-level multi-tenancy reduces the efficiency of pooling and multiplexing at the proxy level. This consideration also applies if the workload uses schema-level multi-tenancy and client sessions use a custom `search_path`. However, if all sessions use the default search path and refer to tables using fully qualified names (`schema_name.table_name`), those sessions can be multiplexed. 

1.  In Amazon RDS and Aurora MySQL, the terms "database" and "schema" are synonyms. Multi-tenancy is often implemented by using one schema per tenant, which in MySQL is the same as one database per tenant. Connections are opened against a MySQL server as a whole and are not tied to a schema. If the application uses schema-level multi-tenancy, connection multiplexing is still possible for clients using the same database user name, even if those connections need to access data in different schemas. Multiplexing will be most effective if tenant separation is done at the application level instead of using different database accounts for each tenant. 

 In multi-schema environments, multiplexing efficiency depends on how you refer to table names: 
+  For clients that choose the current schema using session variables (`SET search_path ...` in PostgreSQL and `USE schema;` in MySQL) and then use unqualified table names in queries (such as `SELECT ... FROM table_name`), connection multiplexing only works between clients using the same schema or the same search path. 
+  For clients that don't modify session state to define the current schema, but instead use fully qualified table names in the SQL statements (such as `SELECT ... FROM schema_name.table_name`), multiplexing is not similarly constrained. 

## Databases serving multiple applications or software stacks
<a name="rds-proxy-best-practices.multiple-applications"></a>

 As discussed in the preceding section, certain connection state characteristics don't cause pinning, but still reduce the proxy's ability to reuse connections between different clients. When used with MySQL targets, RDS Proxy tracks a number of statements and session variables that configure session state, such as the character set, time zone, and collation settings. When a client uses tracked statements or variables to configure session settings, the proxy connection can only be reused for other clients that have the same values for those settings. 

 As a result, certain application and driver behaviors might reduce your ability to reuse connections inside of the proxy. For example, you might allow different applications to connect to the database using the same user name, assuming that the proxy can reuse and multiplex connections between those applications. However, if one application bootstraps connections with time zone A (`SET time_zone = ?`) and another application uses time zone B, connections are reusable within an application but not between applications. This leads to fragmentation of the connection pool, negatively affecting the effectiveness of pooling and multiplexing. 

 For more information, see [What RDS Proxy tracks for RDS for MariaDB and RDS for MySQL databases](rds-proxy-pinning.md#rds-proxy-pinning.mysql-tracked-vars). Session state tracking is not currently supported for database targets other than MySQL. 

 See [Configuration guidelines](rds-proxy-best-practices.configuration.md) for configuration guidelines and best practices for managing session state to avoid connection pinning. 

## Using application-level pooling and advanced drivers with RDS Proxy
<a name="rds-proxy-best-practices.application-pooling"></a>

 RDS Proxy helps improve scalability and connection efficiency in situations where the application itself is not using connection pooling. At the same time, many drivers and frameworks do include pooling features. You might also be using advanced wrappers or drivers that implement some of the proxy's features at the driver level. 

 Using application-level pooling and other connection handling improvements does not inherently conflict with using RDS Proxy, and doesn't negate its benefits. For example, you might be using connection pooling in your application containers, but the number of containers is large enough that you'd still run out of database connection limits without using a proxy. When using RDS Proxy with application-level pools and other connection-related features, review and understand the reasons for advanced connection-handling features to exist at the application level. Decide which of those features are worth keeping (or are harmless), and which can overlap or interfere with the proxy behavior. For example: 

1.  Pooling features built into drivers and frameworks can be useful even if they appear to overlap with the RDS Proxy functionality. If an application-level pool improves local connection efficiency on top of the benefits provided by the proxy, you can keep it. 

1.  Features related to failover handling might interfere with RDS Proxy logic or increase the overall stack complexity without providing benefits. For example, if your application is actively tracking the topology of your Aurora clusters to avoid DNS-related failover delays, it no longer needs to do so with RDS Proxy. Keeping this topology tracking logic might lead to undesirable behavior, such as the application threads bypassing the proxy and connecting directly to individual database instances. In this scenario, you can disable the application-level tracking logic and let RDS Proxy abstract the cluster topology for you. 

1.  Connection pooling libraries might use state management features that seem beneficial in theory, but interfere with proxy behavior. One such example is PostgreSQL libraries calling the `DISCARD ALL` query to reset connection state between borrows. It might seem that resetting connections should help with pooling and multiplexing, but it interferes with Amazon RDS Proxy's internal session state management. When using `DISCARD`, the proxy pins your client connection on release, reducing the multiplexing efficiency. 

 For any application-level connection handling components you do keep, ensure their configuration doesn't interfere with the connection handling logic used by Amazon RDS Proxy. For example: 
+  Align pool sizing across all layers of the stack. If the application-level pools are over-sized (or your proxy pool is under-sized), the application may try to open connections that the proxy isn't configured to handle. Those connections can experience delays at best and rejection errors at worst. 
+  Align timeout settings to reduce churn and avoid confusion around connection behavior. If the application pool keeps connections alive for 300 seconds, but the proxy is configured to close connections after 60 seconds, the application will see premature connection closures instead of the expected behavior. 

 Some of these architectural decisions and configuration choices might require testing and experimentation. It's not always possible to exactly predict application behavior in an environment with multiple layers of pooling and connection management. 

 Refer to [Configuration guidelines](rds-proxy-best-practices.configuration.md) for common configuration guidelines. 