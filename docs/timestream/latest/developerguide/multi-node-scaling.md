

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# Scaling a cluster
<a name="multi-node-scaling"></a>

## Overview
<a name="multi-node-scaling-overview"></a>

Multi-node scaling extends the capabilities of Timestream for InfluxDB 3 Enterprise edition by allowing you to create clusters with up to 15 nodes, enabling horizontal scalability for increased workload demands. This feature provides flexible cluster configuration options to optimize for specific read and write workloads, with nodes distributed across multiple Availability Zones for high availability.

## Key capabilities
<a name="multi-node-key-capabilities"></a>

With multi-node scaling, you can:
+ Create clusters with up to 15 nodes (maximum 4 writer nodes, 13 reader nodes, and 1 dedicated compactor)
+ Dynamically adjust cluster size by adding or removing nodes as your workload requirements change
+ Configure node roles between Writer/Reader mode or Reader-only mode
+ Distribute nodes across multiple Availability Zones for improved availability
+ Access your cluster through dedicated endpoints for read/write or read-only operations

## Cluster configuration
<a name="multi-node-cluster-configuration"></a>

### Node types and roles
<a name="multi-node-types-and-roles"></a>

When configuring your cluster, you can specify:
+ **Writer/Reader Nodes**: Process both write and read operations (1-4 nodes)
+ **Reader-only Nodes**: Dedicated to processing read queries (0-13 nodes)
+ **Dedicated Compactor**: Required for clusters with 3\+ nodes to optimize data storage

### Cluster endpoints
<a name="multi-node-cluster-endpoints"></a>

Timestream for InfluxDB 3 provides two types of endpoints:
+ **Cluster Endpoints**: Distribute traffic among available nodes
  + **Read/Write Endpoint**: Routes traffic to all Writer/Reader nodes
  + **Read-only Endpoint**: Routes traffic to all nodes capable of read operations
+ **Node Endpoints**: Allow direct access to specific nodes for workload isolation

**Important**  
When using node endpoints, there will be downtime if the node is restarted, patched, upgraded, or fails.

**Note**  
When generating writes or reads using multiple parallel threads from the same client machine, DNS caching behavior can affect traffic distribution across cluster nodes. For guidance on optimizing DNS resolution to ensure even traffic distribution, see [Managing DNS resolution for cluster endpoints](timestream-for-influx-managing-dns.md).

## Managing cluster size
<a name="multi-node-managing-cluster-size"></a>

To modify your cluster configuration, you must use parameter groups:

1. Create a new parameter group with your desired configuration

1. Apply the parameter group to your cluster

This approach applies to both scaling up (adding nodes) and scaling down (removing nodes).

**Important**  
When creating a new parameter group for scaling, ensure you are using all the recommended parameters for your instance size. Review the [Supported Instance Types and Specifications](supported-instance-types.md) page for instance-specific guidance. Before applying the new parameter group, verify your current running configuration to ensure no settings are accidentally changed when adding or removing nodes. You can check your effective configuration by following the steps in [Creating Parameter Groups with the AWS CLI](creating-parameter-groups-cli.md).

## Multi-AZ deployment
<a name="multi-node-multi-az-deployment"></a>

When running multi-node clusters, nodes are automatically distributed across different Availability Zones in your selected region. This distribution ensures:
+ No downtime in your cluster when using Cluster endpoints
+ Improved fault tolerance against AZ-level failures
+ Consistent performance across the region

## Requirements and limitations
<a name="multi-node-requirements-limitations"></a>
+ Clusters with 3\+ nodes require a dedicated compactor
+ A minimum of 2 Writer/Reader nodes is recommended for high availability
+ All nodes in a cluster must use the same instance type
+ Node mode changes require creating a new parameter group
+ Node endpoints may experience downtime during maintenance operations

## Best practices
<a name="multi-node-best-practices"></a>
+ Use cluster endpoints instead of node endpoints for production workloads to ensure high availability
+ Scale your cluster based on your read/write workload ratio (more reader nodes for read-heavy workloads)
+ Monitor node performance to determine optimal scaling needs
+ Plan scaling operations during periods of lower activity
+ To maximize performance on write-heavy workloads in multi-node deployments, send write operations only to your writer node(s) and route read queries to your reader-only nodes

**Tip**  
For write-intensive workloads, configure more Writer/Reader nodes. For read-intensive workloads, add more Reader-only nodes while maintaining at least 2 Writer/Reader nodes for high availability.