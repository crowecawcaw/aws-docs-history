# Overview of parameter groups

A _DB parameter group_ acts as a container for engine configuration values that are
applied to one or more DB instances.

_DB cluster parameter groups_ apply to
Multi-AZ DB clusters only. In a Multi-AZ DB cluster, the settings in the DB cluster parameter group
apply to all of the DB instances in the cluster. The default DB parameter group for the DB engine and DB engine
version is used for each DB instance in the DB cluster.

###### Topics

- [Default and custom parameter
  groups](#parameter-groups-overview.custom "#parameter-groups-overview.custom")
- [Static and dynamic DB instance
  parameters](#parameter-groups-overview.db-instance "#parameter-groups-overview.db-instance")
- [Static and dynamic DB cluster
  parameters](#parameter-groups-overview.maz "#parameter-groups-overview.maz")
- [Character set parameters](#parameter-groups-overview.char-sets "#parameter-groups-overview.char-sets")
- [Supported parameters and parameter
  values](#parameter-groups-overview.supported "#parameter-groups-overview.supported")

## Default and custom parameter

groups

If you create a DB instance without specifying a DB parameter group, the DB instance uses a
default DB parameter group. Likewise, if you create a
Multi-AZ DB cluster without
specifying a DB cluster parameter group, the DB cluster uses a default DB cluster parameter group. Each
default parameter group contains database engine defaults and Amazon RDS system defaults
based on the engine, compute class, and allocated storage of the instance.

You can't modify the parameter settings of a default parameter group. Instead,
you can do the following:

1. Create a new parameter group.
2. Change the settings of your desired parameters. Not all DB engine parameters
   in a parameter group are eligible to be modified.
3. Modify your DB instance or DB cluster to associate the new parameter group.

When you associate a new DB parameter group with a DB instance, the
association happens immediately. For information about modifying a DB instance,
see [Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md"). For information about
modifying a Multi-AZ DB clusters, see [Modifying a Multi-AZ DB cluster for Amazon RDS](modify-multi-az-db-cluster.md "modify-multi-az-db-cluster.md").

###### Note

If you have modified your DB instance to use a custom parameter group, and you
start the DB instance, RDS automatically reboots the DB instance as part of the startup
process. For RDS for SQL Server Multi-AZ instances with
AlwaysOn or Mirroring option enabled, a failover is expected when instance is rebooted after the startup process.

RDS applies the modified static and dynamic parameters in a newly associated parameter
group only after the DB instance is rebooted. However, if you modify dynamic parameters in the
DB parameter group after you associate it with the DB instance, these changes are applied immediately
without a reboot. For more information about changing the DB parameter group, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md").

If you update parameters within a DB parameter group, the changes apply to all DB instances
that are associated with that parameter group. Likewise, if you update parameters within
a Multi-AZ DB cluster parameter group, the changes apply to all Aurora DB clusters that are
associated with that DB cluster parameter group.

If you don't want to create a parameter group from scratch, you can copy an existing
parameter group with the AWS CLI [copy-db-parameter-group](../../../cli/latest/reference/rds/copy-db-parameter-group.md "../../../cli/latest/reference/rds/copy-db-parameter-group.md")
command or [copy-db-cluster-parameter-group](../../../cli/latest/reference/rds/copy-db-cluster-parameter-group.md "../../../cli/latest/reference/rds/copy-db-cluster-parameter-group.md") command. You might find that copying a
parameter group is useful in some cases. For example, you might want to include most of
an existing DB parameter group's custom
parameters and values in a new DB parameter
group.

## Static and dynamic DB instance

parameters

DB instance parameters are either static or dynamic. They differ as follows:

- When you change a static parameter and save the DB parameter group, the
  parameter change takes effect after you manually reboot the associated DB instances.
  For static parameters, the console always uses `pending-reboot` for
  the `ApplyMethod`.
- When you change a dynamic parameter, by default the parameter change takes effect
  immediately, without requiring a reboot. When you use the AWS Management Console to change
  DB instance parameter values, it always uses `immediate` for the
  `ApplyMethod` for dynamic parameters. To defer the parameter
  change until after you reboot an associated DB instance, use the AWS CLI or RDS API. Set
  the `ApplyMethod` to `pending-reboot` for the parameter
  change.

###### Note

Using `pending-reboot` with dynamic parameters in the AWS CLI or
RDS API on RDS for SQL Server DB instances generates an error. Use
`apply-immediately` on RDS for SQL Server.

For more information about using the AWS CLI to change a parameter value, see [modify-db-parameter-group](../../../cli/latest/reference/rds/modify-db-parameter-group.md "../../../cli/latest/reference/rds/modify-db-parameter-group.md"). For more information about using the RDS API to
change a parameter value, see [ModifyDBParameterGroup](../APIReference/API_ModifyDBParameterGroup.md "../APIReference/API_ModifyDBParameterGroup.md").

If a DB instance isn't using the latest changes to its associated DB parameter group, the console shows a
status of **pending-reboot** for the DB parameter group. This status doesn't
result in an automatic reboot during the next maintenance window. To apply the latest
parameter changes to that DB instance, manually reboot the DB instance.

## Static and dynamic DB cluster

parameters

DB cluster parameters are either static or dynamic. They differ as follows:

- When you change a static parameter and save the DB cluster parameter group, the
  parameter change takes effect after you manually reboot the associated DB clusters.
  For static parameters, the console always uses `pending-reboot` for
  the `ApplyMethod`.
- When you change a dynamic parameter, by default the parameter change takes
  effect immediately, without requiring a reboot. When you use the AWS Management Console to
  change DB cluster parameter values, it always uses `immediate` for the
  `ApplyMethod` for dynamic parameters. To defer the parameter
  change until after an associated DB cluster is rebooted, use the AWS CLI or RDS API.
  Set the `ApplyMethod` to `pending-reboot` for the
  parameter change.

For more information about using the AWS CLI to change a parameter value, see [modify-db-cluster-parameter-group](../../../cli/latest/reference/rds/modify-db-cluster-parameter-group.md "../../../cli/latest/reference/rds/modify-db-cluster-parameter-group.md"). For more information about using the RDS
API to change a parameter value, see [ModifyDBClusterParameterGroup](../APIReference/API_ModifyDBClusterParameterGroup.md "../APIReference/API_ModifyDBClusterParameterGroup.md").

## Character set parameters

Before you create a DB instance or Multi-AZ DB
cluster, set any parameters that
relate to the character set or collation of your database in your parameter group. Also
do so before you create a database in it. In this way, you ensure that the default
database and new databases use the character set and collation values that you specify.
If you change character set or collation parameters, the parameter changes aren't
applied to existing databases.

For some DB engines, you can change character set or collation values for an existing
database using the `ALTER DATABASE` command, for example:

```
ALTER DATABASE `database_name` CHARACTER SET `character_set_name` COLLATE `collation`;

```

For more information about changing the character set or collation values for a
database, check the documentation for your DB engine.

## Supported parameters and parameter

values

To determine the supported parameters for your DB engine, view the parameters in the
DB parameter group and DB cluster parameter group used by the DB instance or DB cluster. For more
information, see [Viewing parameter values for a
DB parameter group in Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md") and [Viewing parameter values for a DB cluster parameter group](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

In many cases, you can specify integer and Boolean parameter values using expressions,
formulas, and functions. Functions can include a mathematical log expression. However,
not all parameters support expressions, formulas, and functions for parameter values.
For more information, see [Specifying DB parameters](USER_ParamValuesRef.md "USER_ParamValuesRef.md").

Improperly setting parameters in a parameter group can have unintended adverse
effects, including degraded performance and system instability. Always be cautious when
modifying database parameters, and back up your data before modifying a parameter group.
Try parameter group setting changes on a test DB instance or DB cluster before applying those
parameter group changes to a production DB instance or DB cluster.
