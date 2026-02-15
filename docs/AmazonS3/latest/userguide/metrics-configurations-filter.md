# Creating a metrics configuration

that filters by prefix, object tag, or access point

There are three types of Amazon CloudWatch metrics for Amazon S3: storage metrics, request
metrics, and replication metrics. Storage metrics are reported once per day and are
provided to all customers at no additional cost. Request metrics are available at
one-minute intervals after some latency for processing. Request metrics are billed at
the standard CloudWatch rate. You must opt in to request metrics by configuring them in the
console or using the Amazon S3 API. [S3 Replication metrics](viewing-replication-metrics.md "viewing-replication-metrics.md") provide detailed metrics for the replication rules in your replication configuration. With replication metrics, you can monitor minute-by-minute progress by tracking bytes pending, operations pending, operations that failed replication, and replication latency.

For more information about CloudWatch metrics for Amazon S3, see [Monitoring metrics with Amazon CloudWatch](cloudwatch-monitoring.md "cloudwatch-monitoring.md").

When you configure CloudWatch metrics, you can create a filter for all the objects in
your bucket, or you can filter the configuration into groups of related objects
within a single bucket. You can filter objects in a bucket for inclusion in a
metrics configuration based on one or more of the following filter types:

- **Object key name prefix** – Although
  the Amazon S3 data model is a flat structure, you can infer a hierarchy by using
  a prefix. The Amazon S3 console supports these prefixes with the concept of
  folders. If you filter by prefix, objects that have the same prefix are
  included in the metrics configuration. For more information about prefixes,
  see [Organizing objects using prefixes](using-prefixes.md "using-prefixes.md").
- **Tag** – You can add tags, which are
  key-value name pairs, to objects. Tags help you find and organize objects
  easily. You can also use tags as filters for metrics configurations. For
  more information about object tags, see [Categorizing your objects using tags](object-tagging.md "object-tagging.md").
- **Access point** – S3 Access Points are
  named network endpoints that are attached to buckets and simplify managing
  data access at scale for shared datasets in S3. When you create an access point
  filter, Amazon S3 includes requests to the access point that you specify in the metrics
  configuration. For more information, see [Monitoring and logging access points](access-points-monitoring-logging.md "access-points-monitoring-logging.md").

###### Note

When you create a metrics configuration that filters by access point,
you must use the access point Amazon Resource Name (ARN), not the access point
alias. Make sure that you use the ARN for the access point itself, not
the ARN for a specific object. For more information about access point ARNs, see
[Using Amazon S3 access points for general purpose buckets](using-access-points.md "using-access-points.md").
If you specify a filter, only requests that operate on single objects can match
the filter and be included in the reported metrics. Requests like [DeleteObjects](../API/multiobjectdeleteapi.md "../API/multiobjectdeleteapi.md") and `ListObjects` requests
don't return any metrics for configurations with filters.

To request more complex filtering, choose two or more elements. Only objects that
have all of those elements are included in the metrics configuration. If you don't
set filters, all of the objects in the bucket are included in the metrics
configuration.

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **General purpose buckets**
3. In the buckets list, choose the name of the bucket that contains
   the objects that you want request metrics for.
4. Choose the **Metrics** tab.
5. Under **Bucket metrics**, choose **View additional charts**.
6. Choose the **Request metrics** tab.
7. Choose **Create filter**.
8. In the **Filter name** box, enter your filter name.

Names can contain only letters, numbers, periods, dashes, and underscores. 9. Under **Filter scope**, choose **Limit the scope of this filter
using a prefix, object tags, and an S3 Access Point, or a combination of all
three**. 10. Under **Filter type**, choose at least one filter type:
**Prefix**, **Object tags**, or **Access
Point**. 11. To define a prefix filter and limit the scope of the filter to a single path, in the
**Prefix** box, enter a prefix. 12. To define an object tags filter, under **Object tags**, choose
**Add tag**, and then enter a tag **Key** and
**Value**. 13. To define an access point filter, in the **S3 Access Point** field, enter the access point ARN, or choose **Browse S3** to navigate to the access point.

###### Important

You cannot enter an access point alias. You must enter the ARN for the access point
itself, not the ARN for a specific object. 14. Choose **Save changes**.

Amazon S3 creates a filter that uses the prefix, tags, or access point that you specified. 15. On the **Request metrics** tab, under **Filters**, choose the filter that you just created.

You have now created a filter that limits the request metrics scope by prefix, object
tags, or access point. About 15 minutes after CloudWatch begins tracking these request metrics, you can
see charts for the metrics on both the Amazon S3 and CloudWatch consoles. Request metrics are billed at
the standard CloudWatch rate. For more information, see [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").

You can also configure request metrics at the bucket level. For information, see [Creating a CloudWatch metrics
configuration for all the objects in your bucket](configure-request-metrics-bucket.md "configure-request-metrics-bucket.md").

1. Install and set up the AWS CLI. For instructions, see [Installing, updating, and uninstalling
   the AWS CLI](../../../cli/latest/userguide/cli-chap-install.md "../../../cli/latest/userguide/cli-chap-install.md") in the _AWS Command Line Interface User Guide_.
2. Open a terminal.
3. To add a metrics configuration, run one of the following commands:

###### Example: To filter by prefix

```
aws s3api put-bucket-metrics-configuration --bucket ``amzn-s3-demo-bucket`` --id `metrics-config-id` --metrics-configuration '{"Id":"`metrics-config-id`", "Filter":{"Prefix":"`prefix1`"}} '
```

###### Example: To filter by tags

```
aws s3api put-bucket-metrics-configuration --bucket ``amzn-s3-demo-bucket`` --id `metrics-config-id` --metrics-configuration '{"Id":"`metrics-config-id`", "Filter":{"Tag": {"Key": "`string`", "Value": "`string`"}} '
```

###### Example: To filter by access point

```
aws s3api put-bucket-metrics-configuration --bucket ``amzn-s3-demo-bucket`` --id `metrics-config-id` --metrics-configuration '{"Id":"`metrics-config-id`", "Filter":{"AccessPointArn":"arn:aws:s3:`Region`:`account-id`:accesspoint/`access-point-name`"}} '
```

###### Example: To filter by prefix, tags, and access point

```
aws s3api put-bucket-metrics-configuration --endpoint https://s3.`Region`.amazonaws.com --bucket ``amzn-s3-demo-bucket`` --id `metrics-config-id` --metrics-configuration '
{
    "Id": "`metrics-config-id`",
    "Filter": {
        "And": {
            "Prefix": "`string`",
            "Tags": [
                {
                    "Key": "`string`",
                    "Value": "`string`"
                }
            ],
            "AccessPointArn": "arn:aws:s3:`Region`:`account-id`:accesspoint/`access-point-name`"
        }
    }
}'
```

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
