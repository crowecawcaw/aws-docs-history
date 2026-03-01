# Logging Amazon AppFlow API calls with AWS CloudTrail

Amazon AppFlow is integrated with AWS CloudTrail, a service that provides a record of actions taken
by a user, role, or an AWS service in Amazon AppFlow. CloudTrail captures all API calls for
Amazon AppFlow as events. The calls captured include calls from the Amazon AppFlow console and
code calls to the Amazon AppFlow API operations. If you create a trail, you can enable
continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for Amazon AppFlow.
If you don't configure a trail, you can still view the most recent events in the CloudTrail
console in **Event history**. Using the information collected by CloudTrail,
you can determine the request that was made to Amazon AppFlow, the IP address from which the
request was made, who made the request, when it was made, and additional details.

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").

## Amazon AppFlow information in CloudTrail

CloudTrail is enabled on your AWS account when you create the account. When activity occurs
in Amazon AppFlow, that activity is recorded in a CloudTrail event along with other AWS service
events in **Event history**. You can view, search, and download recent events
in your AWS account. For more information, see [Viewing Events with CloudTrail Event History](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").

For an ongoing record of events in your AWS account, including events for Amazon AppFlow,
create a trail. A _trail_ enables CloudTrail to deliver log files to an Amazon S3
bucket. By default, when you create a trail in the console, the trail applies to all AWS
Regions. The trail logs events from all Regions in the AWS partition and delivers the log
files to the S3 bucket that you specify. Additionally, you can configure other AWS services
to further analyze and act upon the event data collected in CloudTrail logs. For more information,
see the following:

- [Overview for Creating a Trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [CloudTrail Supported Services and Integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations")
- [Configuring Amazon SNS Notifications for CloudTrail](../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md "../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md")
- [Receiving CloudTrail Log
  Files from Multiple Regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md")
- [Receiving CloudTrail Log
  Files from Multiple Accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")

All actions are logged by CloudTrail and are documented in the [Amazon AppFlow API Reference](../../1.0/APIReference/Welcome.md "../../1.0/APIReference/Welcome.md"). For example,
calls to the [`CreateFlow`](../../1.0/APIReference/API_CreateFlow.md "../../1.0/APIReference/API_CreateFlow.md"), [`CreateConnectorProfile`](../../1.0/APIReference/API_CreateConnectorProfile.md "../../1.0/APIReference/API_CreateConnectorProfile.md") and [`TagResource`](../../1.0/APIReference/API_TagResource.md "../../1.0/APIReference/API_TagResource.md") API
actions generate entries in the CloudTrail log files.

Every event or log entry contains information about who generated the request. The
identity information helps you determine the following:

- Whether the request was made with root or AWS Identity and Access Management (IAM) user credentials.
- Whether the request was made with temporary security credentials for a role or
  federated user.
- Whether the request was made by another AWS service.

For more information, see the [CloudTrail userIdentity
Element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md").

## Understanding Amazon AppFlow log file entries

A trail is a configuration that enables delivery of events as log files to an S3 bucket
that you specify. CloudTrail log files contain one or more log entries. An event represents a single
request from any source and includes information about the requested action, the date and time
of the action, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of
the public API calls, so they don't appear in any specific order.

The following is an example of a CloudTrail log entry generated when you view the details of a
flow using the Amazon AppFlow console. Amazon AppFlow does not log the response elements, as they could
contain sensitive data.

```
{
    "eventVersion": "1.05",
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "123456789012",
        "arn": "arn:aws:iam::123456789012:user/Alice",
        "accountId": "123456789012",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "userName": "Richard"
    },
    "eventTime": "2020-04-23T17:08:09Z",
    "eventSource": "appflow.amazonaws.com",
    "eventName": "DescribeFlows",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "198.51.100.1",
    "userAgent": "console.amazonaws.com",
    "requestParameters": {
        "flowNames": ["my-flow"]
    },
    "responseElements": {
    },
    "requestID": "ba96f0cf-4c4a-4e42-95b5-d6c69EXAMPLE",
    "eventID": "cce710cd-d1f8-44b3-8bd1-75184EXAMPLE",
    "eventType": "AwsApiCall",
    "recipientAccountId": "123456789012"
}
```
