# Configuring request metrics for directory buckets

You can configure request metrics for directory buckets to monitor the operational performance of your S3 Express One Zone storage. Request metrics are available at 1-minute intervals and help you quickly identify and act on operational issues.

You can configure request metrics for directory buckets using the Amazon S3 console, the AWS Command Line Interface (AWS CLI), or the Amazon S3 REST API.

You can use the Amazon S3 console to configure request metrics for your directory buckets.

###### To configure request metrics for a directory bucket

1. Sign in to the and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Directory buckets**.
3. In the buckets list, choose the name of the directory bucket that contains the objects you want request metrics for.
4. Choose the **Metrics** tab.
5. Under **Bucket metrics**, choose **View additional charts**.
6. Choose the **Request metrics** tab.
7. Choose **Create filter**.
8. In the **Filter name** box, enter your filter name.

Names can only contain letters, numbers, periods, dashes, and underscores. We recommend using the name `EntireBucket` for a filter that applies to all objects. 9. Under **Filter scope**, choose one of the following:

    * **This filter applies to all objects in the bucket** – You don't specify a filter.
    * **Limit the scope of this filter using directory or access point** – You specify a filter. To limit the scope, you can filter by directory or access point.

You can also define a filter so that the metrics are only collected and reported on a subset of objects in the directory bucket. 10. If you chose to limit the scope of the filter, specify the filter details:

    * To filter by **directory**, enter a directory name.
    * To filter by **access point**, enter the access point ARN.

11. Choose **Save changes**.
12. On the **Request metrics** tab, under **Filters**, choose the filter that you just created.

After about 15 minutes, CloudWatch begins tracking these request metrics. You can see them on the **Request metrics** tab. You can see graphs for the metrics on the Amazon S3 or CloudWatch console. Request metrics are billed at the standard CloudWatch rate. For more information, see [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").
You can use the AWS CLI to configure request metrics for your directory buckets.

1. Install and set up the AWS CLI. For instructions, see [Installing, updating, and
   uninstalling the AWS CLI](../../../cli/latest/userguide/cli-chap-getting-set-up.md "../../../cli/latest/userguide/cli-chap-getting-set-up.md") in the
   _AWS Command Line Interface User Guide_.
2. Open a terminal.
3. Run the following command to add a metrics configuration.

```
aws s3api put-bucket-metrics-configuration --endpoint https://s3express-control.`region-code`.amazonaws.com --bucket `directory-bucket-name` --id `metrics-config-id` --metrics-configuration '{"Id":"`metrics-config-id`"}'
```

You can use the Amazon S3 REST API to configure request metrics for your directory buckets. When using the REST API with directory buckets, you must use the S3 Express One Zone endpoint with the regional control endpoint in the format: `https://s3express-control.`region-code`.amazonaws.com`.

For more information about the REST API operations, see the following topics in the _Amazon S3 API Reference_:

- [PUT Bucket metrics](../API/RESTBucketPUTMetricConfiguration.md "../API/RESTBucketPUTMetricConfiguration.md")
- [GET Bucket metrics](../API/RESTBucketGETMetricConfiguration.md "../API/RESTBucketGETMetricConfiguration.md")
- [DELETE Bucket metrics](../API/RESTBucketDELETEMetricConfiguration.md "../API/RESTBucketDELETEMetricConfiguration.md")
- [LIST Bucket metrics](../API/RESTBucketListMetricConfigurations.md "../API/RESTBucketListMetricConfigurations.md")
