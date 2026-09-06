

# Scaling with MemoryDB Multi-Region
<a name="multi-Region.Scaling"></a>

As demand on your clusters changes, you might decide to improve performance or reduce costs by changing the node type or the number of shards in your MemoryDB cluster. Scaling a MemoryDB Multi-Region cluster scales all regional clusters in it. MemoryDB Multi-Region cluster supports online resharding. MemoryDB Multi-Region cluster does not support offline resharding. 

Conditions under which you might decide to rescale your cluster include the following:
+ **Memory pressure**

  If the nodes in your regional clusters are under memory pressure, you might decide to scale out or scale up so that you have more resources to better store data and serve requests. 

  You can determine whether your nodes are under memory pressure by monitoring the following metrics: FreeableMemory, SwapUsage, BytesUsedForMemoryDB, and MultiRegionClusterReplicationLag 
+ **CPU or network bottleneck**

  If latency/throughput issues are plaguing your cluster, you might need to scale out or scale up to resolve the issues.

  You can monitor your latency and throughput levels by monitoring the following metrics: `CPUUtilization`, `NetworkBytesIn`, ` NetworkBytesOut`, `CurrConnections`, ` NewConnections`, ` and MultiRegionClusterReplicationLag`. 
+ ** Your cluster is over-scaled**

  Current demand on your cluster is such that scaling in or scaling down doesn't hurt performance and reduces your costs.

You can monitor your cluster's use to determine whether or not you can safely scale in or scale down using the following metrics: FreeableMemory, SwapUsage, BytesUsedForMemoryDB, CPUUtilization, NetworkBytesIn, NetworkBytesOut, CurrConnections, NewConnections and MultiRegionClusterReplicationLag 

There are two ways to scale your MemoryDB Multi-Region cluster; horizontal and vertical scaling.
+ Horizontal scaling allows you to change the number of shards in the MemoryDB Multi-Region cluster by adding or removing shards. The online resharding process allows scaling in/out while the regional clusters continue serving incoming requests. 
+ Vertical changes the node type to resize the MemoryDB Multi-Region cluster. The online vertical scaling allows scaling up/down while the regional clusters continue serving incoming requests. 

Scaling uses the “coordinated” update strategy by default. This means that either all regional clusters successfully scale, or none of the regional clusters scale. 

The scale-out operation supports the “uncoordinated” update strategy as well. This means some regional clusters may successfully scale-out, while some regional clusters fail a scale-out attempt. If one regional cluster scale-out was successful, then all other regional clusters continue to retry scale-out until each of those other scale-outs are also successful.

A Multi-Region cluster fails an “uncoordinated” scale-out if all regional clusters fail to scale-out. 

**Note**  
An “uncoordinated” scale-out can create prolonged imbalanced capacities among regional clusters when regional clusters scale-out at different times. It can cause increase in MultiRegionClusterReplicationLag metric and regional clusters data may diverge for long time. 

MemoryDB Multi-Region cluster regional clusters can have different configurations for the number of replica nodes, but all shards in a regional cluster have same number of replica nodes. 

If you are reducing the size and memory capacity of the MemoryDB Multi-Region cluster, by either scaling in or scaling down, ensure that the new configuration has sufficient memory and free IPs for your data, sufficent engine overhead, and that the MultiRegionClusterReplicationLag metrics for regional clusters are within seconds or a minute range. 

You can horizontally and vertically scale your MemoryDB Multi-Region cluster using the AWS Management Console, the AWS CLI, and the MemoryDB API. 