

# Runtime troubleshooting
<a name="troubleshooting-runtime"></a>

This section contains information about diagnosing and fixing runtime issues with your Managed Service for Apache Flink application.

**Topics**
+ [Troubleshooting tools](#troubleshooting-tools)
+ [Application issues](troubleshooting-symptoms.md)
+ [Application is restarting](troubleshooting-rt-restarts.md)
+ [Throughput is too slow](troubleshooting-rt-throughput.md)
+ [Unbounded state growth](troubleshooting-rt-stateleaks.md)
+ [I/O bound operators](troubleshooting-io-bound-operators.md)
+ [Upstream or source throttling from a Kinesis data stream](troubleshooting-source-throttling.md)
+ [Checkpoints](troubleshooting-checkpoints.md)
+ [Checkpointing is timing out](troubleshooting-chk-timeout.md)
+ [Checkpoint failure for Apache Beam application](troubleshooting-chk-failure-beam.md)
+ [Backpressure](troubleshooting-backpressure.md)
+ [Data skew](troubleshooting-data-skew.md)
+ [State skew](troubleshooting-state-skew.md)
+ [Integrate with resources in different Regions](troubleshooting-resources-in-different-regions.md)

## Troubleshooting tools
<a name="troubleshooting-tools"></a>

The primary tool for detecting application issues is CloudWatch alarms. Using CloudWatch alarms, you can set thresholds for CloudWatch metrics that indicate error or bottleneck conditions in your application. For information about recommended CloudWatch alarms, see [Use CloudWatch Alarms with Amazon Managed Service for Apache Flink](monitoring-metrics-alarms.md).