# Using the DynamoDB Streams Kinesis adapter to process stream

records

Using the Amazon Kinesis Adapter is the recommended way to consume streams from Amazon DynamoDB. The
DynamoDB Streams API is intentionally similar to that of Kinesis Data Streams. In both services, data streams are composed of shards,
which are containers for stream records. Both services' APIs contain
`ListStreams`, `DescribeStream`, `GetShards`, and
`GetShardIterator` operations. (Although these DynamoDB Streams actions are similar to
their counterparts in Kinesis Data Streams, they are not 100 percent identical.)

As a DynamoDB Streams user, you can use the design patterns found within the KCL to process DynamoDB Streams
shards and stream records. To do this, you use the DynamoDB Streams Kinesis Adapter. The Kinesis Adapter
implements the Kinesis Data Streams interface so that the KCL can be used for consuming and processing
records from DynamoDB Streams. For instructions on how to set up and install the DynamoDB Streams Kinesis Adapter, see
the [GitHub
repository](https://github.com/awslabs/dynamodb-streams-kinesis-adapter "https://github.com/awslabs/dynamodb-streams-kinesis-adapter").

You can write applications for Kinesis Data Streams using the Kinesis Client Library (KCL). The KCL
simplifies coding by providing useful abstractions above the low-level Kinesis Data Streams API. For more
information about the KCL, see the [Developing consumers using the Kinesis
client library](../../../kinesis/latest/dev/developing-consumers-with-kcl.md "../../../kinesis/latest/dev/developing-consumers-with-kcl.md") in the _Amazon Kinesis Data Streams Developer Guide_.

DynamoDB recommends using KCL version 3.x with AWS SDK for Java v2.x. The current DynamoDB Streams
Kinesis Adapter version 1.x with AWS SDK for AWS SDK for Java v1.x will continue to be fully supported
throughout its lifecycle as intended during the transitional period in alignment
with [AWS SDKs and Tools
maintenance policy](../../../sdkref/latest/guide/maint-policy.md "../../../sdkref/latest/guide/maint-policy.md").

###### Note

Amazon Kinesis Client Library (KCL) versions 1.x and 2.x are outdated. KCL 1.x will reach
end-of-support on January 30, 2026. We strongly recommend that you migrate your KCL
applications using version 1.x to the latest KCL version before January 30, 2026. To
find the latest KCL version, see the [Amazon Kinesis Client
Library](https://github.com/awslabs/amazon-kinesis-client "https://github.com/awslabs/amazon-kinesis-client") page on GitHub. For information about the latest KCL versions, see
[Use Kinesis
Client Library](../../../streams/latest/dev/kcl.md "../../../streams/latest/dev/kcl.md"). For information about migrating from KCL 1.x to KCL 3.x, see
Migrating from KCL 1.x to KCL 3.x.

The following diagram shows how these libraries interact with one another.

![Interaction between DynamoDB Streams, Kinesis Data Streams, and KCL for processing DynamoDB Streams records.](images/streams-kinesis-adapter.png)
With the DynamoDB Streams Kinesis Adapter in place, you can begin developing against the KCL interface,
with the API calls seamlessly directed at the DynamoDB Streams endpoint.

When your application starts, it calls the KCL to instantiate a worker. You must provide
the worker with configuration information for the application, such as the stream descriptor
and AWS credentials, and the name of a record processor class that you provide. As it runs
the code in the record processor, the worker performs the following tasks:

- Connects to the stream
- Enumerates the shards within the stream
- Checks and enumerates child shards of a closed parent shard within the stream
- Coordinates shard associations with other workers (if any)
- Instantiates a record processor for every shard it manages
- Pulls records from the stream
- Pushes the records to the corresponding record processor
- Checkpoints processed records
- Balances shard-worker associations when the worker instance count changes
- Balances shard-worker associations when shards are split

###### Note

For a description of the KCL concepts listed here, see [Developing consumers using the
Kinesis client library](../../../kinesis/latest/dev/developing-consumers-with-kcl.md "../../../kinesis/latest/dev/developing-consumers-with-kcl.md") in the _Amazon Kinesis Data Streams Developer Guide_.

For more information on using streams with AWS Lambda see [DynamoDB Streams and AWS Lambda triggers](Streams.md "Streams.md")
