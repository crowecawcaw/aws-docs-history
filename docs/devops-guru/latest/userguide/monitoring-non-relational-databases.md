# Monitoring non-relational databases using DevOps Guru

DevOps Guru is capable of generating insights for your non-relational or NoSQL databases that help you keep your
resources configured according to best practices. For example, DevOps Guru can help you stay on top of capacity planning
by forecasting future needs based on existing traffic. DevOps Guru can identify if you are utilizing less resources than you configured and provide
recommendations to improve application availability based on your historic usage. This can help you reduce unnecessary cost.

Beyond capacity planning, DevOps Guru detects and helps you troubleshoot operational issues such as throttling, transaction conflicts,
conditional check failures, and areas for improvement in SDK parameters. Databases are typically connected with multiple services and resources,
and DevOps Guru can correlate your application structure for analysis using groups based on tagging or AWS CloudFormation aggregation.
Anomalies can involve multiple resources that are all affected by the same solution.
DevOps Guru is capable of correlating across different resource metrics, configurations, logs, and events.
For example, DevOps Guru can analyze and relate data from a Lambda function that might be reading or writing data from a Amazon DynamoDB table.
In this way, DevOps Guru monitors multiple related resources to detect anomalies and provide useful insights for your database solutions.

## Monitoring database operations in Amazon DynamoDB

The table below shows example scenarios and insights that DevOps Guru monitors for Amazon DynamoDB.

| Amazon DynamoDB use case                                                                                                                                                                        | Examples                                                                                                            | Metrics                                                                              |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| Detect when a large percentage of AccountProvisionedReadCapacityUtilization and AccountProvisionedWriteCapacityUtilization<br>are being used, due to a large number of read and write requests. | Amazon DynamoDB table consumption capacities for read or write requests is reaching table-level limits.             | AccountProvisionedReadCapacityUtilization,AccountProvisionedWriteCapacityUtilization |
| Detect conditional check failures in Amazon DynamoDB requests caused by a provided condition expression not matching what is expected in the database.                                          | Conditional check failures are caused by bad data in your table, a strict condition expression, or race conditions. | ConditionalCheckFailedRequests                                                       |

## Monitoring database operations in Amazon ElastiCache

The table below shows example scenarios and insights that DevOps Guru monitors for Amazon ElastiCache.

| Scenario that DevOps Guru identifies                                                                                                     | CloudWatch metrics monitored                    |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| Detect when an Amazon ElastiCache cluster is reaching its compute limit for Redis or Memcached due to changing demands on your clusters. | CPUUtilization, EngineCPUUtilization, Evictions |
