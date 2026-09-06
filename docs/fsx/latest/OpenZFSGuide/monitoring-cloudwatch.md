

# Monitoring with Amazon CloudWatch
<a name="monitoring-cloudwatch"></a>

You can monitor Amazon FSx using CloudWatch, which collects raw data and processes it into readable, near real-time metrics. These statistics are kept for 15 months so that you can access historical information and gain a better perspective on how your application or service is performing. You can also set alarms that watch for certain thresholds and send notifications or take actions when those thresholds are met. For more information about CloudWatch, see [What is Amazon CloudWatch?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) in the *Amazon CloudWatch User Guide*.

FSx for OpenZFS publishes CloudWatch metrics in the following domains:
+ **Network I/O metrics** – Measure activity between clients that access the file system and the file server.
+ **File server metrics** – Measure network throughput utilization, file server CPU and memory, and file server disk throughput and IOPS utilization.
+ **Disk metrics** – Measure activity between the file server and the SSD storage.
+ **Storage capacity metrics** – Measure storage usage.

The following diagram illustrates an FSx for OpenZFS file system, its components, and its metric domains.

![FSx for Windows File Server reports metrics in CloudWatch.](http://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/images/metrics-overview-FSxZ.png)


By default, FSx for OpenZFS sends metric data to CloudWatch at 1-minute intervals. The following are exceptions to the default, and are sent at 5-minute intervals:
+ `FileServerDiskThroughputBalance`
+ `FileServerDiskIopsBalance`

**Note**  
Metrics might not be published during ﬁle system maintenance for Single-AZ (non-HA) ﬁle systems, or during failover and failback between the primary and secondary file servers for Single-AZ (HA) and Multi-AZ (HA) file systems.

**Topics**
+ [Using Amazon FSx for OpenZFS CloudWatch metrics](how_to_use_metrics.md)
+ [Accessing CloudWatch metrics](accessingmetrics.md)
+ [Amazon FSx for OpenZFS metrics and dimensions](fsx-openzfs-metrics.md)
+ [Performance warnings and recommendations](performance-insights-FSxZ.md)
+ [Creating CloudWatch alarms to monitor metrics](creating_alarms.md)