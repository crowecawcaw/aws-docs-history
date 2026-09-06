

# Log AWS Secrets Manager events with AWS CloudTrail
<a name="monitoring-cloudtrail"></a>

AWS CloudTrail records all API calls for Secrets Manager as events, including calls from the Secrets Manager console, as well as several other events for rotation and secret version deletion. For a list of the log entries in Secrets Manager records, see [CloudTrail entries](cloudtrail_log_entries.md).

You can use the CloudTrail console to view the last 90 days of recorded events. For an ongoing record of events in your AWS account, including events for Secrets Manager, create a trail so that CloudTrail delivers log files to an Amazon S3 bucket. See [Creating a trail for your AWS account](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html). You can also configure CloudTrail to receive CloudTrail log files from [multiple AWS accounts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.html) and [AWS Regions](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.html). 

You can configure other AWS services to further analyze and act upon the data collected in CloudTrail logs. See [AWS service integrations with CloudTrail logs](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.html#cloudtrail-aws-service-specific-topics-integrations). You can also get notifications when CloudTrail publishes new log files to your Amazon S3 bucket. See [Configuring Amazon SNS notifications for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/getting_notifications_top_level.html). 

**To retrieve Secrets Manager events from CloudTrail logs (console)**

1. Open the CloudTrail console at [https://console.aws.amazon.com/cloudtrail/](https://console.aws.amazon.com/cloudtrail/).

1. Ensure that the console points to the Region where your events occurred. The console shows only those events that occurred in the selected Region. Choose the Region from the drop-down list in the upper-right corner of the console.

1. In the left-hand navigation pane, choose **Event history**. 

1. Choose **Filter** criteria and/or a **Time range** to help you find the event that you're looking for. For example:

   1. To see all Secrets Manager events, for **Lookup attributes**, choose **Event source**. Then, for **Enter event source**, choose **secretsmanager.amazonaws.com**.

   1. To see all events for a secret, for **Lookup attributes**, choose **Resource name**. Then, for **Enter a resource name**, enter the name of the secret.

1. To see additional details, choose the expand arrow next to the event. To see all of the information available, choose **View event**. 

## AWS CLI
<a name="monitoring-cloudtrail_cli"></a>

**Example Retrieve Secrets Manager events from CloudTrail logs**  
The following [`lookup-events`](https://docs.aws.amazon.com/cli/latest/reference/cloudtrail/lookup-events.html) example looks up Secrets Manager events.  

```
aws cloudtrail lookup-events \
    --region us-east-1 \
    --lookup-attributes AttributeKey=EventSource,AttributeValue=secretsmanager.amazonaws.com
```