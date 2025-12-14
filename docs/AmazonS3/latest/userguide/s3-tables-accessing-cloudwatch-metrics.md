# Accessing CloudWatch metrics

You can monitor S3 Tables metrics using the CloudWatch Console, the AWS CLI, or the CloudWatch API. This section explains how to access your metrics using these different methods.

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Table buckets**.
3. In the buckets list, choose the name of the bucket that contains the tables you want to see metrics for.
4. Choose the **Metrics** tab.
5. Choose the **View in CloudWatch** in any metrics pane to navigate to the CloudWatch console and see your available metrics in the `AWS/S3/Tables` namespace.
   To list metrics for S3 Tables using the AWS CLI, use the `list-metrics` command with the `--namespace` parameter set to `AWS/S3/Tables`:

```
aws cloudwatch list-metrics --namespace AWS/S3/Tables
```

To get statistics for a specific S3 Tables metric, use the `get-metric-statistics` command. For example:

```
aws cloudwatch get-metric-statistics \
--namespace AWS/S3/Tables \
--metric-name TotalBucketStorage \
--dimensions Name=TableBucketName,Value=MyTableBucket \
--start-time 2025-03-01T00:00:00 \
--end-time 2025-03-02T00:00:00 \
--period 86400 \
--statistics Average
```

## Best Practices

- When retrieving metrics, set the Period value based on the metric's granularity. For daily metrics (like storage metrics), use 86400 seconds (24 hours). For minute-level metrics (like request metrics), use 60 seconds.
- Use dimensions appropriately to filter metrics to the desired scope (table bucket, namespace, or individual table level).
- Consider using metric math to create derived metrics that better match your monitoring needs.

## Related Resources

- [Amazon CloudWatch Concepts](../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md "../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md")
- [Using Amazon CloudWatch Dashboards](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md")
