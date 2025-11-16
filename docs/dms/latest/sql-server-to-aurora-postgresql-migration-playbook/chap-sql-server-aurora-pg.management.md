# Resource governor features

This topic provides reference information comparing resource management capabilities between Microsoft SQL Server and Amazon Aurora PostgreSQL. You can understand how SQL Server’s Resource Governor functionality, which allows administrators to control and manage resource consumption, differs from Aurora PostgreSQL. While Aurora PostgreSQL doesn’t have built-in resource management equivalent to SQL Server, it leverages cloud economics and flexibility to address similar needs.

| Feature compatibility            | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences                                                    |
| -------------------------------- | ---------------------------------- | ------------------------- | ------------------------------------------------------------------ |
| Three star feature compatibility | N/A                                | N/A                       | Distribute load, applications, or users across multiple instances. |

## SQL Server Usage

SQL Server Resource Governor provides the capability to control and manage resource consumption. Administrators can specify and enforce workload limits on CPU, physical I/O, and Memory. Resource configurations are dynamic and you can change them in real time.

In SQL Server 2019 configurable value for the `REQUEST_MAX_MEMORY_GRANT_PERCENT` option of `CREATE WORKLOAD GROUP` and `ALTER WORKLOAD GROUP` has been changed from an integer to a float data type to allow more granular control of memory limits. For more information, see [ALTER WORKLOAD GROUP (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/statements/alter-workload-group-transact-sql?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/t-sql/statements/alter-workload-group-transact-sql?view=sql-server-ver15") and [CREATE WORKLOAD GROUP (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/statements/create-workload-group-transact-sql?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/t-sql/statements/create-workload-group-transact-sql?view=sql-server-ver15") in the _SQL Server documentation_.

### Use Cases

The following list identifies typical Resource Governor use cases:

- **Minimize performance bottlenecks and inconsistencies** to better support Service Level Agreements (SLA) for multiple workloads and users.
- **Protect against runaway queries** that consume a large amount of resources or explicitly throttle I/O intensive operations. For example, consistency checks with DBCC that may bottleneck the I/O subsystem and negatively impact concurrent workloads.
- **Allow tracking and control for resource-based pricing scenarios** to improve predictability of user charges.

### Concepts

The three basic concepts in Resource Governor are Resource Pools, Workload Groups, and Classification.

- **Resource Pools** represent physical resources. Two built-in resource pools, internal and default, are created when SQL Server is installed. You can create custom user-defined resource pools for specific workload types.
- **Workload Groups** are logical containers for session requests with similar characteristics. Workload Groups allow aggregate resource monitoring of multiple sessions. Resource limit policies are defined for a Workload Group. Each Workload Group belongs to a Resource Pool.
- **Classification** is a process that inspects incoming connections and assigns them to a specific Workload Group based on the common attributes. User-defined functions are used to implement Classification. For more information, see [User-Defined Functions](chap-sql-server-aurora-pg.tsql.md "chap-sql-server-aurora-pg.tsql.md").

### Examples

Enable the Resource Governor.

```
ALTER RESOURCE GOVERNOR RECONFIGURE;
```

Create a Resource Pool.

```
CREATE RESOURCE POOL ReportingWorkloadPool
    WITH (MAX_CPU_PERCENT = 20);
```

```
ALTER RESOURCE GOVERNOR RECONFIGURE;
```

Create a Workload Group.

```
CREATE WORKLOAD GROUP ReportingWorkloadGroup USING poolAdhoc;
```

```
ALTER RESOURCE GOVERNOR RECONFIGURE;
```

Create a classifier function.

```
CREATE FUNCTION dbo.WorkloadClassifier()
RETURNS sysname WITH SCHEMABINDING
AS
BEGIN
    RETURN (CASE
        WHEN HOST_NAME()= 'ReportServer'
        THEN 'ReportingWorkloadGroup'
        ELSE 'Default'
    END)
END;
```

Register the classifier function.

```
ALTER RESOURCE GOVERNOR with (CLASSIFIER_FUNCTION = dbo.WorkloadClassifier);
```

```
ALTER RESOURCE GOVERNOR RECONFIGURE;
```

For more information, see [Resource Governor](https://docs.microsoft.com/en-us/sql/relational-databases/resource-governor/resource-governor?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/relational-databases/resource-governor/resource-governor?view=sql-server-ver15") in the _SQL Server documentation_.

## PostgreSQL Usage

PostgreSQL doesn’t have built-in resource management capabilities equivalent to the functionality provided by SQL Server’s Resource Governor. However, due to the elasticity and flexibility provided by cloud economics, workarounds could be applicable and such capabilities might not be as of similar importance to monolithic on-premises databases.

The SQL Server’s Resource Governor primarily exists because traditionally, SQL Server instances were installed on very powerful monolithic servers that powered multiple applications simultaneously. The monolithic model made the most sense in an environment where the licensing for the SQL Server database was per-CPU and where SQL Server instances were deployed on physical hardware. In these scenarios, it made sense to consolidate as many workloads as possible into fewer servers. With cloud databases, the strict requirement to maximize the usage of each individual server is often not as important and you can use a different approach.

You can deploy individual Amazon Aurora clusters with varying sizes, each dedicated to a specific application or workload. You can use additional read-only Amazon Aurora Replica servers to offload any reporting workloads from the master instance.

With Amazon Aurora, you can deploy separate and dedicated database clusters, each dedicated to a specific application or workload creating isolation between multiple connected sessions and applications.

Each Amazon Aurora instance (primary or replica) can scale independently in terms of CPU and memory resources using different instance types. Because you can instantly deploy multiple Amazon Aurora Instances and much less overhead is associated with the deployment and management of Amazon Aurora instances when compared to physical servers, separating different workloads to different instance classes could be a suitable solution for controlling resource management.

For more information, see [Amazon EC2 Instance Types](https://aws.amazon.com/ec2/instance-types/ "https://aws.amazon.com/ec2/instance-types/").

In addition, each Amazon Aurora instance can also be directly accessed from your applications using its own endpoint. This capability is especially useful if you have multiple Amazon Aurora read-replicas for a given cluster and you want to use different Amazon Aurora replicas to segment your workload.

You can adjust the resources and some parameters for Amazon Aurora read-replicas in the same cluster to avoid having additional cluster, however, this will allow to be used only for read operations.

### Examples

Follow these steps to create an Amazon Aurora cluster.

1. In the AWS console, choose **RDS**.
2. Choose **Databases**, and then choose **Create database**.
3. Follow the wizard. Your new cluster appears in the **Databases** section.

Suppose that you were using a single SQL Server instance for multiple separate applications and used SQL Server Resource Governor to enforce a workload separation, allocating a specific amount of server resources for each application. With Amazon Aurora, you might want to create multiple separate databases for each individual application.

Follow these steps to add additional replica instances to an existing Amazon Aurora cluster:

1. In the AWS console, choose **RDS**.
2. Choose the Amazon Aurora cluster that you want to scale-out by adding an additional read replica.
3. For **Instance actions**, choose **Create Aurora Replica**.
4. Select the instance class depending on the amount of compute resources your application requires.
5. Choose **Create Aurora Replica**.

### Dedicated Aurora PostgreSQL Instances

| Feature                                                                          | Amazon Aurora instances                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| -------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Set the maximum CPU usage for a resource group.                                  | Create a dedicated Amazon Aurora instance for a specific application.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Limit the degree of parallelism for specific queries.                            | `<br>SET max_parallel_workers_per_gather TO x;<br>`<br>Setting the PostgreSQL `max_parallel_workers_per_gather` parameter should be done as part of your application database connection.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Limit parallel runs                                                              | `<br>SET max_parallel_workers_per_gather TO 0;<br>`<br>or<br>`<br>SET max_parallel_workers TO x; -<br>• for the whole system (since PostgreSQL 10)<br>`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Limit the number of active sessions.                                             | Manually detect the number of connections that are open from a specific application and restrict connectivity either with database procedures or within the application DAL itself.<br>`<br>select pid from pg_stat_activity where usename in( select usename from pg_stat_activity<br>where state = 'active' group by usename having count(*) > 10)<br>and state = 'active' order by query_Start;<br>`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Restrict maximum runtime of queries.                                             | Manually terminate sessions that exceed the required threshold. You can detect the length of running queries using SQL commands and restrict max run duration using either database procedures or within the application DAL itself.<br>`<br>SELECT pg_terminate_backend(pid)<br>FROM pg_stat_activity<br>WHERE now()-pg_stat_activity.query_start > interval '5 minutes';<br>`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Limit the maximum idle time for sessions.                                        | Manually terminate sessions that exceed the required threshold. You can detect the length of your idle sessions using SQL queries and restrict maximum run using either database procedures or within the application DAL itself.<br>`<br>SELECT pg_terminate_backend(pid)<br>FROM pg_stat_activity<br>WHERE datname = 'regress' AND pid <> pg_backend_pid()<br>AND state = 'idle' AND state_change < current_timestamp<br>• INTERVAL '5' MINUTE;<br>`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Limit the time that an idle session holding open locks can block other sessions. | Manually terminate sessions that exceed the required threshold. You can detect the length of blocking idle sessions using SQL queries and restrict max run duration using either database procedures or within the application DAL itself.<br>`<br>SELECT pg_terminate_backend(blocking_locks.pid)<br>FROM pg_catalog.pg_locks AS blocked_locks<br>JOIN pg_catalog.pg_stat_activity AS blocked_activity ON blocked_activity.pid = blocked_locks.pid<br>JOIN pg_catalog.pg_locks AS blocking_locks ON blocking_locks.locktype = blocked_locks.locktype<br>AND blocking_locks.DATABASE IS NOT DISTINCT FROM blocked_locks.DATABASE<br>AND blocking_locks.relation IS NOT DISTINCT FROM blocked_locks.relation<br>AND blocking_locks.page IS NOT DISTINCT FROM blocked_locks.page<br>AND blocking_locks.tuple IS NOT DISTINCT FROM blocked_locks.tuple<br>AND blocking_locks.virtualxid IS NOT DISTINCT FROM blocked_locks.virtualxid<br>AND blocking_locks.transactionid IS NOT DISTINCT FROM blocked_locks.transactionid<br>AND blocking_locks.classid IS NOT DISTINCT FROM blocked_locks.classid<br>AND blocking_locks.objid IS NOT DISTINCT FROM blocked_locks.objid<br>AND blocking_locks.objsubid IS NOT DISTINCT FROM blocked_locks.objsubid<br>AND blocking_locks.pid != blocked_locks.pid<br>JOIN pg_catalog.pg_stat_activity AS blocking_activity<br>ON blocking_activity.pid = blocking_locks.pid<br>WHERE NOT blocked_locks.granted and blocked_activity.state_change < current_timestamp<br>• INTERVAL '5' minute;<br>` |

For more information, see [Resource Consumption](https://www.postgresql.org/docs/13/runtime-config-resource.html "https://www.postgresql.org/docs/13/runtime-config-resource.html") in the _PostgreSQL documentation_.
