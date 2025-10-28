# Scale up Amazon MSK Standard broker storage

You can increase the amount of EBS storage per broker. You can't decrease the storage.

Storage volumes remain available during this scaling-up operation.

###### Important

When storage is scaled for an MSK cluster, the additional storage is
made available right away. However, the cluster requires a cool-down period after
every storage scaling event. Amazon MSK uses this cool-down period to optimize the
cluster before it can be scaled again. This period can range from a minimum of 6
hours to over 24 hours, depending on the cluster's storage size and utilization and
on traffic. This is applicable for both auto scaling events and manual scaling using
the [UpdateBrokerStorage](../../1.0/apireference/clusters-clusterarn-nodes-storage.md#UpdateBrokerStorage "../../1.0/apireference/clusters-clusterarn-nodes-storage.md#UpdateBrokerStorage") operation. For information about right-sizing your
storage, see [Best practices for Standard brokers](bestpractices.md "bestpractices.md").

You can use tiered storage to scale up to unlimited amounts of storage for your broker.
See, [Tiered storage for Standard brokers](msk-tiered-storage.md "msk-tiered-storage.md").

###### Topics

- [Automatic scaling for Amazon MSK clusters](msk-autoexpand.md "msk-autoexpand.md")
- [Manual scaling for Standard brokers](manually-expand-storage.md "manually-expand-storage.md")
