# Logging Reachability Analyzer API calls using AWS CloudTrail

Reachability Analyzer is integrated with AWS CloudTrail, a service that provides a record of actions taken by a
user, a role, or an AWS service in Reachability Analyzer. CloudTrail captures all API calls for Reachability Analyzer as events. The
calls captured include calls from the Reachability Analyzer console and code calls to the Reachability Analyzer API operations. If
you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon S3 bucket,
including events for Reachability Analyzer. If you don't configure a trail, you can still view the most recent
events in the CloudTrail console in **Event history**. Using the information
collected by CloudTrail, you can determine the request that was made to Reachability Analyzer, the IP address from
which the request was made, who made the request, when it was made, and additional
details.

To learn more about CloudTrail, see the _[AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md")_.

## Reachability Analyzer information in CloudTrail

CloudTrail is enabled on your AWS account when you create the account. When activity occurs in
Reachability Analyzer, that activity is recorded in a CloudTrail event along with other AWS service events in
**Event history**. You can view, search, and download recent events in your
AWS account. For more information, see [Viewing events with CloudTrail Event history](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").

For an ongoing record of events in your AWS account, including events for Reachability Analyzer, create a
trail. A _trail_ enables CloudTrail to deliver log files to an Amazon S3 bucket. By
default, when you create a trail in the console, the trail applies to all AWS Regions. The
trail logs events from all Regions in the AWS partition and delivers the log files to the
Amazon S3 bucket that you specify. Additionally, you can configure other AWS services to further
analyze and act upon the event data collected in CloudTrail logs. For more information, see the
following:

- [Overview for creating a trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [CloudTrail supported services and integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md")
- [Configuring Amazon SNS notifications for CloudTrail](../../../awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.md "../../../awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.md")
- [Receiving CloudTrail log files from multiple regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md") and [Receiving CloudTrail log files from multiple accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")

### Supported API calls

For Reachability Analyzer, you can use CloudTrail to log two types of events:

- Reachability Analyzer API calls — All API calls used to create,
  read/describe, update, delete, and list (CRUDL) Reachability Analyzer resources are logged by CloudTrail and
  are documented in the [Amazon EC2 API Reference](../../../AWSEC2/latest/APIReference.md "../../../AWSEC2/latest/APIReference.md"). In this scenario, `ec2.amazonaws.com`
  is the event source.
- AWS Network Manager Chat API calls — CloudTrail also records all
  Network Manager Chat API calls as events. The Network Manager Chat API provides an interface and methods with which
  users can interact and have conversations with Reachability Analyzer through Amazon Q. Calls to the
  following API methods generate entries in the CloudTrail log files:

      + `CreateConversation`
      + `ListConversations`
      + `DeleteConversation`
      + `NotifyConversationIsActive`
      + `SendConversationMessage`
      + `ListConversationMessages`
      + `CancelMessageResponse`

  In this scenario, `networkmanager-chat.amazonaws.com` is the event
  source.

### Identity information

Every event or log entry contains information about who generated the request. The
identity information helps you determine the following:

- Whether the request was made with root or AWS Identity and Access Management (IAM) user credentials.
- Whether the request was made with temporary security credentials for a role or
  federated user.
- Whether the request was made by another AWS service.

For more information, see the [CloudTrail userIdentity element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md").

## Understanding Reachability Analyzer log file

entries

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket
that you specify. CloudTrail log files contain one or more log entries. An event represents a single
request from any source and includes information about the requested action, the date and time
of the action, the request parameters, and so on. CloudTrail log files aren't an ordered stack trace
of the public API calls, so they don't appear in any specific order.

The following example shows a CloudTrail log entry that demonstrates the
`DeleteNetworkInsightsPath` action.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AROAZR5EMTJKE753U4ZDS:test-user",
        "arn": "arn:aws:sts::123456789012:assumed-role/Admin/test-user",
        "accountId": "123456789012",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AROAZR5EMTJKE753U4ZDS",
                "arn": "arn:aws:iam::123456789012:role/Admin",
                "accountId": "123456789012",
                "userName": "Admin"
            },
            "webIdFederationData": {},
            "attributes": {
                "creationDate": "2023-10-23T19:01:21Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2023-10-23T19:04:18Z",
    "eventSource": "ec2.amazonaws.com",
    "eventName": "DeleteNetworkInsightsPath",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "1.1.1.1",
    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0",
    "requestParameters": {
        "DeleteNetworkInsightsPathRequest": {
            "NetworkInsightsPathId": "nip-068b3d73d1EXAMPLE"
        }
    },
    "responseElements": {
        "DeleteNetworkInsightsPathResponse": {
            "xmlns": "http://ec2.amazonaws.com/doc/2016-11-15/",
            "requestId": "ca28860f-504a-4f2d-9f3f-f9cfb4ba0491",
            "networkInsightsPathId": "nip-068b3d73d1EXAMPLE"
        }
    },
    "requestID": "122b3164-b75c-4158-892b-ddfdfecff2d3",
    "eventID": "216247c4-8644-4f63-8b26-171d9d412a22",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "123456789012",
    "eventCategory": "Management",
    "tlsDetails": {
        "tlsVersion": "TLSv1.2",
        "cipherSuite": "ECDHE-RSA-AES128-GCM-SHA256",
        "clientProvidedHostHeader": "ec2.us-west-2.amazonaws.com"
    },
    "sessionCredentialFromConsole": "true"
}
```

The following example shows a CloudTrail log entry that demonstrates the
`SendConversationMessage` action.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AROAZR5EMTJKE753U4ZDS:test-user",
        "arn": "arn:aws:sts::123456789012:assumed-role/Admin/test-user",
        "accountId": "123456789012",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AROAZR5EMTJKE753U4ZDS",
                "arn": "arn:aws:iam::123456789012:role/Admin",
                "accountId": "123456789012",
                "userName": "Admin"
            },
            "webIdFederationData": {},
            "attributes": {
                "creationDate": "2023-10-19T19:55:45Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2023-10-19T19:57:29Z",
    "eventSource": "networkmanager-chat.amazonaws.com",
    "eventName": "SendConversationMessage",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "1.1.1.1",
    "userAgent": "python-requests/2.31.0",
    "requestParameters": {
        "conversationId": "52c59d5f-932b-94c9-90bb-385454d3c3f9",
        "clientToken": "1234abcabefaaa",
        "message": "***"
    },
    "responseElements": {
        "conversationMessage": {
            "MessageContent": "***",
            "MessageContentType": "TEXT",
            "MessageId": "c6c5a4c1-d817-a153-4ac8-b9d96b22748d",
            "MessageState": "AVAILABLE",
            "MessageType": "USER",
            "Timestamp": 1697745449007
        }
    },
    "requestID": "d78c47a4-1b51-4823-bd4d-9c88d00a5dc6",
    "eventID": "4cae0020-429f-4958-b823-11d4afeeec4c",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "123456789012",
    "eventCategory": "Management"
}
```
