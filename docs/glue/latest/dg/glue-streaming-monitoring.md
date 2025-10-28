# About monitoring AWS Glue streaming jobs

Monitoring your streaming job is a critical part of building your ETL pipeline. Apart from using the Spark UI, you can also use Amazon CloudWatch to monitor the metrics. Below is a list of streaming metrics emitted by the AWS Glue framework. For a complete list of all the AWS Glue metrics, see [Monitoring AWS Glue using Amazon CloudWatch metrics](monitoring-awsglue-with-cloudwatch-metrics.md "monitoring-awsglue-with-cloudwatch-metrics.md").

AWS Glue uses a structured streaming framework to process the input events. You can either use the Spark API directly in your code or leverage the `ForEachBatch` provided by `GlueContext`, which publishes these metrics. To understand these metrics, we need to first understand `windowSize`.

**windowSize**: `windowSize` is the micro-batch interval that you provide. If you specify a window size of 60 seconds, the AWS Glue streaming job will wait for 60 seconds (or more if the previous batch hasn’t completed by then) before it will read data in a batch from the streaming source and apply the transformations provided in `ForEachBatch`. This is also referred to as the trigger interval.

Lets review the metrics in greater detail to understand the health and performance characteristics.

###### Note

The metrics are emitted every 30 seconds. If your `windowSize` is less than 30 seconds then the reported metrics are an aggregation. For example say your `windowSize` is 10 seconds and you are steadily processing 20 records per micro-batch. In this scenario, the emitted metric value for numRecords would be 60.

A metric is not emitted if there is no data available for it. Also, in case of the consumer lag metric, you have to enable the feature to get metrics for it.

## How to get the best performance

Spark will try to create one task per shard, to read from, in the Amazon Kinesis stream. The data in each shard becomes a partition. It will then distribute these tasks across the executors/workers, depending of the number of cores on each worker (the number of cores per worker depends on the worker type you select `G.025X`, `G.1X`, etc). However it is non-deterministic how the tasks are distributed. All tasks are executed in parallel on their respective cores. If there are more shards than the number of available executor cores, the tasks are queued up.

You can use a combination of the above metrics and the number of shards, to provision your executors for a stable load with some room for bursts. It is recommend that you run a few iterations of your job in order to determine the approximate number of workers. For an unstable/spiky workload you can do the same by setting up autoscaling and max workers.

Set the `windowSize` as per the SLA requirement of your business. For example, if your business requires that the processed data cannot be more than 120 seconds stale, then set your `windowSize` to at least 60 seconds such that your average consumer lag is less than 120 seconds (refer to the section on consumer lag above). From there depending on the `numRecords` and number of shards, plan for the capacity in DPUs making sure your `batchProcessingTimeInMs` is less than 70% of your `windowSize` most of the time.

###### Note

Hot shards can cause data skew which means that some shards/partitions are much bigger than the others. This may cause some tasks that are running in parallel to take longer time causing straggler tasks. As a result, the next batch can't start until all tasks from the previous one complete, this will impact the `batchProcessingTimeInMillis` and the max lag.
