# Step 2: Configure the Apache Cassandra Spark

Connector

Apache Spark is a general-purpose compute platform that you can configure in different
ways. To configure Spark and the Spark Cassandra Connector for integration with Amazon Keyspaces,
we recommend that you start with the minimum configuration settings described in the
following section, and then increase them later as appropriate for your workload.

- **Create Spark partition sizes smaller than 8
  MBs.**

In Spark, _partitions_ represent an atomic chunk of data
that can be run in parallel. When you are writing data to Amazon Keyspaces with the Spark
Cassandra Connector, the smaller the Spark partition, the smaller the amount of
records that the task is going to write. If a Spark task encounters multiple
errors, it fails after the designated number of retries has been exhausted. To
avoid replaying large tasks and reprocessing a lot of data, keep the size of the
Spark partition small.

- **Use a low concurrent number of writes per executor with
  a large number of retries.**

Amazon Keyspaces returns insufficient capacity errors back to Cassandra drivers as
operation timeouts. You can't address timeouts caused by insufficient capacity
by changing the configured timeout duration because the Spark Cassandra
Connector attempts to retry requests transparently using the
`MultipleRetryPolicy`. To ensure that retries don’t overwhelm the
driver’s connection pool, use a low concurrent number of writes per executor
with a large number of retries. The following code snippet is an example of
this.

```
spark.cassandra.query.retry.count = 500
spark.cassandra.output.concurrent.writes = 3
```

- **Break down the total throughput and distribute it across
  multiple Cassandra sessions.**
  - The Cassandra Spark Connector creates one session for each Spark
    executor. Think about this session as the unit of scale to determine the
    required throughput and the number of connections required.
  - When defining the number of cores per executor and the number of cores
    per task, start low and increase as needed.
  - Set Spark task failures to allow processing in the event of transient
    errors. After you become familiar with your application's traffic
    characteristics and requirements, we recommend setting
    `spark.task.maxFailures` to a bounded value.
  - For example, the following configuration can handle two concurrent
    tasks per executor, per session:

  ```
  spark.executor.instances = configurable -> number of executors for the session.
  spark.executor.cores = 2 -> Number of cores per executor.
  spark.task.cpus = 1 -> Number of cores per task.
  spark.task.maxFailures = -1
  ```

- **Turn off batching.**
  - We recommend that you turn off batching to improve random access
    patterns. The following code snippet is an example of this.

  ```
  spark.cassandra.output.batch.size.rows = 1 (Default = None)
  spark.cassandra.output.batch.grouping.key = none (Default = Partition)
  spark.cassandra.output.batch.grouping.buffer.size = 100 (Default = 1000)
  ```

- **Set `SPARK_LOCAL_DIRS` to a fast, local disk
  with enough space.**
  - By default, Spark saves map output files and resilient distributed
    datasets (RDDs) to a `/tmp` folder. Depending on your
    Spark host’s configuration, this can result in _no space left
    on the device_ style errors.
  - To set the `SPARK_LOCAL_DIRS` environment variable to a
    directory called `/example/spark-dir`, you can use
    the following command.

  ```
  export SPARK_LOCAL_DIRS=/example/spark-dir
  ```
