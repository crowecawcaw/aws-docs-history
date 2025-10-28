# Production monitoring

You should establish a baseline for normal DAX performance in your environment, by measuring performance at
various times and under different load conditions. As you monitor DAX, you should consider storing historical
monitoring data. This stored data gives you a baseline from which to compare current performance data, identify
normal performance patterns and performance anomalies, and devise methods to address issues.

To establish a baseline, you should, at minimum, monitor the following items both during load testing and in
production.

- CPU utilization and throttled requests, so that you can determine whether you might need to use a larger node type in your cluster. The CPU utilization of your cluster is available through the `CPUUtilization` CloudWatch metric. The average stat on this metric provides an average CPU utilization view across all the nodes in your cluster. For cluster scaling decisions, we recommend that you use the maximum stat which is the maximum utilization across all the nodes.

###### Note

AWS has improved the `CPUUtilization` metric's granularity. You might observe changes to the metric starting from 2024-05-17 to 2024-06-22.

- Operation latency (as measure on the client side) should remain consistent within your application's
  latency requirements.
- Error rates should remain low, as seen from the
  `ErrorRequestCount`, `FaultRequestCount`, and
  `FailedRequestCount` CloudWatch metrics.
- Network bytes consumption, so that you can determine if you
  should use more nodes or a larger node type in your cluster. To monitor consumption,
  you can set alerts on `BaselineNetworkBytesInUtilization` and
  `BaselineNetworkBytesOutUtilization` metrics available in CloudWatch, which indicates
  percentage consumption of available network bandwidth for your instance type, for ingress
  and egress traffic respectively.
- Cache memory utilization and evicted size, so that you can determine
  whether the cluster's node type has sufficient memory to hold your working
  set, and if not, switch to a larger node type.

###### Note

In case of a large number of cache misses and writes, cache memory utilization can increase up to 100%
and may cause availability downtime.

- Client connections, so that you can monitor for any unexplained spikes in
  connections to the cluster.
