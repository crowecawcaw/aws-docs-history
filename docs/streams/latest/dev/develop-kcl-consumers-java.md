# Develop consumers with KCL in

Java

## Prerequisites

Before you start using KCL 3.x, make sure that you have the
following:

- Java Development Kit (JDK) 8 or later
- AWS SDK for Java 2.x
- Maven or Gradle for dependency management

KCL collects CPU utilization metrics such as CPU utilization from the
compute host that workers are running on to balance the load to achieve an even
resource utilization level across workers. To enable KCL to collect CPU
utilization metrics from workers, you must meet the following prerequisites:

**Amazon Elastic Compute Cloud(Amazon EC2)**

- Your operating system must be Linux OS.
- You must enable [IMDSv2](../../../AWSEC2/latest/UserGuide/configuring-instance-metadata-service.md "../../../AWSEC2/latest/UserGuide/configuring-instance-metadata-service.md") in your EC2 instance.

**Amazon Elastic Container Service (Amazon ECS) on Amazon EC2**

- Your operating system must be Linux OS.
- You must enable [ECS task metadata endpoint version 4](../../../AmazonECS/latest/developerguide/ec2-metadata.md "../../../AmazonECS/latest/developerguide/ec2-metadata.md").
- Your Amazon ECS container agent version must be 1.39.0 or later.

**Amazon ECS on AWS Fargate**

- You must enable [Fargate task metadata endpoint version 4](../../../AmazonECS/latest/developerguide/task-metadata-endpoint-v4-fargate.md "../../../AmazonECS/latest/developerguide/task-metadata-endpoint-v4-fargate.md"). If you use Fargate
  platform version 1.4.0 or later, this is enabled by default.
- Fargate platform version 1.4.0 or later.

**Amazon Elastic Kubernetes Service (Amazon EKS) on Amazon EC2**

- Your operating system must be Linux OS.

**Amazon EKS on AWS Fargate**

- Fargate platform 1.3.0 or later.

###### Important

If KCL cannot collect CPU utilization metrics from workers, KCL will
fall back to use throughput per worker to assign leases and balance the load
across workers in the fleet. For more information, see [How KCL assigns leases to workers and
balances the load](kcl-dynamoDB.md#kcl-assign-leases "kcl-dynamoDB.md#kcl-assign-leases").

## Install and add

dependencies

If you're using Maven, add the following dependency to your `pom.xml` file.
Make sure you replaced 3.x.x to the latest KCL version.

```
<dependency>
    <groupId>software.amazon.kinesis</groupId>
    <artifactId>amazon-kinesis-client</artifactId>
    <version>3.x.x</version> <!-- Use the latest version -->
</dependency>
```

If you're using Gradle, add the following to your `build.gradle` file. Make
sure you replaced 3.x.x to the latest KCL version.

```
implementation 'software.amazon.kinesis:amazon-kinesis-client:3.x.x'
```

You can check for the latest version of the KCL on the [Maven Central Repository](https://search.maven.org/artifact/software.amazon.kinesis/amazon-kinesis-client "https://search.maven.org/artifact/software.amazon.kinesis/amazon-kinesis-client").

## Implement the

consumer

A KCL consumer application consists of the following key
components:

###### Key components

- [RecordProcessor](#implementation-recordprocessor "#implementation-recordprocessor")
- [RecordProcessorFactory](#implementation-recordprocessorfactory "#implementation-recordprocessorfactory")
- [Scheduler](#implementation-scheduler "#implementation-scheduler")
- [Main Consumer Application](#implementation-main "#implementation-main")

### RecordProcessor

RecordProcessor is the core component where your business logic for processing
Kinesis data stream records resides. It defines how your application processes the
data it receives from the Kinesis stream.

Key responsibilities:

- Initialize processing for a shard
- Process batches of records from the Kinesis stream
- Shutdown processing for a shard (for example, when the shard splits or
  merges, or the lease is handed over to another host)
- Handle checkpointing to track progress

The following shows an implementation example:

```
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.slf4j.MDC;
import software.amazon.kinesis.exceptions.InvalidStateException;
import software.amazon.kinesis.exceptions.ShutdownException;
import software.amazon.kinesis.lifecycle.events.*;
import software.amazon.kinesis.processor.ShardRecordProcessor;

public class SampleRecordProcessor implements ShardRecordProcessor {
    private static final String SHARD_ID_MDC_KEY = "ShardId";
    private static final Logger log = LoggerFactory.getLogger(SampleRecordProcessor.class);
    private String shardId;

    @Override
    public void initialize(InitializationInput initializationInput) {
        shardId = initializationInput.shardId();
        MDC.put(SHARD_ID_MDC_KEY, shardId);
        try {
            log.info("Initializing @ Sequence: {}", initializationInput.extendedSequenceNumber());
        } finally {
            MDC.remove(SHARD_ID_MDC_KEY);
        }
    }

    @Override
    public void processRecords(ProcessRecordsInput processRecordsInput) {
        MDC.put(SHARD_ID_MDC_KEY, shardId);
        try {
            log.info("Processing {} record(s)", processRecordsInput.records().size());
            processRecordsInput.records().forEach(r ->
                log.info("Processing record pk: {} -- Seq: {}", r.partitionKey(), r.sequenceNumber())
            );

            // Checkpoint periodically
            processRecordsInput.checkpointer().checkpoint();
        } catch (Throwable t) {
            log.error("Caught throwable while processing records. Aborting.", t);
        } finally {
            MDC.remove(SHARD_ID_MDC_KEY);
        }
    }

    @Override
    public void leaseLost(LeaseLostInput leaseLostInput) {
        MDC.put(SHARD_ID_MDC_KEY, shardId);
        try {
            log.info("Lost lease, so terminating.");
        } finally {
            MDC.remove(SHARD_ID_MDC_KEY);
        }
    }

    @Override
    public void shardEnded(ShardEndedInput shardEndedInput) {
        MDC.put(SHARD_ID_MDC_KEY, shardId);
        try {
            log.info("Reached shard end checkpointing.");
            shardEndedInput.checkpointer().checkpoint();
        } catch (ShutdownException | InvalidStateException e) {
            log.error("Exception while checkpointing at shard end. Giving up.", e);
        } finally {
            MDC.remove(SHARD_ID_MDC_KEY);
        }
    }

    @Override
    public void shutdownRequested(ShutdownRequestedInput shutdownRequestedInput) {
        MDC.put(SHARD_ID_MDC_KEY, shardId);
        try {
            log.info("Scheduler is shutting down, checkpointing.");
            shutdownRequestedInput.checkpointer().checkpoint();
        } catch (ShutdownException | InvalidStateException e) {
            log.error("Exception while checkpointing at requested shutdown. Giving up.", e);
        } finally {
            MDC.remove(SHARD_ID_MDC_KEY);
        }
    }
}
```

The following is a detailed explanation of each method used in the
example:

**initialize(InitializationInput
initializationInput)**

- Purpose: Set up any necessary resources or state for processing
  records.
- When it's called: Once, when KCL assigns a shard to this
  record processor.
- Key points:
  - `initializationInput.shardId()`: The ID of the
    shard this processor will handle.
  - `initializationInput.extendedSequenceNumber()`: The
    sequence number to start processing from.

**processRecords(ProcessRecordsInput
processRecordsInput)**

- Purpose: Process the incoming records and optionally checkpoint
  progress.
- When it's called: Repeatedly, as long as the record processor holds
  the lease for the shard.
- Key points:
  - `processRecordsInput.records()`: List of records to
    process.
  - `processRecordsInput.checkpointer()`: Used to
    checkpoint the progress.
  - Make sure that you handled any exceptions during processing to
    prevent KCL from failing.
  - This method should be idempotent, as the same record may be
    processed more than once in some scenarios, such as data that
    has not been checkpointed before unexpected worker crashes or
    restarts.
  - Always flush any buffered data before checkpointing to ensure
    data consistency.

**leaseLost(LeaseLostInput
leaseLostInput)**

- Purpose: Clean up any resources specific to processing this
  shard.
- When it's called: When another Scheduler takes over the lease for this
  shard.
- Key points:
  - Checkpointing is not allowed in this method.

**shardEnded(ShardEndedInput
shardEndedInput)**

- Purpose: Finish processing for this shard and checkpoint.
- When it's called: When the shard splits or merges, indicating all data
  for this shard has been processed.
- Key points:
  - `shardEndedInput.checkpointer()`: Used to perform
    the final checkpointing.
  - Checkpointing in this method is mandatory to complete
    processing.
  - Failing to flush data and checkpoint here may result in data
    loss or duplicate processing when the shard is reopened.

**shutdownRequested(ShutdownRequestedInput
shutdownRequestedInput)**

- Purpose: Checkpoint and clean up resources when KCL is
  shutting down.
- When it's called: When KCL is shutting down, for example,
  when the application is terminating).
- Key points:
  - `shutdownRequestedInput.checkpointer()`: Used to
    perform checkpointing before shutdown.
  - Make sure you implemented checkpointing in the method so that
    progress is saved before the application stops.
  - Failure to flush data and checkpoint here may result in data
    loss or reprocessing of records when the application
    restarts.

###### Important

KCL 3.x ensures fewer data reprocessing when the lease is handed
over from one worker to another worker by checkpointing before the previous
worker is shut down. If you don’t implement the checkpointing logic in the
`shutdownRequested()` method, you won’t see this benefit.
Make sure that you have implemented a checkpointing logic inside the
`shutdownRequested()` method.

### RecordProcessorFactory

RecordProcessorFactory is responsible for creating new RecordProcessor
instances. KCL uses this factory to create a new RecordProcessor for
each shard that the application needs to process.

Key responsibilities:

- Create new RecordProcessor instances on demand
- Make sure that each RecordProcessor is properly initialized

The following is an implementation example:

```
import software.amazon.kinesis.processor.ShardRecordProcessor;
import software.amazon.kinesis.processor.ShardRecordProcessorFactory;

public class SampleRecordProcessorFactory implements ShardRecordProcessorFactory {
    @Override
    public ShardRecordProcessor shardRecordProcessor() {
        return new SampleRecordProcessor();
    }
}
```

In this example, the factory creates a new SampleRecordProcessor each time
shardRecordProcessor() is called. You can extend this to include any necessary
initialization logic.

### Scheduler

Scheduler is a high-level component that coordinates all the activities of the
KCL application. It's responsible for the overall orchestration of data
processing.

Key responsibilities:

- Manage the lifecycle of RecordProcessors
- Handle lease management for shards
- Coordinate checkpointing
- Balance shard processing load across multiple workers of your
  application
- Handle graceful shutdown and application termination signals

Scheduler is typically created and started in the Main Application. You can
check the implementation example of Scheduler in the following section, Main
Consumer Application.

### Main Consumer Application

Main Consumer Application ties all the components together. It's responsible
for setting up the KCL consumer, creating necessary clients, configuring the
Scheduler, and managing the application's lifecycle.

Key responsibilities:

- Set up AWS service clients (Kinesis, DynamoDB, CloudWatch)
- Configure the KCL application
- Create and start the Scheduler
- Handle application shutdown

The following is an implementation example:

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.cloudwatch.CloudWatchAsyncClient;
import software.amazon.awssdk.services.dynamodb.DynamoDbAsyncClient;
import software.amazon.awssdk.services.kinesis.KinesisAsyncClient;
import software.amazon.kinesis.common.ConfigsBuilder;
import software.amazon.kinesis.common.KinesisClientUtil;
import software.amazon.kinesis.coordinator.Scheduler;
import java.util.UUID;

public class SampleConsumer {
    private final String streamName;
    private final Region region;
    private final KinesisAsyncClient kinesisClient;

    public SampleConsumer(String streamName, Region region) {
        this.streamName = streamName;
        this.region = region;
        this.kinesisClient = KinesisClientUtil.createKinesisAsyncClient(KinesisAsyncClient.builder().region(this.region));
    }

    public void run() {
        DynamoDbAsyncClient dynamoDbAsyncClient = DynamoDbAsyncClient.builder().region(region).build();
        CloudWatchAsyncClient cloudWatchClient = CloudWatchAsyncClient.builder().region(region).build();

        ConfigsBuilder configsBuilder = new ConfigsBuilder(
            streamName,
            streamName,
            kinesisClient,
            dynamoDbAsyncClient,
            cloudWatchClient,
            UUID.randomUUID().toString(),
            new SampleRecordProcessorFactory()
        );

        Scheduler scheduler = new Scheduler(
            configsBuilder.checkpointConfig(),
            configsBuilder.coordinatorConfig(),
            configsBuilder.leaseManagementConfig(),
            configsBuilder.lifecycleConfig(),
            configsBuilder.metricsConfig(),
            configsBuilder.processorConfig(),
            configsBuilder.retrievalConfig()
        );

        Thread schedulerThread = new Thread(scheduler);
        schedulerThread.setDaemon(true);
        schedulerThread.start();
    }

    public static void main(String[] args) {
        String streamName = "your-stream-name"; // replace with your stream name
        Region region = Region.US_EAST_1; // replace with your region
        new SampleConsumer(streamName, region).run();
    }
}
```

KCL creates an Enhanced Fan-out (EFO) consumer with dedicated
throughput by default. For more information about Enhanced Fan-out, see
[Develop enhanced fan-out consumers with dedicated
throughput](enhanced-consumers.md "enhanced-consumers.md"). If you have less than 2
consumers or don't need read propagation delays under 200 ms, you must
set the following configuration in the scheduler object to use
shared-throughput consumers:

```
configsBuilder.retrievalConfig().retrievalSpecificConfig(new PollingConfig(streamName, kinesisClient))
```

The following code is an example of creating a scheduler object that uses
shared-throughput consumers:

**Imports**:

```
import software.amazon.kinesis.retrieval.polling.PollingConfig;
```

**Code**:

```
Scheduler scheduler = new Scheduler(
            configsBuilder.checkpointConfig(),
            configsBuilder.coordinatorConfig(),
            configsBuilder.leaseManagementConfig(),
            configsBuilder.lifecycleConfig(),
            configsBuilder.metricsConfig(),
            configsBuilder.processorConfig(),
            configsBuilder.retrievalConfig().retrievalSpecificConfig(new PollingConfig(streamName, kinesisClient))
        );/
```
