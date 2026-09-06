

# Minimizing downtime in MemoryDB with Multi-AZ
<a name="autofailover"></a>

There are a number of instances where MemoryDB may need to replace a primary node; these include certain types of planned maintenance and the unlikely event of a primary node or Availability Zone failure. 

The response to node failure depends on which node has failed. However, in all cases, MemoryDB ensures that no data is lost during node replacements or failover. For example, if a replica fails, the failed node is replaced and data is synced from the transaction log. If the primary node fails, a failover is triggered to a consistent replica which ensures no data is lost during failover. The writes are now served from the new primary node. The old primary node is then replaced and synced from the transaction log. 

If a primary node fails on a single node shard (no replicas), MemoryDB stops accepting writes until the primary node is replaced and synced from the transaction log. 

Node replacement may result in some downtime for the cluster, but if Multi-AZ is active, the downtime is minimized. The role of primary node will automatically fail over to one of the replicas. There is no need to create and provision a new primary node, because MemoryDB will handle this transparently. This failover and replica promotion ensure that you can resume writing to the new primary as soon as promotion is complete. 

In case of planned node replacements initiated due to maintenance updates or service updates, be aware the planned node replacements complete while the cluster serves incoming write requests. 

Multi-AZ on your MemoryDB clusters improves your fault tolerance. This is true particularly in cases where your cluster's primary nodes become unreachable or fail for any reason. Multi-AZ on MemoryDB clusters requires each shard to have more than one node, and is automatically enabled.

**Topics**
+ [Failure scenarios with Multi-AZ responses](#autofailover.scenarios)
+ [Testing automatic failover](#auto-failover-test)

## Failure scenarios with Multi-AZ responses
<a name="autofailover.scenarios"></a>

If Multi-AZ is active, a failed primary node fails over to an available replica. The replica is automatically synchronized with the transaction log and becomes primary, which is much faster than creating and reprovisioning a new primary node. This process usually takes just a few seconds until you can write to the cluster again.

When Multi-AZ is active, MemoryDB continually monitors the state of the primary node. If the primary node fails, one of the following actions is performed depending on the type of failure.

**Topics**
+ [Failure scenarios when only the primary node fails](#autofailover.scenarios.primaryonly)
+ [Failure scenarios when the primary node and some replicas fail](#autofailover.scenarios.primaryandeplicas)
+ [Failure scenarios when the entire cluster fails](#autofailover.scenarios.allfail)

### Failure scenarios when only the primary node fails
<a name="autofailover.scenarios.primaryonly"></a>

If only the primary node fails, a replica will automatically become primary. A replacement replica is then created and provisioned in the same Availability Zone as the failed primary.

When only the primary node fails, MemoryDB Multi-AZ does the following:

1. The failed primary node is taken offline.

1. An up-to-date replica automatically become primary.

   Writes can resume as soon as the failover process is complete, typically just a few seconds. 

1. A replacement replica is launched and provisioned.

   The replacement replica is launched in the Availability Zone that the failed primary node was in so that the distribution of nodes is maintained.

1. The replica syncs with the transaction log.

For information about finding the endpoints of a cluster, see the following topics:
+ [Finding the Endpoint for a MemoryDB Cluster (MemoryDB API)](endpoints.md#endpoints.find.api.clusters)

 

### Failure scenarios when the primary node and some replicas fail
<a name="autofailover.scenarios.primaryandeplicas"></a>

If the primary and at least one replica fails, an up-to-date replica is promoted to primary cluster. New replicas are also created and provisioned in the same Availability Zones as the failed nodes.

When the primary node and some replicas fail, MemoryDB Multi-AZ does the following:

1. The failed primary node and failed replicas are taken offline.

1. An available replica will become the primary node.

   Writes can resume as soon as the failover is complete, typically just a few seconds. 

1. Replacement replicas are created and provisioned.

   The replacement replicas are created in the Availability Zones of the failed nodes so that the distribution of nodes is maintained.

1. All nodes sync with the transaction log.

For information about finding the endpoints of a cluster, see the following topics:
+ [Finding the Endpoint for a MemoryDB Cluster (AWS CLI)](endpoints.md#endpoints.find.cli)
+ [Finding the Endpoint for a MemoryDB Cluster (MemoryDB API)](endpoints.md#endpoints.find.api.clusters)

 

### Failure scenarios when the entire cluster fails
<a name="autofailover.scenarios.allfail"></a>

If everything fails, all the nodes are recreated and provisioned in the same Availability Zones as the original nodes. 

There is no data loss in this scenario as the data was persisted in the transaction log. 

When the entire cluster fails, MemoryDB Multi-AZ does the following:

1. The failed primary node and replicas are taken offline.

1. A replacement primary node is created and provisioned, syncing with the transaction log.

1. Replacement replicas are created and provisioned, syncing with the transaction log.

   The replacements are created in the Availability Zones of the failed nodes so that the distribution of nodes is maintained.

For information about finding the endpoints of a cluster, see the following topics:
+ [Finding the Endpoint for a MemoryDB Cluster (AWS CLI)](endpoints.md#endpoints.find.cli)
+ [Finding the Endpoint for a MemoryDB Cluster (MemoryDB API)](endpoints.md#endpoints.find.api.clusters)

## Testing automatic failover
<a name="auto-failover-test"></a>

You can test automatic failover using the MemoryDB console, the AWS CLI, and the MemoryDB API.

When testing, note the following:
+ You can use this operation up to five times in any 24-hour period.
+ If you call this operation on shards in different clusters, you can make the calls concurrently.
+ In some cases, you might call this operation multiple times on different shards in the same MemoryDB cluster. In such cases, the first node replacement must complete before a subsequent call can be made.
+ To determine whether the node replacement is complete, check events using the MemoryDB console, the AWS CLI, or the MemoryDB API. Look for the following events related to `FailoverShard`, listed here in order of likely occurrence:

  1. cluster message: `FailoverShard API called for shard <shard-id>`

  1. cluster message: `Failover from primary node <primary-node-id> to replica node <node-id> completed`

  1. cluster message: `Recovering nodes <node-id>`

  1. cluster message: `Finished recovery for nodes <node-id>`

  For more information, see the following:
  + [DescribeEvents](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DescribeEvents.html) in the *MemoryDB API Reference*
+ This API is designed for testing the behavior of your application in case of MemoryDB failover. It is not designed to be an operational tool for initiating a failover to address an issue with the cluster. Moreover, in certain conditions such as large-scale operational events, AWS may block this API.

**Topics**
+ [Testing automatic failover using the AWS Management Console](#auto-failover-test-con)
+ [Testing automatic failover using the AWS CLI](#auto-failover-test-cli)
+ [Testing automatic failover using the MemoryDB API](#failovershard-test-api)

### Testing automatic failover using the AWS Management Console
<a name="auto-failover-test-con"></a>

Use the following procedure to test automatic failover with the console.

1. Sign in to the AWS Management Console and open the MemoryDB console at [https://console.aws.amazon.com/memorydb/](https://console.aws.amazon.com/memorydb/).

1. Choose the radio button to the left of the cluster you want to test. This cluster must have at least one replica node.

1. In the **Details** area, confirm that this cluster is Multi-AZ enabled. If the cluster isn't Multi-AZ enabled, either choose a different cluster or modify this cluster to enable Multi-AZ. For more information, see [Modifying a MemoryDB cluster](clusters.modify.md).

1. Choose the cluster's name.

1. On the **Shards and nodes** page, for the shard on which you want to test failover, choose the shard's name. 

1. For the node, choose **Failover Primary**.

1. Choose **Continue** to fail over the primary, or **Cancel** to cancel the operation and not fail over the primary node.

   During the failover process, the console continues to show the node's status as *available*. To track the progress of your failover test, choose **Events** from the console navigation pane. On the **Events** tab, watch for events that indicate your failover has started (`FailoverShard API called`) and completed (`Recovery completed`).

 

### Testing automatic failover using the AWS CLI
<a name="auto-failover-test-cli"></a>

You can test automatic failover on any Multi-AZ enabled cluster using the AWS CLI operation [failover-shard](https://docs.aws.amazon.com/cli/latest/reference/memorydb/failover-shard.html).

**Parameters**
+ `--cluster-name` – Required. The cluster that is to be tested.
+ `--shard-name` – Required. The name of the shard you want to test automatic failover on. You can test a maximum of five shards in a rolling 24-hour period.

The following example uses the AWS CLI to call `failover-shard` on the shard `0001` in the MemoryDB cluster `my-cluster`.

For Linux, macOS, or Unix:

```
aws memorydb failover-shard \
   --cluster-name {{my-cluster}} \
   --shard-name {{0001}}
```

For Windows:

```
aws memorydb failover-shard ^
   --cluster-name {{my-cluster}} ^
   --shard-name {{0001}}
```

To track the progress of your failover, use the AWS CLI `describe-events` operation.

It will return the following JSON response:

```
{
    "Events": [
        {
            "SourceName": "my-cluster",
            "SourceType": "cluster",
            "Message": "Failover to replica node my-cluster-0001-002 completed",
            "Date": "2021-08-22T12:39:37.568000-07:00"
        },
        {
            "SourceName": "my-cluster",
            "SourceType": "cluster",
            "Message": "Starting failover for shard 0001",
            "Date": "2021-08-22T12:39:10.173000-07:00"
        }
    ]
}
```

For more information, see the following:
+ [failover-shard](https://docs.aws.amazon.com/cli/latest/reference/memorydb/failover-shard.html)
+ [describe-events](https://docs.aws.amazon.com/cli/latest/reference/memorydb/describe-events.html)

 

### Testing automatic failover using the MemoryDB API
<a name="failovershard-test-api"></a>

The following example calls `FailoverShard` on the shard `0003` in the cluster `memorydb00`.

**Example Testing automatic failover**  

```
https://memory-db.us-east-1.amazonaws.com/
    ?Action=FailoverShard
    &ShardName=0003
    &ClusterName=memorydb00
    &Version=2021-01-01
    &SignatureVersion=4
    &SignatureMethod=HmacSHA256
    &Timestamp=20210801T192317Z
    &X-Amz-Credential=<credential>
```

To track the progress of your failover, use the MemoryDB `DescribeEvents` API operation.

For more information, see the following:
+ [FailoverShard](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_FailoverShard.html) 
+ [DescribeEvents](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DescribeEvents.html) 