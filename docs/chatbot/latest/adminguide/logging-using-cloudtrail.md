AWS Chatbot is now Amazon Q Developer. [Learn more](service-rename.md "service-rename.md")

# Logging Amazon Q Developer in chat applications API calls with AWS CloudTrail

###### Note

AWS Chatbot has integrated with Amazon Q Developer. [Learn more](service-rename.md "service-rename.md")

Amazon Q Developer in chat applications integrates events with AWS CloudTrail, a service that provides a record of actions
taken by a user, role, or an AWS service in Amazon Q Developer in chat applications. CloudTrail captures API calls for Amazon Q Developer in chat applications as
events. The calls captured include calls from the Amazon Q Developer in chat applications console and code calls to the Amazon Q Developer in chat applications API
operations. If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon S3
bucket, including events for Amazon Q Developer in chat applications. If you don't configure a trail, you can still view the most
recent events in the CloudTrail console in **Event history**. Using the information
collected by CloudTrail, you can determine the request that was made to Amazon Q Developer in chat applications, the IP address from
which the request was made, who made the request, when it was made, and additional details. For
more information, see [Viewing Events with
CloudTrail Event History](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").

To learn more about CloudTrail, including how to configure and enable it, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").

When you create a _trail_, you can enable continuous delivery of Amazon Q Developer in chat applications
events to an Amazon S3 bucket that you specify. The trail logs events from all Regions in the
AWS partition for that service and delivers the log files to that Amazon S3 bucket. You can
configure other AWS services to further analyze and act upon the event data collected in CloudTrail
logs. For more information, see the following topics in the _AWS CloudTrail User Guide_:

- [Overview for
  Creating a Trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [CloudTrail Supported Services and Integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations")
- [Configuring Amazon SNS
  Notifications for CloudTrail](../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md "../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md")
- [Receiving CloudTrail Log Files from Multiple Regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md") and [Receiving CloudTrail Log
  Files from Multiple Accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")

## Logging Amazon Q Developer in chat applications API information in CloudTrail

Every event log entry contains information about who generated the request. The identity
information helps you determine the following:

- Whether the request was made with root user or IAM user credentials.
- Whether the request was made with temporary security credentials for a role or for a
  federated user.
- Whether the request was made by another AWS service.

For more information, see the [CloudTrail userIdentity
Element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md").

## Logging other AWS API information in CloudTrail

When you use commands in Amazon Q Developer in chat applications that call APIs from other AWS services, those APIs are
logged in CloudTrail as well.

When you run a command that involves another AWS service, Amazon Q Developer in chat applications assumes an IAM role in
your account to invoke AWS APIs on your behalf. These APIs appear in your CloudTrail events, and
they are associated with the role that was configured for your Amazon Q Developer in chat applications configuration with a
session name that includes **chatbot**, such as
**chatbot-session**.

Because Amazon Q Developer in chat applications is a global service, it may process your events in a different AWS Region.
An API call is logged in the region where the resource behind that API call exists. For
example, if you run a `lambda list-functions` command in Amazon Q Developer in chat applications, CloudTrail will log two
APIs: **AssumeRole** and **ListFunctions**. The
**AssumeRole** call is logged in the Region Amazon Q Developer in chat applications processed it in, and the
**ListFunctions** call is logged in the Region the function exists in.

## Example: Amazon Q Developer in chat applications log file entries

CloudTrail log files contain one or more log entries. An event represents a single
request from any source and includes information about the requested action, the date and time
of the action, request parameters, user identification, and more. CloudTrail log files aren't an ordered stack trace of
the public API calls, so they don't appear in any specific order.

The following example shows a CloudTrail log entry for the Amazon Q Developer in chat applications
`DescribeSlackChannels` action.

```

{
    "eventVersion": "1.05",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AIDACKCEVSQ6C2EXAMPLE:jdoe",
        "arn": "arn:aws:sts::111122223333:assumed-role/user/jdoe",
        "accountId": "111122223333",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "attributes": {
                "mfaAuthenticated": "false",
                "creationDate": "2019-08-01T17:24:13Z"
            },
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AIDACKCEVSQ6C2EXAMPLE",
                "arn": "arn:aws:iam::111122223333:role/user",
                "accountId": "111122223333",
                "userName": "jdoe"
            }
        }
    },
    "eventTime": "2019-08-01T23:16:02Z",
    "eventSource": "chatbot.amazonaws.com",
    "eventName": "DescribeSlackChannels",
    "awsRegion": "us-east-2",
    "sourceIPAddress": "10.24.34.3",
    "userAgent": "aws-internal/3 aws-sdk-java/1.11.590 Linux/4.9.137-0.1.ac.218.74.329.metal1.x86_64 OpenJDK_64-Bit_Server_VM/25.212-b03 java/1.8.0_212 vendor/Oracle_Corporation",
    "requestParameters": {
        "SlackTeamId": "XXXXXXXX",
        "MaxResults": 1000
    },
    "responseElements": null,
    "requestID": "543db7ab-b4b2-11e9-8925-d139e92a1fe8",
    "eventID": "5b2805a5-3e06-4437-a7a2-b5fdb5cbb4e2",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "recipientAccountId": "111122223333"
}

```

The following example shows a CloudTrail log entry for a `DescribeSlackWorkspaces`
action.

```

{
    "eventVersion": "1.05",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AIDACKCEVSQ6C2EXAMPLE:jdoe",
        "arn": "arn:aws:sts::111122223333:assumed-role/user/jdoe",
        "accountId": "111122223333",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "attributes": {
                "mfaAuthenticated": "false",
                "creationDate": "2019-08-07T16:11:27Z"
            },
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AIDACKCEVSQ6C2EXAMPLE",
                "arn": "arn:aws:iam::111122223333:role/user",
                "accountId": "111122223333",
                "userName": "jdoe"
            }
        }
    },
    "eventTime": "2019-08-07T17:46:26Z",
    "eventSource": "chatbot.amazonaws.com",
    "eventName": "DescribeSlackWorkspaces",
    "awsRegion": "us-east-2",
    "sourceIPAddress": "10.24.34.3",
    "userAgent": "aws-internal/3 aws-sdk-java/1.11.590 Linux/4.9.137-0.1.ac.218.74.329.metal1.x86_64 OpenJDK_64-Bit_Server_VM/25.212-b03 java/1.8.0_212 vendor/Oracle_Corporation",
    "requestParameters": null,
    "responseElements": null,
    "requestID": "476570da-b93b-11e9-af41-a744734236af",
    "eventID": "3f061095-b488-43d4-becc-f8652d459ac5",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "recipientAccountId": "111122223333"
}

```
