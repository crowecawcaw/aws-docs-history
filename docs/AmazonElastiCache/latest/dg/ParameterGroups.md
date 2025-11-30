# Modifying an ElastiCache parameter group

###### Important

You cannot modify any default parameter group.

You can modify some parameter values in a parameter group. These
parameter values are applied to clusters associated with the parameter group. For more
information on when a parameter value change is applied to a parameter group, see [Valkey and Redis OSS parameters](ParameterGroups.md#ParameterGroups.Redis "ParameterGroups.md#ParameterGroups.Redis") and [Memcached specific parameters](ParameterGroups.md#ParameterGroups.Memcached "ParameterGroups.md#ParameterGroups.Memcached").

## Modifying a parameter group

(Console)

The following procedure shows how to change the
`cluster-enabled` parameter's value using the ElastiCache console. You
would use the same procedure to change the value of any parameter.

###### To change a parameter's value using the ElastiCache console

1. Sign in to the AWS Management Console and open the ElastiCache console at
   [https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/ "https://console.aws.amazon.com/elasticache/").
2. To see a list of all available parameter groups, in the left hand
   navigation pane choose **Parameter Groups**.
3. Choose the parameter group you want to modify by choosing the box to the
   left of the parameter group's name.

The parameter group's parameters will be listed at the bottom of the
screen. You may need to page through the list to see all the
parameters. 4. To modify one or more parameters, choose **Edit
Parameters**. 5. In the **Edit Parameter Group:** screen, scroll using the
left and right arrows until you find the `binding_protocol`
parameter, then type `ascii` in the **Value**
column. 6. Choose **Save Changes**. 7. For Memcached, to find the name of the parameter you changed, see [Memcached specific parameters](ParameterGroups.md#ParameterGroups.Memcached "ParameterGroups.md#ParameterGroups.Memcached"). If changes to the parameter
take place _After restart_, reboot every cluster that
uses this parameter group. For more information, see [Rebooting clusters](Clusters.md#Rebooting "Clusters.md#Rebooting"). 8. With Valkey and Redis OSS, to find the name of the parameter you changed, see [Valkey and Redis OSS parameters](ParameterGroups.md#ParameterGroups.Redis "ParameterGroups.md#ParameterGroups.Redis").
If you have a Valkey or Redis OSS (cluster mode disabled) cluster and make changes to the following
parameters, you must reboot the nodes in the cluster:

    * activerehashing
    * databases

For more information, see [Rebooting
nodes](nodes.md "nodes.md").

###### Valkey or Redis OSS (Cluster Mode Enabled) parameter changes

If you make changes to the following parameters on a Valkey or Redis OSS (cluster mode enabled)
cluster, follow the ensuing steps.

    * activerehashing
    * databases
    1. With Redis OSS, you can reate a manual backup of your cluster. See [Taking manual backups](backups-manual.md "backups-manual.md").
    2. Delete the cluster. See [Deleting clusters](Clusters.md#Delete "Clusters.md#Delete").
    3. Restore the cluster using the altered parameter group and
     backup to seed the new cluster. See [Restoring from a backup into a new cache](backups-restoring.md "backups-restoring.md").Changes to other parameters do not require this.

## Modifying a parameter group

(AWS CLI)

To change a parameter's value using the AWS CLI, use the command
`modify-cache-parameter-group`.

With Memcached, to find the name and permitted values of the parameter you want to change, see
[Memcached specific parameters](ParameterGroups.md#ParameterGroups.Memcached "ParameterGroups.md#ParameterGroups.Memcached")

The following sample code sets the value of two parameters,
_chunk_size_ and
_chunk_size_growth_fact_ on the parameter group
`myMem14`.

For Linux, macOS, or Unix:

```
aws elasticache modify-cache-parameter-group \
    --cache-parameter-group-name `myMem14` \
    --parameter-name-values \
        ParameterName=`chunk_size`,ParameterValue=`96` \
        ParameterName=`chunk_size_growth_fact`,ParameterValue=`1.5`
```

For Windows:

```
aws elasticache modify-cache-parameter-group ^
    --cache-parameter-group-name `myMem14` ^
    --parameter-name-values ^
        ParameterName=`chunk_size`,ParameterValue=`96` ^
        ParameterName=`chunk_size_growth_fact`,ParameterValue=`1.5`
```

Output from this command will look something like this.

```
{
    "CacheParameterGroupName": "myMem14"
}
```

With Valkey and Redis OSS, to find the name and permitted values of the parameter you want to change, see
[Valkey and Redis OSS parameters](ParameterGroups.md#ParameterGroups.Redis "ParameterGroups.md#ParameterGroups.Redis")

The following sample code sets the value of two parameters,
_reserved-memory-percent_ and
_cluster-enabled_ on the parameter group
`myredis32-on-30`. We set
_reserved-memory-percent_ to `30` (30 percent)
and _cluster-enabled_ to `yes` so that the
parameter group can be used with Valkey or Redis OSS (cluster mode enabled) clusters (replication
groups).

For Linux, macOS, or Unix:

```
aws elasticache modify-cache-parameter-group \
    --cache-parameter-group-name `myredis32-on-30` \
    --parameter-name-values \
        ParameterName=`reserved-memory-percent`,ParameterValue=`30` \
        ParameterName=`cluster-enabled`,ParameterValue=`yes`
```

For Windows:

```
aws elasticache modify-cache-parameter-group ^
    --cache-parameter-group-name `myredis32-on-30` ^
    --parameter-name-values ^
        ParameterName=`reserved-memory-percent`,ParameterValue=`30` ^
        ParameterName=`cluster-enabled`,ParameterValue=`yes`
```

Output from this command will look something like this.

```
{
    "CacheParameterGroupName": "my-redis32-on-30"
}
```

For more information, see [`modify-cache-parameter-group`](../../../cli/latest/reference/elasticache/modify-cache-parameter-group.md "../../../cli/latest/reference/elasticache/modify-cache-parameter-group.md").

To find the name of the parameter you changed, see [Valkey and Redis OSS parameters](ParameterGroups.md#ParameterGroups.Redis "ParameterGroups.md#ParameterGroups.Redis").

If you have a Valkey or Redis OSS (cluster mode disabled) cluster and make changes to the
following parameters, you must reboot the nodes in the cluster:

- activerehashing
- databases

For more information, see [Rebooting
nodes](nodes.md "nodes.md").

###### Valkey or Redis OSS (Cluster Mode Enabled) parameter changes

If you make changes to the following parameters on a Valkey or Redis OSS (cluster mode enabled) cluster,
follow the ensuing steps.

- activerehashing
- databases

1. Create a manual backup of your cluster. See [Taking manual backups](backups-manual.md "backups-manual.md").
2. Delete the cluster. See [Deleting clusters](Clusters.md#Delete "Clusters.md#Delete").
3. Restore the cluster using the altered parameter group and backup to
   seed the new cluster. See [Restoring from a backup into a new cache](backups-restoring.md "backups-restoring.md").
   Changes to other parameters do not require this.

## Modifying a parameter group

(ElastiCache API)

To change a parameter group's parameter values using the ElastiCache API, use the
`ModifyCacheParameterGroup` action.

With Memcached, to find the name and permitted values of the parameter you want to change, see
[Memcached specific parameters](ParameterGroups.md#ParameterGroups.Memcached "ParameterGroups.md#ParameterGroups.Memcached")

The following sample code sets the value of two parameters,
_chunk_size_ and
_chunk_size_growth_fact_ on the parameter group
`myMem14`.

```
https://elasticache.us-west-2.amazonaws.com/
   ?Action=ModifyCacheParameterGroup
   &CacheParameterGroupName=`myMem14`
   &ParameterNameValues.member.1.ParameterName=`chunk_size`
   &ParameterNameValues.member.1.ParameterValue=`96`
   &ParameterNameValues.member.2.ParameterName=`chunk_size_growth_fact`
   &ParameterNameValues.member.2.ParameterValue=`1.5`
   &SignatureVersion=4
   &SignatureMethod=HmacSHA256
   &Timestamp=20150202T192317Z
   &Version=2015-02-02
   &X-Amz-Credential=<credential>
```

With Valkey and Redis OSS, to find the name and permitted values of the parameter you want to change, see
[Valkey and Redis OSS parameters](ParameterGroups.md#ParameterGroups.Redis "ParameterGroups.md#ParameterGroups.Redis")

The following sample code sets the value of two parameters,
_reserved-memory-percent_ and
_cluster-enabled_ on the parameter group
`myredis32-on-30`. We set
_reserved-memory-percent_ to `30` (30 percent)
and _cluster-enabled_ to `yes` so that the
parameter group can be used with Valkey or Redis OSS (cluster mode enabled) clusters (replication
groups).

```
https://elasticache.us-west-2.amazonaws.com/
   ?Action=ModifyCacheParameterGroup
   &CacheParameterGroupName=`myredis32-on-30`
   &ParameterNameValues.member.1.ParameterName=`reserved-memory-percent`
   &ParameterNameValues.member.1.ParameterValue=`30`
   &ParameterNameValues.member.2.ParameterName=`cluster-enabled`
   &ParameterNameValues.member.2.ParameterValue=`yes`
   &SignatureVersion=4
   &SignatureMethod=HmacSHA256
   &Timestamp=20150202T192317Z
   &Version=2015-02-02
   &X-Amz-Credential=<credential>
```

For more information, see [`ModifyCacheParameterGroup`](../APIReference/API_ModifyCacheParameterGroup.md "../APIReference/API_ModifyCacheParameterGroup.md").

If you have a Valkey or Redis OSS (cluster mode disabled) cluster and make changes to the
following parameters, you must reboot the nodes in the cluster:

- activerehashing
- databases

For more information, see [Rebooting nodes](nodes.md "nodes.md").

###### Valkey or Redis OSS (Cluster Mode Enabled) parameter changes

If you make changes to the following parameters on a Valkey or Redis OSS (cluster mode enabled) cluster,
follow the ensuing steps.

- activerehashing
- databases

1. Create a manual backup of your cluster. See [Taking manual backups](backups-manual.md "backups-manual.md").
2. Delete the cluster. See [Deleting a cluster in ElastiCache](Clusters.md "Clusters.md").
3. Restore the cluster using the altered parameter group and backup to
   seed the new cluster. See [Restoring from a backup into a new cache](backups-restoring.md "backups-restoring.md").
   Changes to other parameters do not require this.
