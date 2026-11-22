

# Configuring Amazon MSK event sources for Lambda

To use an Amazon MSK cluster as an event source for your Lambda Event Function, you create an [event source mapping](invocation-eventsourcemapping.md) that connects the two resources. This page describes how to create an event source mapping for Amazon MSK.

This page assumes that you've already properly configured your MSK cluster and the [Amazon Virtual Private Cloud (VPC)](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) it resides in. If you need to set up your cluster or VPC, see [Configuring your Amazon MSK cluster and Amazon VPC network for Lambda](with-msk-cluster-network.md). To configure retry behavior for error handling, see [Configuring error handling controls for Kafka event sources](kafka-retry-configurations.md).

**Topics**
+ [Using an Amazon MSK cluster as an event source](#msk-esm-overview)
+ [Configuring Amazon MSK cluster authentication methods in Lambda](msk-cluster-auth.md)
+ [Creating a Lambda event source mapping for an Amazon MSK event source](msk-esm-create.md)
+ [Creating cross-account event source mappings in Lambda](msk-cross-account.md)
+ [All Amazon MSK event source configuration parameters in Lambda](msk-esm-parameters.md)

## Using an Amazon MSK cluster as an event source
<a name="msk-esm-overview"></a>

When you add your Apache Kafka or Amazon MSK cluster as a trigger for your Lambda Event Function, the cluster is used as an [event source](invocation-eventsourcemapping.md).

Lambda reads event data from the Kafka topics that you specify as `Topics` in a [CreateEventSourceMapping](https://docs.aws.amazon.com/lambda/latest/api/API_CreateEventSourceMapping.html) request, based on the [starting position](kafka-starting-positions.md) that you specify. After successful processing, your Kafka topic is committed to your Kafka cluster.

Lambda reads messages sequentially for each Kafka topic partition. A single Lambda payload can contain messages from multiple partitions. When more records are available, Lambda continues processing records in batches, based on the BatchSize value that you specify in a [CreateEventSourceMapping](https://docs.aws.amazon.com/lambda/latest/api/API_CreateEventSourceMapping.html) request, until your function catches up with the topic.

After Lambda processes each batch, it commits the offsets of the messages in that batch. If your function returns an error for any of the messages in a batch, Lambda retries the whole batch of messages until processing succeeds or the messages expire. You can send records that fail all retry attempts to an on-failure destination for later processing.

**Note**  
While Lambda Event Functions typically have a maximum timeout limit of 30 minutes, on-demand Kafka event source mappings created before 30-minute timeouts were available support function timeouts of up to 14 minutes. Kafka event source mappings in [provisioned mode](kafka-scaling-modes.md#kafka-provisioned-mode), and on-demand Kafka event source mappings created after that, support function timeouts of up to 30 minutes. To use a longer timeout with an existing on-demand event source mapping, turn on provisioned mode. For functions using Lambda Managed Instances, Kafka event source mappings support function timeouts of up to 90 minutes.