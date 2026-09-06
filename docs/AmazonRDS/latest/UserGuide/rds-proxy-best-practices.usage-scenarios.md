

# Common usage scenarios
<a name="rds-proxy-best-practices.usage-scenarios"></a>

**Topics**
+ [Application scalability](#rds-proxy-best-practices.application-scalability)
+ [High availability](#rds-proxy-best-practices.high-availability)
+ [Using multiple proxies with one target](#rds-proxy-best-practices.multiple-proxies)

## Application scalability
<a name="rds-proxy-best-practices.application-scalability"></a>

### Connection handling in serverless and event-driven applications
<a name="rds-proxy-best-practices.serverless-connections"></a>

Serverless and event-driven applications, such as APIs and web services backed by AWS Lambda, must often support a large number of short-lived client requests. This usage pattern can cause connection churn on the database side with no possibility to implement connection pooling on the application side. Database performance could become degraded due to the number of concurrent connections alone, or the database might exceed its connection limit leading to client-facing errors.

In these scenarios, RDS Proxy can bring the following benefits:

1. It offloads the cost of establishing connections from the database to the proxy, and provides connection pooling and multiplexing to translate a large number of client connections to a much smaller number of back-end database connections. This helps reduce connection overhead and database contention, particularly in database engines such as PostgreSQL where the cost of establishing and maintaining connections is relatively high.

1. It can handle connection surges more gracefully. For example, when a database exceeds its connection limit, it immediately returns an error to the client. When RDS Proxy needs to borrow a connection from the pool but the pool is already at capacity, the proxy can wait for a connection to become available. This capability can improve client experience by turning hard errors into a slight increase in query latency.

1. With the configurable connection pool size, you can also use RDS Proxy as a throttling or load shedding mechanism. If the number of connections exceeds the limits you specify, RDS Proxy waits for a connection to become available within a configurable timeout. This can be useful in cases where the database serves multiple workloads, and you want to limit the amount of pressure a particular workload can create on the database.

### Connection handling in container-based distributed applications
<a name="rds-proxy-best-practices.container-connections"></a>

A container-based distributed application architecture may have hundreds or even thousands of containers, each running a copy of the application code. Even if the individual containers are capable of connection pooling, those pools are container-specific and therefore very small. The number of containers multiplied by the size of each container mini-pool can potentially exceed connection limits on your Amazon RDS or Aurora databases.

In this situation, RDS Proxy's ability to perform connection pooling (reusing connections) and multiplexing (serving multiple clients using one back-end connection) is most valuable. You can still use connection pooling inside each container to reduce churn between the application threads and RDS Proxy, but the proxy can help bring the number of back-end database connections down to a manageable level.

### Improving read replica utilization
<a name="rds-proxy-best-practices.replica-utilization"></a>

Read-heavy databases may require multiple read replicas to support read-only traffic. Applications can use their own logic for choosing which replica to connect to or, more commonly, they use a DNS-based round-robin mechanism such as the Aurora cluster reader endpoint. However, a DNS-based approach can lead to uneven replica utilization as a result of DNS caching. For example, clients could "pin" themselves to a particular replica, they could fail to recognize new replicas being added to the cluster, or they might try connecting to replicas that no longer exist.

When you use an RDS Proxy read-only endpoint, the proxy routes client connections between all available replicas using a "least outstanding connections" logic. RDS Proxy does not load-balance traffic based on database metrics such as CPU utilization, but it attempts to equalize the number of client connections on each replica, weighted by the database's connection limit. For example, if you have three Aurora replicas running with a `max_connections` setting of 500, 500, and 1000 (respectively), the proxy tries to send roughly twice the number of connections to the third replica versus to the other two.

You can use RDS Proxy reader endpoints with Aurora clusters or Amazon RDS Multi-AZ DB cluster deployments with two readable standbys. Proxy reader endpoints aren't supported for Amazon RDS DB instance deployments with read replicas.

### Improving connection efficiency
<a name="rds-proxy-best-practices.connection-efficiency"></a>

When introducing a proxy between client applications and the database, your goal is typically to increase the efficiency of connection handling while also considering the latency cost of an additional network hop through the proxy. An additional intermediate layer can seem counterintuitive for improving connection efficiency because any connection that would have been opened directly against the database is now opened against the proxy. The protocol handshake steps are the same in both cases, so if you're still spending resources on connection handshakes, it might not be obvious where the efficiency improvements come from.

The proxy doesn't necessarily make connections cheaper to establish. Instead, it moves most of the burden of handshake handling from the database layer to the proxy layer. When you pay for database resources, you want those resources to be spent on database work and not on auxiliary overhead. This becomes particularly important when using encrypted connections: although the overhead of transmitting encrypted data over an existing connection is not significant, the initial overhead of setting up an encrypted connection is substantial. In environments that churn through hundreds or thousands of connections per second, that extra effort can quickly add up. You might not want to spend that CPU time on (relatively expensive) database resources and instead offload them to (comparatively cheap) proxy layer.

Regarding the latency introduced by an additional network hop, the degree to which it matters depends on how "chatty" your application is and how many statements it runs per each "conversation" with the database. In RDS Proxy, you typically observe added latency in the low single-digit milliseconds, but it won't necessarily cause a visible impact on your applications. For example:
+ A workload where query execution times are in the order of tens or hundreds of milliseconds (or more) is unlikely to notice the proxy overhead because it's a small fraction of the total query time.
+ An application that runs single-digit millisecond or sub-millisecond queries can notice a difference because the query overhead (one additional network hop per query) is substantial compared to the query execution time. This might not be an issue if a client session only involves a handful of queries, so that the cumulative overhead is still small.

If the added latency in your situation is both noticeable and undesirable, you must weigh it against the other benefits of using a proxy (pooling, multiplexing, failover handling).

## High availability
<a name="rds-proxy-best-practices.high-availability"></a>

Multi-AZ databases running on Amazon RDS and Aurora (excluding Aurora DSQL) use failover mechanisms to restore availability in case of issues with the primary database instance. Failovers are also used as part of operational workflows, such as compute scaling for the primary instance. A failover involves a DNS change that moves the primary (read/write-capable) database endpoint from the previous primary instance to the newly promoted one. This DNS change must be observed and recognized by client applications, so that the clients can follow the primary without delay.

Some applications can struggle with the timely recognition of DNS changes as a result of DNS caching in the operating system or at the application level. While it's a best practice to address DNS caching issues at the application level, it's not always feasible due to application complexity or the cost of introducing changes.

In this scenario, RDS Proxy is an effective way to avoid DNS-related failover delays. The read/write endpoints and the optional read-only endpoints provided by RDS Proxy are "stable" in the sense that the IP addresses behind those endpoints don't change when database instances exchange their roles. RDS Proxy continuously tracks the topology of the back-end database and abstracts instance role changes from the clients.

There are alternative ways of handling DNS caching issues, such as by using advanced drivers directly capable of detecting the database topology without relying on DNS. However, it might be easier to deploy a single proxy in front of the database instead of introducing code changes and new drivers at the application level.

### Read availability
<a name="rds-proxy-best-practices.read-availability"></a>

In addition to improving client experience during database failovers, RDS Proxy also helps with application availability in case of read replica issues. It does so in two ways:

1. If a read replica becomes unavailable, but there are other replicas available in the cluster, the proxy can route new connections to the available replicas. The clients don't need to worry about DNS propagation delays or DNS caching.

1. For an existing client connection that is multiplexed, the proxy can send subsequent queries from that connection to a different replica that's available. In this situation, the client might not even notice that a back-end replica experienced an issue. When using this technique, RDS Proxy ensures that the new replica isn't behind the previous one in terms of replication lag. That way, subsequent queries sent by the client won't see data that could be considered stale.

## Using multiple proxies with one target
<a name="rds-proxy-best-practices.multiple-proxies"></a>

As a best practice, use one RDS Proxy per database target such as an Amazon RDS instance or an Aurora cluster. This works well in most scenarios, it keeps the configuration simple, and it makes the client experience more predictable. By comparison, using multiple proxies requires you to carefully align the configuration across all proxies to avoid unexpected behavior. For example, you must ensure that the combined size of all proxy pools doesn't exceed the connection limits of the single database target.

You might still explore the idea of using multiple proxies in certain situations. The following sections discuss the most common scenarios and outline the pros and cons of a single proxy versus a multi-proxy approach.

### Proxy availability
<a name="rds-proxy-best-practices.proxy-availability"></a>

The RDS Proxy infrastructure is highly available and deployed over multiple Availability Zones (AZs) by design. The proxy capacity is distributed across many nodes with continuous health monitoring, and it is automatically adjusted based on the provisioned instance size or the Serverless v2 maximum ACU settings of your database. As a result of the proxy's distributed Multi-AZ design, you don't need to run multiple proxies in front of your Amazon RDS or Aurora clusters for the purpose of high availability.

In fact, using multiple proxies in front of a single database target means that the application stack is now responsible for detecting and reacting to issues instead of relying on the robust mechanisms built into the proxy. Consequently, using multiple proxies for high availability reasons is strongly discouraged as it's likely to introduce more issues than it can solve.

### Handling multiple client pools
<a name="rds-proxy-best-practices.multiple-client-pools"></a>

Each proxy provides one read/write endpoint and (optionally) additional read/write or read-only endpoints. When a single proxy is used to handle multiple groups of clients or multiple workloads, those workloads can potentially interfere. For example, one workload can monopolize the connection pool to the point where there aren't enough free connections left to handle other workloads. Using separate proxies to isolate workloads could be a compelling solution, but you can consider other options first:
+ The database itself might provide simpler alternatives to running multiple proxies. For example, if the issue is caused by certain users monopolizing the pool, you could use the database's permission system to limit the number of concurrent connections those users are allowed to open.
+ Similarly, database-level query timeouts and idle timeouts can address issues with orphaned connections or runaway queries.
+ If the issue is caused by query or transaction duration or per-query resource consumption rather than the number of concurrent connections, using additional proxies won't help because the proxy doesn't impose limits on query or transaction weight. If the issue can't be addressed at the source, you can use the database's event scheduler to run code that detects and terminates client activity based on arbitrary conditions instead of moving those problematic clients to a separate proxy.

If you decide to use multiple proxies in front of the same target, ensure that the total size of all connection pools doesn't exceed the capabilities of the target database. For example, the sum of `MaxConnectionsPercent` across all proxies must be less than 100, otherwise the proxies may try to open more connections than the database is configured to handle.

Each proxy is billed separately, and the billing rate depends on the size of underlying database resources and not the workload activity. Consider the cost of running multiple proxies versus the cost of implementing alternative solutions, if any exist.

### Controlling read and write pools independently
<a name="rds-proxy-best-practices.independent-rw-pools"></a>

Each proxy provides one read/write endpoint and (optionally) additional read/write or read-only endpoints, but the limits and timeouts are configured for the entire proxy target and not individually for each proxy endpoint.

For example, you might have an Aurora cluster handling a large volume of read-only queries using multiple read replicas and the proxy's reader endpoint, but you want to limit the number of read/write connections to reduce resource pressure on the single writer. Since the `MaxConnectionsPercent` setting is defined for the entire proxy target (cluster), you can't limit the number of connections against the read/write endpoint without also affecting the limits of the read-only endpoint.

There are multiple ways to approach this challenge:

You can launch additional read replicas in the cluster and proportionally reduce the proxy's `MaxConnectionsPercent` setting. This preserves the total size of the read-only connection pool while reducing the maximum number of connections allowed on the writer. However, it also increases the cluster cost and it's progressively less effective the more replicas you have.

You could use instance-level parameter groups to configure database connection limits (such as `max_connections` in Aurora MySQL or PostgreSQL) for the read replicas separately from the writer. However, you must avoid using asymmetric parameter configuration because replicas can be promoted to a writer role during a failover, so the initial parameter differentiation won't be permanent. You might think of changing instance-level failover priority settings to influence which replicas are selected for promotion during failovers, and use that as a soft failover exclusion mechanism making the asymmetric configuration more predictable. However, failover priorities only serve as hints and are not a firm guarantee of failover behavior. Multi-instance configurations with asymmetric settings are therefore discouraged since they require continuous monitoring and can produce unexpected behavior if a failover lands on an instance that you didn't prefer.

In this scenario, using multiple proxies could be the cleanest way of managing read and write pools separately. You can create two proxies for the single database target, then configure applications to use the writer endpoint from the first proxy and the read-only endpoint from the second proxy. One proxy handles write workloads only, the other proxy handles read workloads only, and the `MaxConnectionsPercent` (as well as other settings) can be configured independently for each proxy. This solution involves an additional cost for running the second proxy, but it's simpler and more predictable than the preceding alternatives.