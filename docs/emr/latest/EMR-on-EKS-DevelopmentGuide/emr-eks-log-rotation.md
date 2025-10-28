# Using Spark event log rotation

With Amazon EMR 6.3.0 and later, you can turn on the Spark event log rotation feature for
Amazon EMR on EKS. Instead of generating a single event log file, this feature rotates the file based
on your configured time interval and removes the oldest event log files.

Rotating Spark event logs can help you avoid potential issues with a large Spark event log
file generated for long running or streaming jobs. For example, you start a long running Spark
job with an event log enabled with the `persistentAppUI` parameter. The Spark
driver generates an event log file. If the job runs for hours or days and there is a limited
disk space on the Kubernetes node, the event log file can consume all available disk space.
Turning on the Spark event log rotation feature solves the problem by splitting the log file
into multiple files and removing the oldest files.

###### Note

This feature only works with Amazon EMR on EKS. Amazon EMR running on Amazon EC2 doesn't support Spark
event log rotation.

To turn on the Spark event log rotation feature, configure the following Spark
parameters:

- `spark.eventLog.rotation.enabled` ‐ turns on log rotation. It is
  disabled by default in the Spark configuration file. Set it to true to turn on this
  feature.
- `spark.eventLog.rotation.interval` ‐ specifies time interval for the
  log rotation. The minimum value is 60 seconds. The default value is 300 seconds.
- `spark.eventLog.rotation.minFileSize` ‐ specifies a minimum file size
  to rotate the log file. The minimum and default value is 1 MB.
- `spark.eventLog.rotation.maxFilesToRetain` ‐ specifies how many
  rotated log files to keep during cleanup. The valid range is 1 to 10. The default value is

2.  You can specify these parameters in the `sparkSubmitParameters` section of the
    [StartJobRun](emr-eks-jobs-submit.md "emr-eks-jobs-submit.md") API, as the following
    example shows.

```
"sparkSubmitParameters": "--class org.apache.spark.examples.SparkPi --conf spark.eventLog.rotation.enabled=true --conf spark.eventLog.rotation.interval=300 --conf spark.eventLog.rotation.minFileSize=1m --conf spark.eventLog.rotation.maxFilesToRetain=2"
```
