# Managing cluster operations

DAX handles the cluster’s maintenance and health for you. However, you need to provide operational input to scale the cluster horizontally or vertically to match your usage patterns. This section describes the recommended process to scale your DAX clusters.

###### In this section

- [Scaling a cluster horizontally](#dax-cluster-horizontal-scaling "#dax-cluster-horizontal-scaling")
- [Scaling a cluster vertically](#dax-cluster-vertical-scaling "#dax-cluster-vertical-scaling")

## Scaling a cluster horizontally

Scaling a DAX cluster involves adjusting its capacity to meet throughput demands. This adjustment is done by increasing or decreasing the number of nodes (replicas) in the cluster while it's running. This process, known as [horizontal scaling](DAX.md#DAX.cluster-management.scaling.read-scaling "DAX.md#DAX.cluster-management.scaling.read-scaling"), helps distribute the workload across more nodes or consolidate to fewer nodes when demand is low.

You can horizontally scale your DAX cluster in and out using the `decrease-replication-factor` or `increase-replication-factor` commands in the AWS CLI.

###### Increase replication factor (scale out)

Increasing the replication factor of a DAX cluster adds more nodes to the cluster. The following example shows the usage of the `increase-replication-factor` command.

```
aws dax **increase-replication-factor** \
    --cluster-name `yourClusterName`  \
    --new-replication-factor `desiredReplicationFactor`
```

- In this command, the `cluster-name` argument specifies the name of your cluster. For example, `yourClusterName`.
- The `new-replication-factor` argument specifies the total number of nodes to add in the cluster after scaling. This includes the primary node and replica nodes. For example, if your cluster currently has 3 nodes and you want to add 2 more nodes, set the value of `new-replication-factor` to 5.

###### Decrease replication factor (scale in)

Decreasing the replication factor of a DAX cluster removes nodes from the cluster. Removing nodes can help reduce cost during periods of low demand. The following example shows the usage of the `decrease-replication-factor` command.

```
aws dax decrease-replication-factor \
    --cluster-name `yourClusterName`  \
    --new-replication-factor `desiredReplicationFactor`
```

- In this command, the `cluster-name` argument specifies the name of your cluster. For example, `yourClusterName`.
- The `new-replication-factor` argument specifies the reduced number of nodes in your cluster after scaling. This number must be lower than the current replication factor and must include the primary node. For instance, if your cluster has 5 nodes and you want to remove 2 nodes, set the value of `new-replication-factor` to 3.

### Horizontal scaling considerations

Consider the following when you plan horizontal scaling:

- **Primary node** – The DAX cluster includes a primary node. The replication factor includes this primary node. For example, a replication factor of 3 means one primary node and two replica nodes.
- **Availability** – Adding or removing DAX nodes changes the cluster's availability and fault tolerance. More nodes can improve availability, but they also increase costs.
- **Data migration** – When you increase the replication factor, DAX automatically handles data distribution across the new set of nodes. When a new node begins serving traffic, its cache is already warmed. However, during this process, there might be a temporary impact on performance during data migration.

Make sure you monitor your DAX clusters closely during and after the scaling process to ensure they're performing as expected and make further adjustments as necessary.

## Scaling a cluster vertically

To vertically scale the node size of an existing cluster, you need to create a new cluster and migrate the application traffic to the new cluster. Migrating to a new cluster with different nodes involves several steps to ensure a smooth transition with minimal impact on your application's performance and availability.

To create a new cluster for scaling your node size vertically, consider the following points:

- **Access your current setup** – Review the metrics of your current DAX cluster to determine the new node size and quantity you need. Use this information as input to define your cluster size. For information, see [Sizing your DAX cluster](dax-cluster-sizing.md "dax-cluster-sizing.md").
- **Set up a new DAX cluster** – Create a new DAX cluster with the node type and quantity you determined. You can use the existing configuration settings from your [parameter group](dax-deploy-cluster.md#dax-cluster-parameter-group "dax-deploy-cluster.md#dax-cluster-parameter-group"), unless you need to make adjustments.
- **Synchronize data** – Because DAX is a caching layer for DynamoDB, you don't need to migrate data directly. However, the new DAX cluster won't have any of your working dataset in memory until you send traffic to it.
- **Update application configuration** – Update your application's configuration to point to the new [DAX cluster's endpoint](DAX.concepts.md#DAX.concepts.cluster-endpoint "DAX.concepts.md#DAX.concepts.cluster-endpoint"). You might need to change code or update environment variables, depending on your application's configuration.

To reduce impact when you switch to a new cluster, send canary traffic to the new cluster from a small portion of your application fleet. You can do this by slowly rolling out application updates or by using a weight-based routing DNS entry in front of your DAX endpoint.

- **Monitor and optimize** – After you switch to the new DAX cluster, closely monitor its performance [metrics and logs](DAX.md "DAX.md") for any issues. Be ready to adjust the number of nodes based on updated workload patterns.

Until the new cluster caches your working dataset properly, you'll see higher cache miss rates and latencies.

- **Decommission old cluster** – When you're sure that the new cluster is performing as expected, safely decommission the old DAX cluster to avoid unnecessary costs.
