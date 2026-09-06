

# Monitoring metrics with Amazon CloudWatch
<a name="monitoring-cloudwatch"></a>

You can monitor file systems using Amazon CloudWatch, which collects and processes raw data from Amazon EFS into readable, near real-time metrics. These statistics are recorded for a period of 15 months, so that you can gain a better perspective on how your web application or service is performing.

By default, Amazon EFS metric data is automatically sent to CloudWatch at 1-minute periods, unless noted for some individual metrics. The Amazon EFS console displays a series of graphs based on the raw data from Amazon CloudWatch. Depending on your needs, you might prefer to get data for your file systems from CloudWatch instead of the graphs in the console.

For more information about Amazon CloudWatch, see [What is Amazon CloudWatch?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) in the *Amazon CloudWatch User Guide*.

Amazon EFS CloudWatch metrics are reported as raw *bytes*. Bytes are not rounded to either a decimal or binary multiple of the unit.

**Topics**
+ [CloudWatch metrics for Amazon EFS](efs-metrics.md)
+ [Accessing CloudWatch metrics for Amazon EFS](accessingmetrics.md)
+ [Using CloudWatch metrics for Amazon EFS](how_to_use_metrics.md)
+ [Using metric math with CloudWatch metrics](monitoring-metric-math.md)
+ [Monitoring mount attempt successes and failures](how-to-monitor-mount-status.md)
+ [Creating CloudWatch alarms to monitor Amazon EFS](creating_alarms.md)