# Logging

Security Hub
API calls with CloudTrail

AWS Security Hub CSPM is integrated with AWS CloudTrail, a service that provides a record of actions taken
by a user, role, or an AWS service in Security Hub CSPM. CloudTrail captures API calls for Security Hub CSPM as events.
The captured calls include calls from the Security Hub CSPM console and code calls to the Security Hub CSPM API
operations. If you create a trail, you can enable continuous delivery of CloudTrail events to an
Amazon S3 bucket, including events for Security Hub CSPM. If you don't configure a trail, you can still view
the most recent events on the CloudTrail console in **Event history**. Using the
information that CloudTrail collects, you can determine the request that was made to Security Hub CSPM, the IP
address that the request was made from, who made the request, when it was made, and
additional details.

To learn more about CloudTrail, including how to configure and enable it, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md").

## Security Hub CSPM information in CloudTrail

CloudTrail is enabled on your AWS account when you create the account. When supported
event activity occurs in Security Hub CSPM, that activity is recorded in a CloudTrail event along with
other AWS service events in **Event history**. You can view, search,
and download recent events in your account. For more information, see [Viewing events with CloudTrail event history](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").

For an ongoing record of events in your account, including events for Security Hub CSPM, create a
trail. A _trail_ enables CloudTrail to deliver log files to an Amazon S3 bucket.
By default, when you create a trail on the console, the trail applies to all AWS
Regions. The trail logs events from all Regions in the AWS partition and delivers the
log files to the Amazon S3 bucket that you specify. Additionally, you can configure other
AWS services to further analyze and act upon the event data collected in CloudTrail logs.
For more information, see the following:

- [Overview for creating a trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [CloudTrail supported services and integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations")
- [Configuring Amazon SNS notifications for CloudTrail](../../../awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.md "../../../awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.md")
- [Receiving CloudTrail log files from multiple regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md")
  and [Receiving CloudTrail log files from multiple
  accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")

Security Hub CSPM supports logging all of the Security Hub CSPM API actions as events in CloudTrail logs. To view a
list of Security Hub CSPM operations, see the [Security Hub CSPM API Reference](../../1.0/APIReference/Welcome.md "../../1.0/APIReference/Welcome.md").

When activity for the following actions is logged to CloudTrail, the value for
`responseElements` is set to `null`. This ensures that
sensitive information isn't included in CloudTrail logs.

- `BatchImportFindings`
- `GetFindings`
- `GetInsights`
- `GetMembers`
- `UpdateFindings`

Every event or log entry contains information about who generated the request. The
identity information helps you determine the following:

- Whether the request was made with root or AWS Identity and Access Management (IAM) user
  credentials
- Whether the request was made with temporary security credentials for a role or
  federated user
- Whether the request was made by another AWS service

For more information, see the [CloudTrail userIdentity element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md").

## Example: Security Hub CSPM log file

entries

A trail is a configuration that enables delivery of events as log files to an Amazon S3
bucket that you specify. CloudTrail log files contain one or more log entries. An event
represents a single request from any source and includes information about the requested
action, the date and time of the action, request parameters, and so on. CloudTrail log files
aren't an ordered stack trace of the public API calls, so they don't appear in any
specific order.

The following example shows a CloudTrail log entry that demonstrates the
`CreateInsight` action. In this example, an insight called `Test
 Insight` is created. The `ResourceId` attribute is specified as the
**Group by** aggregator, and no optional filters for this insight
are specified. For more information about insights, see [Viewing insights in Security Hub CSPM](securityhub-insights.md "securityhub-insights.md").

```
{
    "eventVersion": "1.05",
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "AIDAJK6U5DS22IAVUI7BW",
        "arn": "arn:aws:iam::012345678901:user/TestUser",
        "accountId": "012345678901",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "userName": "TestUser"
    },
    "eventTime": "2018-11-25T01:02:18Z",
    "eventSource": "securityhub.amazonaws.com",
    "eventName": "CreateInsight",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "205.251.233.179",
    "userAgent": "aws-cli/1.11.76 Python/2.7.10 Darwin/17.7.0 botocore/1.5.39",
    "requestParameters": {
        "Filters": {},
        "ResultField": "ResourceId",
        "Name": "Test Insight"
    },
    "responseElements": {
        "InsightArn": "arn:aws:securityhub:us-west-2:0123456789010:insight/custom/f4c4890b-ac6b-4c26-95f9-e62cc46f3055"
    },
    "requestID": "c0fffccd-f04d-11e8-93fc-ddcd14710066",
    "eventID": "3dabcebf-35b0-443f-a1a2-26e186ce23bf",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "recipientAccountId": "012345678901"
}
```
