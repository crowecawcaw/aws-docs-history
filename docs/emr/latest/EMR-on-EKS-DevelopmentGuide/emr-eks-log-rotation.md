

# Using Spark event log rotation
<a name="emr-eks-log-rotation"></a>

With Amazon EMR 6.3.0 and later, you can turn on the Spark event log rotation feature for Amazon EMR on EKS. Instead of generating a single event log file, this feature rotates the file based on your configured time interval and removes the oldest event log files.

Rotating Spark event logs can help you avoid potential issues with a large Spark event log file generated for long running or streaming jobs. For example, you start a long running Spark job with an event log enabled with the `persistentAppUI` parameter. The Spark driver generates an event log file. If the job runs for hours or days and there is a limited disk space on the Kubernetes node, the event log file can consume all available disk space. Turning on the Spark event log rotation feature solves the problem by splitting the log file into multiple files and removing the oldest files.

**Note**  
This feature only works with Amazon EMR on EKS. Amazon EMR running on Amazon EC2 doesn't support Spark event log rotation.

**Note**  
On Amazon EMR on EKS, time-based event log rotation (the `spark.eventLog.rotation.*` parameters described on this page) caps Spark event log growth based on a time interval, and is the supported mechanism for doing so. The open-source size-based rolling event log (`spark.eventLog.rolling.*`) is **not supported** for event log upload on Amazon EMR on EKS. When rolling is enabled, the Spark driver writes size-based segment files. The Amazon EMR on EKS managed log-shipping component (the agent that uploads event logs so applications appear in the Spark History Server) does not collect these files. As a result, the application does not appear in the Spark History Server even though the job runs successfully.  
If your event logs are not appearing in the Spark History Server, check whether `spark.eventLog.rolling.enabled` is set, and switch to event log rotation as described in the following section.

To turn on the Spark event log rotation feature, configure the following Spark parameters:
+ `spark.eventLog.rotation.enabled` ‐ turns on log rotation. It is disabled by default in the Spark configuration file. Set it to true to turn on this feature. 
+ `spark.eventLog.rotation.interval` ‐ specifies time interval for the log rotation. The minimum value is 60 seconds. The default value is 300 seconds. 
+ `spark.eventLog.rotation.minFileSize` ‐ specifies a minimum file size to rotate the log file. The minimum and default value is 1 MB. 
+ `spark.eventLog.rotation.maxFilesToRetain` ‐ specifies how many rotated log files to keep during cleanup. The valid range is 1 to 10. The default value is 2. 

You can specify these parameters in the `sparkSubmitParameters` section of the [`StartJobRun`](emr-eks-jobs-submit.md) API, as the following example shows.

```
"sparkSubmitParameters": "--class org.apache.spark.examples.SparkPi --conf spark.eventLog.rotation.enabled=true --conf spark.eventLog.rotation.interval=300 --conf spark.eventLog.rotation.minFileSize=1m --conf spark.eventLog.rotation.maxFilesToRetain=2"
```

## Migrating from the rolling event log to rotation
<a name="emr-eks-log-rotation-migrate-rolling"></a>

If you currently use the open-source size-based rolling event log, replace the `spark.eventLog.rolling.*` parameters with the rotation parameters. Rotation caps the event log by a time *interval* (with a minimum file size) rather than purely by file size, so choose an interval and minimum file size that suit your job's event rate. Remove all `spark.eventLog.rolling.*` settings when you switch. The following table maps each rolling parameter to its rotation equivalent.


| Rolling parameter (not supported) | Rotation parameter (supported) | 
| --- | --- | 
| spark.eventLog.rolling.enabled=true | spark.eventLog.rotation.enabled=true | 
| spark.eventLog.rolling.maxFileSize (caps by size) | spark.eventLog.rotation.interval (caps by time; minimum 60 seconds, default 300 seconds), used with spark.eventLog.rotation.minFileSize (minimum and default 1 MB) | 
| spark.eventLog.rolling.maxFilesToRetain | spark.eventLog.rotation.maxFilesToRetain (valid range 1 to 10, default 2) | 