

# Managing log retention
<a name="sal-cw-retention"></a>

When you deliver server access logs to CloudWatch Logs, log retention is controlled by the retention setting on the log group. You set retention when you create the log group, or update it at any time using the CloudWatch Logs console, AWS CLI, or API.

Retention options range from 1 day to 10 years, or you can choose to never expire logs. When log data reaches the end of its retention period, it is automatically deleted from the log group.

If you have enabled the S3 Tables mirror for your log group, the mirrored data in the S3 table follows the same retention. When log data expires from the log group, the corresponding records are removed from the S3 table. You do not need to manage retention separately for the S3 table.

**To set or update log group retention**

1. Open the CloudWatch Logs console at [CloudWatch Logs console](https://console.aws.amazon.com/cloudwatch/home#logsV2:log-groups).

1. Select the log group that receives your server access logs.

1. Choose **Actions**, then **Edit retention setting**.

1. Select a retention period and choose **Save**.

To set retention using the AWS CLI:

```
aws logs put-retention-policy \
  --log-group-name "/aws/vendedlogs/s3/DOC-EXAMPLE-BUCKET/S3_SERVER_ACCESS_LOGS" \
  --retention-in-days 90
```

For more information, see [Change log data retention in CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html#SettingLogRetention) in the *CloudWatch Logs User Guide*.