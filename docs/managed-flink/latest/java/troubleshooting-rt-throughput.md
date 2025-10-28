Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Throughput is too slow

If your application is not processing incoming streaming data quickly enough,
it will perform poorly and become unstable. This section describes symptoms and
troubleshooting steps for this condition.

## Symptoms

This condition can have the following symptoms:

- If the data source for your application is a Kinesis stream, the stream's
  `millisbehindLatest` metric continually increases.
- If the data source for your application is an Amazon MSK cluster, the cluster's
  consumer lag metrics continually increase. For more information, see
  [Consumer-Lag Monitoring](../../../msk/latest/developerguide/consumer-lag.md "../../../msk/latest/developerguide/consumer-lag.md") in the [Amazon MSK Developer Guide](../../../msk/latest/developerguide/what-is-msk.md "../../../msk/latest/developerguide/what-is-msk.md").
- If the data source for your application is a different service or source,
  check any available consumer lag metrics or data available.

## Causes and solutions

There can be many causes for slow application throughput. If your application is not keeping up with input, check the following:

- If throughput lag is spiking and then tapering off, check if the application is restarting. Your application will
  stop processing input while it restarts, causing lag to spike. For information about application failures, see
  [Application is restarting](troubleshooting-rt-restarts.md "troubleshooting-rt-restarts.md").
- If throughput lag is consistent, check to see if your application is optimized for performance. For information on
  optimizing your application's performance, see [Troubleshoot performance issues](performance-troubleshooting.md "performance-troubleshooting.md").
- If throughput lag is not spiking but continuously increasing, and your application is optimized for performance,
  you must increase your application resources. For information on increasing application resources, see
  [Implement application scaling](how-scaling.md "how-scaling.md").
- If your application reads from a Kafka cluster in a different Region and `FlinkKafkaConsumer` or `KafkaSource` are mostly idle (high `idleTimeMsPerSecond` or
  low `CPUUtilization`) despite high consumer lag, you can increase the value for `receive.buffer.byte`, such as 2097152. For more information, see the high latency environment section in
  [Custom MSK configurations](../../../msk/latest/developerguide/msk-configuration-properties.md "../../../msk/latest/developerguide/msk-configuration-properties.md").

For troubleshooting
steps for slow throughput or consumer lag increasing in the application source, see
[Troubleshoot performance issues](performance-troubleshooting.md "performance-troubleshooting.md").
