

This guide documents the new AWS Wickr administration console, released on March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide-classic/what-is-wickr.html).

# Monitor the data retention bot for your Wickr network
<a name="data-retention-bot-monitoring"></a>

The following topics describe the CloudWatch alarms that we recommend for the data retention bot.

## Recommended: Add an alarm on your Amazon S3 bucket
<a name="dr-bot-s3-bucket-alarm"></a>

If you store data in an Amazon S3 bucket, we recommend that you create a CloudWatch alarm that notifies you when the data retention bot stops writing new objects to the bucket. This helps you detect a gap in retained data early.

The bot writes a new object each time it rotates its received messages file. It rotates the file when a message arrives after the `WICKRIO_COMP_TIMEROTATE` interval has passed, so it writes nothing while no messages are sent on your network. This alarm will fire if no messages are sent over the network during this period. To avoid false alarms, set the alarm period longer than `WICKRIO_COMP_TIMEROTATE` and your network's normal quiet periods. Since the alarm period is recommended to be set greater than the `WICKRIO_COMP_TIMEROTATE` setting to prevent alarming when there are extended periods of no message activity, this alarm may not detect gaps in individual writes to the Amazon S3 bucket but helps you detect a prolonged gap. For more information, see [Environment variables to configure data retention bot in AWS Wickr](data-retention-bot-env-variables.md).

This alarm uses Amazon S3 request metrics, which are not turned on by default. Request metrics are billed at CloudWatch custom metric rates. Before you create the alarm, turn on request metrics for the bucket that you set in `WICKRIO_S3_BUCKET_NAME`. For more information, see [Creating a CloudWatch metrics configuration for all the objects in your bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/configure-request-metrics-bucket.html) in the *Amazon S3 User Guide*.

Amazon S3 does not publish a request metric data point when there are no requests. The alarm treats missing data as breaching so that it fires when no new objects are written.

Complete the following procedure to create the alarm.

1. Open the CloudWatch console, choose **Alarms**, and then choose **Create alarm**.

1. Choose **Select metric**, choose **S3**, and then choose **Request metrics**. Choose the `PutRequests` metric for your data retention bucket.

1. Set **Statistic** to **Sum** and **Period** to a value that matches how often your network normally sends messages and is greater than your `WICKRIO_COMP_TIMEROTATE` value, for example **1 hour**.

1. Set the condition to **Lower than** `1`.

1. Under **Additional configuration**, set **Missing data treatment** to **Treat missing data as bad (breaching threshold)**.

1. Add SNS topic for email and SMS notifications.

1. Name the alarm, and then choose **Create alarm**.