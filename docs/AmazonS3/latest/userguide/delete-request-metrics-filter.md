# Deleting a metrics filter

You can delete an Amazon CloudWatch request metrics filter if you no longer need it. When you
 delete a filter, you are no longer charged for request metrics that use that
 *specific filter*. However, you will continue to be charged for any
 other filter configurations that exist. 

When you delete a filter, you can no longer use the filter for request metrics. Deleting a
 filter cannot be undone. 

For information about creating a request metrics filter, see the following topics:


* [Creating a CloudWatch metrics
 configuration for all the objects in your bucket](configure-request-metrics-bucket.md "configure-request-metrics-bucket.md")
* [Creating a metrics configuration
 that filters by prefix, object tag, or access point](metrics-configurations-filter.md "metrics-configurations-filter.md")
1. Sign in to the AWS Management Console and open the Amazon S3 console at
 [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **General purpose buckets**.
3. In the buckets list, choose the name of the bucket you want to delete a request metrics filter for.
4. Choose the **Metrics** tab.
5. Under **Bucket metrics**, choose **View
 additional charts**.
6. Choose the **Request metrics** tab.
7. Choose **Manage filters**.
8. Choose your filter.


###### Important

Deleting a filter cannot be undone.
9. Choose **Delete**.


Amazon S3 deletes your filter.
You can also add metrics configurations programmatically with the Amazon S3 REST API.
 For more information about adding and working with metrics configurations, see the following topics in the
 *Amazon Simple Storage Service API Reference*:


* [PUT Bucket
 Metric Configuration](../API/RESTBucketPUTMetricConfiguration.md "../API/RESTBucketPUTMetricConfiguration.md")
* [GET Bucket
 Metric Configuration](../API/RESTBucketGETMetricConfiguration.md "../API/RESTBucketGETMetricConfiguration.md")
* [List
 Bucket Metric Configuration](../API/RESTListBucketMetricsConfiguration.md "../API/RESTListBucketMetricsConfiguration.md")
* [DELETE
 Bucket Metric Configuration](../API/RESTDeleteBucketMetricsConfiguration.md "../API/RESTDeleteBucketMetricsConfiguration.md")
