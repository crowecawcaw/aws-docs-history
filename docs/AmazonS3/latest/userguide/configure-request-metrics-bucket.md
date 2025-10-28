# Creating a CloudWatch metrics

configuration for all the objects in your bucket

When you configure request metrics, you can create a CloudWatch metrics configuration
for all the objects in your bucket, or you can filter by prefix, object tag, or
access point. The procedures in this topic show you how to create a configuration
for all the objects in your bucket. To create a configuration that filters by object
tag, prefix, or access point, see [Creating a metrics configuration
that filters by prefix, object tag, or access point](metrics-configurations-filter.md "metrics-configurations-filter.md").

There are three types of Amazon CloudWatch metrics for Amazon S3: storage metrics, request
metrics, and replication metrics. Storage metrics are reported once per day and are
provided to all customers at no additional cost. Request metrics are available at
one-minute intervals after some latency for processing. Request metrics are billed at
the standard CloudWatch rate. You must opt in to request metrics by configuring them in the
console or using the Amazon S3 API. [S3 Replication metrics](viewing-replication-metrics.md "viewing-replication-metrics.md") provide detailed metrics for the replication rules in your replication configuration. With replication metrics, you can monitor minute-by-minute progress by tracking bytes pending, operations pending, operations that failed replication, and replication latency.

For more information about CloudWatch metrics for Amazon S3, see [Monitoring metrics with Amazon CloudWatch](cloudwatch-monitoring.md "cloudwatch-monitoring.md").

You can add metrics configurations to a bucket using the Amazon S3 console, the
AWS Command Line Interface (AWS CLI), or the Amazon S3 REST API.

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **General purpose buckets**.
3. In the buckets list, choose the name of the bucket that contains
   the objects you want request metrics for.
4. Choose the **Metrics** tab.
5. Under **Bucket metrics**, choose **View additional
   charts**.
6. Choose the **Request metrics** tab.
7. Choose **Create filter**.
8. In the **Filter name** box, enter your filter name.

Names can only contain letters, numbers, periods, dashes, and underscores. We recommend
using the name `EntireBucket` for a filter that applies to all objects. 9. Under **Filter scope**, choose **This filter applies to all
objects in the bucket**.

You can also define a filter so that the metrics are only collected and reported on a
subset of objects in the bucket. For more information, see [Creating a metrics configuration
that filters by prefix, object tag, or access point](metrics-configurations-filter.md "metrics-configurations-filter.md"). 10. Choose **Save changes**. 11. On the **Request metrics** tab, under **Filters**, choose the filter that you just created.

After about 15 minutes, CloudWatch begins tracking these request metrics. You can see them on the **Request metrics** tab. You can see
graphs for the metrics on the Amazon S3 or CloudWatch console. Request metrics are billed at the
standard CloudWatch rate. For more information, see [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").
You can also add metrics configurations programmatically with the Amazon S3 REST API.
For more information about adding and working with metrics configurations, see the following topics in the
_Amazon Simple Storage Service API Reference_:

- [PUT Bucket
  Metric Configuration](../API/RESTBucketPUTMetricConfiguration.md "../API/RESTBucketPUTMetricConfiguration.md")
- [GET Bucket
  Metric Configuration](../API/RESTBucketGETMetricConfiguration.md "../API/RESTBucketGETMetricConfiguration.md")
- [List
  Bucket Metric Configuration](../API/RESTListBucketMetricsConfiguration.md "../API/RESTListBucketMetricsConfiguration.md")
- [DELETE
  Bucket Metric Configuration](../API/RESTDeleteBucketMetricsConfiguration.md "../API/RESTDeleteBucketMetricsConfiguration.md")

1. Install and set up the AWS CLI. For instructions, see [Installing, updating, and
   uninstalling the AWS CLI](../../../cli/latest/userguide/cli-chap-getting-set-up.md "../../../cli/latest/userguide/cli-chap-getting-set-up.md") in the
   _AWS Command Line Interface User Guide_.
2. Open a terminal.
3. Run the following command to add a metrics configuration.

```
aws s3api put-bucket-metrics-configuration --endpoint https://s3.us-west-2.amazonaws.com --bucket `bucket-name` --id `metrics-config-id` --metrics-configuration '{"Id":"`metrics-config-id`"}'
```
