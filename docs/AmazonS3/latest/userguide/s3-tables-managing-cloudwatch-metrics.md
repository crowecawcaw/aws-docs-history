# Managing CloudWatch metrics

Storage metrics are enabled by default for all Amazon S3 tables and table buckets. You can enable or disable additional Request metrics through the console, AWS CLI, or SDKs.

## Prerequisites

- Requires `s3table:PutTableBucketMetricsConfiguration` IAM permission

###### Note

S3 Tables Request metrics are billed at the same rate as CloudWatch custom metrics.

## Using the AWS Management Console

To enable or disable additional metrics

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Table buckets**.
3. In the buckets list, choose the name of the table bucket that contains the tables you want to request metrics for.
4. Choose the **Metrics** tab.
5. From the Request metrics panel, choose **Edit**.
6. Select **Enabled** or **Disabled**, then **Save changes**.
