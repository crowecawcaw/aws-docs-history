Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Application is restarting

If your application is not healthy, its Apache Flink job continually
fails and restarts. This section describes
symptoms and troubleshooting steps for this condition.

## Symptoms

This condition can have the following symptoms:

- The `FullRestarts` metric is not zero. This metric
  represents the number of times the application's job has restarted since you started
  the application.
- The `Downtime` metric is not zero. This metric represents
  the number of milliseconds that the application is in the `FAILING`
  or `RESTARTING` status.
- The application log contains status changes to `RESTARTING`
  or `FAILED`. You can query your application log for these status changes using the
  following CloudWatch Logs Insights query:
  [Analyze errors: Application task-related
  failures](cloudwatch-logs-reading.md#cloudwatch-logs-reading-apps "cloudwatch-logs-reading.md#cloudwatch-logs-reading-apps").

## Causes and solutions

The following conditions may cause your application to become unstable and repeatedly restart:

- **Operator is throwing an exception:** If any exception in an
  operator in your application is unhandled, the application fails over (by
  interpreting that the failure cannot be handled by operator). The application
  restarts from the latest checkpoint to maintain "exactly-once" processing
  semantics. As a result, `Downtime` is not zero during these restart
  periods. In order to prevent this from happening, we recommend that you handle
  any retryable exceptions in the application code.

You can investigate the causes of this condition by querying your
application logs for changes from your application's state from
`RUNNING` to `FAILED`. For more information, see
[Analyze errors: Application task-related
failures](cloudwatch-logs-reading.md#cloudwatch-logs-reading-apps "cloudwatch-logs-reading.md#cloudwatch-logs-reading-apps").

- **Kinesis data streams are not properly provisioned:** If a source
  or sink for your application is a Kinesis data stream, check the [metrics](../../../streams/latest/dev/monitoring-with-cloudwatch.md "../../../streams/latest/dev/monitoring-with-cloudwatch.md") for
  the stream for `ReadProvisionedThroughputExceeded` or
  `WriteProvisionedThroughputExceeded` errors.

If you see these errors, you can increase the available throughput for the Kinesis stream
by increasing the stream's number of shards. For more information, see
[How do I change the number of open shards in Kinesis Data Streams?](https://aws.amazon.com/premiumsupport/knowledge-center/kinesis-data-streams-open-shards/ "https://aws.amazon.com/premiumsupport/knowledge-center/kinesis-data-streams-open-shards/").

- **Other sources or sinks are not properly provisioned
  or available:**
  Verify that your application is correctly provisioning sources and sinks. Check that any sources
  or sinks used in the application (such as other AWS services, or external sources or
  destinations) are well provisioned, are not experiencing read
  or write throttling, or are periodically unavailable.

If you are experiencing throughput-related issues with your dependent services, either
increase resources available to those services, or investigate the cause of any errors or
unavailability.

- **Operators are not properly provisioned:**
  If the workload on the threads for one of the operators in your application is not
  correctly distributed, the operator can become overloaded and the application can crash.
  For information about tuning operator parallelism, see
  [Manage operator scaling properly](performance-improving.md#performance-improving-scaling-op "performance-improving.md#performance-improving-scaling-op").
- **Application fails with DaemonException:** This
  error appears in your application log if you are using a version of Apache Flink prior to 1.11. You may need to upgrade to a later version of Apache Flink so that a KPL version of 0.14 or later is used.
- **Application fails with TimeoutException, FlinkException, or
  RemoteTransportException:** These errors may appear in your application log if your task managers are crashing.
  If your application is overloaded, your task managers can experience CPU or memory resource pressure, causing them to fail.

These errors may look like the following:

    + `java.util.concurrent.TimeoutException: The heartbeat of JobManager with id xxx timed out`
    + `org.apache.flink.util.FlinkException: The assigned slot xxx was removed`
    + `org.apache.flink.runtime.io.network.netty.exception.RemoteTransportException: Connection unexpectedly closed by remote task manager`

To troubleshoot this condition, check the following:

    + Check your CloudWatch metrics for unusual spikes in CPU or memory usage.
    + Check your application for throughput issues. For more information,
     see [Troubleshoot performance issues](performance-troubleshooting.md "performance-troubleshooting.md").
    + Examine your application log for unhandled exceptions
     that your application code is raising.

- **Application fails with JaxbAnnotationModule Not Found error:**
  This error occurs if your application uses Apache Beam, but doesn't have the correct
  dependencies or dependency versions. Managed Service for Apache Flink applications that use Apache Beam must use the following versions of dependencies:

```
<jackson.version>**2.10.2**</jackson.version>
...
<dependency>
    <groupId>com.fasterxml.jackson.module</groupId>
    <artifactId>jackson-module-jaxb-annotations</artifactId>
    <version>**2.10.2**</version>
</dependency>
```

If you do not provide the correct version of `jackson-module-jaxb-annotations`
as an explicit dependency, your application loads it from the environment dependencies,
and since the versions do not match, the application crashes at runtime.

For more information about using Apache Beam with Managed Service for Apache Flink, see [Use CloudFormation](examples-beam.md "examples-beam.md").

- **Application fails with java.io.IOException: Insufficient number of network buffers**

This happens when an application does not have enough memory allocated for network buffers. Network buffers facilitate communication between subtasks.
They are used to store records before transmission over a network, and to store incoming data before dissecting it into records and handing them to subtasks.
The number of network buffers required scales directly with the parallelism and complexity of your job graph. There are a number of approaches to mitigate this issue:

    + You can configure a lower `parallelismPerKpu` so that there is more memory allocated per-subtask and network buffers.
     Note that lowering `parallelismPerKpu` will increase KPU and therefore cost. To avoid this, you can keep the same amount of KPU by
     lowering parallelism by the same factor.
    + You can simplify your job graph by reducing the number of operators or chaining them so that fewer buffers are needed.
    + Otherwise, you can reach out to https://aws.amazon.com/premiumsupport/ for custom network buffer configuration.
