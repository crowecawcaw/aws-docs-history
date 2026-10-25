

This guide documents the new AWS Wickr administration console, released on March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide-classic/what-is-wickr.html).

# Monitoring and management
<a name="monitor-manage"></a>

## CloudWatch dashboards
<a name="cloudwatch-dashboards"></a>

Complete the following procedure to access CloudWatch dashboards.

1. Open the AWS Management Console for Wickr at [https://console.aws.amazon.com/wickr/](https://console.aws.amazon.com/wickr/).

1. On the **Networks** page, select the network name to navigate to that network.

1. In the navigation pane, choose **CloudWatch**.

1. Select **Dashboards**, and then select `WickrDataRetentionService-[NetworkID]`.

The deployment automatically creates CloudWatch dashboards showing:
+ **Error Rate**: Failed message processing attempts
+ **Storage Metrics**: S3 bucket size and object count

## Automatic alarms
<a name="automatic-alarms"></a>

Pre-configured CloudWatch alarms notify you of:
+ **Processing Failures**: Any messages failing to decrypt or store

Complete the following procedure to configure alarm notifications.

1. Open the AWS Management Console for Wickr at [https://console.aws.amazon.com/wickr/](https://console.aws.amazon.com/wickr/).

1. On the **Networks** page, select the network name to navigate to that network.

1. In the navigation pane, choose **CloudWatch**.

1. Choose **Alarms**.

1. Select a **Wickr Data Retention** alarm.

1. Choose **Actions**, and then choose **Edit**.

1. Add SNS topic for email and SMS notifications.

## Recommended: Add an alarm on your Amazon S3 bucket
<a name="s3-bucket-alarm"></a>

The automatic alarms notify you when messages fail to process. They do not notify you if retained data stops arriving in your Amazon S3 bucket. We recommend that you create a CloudWatch alarm on your retention bucket that notifies you when no new objects are written for a period of time. This helps you detect a gap in retained data early.

The alarm also goes off if no messages are sent on your network for the whole alarm period, because no new objects are written when there are no messages. To avoid false alarms, set the alarm period longer than your network's normal quiet periods. Because each period then usually covers several writes, the alarm detects a prolonged gap in retained data but may not detect a single failed write.

This alarm uses Amazon S3 request metrics, which are not turned on by default. Request metrics are billed at CloudWatch custom metric rates. Before you create the alarm, turn on request metrics for your retention bucket. For more information, see [Creating a CloudWatch metrics configuration for all the objects in your bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/configure-request-metrics-bucket.html) in the *Amazon S3 User Guide*.

Amazon S3 does not publish a request metric data point when there are no requests. The alarm treats missing data as breaching so that it fires when no new objects are written.

Complete the following procedure to create the alarm.

1. Open the CloudWatch console, choose **Alarms**, and then choose **Create alarm**.

1. Choose **Select metric**, choose **S3**, and then choose **Request metrics**. Choose the `PutRequests` metric for your retention bucket.

1. Set **Statistic** to **Sum** and **Period** to a value that matches how often your network normally sends messages, for example **1 hour**.

1. Set the condition to **Lower than** `1`.

1. Under **Additional configuration**, set **Missing data treatment** to **Treat missing data as bad (breaching threshold)**.

1. Add SNS topic for email and SMS notifications.

1. Name the alarm, and then choose **Create alarm**.

## Additional recommended alarms
<a name="recommended-alarms"></a>

The template creates one alarm, which detects decryption errors. An alarm on missing Amazon S3 writes can detect when retained data stops arriving. The following alarms can detect other failures that neither of those alarms covers. Send all of them to an Amazon SNS topic that your operations team monitors.

The following table lists the additional alarms, their conditions, and what each one tells you.


| Alarm | Metric and condition | What it tells you | 
| --- | --- | --- | 
| Bucket errors | Amazon S3 `4xxErrors` and `5xxErrors` (Sum) on the retention bucket, filter `WickrEncryptedBucketMetric`, is 1 or greater. | Writes are being rejected, for example by a changed bucket policy or a service control policy. | 
| Key unavailable | An EventBridge rule on the CloudTrail events `DisableKey` and `ScheduleKeyDeletion` for your retention key, and a metric filter on AWS KMS `AccessDenied` errors. | Disabling or deleting the key, or editing its policy, immediately stops retention. | 
| Decryption workflow failures | Step Functions `ExecutionsFailed`, `ExecutionsTimedOut`, and `ExecutionThrottled` for the `decryption` state machine is 1 or greater. | An on-demand decryption you requested did not complete. The dashboard graphs these values but does not alarm on them. | 
| Unexpected storage growth or drop | Amazon S3 `BucketSizeBytes` with a CloudWatch anomaly detection band. | A sustained deviation from your normal volume of retained data. | 

Additional recommendations:
+ Review the **KMS Key Success** graph on the dashboard regularly. Retention activity produces a steady stream of AWS KMS requests, so a flat line is an early sign of a stoppage.
+ Periodically send a test message in the network from a test user and confirm that the corresponding object appears in the retention bucket. This verifies the full path from client to bucket.
+ Keep CloudTrail enabled in the account and Region of your retention key so that key usage and policy changes are auditable. The decryption state machine also writes execution logs to the `/aws/vendedlogs/states/` CloudWatch Logs group, retained for one year.

For more information about creating alarms, see [Using CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) in the *Amazon CloudWatch User Guide*.