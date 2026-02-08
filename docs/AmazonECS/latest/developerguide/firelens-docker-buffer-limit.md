# Configuring Amazon ECS logs for high

throughput

For high log throughput scenarios, we recommend using the `awsfirelens` log
driver with FireLens and Fluent Bit. Fluent Bit is a
lightweight log processor that's efficient with resources and can handle millions of log
records. However, achieving optimal performance at scale requires tuning its
configuration.

This section covers advanced Fluent Bit optimization techniques for
handling high log throughput while maintaining system stability and ensuring no data
loss.

For information about how to use custom configuration files with FireLens, see
[Use a custom configuration file](firelens-taskdef.md#firelens-taskdef-customconfig "firelens-taskdef.md#firelens-taskdef-customconfig"). For additional examples,
see [Amazon
ECS FireLens examples](https://github.com/aws-samples/amazon-ecs-firelens-examples "https://github.com/aws-samples/amazon-ecs-firelens-examples") on GitHub.

###### Note

Some configuration options in this section, such as `workers` and
`threaded`, require AWS for Fluent Bit version 3 or
later. For information about available versions, see [AWS for Fluent Bit
releases](https://github.com/aws/aws-for-fluent-bit/releases "https://github.com/aws/aws-for-fluent-bit/releases").

## Use filesystem buffering

By default, Fluent Bit buffers all data in memory. When data is
ingested faster than it can be flushed to outputs, the buffer fills up. Once full,
the input plugin pauses until buffer space becomes available, which can cause
backpressure and slow down your application.

For high-throughput scenarios, we recommend using filesystem buffering. For more information about how
Fluent Bit manages buffering and storage, see [Buffering and Storage](https://docs.fluentbit.io/manual/administration/buffering-and-storage "https://docs.fluentbit.io/manual/administration/buffering-and-storage") in the Fluent Bit
documentation.

Filesystem buffering provides the following advantages:

- **Larger buffer capacity** – Disk space is
  typically more abundant than memory.
- **Persistence** – Buffered data survives
  Fluent Bit restarts.
- **Graceful degradation** – During output
  failures, data accumulates on disk rather than causing memory
  exhaustion.

To enable filesystem buffering, provide a custom Fluent Bit
configuration file. The following example shows the recommended configuration:

```
[SERVICE]
    # Flush logs every 1 second
    Flush 1
    # Wait 120 seconds during shutdown to flush remaining logs
    Grace 120
    # Directory for filesystem buffering
    storage.path             /var/log/flb-storage/
    # Limit chunks stored 'up' in memory (reduce for memory-constrained environments)
    storage.max_chunks_up    32
    # Flush backlog chunks to destinations during shutdown (prevents log loss)
    storage.backlog.flush_on_shutdown On

[INPUT]
    Name forward
    unix_path /var/run/fluent.sock
    # Run input in separate thread to prevent blocking
    threaded true
    # Enable filesystem buffering for persistence
    storage.type filesystem

[OUTPUT]
    Name cloudwatch_logs
    Match *
    region `us-west-2`
    log_group_name `/aws/ecs/my-app`
    log_stream_name $(ecs_task_id)
    # Use multiple workers for parallel processing
    workers 2
    # Retry failed flushes up to 15 times
    retry_limit 15
    # Maximum disk space for buffered data for this output
    storage.total_limit_size 10G
```

Key configuration parameters:

`storage.path`

The directory where Fluent Bit stores buffered chunks
on disk.

`storage.backlog.flush_on_shutdown`

When enabled, Fluent Bit attempts to flush all backlog
filesystem chunks to their destinations during shutdown. This helps
ensure data delivery before Fluent Bit stops, but may
increase shutdown time.

`storage.max_chunks_up`

The number of chunks that remain in memory. The default is 128 chunks,
which can consume 500 MB+ of memory because each chunk can use up to 4–5
MB. In memory-constrained environments, lower this value. For example, if
you have 50 MB available for buffering, set this to 8–10 chunks.

`storage.type filesystem`

Enables filesystem storage for the input plugin. Despite the name,
Fluent Bit uses `mmap` to map chunks to
both memory and disk, providing persistence without sacrificing
performance.

`threaded true`

Runs the input in its own thread, separate from Fluent
Bit's main event loop. This prevents slow inputs from
blocking the entire pipeline.

## Optimize output configuration

Network issues, service outages, and destination throttling can prevent logs from
being delivered. Proper output configuration ensures resilience without data
loss.

When an output flush fails, Fluent Bit can retry the operation. The
following parameters control retry behavior:

`retry_limit`

The maximum retry attempts before dropping records. The default is 1.
For production environments, we recommend 15 or higher, which covers
several minutes of outage with exponential backoff.

`scheduler.base`

The minimum seconds between retries. We recommend 10 seconds.

`scheduler.cap`

The maximum seconds between retries when using exponential backoff. We
recommend 60 seconds.

`workers`

The number of threads for parallel output processing. Multiple workers
allow concurrent flushes, improving throughput when processing many
chunks.

The `Grace` parameter in the `[SERVICE]` section sets the
time Fluent Bit waits during shutdown to flush buffered data. The
`Grace` period must be coordinated with the container's
`stopTimeout`. Ensure that `stopTimeout` exceeds the
`Grace` period to allow Fluent Bit to complete flushing
before receiving `SIGKILL`. For example, if `Grace` is 120
seconds, set `stopTimeout` to 150 seconds.

The following example shows a complete Fluent Bit configuration with
all recommended settings for high-throughput scenarios:

```
[SERVICE]
    # Flush logs every 1 second
    Flush 1
    # Wait 120 seconds during shutdown to flush remaining logs
    Grace 120
    # Directory for filesystem buffering
    storage.path             /var/log/flb-storage/
    # Limit chunks stored 'up' in memory (reduce for memory-constrained environments)
    storage.max_chunks_up    32
    # Flush backlog chunks to destinations during shutdown (prevents log loss)
    storage.backlog.flush_on_shutdown On
    # Minimum seconds between retries
    scheduler.base           10
    # Maximum seconds between retries (exponential backoff cap)
    scheduler.cap            60

[INPUT]
    Name forward
    unix_path /var/run/fluent.sock
    # Run input in separate thread to prevent blocking
    threaded true
    # Enable filesystem buffering for persistence
    storage.type filesystem

[OUTPUT]
    Name cloudwatch_logs
    Match *
    region `us-west-2`
    log_group_name `/aws/ecs/my-app`
    log_stream_name $(ecs_task_id)
    # Use multiple workers for parallel processing
    workers 2
    # Retry failed flushes up to 15 times
    retry_limit 15
    # Maximum disk space for buffered data for this output
    storage.total_limit_size 10G
```

## Use multi-destination logging for

reliability

Sending logs to multiple destinations eliminates single points of failure. For
example, if CloudWatch Logs experiences an outage, logs still reach Amazon S3.

Multi-destination logging provides the following benefits. The Amazon S3 output plugin
also supports compression options such as gzip and Parquet format, which can reduce
storage costs. For more information, see [S3
compression](https://docs.fluentbit.io/manual/pipeline/outputs/s3#compression "https://docs.fluentbit.io/manual/pipeline/outputs/s3#compression") in the Fluent Bit documentation.

Multi-destination logging can provide the following benefits:

- **Redundancy** – If one destination fails,
  logs still reach the other.
- **Recovery** – Reconstruct gaps in one system
  from the other.
- **Durability** – Archive logs in Amazon S3
  for long-term retention.
- **Cost optimization** – Keep recent logs in a
  fast query service like CloudWatch Logs with shorter retention, while archiving all
  logs to lower-cost Amazon S3 storage for long-term retention.

The following Fluent Bit configuration sends logs to both CloudWatch Logs and
Amazon S3:

```
[OUTPUT]
    Name cloudwatch_logs
    Match *
    region `us-west-2`
    log_group_name `/aws/ecs/my-app`
    log_stream_name $(ecs_task_id)
    workers 2
    retry_limit 15

[OUTPUT]
    Name s3
    Match *
    bucket `my-logs-bucket`
    region `us-west-2`
    total_file_size 100M
    s3_key_format /fluent-bit-logs/$(ecs_task_id)/%Y%m%d/%H/%M/$UUID
    upload_timeout 10m
    # Maximum disk space for buffered data for this output
    storage.total_limit_size 5G
```

Both outputs use the same `Match *` pattern, so all records are sent to
both destinations independently. During an outage of one destination, logs continue
flowing to the other while failed flushes accumulate in the filesystem buffer for
later retry.

## Use file-based logging with the tail input

plugin

For high-throughput scenarios where log loss is a critical concern, you can use an
alternative approach: have your application write logs to files on disk, and
configure Fluent Bit to read them using the `tail` input
plugin. This approach bypasses the Docker logging driver layer entirely.

File-based logging with the tail plugin provides the following benefits:

- **Offset tracking** – The tail plugin can
  store file offsets in a database file (using the `DB` option),
  providing durability across Fluent Bit restarts. This helps
  prevent log loss during container restarts.
- **Input-level buffering** – You can configure
  memory buffer limits directly on the input plugin using
  `Mem_Buf_Limit`, providing more granular control over memory
  usage.
- **Avoids Docker overhead** – Logs go directly
  from file to Fluent Bit without passing through Docker's
  log buffers.

To use this approach, your application must write logs to files instead of
`stdout`. Both the application container and the Fluent
Bit container mount a shared volume where the log files are stored.

The following example shows a tail input configuration with best practices:

```
[INPUT]
    Name tail
    # File path or glob pattern to tail
    Path `/var/log/app.log`
    # Database file for storing file offsets (enables resuming after restart)
    DB /var/log/flb_tail.db
    # when true, controls that only fluent-bit will access the database (improves performance)
    DB.locking true
    # Skip long lines instead of skipping the entire file
    Skip_Long_Lines On
    # How often (in seconds) to check for new files matching the glob pattern
    Refresh_Interval 10
    # Extra seconds to monitor a file after rotation to account for pending flush
    Rotate_Wait 30
    # Maximum size of the buffer for a single line
    Buffer_Max_Size 10MB
    # Initial allocation size for reading file data
    Buffer_Chunk_Size 1MB
    # Maximum memory buffer size (tail pauses when full)
    Mem_Buf_Limit 75MB
```

When using the tail input plugin, consider the following:

- Implement log rotation for your application logs to prevent disk
  exhaustion. Monitor the underlying volume metrics to gauge performance.
- Consider settings like `Ignore_Older`,
  `Read_from_Head`, and multiline parsers based on your log
  format.

For more information, see [Tail](https://docs.fluentbit.io/manual/pipeline/inputs/tail "https://docs.fluentbit.io/manual/pipeline/inputs/tail") in the
Fluent Bit documentation. For best practices, see [Tail config with best practices](https://github.com/aws/aws-for-fluent-bit/blob/mainline/troubleshooting/debugging.md#tail-config-with-best-practices "https://github.com/aws/aws-for-fluent-bit/blob/mainline/troubleshooting/debugging.md#tail-config-with-best-practices") in the AWS for Fluent
Bit troubleshooting guide.

## Log directly to FireLens

When the `awsfirelens` log driver is specified in a task definition,
the Amazon ECS container agent injects the following environment variables into the
container:

`FLUENT_HOST`

The IP address that's assigned to the FireLens container.

###### Note

If you're using EC2 with the `bridge` network mode, the
`FLUENT_HOST` environment variable in your
application container can become inaccurate after a restart of the
FireLens log router container (the container with the
`firelensConfiguration` object in its container
definition). This is because `FLUENT_HOST` is a dynamic
IP address and can change after a restart. Logging directly from
the application container to the `FLUENT_HOST` IP
address can start failing after the address changes. For more
information about restarting individual containers, see [Restart individual containers in Amazon ECS tasks with
container restart policies](container-restart-policy.md "container-restart-policy.md").

`FLUENT_PORT`

The port that the Fluent Forward protocol is listening on.

You can use these environment variables to log directly to the Fluent
Bit log router from your application code using the Fluent Forward
protocol, instead of writing to `stdout`. This approach bypasses the
Docker logging driver layer, which provides the following benefits:

- **Lower latency** – Logs go directly to
  Fluent Bit without passing through Docker's logging
  infrastructure.
- **Structured logging** – Send structured log
  data natively without JSON encoding overhead.
- **Better control** – Your application can
  implement its own buffering and error handling logic.

The following Fluent logger libraries support the Fluent Forward protocol and can
be used to send logs directly to Fluent Bit:

- **Go** – [fluent-logger-golang](https://github.com/fluent/fluent-logger-golang "https://github.com/fluent/fluent-logger-golang")
- **Python** – [fluent-logger-python](https://github.com/fluent/fluent-logger-python "https://github.com/fluent/fluent-logger-python")
- **Java** – [fluent-logger-java](https://github.com/fluent/fluent-logger-java "https://github.com/fluent/fluent-logger-java")
- **Node.js** – [fluent-logger-node](https://github.com/fluent/fluent-logger-node "https://github.com/fluent/fluent-logger-node")
- **Ruby** – [fluent-logger-ruby](https://github.com/fluent/fluent-logger-ruby "https://github.com/fluent/fluent-logger-ruby")

## Configure the Docker buffer limit

When you create a task definition, you can specify the number of log lines that are
buffered in memory by specifying the value in `log-driver-buffer-limit`.
This controls the buffer between Docker and Fluent Bit. For more
information, see [Fluentd logging
driver](https://docs.docker.com/engine/logging/drivers/fluentd/ "https://docs.docker.com/engine/logging/drivers/fluentd/") in the Docker documentation.

Use this option when there's high throughput, because Docker might run out of
buffer memory and discard buffer messages so it can add new messages.

Consider the following when using this option:

- This option is supported on EC2 and Fargate type with platform version
  `1.4.0` or later.
- The option is only valid when `logDriver` is set to
  `awsfirelens`.
- The default buffer limit is `1048576` log lines.
- The buffer limit must be greater than or equal to `0` and less
  than `536870912` log lines.
- The maximum amount of memory used for this buffer is the product of the
  size of each log line and the size of the buffer. For example, if the
  application's log lines are on average `2` KiB, a buffer limit
  of 4096 would use at most `8` MiB. The total amount of memory
  allocated at the task level should be greater than the amount of memory
  that's allocated for all the containers in addition to the log driver
  memory buffer.

The following task definition shows how to configure
`log-driver-buffer-limit`:

```
{
    "containerDefinitions": [
        {
            "name": "`my_service_`log_router",
            "image": "public.ecr.aws/aws-observability/aws-for-fluent-bit:3",
            "cpu": 0,
            "memoryReservation": 51,
            "essential": true,
            "firelensConfiguration": {
                "type": "fluentbit"
            }
        },
        {
            "essential": true,
            "image": "public.ecr.aws/docker/library/httpd:latest",
            "name": "app",
            "logConfiguration": {
                "logDriver": "awsfirelens",
                "options": {
                    "Name": "firehose",
                    "region": "us-west-2",
                    "delivery_stream": "my-stream",
                    "log-driver-buffer-limit": "52428800"
                }
            },
            "dependsOn": [
                {
                    "containerName": "`my_service_`log_router",
                    "condition": "START"
                }
            ],
            "memoryReservation": 100
        }
    ]
}
```
