# Troubleshooting latency issues

This section contains troubleshooting steps for replication latency.

To troubleshoot latency, do the following:

- First, determine the type and amount of latency for the task. Check the task's Table
  Statistics section from the DMS console or CLI. If the counters are changing, then data transmission
  is in progress. Check the `CDCLatencySource` and`CDCLatencyTarget` metrics
  together to determine if there's a bottleneck during CDC.
- If high `CDCLatencySource` or `CDCLatencyTarget` metrics indicate
  a bottleneck in your replication, check the following:

      + If `CDCLatencySource` is high and `CDCLatencyTarget` is equal to
       `CDCLatencySource`, this indicates that there is a bottleneck in your source endpoint,
       and AWS DMS is writing data to the target smoothly. See
       [Troubleshooting source latency issues](CHAP_Troubleshooting_Latency_Source.md "CHAP_Troubleshooting_Latency_Source.md") following.
      + If `CDCLatencySource` is low and `CDCLatencyTarget` is high,
       this indicates that there is a bottleneck in your target endpoint,
       and AWS DMS is reading data from the source smoothly. See
       [Troubleshooting target latency issues](CHAP_Troubleshooting_Latency_Target.md "CHAP_Troubleshooting_Latency_Target.md") following.
      + If `CDCLatencySource` is high and `CDCLatencyTarget` is
       significantly higher than `CDCLatencySource`, this indicates bottlenecks on both source
       reads and target writes. Investigate source latency first, and then investigate target latency.

  For information about monitoring DMS task metrics, see [Monitoring AWS DMS tasks](CHAP_Monitoring.md "CHAP_Monitoring.md").
