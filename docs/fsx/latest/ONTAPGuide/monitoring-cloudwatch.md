

# Monitoring with Amazon CloudWatch
<a name="monitoring-cloudwatch"></a>

You can monitor file systems using Amazon CloudWatch, which collects and processes raw data from Amazon FSx for NetApp ONTAP into readable, near real-time metrics. These statistics are retained for a period of 15 months, so that you can access historical information to determine how your file system is performing. FSx for ONTAP metric data is automatically sent to CloudWatch at 1-minute periods by default. For more information about CloudWatch, see [What is Amazon CloudWatch?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) in the *Amazon CloudWatch User Guide*.

**Note**  
By default, FSx for ONTAP sends metric data to CloudWatch at 1-minute periods except for the following metrics that are sent in 5-minute intervals:   
`FileServerDiskThroughputBalance`
`FileServerDiskIopsBalance`

CloudWatch metrics for FSx for ONTAP are organized into four categories, which are defined by the dimensions that are used to query each metric. For more information about dimensions, see [Dimensions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Dimension) in the *Amazon CloudWatch User Guide*.
+ **File system metrics**: File-system-level performance and storage capacity metrics.
+ **File server metrics**: File-server-level metrics.
+ **Detailed file system aggregate metrics**: Detailed file system metrics per aggregate.
+ **Detailed file system metrics**: File-system-level storage metrics per storage tier (SSD and capacity pool).
+ **Volume metrics**: Per-volume performance and storage capacity metrics.
+ **Detailed volume metrics**: Per-volume storage capacity metrics by storage tier or by the type of data (user, snapshot, or other).

All CloudWatch metrics for FSx for ONTAP are published to the `AWS/FSx` namespace in CloudWatch. 

**Topics**
+ [Accessing CloudWatch metrics](accessingmetrics.md)
+ [Monitoring in the Amazon FSx console](monitor-throughput-cloudwatch.md)
+ [File system metrics](file-system-metrics.md)
+ [Second-generation file system metrics](so-file-system-metrics.md)
+ [Volume metrics](volume-metrics.md)