

# Using the DynamoDB Streams Kinesis Adapter to read records from a timestamp
<a name="Streams.Timestamp"></a>

With timestamp-based stream processing, you can start reading DynamoDB Streams records from a specific point in time. This guide explains how to configure the feature with the DynamoDB Streams Kinesis Adapter and how it behaves in different scenarios.

## Prerequisites
<a name="Streams.Timestamp.Prerequisites"></a>

To read DynamoDB Streams records from a specific point in time, make sure that your application uses the following:
+ DynamoDB Streams Kinesis Adapter version 2.5.0 or later.
+ The same *AWS Identity and Access Management* (IAM) permissions required by an existing adapter application. This feature does not require additional API permissions.

For more information about adapter setup, see [Using the DynamoDB Streams Kinesis adapter to process stream records](Streams.KCLAdapter.md).

## Configure the starting timestamp
<a name="Streams.Timestamp.Configure"></a>

1. Create an `InitialPositionInStreamExtended` instance with the desired timestamp.

1. Pass it to `StreamsSchedulerFactory.createSingleStreamTracker`.

1. Add the returned `StreamTracker` to the `ConfigsBuilder` for your Kinesis Client Library (KCL) application.

The following Java example shows how to configure the starting timestamp:

```
// Create the initial position with the desired timestamp
InitialPositionInStreamExtended initialPosition =
    InitialPositionInStreamExtended.newInitialPositionAtTimestamp(
        Date.from(Instant.ofEpochMilli(1790467200000L)));

// Create the stream tracker
StreamTracker streamTracker = StreamsSchedulerFactory.createSingleStreamTracker(
    streamArn,
    initialPosition);

// Register the stream tracker, so that the scheduler uses the configured timestamp to read shards
configsBuilder.streamTracker(streamTracker);
```

The adapter initializes each new lease with `AT_TIMESTAMP` as the initial position. For each lease, it calls `GetShardIterator` with the specified timestamp to obtain an iterator. It then passes the iterator to `GetRecords`, which returns records beginning with the first record whose `ApproximateCreationDateTime` is at or after the specified timestamp.

## Timestamp scenarios
<a name="Streams.Timestamp.Scenarios"></a>

### The timestamp is older than the retained stream records
<a name="Streams.Timestamp.Scenarios.OlderThanRetention"></a>

The application starts at the oldest record still available in each shard. It does not return an error. You cannot recover records that have gone past the DynamoDB Streams 24-hour retention window.

### The timestamp is in the future
<a name="Streams.Timestamp.Scenarios.Future"></a>

The adapter validates the timestamp during initialization. If the timestamp is in the future, the adapter rejects it without making any API calls, and processing cannot start. Use a timestamp at or before the current time. Allow for clock differences between the application host and the service when choosing a timestamp close to the current time.

## Changing the timestamp or initial position with an existing lease table
<a name="Streams.Timestamp.ConfigChange"></a>

Do not change the timestamp or switch between `AT_TIMESTAMP`, `TRIM_HORIZON`, and `LATEST` in a running application which has the state stored in the lease table. Shards that store sequence numbers as checkpoints in the lease table continue from those checkpoints. Shards that have not started can use the new configuration, or fail if it is incompatible with their existing leases. The application can therefore process different shards from different starting positions.

To apply either change safely, stop the existing application and choose one of these approaches:

1. **Delete the lease table and restart the application (recommended)**: Stop every worker, delete the existing lease table, update the configuration, and then restart the application.

1. **Use a new application name**: The adapter creates a new lease table and applies the new timestamp or initial position when the application starts. By default, KCL uses the application name as the name of the lease table unless explicitly overridden. The existing lease table remains available if you need to roll back.

## Pricing
<a name="Streams.Timestamp.Pricing"></a>

There is no additional charge for reading stream records from a timestamp beyond the standard `GetRecords` charges. For more information, see [DynamoDB pricing](https://aws.amazon.com/dynamodb/pricing/).

## See also
<a name="Streams.Timestamp.SeeAlso"></a>
+ [Using the DynamoDB Streams Kinesis adapter to process stream records](Streams.KCLAdapter.md)
+ [Developing consumers using the Kinesis Client Library](https://docs.aws.amazon.com/streams/latest/dev/kcl.html)
+ [DynamoDB Streams Kinesis Adapter on the GitHub website](https://github.com/awslabs/dynamodb-streams-kinesis-adapter)