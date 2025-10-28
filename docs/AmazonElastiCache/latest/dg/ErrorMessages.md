# Amazon ElastiCache error messages

The following error messages are returned by Amazon ElastiCache.
You may receive other error messages that are returned by ElastiCache, other AWS services, or by Valkey, Memcached, or Redis OSS.
For descriptions of error messages from sources other than ElastiCache, see the documentation from the source that
is generating the error message.

- [Cluster node quota exceeded](#ErrorMessages.ClusterNodeQuota "#ErrorMessages.ClusterNodeQuota")
- [Customer's node quota exceeded](#ErrorMessages.CACHE_CLUSTER_CUSTOMER_QUOTA_EXCEEDED "#ErrorMessages.CACHE_CLUSTER_CUSTOMER_QUOTA_EXCEEDED")
- [Manual snapshot quota exceeded](#ErrorMessages.MANUAL_SNAPSHOT_WITHIN_24_HOURS_QUOTA_EXCEEDED "#ErrorMessages.MANUAL_SNAPSHOT_WITHIN_24_HOURS_QUOTA_EXCEEDED")
- [Insufficient cluster capacity](#ErrorMessages.INSUFFICIENT_CACHE_CLUSTER_CAPACITY "#ErrorMessages.INSUFFICIENT_CACHE_CLUSTER_CAPACITY")

Error Message:
**Cluster node quota exceeded.
Each cluster can have at most _%n_ nodes in this region.**

**Cause:**
You attempted to create or modify a cluster with the result that the
cluster would have more than _%n_ nodes.

**Solution:**
Change your request so that the cluster does not have more than _%n_ nodes.
Or, if you need more than _%n_ nodes, make your request using the [Amazon ElastiCache Node request form](https://aws.amazon.com/contact-us/elasticache-node-limit-request/ "https://aws.amazon.com/contact-us/elasticache-node-limit-request/").

For more information, see [Amazon ElastiCache Limits](../../../general/latest/gr/aws_service_limits.md#limits_elasticache "../../../general/latest/gr/aws_service_limits.md#limits_elasticache") in _Amazon Web Services General Reference_.

 

Error Messages:
**Customer node quota exceeded.
You can have at most _%n_ nodes in this region**

Or, **You have already reached your quota of %s nodes in this region.**

**Cause:**
You attempted to create or modify a cluster with the result that your
account would have more than _%n_ nodes across all clusters in this region.

**Solution:**
Change your request so that the total nodes in the region across all clusters
for this account does not exceed _%n_.
Or, if you need more than _%n_ nodes, make your request using the [Amazon ElastiCache Node request form](https://aws.amazon.com/contact-us/elasticache-node-limit-request/ "https://aws.amazon.com/contact-us/elasticache-node-limit-request/").

For more information, see [Amazon ElastiCache Limits](../../../general/latest/gr/aws_service_limits.md#limits_elasticache "../../../general/latest/gr/aws_service_limits.md#limits_elasticache") in _Amazon Web Services General Reference_.

 

Error Messages:
**The maximum number of manual snapshots for this cluster taken within 24 hours has been reached**

or **The maximum number of manual snapshots for this node taken within 24 hours has been reached its quota of _%n_**

**Cause:**
You attempted to take a manual snapshot of a cluster when you have already taken the maximum
number of manual snapshots allowed in a 24-hour period.

**Solution:**
Wait 24 hours to attempt another manual snapshot of the cluster.
Or, if you need to take a manual snapshot now, take the snapshot of another node
that has the same data, such as a different node in a cluster.

 

Error Messages:
**InsufficientCacheClusterCapacity**

**Cause:**
AWS does not currently have enough available On-Demand capacity to service your request.

**Solution:**

- Wait a few minutes and then submit your request again; capacity can shift frequently.
- Submit a new request with a reduced number of nodes or shards (node groups). For example, if you're
  making a single request to launch 15 nodes, try making 3 requests of 5 nodes, or 15 requests for
  1 node instead.
- If you're launching a cluster, submit a new request without specifying an Availability Zone.
- If you're launching a cluster, submit a new request using a different node type (which you can scale up at
  a later stage). For more information, see [Scaling ElastiCache](Scaling.md "Scaling.md").
