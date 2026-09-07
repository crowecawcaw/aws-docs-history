

# Logging WorkSpaces API Calls by Using CloudTrail
<a name="cloudtrail_logging"></a>

The WorkSpaces API is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in WorkSpaces. CloudTrail captures API calls for WorkSpaces as events. The calls captured include calls from the WorkSpaces console and code calls to the WorkSpaces API operations. If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for WorkSpaces. If you don't configure a trail, you can still view the most recent events in the CloudTrail console in **Event history**. Using the information collected by CloudTrail, you can determine the request that was made to WorkSpaces, the IP address from which the request was made, who made the request, when it was made, and additional details.

To learn more about CloudTrail, including how to configure and enable it, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/).

## WorkSpaces Information in CloudTrail
<a name="service-name-info-in-cloudtrail"></a>

CloudTrail is enabled on your AWS account when you create the account. When supported event activity occurs in WorkSpaces, that activity is recorded in a CloudTrail event along with other AWS service events in **Event history**. For example, calls to create, rebuild, or terminate WorkSpaces generate entries in CloudTrail log files. For more information, see [Actions](https://docs.aws.amazon.com/workspaces/latest/api/API_Operations.html).

You can view, search, and download recent events in your AWS account. For more information, see [Viewing Events with CloudTrail Event History](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html).

For an ongoing record of events in your AWS account, including events for WorkSpaces, create a trail. A *trail* enables CloudTrail to deliver log files to an Amazon S3 bucket. By default, when you create a trail in the console, the trail applies to all AWS Regions. The trail logs events from all Regions in the AWS partition and delivers the log files to the Amazon S3 bucket that you specify. Additionally, you can configure other AWS services to further analyze and act upon the event data collected in CloudTrail logs. For more information, see the following:
+ [Overview for Creating a Trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html)
+ [CloudTrail Supported Services and Integrations](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.html#cloudtrail-aws-service-specific-topics-integrations)
+ [Configuring Amazon SNS Notifications for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/getting_notifications_top_level.html)
+ [Receiving CloudTrail Log Files from Multiple Regions](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.html) and [Receiving CloudTrail Log Files from Multiple Accounts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.html)

## Example: WorkSpaces Log File Entry
<a name="understanding-service-name-entries"></a>

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket that you specify. CloudTrail log files contain one or more log entries. An event represents a single request from any source and includes information about the requested action, the date and time of the action, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of the public API calls, so they don't appear in any specific order.

Any sensitive information, such as passwords, authentication tokens, file comments, and file contents are redacted in the log entries. 

The following shows an example of a CloudTrail log entry for WorkSpaces.

```
{
  "Records" : [
    {
      "eventVersion" : "1.02",
      "userIdentity" :
      {
        "type" : "IAMUser",
        "principalId" : "{{user_id}}",
        "arn" : "{{user_arn}}",
        "accountId" : "{{account_id}}",
        "accessKeyId" : "{{access_key_id}}",
        "userName" : "{{username}}"
      },
      "eventTime" : "{{event_time}}",
      "eventSource" : "workspaces.amazonaws.com",
      "eventName" : "DescribeWorkspaces",
      "awsRegion" : "{{region}}",
      "sourceIPAddress" : "{{IP_address}}",
      "userAgent" : "{{user_agent}}",
      "requestParameters" :
      {
        "requestContext" :
        {
          "awsAccountId" : "{{account_id}}"
        }
      },
      "responseElements" : null,
      "requestID" : "{{request_id}}",
      "eventID" : "{{event_id}}",
      "eventType" : "AwsApiCall",
      "recipientAccountId" : "{{account_id}}"
    }
  ]
}
```