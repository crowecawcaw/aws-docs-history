# Logging Amazon IVS API Calls with AWS CloudTrail

Amazon Interactive Video Service (IVS) is integrated with AWS CloudTrail, a service that
provides a record of actions taken by a user, role, or AWS service in Amazon IVS. CloudTrail
captures all API calls for Amazon IVS as events. The calls captured include API calls from the
Amazon IVS console and from your applications.

If you create a _trail_, you can enable continuous delivery
of CloudTrail events to an Amazon S3 bucket, including Amazon IVS events. If you don't configure
a trail, you can still view the most recent events in the CloudTrail console in **Event history**. Using the information collected by CloudTrail, you can
determine the request that was made to Amazon IVS, the IP address from which the request was
made, who made the request, when it was made, and additional details.

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").

## Amazon IVS Information in CloudTrail

CloudTrail is enabled on your AWS account when you create the account. When activity
occurs in Amazon IVS, that activity is recorded in a CloudTrail event along with other AWS
service events in **Event history**. You can view, search, and
download recent events in your AWS account. For more information, see [Viewing Events with CloudTrail Event
History](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").

For an ongoing record of events in your AWS account, including events for Amazon IVS,
create a trail. A trail enables CloudTrail to deliver log files to an Amazon S3 bucket. By
default, when you create a trail in the CloudTrail console, the trail applies to all AWS
regions. The trail logs events from all Regions in the AWS partitions and delivers the log
files to the Amazon S3 bucket that you specify. Additionally, you can configure other AWS
services to analyze and act on the event data collected in CloudTrail logs. For more
information, see these items in the _CloudTrail User
Guide_:

- [Creating a Trail
  For Your AWS Account](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md") (overview)
- [CloudTrail Supported Services and Integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations")
- [Configuring Amazon SNS
  Notifications for CloudTrail](../../../awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.md "../../../awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.md")
- [Receiving CloudTrail Log Files from Multiple Regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md")
- [Receiving CloudTrail Log Files from Multiple Accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")

All Amazon IVS actions are logged by CloudTrail and documented in the [IVS Low-Latency Streaming API Reference](../LowLatencyAPIReference/Welcome.md "../LowLatencyAPIReference/Welcome.md"),
[IVS Real-Time Streaming API Reference](../RealTimeAPIReference/Welcome.md "../RealTimeAPIReference/Welcome.md"), and
[IVS Chat API Reference](../ChatAPIReference/Welcome.md "../ChatAPIReference/Welcome.md"). For
example, calls to the `CreateChannel`, `ListChannels`, and
`DeleteChannel` operations generate entries in the CloudTrail log files.

Every event or log entry contains information about who generated the request. The
identity information helps you determine whether the request was made:

- With root or AWS Identity and Access Management (IAM) user credentials
- With temporary security credentials for a role or federated user.
- By another AWS service.

For more information, see the [CloudTrail userIdentity
Element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md").

## Understanding Amazon IVS Log File

Entries

A trail is a configuration that enables delivery of events as log files to an Amazon S3
bucket that you specify. An event represents a single request from any source and includes
information about the requested action, the date and time of the action, request parameters,
and so on.

CloudTrail log files contain one or more log entries. CloudTrail log files are not an
ordered stack trace of the public API calls, so they do not appear in any specific
order.

The following example shows a CloudTrail log entry for the `CreateChannel`
operation.

```
{
    "eventVersion": "1.05",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "ABCDEFGHIJK1L2EXAMPLE:account_name",
        "arn": "arn:aws:sts::123456789012:assumed-role/First_Streamer/1234567890123456789",
        "accountId": "123456789012",
        "accessKeyId": "ABCDEFGHIJKL1EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "ABCDEFGHIJK1L2EXAMPLE",
                "arn": "arn:aws:iam::123456789012:role/Admin",
                "accountId": "123456789012",
                "userName": "First_Streamer"
            },
            "webIdFederationData": {},
            "attributes": {
                "mfaAuthenticated": "false",
                "creationDate": "2020-04-02T20:57:43Z"
            }
        }
    },
    "eventTime": "2020-04-02T20:57:46Z",
    "eventSource": "ivs.amazonaws.com",
    "eventName": "CreateChannel",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "10.10.10.10",
    "userAgent": "console.amazonaws.com",
    "requestParameters": {
        "name": "default"
    },
    "responseElements": {
        "channel": {
            "arn": "arn:aws:ivs:us-west-2:123456789012:channel/1EXAMPLE",
            "authorized": false,
            "ingestEndpoint": "EXAMPLE.global-contribute.live-video.net",
            "latencyMode": "LOW",
            "name": "default",
            "playbackUrl": "https://EXAMPLE.m3u8",
            "tags": {}
        },
        "streamKey": {
            "arn": "arn:aws:ivs:us-west-2:123456789012:stream-key/2EXAMPLE",
            "channelArn": "arn:aws:ivs:us-west-2:123456789012:channel/1EXAMPLE",
            "tags": {}
        }
    },
    "requestID": "12a34bc5-EXAMPLE",
    "eventID": "a1b2c3de-EXAMPLE",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "recipientAccountId": "123456789012"
}
```
