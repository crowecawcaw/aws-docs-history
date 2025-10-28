# EMR Serverless job run cancellation with grace period

In data processing systems, abrupt terminations can lead to resource waste, incomplete operations, and potential data inconsistencies. Amazon EMR Serverless allows
you to specify a grace period when canceling job runs. This feature allows time for proper cleanup and completion of in-progress
work before job termination.

When cancelling a job run, specify a grace period (in seconds) using the parameter `shutdownGracePeriodInSeconds` during which the job can
perform cleanup operations prior to final termination. The behavior and default settings vary between
batch and streaming jobs.

## Grace Period For batch jobs

For batch jobs, EMR Serverless allows you to implement custom cleanup operations that execute during the grace period. You can register
these cleanup operations as part of the JVM shutdown hook in your application code.

**Default behavior**

The default behavior for shutdown is to have no grace period. It consists of the following two actions:

- Immediate termination
- Resources are released immediately

**Configuration options**

You can specify settings that result in graceful shutdown:

- Valid Range for Shutdown Grace period: 15-1800 seconds (optional)
- Immediate termination (without any grace period): 0 second

### Enable graceful shutdown

To implement graceful shutdown for batch jobs, follow these steps:

1. Add shutdown hook in your application code containing custom shutdown logic.

Example in Scala

```
import org.apache.hadoop.util.ShutdownHookManager

// Register shutdown hook with priority (second argument)
// Higher priority hooks run first
ShutdownHookManager.get().addShutdownHook(() => {
    logger.info("Performing cleanup operations...")
}, 100)
```

Using [ShutdownHookManager](https://hadoop.apache.org/docs/r2.8.0/hadoop-project-dist/hadoop-common/api/org/apache/hadoop/util/ShutdownHookManager.html "https://hadoop.apache.org/docs/r2.8.0/hadoop-project-dist/hadoop-common/api/org/apache/hadoop/util/ShutdownHookManager.html")

Example in PySpark

```
import atexit

def cleanup():
    # Your cleanup logic here
    print("Performing cleanup operations...")

# Register the cleanup function
atexit.register(cleanup)
```

2. Specify a grace period when canceling the job to allow time for the hooks added previously to execute

**Example**

```
# Default (immediate termination)
aws emr-serverless cancel-job-run \
  --application-id `APPLICATION_ID` \
  --job-run-id `JOB_RUN_ID`

# With 5-minute grace period
aws emr-serverless cancel-job-run \
  --application-id `APPLICATION_ID` \
  --job-run-id `JOB_RUN_ID` \
  --shutdown-grace-period-in-seconds 300
```

## Grace Period For Streaming Jobs

In Spark Structured Streaming, where computations involve reading from or writing to external data sources, abrupt shutdowns can
lead to unwanted results. Streaming jobs process data in micro-batches, and interrupting these operations mid-way can result in duplicate
processing in subsequent attempts. This happens when the latest checkpoint from the previous micro-batch was not written, causing
the same data to be processed again when the streaming job restarts. Such duplicate processing not only wastes computing resources
but can also impact business operations, making it crucial to
avoid abrupt shutdowns.

EMR Serverless provides built-in support for graceful shutdown through a streaming query listener. This ensures proper completion
of ongoing micro-batches before job termination. The service automatically manages graceful shutdown between micro-batches for
streaming applications, ensuring that the current micro-batch completes processing, checkpoints are properly written, and the
streaming context is terminated cleanly without ingesting new data during the shutdown process.

**Default behavior**

- 120-second grace period enabled by default.
- Built-in streaming query listener manages graceful shutdown.

**Configuration options**

- Valid Range for Shutdown Grace period: 15-1800 seconds (optional)
- Immediate Termination: 0 second

### Enable Graceful Shutdown

To implement graceful shutdown for streaming jobs:

Specify a grace period when canceling the job to allow time for the ongoing micro batch to get completed.

**Example**

```
# Default graceful shutdown (120 seconds)
aws emr-serverless cancel-job-run \
  --application-id `APPLICATION_ID` \
  --job-run-id `JOB_RUN_ID`

# Custom grace period (e.g. 300 seconds)
aws emr-serverless cancel-job-run \
  --application-id `APPLICATION_ID` \
  --job-run-id `JOB_RUN_ID` \
  --shutdown-grace-period-in-seconds 300

# Immediate Termination
aws emr-serverless cancel-job-run \
  --application-id `APPLICATION_ID` \
  --job-run-id `JOB_RUN_ID` \
  --shutdown-grace-period-in-seconds 0
```

### Add custom shutdown hooks (optional)

While EMR Serverless manages graceful shutdown by default through its built-in streaming query
listener, you can optionally implement custom shutdown logic for individual streaming queries. EMR Serverless
registers its graceful shutdown listener with priority 60 (using ShutdownHookManager). Since higher priority hooks run first, you
can register your custom cleanup operations with a priority greater than 60 to ensure they execute before EMR Serverless' shutdown process begins.

In order to add a custom hook, refer to the first example in this topic that shows how to add a shutdown hook in your application code. Here, 100 is the priority, which
is greater than 60. Hence such a shutdown hook runs first.

###### Note

Custom shutdown hooks are optional and not required for graceful shutdown functionality, which is handled
automatically by EMR Serverless.

### Grace Period Charges and Batch Duration

If the default value for grace period (120 seconds) is used:

- If your batch duration is less than 120 seconds, you'll only be charged for the actual time needed to complete the batch.
- If your batch duration exceeds 120 seconds, you'll be charged for the maximum grace period (120 seconds), but the query may not shutdown gracefully as it will be forcefully terminated.

To optimize costs and ensure graceful shutdown:

- For batch durations > 120 seconds: Consider increasing the grace period to match your batch duration
- For batch durations < 120 seconds: No need to adjust the grace period as you'll only be charged
  for the actual processing time

## Considerations

### Grace Period Behavior

- The grace period provides time for your registered shutdown hooks to complete.
- Job terminates as soon as the shutdown hook finishes even if it is well before grace period.
- If cleanup operations exceed the grace period, the job will be forcefully terminated.

### Service Behavior

- Grace period shutdown is only available for jobs in RUNNING state.
- Subsequent cancel requests during the CANCELLING state are ignored.
- If EMR Serverless fails to initiate grace period shutdown due to internal service errors:
  - The service will retry for up to 2 minutes.
  - If retries are unsuccessful, the job will be forcefully terminated.

### Billing

Jobs are billed for the compute resources used until the job completely shuts down, including any time taken during the grace period.
