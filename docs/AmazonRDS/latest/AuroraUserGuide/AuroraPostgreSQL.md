# Best practices with

Amazon Aurora PostgreSQL

Following, you can find several best practices for managing your Amazon Aurora PostgreSQL DB
cluster. Be sure to also review basic maintenance tasks. For more information, see [Performance and scaling for
Amazon Aurora PostgreSQL](AuroraPostgreSQL.md "AuroraPostgreSQL.md").

###### Topics

- [Avoiding slow performance,
  automatic restart, and failover for Aurora PostgreSQL DB instances](#AuroraPostgreSQL.BestPractices.Avoiding "#AuroraPostgreSQL.BestPractices.Avoiding")
- [Diagnosing table and index bloat](AuroraPostgreSQL.md "AuroraPostgreSQL.md")
- [Improved memory
  management in Aurora PostgreSQL](AuroraPostgreSQL.BestPractices.memory.md "AuroraPostgreSQL.BestPractices.memory.md")
- [Fast failover with
  Amazon Aurora PostgreSQL](AuroraPostgreSQL.BestPractices.md "AuroraPostgreSQL.BestPractices.md")
- [Fast recovery after failover with
  cluster cache management for Aurora PostgreSQL](AuroraPostgreSQL.md "AuroraPostgreSQL.md")
- [Managing Aurora PostgreSQL connection churn with pooling](AuroraPostgreSQL.BestPractices.md "AuroraPostgreSQL.BestPractices.md")
- [Dead connection
  handling in PostgreSQL](Appendix.PostgreSQL.CommonDBATasks.md "Appendix.PostgreSQL.CommonDBATasks.md")
- [Tuning memory parameters for
  Aurora PostgreSQL](AuroraPostgreSQL.BestPractices.md "AuroraPostgreSQL.BestPractices.md")
- [Using Amazon CloudWatch metrics to analyze
  resource usage for Aurora PostgreSQL](AuroraPostgreSQL_AnayzeResourceUsage.md "AuroraPostgreSQL_AnayzeResourceUsage.md")
- [Using logical replication to perform a major version upgrade for Aurora PostgreSQL](AuroraPostgreSQL.md "AuroraPostgreSQL.md")
- [Troubleshooting
  storage issues in Aurora PostgreSQL](AuroraPostgreSQL.BestPractices.md "AuroraPostgreSQL.BestPractices.md")

## Avoiding slow performance,

automatic restart, and failover for Aurora PostgreSQL DB instances

If you're running a heavy workload or workloads that spike beyond the allocated
resources of your DB instance, you can exhaust the resources on which you're running
your application and Aurora database. To get metrics on your database instance such as
CPU utilization, memory usage, and number of database connections used, you can refer to
the metrics provided by Amazon CloudWatch, Performance Insights, and Enhanced Monitoring. For more information on monitoring
your DB instance, see [Monitoring metrics in an Amazon Aurora cluster](MonitoringAurora.md "MonitoringAurora.md").

If your workload exhausts the resources you're using, your DB instance might slow
down, restart, or even fail over to another DB instance. To avoid this, monitor your
resource utilization, examine the workload running on your DB instance, and make
optimizations where necessary. If optimizations don't improve the instance metrics and
mitigate the resource exhaustion, consider scaling up your DB instance before you reach
its limits. For more information on available DB instance classes and their
specifications, see [Amazon Aurora DB instance classes](Concepts.md "Concepts.md").
