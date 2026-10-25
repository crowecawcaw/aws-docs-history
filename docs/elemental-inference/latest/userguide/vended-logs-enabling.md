

# Enabling logs
<a name="vended-logs-enabling"></a>

To enable logging, confirm the prerequisites, and then set up delivery in the console or with the CloudWatch Logs API.

## Prerequisites
<a name="vended-logs-prereqs"></a>

Elemental Inference uses CloudWatch Logs vended logs to deliver application logs for each feed. To enable logging, you will need permissions to the log destination that you specify. To see the required permissions for each choice of logging destination, view the corresponding pages in the *Amazon CloudWatch Logs User Guide*:
+ [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-infrastructure-V2-CloudWatchLogs.html)
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-infrastructure-V2-S3.html)
+ [Amazon Data Firehose](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-infrastructure-V2-Firehose.html)

In addition, your IAM user or role must include the `elemental-inference:AllowVendedLogDeliveryForResource` permission for any feed you would like to receive logs for. See the following example to grant permissions for any feed.

------
#### [ JSON ]

****  

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ServiceLevelAccessForLogDelivery",
            "Effect": "Allow",
            "Action": [
                "elemental-inference:AllowVendedLogDeliveryForResource"
            ],
            "Resource": "arn:aws:elemental-inference:{{region}}:{{123456789012}}:feed/*"
        }
    ]
}
```

------

To set up log delivery in the console, ensure that you have additional [Console-specific permissions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-infrastructure-V2-console.html). For more information about the permissions to manage log delivery, see [Logging that requires additional permissions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-vended-logs-permissions-V2.html).

## Supported log types
<a name="vended-logs-types"></a>

Elemental Inference supports the following log type:
+ `APPLICATION_LOGS`: Records processing activity for a feed at the `INFO`, `WARN`, and `ERROR` levels. Use these logs to troubleshoot a feed and monitor its health.

## Using the console
<a name="vended-logs-console"></a>

**To enable logging using the console**

1. Open the [Elemental Inference console](https://console.aws.amazon.com/elemental-inference/).

1. Create a feed, or open the details page of an existing feed. For instructions on creating a feed, see [Step A: Create the feed in Elemental Inference](create-feed.md). For instructions on working with an existing feed, see [Work with existing Elemental Inference feeds](elemental-inference-modify-delete.md).

1. On the feed details page, choose the **Log delivery** tab. Add a log delivery, and set the following:
   + The logging destination: CloudWatch Logs, Amazon S3, or Firehose.
   + The destination resource: a log group for CloudWatch Logs, a bucket for Amazon S3, or a stream for Firehose.

1. Verify that the log delivery appears under the **Log delivery** tab on the feed details page.

After delivery is active, you can view recent feed logs on the **Monitoring** tab of the feed details page. For more information, see [Monitoring tab](monitoring-inference-via-console.md#monitor-console-monitoring-tab).

**Note**  
To view recent feed logs in the console, you must set up at least one log delivery to CloudWatch Logs.

## Using the CloudWatch Logs API
<a name="vended-logs-api"></a>

In CloudWatch Logs, you create three elements to represent the pieces of log delivery. For more information about these elements, see [CreateDelivery](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.html) in the *Amazon CloudWatch Logs API Reference*.

**To enable logging using the CloudWatch Logs API**

1. Get the Amazon Resource Name (ARN) of your feed. A feed ARN uses the format `arn:aws:elemental-inference:{{region}}:{{account-id}}:feed/{{feed-id}}`.

1. Call [PutDeliverySource](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.html) to create a delivery source for the feed. Pass the feed ARN as the `resourceArn`, and set `logType` to `APPLICATION_LOGS`.

   ```
   {
     "name": "my-feed-delivery-source",
     "resourceArn": "arn:aws:elemental-inference:us-west-2:111122223333:feed/abc123example",
     "logType": "APPLICATION_LOGS"
   }
   ```

1. Call [PutDeliveryDestination](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestination.html) to configure where to store the logs. Choose CloudWatch Logs, Amazon S3, or Firehose, and specify the ARN of that destination.

   To deliver logs to another account, use [PutDeliveryDestinationPolicy](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestinationPolicy.html) in the destination account. This policy grants delivery from the source account.

1. Call [CreateDelivery](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.html) to link the delivery source to the delivery destination.

1. To confirm that delivery is set up, call [ListDeliveries](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_ListDeliveries.html) and verify that your delivery appears in the results.