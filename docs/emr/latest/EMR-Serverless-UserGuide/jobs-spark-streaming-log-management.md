# Streaming job log

management

Streaming jobs support log rotation for Spark application logs and event logs,
and log compaction for Spark event logs. This helps you manage your
resources effectively.

**Log rotation**

Streaming jobs support log rotation for Spark application logs and event logs. Log rotation prevents long streaming jobs from generating large log files that might take up all
of your available disk space. Log rotation helps you save disk storage and prevents job failures because of low disk space. For more information, refer to
[Rotating logs](rotating-logs.md "rotating-logs.md").

**Log compaction**

Streaming jobs also support log compaction for Spark event logs whenever managed logging is available. For more details about managed logging,
refer to [Logging with managed storage](logging.md#jobs-log-storage-managed-storage "logging.md#jobs-log-storage-managed-storage"). Streaming jobs can run for a
long time, and the amount of event data can build up over time and significantly increase log file sizes. The Spark History Server reads and loads these events into memory for the Spark application UI.
This process can cause high latencies and costs, especially if event logs stored in Amazon S3 are very large.

Log compaction reduces the event log size, so the Spark History Server does not need to load more than 1 GB of event logs at any time. For more information, refer to
[Monitoring and Instrumentation](https://spark.apache.org/docs/latest/monitoring.html "https://spark.apache.org/docs/latest/monitoring.html") in the Apache Spark documentation.
