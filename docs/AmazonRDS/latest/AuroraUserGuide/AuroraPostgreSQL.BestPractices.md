

# Best practices with Amazon Aurora PostgreSQL
<a name="AuroraPostgreSQL.BestPractices"></a>

Following, you can find several best practices for managing your Amazon Aurora PostgreSQL DB cluster. Be sure to also review basic maintenance tasks. For more information, see [Performance and scaling for Amazon Aurora PostgreSQL](AuroraPostgreSQL.Managing.md). 

**Topics**
+ [Avoiding slow performance, automatic restart, and failover for Aurora PostgreSQL DB instances](#AuroraPostgreSQL.BestPractices.Avoiding)
+ [Diagnosing table and index bloat](AuroraPostgreSQL.diag-table-ind-bloat.md)
+ [Managing high object counts in Amazon Aurora PostgreSQL](PostgreSQL.HighObjectCount.md)
+ [Improved memory management in Aurora PostgreSQL](AuroraPostgreSQL.BestPractices.memory.management.md)
+ [Fast failover with Amazon Aurora PostgreSQL](AuroraPostgreSQL.BestPractices.FastFailover.md)
+ [Fast recovery after failover with cluster cache management for Aurora PostgreSQL](AuroraPostgreSQL.cluster-cache-mgmt.md)
+ [Managing Aurora PostgreSQL connection churn with pooling](AuroraPostgreSQL.BestPractices.connection_pooling.md)
+ [Dead connection handling in PostgreSQL](Appendix.PostgreSQL.CommonDBATasks.DeadConnectionHandling.md)
+ [Tuning memory parameters for Aurora PostgreSQL](AuroraPostgreSQL.BestPractices.Tuning-memory-parameters.md)
+ [Using Amazon CloudWatch metrics to analyze resource usage for Aurora PostgreSQL](AuroraPostgreSQL_AnayzeResourceUsage.md)
+ [Using logical replication to perform a major version upgrade for Aurora PostgreSQL](AuroraPostgreSQL.MajorVersionUpgrade.md)
+ [Managing custom casts in Aurora PostgreSQL](PostgreSQL.CustomCasts.md)
+ [Best Practices for Parallel Queries in Aurora PostgreSQL](PostgreSQL.ParallelQueries.md)
+ [Avoiding performance issues with REPLICA IDENTITY FULL in Aurora PostgreSQL](PostgreSQL.ReplicaIdentityFull.md)
+ [Initial troubleshooting for common PostgreSQL performance issues in Aurora PostgreSQL](PostgreSQL.InitialTroubleshooting.md)
+ [Troubleshooting storage issues in Aurora PostgreSQL](AuroraPostgreSQL.BestPractices.TroubleshootingStorage.md)

## Avoiding slow performance, automatic restart, and failover for Aurora PostgreSQL DB instances
<a name="AuroraPostgreSQL.BestPractices.Avoiding"></a>

If you're running a heavy workload or workloads that spike beyond the allocated resources of your DB instance, you can exhaust the resources on which you're running your application and Aurora database. To get metrics on your database instance such as CPU utilization, memory usage, and number of database connections used, you can refer to the metrics provided by Amazon CloudWatch, Performance Insights, and Enhanced Monitoring. For more information on monitoring your DB instance, see [Monitoring metrics in an Amazon Aurora cluster](MonitoringAurora.md).

If your workload exhausts the resources you're using, your DB instance might slow down, restart, or even fail over to another DB instance. To avoid this, monitor your resource utilization, examine the workload running on your DB instance, and make optimizations where necessary. If optimizations don't improve the instance metrics and mitigate the resource exhaustion, consider scaling up your DB instance before you reach its limits. For more information on available DB instance classes and their specifications, see [Amazon AuroraDB instance classes](Concepts.DBInstanceClass.md).