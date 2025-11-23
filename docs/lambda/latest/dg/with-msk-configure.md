# Configuring Amazon MSK event sources for Lambda

To use an Amazon MSK cluster as an event source for your Lambda function, you create an [event source mapping](invocation-eventsourcemapping.md "invocation-eventsourcemapping.md") that connects the two resources.
This page describes how to create an event source mapping for Amazon MSK.

This page assumes that you've already properly configured your MSK cluster and the
[Amazon Virtual Private Cloud (VPC)](../../../vpc/latest/userguide/what-is-amazon-vpc.md "../../../vpc/latest/userguide/what-is-amazon-vpc.md")
it resides in. If you need to set up your cluster or VPC, see [Configuring your Amazon MSK cluster and Amazon VPC network for Lambda](with-msk-cluster-network.md "with-msk-cluster-network.md").
To configure retry behavior for error handling, see [Configuring error handling controls for Kafka event sources](kafka-retry-configurations.md "kafka-retry-configurations.md").

###### Topics

- [Using an Amazon MSK cluster as an event source](#msk-esm-overview "#msk-esm-overview")
- [Configuring Amazon MSK ycluster authentication methods in Lambda](msk-cluster-auth.md "msk-cluster-auth.md")
- [Creating a Lambda event source mapping for an Amazon MSK event source](msk-esm-create.md "msk-esm-create.md")
- [Creating cross-account event source mappings in Lambda](msk-cross-account.md "msk-cross-account.md")
- [All Amazon MSK event source configuration parameters in Lambda](msk-esm-parameters.md "msk-esm-parameters.md")

## Using an Amazon MSK cluster as an event source

When you add your Apache Kafka or Amazon MSK cluster as a trigger for your Lambda function, the cluster is used
as an [event source](invocation-eventsourcemapping.md "invocation-eventsourcemapping.md").

Lambda reads event data from the Kafka topics that you specify as `Topics` in a
[CreateEventSourceMapping](../api/API_CreateEventSourceMapping.md "../api/API_CreateEventSourceMapping.md") request, based on the [starting
position](kafka-starting-positions.md "kafka-starting-positions.md") that you specify. After successful processing, your Kafka topic is committed to your
Kafka cluster.

Lambda reads messages sequentially for each Kafka topic partition. A single Lambda payload can contain
messages from multiple partitions. When more records are available, Lambda continues processing records in
batches, based on the BatchSize value that you specify in a [CreateEventSourceMapping](../api/API_CreateEventSourceMapping.md "../api/API_CreateEventSourceMapping.md") request, until
your function catches up with the topic.

After Lambda processes each batch, it commits the offsets of the messages in that batch. If your function
returns an error for any of the messages in a batch, Lambda retries the whole batch of messages until
processing succeeds or the messages expire. You can send records that fail all retry attempts to an
on-failure destination for later processing.

###### Note

While Lambda functions typically have a maximum timeout limit of 15 minutes, event source mappings
for Amazon MSK, self-managed Apache Kafka, Amazon DocumentDB, and Amazon MQ for ActiveMQ and RabbitMQ only support functions with maximum
timeout limits of 14 minutes.
