# Understand MSK Connect

MSK Connect is a feature of Amazon MSK that makes it easy for developers to stream data to
and from their Apache Kafka clusters. MSK Connect uses Kafka Connect versions 2.7.1 or
3.7.x, which are open-source frameworks for connecting Apache Kafka clusters with external
systems such as databases, search indexes, and file systems. With MSK Connect, you can deploy fully managed connectors built for Kafka Connect that
move data into or pull data from popular data stores like Amazon S3 and Amazon OpenSearch Service. You can deploy
connectors developed by 3rd parties like Debezium for streaming change logs from databases
into an Apache Kafka cluster, or deploy an existing connector with no code changes.
Connectors automatically scale to adjust for changes in load and you pay only for the
resources that you use.

Use source connectors to import data from external systems into your topics. With sink connectors, you can export data from your topics to external systems.

MSK Connect supports connectors for any Apache Kafka cluster with connectivity to an
Amazon VPC, whether it is an MSK cluster or an independently hosted Apache Kafka cluster.

MSK Connect continuously monitors connector health and delivery state, patches and
manages the underlying hardware, and autoscales the connectors to match changes in
throughput.

To get started using MSK Connect, see [Getting started with MSK Connect](msk-connect-getting-started.md "msk-connect-getting-started.md").

To learn about the AWS resources that you can create with MSK Connect, see [Understand connectors](msk-connect-connectors.md "msk-connect-connectors.md"), [Create custom plugins](msk-connect-plugins.md "msk-connect-plugins.md"), and [Understand MSK Connect workers](msk-connect-workers.md "msk-connect-workers.md").

For information about the MSK Connect API, see the [Amazon MSK Connect API
Reference](../../../MSKC/latest/mskc/Welcome.md "../../../MSKC/latest/mskc/Welcome.md").

## Benefits of using Amazon MSK Connect

Apache Kafka is one of the most widely adopted open source streaming platforms for ingesting and processing real-time data streams. With Apache Kafka, you can decouple and independently scale your data-producing and data-consuming applications.

Kafka Connect is an important component of building and running streaming applications with Apache Kafka. Kafka Connect provides a standardized way of moving data between Kafka and external systems. Kafka Connect is highly scalable and can handle large volumes of data Kafka Connect provides a powerful set of API operations and tools for configuring, deploying, and monitoring connectors that move data between Kafka topics and external systems. You can use these tools to customize and extend the functionality of Kafka Connect to meet the specific needs of your streaming application.

You might encounter challenges when you’re operating Apache Kafka Connect clusters on their own, or when you’re trying to migrate open source Apache Kafka Connect applications to AWS. These challenges include time required to setup infrastructure and deploying applications, engineering obstacles when setting up self-managed Apache Kafka Connect clusters, and administrative operational overhead.

To address these challenges, we recommend using Amazon Managed Streaming for Apache Kafka Connect (Amazon MSK Connect) to migrate your open source Apache Kafka Connect applications to AWS. Amazon MSK Connect simplifies using Kafka Connect to stream data to and from between Apache Kafka clusters and external systems, such as databases, search indexes, and file systems.

Here are some of the benefits to migrating to Amazon MSK Connect:

- **Elimination of operational overhead** — Amazon MSK Connect takes away the operational burden associated with patching, provisioning, and scaling of Apache Kafka Connect clusters. Amazon MSK Connect continuously monitors the health of your Connect clusters and automates patching and version upgrades without causing any disruptions to your workloads.
- **Automatic restarting of Connect tasks** — Amazon MSK Connect can automatically recover failed tasks to reduce production disruptions. Task failures can be caused by temporary errors, such as breaching the TCP connection limit for Kafka, and task rebalancing when new workers join the consumer group for sink connectors.
- **Automatic horizontal and vertical scaling** — Amazon MSK Connect enables the connector application to automatically scale to support higher throughputs. Amazon MSK Connect manages scaling for you. You only need to specifying the number of workers in the auto scaling group and the utilization thresholds. You can use the Amazon MSK Connect `UpdateConnector` API operation to vertically scale up or scale down the vCPUs between 1 and 8 vCPUs for supporting variable throughput.
- **Private network connectivity** — Amazon MSK Connect privately connects to source and sink systems by using AWS PrivateLink and private DNS names.
