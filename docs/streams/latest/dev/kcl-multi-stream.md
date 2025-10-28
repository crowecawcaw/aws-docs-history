# Multi-stream processing with KCL

This section describes the required changes in KCL that allow you to create KCL
consumer applications that can process more than one data stream at the same
time.

###### Important

- Multi-stream processing is only supported in KCL 2.3 or later.
- Multi-stream processing is _not_ supported for KCL
  consumers written in non-Java languages that run with
  `multilangdaemon`.
- Multi-stream processing is _not_ supported in any
  versions of KCL 1.x.

- **MultistreamTracker interface**
  - To build a consumer application that can process multiple streams at
    the same time, you must implement a new interface called [MultistreamTracker](https://github.com/awslabs/amazon-kinesis-client/blob/0c5042dadf794fe988438436252a5a8fe70b6b0b/amazon-kinesis-client/src/main/java/software/amazon/kinesis/processor/MultiStreamTracker.java "https://github.com/awslabs/amazon-kinesis-client/blob/0c5042dadf794fe988438436252a5a8fe70b6b0b/amazon-kinesis-client/src/main/java/software/amazon/kinesis/processor/MultiStreamTracker.java"). This interface includes the
    `streamConfigList` method that returns the list of data
    streams and their configurations to be processed by the KCL consumer
    application. Notice that the data streams that are being processed can
    be changed during the consumer application runtime.
    `streamConfigList` is called periodically by KCL to learn
    about the changes in data streams to process.
  - The `streamConfigList` populates the [StreamConfig](https://github.com/awslabs/amazon-kinesis-client/blob/0c5042dadf794fe988438436252a5a8fe70b6b0b/amazon-kinesis-client/src/main/java/software/amazon/kinesis/common/StreamConfig.java#L23 "https://github.com/awslabs/amazon-kinesis-client/blob/0c5042dadf794fe988438436252a5a8fe70b6b0b/amazon-kinesis-client/src/main/java/software/amazon/kinesis/common/StreamConfig.java#L23") list.

```
package software.amazon.kinesis.common;

import lombok.Data;
import lombok.experimental.Accessors;

@Data
@Accessors(fluent = true)
public class StreamConfig {
    private final StreamIdentifier streamIdentifier;
    private final InitialPositionInStreamExtended initialPositionInStreamExtended;
    private String consumerArn;
}
```

    + The `StreamIdentifier` and
     `InitialPositionInStreamExtended` are required fields,
     while `consumerArn` is optional. You must provide the
     `consumerArn` only if you are using KCL to implement an
     enhanced fan-out consumer application.
    + For more information about `StreamIdentifier`, see [https://github.com/awslabs/amazon-kinesis-client/blob/v2.5.8/amazon-kinesis-client/src/main/java/software/amazon/kinesis/common/StreamIdentifier.java#L129](https://github.com/awslabs/amazon-kinesis-client/blob/v2.5.8/amazon-kinesis-client/src/main/java/software/amazon/kinesis/common/StreamIdentifier.java#L129 "https://github.com/awslabs/amazon-kinesis-client/blob/v2.5.8/amazon-kinesis-client/src/main/java/software/amazon/kinesis/common/StreamIdentifier.java#L129").
     To create a `StreamIdentifier`, we recommend that you create
     a multistream instance from the `streamArn` and the
     `streamCreationEpoch` that is available in KCL 2.5.0 or
     later. In KCL v2.3 and v2.4, which don't support `streamArm`,
     create a multistream instance by using the format
     `account-id:StreamName:streamCreationTimestamp`. This
     format will be deprecated and no longer supported starting with the next
     major release.
    + MultistreamTracker also includes a strategy for deleting leases of
     old streams in the lease table (formerStreamsLeasesDeletionStrategy).
     Notice that the strategy CANNOT be changed during the consumer
     application runtime. For more information, see [https://github.com/awslabs/amazon-kinesis-client/blob/0c5042dadf794fe988438436252a5a8fe70b6b0b/amazon-kinesis-client/src/main/java/software/amazon/kinesis/processor/FormerStreamsLeasesDeletionStrategy.java](https://github.com/awslabs/amazon-kinesis-client/blob/0c5042dadf794fe988438436252a5a8fe70b6b0b/amazon-kinesis-client/src/main/java/software/amazon/kinesis/processor/FormerStreamsLeasesDeletionStrategy.java "https://github.com/awslabs/amazon-kinesis-client/blob/0c5042dadf794fe988438436252a5a8fe70b6b0b/amazon-kinesis-client/src/main/java/software/amazon/kinesis/processor/FormerStreamsLeasesDeletionStrategy.java").

- Or you can initialize ConfigsBuilder with `MultiStreamTracker` if
  you want to implement a KCL consumer application that processes multiple streams
  at the same time.

```

* Constructor to initialize ConfigsBuilder with MultiStreamTracker
     * @param multiStreamTracker
     * @param applicationName
     * @param kinesisClient
     * @param dynamoDBClient
     * @param cloudWatchClient
     * @param workerIdentifier
     * @param shardRecordProcessorFactory
     */
    public ConfigsBuilder(@NonNull MultiStreamTracker multiStreamTracker, @NonNull String applicationName,
            @NonNull KinesisAsyncClient kinesisClient, @NonNull DynamoDbAsyncClient dynamoDBClient,
            @NonNull CloudWatchAsyncClient cloudWatchClient, @NonNull String workerIdentifier,
            @NonNull ShardRecordProcessorFactory shardRecordProcessorFactory) {
        this.appStreamTracker = Either.left(multiStreamTracker);
        this.applicationName = applicationName;
        this.kinesisClient = kinesisClient;
        this.dynamoDBClient = dynamoDBClient;
        this.cloudWatchClient = cloudWatchClient;
        this.workerIdentifier = workerIdentifier;
        this.shardRecordProcessorFactory = shardRecordProcessorFactory;
    }

```

- With multi-stream support implemented for your KCL consumer application, each
  row of the application's lease table now contains the shard ID and the stream
  name of the multiple data streams that this application processes.
- When multi-stream support for your KCL consumer application is implemented,
  the leaseKey takes the following structure:
  `account-id:StreamName:streamCreationTimestamp:ShardId`. For
  example,
  `111111111:multiStreamTest-1:12345:shardId-000000000336`.

###### Important

When your existing KCL consumer application is configured to process only one data
stream, the `leaseKey` (which is the partition key for the lease table)
is the shard ID. If you reconfigure an existing KCL consumer application to process
multiple data streams, it breaks your lease table, because the `leaseKey`
structure must be as follows:
`account-id:StreamName:StreamCreationTimestamp:ShardId` to support
multi-stream.
