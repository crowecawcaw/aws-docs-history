

# Logging Savings Plans API Calls with AWS CloudTrail
<a name="logging-using-cloudtrail"></a>

AWS Savings Plans is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in Savings Plans. CloudTrail captures all API calls for Savings Plans as events. The calls captured include calls from the AWS Management Console and code calls to the Savings Plans API operations. If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for Savings Plans. If you don't configure a trail, you can still view the most recent events in the CloudTrail console in **Event history**. Using the information collected by CloudTrail, you can determine the request that was made to Savings Plans, the IP address from which the request was made, who made the request, when it was made, and additional details. 

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/).

## Savings Plans Information in CloudTrail
<a name="service-name-info-in-cloudtrail"></a>

CloudTrail is enabled on your AWS account when you create the account. When activity occurs in Savings Plans, that activity is recorded in a CloudTrail event along with other AWS service events in **Event history**. You can view, search, and download recent events in your AWS account. For more information, see [Viewing Events with CloudTrail Event History](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html). 

For an ongoing record of events in your AWS account, including events for Savings Plans, create a trail. A *trail* enables CloudTrail to deliver log files to an Amazon S3 bucket. By default, when you create a trail in the console, the trail applies to all AWS Regions. The trail logs events from all Regions in the AWS partition and delivers the log files to the Amazon S3 bucket that you specify. Additionally, you can configure other AWS services to further analyze and act upon the event data collected in CloudTrail logs. For more information, see the following: 
+ [Overview for Creating a Trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html)
+ [CloudTrail Supported Services and Integrations](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.html#cloudtrail-aws-service-specific-topics-integrations)
+ [Configuring Amazon SNS Notifications for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/getting_notifications_top_level.html)
+ [Receiving CloudTrail Log Files from Multiple Regions](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.html) and [Receiving CloudTrail Log Files from Multiple Accounts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.html)

All Savings Plans actions are logged by CloudTrail and are documented in the [AWS Savings Plans API Reference](https://docs.aws.amazon.com/savingsplans/latest/APIReference/). For example, calling the `CreateSavingsPlan` action generates an entry in the CloudTrail logs.

Every event or log entry contains information about who generated the request. The identity information helps you determine the following: 
+ Whether the request was made with root or user role credentials.
+ Whether the request was made with temporary security credentials for a role or federated user.
+ Whether the request was made by another AWS service.

For more information, see the [CloudTrail userIdentity Element](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html).

## Understanding Savings Plans Log File Entries
<a name="understanding-service-name-entries"></a>

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket that you specify. CloudTrail log files contain one or more log entries. An event represents a single request from any source and includes information about the requested action, the date and time of the action, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of the public API calls, so they don't appear in any specific order.

The following is an example CloudTrail log entry for the `CreateSavingsPlan` action.

```
{
    "eventVersion": "1.05",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "[principalId]/[userName]",
        "arn": "arn:aws:sts::[accountId]:assumed-role/[userName]/",
        "accountId": "[accountId]",
        "accessKeyId": "[accessKeyId]",
        "sessionContext": {
            "attributes": {
                "mfaAuthenticated": "false",
                "creationDate": "2019-10-01T00:00:00Z"
            },
            "sessionIssuer": {
                "type": "Role",
                "principalId": "[principalId]",
                "arn": "arn:aws:iam::[accountId]:role/[userName]",
                "accountId": "[accountId]",
                "userName": "[userName]"
            }
        }
    },
    "eventTime": "2019-10-01T00:00:00Z",
    "eventSource": "savingsplans.amazonaws.com",
    "eventName": "CreateSavingsPlan",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "127.0.0.1",
    "userAgent": "[userAgent]",
    "requestParameters": {
        "commitment": "2.50",
        "savingsPlanOfferingId": "[savingsPlanOfferingId]",
        "clientToken": "[clientToken]",
        "tags": {
            "tag-key": "tag-value"
        }
    },
    "responseElements": {
        "savingsPlanId": "[savingsPlanId]"
    },
    "requestID": "[requestId]",
    "eventID": "[eventId]",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "recipientAccountId": "[accountId]"
}
```