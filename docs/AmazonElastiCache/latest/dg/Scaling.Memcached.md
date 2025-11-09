# Manual scaling for Memcached clusters

Manually horizontally scaling a Memcached cluster in or out is as easy as adding or removing nodes from the cluster. Memcached clusters are composed of 1 to 60 nodes.

Because you can partition your data across all the nodes in a Memcached cluster, scaling up
to a node type with greater memory is seldom required. However, because the Memcached
engine does not persist data, if you do scale to a different node type then your new cluster
starts out empty unless your application populates it.

To manually vertically scale your Memcached cluster, you must create a new cluster. Memcached
clusters always start out empty unless your application populates it.

| Manually scaling Memcached clusters | Action                                                                                                                     | Topic |
| ----------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ----- |
| Scaling out                         | [Adding nodes to a cluster](Clusters.md#AddNode "Clusters.md#AddNode")                                                     |
| Scaling in                          | [Deleting nodes from a cluster](Clusters.md#DeleteNode "Clusters.md#DeleteNode")                                           |
| Changing node types                 | [Manually scaling node-based Memcached clusters vertically](#Scaling.Memcached.Vertically "#Scaling.Memcached.Vertically") |

###### Topics

- [Manually scaling a node-based Memcached cluster horizontally](#Scaling.Memcached.Horizontally "#Scaling.Memcached.Horizontally")
- [Manually scaling node-based Memcached clusters vertically](#Scaling.Memcached.Vertically "#Scaling.Memcached.Vertically")

## Manually scaling a node-based Memcached cluster horizontally

The Memcached engine supports partitioning your data across multiple nodes.
Because of this, Memcached clusters scale horizontally easily.
To horizontally scale your Memcached cluster, merely add or remove nodes.

The following topics detail how to scale your Memcached cluster out or in by adding or removing nodes.

- [Adding nodes to a cluster](Clusters.md#AddNode "Clusters.md#AddNode")
- [Deleting nodes from your cluster](Clusters.md#AddNode "Clusters.md#AddNode")

Each time you change the number of nodes in your Memcached cluster,
you must re-map at least some of your keyspace so it maps to the correct node.
For more detailed information on load balancing your Memcached cluster, see [Configuring your ElastiCache client for efficient load balancing (Memcached)](BestPractices.md "BestPractices.md").

If you use auto discovery on your Memcached cluster, you do not need to change the
endpoints in your application as you add or remove nodes. For more information on
auto discovery, see [Automatically identify nodes in your cluster (Memcached)](AutoDiscovery.md "AutoDiscovery.md")
If you do not use auto discovery, each time you change the number of nodes in your
Memcached cluster you must update the endpoints in your application.

## Manually scaling node-based Memcached clusters vertically

When you manually scale your Memcached cluster up or down, you must create a new cluster. Memcached
clusters always start out empty unless your application populates it.

###### Important

If you are scaling down to a smaller node type,
be sure that the smaller node type is adequate for your data and overhead.
For more information, see [Choosing your node size](CacheNodes.md "CacheNodes.md").

###### Topics

- [Scaling a node-based Memcached cluster vertically (Console)](#Scaling.Memcached.Vertically.CON "#Scaling.Memcached.Vertically.CON")
- [Scaling a node-based Memcached cluster vertically (AWS CLI)](#Scaling.Memcached.Vertically.CLI "#Scaling.Memcached.Vertically.CLI")
- [Scaling a node-based Memcached cluster vertically (ElastiCache API)](#Scaling.Memcached.Vertically.API "#Scaling.Memcached.Vertically.API")

### Scaling a node-based Memcached cluster vertically (Console)

The following procedure walks you through scaling a node-based Memcached cluster vertically using the AWS Management Console.

1. Create a new cluster with the new node type.
   For more information, see [Creating a Memcached cluster (console)](Clusters.md#Clusters.Create.CON.Memcached "Clusters.md#Clusters.Create.CON.Memcached").
2. In your application, update the endpoints to the new cluster's endpoints.
   For more information, see [Finding a Cluster's Endpoints (Console) (Memcached)](Endpoints.md#Endpoints.Find.Memcached "Endpoints.md#Endpoints.Find.Memcached").
3. Delete the old cluster. For more information, see [Deleting a new node in Memcached](Clusters.md#Delete.CON.Memcached "Clusters.md#Delete.CON.Memcached").

### Scaling a node-based Memcached cluster vertically (AWS CLI)

The following procedure walks you through scaling a node-based Memcached cluster vertically using the AWS CLI.

1. Create a new cluster with the new node type.
   For more information, see [Creating a cluster (AWS CLI)](Clusters.md#Clusters.Create.CLI "Clusters.md#Clusters.Create.CLI").
2. In your application, update the endpoints to the new cluster's endpoints.
   For more information, see [Finding Endpoints (AWS CLI)](Endpoints.md#Endpoints.Find.CLI "Endpoints.md#Endpoints.Find.CLI").
3. Delete the old cluster.
   For more information, see [Using the AWS CLI to delete an ElastiCache cluster](Clusters.md#Clusters.Delete.CLI "Clusters.md#Clusters.Delete.CLI").

### Scaling a node-based Memcached cluster vertically (ElastiCache API)

The following procedure walks you through scaling a node-based Memcached cluster vertically using the ElastiCache API.

1. Create a new cluster with the new node type.
   For more information, see [Creating a cluster for Memcached (ElastiCache API)](Clusters.md#Clusters.Create.API.mem-heading "Clusters.md#Clusters.Create.API.mem-heading")
2. In your application, update the endpoints to the new cluster's endpoints.
   For more information, see [Finding Endpoints (ElastiCache API)](Endpoints.md#Endpoints.Find.API "Endpoints.md#Endpoints.Find.API").
3. Delete the old cluster.
   For more information, see [Using the ElastiCache API](Clusters.md#Clusters.Delete.API "Clusters.md#Clusters.Delete.API").
