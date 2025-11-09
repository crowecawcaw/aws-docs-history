# Turning parallel query on and

off in Aurora MySQL

When parallel query is turned on, Aurora MySQL determines whether to use it at runtime for each query. In the case of joins,
unions, subqueries, and so on, Aurora MySQL determines whether to use parallel query at runtime for each query block. For details,
see [Verifying which statements use parallel query for Aurora MySQL](aurora-mysql-parallel-query-verifying.md "aurora-mysql-parallel-query-verifying.md") and [SQL constructs for parallel query in Aurora MySQL](aurora-mysql-parallel-query-sql.md "aurora-mysql-parallel-query-sql.md").

You can turn on and turn off parallel query dynamically at both the global and session level for a DB instance by using the
**aurora_parallel_query** option. You can change the `aurora_parallel_query` setting in your
DB cluster group to turn parallel query on or off by default.

```
`mysql>` select @@aurora_parallel_query;
`+------------------------+
| @@aurora_parallel_query|
+------------------------+
| 1 |
+------------------------+`

```

To toggle the `aurora_parallel_query` parameter at the session level, use
the standard methods to change a client configuration setting. For example, you can do so
through the `mysql` command line or within a JDBC or ODBC application. The
command on the standard MySQL client is `set session aurora_parallel_query =
 {'ON'/'OFF'}`. You can also add the session-level parameter to the JDBC
configuration or within your application code to turn on or turn off parallel query
dynamically.

You can permanently change the setting for the `aurora_parallel_query` parameter, either for a specific
DB instance or for your whole cluster. If you specify the parameter value in a DB parameter group, that value only
applies to specific DB instance in your cluster. If you specify the parameter value in a DB cluster parameter group,
all DB instances in the cluster inherit the same setting. To toggle the `aurora_parallel_query` parameter,
use the techniques for working with parameter groups, as described in
[Parameter groups for Amazon Aurora](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").
Follow these steps:

1. Create a custom cluster parameter group (recommended) or a custom DB parameter group.
2. In this parameter group, update `parallel_query` to the value that you want.
3. Depending on whether you created a DB cluster parameter group or a DB parameter group, attach the parameter group
   to your Aurora cluster or to the specific DB instances where you plan to use the parallel query feature.

###### Tip

Because `aurora_parallel_query` is a dynamic parameter, it doesn't require a cluster restart after
changing this setting. However, any connections that were using parallel query before toggling the option will
continue to do so until the connection is closed, or the instance is rebooted.
You can modify the parallel query parameter by using the
[ModifyDBClusterParameterGroup](../APIReference/API_ModifyDBClusterParameterGroup.md "../APIReference/API_ModifyDBClusterParameterGroup.md")
or [ModifyDBParameterGroup](../APIReference/API_ModifyDBParameterGroup.md "../APIReference/API_ModifyDBParameterGroup.md")
API operation or the AWS Management Console.

You can turn on hash join for parallel query clusters, turn parallel query on and off using the Amazon RDS console or the AWS CLI, and override the parallel query optimizer.

###### Contents

- [Turning on hash join for
  parallel query clusters](aurora-mysql-parallel-query-enabling.md#aurora-mysql-parallel-query-enabling-hash-join "aurora-mysql-parallel-query-enabling.md#aurora-mysql-parallel-query-enabling-hash-join")
- [Turning on and turning off
  parallel query using the console](aurora-mysql-parallel-query-enabling.md#aurora-mysql-parallel-query-enabling-console "aurora-mysql-parallel-query-enabling.md#aurora-mysql-parallel-query-enabling-console")
- [Turning on and turning off
  parallel query using the CLI](aurora-mysql-parallel-query-enabling.md#aurora-mysql-parallel-query-enabling-cli "aurora-mysql-parallel-query-enabling.md#aurora-mysql-parallel-query-enabling-cli")
- [Overriding the parallel query optimizer](aurora-mysql-parallel-query-enabling.md#aurora-mysql-parallel-query-enabling.aurora_pq_force "aurora-mysql-parallel-query-enabling.md#aurora-mysql-parallel-query-enabling.aurora_pq_force")

## Turning on hash join for

parallel query clusters

Parallel query is typically used for the kinds of resource-intensive queries that benefit from the hash join optimization.
Thus, it's helpful to make sure that hash joins are turned on for clusters where you plan to use parallel query. For
information about how to use hash joins effectively, see [Optimizing large Aurora MySQL join queries with hash joins](AuroraMySQL.BestPractices.md#Aurora.BestPractices.HashJoin "AuroraMySQL.BestPractices.md#Aurora.BestPractices.HashJoin").

## Turning on and turning off

parallel query using the console

You can turn on or turn off parallel query at the DB instance level or the DB cluster
level by working with parameter groups.

###### To turn on or turn off parallel query for a DB cluster with the AWS Management Console

1. Create a custom parameter group, as described in
   [Parameter groups for Amazon Aurora](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").
2. Update **aurora_parallel_query** to **1** (turned on) or **0** (turned
   off). For clusters where the parallel query feature is available, **aurora_parallel_query** is
   turned off by default.
3. If you use a custom cluster parameter group, attach it to the Aurora DB cluster where you plan to use the parallel query
   feature. If you use a custom DB parameter group, attach it to one or more DB instances in the cluster. We recommend
   using a cluster parameter group. Doing so makes sure that all DB instances in the cluster have the same settings for
   parallel query and associated features such as hash join.

## Turning on and turning off

parallel query using the CLI

You can modify the parallel query parameter by using the `modify-db-cluster-parameter-group`
or `modify-db-parameter-group` command. Choose the appropriate command depending on whether
you specify the value of `aurora_parallel_query` through a DB cluster parameter group or a
DB parameter group.

###### To turn on or turn off parallel query for a DB cluster with the CLI

- Modify the parallel query parameter by using the `modify-db-cluster-parameter-group`
  command. Use a command such as the following. Substitute the appropriate name for your own
  custom parameter group. Substitute either `ON` or `OFF` for the
  `ParameterValue` portion of the `--parameters` option.

```

`$` aws rds modify-db-cluster-parameter-group --db-cluster-parameter-group-name `cluster_param_group_name` \
  --parameters ParameterName=aurora_parallel_query,ParameterValue=ON,ApplyMethod=pending-reboot
`{
 "DBClusterParameterGroupName": "`cluster_param_group_name`"
}`

aws rds modify-db-cluster-parameter-group --db-cluster-parameter-group-name `cluster_param_group_name` \
  --parameters ParameterName=aurora_pq,ParameterValue=ON,ApplyMethod=pending-reboot
```

You can also turn on or turn off parallel query at the session level, for example through the `mysql` command line
or within a JDBC or ODBC application. To do so, use the standard methods to change a client configuration setting. For
example, the command on the standard MySQL client is `set session aurora_parallel_query = {'ON'/'OFF'}` for
Aurora MySQL.

You can also add the session-level parameter to the JDBC configuration or within your
application code to turn on or turn off parallel query dynamically.

## Overriding the parallel query optimizer

You can use the `aurora_pq_force` session variable to override the parallel query optimizer and request
parallel query for every query. We recommend that you do this only for testing purposes The following example shows how to
use `aurora_pq_force` in a session.

```
set SESSION aurora_parallel_query = ON;
set SESSION aurora_pq_force = ON;
```

To turn off the override, do the following:

```
set SESSION aurora_pq_force = OFF;
```
