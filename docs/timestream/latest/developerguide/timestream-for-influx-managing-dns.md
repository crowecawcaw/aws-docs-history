For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Managing DNS resolution for cluster endpoints

Timestream for InfluxDB for InfluxDB 3 multi-node clusters use DNS-based traffic distribution to balance connections across nodes. When a failover occurs or nodes are replaced, DNS records automatically update to point to available instances. To ensure your application can discover these changes and maintain optimal traffic distribution, proper DNS resolution configuration is essential.

## Understanding DNS caching

Many programming environments cache DNS lookups to improve performance. However, this caching can prevent your application from discovering updated IP addresses after failovers or from distributing connections across multiple cluster nodes. The impact varies by language and runtime:

- **Java/JVM-based applications** — The JVM caches DNS lookups for a configurable time-to-live (TTL). Some configurations cache indefinitely until the JVM restarts.
- **Other languages** — Python, Go, Node.js, and other runtimes typically rely on operating system DNS resolution and may not exhibit the same caching behavior.

## Solution 1: Configure JVM DNS TTL (Java applications)

For Java applications connecting to Timestream for InfluxDB for InfluxDB 3 cluster endpoints, set the JVM DNS cache TTL to **zero**. This ensures each connection triggers a fresh DNS lookup, enabling proper traffic distribution and immediate failover detection.

Check your current TTL setting:

```
String ttl = java.security.Security.getProperty("networkaddress.cache.ttl");
```

Configure the TTL using one of these methods:

- **Global configuration** — Set `networkaddress.cache.ttl` in `$JAVA_HOME/jre/lib/security/java.security`:

```
networkaddress.cache.ttl=0
```

- **Application-specific configuration** — Set the property in your application initialization code before establishing network connections:

```
java.security.Security.setProperty("networkaddress.cache.ttl", "0");
```

- **JVM argument** — Pass as a system property when starting your application:

```
java -Dsun.net.inetaddr.ttl=0 -jar your-application.jar
```

###### Note

For non-cluster endpoints or general AWS resources, a TTL of 60 seconds is typically sufficient. The zero TTL recommendation is specific to InfluxDB 3 cluster endpoints where traffic distribution and rapid failover detection are critical.

## Solution 2: Direct resolution via authoritative nameservers

If TTL configuration is insufficient — for example, due to intermediate OS-level caching, or if your programming language doesn't exhibit DNS caching issues — you can force fresh DNS resolution by querying authoritative nameservers directly. Use this approach only when standard TTL configuration doesn't resolve the issue.

###### Direct resolution workflow

1. Identify the authoritative nameserver for your cluster endpoint:

```
dig <cluster-endpoint> NS
```

In the `AUTHORITY SECTION` of the output, note the nameserver listed after `IN SOA`. For example: `ns-1458.awsdns-54.org`. 2. Query the authoritative nameserver directly to bypass caches:

```
dig @ns-1458.awsdns-54.org <cluster-endpoint>
```

This returns the current IP addresses for the endpoint, reflecting the actual DNS-based traffic distribution. 3. Use the resolved IP address(es) for your application connections. Repeat this resolution periodically or when connection errors occur to refresh addresses.

**Example:**

```
# Find authoritative nameserver
dig my-cluster.timestream-influxdb.us-east-1.amazonaws.com NS

# Resolve using authoritative nameserver
dig @ns-1458.awsdns-54.org my-cluster.timestream-influxdb.us-east-1.amazonaws.com

# Use returned IP addresses in your application
```

## Handling node IP changes

###### Important

Node IP addresses are **not static**. They change during failovers, node restarts, maintenance operations, and cluster scaling. Never cache resolved IP addresses indefinitely.

Implement these practices to handle IP changes:

- **Periodic re-resolution** — Re-resolve endpoints every 30-60 seconds using a background task. Compare new IP addresses against cached values and update your connection pool accordingly.
- **Error-driven re-resolution** — When a connection fails (timeout, connection refused, reset), immediately re-resolve the endpoint and retry with updated IP addresses.
- **Graceful connection draining** — When an IP address is no longer in the DNS record set, allow in-flight requests to complete but stop creating new connections to that IP.
- **New connection creation** — After re-resolution, create new connections using updated IP addresses. Existing connections pinned to old IPs won't benefit from re-resolution.

## Best practices

- **Start with TTL configuration** — For Java applications, always try setting `networkaddress.cache.ttl=0` first. This is the simplest and most effective solution.
- **Use direct resolution sparingly** — Only use authoritative nameserver queries when TTL configuration is insufficient or when dealing with persistent intermediate caching.
- **Automate nameserver discovery** — Don't hardcode nameserver addresses. Discover them dynamically as nameserver assignments can change.
- **Applies to cluster endpoints only** — These techniques are for cluster-level endpoints (write and read) that use DNS-based distribution. Node-specific endpoints that target individual nodes directly don't require this configuration.
- **Test your implementation** — Verify that your application correctly distributes connections across multiple nodes and recovers from simulated node failures.
