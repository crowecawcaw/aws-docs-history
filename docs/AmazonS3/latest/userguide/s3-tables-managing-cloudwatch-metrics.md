

# Managing CloudWatch metrics
<a name="s3-tables-managing-cloudwatch-metrics"></a>

Storage metrics are enabled by default for all Amazon S3 tables and table buckets. You can enable or disable additional Request metrics through the console, AWS Command Line Interface (AWS CLI), or AWS SDKs.

## Prerequisites
<a name="prerequisites"></a>
+ Requires `s3table:PutTableBucketMetricsConfiguration` IAM permission

**Note**  
S3 Tables Request metrics are billed at the same rate as CloudWatch custom metrics.

## Using the AWS Management Console
<a name="using-console-managing"></a>

To enable or disable additional metrics

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. In the left navigation pane, choose **Table buckets**.

1. In the buckets list, choose the name of the table bucket that contains the tables you want to request metrics for.

1. Choose the **Metrics** tab.

1. From the Request metrics panel, choose **Edit**.

1. Select **Enabled** or **Disabled**, then **Save changes**.

## Using the AWS CLI
<a name="using-cli-managing"></a>

These examples show how to enable or disable request metrics for table buckets by using the AWS CLI. To use these commands, replace the {{user input placeholders}} with your own information.

**Example : To enable request metrics for a table bucket:**  

```
aws s3tables put-table-bucket-metrics-configuration \
--table-bucket-arn arn:aws:s3tables:{{us-east-1}}:{{111122223333}}:bucket/{{amzn-s3-demo-table-bucket}}
```

**Example : To disable request metrics for a table bucket:**  

```
aws s3tables delete-table-bucket-metrics-configuration \
--table-bucket-arn arn:aws:s3tables:{{us-east-1}}:{{111122223333}}:bucket/{{amzn-s3-demo-table-bucket}}
```