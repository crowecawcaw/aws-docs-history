

# Monitoring metrics with Amazon CloudWatch for directory buckets
<a name="cloudwatch-monitoring-directory-buckets"></a>

Amazon CloudWatch metrics for directory buckets can help you understand and improve the performance of applications that use directory buckets. There are several sets of CloudWatch metrics that you can use with directory buckets for the S3 Express One Zone storage class and the S3 One Zone-Infrequent Access (S3 One Zone-IA; Z-IA) storage class in a local zone.

**Daily storage metrics**  
Monitor the amount of data stored in directory buckets, including total size in bytes and number of objects. These storage metrics for S3 Express One Zone are reported once per day and are provided to all customers at no additional cost.

**Request metrics**   
Monitor directory bucket requests to quickly identify and act on operational issues. The metrics are available at 1-minute intervals after some latency for processing. These CloudWatch metrics are billed at the same rate as the Amazon CloudWatch custom metrics. For information about CloudWatch pricing, see [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/). To learn how to opt in to getting these metrics, see [Configuring request metrics for directory buckets](metrics-configurations-directory-buckets.md).  
When enabled, request metrics are reported for all object operations. By default, these 1-minute metrics are available at the directory bucket level. You can also define a filter for the metrics using a shared directory or access point:  
+ **Access point** – Access points are named network endpoints that are attached to directory buckets and simplify managing data access at scale for shared datasets in S3. With the access point filter, you can gain insights into your access point usage. For more information about access points for directory buckets, see [Managing access to shared datasets in directory buckets with access points](access-points-directory-buckets.md).
+ **Directory** – directory buckets use actual directories to organize objects hierarchically. A directory enables you to group similar objects together in a directory bucket. If you filter by directory, objects that are stored in the same directory are included in the metrics configuration.
To align these metrics to specific business applications, workflows, or internal organizations, you can filter on a shared directory or access point. 

All CloudWatch statistics are retained for a period of 15 months so that you can access historical information and gain a better perspective on how your web application or service is performing. For more information about CloudWatch, see [What is Amazon CloudWatch?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) in the *Amazon CloudWatch User Guide*. You may need some additional configurations to your CloudWatch alarms, depending on your use cases. For example, you can use metric math expression to create an alarm. For more information, see [Use CloudWatch metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html), [Use metric math](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html), [Using Amazon CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html), and [Create a CloudWatch alarm based on a metric math expression](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) in the *Amazon CloudWatch User Guide*.

**Best-effort CloudWatch metrics delivery**  
 CloudWatch metrics are delivered on a best-effort basis. Most requests for an Amazon S3 object that have request metrics result in a data point being sent to CloudWatch.

The completeness and timeliness of metrics are not guaranteed. The data point for a particular request might be returned with a timestamp that is later than when the request was actually processed. The data point for a minute might be delayed before being available through CloudWatch, or it might not be delivered at all. CloudWatch request metrics give you an idea of the nature of traffic against your bucket in near-real time. It is not meant to be a complete accounting of all requests.

It follows from the best-effort nature of this feature that the reports available at the [Billing & Cost Management Dashboard](https://console.aws.amazon.com/billing/home?#/) might include one or more access requests that do not appear in the bucket metrics.

For more information, see the following topics.

**Topics**
+ [Metrics and dimensions for directory buckets](metrics-dimensions-directory-buckets.md)
+ [Configuring request metrics for directory buckets](metrics-configurations-directory-buckets.md)