# Resource governor features

This topic provides reference information about resource management and workload isolation capabilities in SQL Server 2019 and Amazon Aurora MySQL. You can understand the differences in how these database systems handle resource limits and workload management.

| Feature compatibility          | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences                       |
| ------------------------------ | ---------------------------------- | ------------------------- | ------------------------------------- |
| One star feature compatibility | N/A                                | N/A                       | Use the resource limit for each user. |

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
- **Classification** is a process that inspects incoming connections and assigns them to a specific Workload Group based on the common attributes. User-defined functions are used to implement Classification. For more information, see [User-Defined Functions](chap-sql-server-aurora-mysql.tsql.md "chap-sql-server-aurora-mysql.tsql.md").

### Examples

Turn on the Resource Governor.

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

## MySQL Usage

Amazon Aurora MySQL-Compatible Edition (Aurora MySQL) doesn’t support a server-wide, granular, resource-based, workload resource isolation and management capability similar to SQL Server Resource Governor. However, Aurora MySQL does support the feature User Resource Limit Options that you can use to achieve similar high-level functionality for limiting resource consumption of user connections.

You can specify User Resource Limit Options as part of the `CREATE USER` statement to place the following limits on users:

- The number of total queries in hour an account is allowed to issue.
- The number of updates in hour an account is allowed to issue.
- The number of times in hour an account can establish a server connection.
- The total number of concurrent server connections allowed for the account.

For more information, see [Users and Roles](chap-sql-server-aurora-mysql.security.md "chap-sql-server-aurora-mysql.security.md").

### Syntax

```
CREATE USER <User Name> ...
WITH
MAX_QUERIES_PER_HOUR count |
MAX_UPDATES_PER_HOUR count |
MAX_CONNECTIONS_PER_HOUR count |
MAX_USER_CONNECTIONS count
```

### Migration Considerations

Although both SQL Server Resource Manager and Aurora MySQL User Resource Limit Options provide the same basic function — limiting the amount of resources for distinct types of workloads — they differ significantly in scope and flexibility.

SQL Server Resource Manager is a dynamically configured independent framework based on actual run-time resource consumption. User Resource Limit Options are defined as part of the security objects and requires application connection changes to map to limited users. To modify these limits, you must alter the user object.

User Resource Limit Options don’t allow limiting workload activity based on actual resource consumption, but rather provides a quantitative limit for the number of queries or number of connections. A runaway query that consumes a large amount of resources may slow down the server.

Another important difference is how exceeded resource limits are handled. SQL Server Resource Governor throttles the run; Aurora MySQL raises errors.

### Example

Create a resource-limited user.

```
CREATE USER 'ReportUsers'@'localhost'
IDENTIFIED BY 'ReportPassword'
WITH
MAX_QUERIES_PER_HOUR 60
MAX_UPDATES_PER_HOUR 0
MAX_CONNECTIONS_PER_HOUR 5
MAX_USER_CONNECTIONS 2;
```

## Summary

| Feature                                   | SQL Server Resource Governor                                                 | Aurora MySQL User Resource Limit Options  | Comments                                                           |
| ----------------------------------------- | ---------------------------------------------------------------------------- | ----------------------------------------- | ------------------------------------------------------------------ |
| Scope                                     | Dynamic workload pools and workload groups, mapped to a classifier function. | For each user.                            | Application connection strings need to use specific limited users. |
| Limited resources                         | IO, CPU, and memory.                                                         | Number of queries, number of connections. |                                                                    |
| Modifying limits                          | `ALTER RESOURCE POOL`                                                        | `ALTER USER`                              | Application may use a dynamic connection string.                   |
| When resource threshold limit is reached. | Throttles and queues runs.                                                   | Raises an error.                          | Application retry logic may need to be added.                      |

For more information, see [CREATE USER Resource-Limit Options](https://dev.mysql.com/doc/refman/5.7/en/create-user.html#create-user-resource-limits "https://dev.mysql.com/doc/refman/5.7/en/create-user.html#create-user-resource-limits") and [Setting Account Resource Limits](https://dev.mysql.com/doc/refman/5.7/en/user-resources.html "https://dev.mysql.com/doc/refman/5.7/en/user-resources.html") in the _MySQL documentation_.
