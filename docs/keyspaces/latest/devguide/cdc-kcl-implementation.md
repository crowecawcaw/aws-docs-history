# Implement a KCL consumer application for Amazon Keyspaces CDC streams

This topic provides a step-by-step guide to implementing a KCL consumer application to process Amazon Keyspaces CDC streams.

1. Prerequisites: Before you begin, ensure you have:
   - An Amazon Keyspaces table with a CDC stream
   - Required IAM permissions for the IAM principal to access the Amazon Keyspaces CDC stream,
     create and access DynamoDB tables for KCL stream processing, and permissions to publish metrics to CloudWatch. For more
     information and a policy example, see [Permissions to process Amazon Keyspaces CDC streams with the Kinesis Client Library (KCL)](configure-cdc-permissions.md#cdc-permissions-kcl "configure-cdc-permissions.md#cdc-permissions-kcl").
   - Ensure that valid AWS credentials are set up in your local configuration. For more
     information, see [Store access keys for programmatic access](aws.credentials.md "aws.credentials.md").
   - Java Development Kit (JDK) 8 or later
   - Requirements listed in the [Readme](https://github.com/aws/keyspaces-streams-kinesis-adapter "https://github.com/aws/keyspaces-streams-kinesis-adapter") on Github.

2. In this step, you add the KCL dependency to your project. For Maven, add the following
   to your pom.xml:

```
<dependencies>
        <dependency>
            <groupId>software.amazon.kinesis</groupId>
            <artifactId>amazon-kinesis-client</artifactId>
            <version>3.1.0</version>
        </dependency>
        <dependency>
            <groupId>software.amazon.keyspaces</groupId>
            <artifactId>keyspaces-streams-kinesis-adapter</artifactId>
            <version>1.0.0</version>
        </dependency>
    </dependencies>
```

###### Note

Always check for the latest version of KCL at the [KCL GitHub repository](https://github.com/awslabs/amazon-kinesis-client "https://github.com/awslabs/amazon-kinesis-client"). 3. Create a factory class that produces record processor instances:

```
import software.amazon.awssdk.services.keyspacesstreams.model.Record;
import software.amazon.keyspaces.streamsadapter.adapter.KeyspacesStreamsClientRecord;
import software.amazon.keyspaces.streamsadapter.model.KeyspacesStreamsProcessRecordsInput;
import software.amazon.keyspaces.streamsadapter.processor.KeyspacesStreamsShardRecordProcessor;
import software.amazon.kinesis.lifecycle.events.InitializationInput;
import software.amazon.kinesis.lifecycle.events.LeaseLostInput;
import software.amazon.kinesis.lifecycle.events.ShardEndedInput;
import software.amazon.kinesis.lifecycle.events.ShutdownRequestedInput;
import software.amazon.kinesis.processor.RecordProcessorCheckpointer;

public class RecordProcessor implements KeyspacesStreamsShardRecordProcessor {
    private String shardId;

    @Override
    public void initialize(InitializationInput initializationInput) {
        this.shardId = initializationInput.shardId();
        System.out.println("Initializing record processor for shard: " + shardId);
    }

    @Override
    public void processRecords(KeyspacesStreamsProcessRecordsInput processRecordsInput) {
        try {
            for (KeyspacesStreamsClientRecord record : processRecordsInput.records()) {
                Record keyspacesRecord = record.getRecord();
                System.out.println("Received record: " + keyspacesRecord);
            }

            if (!processRecordsInput.records().isEmpty()) {
                RecordProcessorCheckpointer checkpointer = processRecordsInput.checkpointer();
                try {
                    checkpointer.checkpoint();
                    System.out.println("Checkpoint successful for shard: " + shardId);
                } catch (Exception e) {
                    System.out.println("Error while checkpointing for shard: " + shardId + " " + e);
                }
            }
        } catch (Exception e) {
            System.out.println("Error processing records for shard: " + shardId + " " + e);
        }
    }

    @Override
    public void leaseLost(LeaseLostInput leaseLostInput) {
        System.out.println("Lease lost for shard: " + shardId);
    }

    @Override
    public void shardEnded(ShardEndedInput shardEndedInput) {
        System.out.println("Shard ended: " + shardId);
        try {
            // This is required. Checkpoint at the end of the shard
            shardEndedInput.checkpointer().checkpoint();
            System.out.println("Final checkpoint successful for shard: " + shardId);
        } catch (Exception e) {
            System.out.println("Error while final checkpointing for shard: " + shardId + " " + e);
            throw new RuntimeException("Error while final checkpointing", e);
        }
    }

    @Override
    public void shutdownRequested(ShutdownRequestedInput shutdownRequestedInput) {
        System.out.println("Shutdown requested for shard " + shardId);
        try {
            shutdownRequestedInput.checkpointer().checkpoint();
        } catch (Exception e) {
            System.out.println("Error while checkpointing on shutdown for shard: " + shardId + " " + e);
        }
    }
}
```

4. Create a record factory as shown in the following example.

```
import software.amazon.kinesis.processor.ShardRecordProcessor;
import software.amazon.kinesis.processor.ShardRecordProcessorFactory;

import java.util.Queue;
import java.util.concurrent.ConcurrentLinkedQueue;

public class RecordProcessorFactory implements ShardRecordProcessorFactory {
    private final Queue<RecordProcessor> processors = new ConcurrentLinkedQueue<>();

    @Override
    public ShardRecordProcessor shardRecordProcessor() {
        System.out.println("Creating new RecordProcessor");
        RecordProcessor processor = new RecordProcessor();
        processors.add(processor);
        return processor;
    }
}
```

5. In this step you
   create the base class to configure KCLv3 and the Amazon Keyspaces adapter.

```
import com.example.KCLExample.utils.RecordProcessorFactory;
import software.amazon.keyspaces.streamsadapter.AmazonKeyspacesStreamsAdapterClient;
import software.amazon.keyspaces.streamsadapter.StreamsSchedulerFactory;
import java.util.Arrays;
import java.util.List;
import java.util.concurrent.ExecutionException;

import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.cloudwatch.CloudWatchAsyncClient;
import software.amazon.awssdk.services.dynamodb.DynamoDbAsyncClient;
import software.amazon.awssdk.services.dynamodb.model.DeleteTableRequest;
import software.amazon.awssdk.services.dynamodb.model.DeleteTableResponse;
import software.amazon.awssdk.services.keyspacesstreams.KeyspacesStreamsClient;
import software.amazon.awssdk.services.kinesis.KinesisAsyncClient;
import software.amazon.kinesis.common.ConfigsBuilder;
import software.amazon.kinesis.common.InitialPositionInStream;
import software.amazon.kinesis.common.InitialPositionInStreamExtended;
import software.amazon.kinesis.coordinator.CoordinatorConfig;
import software.amazon.kinesis.coordinator.Scheduler;
import software.amazon.kinesis.leases.LeaseManagementConfig;
import software.amazon.kinesis.processor.ProcessorConfig;
import software.amazon.kinesis.processor.StreamTracker;
import software.amazon.kinesis.retrieval.polling.PollingConfig;

public class KCLTestBase {

    protected KeyspacesStreamsClient streamsClient;
    protected KinesisAsyncClient adapterClient;
    protected DynamoDbAsyncClient dynamoDbAsyncClient;
    protected CloudWatchAsyncClient cloudWatchClient;
    protected Region region;
    protected RecordProcessorFactory recordProcessorFactory;
    protected Scheduler scheduler;
    protected Thread schedulerThread;

    public void baseSetUp() {
        recordProcessorFactory = new RecordProcessorFactory();
        setupKCLBase();
    }

    protected void setupKCLBase() {
        region = Region.US_EAST_1;

        streamsClient = KeyspacesStreamsClient.builder()
                .region(region)
                .build();
        adapterClient = new AmazonKeyspacesStreamsAdapterClient(
                streamsClient,
                region);
        dynamoDbAsyncClient = DynamoDbAsyncClient.builder()
                .region(region)
                .build();
        cloudWatchClient = CloudWatchAsyncClient.builder()
                .region(region)
                .build();
    }

    protected void startScheduler(Scheduler scheduler) {
        this.scheduler = scheduler;
        schedulerThread = new Thread(() -> scheduler.run());
        schedulerThread.start();
    }

    protected void shutdownScheduler() {
        if (scheduler != null) {
            scheduler.shutdown();
            try {
                schedulerThread.join(30000);
            } catch (InterruptedException e) {
                System.out.println("Error while shutting down scheduler " + e);
            }
        }
    }

    protected Scheduler createScheduler(String streamArn, String leaseTableName) {
        String workerId = "worker-" + System.currentTimeMillis();

        // Create ConfigsBuilder
        ConfigsBuilder configsBuilder = createConfigsBuilder(streamArn, workerId, leaseTableName);

        // Configure retrieval config for polling
        PollingConfig pollingConfig = new PollingConfig(streamArn, adapterClient);

        // Create the Scheduler
        return StreamsSchedulerFactory.createScheduler(
                configsBuilder.checkpointConfig(),
                configsBuilder.coordinatorConfig(),
                configsBuilder.leaseManagementConfig(),
                configsBuilder.lifecycleConfig(),
                configsBuilder.metricsConfig(),
                configsBuilder.processorConfig(),
                configsBuilder.retrievalConfig().retrievalSpecificConfig(pollingConfig),
                streamsClient,
                region
        );
    }

    private ConfigsBuilder createConfigsBuilder(String streamArn, String workerId, String leaseTableName) {
        ConfigsBuilder configsBuilder = new ConfigsBuilder(
                streamArn,
                leaseTableName,
                adapterClient,
                dynamoDbAsyncClient,
                cloudWatchClient,
                workerId,
                recordProcessorFactory);

        configureCoordinator(configsBuilder.coordinatorConfig());
        configureLeaseManagement(configsBuilder.leaseManagementConfig());
        configureProcessor(configsBuilder.processorConfig());
        configureStreamTracker(configsBuilder, streamArn);

        return configsBuilder;
    }

    private void configureCoordinator(CoordinatorConfig config) {
        config.skipShardSyncAtWorkerInitializationIfLeasesExist(true)
                .parentShardPollIntervalMillis(1000)
                .shardConsumerDispatchPollIntervalMillis(500);
    }

    private void configureLeaseManagement(LeaseManagementConfig config) {
        config.shardSyncIntervalMillis(0)
                .leasesRecoveryAuditorInconsistencyConfidenceThreshold(0)
                .leasesRecoveryAuditorExecutionFrequencyMillis(5000)
                .leaseAssignmentIntervalMillis(1000L);
    }

    private void configureProcessor(ProcessorConfig config) {
        config.callProcessRecordsEvenForEmptyRecordList(true);
    }

    private void configureStreamTracker(ConfigsBuilder configsBuilder, String streamArn) {
        StreamTracker streamTracker = StreamsSchedulerFactory.createSingleStreamTracker(
                streamArn,
                InitialPositionInStreamExtended.newInitialPosition(InitialPositionInStream.TRIM_HORIZON)
        );
        configsBuilder.streamTracker(streamTracker);
    }

    public void deleteAllDdbTables(String baseTableName) {
        List<String> tablesToDelete = Arrays.asList(
                baseTableName,
                baseTableName + "-CoordinatorState",
                baseTableName + "-WorkerMetricStats"
        );

        for (String tableName : tablesToDelete) {
            deleteTable(tableName);
        }
    }

    private void deleteTable(String tableName) {
        DeleteTableRequest deleteTableRequest = DeleteTableRequest.builder()
                .tableName(tableName)
                .build();

        try {
            DeleteTableResponse response = dynamoDbAsyncClient.deleteTable(deleteTableRequest).get();
            System.out.println("Table deletion response " + response);
        } catch (InterruptedException | ExecutionException e) {
            System.out.println("Error deleting table: " + tableName + " " + e);
        }
    }
}
```

6. In this step you implement the record processor class for your application to start processing change events.

```
 import software.amazon.kinesis.coordinator.Scheduler;

public class KCLTest {

    private static final int APP_RUNTIME_SECONDS = 1800;
    private static final int SLEEP_INTERNAL_MS = 60*1000;

    public static void main(String[] args) {
        KCLTestBase kclTestBase;

        kclTestBase = new KCLTestBase();
        kclTestBase.baseSetUp();

        // Create and start scheduler
        String leaseTableName = generateUniqueApplicationName();

        // Update below to your Stream ARN
        String streamArn = "arn:aws:cassandra:us-east-1:759151643516:/keyspace/cdc_sample_test/table/test_kcl_bool/stream/2025-07-01T15:52:57.529";
        Scheduler scheduler = kclTestBase.createScheduler(streamArn, leaseTableName);
        kclTestBase.startScheduler(scheduler);

        // Wait for specified time before shutting down - KCL applications are designed to run forever, however in this
        // example we will shut it down after APP_RUNTIME_SECONDS
        long startTime = System.currentTimeMillis();
        long endTime = startTime + (APP_RUNTIME_SECONDS * 1000);
        while (System.currentTimeMillis() < endTime) {
            try {
                // Print and sleep every minute
                Thread.sleep(SLEEP_INTERNAL_MS);
                System.out.println("Application is running");
            } catch (InterruptedException e) {
                System.out.println("Interrupted while waiting for records");
                Thread.currentThread().interrupt();
                break;
            }
        }

        // Stop the scheduler
        kclTestBase.shutdownScheduler();
        kclTestBase.deleteAllDdbTables(leaseTableName);
    }

    public static String generateUniqueApplicationName() {
        String timestamp = String.valueOf(System.currentTimeMillis());
        String randomString = java.util.UUID.randomUUID().toString().substring(0, 8);
        return String.format("KCL-App-%s-%s", timestamp, randomString);
    }
}
```

## Best practices

Follow these best practices when using KCL with Amazon Keyspaces CDC streams:

**Error handling**

Implement robust error handling in your record processor to handle exceptions gracefully. Consider implementing retry logic for
transient failures.

**Checkpointing frequency**

Balance checkpointing frequency to minimize duplicate processing while ensuring reasonable progress tracking. Too frequent
checkpointing can impact performance, while too infrequent checkpointing can lead to more reprocessing if a worker fails.

**Worker scaling**

Scale the number of workers based on the number of shards in your CDC stream. A good starting point is to have one worker per
shard, but you may need to adjust based on your processing requirements.

**Monitoring**

Use CloudWatch metrics provided by KCL to monitor the health and performance of your consumer application. Key metrics include
processing latency, checkpoint age, and lease counts.

**Testing**

Test your consumer application thoroughly, including scenarios like worker failures, stream resharding, and varying load conditions.

## Using KCL with non-Java languages

While KCL is primarily a Java library, you can use it with other programming languages through the MultiLangDaemon.
The MultiLangDaemon is a Java-based daemon that manages the interaction between your non-Java record processor and the KCL.

KCL provides support for the following languages:

- Python
- Ruby
- Node.js
- .NET

For more information about using KCL with non-Java languages, see the
[KCL MultiLangDaemon documentation](https://github.com/awslabs/amazon-kinesis-client/tree/master/amazon-kinesis-client-multilang "https://github.com/awslabs/amazon-kinesis-client/tree/master/amazon-kinesis-client-multilang").

## Troubleshooting

This section provides solutions to common issues you might encounter when using KCL with Amazon Keyspaces CDC streams.

**Slow processing**

If your consumer application is processing records slowly, consider:

- Increasing the number of worker instances
- Optimizing your record processing logic
- Checking for bottlenecks in downstream systems

**Duplicate processing**

If you're seeing duplicate processing of records, check your checkpointing logic. Ensure you're checkpointing after successfully
processing records.

**Worker failures**

If workers are failing frequently, check:

- Resource constraints (CPU, memory)
- Network connectivity issues
- Permissions issues

**Lease table issues**

If you're experiencing issues with the KCL lease table:

- Check that your application has appropriate permissions to access the Amazon Keyspaces table
- Verify that the table has sufficient provisioned throughput
