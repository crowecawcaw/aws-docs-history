# Migrating from KCL 1.x to KCL 3.x

## Overview

This guide provides instructions for migrating your consumer application from KCL 1.x to
KCL 3.x. Due to architectural differences between KCL 1.x and KCL 3.x, migration requires
updating several components to ensure compatibility.

KCL 1.x uses different classes and interfaces compared to KCL 3.x. You must migrate the record processor, record
processor factory, and worker classes to the KCL 3.x compatible format first, and follow the
migration steps for KCL 1.x to KCL 3.x migration.

## Migration steps

###### Topics

- [Step 1: Migrate the record processor](#step1-record-processor "#step1-record-processor")
- [Step 2: Migrate the record processor
  factory](#step2-record-processor-factory "#step2-record-processor-factory")
- [Step 3: Migrate the worker](#step3-worker-migration "#step3-worker-migration")
- [Step 4: KCL 3.x configuration overview and
  recommendations](#step4-configuration-migration "#step4-configuration-migration")
- [Step 5: Migrate from KCL 2.x to KCL 3.x](#step5-kcl2-to-kcl3 "#step5-kcl2-to-kcl3")

### Step 1: Migrate the record processor

The following example shows a record processor implemented for KCL 1.x DynamoDB Streams Kinesis
adapter:

```
package com.amazonaws.kcl;

import com.amazonaws.services.kinesis.clientlibrary.exceptions.InvalidStateException;
import com.amazonaws.services.kinesis.clientlibrary.exceptions.ShutdownException;
import com.amazonaws.services.kinesis.clientlibrary.interfaces.IRecordProcessorCheckpointer;
import com.amazonaws.services.kinesis.clientlibrary.interfaces.v2.IRecordProcessor;
import com.amazonaws.services.kinesis.clientlibrary.interfaces.v2.IShutdownNotificationAware;
import com.amazonaws.services.kinesis.clientlibrary.lib.worker.ShutdownReason;
import com.amazonaws.services.kinesis.clientlibrary.types.InitializationInput;
import com.amazonaws.services.kinesis.clientlibrary.types.ProcessRecordsInput;
import com.amazonaws.services.kinesis.clientlibrary.types.ShutdownInput;

public class StreamsRecordProcessor implements IRecordProcessor, IShutdownNotificationAware {
    @Override
    public void initialize(InitializationInput initializationInput) {
        //
        // Setup record processor
        //
    }

    @Override
    public void processRecords(ProcessRecordsInput processRecordsInput) {
        for (Record record : processRecordsInput.getRecords()) {
            String data = new String(record.getData().array(), Charset.forName("UTF-8"));
            System.out.println(data);
            if (record instanceof RecordAdapter) {
                // record processing and checkpointing logic
            }
        }
    }

    @Override
    public void shutdown(ShutdownInput shutdownInput) {
        if (shutdownInput.getShutdownReason() == ShutdownReason.TERMINATE) {
            try {
                shutdownInput.getCheckpointer().checkpoint();
            } catch (ShutdownException | InvalidStateException e) {
                throw new RuntimeException(e);
            }
        }
    }

    @Override
    public void shutdownRequested(IRecordProcessorCheckpointer checkpointer) {
        try {
            checkpointer.checkpoint();
        } catch (ShutdownException | InvalidStateException e) {
            //
            // Swallow exception
            //
            e.printStackTrace();
        }
    }
}
```

###### To migrate the RecordProcessor class

1. Change the interfaces from
   `com.amazonaws.services.kinesis.clientlibrary.interfaces.v2.IRecordProcessor`
   and
   `com.amazonaws.services.kinesis.clientlibrary.interfaces.v2.IShutdownNotificationAware`
   to
   `com.amazonaws.services.dynamodbv2.streamsadapter.processor.DynamoDBStreamsShardRecordProcessor`
   as follows:

```
// import com.amazonaws.services.kinesis.clientlibrary.interfaces.v2.IRecordProcessor;
// import com.amazonaws.services.kinesis.clientlibrary.interfaces.v2.IShutdownNotificationAware;

import com.amazonaws.services.dynamodbv2.streamsadapter.processor.DynamoDBStreamsShardRecordProcessor;
```

2. Update import statements for the `initialize` and
   `processRecords` methods:

```
// import com.amazonaws.services.kinesis.clientlibrary.types.InitializationInput;
import software.amazon.kinesis.lifecycle.events.InitializationInput;

// import com.amazonaws.services.kinesis.clientlibrary.types.ProcessRecordsInput;
import com.amazonaws.services.dynamodbv2.streamsadapter.model.DynamoDBStreamsProcessRecordsInput;
```

3. Replace the `shutdownRequested` method with the following new methods:
   `leaseLost`, `shardEnded`, and
   `shutdownRequested`.

```
//    @Override
//    public void shutdownRequested(IRecordProcessorCheckpointer checkpointer) {
//        //
//        // This is moved to shardEnded(...) and shutdownRequested(ShutdownReauestedInput)
//        //
//        try {
//            checkpointer.checkpoint();
//        } catch (ShutdownException | InvalidStateException e) {
//            //
//            // Swallow exception
//            //
//            e.printStackTrace();
//        }
//    }

    @Override
    public void leaseLost(LeaseLostInput leaseLostInput) {

    }

    @Override
    public void shardEnded(ShardEndedInput shardEndedInput) {
        try {
            shardEndedInput.checkpointer().checkpoint();
        } catch (ShutdownException | InvalidStateException e) {
            //
            // Swallow the exception
            //
            e.printStackTrace();
        }
    }

    @Override
    public void shutdownRequested(ShutdownRequestedInput shutdownRequestedInput) {
        try {
            shutdownRequestedInput.checkpointer().checkpoint();
        } catch (ShutdownException | InvalidStateException e) {
            //
            // Swallow the exception
            //
            e.printStackTrace();
        }
    }
```

The following is the updated version of the record processor class:

```
package com.amazonaws.codesamples;

import software.amazon.kinesis.exceptions.InvalidStateException;
import software.amazon.kinesis.exceptions.ShutdownException;
import software.amazon.kinesis.lifecycle.events.InitializationInput;
import software.amazon.kinesis.lifecycle.events.LeaseLostInput;
import com.amazonaws.services.dynamodbv2.streamsadapter.model.DynamoDBStreamsProcessRecordsInput;
import software.amazon.kinesis.lifecycle.events.ShardEndedInput;
import software.amazon.kinesis.lifecycle.events.ShutdownRequestedInput;
import software.amazon.dynamodb.streamsadapter.processor.DynamoDBStreamsShardRecordProcessor;
import software.amazon.dynamodb.streamsadapter.adapter.DynamoDBStreamsKinesisClientRecord;
import com.amazonaws.services.dynamodbv2.streamsadapter.processor.DynamoDBStreamsShardRecordProcessor;
import com.amazonaws.services.dynamodbv2.streamsadapter.adapter.DynamoDBStreamsClientRecord;
import software.amazon.awssdk.services.dynamodb.model.Record;

public class StreamsRecordProcessor implements DynamoDBStreamsShardRecordProcessor {

    @Override
    public void initialize(InitializationInput initializationInput) {

    }

    @Override
    public void processRecords(DynamoDBStreamsProcessRecordsInput processRecordsInput) {
        for (DynamoDBStreamsKinesisClientRecord record: processRecordsInput.records())
            Record ddbRecord = record.getRecord();
            // processing and checkpointing logic for the ddbRecord
        }
    }

    @Override
    public void leaseLost(LeaseLostInput leaseLostInput) {

    }

    @Override
    public void shardEnded(ShardEndedInput shardEndedInput) {
        try {
            shardEndedInput.checkpointer().checkpoint();
        } catch (ShutdownException | InvalidStateException e) {
            //
            // Swallow the exception
            //
            e.printStackTrace();
        }
    }

    @Override
    public void shutdownRequested(ShutdownRequestedInput shutdownRequestedInput) {
        try {
            shutdownRequestedInput.checkpointer().checkpoint();
        } catch (ShutdownException | InvalidStateException e) {
            //
            // Swallow the exception
            //
            e.printStackTrace();
        }
    }
}
```

###### Note

DynamoDB Streams Kinesis Adapter now uses SDKv2 Record model. In SDKv2, complex
`AttributeValue` objects (`BS`, `NS`, `M`,
`L`, `SS`) never return null. Use `hasBs()`,
`hasNs()`, `hasM()`, `hasL()`, `hasSs()`
methods to verify if these values exist.

### Step 2: Migrate the record processor

factory

The record processor factory is responsible for creating record processors when a lease
is acquired. The following is an example of a KCL 1.x factory:

```
package com.amazonaws.codesamples;

import software.amazon.dynamodb.AmazonDynamoDB;
import com.amazonaws.services.kinesis.clientlibrary.interfaces.v2.IRecordProcessor;
import com.amazonaws.services.kinesis.clientlibrary.interfaces.v2.IRecordProcessorFactory;

public class StreamsRecordProcessorFactory implements IRecordProcessorFactory {

    @Override
    public IRecordProcessor createProcessor() {
        return new StreamsRecordProcessor(dynamoDBClient, tableName);
    }
}
```

###### To migrate the `RecordProcessorFactory`

- Change the implemented interface from
  `com.amazonaws.services.kinesis.clientlibrary.interfaces.v2.IRecordProcessorFactory`
  to `software.amazon.kinesis.processor.ShardRecordProcessorFactory`, as
  follows:

```
// import com.amazonaws.services.kinesis.clientlibrary.interfaces.v2.IRecordProcessor;
import software.amazon.kinesis.processor.ShardRecordProcessor;

// import com.amazonaws.services.kinesis.clientlibrary.interfaces.v2.IRecordProcessorFactory;
import software.amazon.kinesis.processor.ShardRecordProcessorFactory;

// public class TestRecordProcessorFactory implements IRecordProcessorFactory {
public class StreamsRecordProcessorFactory implements ShardRecordProcessorFactory {

Change the return signature for createProcessor.

// public IRecordProcessor createProcessor() {
public ShardRecordProcessor shardRecordProcessor() {
```

The following is an example of the record processor factory in 3.0:

```
package com.amazonaws.codesamples;

import software.amazon.kinesis.processor.ShardRecordProcessor;
import software.amazon.kinesis.processor.ShardRecordProcessorFactory;

public class StreamsRecordProcessorFactory implements ShardRecordProcessorFactory {

    @Override
    public ShardRecordProcessor shardRecordProcessor() {
        return new StreamsRecordProcessor();
    }
}
```

### Step 3: Migrate the worker

In version 3.0 of the KCL, a new class, called **Scheduler**, replaces the **Worker** class. The
following is an example of a KCL 1.x worker:

```
final KinesisClientLibConfiguration config = new KinesisClientLibConfiguration(...)
final IRecordProcessorFactory recordProcessorFactory = new RecordProcessorFactory();
final Worker worker = StreamsWorkerFactory.createDynamoDbStreamsWorker(
        recordProcessorFactory,
        workerConfig,
        adapterClient,
        amazonDynamoDB,
        amazonCloudWatchClient);
```

###### To migrate the worker

1. Change the `import` statement for the `Worker` class to the
   import statements for the `Scheduler` and `ConfigsBuilder`
   classes.

```
// import com.amazonaws.services.kinesis.clientlibrary.lib.worker.Worker;
import software.amazon.kinesis.coordinator.Scheduler;
import software.amazon.kinesis.common.ConfigsBuilder;
```

2. Import `StreamTracker` and change import of
   `StreamsWorkerFactory` to `StreamsSchedulerFactory`.

```
import software.amazon.kinesis.processor.StreamTracker;
// import software.amazon.dynamodb.streamsadapter.StreamsWorkerFactory;
import software.amazon.dynamodb.streamsadapter.StreamsSchedulerFactory;
```

3. Choose the position from which to start the application. It can be
   `TRIM_HORIZON` or `LATEST`.

```
import software.amazon.kinesis.common.InitialPositionInStream;
import software.amazon.kinesis.common.InitialPositionInStreamExtended;
```

4. Create a `StreamTracker` instance.

```
StreamTracker streamTracker = StreamsSchedulerFactory.createSingleStreamTracker(
        streamArn,
        InitialPositionInStreamExtended.newInitialPosition(InitialPositionInStream.TRIM_HORIZON)
);
```

5. Create the `AmazonDynamoDBStreamsAdapterClient` object.

```
import software.amazon.dynamodb.streamsadapter.AmazonDynamoDBStreamsAdapterClient;
import software.amazon.awssdk.auth.credentials.AwsCredentialsProvider;
import software.amazon.awssdk.auth.credentials.DefaultCredentialsProvider;

...

AwsCredentialsProvider credentialsProvider = DefaultCredentialsProvider.create();

AmazonDynamoDBStreamsAdapterClient adapterClient = new AmazonDynamoDBStreamsAdapterClient(
        credentialsProvider, awsRegion);
```

6. Create the `ConfigsBuilder` object.

```
import software.amazon.kinesis.common.ConfigsBuilder;

...
ConfigsBuilder configsBuilder = new ConfigsBuilder(
                streamTracker,
                applicationName,
                adapterClient,
                dynamoDbAsyncClient,
                cloudWatchAsyncClient,
                UUID.randomUUID().toString(),
                new StreamsRecordProcessorFactory());
```

7. Create the `Scheduler` using `ConfigsBuilder` as shown in the
   following example:

```

import java.util.UUID;

import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.dynamodb.DynamoDbAsyncClient;
import software.amazon.awssdk.services.cloudwatch.CloudWatchAsyncClient;
import software.amazon.awssdk.services.kinesis.KinesisAsyncClient;

import software.amazon.kinesis.common.KinesisClientUtil;
import software.amazon.kinesis.coordinator.Scheduler;

...


DynamoDbAsyncClient dynamoClient = DynamoDbAsyncClient.builder().region(region).build();
CloudWatchAsyncClient cloudWatchClient = CloudWatchAsyncClient.builder().region(region).build();


DynamoDBStreamsPollingConfig pollingConfig = new DynamoDBStreamsPollingConfig(adapterClient);
pollingConfig.idleTimeBetweenReadsInMillis(idleTimeBetweenReadsInMillis);

// Use ConfigsBuilder to configure settings
RetrievalConfig retrievalConfig = configsBuilder.retrievalConfig();
retrievalConfig.retrievalSpecificConfig(pollingConfig);

CoordinatorConfig coordinatorConfig = configsBuilder.coordinatorConfig();
coordinatorConfig.clientVersionConfig(CoordinatorConfig.ClientVersionConfig.CLIENT_VERSION_CONFIG_COMPATIBLE_WITH_2X);

Scheduler scheduler = StreamsSchedulerFactory.createScheduler(
                configsBuilder.checkpointConfig(),
                coordinatorConfig,
                configsBuilder.leaseManagementConfig(),
                configsBuilder.lifecycleConfig(),
                configsBuilder.metricsConfig(),
                configsBuilder.processorConfig(),
                retrievalConfig,
                adapterClient
        );
```

###### Important

The `CLIENT_VERSION_CONFIG_COMPATIBLE_WITH_2X` setting maintains
compatibility between DynamoDB Streams Kinesis Adapter for KCL v3 and KCL v1, not between KCL v2 and
v3.

### Step 4: KCL 3.x configuration overview and

recommendations

For a detailed description of the configurations introduced post KCL 1.x that are
relevant in KCL 3.x see [KCL configurations](../../../streams/latest/dev/kcl-configuration.md "../../../streams/latest/dev/kcl-configuration.md") and [KCL
migration client configuration](../../../streams/latest/dev/kcl-migration.md#client-configuration "../../../streams/latest/dev/kcl-migration.md#client-configuration").

###### Important

Instead of directly creating objects of `checkpointConfig`,
`coordinatorConfig`, `leaseManagementConfig`,
`metricsConfig`, `processorConfig` and
`retrievalConfig`, we recommend using `ConfigsBuilder` to set
configurations in KCL 3.x and later versions to avoid Scheduler initialization issues.
`ConfigsBuilder` provides a more flexible and maintainable way to configure
your KCL application.

#### Configurations with update default value in

KCL 3.x

`**billingMode**`

In KCL version 1.x, the default value for `billingMode` is set to
`PROVISIONED`. However, with KCL version 3.x, the default
`billingMode` is `PAY_PER_REQUEST` (on-demand mode). We
recommend that you use the on-demand capacity mode for your lease table to
automatically adjust the capacity based on your usage. For guidance on using
provisioned capacity for your lease tables, see [Best practices for the
lease table with provisioned capacity mode](../../../streams/latest/dev/kcl-migration-lease-table.md "../../../streams/latest/dev/kcl-migration-lease-table.md").

`**idleTimeBetweenReadsInMillis**`

In KCL version 1.x, the default value for
`idleTimeBetweenReadsInMillis` is set to is 1,000 (or 1 second). KCL
version 3.x sets the default value for i`dleTimeBetweenReadsInMillis` to
1,500 (or 1.5 seconds), but Amazon DynamoDB Streams Kinesis Adapter overrides the default value to
1,000 (or 1 second).

#### New configurations in KCL 3.x

`**leaseAssignmentIntervalMillis**`

This configuration defines the time interval before newly discovered shards
begin processing, and is calculated as 1.5 ×
`leaseAssignmentIntervalMillis`. If this setting isn't explicitly
configured, the time interval defaults to 1.5 × `failoverTimeMillis`.
Processing new shards involves scanning the lease table and querying a global
secondary index (GSI) on the lease table. Lowering the
`leaseAssignmentIntervalMillis` increases the frequency of these scan
and query operations, resulting in higher DynamoDB costs. We recommend setting this
value to 2000 (or 2 seconds) to minimize the delay in processing new shards.

`**shardConsumerDispatchPollIntervalMillis**`

This configuration defines the interval between successive polls by the shard
consumer to trigger state transitions. In KCL version 1.x, this behavior was
controlled by the `idleTimeInMillis` parameter, which was not exposed as
a configurable setting. With KCL version 3.x, we recommend setting this config to
match the value used for `idleTimeInMillis` in your KCL version 1.x
setup.

### Step 5: Migrate from KCL 2.x to KCL 3.x

To ensure a smooth transition and compatibility with the latest Kinesis Client Library
(KCL) version, follow steps 5-8 in the migration guide's instructions for [upgrading from KCL 2.x to KCL 3.x](../../../streams/latest/dev/kcl-migration-from-2-3.md#kcl-migration-from-2-3-worker-metrics "../../../streams/latest/dev/kcl-migration-from-2-3.md#kcl-migration-from-2-3-worker-metrics").

For common KCL 3.x troubleshooting issues, see [Troubleshooting KCL consumer applications](../../../streams/latest/dev/troubleshooting-consumers.md "../../../streams/latest/dev/troubleshooting-consumers.md").
