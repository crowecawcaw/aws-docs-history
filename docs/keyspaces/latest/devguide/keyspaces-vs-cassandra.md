# How does Amazon Keyspaces (for Apache Cassandra) compare to Apache

Cassandra?

To establish a connection to Amazon Keyspaces, you can either use a public [AWS service endpoint](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md")
or a private endpoint using
[Interface VPC endpoints (AWS PrivateLink)](../../../vpc/latest/privatelink/vpce-interface.md "../../../vpc/latest/privatelink/vpce-interface.md") in the
[Amazon Virtual Private Cloud](../../../vpc/latest/userguide.md "../../../vpc/latest/userguide.md") . Depending on the endpoint used,
Amazon Keyspaces can appear to the client in one of the following ways.

**AWS service endpoint connection**
This is a connection established over any [public endpoint](programmatic.md#global_endpoints "programmatic.md#global_endpoints").
In this case, Amazon Keyspaces appears as a **nine-node** Apache Cassandra 3.11.2
cluster to the client.

**Interface VPC endpoint connection**
This is a private connection established using an [interface VPC endpoint](vpc-endpoints.md "vpc-endpoints.md"). In this case, Amazon Keyspaces appears as a **three-node** Apache
Cassandra 3.11.2 cluster to the client.

Independent of the connection type and the number of nodes that are visible to the client,
Amazon Keyspaces provides virtually limitless throughput and storage. To do this, Amazon Keyspaces maps the nodes
to load balancers that route your queries to one of the many underlying storage partitions.
For more information about connections, see [How connections work in Amazon Keyspaces](connections.md#connections.howtheywork "connections.md#connections.howtheywork").

Amazon Keyspaces stores data in partitions. A partition is an allocation of storage for a table,
backed by solid state drives (SSDs). Amazon Keyspaces automatically replicates your data across
multiple [Availability Zones](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ "https://aws.amazon.com/about-aws/global-infrastructure/regions_az/") within an AWS Region for durability and high availability.
As your throughput or storage needs grow, Amazon Keyspaces handles the partition management for you and
automatically provisions the required additional partitions.

Amazon Keyspaces supports all commonly used Cassandra data-plane operations, such as creating
keyspaces and tables, reading data, and writing data. Amazon Keyspaces is [serverless](serverless_resource_management.md "serverless_resource_management.md"), so you don’t have to provision,
patch, or manage servers. You also don’t have to install, maintain, or operate software. As
a result, in Amazon Keyspaces you don't need to use the Cassandra control plane API operations to
manage cluster and node settings.

Amazon Keyspaces automatically configures settings such as replication factor and consistency level
to provide you with high availability, durability, and single-digit-millisecond performance.
For even more resiliency and low-latency local reads, Amazon Keyspaces offers [multi-Region replication](multiRegion-replication.md "multiRegion-replication.md").

###### Topics

- [Functional differences: Amazon Keyspaces vs. Apache Cassandra](functional-differences.md "functional-differences.md")
- [Supported Cassandra APIs, operations, functions, and data
  types](cassandra-apis.md "cassandra-apis.md")
- [Supported Apache Cassandra read and write consistency levels and associated costs](consistency.md "consistency.md")
