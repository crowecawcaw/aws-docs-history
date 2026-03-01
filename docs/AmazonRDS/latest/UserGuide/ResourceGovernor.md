# Using Microsoft SQL Server resource governor for your RDS for SQL Server instance

After adding the resource governor option to your option group, resource governor
is not yet active at the database engine level. To fully enable resource governor, you must use
RDS for SQL Server stored procedures to enable it and create the necessary resource governor objects.
For more information, see [Connecting to your Microsoft SQL Server DB instance](USER_ConnectToMicrosoftSQLServerInstance.md "USER_ConnectToMicrosoftSQLServerInstance.md").

First, connect to your SQL Server database, then call the appropriate RDS for SQL Server stored procedures
to complete the configuration. For instructions on connecting to your database, see [Connecting to your Microsoft SQL Server DB instance](USER_ConnectToMicrosoftSQLServerInstance.md "USER_ConnectToMicrosoftSQLServerInstance.md").

For instructions on how to call each stored procedure, see the following topics:

###### Topics

- [Manage resource pool](#ResourceGovernor.ManageResourcePool "#ResourceGovernor.ManageResourcePool")
- [Manage workload groups](#ResourceGovernor.ManageWorkloadGroups "#ResourceGovernor.ManageWorkloadGroups")
- [Create and register classifier function](#ResourceGovernor.ClassifierFunction "#ResourceGovernor.ClassifierFunction")
- [Drop classifier function](#ResourceGovernor.DropClassifier "#ResourceGovernor.DropClassifier")
- [De-register classifier function](#ResourceGovernor.DeregisterClassifier "#ResourceGovernor.DeregisterClassifier")
- [Reset statistics](#ResourceGovernor.ResetStats "#ResourceGovernor.ResetStats")
- [Resource governor configuration changes](#ResourceGovernor.ConfigChanges "#ResourceGovernor.ConfigChanges")
- [Bind TempDB to a resource pool](#ResourceGovernor.BindTempDB "#ResourceGovernor.BindTempDB")
- [Unbind TempDB from a resource pool](#ResourceGovernor.UnbindTempDB "#ResourceGovernor.UnbindTempDB")
- [Cleanup resource governor](#ResourceGovernor.Cleanup "#ResourceGovernor.Cleanup")

## Manage resource pool

### Create resource Pool

Once resource governor is enabled on the option group, you can create custom
resource pools using `rds_create_resource_pool`. These pools let you allocate
specific percentages of CPU, memory, and IOPS to different workloads.

**Usage**

```
USE [msdb]
EXEC dbo.rds_create_resource_pool
    @pool_name=value,
    @MAX_CPU_PERCENT=value,
    @CAP_CPU_PERCENT=value,
    @MAX_MEMORY_PERCENT=value,
    @MAX_IOPS_PER_VOLUME=value
```

The following parameters are required:

- `@group_name` - Is the name of an existing user-defined workload group.
- `@pool_name` - Is the user-defined name for the resource pool.
  `pool_name` is alphanumeric, can be up to 128 characters,
  must be unique within a Database Engine instance, and must comply with the rules for database identifiers.

The following parameters are optional:

- `@MAX_CPU_PERCENT` - Specifies the maximum average CPU bandwidth that all requests in resource pool
  receive when there's CPU contention. `value` is an integer with a default setting of 100.
  The allowed range for `value` is from 1 through 100.
- `@CAP_CPU_PERCENT` - Specifies a hard cap on the CPU bandwidth that all requests in the resource pool receive.
  Limits the maximum CPU bandwidth level to be the same as the specified value. `value` is an integer
  with a default setting of 100. The allowed range for `value` is from 1 through 100.
- `@MAX_MEMORY_PERCENT` - Specifies the maximum amount of query workspace memory that requests in this resource
  pool can use. `value` is an integer with a default setting of 100. The allowed range for
  `value` is from 1 through 100.
- `@MAX_IOPS_PER_VOLUME` - Specifies the maximum I/O operations per second (IOPS) per disk volume to allow for
  the resource pool. The allowed range for `value` is from 0 through 2^31-1 (2,147,483,647).
  Specify 0 to remove an IOPS limit for the pool. The default is 0.

**Examples**

Example of creating resource pool with all default values:

```
--This creates resource pool 'SalesPool' with all default values
USE [msdb]
EXEC rds_create_resource_pool @pool_name = 'SalesPool';

--Apply changes
USE [msdb]
EXEC msdb.dbo.rds_alter_resource_governor_configuration;

--Validate configuration
select * from sys.resource_governor_resource_pools
```

Example of creating resource pool with different parameters specified:

```
--creates resource pool
USE [msdb]
EXEC dbo.rds_create_resource_pool
@pool_name='analytics',
@MAX_CPU_PERCENT = 30,
@CAP_CPU_PERCENT = 40,
@MAX_MEMORY_PERCENT = 20;

--Apply changes
EXEC msdb.dbo.rds_alter_resource_governor_configuration;

--Validate configuration
select * from sys.resource_governor_resource_pools
```

### Alter resource pool

**Usage**

```
USE [msdb]
EXEC dbo.rds_alter_resource_pool
    @pool_name=value,
    @MAX_CPU_PERCENT=value,
    @CAP_CPU_PERCENT=value,
    @MAX_MEMORY_PERCENT=value,
    @MAX_IOPS_PER_VOLUME=value;
```

The following parameters are required:

- `@pool_name` - Is the name of an existing user-defined resource pool.
  Altering default resource pool isn't allowed in Amazon RDS SQL Server.

At least one of the optional parameter must be specified:

- `@MAX_CPU_PERCENT` - Specifies the maximum average CPU bandwidth that all requests in resource pool
  receive when there's CPU contention. `value` is an integer with a default setting of 100. The allowed range for `value` is from 1 through 100.
- `@CAP_CPU_PERCENT` - Specifies a hard cap on the CPU bandwidth that all requests in the resource pool receive.
  Limits the maximum CPU bandwidth level to be the same as the specified value. `value` is an integer with a default setting of 100. The allowed range for `value` is from 1 through 100.
- `@MAX_MEMORY_PERCENT` - Specifies the maximum amount of query workspace memory that requests in this resource pool can use.
  `value` is an integer with a default setting of 100. The allowed range for `value` is from 1 through 100.
- `@MAX_IOPS_PER_VOLUME` - Specifies the maximum I/O operations per second (IOPS) per disk volume to allow for the resource pool.
  The allowed range for `value` is from 0 through 2^31-1 (2,147,483,647). Specify 0 to remove an IOPS limit for the pool. The default is 0.

**Examples**

```
--This alters resource pool
USE [msdb]
EXEC dbo.rds_alter_resource_pool
    @pool_name='analytics',
    @MAX_CPU_PERCENT = 10,
    @CAP_CPU_PERCENT = 20,
    @MAX_MEMORY_PERCENT = 50;

--Apply changes
EXEC msdb.dbo.rds_alter_resource_governor_configuration;

--Validate configuration.
select * from sys.resource_governor_resource_pools
```

### Drop resource pool

**Usage**

```
USE [msdb]
EXEC dbo.rds_drop_resource_pool
@pool_name=value;
```

The following parameter is required:

- `@pool_name` - Is the name of an existing user-defined resource pool.

###### Note

Dropping Internal or default resource pool isn't allowed in SQL Server.

**Examples**

```
--This drops resource pool
USE [msdb]
EXEC dbo.rds_drop_resource_pool
@pool_name='analytics'

--Apply changes
EXEC msdb.dbo.rds_alter_resource_governor_configuration;

--Validate configuration
select * from sys.resource_governor_resource_pools
```

## Manage workload groups

Workload groups, created and managed with `rds_create_workload_group` and
`rds_alter_workload_group`, allow you to set importance levels, memory grants,
and other parameters for groups of queries.

### Create workload group

**Usage**

```
USE [msdb]
EXEC dbo.rds_create_workload_group
@group_name = value,
@IMPORTANCE ={ LOW | MEDIUM | HIGH },
@REQUEST_MAX_MEMORY_GRANT_PERCENT =value,
@REQUEST_MAX_CPU_TIME_SEC = value ,
@REQUEST_MEMORY_GRANT_TIMEOUT_SEC = value,
@MAX_DOP = value,
@GROUP_MAX_REQUESTS = value,
@pool_name = value
```

The following parameters are required:

- `@pool_name` - Is the name of an existing user-defined resource pool.
- `@group_name` - Is the name of an existing user-defined workload group.

The following parameters are optional:

- `@IMPORTANCE` - Specifies the relative importance of a request in the workload group. The default value is `MEDIUM`.
- `@REQUEST_MAX_MEMORY_GRANT_PERCENT` - Specifies the maximum amount of query workspace memory
  that a single request can take from the pool. `value` is a percentage of the resource
  pool size defined by `MAX_MEMORY_PERCENT`. Default value is 25.
- `@REQUEST_MAX_CPU_TIME_SEC` - Specifies the maximum amount of CPU time, in seconds,
  that a batch request can use. `value` must be 0 or a positive integer.
  The default setting for `value` is 0, which means unlimited.
- `@REQUEST_MEMORY_GRANT_TIMEOUT_SEC` - Specifies the maximum time, in seconds, that a
  query can wait for a memory grant from the query workspace memory to become available.
  `value` must be 0 or a positive integer. The default setting for `value`,
  0, uses an internal calculation based on query cost to determine the maximum time.
- `@MAX_DOP` - Specifies the maximum degree of parallelism (`MAXDOP`) for parallel query execution.
  The allowed range for `value` is from 0 through 64. The default setting for `value`,
  0, uses the global setting.
- `@GROUP_MAX_REQUESTS` = Specifies the maximum number of simultaneous requests that are allowed to execute
  in the workload group. `value` must be 0 or a positive integer. The default setting for
  `value` is 0, and allows unlimited requests.
- `@pool_name` = Associates the workload group with the user-defined resource pool identified by
  `pool_name`, or with the `default` resource pool. If `pool_name`
  isn't provided, the workload group is associated with the built-in `default` pool.

**Examples**

```
--This creates workload group named 'analytics'
USE msdb;
EXEC dbo.rds_create_workload_group
    @group_name = 'analytics',
    @IMPORTANCE = 'HIGH',
    @REQUEST_MAX_MEMORY_GRANT_PERCENT = 25,
    @REQUEST_MAX_CPU_TIME_SEC = 0,
    @REQUEST_MEMORY_GRANT_TIMEOUT_SEC = 0,
    @MAX_DOP = 0,
    @GROUP_MAX_REQUESTS = 0,
    @pool_name = 'analytics';

--Apply changes
EXEC msdb.dbo.rds_alter_resource_governor_configuration;

--Validate configuration
select * from sys.resource_governor_workload_groups
```

### Alter workload group

**Usage**

```
EXEC msdb.dbo.rds_alter_workload_group
    @group_name = value,
    @IMPORTANCE = 'LOW|MEDIUM|HIGH',
    @REQUEST_MAX_MEMORY_GRANT_PERCENT = value,
    @REQUEST_MAX_CPU_TIME_SEC = value,
    @REQUEST_MEMORY_GRANT_TIMEOUT_SEC = value,
    @MAX_DOP = value,
    @GROUP_MAX_REQUESTS = value,
    @pool_name = value
```

The following parameters are required:

- `@group_name` - Is the name of default or an existing user-defined workload group.

###### Note

Changing only `REQUEST_MAX_MEMORY_GRANT_PERCENT` parameter on the default workload
group is supported. For default workload group the `REQUEST_MAX_MEMORY_GRANT_PERCENT` must be between
1 and 70. No other parameters can be modified in default workload group. All parameters can be modified in the user-defined workload group.

The following parameters are optional:

- `@IMPORTANCE` - Specifies the relative importance of a request in the workload group.
  The default value is MEDIUM.
- `@REQUEST_MAX_MEMORY_GRANT_PERCENT` - Specifies the maximum amount of query
  workspace memory that a single request can take from the pool. `value`
  is a percentage of the resource pool size defined by `MAX_MEMORY_PERCENT`.
  Default value is 25. On Amazon RDS, `REQUEST_MAX_MEMORY_GRANT_PERCENT` must be between 1 and 70.
- `@REQUEST_MAX_CPU_TIME_SEC` - Specifies the maximum amount of CPU time, in seconds, that a batch request can use.
  `value` must be 0 or a positive integer. The default setting for `value` is 0, which means unlimited.
- `@REQUEST_MEMORY_GRANT_TIMEOUT_SEC` - Specifies the maximum time, in seconds, that a query can wait for a memory
  grant from the query workspace memory to become available. `value` must be 0 or a positive integer.
  The default setting for `value`, 0, uses an internal calculation based on query cost to determine the maximum time.
- `@MAX_DOP` - Specifies the maximum degree of parallelism (MAXDOP) for parallel query execution. The allowed range for
  `value` is from 0 through 64. The default setting for `value`, 0, uses the global setting.
- `@GROUP_MAX_REQUESTS` - Specifies the maximum number of simultaneous requests that are allowed to execute in the workload group.
  `value` must be 0 or a positive integer. The default setting for `value` is 0, and allows unlimited requests.
- `@pool_name` - Associates the workload group with the user-defined resource pool identified by `pool_name`.

**Examples**

Example to Modify default workload group change REQUEST_MAX_MEMORY_GRANT_PERCENT:

```
--Modify default workload group (set memory grant cap to 10%)
USE msdb
EXEC dbo.rds_alter_workload_group
    @group_name = 'default',
    @REQUEST_MAX_MEMORY_GRANT_PERCENT=10;

--Apply changes
EXEC msdb.dbo.rds_alter_resource_governor_configuration;

--Validate configuration
SELECT * FROM sys.resource_governor_workload_groups WHERE name='default';
```

Example to modify non-default workload group:

```
EXEC msdb.dbo.rds_alter_workload_group
    @group_name = 'analytics',
    @IMPORTANCE = 'HIGH',
    @REQUEST_MAX_MEMORY_GRANT_PERCENT = 30,
    @REQUEST_MAX_CPU_TIME_SEC = 3600,
    @REQUEST_MEMORY_GRANT_TIMEOUT_SEC = 60,
    @MAX_DOP = 4,
    @GROUP_MAX_REQUESTS = 100;

--Apply changes
EXEC msdb.dbo.rds_alter_resource_governor_configuration;
```

Example to move a Non-Default Workload Group to another resource pool:

```
EXEC msdb.dbo.rds_alter_workload_group
@group_name = 'analytics',
@pool_name='abc'

--Apply changes
EXEC msdb.dbo.rds_alter_resource_governor_configuration;

--Validate configuration
select * from sys.resource_governor_workload_groups
```

### Drop workload group

**Usage**

```
EXEC msdb.dbo.rds_drop_workload_group
@group_name = value
```

The following parameters are required:

- `@group_name` - Is the name of an existing user-defined workload group.

**Examples**

```
--Drops a Workload Group:
EXEC msdb.dbo.rds_drop_workload_group
@group_name = 'analytics';

--Apply changes
EXEC msdb.dbo.rds_alter_resource_governor_configuration;

--Validate configuration
select * from sys.resource_governor_workload_groups
```

## Create and register classifier function

This procedure creates a resource governor classifier function in master database that
routes connections to custom workload groups based on specified criteria (user name, database, host, or application name).
If resource governor is enabled and a classifier function is specified in the resource governor configuration, then the
function output determines the workload group used for new sessions. In the absence of a classifier function, all sessions
are classified into the `default` group.

**Features:**

- Supports up to two workload groups with their respective routing conditions.
- Combines criterion with `AND` conditions within each group.
- Requires at least one routing criterion per workload group.
- Function name must start with `rg_classifier_`.
- Default group assignment if no conditions match.

The classifier function has the following characteristics and behaviors:

- The function is defined in the server scope (in the master database).
- The function is defined with schema binding.
- The function is evaluated for every new session, even when connection pooling is enabled.
- The function returns the workload group context for the session. The session is assigned to the
  workload group returned by the classifier for the lifetime of the session.
- If the function returns NULL, default, or the name of a nonexistent workload group,
  the session is given the default workload group context.
  The session is also given the default context if the function fails for any reason.
- You can create multiple classifier functions. However, SQL Server allows only one classifier function to be registered at a time.
- The classifier function can't be dropped unless its classifier status is removed using the de-register procedure
  (`EXEC dbo.msdb.rds_alter_resource_governor_configuration @deregister_function = 1;`) that sets the function name
  to NULL or another classifier function is registered using (`EXEC dbo.msdb.rds_alter_resource_governor_configuration @classifier_function = <function_name>;`)
- In the absence of a classifier function, all sessions are classified into the default group.
- You can't modify a classifier function while it is referenced in the resource governor configuration.
  However, you can modify the configuration to use a different classifier function. If you want to make changes to the classifier,
  consider creating a pair of classifier functions. For example, you might create `rg_classifier_a` and `rg_classifier_b`.

**Usage**

```
EXEC msdb.dbo.rds_create_classifier_function
@function_name = value,
@workload_group1 = value,
@user_name1 = value,
@db_name1 = value,
@host_name1 = value,
@app_name1 = value,
@workload_group2 = value,
@user_name2 = value,
@db_name2 = value,
@host_name2 = value,
@app_name2 = value
```

The following parameters are required:

- `@function_name` - Name of the classifier function.
  Must start with `rg_classifier_`
- `@workload_group1` - Name of the first workload group

The following parameters are optional:

(At least one of these criteria must be specified for group 1)

- `@user_name1` - Login name for group 1
- `@db_name1` - Database name for group 1
- `@host_name1` - Host name for group 1
- `@app_name1` - Application name for group 1

(If group 2 is specified, at least one criterion must be provided)

- `@workload_group2` - Name of the second workload group
- `@user_name2` - Login name for group 2
- `@db_name2` - Database name for group 2
- `@host_name2` - Host name for group 2
- `@app_name2` - Application name for group 2

###### Note

System accounts, databases, applications and host are restricted.

**Examples**

Basic Example with One Workload Group:

```
/*Create a classifier to route all requests from 'PowerBI' app to workload group
'reporting_group'*/

EXEC msdb.dbo.rds_create_classifier_function
@function_name = 'rg_classifier_a',
@workload_group1 = 'reporting_group',
@app_name1 = 'PowerBI';

--Register the classifier
EXEC msdb.dbo.rds_alter_resource_governor_configuration
@classifier_function = 'rg_classifier_a';

-- Apply changes
EXEC msdb.dbo.rds_alter_resource_governor_configuration

/*Query sys.resource_governor_configuration to validate that resource governor is enabled and is using the classifier function we created and registered*/

use master
go
SELECT OBJECT_SCHEMA_NAME(classifier_function_id) AS classifier_schema_name,
       OBJECT_NAME(classifier_function_id) AS classifier_object_name,
       is_enabled
FROM sys.resource_governor_configuration;
```

## Drop classifier function

**Usage**

```
USE [msdb]
EXEC dbo.rds_drop_classifier_function
@function_name = value;
```

The following parameter is required:

- `@function_name` - Is the name of an existing user-defined classifier function

**Example**

```
EXEC msdb.dbo.rds_drop_classifier_function
@function_name = 'rg_classifier_b';
```

## De-register classifier function

Use this procedure to de-register classifier function.
After the function is de-registered, new sessions are automatically assigned
to the default workload group.

**Usage**

```
USE [msdb]
EXEC dbo.rds_alter_resource_governor_configuration
@deregister_function = 1;
```

For de-registration the following parameter is required:

- `@deregister_function` must be 1

**Example**

```
EXEC msdb.dbo.rds_alter_resource_governor_configuration
    @deregister_function = 1;
GO

-- Apply changes
EXEC msdb.dbo.rds_alter_resource_governor_configuration;
```

## Reset statistics

Resource governor statistics are cumulative since the last server restart. If you need to
collect statistics starting from a certain time, you can reset statistics using the following Amazon RDS stored procedure.

**Usage**

```
USE [msdb]
EXEC dbo.rds_alter_resource_governor_configuration
@reset_statistics = 1;
```

For reset stats the following parameter is required:

- `@reset_statistics` must be 1

## Resource governor configuration changes

When resource governor isn’t enabled, `rds_alter_resource_governor_configuration` enables resource governor.
Enabling resource governor has the following results:

- The classifier function, if any, is executed for new sessions, assigning them to workload groups.
- The resource limits that are specified in resource governor configuration are honored and enforced.
- The resource limits that are specified in resource governor configuration are honored and enforced.
- Requests that existed before enabling resource governor might
  be affected by any configuration changes made when resource governor is enabled.
- Existing requests, before enabling resource governor, might be affected
  by any configuration changes made when resource governor is enabled.
- On RDS for SQL Server, `EXEC msdb.dbo.rds_alter_resource_governor_configuration` must be
  executed for any resource governor configuration changes to take effect.

**Usage**

```
USE [msdb]
EXEC dbo.rds_alter_resource_governor_configuration
```

## Bind TempDB to a resource pool

You can bind tempdb memory optimized metadata to a specific resource pool using
`rds_bind_tempdb_metadata_to_resource_pool` in Amazon RDS SQL Server version 2019 and above.

###### Note

Memory-optimized tempdb metadata feature must be enabled before binding tempdb metadata to
resource pool. To enable this feature on Amazon RDS its a static parameter `tempdb metadata memory-optimized`.

Enable the static parameter on Amazon RDS and perform a reboot without failover for the parameter to take effect:

```
aws rds modify-db-parameter-group \
    --db-parameter-group-name test-sqlserver-ee-2022 \
    --parameters "ParameterName='tempdb metadata memory-optimized',ParameterValue=True,ApplyMethod=pending-reboot"
```

**Usage**

```
USE [msdb]
EXEC dbo.rds_bind_tempdb_metadata_to_resource_pool
@pool_name=value;
```

The following parameter is required:

- `@pool_name` - Is the name of an existing user-defined resource pool.

###### Note

This change also requires sql service reboot without failover to take effect, even if Memory-optimized TempDB metadata feature is already enabled.

## Unbind TempDB from a resource pool

Unbind tempdb memory optimized metadata from a resource pool.

###### Note

This change also requires sql service reboot without failover to take effect

**Usage**

```
USE [msdb]
EXEC dbo.rds_unbind_tempdb_metadata_from_resource_pool
```

## Cleanup resource governor

This procedure is to clean up all associated objects after you have removed the resource governor option from the option group.
This disables resource governor, reverts default workload group to default settings,
remove custom workload groups, resource pools, and classifier functions.

**Key features**

- Reverts default workload group to default settings
- Disables resource governor
- Removes custom workload groups
- Removes custom resource pools
- Drops classifier functions
- Removes tempdb resource pool binding if enabled

###### Important

This cleanup can error out if there are active sessions on the workload group.
Either wait for the active sessions to finish or terminate the active sessions as per
your business requirement. It's recommended to run this during the maintenance window.

This cleanup can error out if a resource pool was bound to tempdb and reboot without failover
hasn't been taken place yet. If you bound a resource pool to tempdb or unbound a resource pool
from tempdb earlier, perform a reboot without failover to make the change effective. It's recommended to run this during the maintenance window.

**Usage**

```
USE [msdb]
EXEC dbo.rds_cleanup_resource_governor
```
