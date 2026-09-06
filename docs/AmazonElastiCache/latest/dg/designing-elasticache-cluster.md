

# Creating and managing a node-based ElastiCache cluster
<a name="designing-elasticache-cluster"></a>

If you need fine-grained control over your ElastiCache cluster, you can create a node-based cluster. ElastiCache enables you to operate a node-based cluster by choosing the node-type, number of nodes, and node placement across AWS Availability Zones for your cluster. Since ElastiCache is a fully-managed service, it automatically manages hardware provisioning, monitoring, node replacements, and software patching for your cluster.

For information on setting up see [Setting up ElastiCache](set-up.md). For details on managing, updating or deleting nodes or clusters, see [Managing nodes in ElastiCache](CacheNodes.md). For an overview of the major components of an Amazon ElastiCache deployment when you create a node-based ElastiCache cluster, see these [key concepts.](WhatIs.corecomponents.md) 

**Topics**
+ [ElastiCache components and features](WhatIs.Components.md)
+ [ElastiCache terminology](WhatIs.Terms.md)
+ [Tutorial: How to create a node-based ElastiCache cluster](SubnetGroups.designing-cluster-pre.md)
+ [Deleting a cluster](Clusters.Delete-gs.redis.md)
+ [Other ElastiCache tutorials and videos](Tutorials.md)
+ [Managing nodes in ElastiCache](CacheNodes.md)
+ [Managing clusters in ElastiCache](Clusters.md)
+ [Comparing node-based Valkey, Memcached, and Redis OSS clusters](SelectEngine.md)
+ [Online migration for Valkey or Redis OSS](OnlineMigration.md)
+ [Choosing regions and availability zones for ElastiCache](RegionsAndAZs.md)