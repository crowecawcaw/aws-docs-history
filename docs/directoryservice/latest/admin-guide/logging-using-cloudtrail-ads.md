

# Logging AWS Directory Service API calls using AWS CloudTrail
<a name="logging-using-cloudtrail-ads"></a>

The AWS Managed Microsoft AD API is integrated with AWS CloudTrail, a service that captures API calls made by or on behalf of AWS Managed Microsoft AD in your AWS account and delivers the log files to an Amazon S3 bucket that you specify. CloudTrail captures API calls from the AWS Managed Microsoft AD console and from code calls to the AWS Managed Microsoft AD APIs. Using the information collected by CloudTrail, you can determine what request was made to AWS Managed Microsoft AD, the source IP address from which the request was made, who made the request, when it was made, and so on. To learn more about CloudTrail, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/).

## AWS Managed Microsoft AD Information in CloudTrail
<a name="service-name-info-in-cloudtrail"></a>

CloudTrail is enabled on your AWS account when you create the account. When activity occurs in AWS Managed Microsoft AD, that activity is recorded in a CloudTrail event along with other AWS service events in **Event history**. You can view, search, and download recent events in your AWS account. For more information, see [Viewing Events with CloudTrail Event History](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html). 

For an ongoing record of events in your AWS account, including events for AWS Managed Microsoft AD, create a trail. A *trail* enables CloudTrail to deliver log files to an Amazon S3 bucket. By default, when you create a trail in the console, the trail applies to all AWS Regions. The trail logs events from all Regions in the AWS partition and delivers the log files to the Amazon S3 bucket that you specify. Additionally, you can configure other AWS services to further analyze and act upon the event data collected in CloudTrail logs. For more information, see the following: 
+ [Overview for Creating a Trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html)
+ [CloudTrail Supported Services and Integrations](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.html#cloudtrail-aws-service-specific-topics-integrations)
+ [Configuring Amazon SNS Notifications for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/getting_notifications_top_level.html)
+ [Receiving CloudTrail Log Files from Multiple Regions](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.html) and [Receiving CloudTrail Log Files from Multiple Accounts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.html)

When CloudTrail logging is enabled in your AWS account, all API calls made to AWS Managed Microsoft AD actions are tracked in log files. AWS Managed Microsoft AD records are written together with other AWS service records in a log file. CloudTrail determines when to create and write to a new file based on a time period and file size. All calls made to the Directory Service API or CLI calls are logged by CloudTrail.

Every log entry contains information about who generated the request. The user identity information in the log helps you determine whether the request was made with root or IAM user credentials, with temporary security credentials for a role or federated user, or by another AWS service. For more information, see the **userIdentity** field in the [CloudTrail Event Reference](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/event_reference_top_level.html).

You can store your log files in your bucket for as long as you want, but you can also define Amazon S3 lifecycle rules to archive or delete log files automatically. By default, your log files are encrypted by using Amazon S3 server-side encryption (SSE).

You can choose to have CloudTrail publish Amazon SNS notifications when new log files are delivered if you want to take quick action upon log file delivery. For more information, see [Configuring Amazon SNS Notifications](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/getting_notifications_top_level.html).

You can also aggregate AWS Managed Microsoft AD log files from multiple AWS Regions and AWS accounts into a single Amazon S3 bucket. For more information, see [Aggregating CloudTrail Log Files to a Single Amazon S3 Bucket](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/aggregating_logs_top_level.html).

## Understanding AWS Managed Microsoft AD Log File Entries
<a name="understanding-service-name-entries"></a>

CloudTrail log files can contain one or more log entries, where each entry is made up of multiple JSON-formatted events. A log entry represents a single request from any source and includes information about the requested action, any parameters, the date and time of the action, and so on. The log entries are not guaranteed to be in any particular order; that is, they are not an ordered stack trace of the public API calls.

Sensitive information, such as passwords, authentication tokens, file comments, and file contents are redacted in the log entries.

The following example shows an example of a CloudTrail log entry for AWS Managed Microsoft AD:

```
{
  "Records" : [
    {
      "eventVersion" : "1.02",
      "userIdentity" :
      {
        "type" : "IAMUser",
        "principalId" : "{{<user_id>}}",
        "arn" : "{{<user_arn>}}",
        "accountId" : "{{<account_id>}}",
        "accessKeyId" : "{{<access_key_id>}}",
        "userName" : "{{<username>}}"
      },
      "eventTime" : "{{<event_time>}}",
      "eventSource" : "ds.amazonaws.com",
      "eventName" : "CreateDirectory",
      "awsRegion" : "{{<region>}}",
      "sourceIPAddress" : "{{<IP_address>}}",
      "userAgent" : "{{<user_agent>}}",
      "requestParameters" :
      {
        "name" : "{{<name>}}",
        "shortName" : "{{<short_name>}}",
        "vpcSettings" :
        {
          "vpcId" : "{{<vpc_id>}}",
          "subnetIds" : [
            "{{<subnet_id_1>}}",
            "{{<subnet_id_2>}}"
          ]
        },
        "type" : "{{<size>}}",
        "setAsDefault" : {{<option>}},
        "password" : "***OMITTED***"
      },
      "responseElements" :
      {
        "requestId" : "{{<request_id>}}",
        "directoryId" : "{{<directory_id>}}"
      },
      "requestID" : "{{<request_id>}}",
      "eventID" : "{{<event_id>}}",
      "eventType" : "AwsApiCall",
      "recipientAccountId" : "{{<account_id>}}"
    }
  ]
}
```