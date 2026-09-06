

# Deleting a metrics filter
<a name="delete-request-metrics-filter"></a>

You can delete an Amazon CloudWatch request metrics filter if you no longer need it. When you delete a filter, you stop being charged for request metrics that use that *specific filter*. However, charges still apply for any other filters that remain. 

You cannot undo a filter deletion. After you delete a filter, you can no longer use it for request metrics.

To create a request metrics filter, see the following topics:
+ [Creating a CloudWatch metrics configuration for all the objects in your bucket](configure-request-metrics-bucket.md)
+ [Creating a metrics configuration that filters by prefix, object tag, or access point](metrics-configurations-filter.md)

## Using the S3 console
<a name="delete-request-metrics-filter-console"></a>

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. In the left navigation pane, choose **General purpose buckets**.

1. In the buckets list, choose the name of the bucket you want to delete a request metrics filter for.

1. Choose the **Metrics** tab.

1. Under **Bucket metrics**, choose **View additional charts**.

1. Choose the **Request metrics** tab.

1. Choose **Manage filters**.

1. Choose your filter.
**Important**  
Deleting a filter cannot be undone.

1. Choose **Delete**.

   Amazon S3 deletes your filter.

## Using the REST API
<a name="delete-request-metrics-filter-rest"></a>

You can also add metrics configurations programmatically with the Amazon S3 REST API. For more information about adding and working with metrics configurations, see the following topics in the *Amazon Simple Storage Service API Reference*:
+ [PUT Bucket Metric Configuration](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTMetricConfiguration.html)
+ [GET Bucket Metric Configuration](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketGETMetricConfiguration.html)
+ [List Bucket Metric Configuration](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTListBucketMetricsConfiguration.html)
+ [DELETE Bucket Metric Configuration](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTDeleteBucketMetricsConfiguration.html)