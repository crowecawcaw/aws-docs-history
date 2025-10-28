Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Runtime troubleshooting

This section contains information about diagnosing and fixing runtime issues with your
Managed Service for Apache Flink application.

###### Topics

- [Troubleshooting tools](#troubleshooting-tools "#troubleshooting-tools")
- [Application issues](troubleshooting-symptoms.md "troubleshooting-symptoms.md")
- [Application is restarting](troubleshooting-rt-restarts.md "troubleshooting-rt-restarts.md")
- [Throughput is too slow](troubleshooting-rt-throughput.md "troubleshooting-rt-throughput.md")
- [Unbounded state growth](troubleshooting-rt-stateleaks.md "troubleshooting-rt-stateleaks.md")
- [I/O bound operators](troubleshooting-io-bound-operators.md "troubleshooting-io-bound-operators.md")
- [Upstream or source throttling from a Kinesis data
  stream](troubleshooting-source-throttling.md "troubleshooting-source-throttling.md")
- [Checkpoints](troubleshooting-checkpoints.md "troubleshooting-checkpoints.md")
- [Checkpointing is timing out](troubleshooting-chk-timeout.md "troubleshooting-chk-timeout.md")
- [Checkpoint failure for Apache Beam application](troubleshooting-chk-failure-beam.md "troubleshooting-chk-failure-beam.md")
- [Backpressure](troubleshooting-backpressure.md "troubleshooting-backpressure.md")
- [Data skew](troubleshooting-data-skew.md "troubleshooting-data-skew.md")
- [State skew](troubleshooting-state-skew.md "troubleshooting-state-skew.md")
- [Integrate with resources in
  different Regions](troubleshooting-resources-in-different-regions.md "troubleshooting-resources-in-different-regions.md")

## Troubleshooting tools

The primary tool for detecting application issues is CloudWatch alarms. Using CloudWatch
alarms, you can set thresholds for CloudWatch metrics that indicate error or bottleneck
conditions in your application. For information about recommended CloudWatch alarms,
see [Use CloudWatch Alarms with Amazon Managed Service for Apache Flink](monitoring-metrics-alarms.md "monitoring-metrics-alarms.md").
