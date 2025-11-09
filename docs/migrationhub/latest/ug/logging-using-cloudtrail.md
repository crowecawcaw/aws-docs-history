AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Logging Migration Hub API calls with AWS CloudTrail

Migration Hub is integrated with AWS CloudTrail, a service that provides a record of actions taken
by a user, role, or an AWS service in Migration Hub. CloudTrail captures all API calls for
Migration Hub as events. The calls captured include calls from the Migration Hub console and
code calls to the Migration Hub API operations.

If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon S3 bucket,
including events for Migration Hub. If you don't configure a trail, you can still view the most
recent events in the CloudTrail console in **Event history**.

Using the information collected by CloudTrail, you can determine the request that was made to
Migration Hub, the IP address from which the request was made, who made the request, when it was
made, and additional details.

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").

## Migration Hub information in CloudTrail

CloudTrail is enabled on your AWS account when you create the account. When activity occurs in
Migration Hub, that activity is recorded in a CloudTrail event along with other AWS service events
in **Event history**. You can view, search, and download recent events in
your AWS account. For more information, see [Viewing Events with CloudTrail Event
History](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").

For an ongoing record of events in your AWS account, including events for Migration Hub,
create a trail. A _trail_ enables CloudTrail to deliver log files to an Amazon S3
bucket. By default, when you create a trail in the console, the trail applies to all AWS
Regions. The trail logs events from all Regions in the AWS partition and delivers the log
files to the Amazon S3 bucket that you specify. Additionally, you can configure other AWS
services to further analyze and act upon the event data collected in CloudTrail logs. For more
information, see the following:

- [Overview for
  Creating a Trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [CloudTrail Supported Services and Integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations")
- [Configuring Amazon SNS
  Notifications for CloudTrail](../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md "../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md")
- [Receiving CloudTrail Log Files from Multiple Regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md") and [Receiving CloudTrail
  Log Files from Multiple Accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")

All Migration Hub actions are logged by CloudTrail and are documented in the
[AWS Migration Hub API](api-reference.md "api-reference.md"). For example, calls to the `AssociateDiscoveredResource`,
`ListCreatedArtifacts` and `PutResourceAttributes` actions generate
entries in the CloudTrail log files.

Every event or log entry contains information about who generated the request. The
identity information helps you determine the following:

- Whether the request was made with root or AWS Identity and Access Management (IAM) user credentials.
- Whether the request was made with temporary security credentials for a role or
  federated user.
- Whether the request was made by another AWS service.

For more information, see the [CloudTrail userIdentity
Element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md").

## Understanding Migration Hub log file

entries

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket
that you specify. CloudTrail log files contain one or more log entries. An event represents a single
request from any source and includes information about the requested action, the date and time
of the action, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of
the public API calls, so they don't appear in any specific order.

The following example shows a CloudTrail log entry that demonstrates the
`DescribeApplicationState` action.

```
{
    "eventVersion": "1.05",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AROAIGZQV3RRQMO4RQZCI:sally-90b99f9f-2ffd-4187-9ef1-26b9f22d6419",
        "arn": "arn:aws:sts::123456789012:assumed-role/Sally/sally-90b99f9f-2ffd-4187-9ef1-26b9f22d6419",
        "accountId": "123456789012",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "attributes": {
                "mfaAuthenticated": "false",
                "creationDate": "2017-05-23T23:54:04Z"
            },
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AROAIGZQV3RRQMO4RQZCI",
                "arn": "arn:aws:iam::123456789012:role/Sally",
                "accountId": "123456789012",
                "userName": "Sally"
            }
        }
    },
    "eventTime": "2017-05-24T00:03:06Z",
    "eventSource": "migrationhub.amazonaws.com",
    "eventName": "DescribeApplicationState",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "34.223.252.133",
    "userAgent": "aws-internal/3, sally-generated exec-env/AWS_Lambda_java8",
    "requestParameters": {"applicationId": "d-application-05d4e9901fa320fa0"},
    "responseElements": null,
    "requestID": "5d4eacdc-4014-11e7-925d-65290d4fc127",
    "eventID": "b12097ee-d121-43f4-a3f8-ca4aa57e6c94",
    "eventType": "AwsApiCall",
    "recipientAccountId": "123456789012"
}

```
