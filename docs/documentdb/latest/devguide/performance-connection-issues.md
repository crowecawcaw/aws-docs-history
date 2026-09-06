

# Connection issues with Amazon DocumentDB
<a name="performance-connection-issues"></a>

## Identification - Spot the problem
<a name="connection-identification"></a>

**Common Causes**

Connection problems typically stem from three main areas:

Connection pool exhaustion occurs when an application reaches its maximum allowed connections to Amazon DocumentDB, either through the client-side connection pool limits or server-side instance limits. This condition leads to degraded application performance, timeouts, and potential failures as new connection requests are either queued or rejected.

Authentication overload occurs when Amazon DocumentDB experiences excessive concurrent authentication requests, particularly when processing more than 1,000 new connections in a short time period. During authentication maintenance, Amazon DocumentDB holds an exclusive lock on the sessions map, causing subsequent authentication attempts to queue until maintenance completes.

Configuration issues in Amazon DocumentDB often stem from misconfigurations in networking, security, and client settings. This includes items such as incorrect security group settings, improper VPC configuration, or SSL/TLS certificate problems. Understanding proper configuration is essential for maintaining secure and reliable database access.

## Diagnose - Find root cause
<a name="connection-diagnose"></a>

**Connection pools**

The connection pool initializes when creating a MongoClient instance. Each pool maintains connections based on two key parameters:

minPoolSize - Minimum number of connections maintained

maxPoolSize - Maximum allowed connections

When a request needs a connection:

1. The pool checks for available idle connections

1. If none exist and pool size < maxPoolSize, it creates new connection

1. If at maxPoolSize, the request enters a wait queue

1. If the queue is full or timeout reached, it throws MongoWaitQueueFullException

The behavior of the wait queue is handled via these parameters:

waitQueueTimeoutMS - Maximum wait time for connection

waitQueueSize - Maximum queued requests

Here's an example of a problematic approach for connecting to Amazon DocumentDB where a new pool is created each time:

```
for(Request request : requests) {
    MongoClient client = MongoClients.create(settings);
    // Process request
    client.close();
}
```

Critical CloudWatch metrics to monitor are:
+ `DatabaseConnections` - The number of connections (active and idle) open on an instance taken at a 1-minute frequency.
+ `DatabaseConnectionsMax` - The maximum number of open database connections (active and idle) on an instance in a 1-minute period.
+ `DatabaseConnectionsLimit` - The maximum number of concurrent database connections (active and idle) allowed on an instance at any given time.
+ `LowMemNumOperationsThrottled` - The number of requests that are throttled due to low available memory in a 1-minute period.

For quotas per instance class, see [Instance quotas](limits.md#limits.instance).

Common warning signs of connection pool issues at the application level include:
+ Increasing connection acquisition times
+ Growing wait queue size
+ Rising number of timeout exceptions

**Authentication overload**

Connecting to Amazon DocumentDB follows a flow similar to below:

Connection Request → SSL Handshake → Authentication → Session Creation → Connection Ready

When processing >1,000 new connections, additional connection requests will enter a queue for Authentication after completing the SSL handshake. Average connection times from your application will increase during these overload events.

Critical CloudWatch metrics to monitor are:
+ `DatabaseConnections` - The number of connections (active and idle) open on an instance taken at a 1-minute frequency.
+ `DatabaseConnectionsMax` - The maximum number of open database connections (active and idle) on an instance in a 1-minute period.
+ `DatabaseConnectionsLimit` - The maximum number of concurrent database connections (active and idle) allowed on an instance at any given time.

**Configuration issues**

The most common configuration issue is caused when trying to connect to a private Amazon DocumentDB cluster endpoint from an environment without access to the private network environment. Amazon DocumentDB is virtual private cloud (VPC)-only and does not currently support public endpoints. You can't connect directly to your Amazon DocumentDB cluster from your laptop or local development environment outside of your VPC.

This will manifest in errors such as below:

```
Error: couldn't connect to server...
Failed to connect to...
exception: connect failed
connection attempt failed
```

Incorrect security group configurations can also cause connection failures. A Amazon DocumentDB cluster listens for connections on TCP port 27017 by default. Your application will fail if trying to connect to a port different from what the cluster was deployed with, or if the application is not covered in the ingress security group configuration for the cluster.

Incorrect certificate management can also lead to connection issues. By default, encryption in transit is enabled for newly created Amazon DocumentDB clusters. When encryption in transit is enabled, secure connections using TLS are required to connect to the cluster using the global-bundle.pem certificate. If you attempt to use the incorrect certificate, you will receive errors such as:

```
unable to get local issuer certificate
```

If attempting to connect to a cluster with TLS enabled without specifying the TLS parameters, you will receive errors such as:

```
Server selection timed out after 30000 ms
```

## Resolve - Fix the issue
<a name="connection-resolve"></a>

**Connection pools**: Review connection pooling by implementing or adjusting pool sizes to match workload requirements. Optimal pool configurations depend on your workload and requirements. You should keep a minPoolSize such that core connections are ready and available, and a maxWaitTime short enough to fail fast if the pool has been exhausted.

Here's an example of how to reuse a single pool without creating a new one each time:

```
MongoClient client = MongoClients.create(settings); 
    for(Request request : requests) { 
    // Process request
}
```

**Authentication overload**: Manage authentication by implementing gradual connection ramp-up and limiting new connections to 1,000 at a time. Use connection pooling to reuse authenticated connections effectively. To avoid overloading the Amazon DocumentDB cluster with connections, implement a connection ramp-up strategy.

```
public class ConnectionManager {
    private static final int BATCH_SIZE = 100;
    private static final int DELAY_MS = 1000;
    
    public void establishConnections(int totalRequired) {
        int established = 0;
        while (established < totalRequired) {
            int batch = Math.min(BATCH_SIZE, totalRequired - established);
            createConnections(batch);
            Thread.sleep(DELAY_MS);
            established += batch;
        }
    }
}
```

You can also configure your connection pool settings to limit the total number of allowed connections.

```
MongoClientSettings settings = MongoClientSettings.builder()
    .applyToConnectionPoolSettings(builder -> {
        builder.maxSize(500)                     // Limit total connections
               .minSize(10)                      // Maintain base connections
               .maxConnectionLifeTime(3600000)   // Rotate connections hourly
    })
    .applyToServerSettings(builder -> {
        builder.heartbeatFrequency(10000)        // Regular server checks
    })
    .build();
```

**Configuration issues**: Ensure your application has access to the private VPC and subnet where your Amazon DocumentDB resources are located. If using VPC Peering, check the developer guide Troubleshoot a VPC peering connection for more information. You can also review the Knowledge Center article [How do I troubleshoot connectivity issues from the internet to Amazon EC2 instances within my VPC?](https://repost.aws/knowledge-center/instance-vpc-troubleshoot).

For security group configuration, you must include an ingress rule in your Amazon DocumentDB security group to allow connections from your application.

```
{
  "SecurityGroupIngress": [
    {
      "IpProtocol": "tcp",
      "FromPort": 27017,
      "ToPort": 27017,
      "SourceSecurityGroupId": "<application-security-group>",
      "Description": "DocumentDB access from application tier"
    }
  ],
  "SecurityGroupEgress": [
    {
      "IpProtocol": "-1",
      "FromPort": -1,
      "ToPort": -1,
      "CidrIp": "0.0.0.0/0"
    }
  ]
}
```

If the cluster is configured with TLS encryption, download the TLS certificate for Amazon Amazon DocumentDB named global-bundle.pem and use it when connecting to the cluster.

```
wget https://truststore.pki.rds.amazonaws.com/global/global-bundle.pem
```

**Long-term Solutions**

Instance scaling may be necessary through upgrading to a larger instance class or adding read replicas to distribute connection load. Proper load balancing implementation ensures optimal resource utilization across the cluster.

Application changes should focus on implementing robust connection handling, comprehensive monitoring, and adherence to connection pooling best practices. This includes proper error handling and connection lifecycle management.

Architecture improvements might involve adopting Amazon DocumentDB Serverless for variable workloads, implementing sophisticated retry logic, and designing for fault tolerance. Consider restructuring application architecture to better handle connection management.

## Best practices
<a name="connection-best-practices"></a>

**Connection pools**

Through proper connection pool management and monitoring, applications can maintain stable database connectivity while preventing exhaustion scenarios that could impact system reliability and performance. Configure appropriate timeouts and size your pool based on your workload's characteristics.

Connection pool setting example

```
MongoClientSettings settings = MongoClientSettings.builder()
    .applyToConnectionPoolSettings(builder ->
        builder.maxSize(10))
    .applyToConnectionPoolSettings(builder ->
        builder.maxWaitQueueSize(2))
    .applyToConnectionPoolSettings(builder ->
        builder.maxConnectionIdleTime(10, TimeUnit.MINUTES))
    .build();
```

For more information, see [Building resilient applications with Amazon DocumentDB – Part 1: Client configuration](https://aws.amazon.com/blogs/database/building-resilient-applications-with-amazon-documentdb-with-mongodb-compatibility-part-1-client-configuration/).

**Authentication overload**

Always implement connection pooling with appropriate values for parameters based on your workload. Use a gradual connection establishment technique and maintain persistent connections, where possible. Implement proper connection cleanup to ensure no idle resources are wasted.

**Configuration issues**

Ensure you have configured appropriate routing from your application to the Amazon DocumentDB resources. Utilize TLS for encryption in transit and implement least privilege access. Verify your Amazon DocumentDB credentials and validate connection string values.