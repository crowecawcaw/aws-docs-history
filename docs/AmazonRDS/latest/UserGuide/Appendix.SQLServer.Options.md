# Microsoft SQL Server resource governor with RDS for SQL Server

Resource governor is a SQL Server Enterprise Edition feature that gives you precise control over
your instance resources. It enables you to set specific limits on how workloads use CPU,
memory, and physical I/O resources. With resource governor, you can:

- Prevent resource monopolization in multi-tenant environments by managing how different workloads share instance resources
- Deliver predictable performance by setting specific resource limits and priorities for different users and applications
  You can enable resource governor on either an existing or new RDS for SQL Server DB instance.

Resource governor uses three fundamental concepts:

- **Resource pool** - A container that manages your instance physical resources (CPU, memory, and I/O).
  You get two built-in pools (internal and default) and you can create additional custom pools.
- **Workload group** - A container for database sessions with similar characteristics.
  Every workload group belongs to a resource pool. You get two built-in workload groups
  (internal and default) and you can create additional custom workload groups.
- **Classification** - The process that determines which workload
  group handles incoming sessions based on user name, application name, database name or host name.
  For additional details about resource governor functionality in SQL Server,
  see [Resource Governor](https://learn.microsoft.com/en-us/sql/relational-databases/resource-governor/resource-governor?view=sql-server-ver16 "https://learn.microsoft.com/en-us/sql/relational-databases/resource-governor/resource-governor?view=sql-server-ver16")
  in the Microsoft documentation.

###### Contents

- [Supported versions and Regions](Appendix.SQLServer.Options.md#ResourceGovernor.SupportedVersions "Appendix.SQLServer.Options.md#ResourceGovernor.SupportedVersions")
- [Limitations and recommendations](Appendix.SQLServer.Options.md#ResourceGovernor.Limitations "Appendix.SQLServer.Options.md#ResourceGovernor.Limitations")
- [Enabling Microsoft SQL Server resource governor for your RDS for SQL Server instance](ResourceGovernor.md "ResourceGovernor.md")
  - [Creating the option group for RESOURCE_GOVERNOR](ResourceGovernor.md#ResourceGovernor.OptionGroup "ResourceGovernor.md#ResourceGovernor.OptionGroup")
  - [Adding the RESOURCE_GOVERNOR option to the option group](ResourceGovernor.md#ResourceGovernor.Add "ResourceGovernor.md#ResourceGovernor.Add")
  - [Associating the option group with your DB instance](ResourceGovernor.md#ResourceGovernor.Apply "ResourceGovernor.md#ResourceGovernor.Apply")

- [Using Microsoft SQL Server resource governor for your RDS for SQL Server instance](ResourceGovernor.md "ResourceGovernor.md")
  - [Manage resource pool](ResourceGovernor.md#ResourceGovernor.ManageResourcePool "ResourceGovernor.md#ResourceGovernor.ManageResourcePool")
    - [Create resource Pool](ResourceGovernor.md#ResourceGovernor.CreateResourcePool "ResourceGovernor.md#ResourceGovernor.CreateResourcePool")
    - [Alter resource pool](ResourceGovernor.md#ResourceGovernor.AlterResourcePool "ResourceGovernor.md#ResourceGovernor.AlterResourcePool")
    - [Drop resource pool](ResourceGovernor.md#ResourceGovernor.DropResourcePool "ResourceGovernor.md#ResourceGovernor.DropResourcePool")

  - [Manage workload groups](ResourceGovernor.md#ResourceGovernor.ManageWorkloadGroups "ResourceGovernor.md#ResourceGovernor.ManageWorkloadGroups")
    - [Create workload group](ResourceGovernor.md#ResourceGovernor.CreateWorkloadGroup "ResourceGovernor.md#ResourceGovernor.CreateWorkloadGroup")
    - [Alter workload group](ResourceGovernor.md#ResourceGovernor.AlterWorkloadGroup "ResourceGovernor.md#ResourceGovernor.AlterWorkloadGroup")
    - [Drop workload group](ResourceGovernor.md#ResourceGovernor.DropWorkloadGroup "ResourceGovernor.md#ResourceGovernor.DropWorkloadGroup")

  - [Create and register classifier function](ResourceGovernor.md#ResourceGovernor.ClassifierFunction "ResourceGovernor.md#ResourceGovernor.ClassifierFunction")
  - [Drop classifier function](ResourceGovernor.md#ResourceGovernor.DropClassifier "ResourceGovernor.md#ResourceGovernor.DropClassifier")
  - [De-register classifier function](ResourceGovernor.md#ResourceGovernor.DeregisterClassifier "ResourceGovernor.md#ResourceGovernor.DeregisterClassifier")
  - [Reset statistics](ResourceGovernor.md#ResourceGovernor.ResetStats "ResourceGovernor.md#ResourceGovernor.ResetStats")
  - [Resource governor configuration changes](ResourceGovernor.md#ResourceGovernor.ConfigChanges "ResourceGovernor.md#ResourceGovernor.ConfigChanges")
  - [Bind TempDB to a resource pool](ResourceGovernor.md#ResourceGovernor.BindTempDB "ResourceGovernor.md#ResourceGovernor.BindTempDB")
  - [Unbind TempDB from a resource pool](ResourceGovernor.md#ResourceGovernor.UnbindTempDB "ResourceGovernor.md#ResourceGovernor.UnbindTempDB")
  - [Cleanup resource governor](ResourceGovernor.md#ResourceGovernor.Cleanup "ResourceGovernor.md#ResourceGovernor.Cleanup")

- [Considerations for Multi-AZ deployment](Appendix.SQLServer.Options.md#ResourceGovernor.Considerations "Appendix.SQLServer.Options.md#ResourceGovernor.Considerations")
- [Considerations for read replicas](Appendix.SQLServer.Options.md#ResourceGovernor.ReadReplica "Appendix.SQLServer.Options.md#ResourceGovernor.ReadReplica")
- [Monitor Microsoft SQL Server resource governor using system views for your RDS for SQL Server instance](ResourceGovernor.md "ResourceGovernor.md")
  - [Resource pool runtime statistics](ResourceGovernor.md#ResourceGovernor.ResourcePoolStats "ResourceGovernor.md#ResourceGovernor.ResourcePoolStats")

- [Disabling Microsoft SQL Server resource governor for your RDS for SQL Server instance](ResourceGovernor.md "ResourceGovernor.md")
- [Best practices for configuring resource governor on RDS for SQL Server](ResourceGovernor.md "ResourceGovernor.md")

## Supported versions and Regions

Resource governor is available in all AWS Regions where RDS for SQL Server is available.
It is only supported for SQL Server Enterprise Edition for SQL Server 2016, SQL Server 2017,
SQL Server 2019, and SQL Server 2022.

## Limitations and recommendations

The following limitations and recommendations apply to resource governor:

- Edition and service restrictions:
  - Available only in SQL Server Enterprise Edition.
  - Resource management is limited to the SQL Server Database Engine.
    Resource governor for Analysis Services, Integration Services, and Reporting Services are not supported.

- Configuration restrictions:
  - Must use Amazon RDS stored procedures for all configurations.
  - Native DDL statements and SQL Server Management Studio GUI configurations aren't supported.

- Resource pool parameters:
  - Pool names starting with `rds_` aren't supported.
  - Internal and default resource pool modifications aren't permitted.
  - For the user-defined resource pools the following resource pool parameters aren't supported:
    - `MIN_MEMORY_PERCENT`
    - `MIN_CPU_PERCENT`
    - `MIN_IOPS_PER_VOLUME`
    - `AFFINITY`

- Workload group parameters:
  - Workload group names starting with `rds_` aren't supported.
  - Internal workload group modification isn't permitted.
  - For the default workload group:
    - Only the `REQUEST_MAX_MEMORY_GRANT_PERCENT` parameter can be modified.
    - For the default workload group, `REQUEST_MAX_MEMORY_GRANT_PERCENT` must be between 1 and 70.
    - All other parameters are locked and can't be changed.

  - User-defined workload groups allow modification of all parameters.

- Classifier function limitations:
  - Classifier function routes connections to custom workload groups
    based on specified criteria (user name, database, host, or application name).
  - Supports up to two user-defined workload groups with their
    respective routing conditions.
  - Combines criterion with `AND` conditions within each group.
  - Requires at least one routing criterion per workload group.
  - Only the classification methods listed above are supported.
  - Function name must start with `rg_classifier_`.
  - Default group assignment if no conditions match.

## Considerations for Multi-AZ deployment

RDS for SQL Server replicates resource governor to secondary instance in a Multi-AZ deployment.
You can verify when modified and new resource governor last synchronized with the secondary instance.

Use the following query to check the `last_sync_time` of the replication:

```
SELECT * from msdb.dbo.rds_fn_server_object_last_sync_time();
```

In the query results, if the sync time is past the resource governor updated or creation time, then the resource governor syncs with the secondary.

To perform a manual DB failover to confirm that the resource governor replicate,
wait for the `last_sync_time` to update first. Then, proceed with the Multi-AZ failover.

## Considerations for read replicas

- For SQL Server replicas in the same Region as the source DB instance,
  use the same option group as the source. Changes to the option group propagate
  to replicas immediately, regardless of their maintenance windows.
- When you create a SQL Server cross-Region replica, RDS creates a dedicated option group for it.
- You can't remove an SQL Server cross-Region replica from its dedicated option group.
  No other DB instances can use the dedicated option group for a SQL Server cross-Region replica.
- Resource governor option is non-replicated options.
  You can add or remove non-replicated options from a dedicated option group.
- When you promote a SQL Server cross-Region read replica, the promoted replica
  behaves the same as other SQL Server DB instances, including the management of its options.

###### Note

When using Resource governor on a read replica, you must manually ensure that resource governor has been configured on your read replica
using Amazon RDS stored procedures after the option is added to the option group. Resource governor configurations do not automatically replicate to
the read replica. Also, the workload on read replica is typically different than the primary instance.
Hence, it's recommended to apply the resource configuration on the replica based on your workload and instance type.
You can run these Amazon RDS stored procedures on read replica independently to configure resource governor on read replica.
