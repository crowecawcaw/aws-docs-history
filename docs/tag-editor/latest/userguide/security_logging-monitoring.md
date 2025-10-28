# Logging and monitoring in Tag Editor

All Tag Editor actions are logged in AWS CloudTrail.

## Logging Tag Editor API calls with CloudTrail

Tag Editor is integrated with AWS CloudTrail, a service that provides a record of actions taken
by a user, role, or an AWS service in Tag Editor. CloudTrail captures all API calls for Tag Editor
as events, including calls from the Tag Editor console and from code calls to the
Resource Groups Tagging API. If you create a trail, you can enable continuous delivery of CloudTrail events to
an Amazon S3 bucket, including events for Tag Editor. If you don't configure a trail, you can
still view the most recent events in the CloudTrail console in **Event
history**. Using the information collected by CloudTrail, you can determine the
request that was made to Tag Editor, the IP address from which the request was made, who
made the request, when it was made, and additional details.

For more information about CloudTrail, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").

### Tag Editor information in

CloudTrail

CloudTrail is enabled on your AWS account when you create the account. When activity
occurs in Tag Editor, or in the Tag Editor console, that activity is recorded in a CloudTrail
event along with other AWS service events in **Event history**.
You can view, search, and download recent events in your AWS account. For more
information, see [Viewing events with CloudTrail Event
history](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").

For an ongoing record of events in your AWS account, including events for
Tag Editor, create a trail. A trail enables CloudTrail to deliver log files to an Amazon S3
bucket. By default, when you create a trail in the console, the trail applies to all
AWS Regions. The trail logs events from all Regions in the AWS partition and
delivers the log files to the Amazon S3 bucket that you specify. Additionally, you can
configure other AWS services to further analyze and act upon the event data
collected in CloudTrail logs. For more information, see the following resources:

- [Creating
  a trail for your AWS account](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [CloudTrail
  supported services and integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md")
- [Configuring
  Amazon SNS notifications for CloudTrail](../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md "../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md")
- [Receiving CloudTrail log files from multiple Regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md") and [Receiving CloudTrail log files from multiple accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")

All Tag Editor actions are logged by CloudTrail and are documented in the [Tag Editor API Reference](../../../ARG/latest/APIReference.md "../../../ARG/latest/APIReference.md").
Tag Editor actions in the console are logged by CloudTrail, and are shown as events with
`tagging.amazonaws.com` as the `eventSource`.

Every event or log entry contains information about who generated the request. The
identity information helps you determine the following:

- Whether the request was made with root or IAM user credentials.
- Whether the request was made with temporary security credentials for a
  role or federated user.
- Whether the request was made by another AWS service.

For more information, see the [CloudTrail
`userIdentity` element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md").

### Understanding Tag Editor log file

entries

A trail is a configuration that enables delivery of events as log files to an Amazon S3
bucket that you specify. CloudTrail log files contain one or more log entries. An event
represents a single request from any source and includes information about the
requested action, the date and time of the action, request parameters, and so on.
CloudTrail log files are not an ordered stack trace of the public API calls, so they do
not appear in any specific order.

The following example shows a CloudTrail log entry that demonstrates the action
`TagResources`.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AROAEXAMPLEEXAMPLE:botocore-session-1661372702",
        "arn": "arn:aws:sts::123456789012:assumed-role/cli-role/botocore-session-1661372702",
        "accountId": "123456789012",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AROAEXAMPLEEXAMPLE",
                "arn": "arn:aws:iam::123456789012:role/cli-role",
                "accountId": "123456789012",
                "userName": "cli-role"
            },
            "webIdFederationData": {},
            "attributes": {
                "creationDate": "2022-08-24T20:25:03Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2022-08-24T20:27:14Z",
    "eventSource": "tagging.amazonaws.com",
    "eventName": "TagResources",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "72.21.198.65",
    "userAgent": "aws-cli/2.7.14 Python/3.9.11 Windows/10 exe/AMD64 prompt/off command/resourcegroupstaggingapi.tag-resources",
    "requestParameters": {
        "resourceARNList": [
            "arn:aws:events:us-east-1:123456789012:rule/SecretsManagerMonitorRule"
        ],
        "tags": {
            "owner": "alice"
        }
    },
    "responseElements": {
        "failedResourcesMap": {}
    },
    "requestID": "8f9ea891-4125-460c-802f-26c11EXAMPLE",
    "eventID": "b2c9322a-aad7-424b-8f0b-423daEXAMPLE",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "123456789012",
    "eventCategory": "Management",
    "tlsDetails": {
        "tlsVersion": "TLSv1.2",
        "cipherSuite": "ECDHE-RSA-AES128-GCM-SHA256",
        "clientProvidedHostHeader": "tagging.us-east-1.amazonaws.com"
    }
}
```
