

# DB cluster parameter groups for Amazon Aurora DB clusters
<a name="USER_WorkingWithDBClusterParamGroups"></a>

Amazon Aurora DB clusters use DB cluster parameter groups. The following sections describe configuring and managing DB cluster parameter groups.

**Topics**
+ [Amazon Aurora DB cluster and DB instance parameters](#Aurora.Managing.ParameterGroups)
+ [Creating a DB cluster parameter groupin Amazon Aurora](USER_WorkingWithParamGroups.CreatingCluster.md)
+ [Associating a DB cluster parameter group with a DB cluster in Amazon Aurora](USER_WorkingWithParamGroups.AssociatingCluster.md)
+ [Modifying parameters in a DB cluster parameter groupin Amazon Aurora](USER_WorkingWithParamGroups.ModifyingCluster.md)
+ [Resetting parameters in a DB cluster parameter groupin Amazon Aurora](USER_WorkingWithParamGroups.ResettingCluster.md)
+ [Copying a DB cluster parameter groupin Amazon Aurora](USER_WorkingWithParamGroups.CopyingCluster.md)
+ [Listing DB cluster parameter groupsin Amazon Aurora](USER_WorkingWithParamGroups.ListingCluster.md)
+ [Viewing parameter values for a DB cluster parameter groupin Amazon Aurora](USER_WorkingWithParamGroups.ViewingCluster.md)
+ [Deleting a DB cluster parameter groupin Amazon Aurora](USER_WorkingWithParamGroups.DeletingCluster.md)

## Amazon Aurora DB cluster and DB instance parameters
<a name="Aurora.Managing.ParameterGroups"></a>

 Aurora uses a two-level system of configuration settings: 
+  Parameters in a *DB cluster parameter group* apply to every DB instance in a DB cluster. Your data is stored in the Aurora shared storage subsystem. Because of this, all parameters related to physical layout of table data must be the same for all DB instances in an Aurora cluster. Likewise, because Aurora DB instances are connected by replication, all the parameters for replication settings must be identical throughout an Aurora cluster. 
+  Parameters in a *DB parameter group* apply to a single DB instance in an Aurora DB cluster. These parameters are related to aspects such as memory usage that you can vary across DB instances in the same Aurora cluster. For example, a cluster often contains DB instances with different AWS instance classes. 

 Every Aurora cluster is associated with a DB cluster parameter group. This parameter group assigns default values for every configuration value for the corresponding DB engine. The cluster parameter group includes defaults for both the cluster-level and instance-level parameters. Each DB instance within a provisioned or Aurora serverless cluster inherits the settings from that DB cluster parameter group. 

 Each DB instance is also associated with a DB parameter group. The values in the DB parameter group can override default values from the cluster parameter group. For example, if one instance in a cluster experienced issues, you might assign a custom DB parameter group to that instance. The custom parameter group might have specific settings for parameters related to debugging or performance tuning. 

 Aurora assigns default parameter groups when you create a cluster or a new DB instance, based on the specified database engine and version. You can specify custom parameter groups instead. You create those parameter groups yourself, and you can edit the parameter values. You can specify these custom parameter groups at creation time. You can also modify a DB cluster or instance later to use a custom parameter group. 

 For provisioned and Aurora serverless instances, any configuration values that you modify in the DB cluster parameter group override default values in the DB parameter group. If you edit the corresponding values in the DB parameter group, those values override the settings from the DB cluster parameter group. 

 Any DB parameter settings that you modify take precedence over the DB cluster parameter group values, even if you change the configuration parameters back to their default values. You can see which parameters are overridden by using the [describe-db-parameters](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-parameters.html) AWS CLI command or the [DescribeDBParameters](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBParameters.html) RDS API operation. The `Source` field contains the value `user` if you modified that parameter. To reset one or more parameters so that the value from the DB cluster parameter group takes precedence, use the [reset-db-parameter-group](https://docs.aws.amazon.com/cli/latest/reference/rds/reset-db-parameter-group.html) AWS CLI command or the [ResetDBParameterGroup](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ResetDBParameterGroup.html) RDS API operation. 

The DB cluster and DB instance parameters available to you in Aurora vary depending on database engine compatibility.


| Database engine | Parameters | 
| --- | --- | 
| Aurora MySQL | See [Aurora MySQL configuration parameters](AuroraMySQL.Reference.ParameterGroups.md).<br /> For Aurora Serverless clusters, see additional details in [Working with parameter groups for Aurora serverless](aurora-serverless-v2.setting-capacity.md#aurora-serverless-v2.parameter-groups).  | 
| Aurora PostgreSQL | See [Amazon Aurora PostgreSQL parameters](AuroraPostgreSQL.Reference.ParameterGroups.md).<br /> For Aurora Serverless clusters, see additional details in [Working with parameter groups for Aurora serverless](aurora-serverless-v2.setting-capacity.md#aurora-serverless-v2.parameter-groups).  | 

**Note**  
 Aurora serverless uses both DB cluster parameter groups and DB parameter groups. With Aurora serverless, you can modify almost all of the configuration parameters. Aurora serverless overrides the settings of some capacity-related configuration parameters so that your workload isn't interrupted when Aurora serverless instances scale down.   
 To learn more about Aurora Serverless configuration settings and which settings you can modify, see [Working with parameter groups for Aurora serverless](aurora-serverless-v2.setting-capacity.md#aurora-serverless-v2.parameter-groups). 