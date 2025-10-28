# DB cluster parameter groups for Amazon Aurora DB clusters

Amazon Aurora DB clusters use DB cluster parameter groups. The following sections
describe configuring and managing DB cluster parameter groups.

###### Topics

- [Amazon Aurora DB cluster and DB instance
  parameters](#Aurora.Managing.ParameterGroups "#Aurora.Managing.ParameterGroups")
- [Creating a DB cluster parameter group in Amazon Aurora](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md")
- [Associating a DB cluster parameter group with a DB cluster in Amazon Aurora](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md")
- [Modifying parameters in a DB cluster parameter group in Amazon Aurora](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md")
- [Resetting parameters in a DB cluster parameter group in Amazon Aurora](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md")
- [Copying a DB cluster parameter group in Amazon Aurora](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md")
- [Listing DB cluster parameter groups in Amazon Aurora](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md")
- [Viewing parameter values for a DB cluster parameter group in Amazon Aurora](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md")
- [Deleting a DB cluster parameter group in Amazon Aurora](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md")

## Amazon Aurora DB cluster and DB instance

parameters

Aurora uses a two-level system of configuration settings:

- Parameters in a _DB cluster parameter group_ apply to every DB instance in a DB
  cluster. Your data is stored in the Aurora shared storage subsystem. Because of this, all parameters
  related to physical layout of table data must be the same for all DB instances in an Aurora cluster.
  Likewise, because Aurora DB instances are connected by replication, all the parameters for replication
  settings must be identical throughout an Aurora cluster.
- Parameters in a _DB parameter group_ apply to a single DB instance in an Aurora DB
  cluster. These parameters are related to aspects such as memory usage that you can vary across DB
  instances in the same Aurora cluster. For example, a cluster often contains DB instances with different
  AWS instance classes.

Every Aurora cluster is associated with a DB cluster parameter group. This parameter group
assigns default values for every configuration value for the corresponding DB engine.
The cluster parameter group includes defaults for both the cluster-level and instance-level
parameters. Each DB instance within a provisioned or Aurora Serverless v2 cluster inherits the settings from
that DB cluster parameter group.

Each DB instance is also associated with a DB parameter group. The values in the DB parameter
group can override default values from the cluster parameter group. For example, if one
instance in a cluster experienced issues, you might assign a custom DB parameter group to
that instance. The custom parameter group might have specific settings for parameters related
to debugging or performance tuning.

Aurora assigns default parameter groups when you create a cluster or a new DB instance, based on
the specified database engine and version. You can specify custom parameter groups instead. You create
those parameter groups yourself, and you can edit the parameter values. You can specify these custom
parameter groups at creation time. You can also modify a DB cluster or instance later to use a custom
parameter group.

For provisioned and Aurora Serverless v2 instances, any configuration values that you modify in the
DB cluster parameter group override default values in the DB parameter group. If you edit the
corresponding values in the DB parameter group, those values override the settings from the
DB cluster parameter group.

Any DB parameter settings that you modify take precedence over the DB cluster parameter
group values, even if you change the configuration parameters back to their default values. You
can see which parameters are overridden by using the [describe-db-parameters](../../../cli/latest/reference/rds/describe-db-parameters.md "../../../cli/latest/reference/rds/describe-db-parameters.md") AWS CLI
command or the [DescribeDBParameters](../APIReference/API_DescribeDBParameters.md "../APIReference/API_DescribeDBParameters.md") RDS API operation. The `Source` field contains the
value `user` if you modified that parameter. To reset one or more parameters so that
the value from the DB cluster parameter group takes precedence, use the [reset-db-parameter-group](../../../cli/latest/reference/rds/reset-db-parameter-group.md "../../../cli/latest/reference/rds/reset-db-parameter-group.md") AWS CLI
command or the [ResetDBParameterGroup](../APIReference/API_ResetDBParameterGroup.md "../APIReference/API_ResetDBParameterGroup.md") RDS API operation.

The DB cluster and DB instance parameters available to you in Aurora vary depending on database engine compatibility.

| Database engine   | Parameters                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Aurora MySQL      | See [Aurora MySQL configuration parameters](AuroraMySQL.Reference.md "AuroraMySQL.Reference.md"). For Aurora Serverless clusters, see additional details in [Working with parameter groups for Aurora Serverless v2](aurora-serverless-v2.md#aurora-serverless-v2.parameter-groups "aurora-serverless-v2.md#aurora-serverless-v2.parameter-groups") and [Parameter groups for Aurora Serverless v1](aurora-serverless-v1.md#aurora-serverless.parameter-groups "aurora-serverless-v1.md#aurora-serverless.parameter-groups").         |
| Aurora PostgreSQL | See [Amazon Aurora PostgreSQL parameters](AuroraPostgreSQL.Reference.md "AuroraPostgreSQL.Reference.md"). For Aurora Serverless clusters, see additional details in [Working with parameter groups for Aurora Serverless v2](aurora-serverless-v2.md#aurora-serverless-v2.parameter-groups "aurora-serverless-v2.md#aurora-serverless-v2.parameter-groups") and [Parameter groups for Aurora Serverless v1](aurora-serverless-v1.md#aurora-serverless.parameter-groups "aurora-serverless-v1.md#aurora-serverless.parameter-groups"). | ###### Note Aurora Serverless v1 clusters have only DB cluster parameter groups, not DB parameter groups. For Aurora Serverless v2 clusters, you make all your changes to custom parameters in the DB cluster parameter group. Aurora Serverless v2 uses both DB cluster parameter groups and DB parameter groups. With Aurora Serverless v2, you can modify almost all of the configuration parameters. Aurora Serverless v2 overrides the settings of some capacity-related configuration parameters so that your workload isn't interrupted when Aurora Serverless v2 instances scale down. To learn more about Aurora Serverless configuration settings and which settings you can modify, see [Working with parameter groups for Aurora Serverless v2](aurora-serverless-v2.md#aurora-serverless-v2.parameter-groups "aurora-serverless-v2.md#aurora-serverless-v2.parameter-groups") and [Parameter groups for Aurora Serverless v1](aurora-serverless-v1.md#aurora-serverless.parameter-groups "aurora-serverless-v1.md#aurora-serverless.parameter-groups"). |
