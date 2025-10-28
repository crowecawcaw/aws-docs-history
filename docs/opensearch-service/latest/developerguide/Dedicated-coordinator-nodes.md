# Dedicated coordinator nodes in

Amazon OpenSearch Service

Dedicated coordinator nodes in Amazon OpenSearch Service are specialized nodes that offload coordination
tasks from data nodes. These tasks include managing search requests and hosting
OpenSearch Dashboards. By separating these functions, dedicated coordinator nodes reduce the load
on data nodes, which allows them to focus on data storage, indexing, and search operations.
This improves overall cluster performance and resource utilization.

Additionally, dedicated coordinator nodes help reduce the number of private IP addresses
required for VPC configurations, which leads to more efficient network management. This
setup can result in up to 15% improvement in indexing throughput and 20% better query
performance, depending on workload characteristics.

## When to use dedicated coordinator

nodes

Dedicated coordinator nodes are most beneficial in the following scenarios.

- **Large clusters** – In environments with
  a high volume of data or complex queries, offloading coordination tasks to
  dedicated nodes can improve cluster performance.
- **Frequent queries** – Workloads involving
  frequent search queries or aggregations, especially those with complex date
  histograms or multiple aggregations, benefit from faster query
  processing.
- **Heavy Dashboards use** –
  OpenSearch Dashboards can be resource-intensive. Offloading this responsibility to
  dedicated coordinator nodes reduces the strain on data nodes.

## Architecture and

behavior

In an OpenSearch cluster, dedicated coordinator nodes handle two key
responsibilities.

- **Request handling** – These nodes receive
  incoming search requests and forward them to the appropriate data nodes, which
  store the relevant data. They then consolidate the results from multiple data
  nodes into a single global result set, which is returned to the client.
- **Dashboards hosting** – Coordinator nodes
  manage OpenSearch Dashboards, which relieves data nodes from the additional burden of
  hosting OpenSearch Dashboards and handling related traffic.

In VPC domains, dedicated coordinator nodes are assigned Elastic Network Interfaces
(ENIs) rather than data nodes. This arrangement helps reduce the number of private IP
addresses required for VPCs, which improves network efficiency. Typically, dedicated
coordinator nodes make up around 10% of the total data nodes.

## Requirements and

limitations

Dedicated coordinator nodes have the following requirements and limitations.

- Dedicated coordinator nodes are supported in all OpenSearch versions and
  Elasticsearch versions 6.8 to 7.10.
- To enable dedicated coordinator nodes, your domain must have dedicated master
  nodes enabled. For more information, see [Dedicated master nodes in
  Amazon OpenSearch Service](managedomains-dedicatedmasternodes.md "managedomains-dedicatedmasternodes.md").
- Provisioning dedicated coordinator nodes can incur additional costs. However,
  the improved resource efficiency and enhanced performance justify the
  investment, particularly for large or complex clusters.

## Provisioning dedicated

coordinator nodes

Perform the following steps to provision dedicated coordinator nodes in an existing
domain. Make sure your domain has dedicated _master_ nodes enabled
before you provision coordinator nodes.

###### To provision dedicated coordinator nodes in the AWS Management Console

1. Sign in to the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/home](https://console.aws.amazon.com/aos/home "https://console.aws.amazon.com/aos/home").
2. Choose **Domains**, then select the domain you want
   to modify.
3. In the **Cluster configuration** section, choose
   **Edit**.
4. Choose **Enable dedicated coordinator nodes**.
5. Select the instance type and number of coordinator nodes to
   provision.
6. Choose **Save changes**. It might take several
   minutes for the domain to update.
   To provision dedicated coordinator nodes using the AWS CLI, use the [update-domain-config](../../../cli/latest/reference/opensearch/update-domain-config.md "../../../cli/latest/reference/opensearch/update-domain-config.md") command. The following example provisions
   three `r6g.large.search` coordinator nodes in a domain.

```
aws opensearch update-domain-config \
  --domain-name `my-opensearch-domain` \
  --cluster-config InstanceCount=3,InstanceType=r6g.large.search,DedicatedCoordinatorCount=3,ZoneAwarenessEnabled=true,DedicatedCoordinatorEnabled=true
```

This command enables dedicated coordinator nodes, sets the instance type and
count for the coordinator nodes, and enables zone awareness for higher
availability.

## Best practices

Consider the following best practices when you use dedicated coordinator nodes.

- Use general purpose instances for most use cases. They provide a balanced
  approach between cost and performance. Memory-optimized instances are ideal for
  workloads that require substantial memory resources, such as those that involve
  complex aggregations or large-scale searches.
- A good starting point is to provision between 5% and 10% of your data nodes as
  dedicated coordinator nodes. For example, if your domain has 90 data nodes of a
  particular instance type, consider provisioning 5 to 9 coordinator nodes of the
  same instance type.

###### Note

Instance type availability varies by region. When selecting instance types
for coordinator nodes, verify that your chosen instance type is available in
your target region. You can check instance type availability in the OpenSearch Service
console when creating or modifying your domain.

- To minimize the risk of a single point of failure, provision at least two
  dedicated coordinator nodes. This ensures that your cluster remains operational
  even if one node fails.
- If you're using cross-Region search, provision dedicated
  coordinator nodes in the destination domains. Source domains typically don't
  handle coordination tasks.
- For indexing-heavy environments, consider CPU-optimized instances that match
  the instance size of your data nodes for optimal performance.
- For memory-intensive workloads, use a slightly larger instance type for your
  dedicated coordinator nodes to help manage the increased memory demands.
- Track the `CoordinatorCPUUtilization` Amazon CloudWatch metric. If it
  consistently exceeds 80%, it might indicate that you need larger or additional
  coordinator nodes to handle the load.
- Size your dedicated coordinator nodes to match your data nodes. For example,
  start with 4xlarge general purpose coordinator nodes when using 4xlarge data
  nodes.
- Use multiple smaller instances instead of fewer larger instances for
  coordinator nodes, unless your individual requests or responses need extremely
  high memory (in GBs). For example, choose 12 4xl instances rather than 6 8xlarge
  general purpose instances.

### Node recommendations by cluster

size

Use the following guidelines as a starting point for provisioning dedicated
coordinator nodes based on your cluster size. Adjust the number and type of nodes
based on workload characteristics and performance metrics.

| Cluster size           | Recommended coordinator nodes | Instance type    |
| ---------------------- | ----------------------------- | ---------------- |
| Small (up to 50 nodes) | 3-5 nodes                     | General purpose  |
| Medium (50-100 nodes)  | 5-9 nodes                     | Memory optimized |
| Large (100+ nodes)     | 10-15 nodes                   | Memory optimized |
