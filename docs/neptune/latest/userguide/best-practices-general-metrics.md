# Best practices for using Neptune metrics

To identify performance issues caused by insufficient resources and other common
bottlenecks, you can monitor the metrics available for your Neptune DB cluster.

Monitor performance metrics on a regular basis to gather data about the average, maximum,
and minimum values for a variety of time ranges. This helps identify when performance is
degraded. Using this data, you can set Amazon CloudWatch alarms for particular metric thresholds so you
are alerted if they are reached.

When you set up a new DB cluster and get it running with a typical workload, try to
capture the average, maximum, and minimum values of all of the performance metrics at a number
of different intervals (for example, one hour, 24 hours, one week, two weeks). This gives you
an idea of what is normal. It helps to get comparisons for both peak and off-peak hours of
operation. You can then use this information to identify when performance is dropping below
standard levels, and can set alarms accordingly.

See [Monitoring Neptune Using Amazon CloudWatch](cloudwatch.md "cloudwatch.md") for information about
how to view Neptune metrics.

The following are the most important metrics to start with:

- **BufferCacheHitRatio** — The percentage
  of requests that are served by the buffer cache. Cache misses add significant latency to
  query execution. If the cache hit ratio is below 99.9% and latency is an issue for your
  application, consider upgrading the instance type to cache more data in memory.
- **CPU utilization** — Percentage of computer processing
  capacity used. High values for CPU consumption might be appropriate, depending on your
  query-performance goals.
- **Freeable memory** — How much RAM is available on the DB
  instance, in megabytes. Neptune has its own memory manager, so this metric may be lower
  than you expect. A good sign that you should consider upgrading your instance class to one
  with more RAM is if queries often throw out-of-memory exceptions.
  The red line in the **Monitoring** tab metrics is marked at 75% for CPU
  and Memory Metrics. If instance memory consumption frequently crosses that line, check your
  workload and consider upgrading your instance to improve query performance.
