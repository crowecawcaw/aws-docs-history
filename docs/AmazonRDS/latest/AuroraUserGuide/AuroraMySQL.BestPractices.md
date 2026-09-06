

# Best practices with Amazon Aurora MySQL
<a name="AuroraMySQL.BestPractices"></a><a name="best_practices"></a>

This topic includes information on best practices and options for using or migrating data to an Amazon Aurora MySQL DB cluster. The information in this topic summarizes and reiterates some of the guidelines and procedures that you can find in [Managing an Amazon Aurora DB cluster](CHAP_Aurora.md).

**Contents**
+ [Determining which DB instance you are connected to](#AuroraMySQL.BestPractices.DeterminePrimaryInstanceConnection)
+ [Best practices for Aurora MySQL performance and scaling](AuroraMySQL.BestPractices.Performance.md)
  + [Using T instance classes for development and testing](AuroraMySQL.BestPractices.Performance.md#AuroraMySQL.BestPractices.T2Medium)
  + [Optimizing Aurora MySQL indexed join queries with asynchronous key prefetch](AuroraMySQL.BestPractices.Performance.md#Aurora.BestPractices.AKP)
    + [Enabling asynchronous key prefetch](AuroraMySQL.BestPractices.Performance.md#Aurora.BestPractices.AKP.Enabling)
    + [Optimizing queries for asynchronous key prefetch](AuroraMySQL.BestPractices.Performance.md#Aurora.BestPractices.AKP.Optimizing)
  + [Optimizing large Aurora MySQL join queries with hash joins](AuroraMySQL.BestPractices.Performance.md#Aurora.BestPractices.HashJoin)
    + [Enabling hash joins](AuroraMySQL.BestPractices.Performance.md#Aurora.BestPractices.HashJoin.Enabling)
    + [Optimizing queries for hash joins](AuroraMySQL.BestPractices.Performance.md#Aurora.BestPractices.HashJoin.Optimizing)
  + [Using Amazon Aurora to scale reads for your MySQL database](AuroraMySQL.BestPractices.Performance.md#AuroraMySQL.BestPractices.ReadScaling)
  + [Optimizing timestamp operations](AuroraMySQL.BestPractices.Performance.md#AuroraMySQL.BestPractices.Performance.TimeZone)
  + [Virtual index ID overflow errors](AuroraMySQL.BestPractices.Performance.md#AuroraMySQL.BestPractices.Performance.VirtualIndexIDOverflow)
+ [Best practices for Aurora MySQL high availability](AuroraMySQL.BestPractices.HA.md)
  + [Using Amazon Aurora for Disaster Recovery with your MySQL databases](AuroraMySQL.BestPractices.HA.md#AuroraMySQL.BestPractices.DisasterRecovery)
  + [Migrating from MySQL to Amazon Aurora MySQL with reduced downtime](AuroraMySQL.BestPractices.HA.md#AuroraMySQL.BestPractices.Migrating)
  + [Avoiding slow performance, automatic restart, and failover for Aurora MySQL DB instances](AuroraMySQL.BestPractices.HA.md#AuroraMySQL.BestPractices.Avoiding)
+ [Recommendations for MySQL features in Aurora MySQL](AuroraMySQL.BestPractices.FeatureRecommendations.md)
  + [Using multithreaded replication in Aurora MySQL](AuroraMySQL.BestPractices.FeatureRecommendations.md#AuroraMySQL.BestPractices.MTReplica)
  + [Invoking AWS Lambda functions using native MySQL functions](AuroraMySQL.BestPractices.FeatureRecommendations.md#AuroraMySQL.BestPractices.Lambda)
  + [Avoiding XA transactions with Amazon Aurora MySQL](AuroraMySQL.BestPractices.FeatureRecommendations.md#AuroraMySQL.BestPractices.XA)
  + [Keeping foreign keys turned on during DML statements](AuroraMySQL.BestPractices.FeatureRecommendations.md#Aurora.BestPractices.ForeignKeys)
  + [Configuring how frequently the log buffer is flushed](AuroraMySQL.BestPractices.FeatureRecommendations.md#AuroraMySQL.BestPractices.Flush)
  + [Minimizing and troubleshooting Aurora MySQL deadlocks](AuroraMySQL.BestPractices.FeatureRecommendations.md#AuroraMySQL.BestPractices.deadlocks)
    + [Minimizing InnoDB deadlocks](AuroraMySQL.BestPractices.FeatureRecommendations.md#AuroraMySQL.BestPractices.deadlocks-minimize)
    + [Monitoring InnoDB deadlocks](AuroraMySQL.BestPractices.FeatureRecommendations.md#AuroraMySQL.BestPractices.deadlocks-monitor)
+ [Evaluating DB instance usage for Aurora MySQL with Amazon CloudWatch metrics](AuroraMySQL.BestPractices.CW.md)

## Determining which DB instance you are connected to
<a name="AuroraMySQL.BestPractices.DeterminePrimaryInstanceConnection"></a>

To determine which DB instance in an Aurora MySQL DB cluster a connection is connected to, check the `innodb_read_only` global variable, as shown in the following example.

```
SHOW GLOBAL VARIABLES LIKE 'innodb_read_only'; 
```

The `innodb_read_only` variable is set to `ON` if you are connected to a reader DB instance. This setting is `OFF` if you are connected to a writer DB instance, such as primary instance in a provisioned cluster.

This approach can be helpful if you want to add logic to your application code to balance the workload or to ensure that a write operation is using the correct connection.