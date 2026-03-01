# Parameter management in ElastiCache

ElastiCache parameters are grouped together into named parameter groups for easier parameter
management. A parameter group represents a combination of specific values for the
parameters that are passed to the engine software during startup. These values determine
how the engine processes on each node behave at runtime. The parameter values on a
specific parameter group apply to all nodes that are associated with the group,
regardless of which cluster they belong to.

To fine-tune your cluster's performance, you can modify some parameter values or
change the cluster's parameter group.

- You cannot modify or delete the default parameter groups. If you need custom
  parameter values, you must create a custom parameter group.
- For Memcached, the parameter group family and the cluster you're
  assigning it to must be compatible. For example, if your cluster is running
  Memcached version 1.4.8, you can only use parameter groups, default or custom,
  from the Memcached 1.4 family.

For Redis OSS, the parameter group family and the cluster you're
assigning it to must be compatible. For example, if your cluster is running
Redis OSS version 3.2.10, you can only use parameter groups, default or custom, from
the Redis OSS 3.2 family.

- If you change a cluster's parameter group, the values for any
  conditionally modifiable parameter must be the same in both the current and new
  parameter groups.
- For Memcached, when you change a cluster's parameters the change is applied to the
  cluster immediately. This is true whether you change the cluster's
  parameter group itself or a parameter value within the cluster's parameter
  group. To determine when a particular parameter change is applied, see the
  **Changes Take Effect** column in the tables
  for [Memcached specific parameters](ParameterGroups.md#ParameterGroups.Memcached "ParameterGroups.md#ParameterGroups.Memcached"). For information on rebooting a
  cluster's nodes, see [Rebooting clusters](Clusters.md#Rebooting "Clusters.md#Rebooting").
- For Redis OSS, when you change a cluster's parameters, the change is applied to the
  cluster either immediately or, with the exceptions noted following, after the
  cluster nodes are rebooted. This is true whether you change the cluster's
  parameter group itself or a parameter value within the cluster's parameter
  group. To determine when a particular parameter change is applied, see the
  **Changes Take Effect** column in the tables
  for [Valkey and Redis OSS parameters](ParameterGroups.md#ParameterGroups.Redis "ParameterGroups.md#ParameterGroups.Redis").

For more information on rebooting Valkey or Redis OSS nodes, see [Rebooting nodes](nodes.md "nodes.md").

###### Valkey or Redis OSS (Cluster Mode Enabled) parameter changes

If you make changes to the following parameters on a Valkey or Redis OSS (cluster mode enabled)
cluster, follow the ensuing steps.

    + activerehashing
    + databases
    1. Create a manual backup of your cluster. See [Taking manual backups](backups-manual.md "backups-manual.md").
    2. Delete the cluster. See [Deleting clusters](Clusters.md#Delete "Clusters.md#Delete").
    3. store the cluster using the altered parameter group and backup
     to seed the new cluster. See [Restoring from a backup into a new cache](backups-restoring.md "backups-restoring.md").Changes to other parameters do not require this.

- You can associate parameter groups with Valkey and Redis OSS global datastores. _Global datastores_ are a collection of one or more
  clusters that span AWS Regions. In this case, the parameter group is shared by
  all clusters that make up the global datastore. Any modifications to the
  parameter group of the primary cluster are replicated to all remaining clusters
  in the global datastore. For more information, see [Replication across AWS Regions using global datastores](Redis-Global-Datastore.md "Redis-Global-Datastore.md").

You can check if a parameter group is part of a global datastore by looking in
these locations:

    + On the ElastiCache console on the **Parameter Groups**
     page, the yes/no **Global** attribute
    + The yes/no `IsGlobal` property of the [CacheParameterGroup](../APIReference/API_CacheParameterGroup.md "../APIReference/API_CacheParameterGroup.md") API operation
