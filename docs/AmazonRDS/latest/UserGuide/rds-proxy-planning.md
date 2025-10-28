# Planning where to use RDS Proxy

You can determine which of your DB instances, clusters, and applications might benefit the most from using
RDS Proxy. To do so, consider these factors:

- Any DB instance
  that encounters "too many connections" errors is a good candidate
  for associating with a proxy. This is often characterized by a high value of the
  `ConnectionAttempts` CloudWatch metric. The proxy enables applications to open many client connections, while the
  proxy manages a smaller number of long-lived connections to the DB instance
  .
- For DB instances that use smaller AWS instance classes, such as T2 or T3, using a proxy can
  help avoid out-of-memory conditions. It can also help reduce the CPU overhead for establishing
  connections. These conditions can occur when dealing with large numbers of connections.
- You can monitor certain Amazon CloudWatch metrics to determine whether a DB instance is approaching
  certain types of limit. These limits are for the number of connections and the memory associated with
  connection management. You can also monitor certain CloudWatch metrics to determine whether a DB instance
  is handling many short-lived connections. Opening and closing such connections can impose
  performance overhead on your database. For information about the metrics to monitor, see
  [Monitoring RDS Proxy metrics with Amazon CloudWatch](rds-proxy.md "rds-proxy.md").
- AWS Lambda functions can also be good candidates for using a proxy. These functions make frequent short
  database connections that benefit from connection pooling offered by RDS Proxy. You can take advantage of
  any IAM authentication you already have for Lambda functions, instead of managing database credentials in
  your Lambda application code.
- Applications that typically open and close large numbers of database
  connections and don't have built-in connection pooling mechanisms are good
  candidates for using a proxy.
- Applications that keep a large number of connections open for long periods are typically good candidates
  for using a proxy. Applications in industries such as software as a service (SaaS) or ecommerce often
  minimize the latency for database requests by leaving connections open. With RDS Proxy, an application can
  keep more connections open than it can when connecting directly to the DB
  instance.
- You might not have adopted IAM authentication and Secrets Manager due to the complexity of setting up such
  authentication for all DB instances
  . The proxy can enforce the authentication policies for client
  connections for particular applications. You can take advantage of any IAM
  authentication you already have for Lambda functions, instead of managing database credentials in your
  Lambda application code.
- RDS Proxy can help make applications more resilient and transparent to database failures. RDS Proxy bypasses Domain Name System (DNS) caches
  to reduce failover times by up to 66% for Amazon RDS Multi-AZ DB instances.
  RDS Proxy also automatically routes traffic to a new database instance while preserving application connections. This makes failovers more transparent
  for applications.
