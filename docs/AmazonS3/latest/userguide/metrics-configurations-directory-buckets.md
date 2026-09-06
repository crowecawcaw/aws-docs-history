

# Configuring request metrics for directory buckets
<a name="metrics-configurations-directory-buckets"></a>

You can configure request metrics for directory buckets to monitor the operational performance of your S3 Express One Zone storage. Request metrics are available at 1-minute intervals and help you quickly identify and act on operational issues.

You can configure request metrics for directory buckets using the Amazon S3 console, the AWS Command Line Interface (AWS CLI), or the Amazon S3 REST API.

## Using the S3 console
<a name="metrics-configuration-console-directory-buckets"></a>

You can use the Amazon S3 console to configure request metrics for your directory buckets.

**To configure request metrics for a directory bucket**

1. Sign in to the and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. In the left navigation pane, choose **Directory buckets**.

1. In the buckets list, choose the name of the directory bucket that contains the objects you want request metrics for.

1. Choose the **Metrics** tab.

1. Under **Bucket metrics**, choose **View additional charts**.

1. Choose the **Request metrics** tab.

1. Choose **Create filter**.

1. In the **Filter name** box, enter your filter name.

   Names can only contain letters, numbers, periods, dashes, and underscores. We recommend using the name `EntireBucket` for a filter that applies to all objects.

1. Under **Filter scope**, choose one of the following:
   + **This filter applies to all objects in the bucket** – You don't specify a filter.
   + **Limit the scope of this filter using directory or access point** – You specify a filter. To limit the scope, you can filter by directory or access point.

   You can also define a filter so that the metrics are only collected and reported on a subset of objects in the directory bucket.

1. If you chose to limit the scope of the filter, specify the filter details:
   + To filter by **directory**, enter a directory name.
   + To filter by **access point**, enter the access point ARN.

1. Choose **Save changes**.

1. On the **Request metrics** tab, under **Filters**, choose the filter that you just created.

   After about 15 minutes, CloudWatch begins tracking these request metrics. You can see them on the **Request metrics** tab. You can see graphs for the metrics on the Amazon S3 or CloudWatch console. Request metrics are billed at the standard CloudWatch rate. For more information, see [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/).

## Using the AWS CLI
<a name="metrics-configuration-cli-directory-buckets"></a>

You can use the AWS CLI to configure request metrics for your directory buckets.

1. Install and set up the AWS CLI. For instructions, see [Installing, updating, and uninstalling the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-set-up.html) in the *AWS Command Line Interface User Guide*.

1. Open a terminal.

1. Run the following command to add a metrics configuration.

   ```
   aws s3api put-bucket-metrics-configuration --endpoint https://s3express-control.{{region-code}}.amazonaws.com --bucket {{directory-bucket-name}} --id {{metrics-config-id}} --metrics-configuration '{"Id":"{{metrics-config-id}}"}'
   ```

## Using the REST API
<a name="metrics-configuration-rest-directory-buckets"></a>

You can use the Amazon S3 REST API to configure request metrics for your directory buckets. When using the REST API with directory buckets, you must use the S3 Express One Zone endpoint with the regional control endpoint in the format: `https://s3express-control.{{region-code}}.amazonaws.com`.

For more information about the REST API operations, see the following topics in the *Amazon S3 API Reference*:
+ [PUT Bucket metrics](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTMetricConfiguration.html)
+ [GET Bucket metrics](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketGETMetricConfiguration.html)
+ [DELETE Bucket metrics](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketDELETEMetricConfiguration.html)
+ [LIST Bucket metrics](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketListMetricConfigurations.html)