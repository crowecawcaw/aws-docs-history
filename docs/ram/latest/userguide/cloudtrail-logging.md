# Logging AWS RAM API calls with AWS CloudTrail

AWS RAM is integrated with AWS CloudTrail, a service that provides a record of actions
taken by a user, role, or an AWS service in AWS RAM. CloudTrail captures all API calls for
AWS RAM as events. The calls captured include calls from the AWS RAM console and
code calls to the AWS RAM API operations. If you create a trail, you can enable
continuous delivery of CloudTrail events to an Amazon S3 bucket that you specify, including events for
AWS RAM. If you don't configure a trail, you can still view the most recent events in
the CloudTrail console in **Event history**. Use the information collected by
CloudTrail to determine the request that was made to AWS RAM, the requesting IP address, the
requester, when it was made, and additional details.

For more information about CloudTrail, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").

## AWS RAM information in CloudTrail

CloudTrail is enabled on your AWS account when you create the account. When activity
occurs in AWS RAM, that activity is recorded in a CloudTrail event along with other
AWS service events in **Event history**. You can view, search, and
download recent events in your AWS account. For more information, see [Viewing Events with CloudTrail Event
History](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").

For an ongoing record of events in your AWS account, including events for
AWS RAM, create a trail. A _trail_ enables CloudTrail to deliver log
files to an Amazon S3 bucket. By default, when you create a trail in the console, the trail
applies to all AWS Regions. The trail logs events from all Regions in the AWS
partition and delivers the log files to the Amazon S3 bucket that you specify. Additionally,
you can configure other AWS services to further analyze and act upon the event data
collected in CloudTrail logs. For more information, see the following:

- [Creating a
  trail for your AWS account](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [AWS service integrations with CloudTrail logs](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations")
- [Configuring
  Amazon SNS Notifications for CloudTrail](../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md "../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md")
- [Receiving CloudTrail log files from multiple Regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md") and [Receiving CloudTrail log files from multiple accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")

All AWS RAM actions are logged by CloudTrail and are documented in the [AWS RAM API Reference](../APIReference.md "../APIReference.md"). For example, calls to the
`CreateResourceShare`, `AssociateResourceShare`, and
`EnableSharingWithAwsOrganization` actions generate entries in the CloudTrail
log files.

Every event or log entry contains information that helps you determine who made the
request.

- AWS account root credentials
- Temporary security credentials from an AWS Identity and Access Management (IAM) role or federated
  user.
- Long-term security credentials from an IAM user.
- Another AWS service.

For more information, see the [CloudTrail userIdentity
element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md").

## Understanding AWS RAM log file

entries

A trail is a configuration that enables delivery of events as log files to an Amazon S3
bucket that you specify. CloudTrail log files contain one or more log entries. An event
represents a single request from any source and includes information about the requested
action, the date and time of the action, request parameters, and so on. CloudTrail log files
aren't an ordered stack trace of the public API calls, so they don't appear in any
specific order.

The following example shows a CloudTrail log entry for the `CreateResourceShare`
action.

```
{
    "eventVersion": "1.05",
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "NOPIOSFODNN7EXAMPLE",
        "arn": "arn:aws:iam::111122223333:user/admin",
        "accountId": "111122223333",
        "accessKeyId": "BCDIOSFODNN7EXAMPLE",
        "userName": "admin"
    },
    "eventTime": "2018-11-03T04:23:19Z",
    "eventSource": "ram.amazonaws.com",
    "eventName": "CreateResourceShare",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "192.0.1.0",
    "userAgent": "aws-cli/1.16.2 Python/2.7.10 Darwin/16.7.0 botocore/1.11.2",
    "requestParameters": {
        "name": "foo"
    },
    "responseElements": {
        "resourceShare": {
            "allowExternalPrincipals": true,
            "name": "foo",
            "owningAccountId": "111122223333",
            "resourceShareArn": "arn:aws:ram:us-east-1:111122223333:resource-share/EXAMPLE0-1234-abcd-1212-987656789098",
            "status": "ACTIVE"
        }
    },
    "requestID": "EXAMPLE0-abcd-1234-mnop-987654567876",
    "eventID": "EXAMPLE0-1234-abcd-hijk-543234565434",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "recipientAccountId": "111122223333"
}
```
