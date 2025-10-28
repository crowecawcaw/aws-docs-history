# Logging AWS User Notifications API calls using AWS CloudTrail

AWS User Notifications integrates with AWS CloudTrail, a service that records actions taken by users, roles, or
AWS services in User Notifications. CloudTrail captures all API calls for User Notifications as events. The calls captured
include calls from the User Notifications console and code calls to User Notifications API operations. If you create a
trail, you can receive continuous delivery of CloudTrail events to an Amazon S3 bucket, including events
for User Notifications. If you don't configure a trail, you can still view the most recent events in the CloudTrail
console in **Event history**. With the information collected by CloudTrail, you can
identify the following details:

- The request made to User Notifications.
- The IP address that sent the request.
- The identity that sent the request.
- The time and date when the request was made.
- Additional, request-specific details.
  For more information, see [Viewing
  Events with CloudTrail Event History](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").

To learn more about CloudTrail, including how to turn on and configure it, see the
[AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").

For an ongoing record of events in your AWS account, including events for User Notifications, create a
trail. A _trail_ enables CloudTrail to deliver log files to an Amazon S3 bucket. By
default, when you create a trail in the console, the trail applies to all AWS Regions. The
trail logs events from all Regions in the AWS partition and delivers the log files to the Amazon S3
bucket that you specify. Additionally, you can configure other AWS services to analyze further
and act upon the event data collected in CloudTrail logs. For more information, see the
following:

- [Overview for
  creating a trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [CloudTrail supported services and integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations")
- [Configuring Amazon SNS
  notifications for CloudTrail](../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md "../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md")
- [Receiving CloudTrail log files from multiple Regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md")
- [Receiving
  CloudTrail log files from multiple accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")

## User Notifications information in CloudTrail

CloudTrail logs all actions from User Notifications. For example, calls to the
`AssociateChannel`, `ListChannels` and
`CreateNotificationConfiguration` actions generate entries in your CloudTrail log
files.

Every event or log entry contains information about who generated the request. The
identity information helps you determine the following:

- Whether the request was made with root or AWS Identity and Access Management (IAM) user credentials.
- Whether the request was made with temporary security credentials for a role or
  federated user.
- Whether the request was made by another AWS service.

For more information, see the [CloudTrail userIdentity
element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md").

###### Note

Sensitive fields are automatically redacted by CloudTrail. Contact names and activation codes
are always considered sensitive. Email addresses are considered sensitive except upon
creation.

## Understanding User Notifications log file

entries

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket
that you specify. CloudTrail log files contain one or more log entries. An event represents a single
request from any source. It includes information about the requested action, including the
date and time of the action and request parameters. CloudTrail log files aren't an ordered stack
trace of the public API calls, so they don't appear in any specific order.

The following example shows a CloudTrail log entry that demonstrates the
`AssociateChannel` action.

```
{
  "eventVersion" : "1.08",
  "userIdentity" : {
    "type" : "AssumedRole",
    "principalId" : "AIDACKCEVSQ6C2EXAMPLE:jdoe",
    "arn" : "arn:aws:sts::111122223333:assumed-role/user/jdoe",
    "accountId" : "111122223333",
    "accessKeyId" : "AKIAIOSFODNN7EXAMPLE",
    "sessionContext" : {
      "sessionIssuer" : {
        "type" : "Role",
        "principalId" : "AIDACKCEVSQ6C2EXAMPLE",
        "arn" : "arn:aws:iam::111122223333:role/user",
        "accountId" : "111122223333",
        "userName" : "jdoe"
      },
      "webIdFederationData" : { },
      "attributes" : {
        "creationDate" : "2022-12-09T23:48:51Z",
        "mfaAuthenticated" : "false"
      }
    }
  },
  "eventTime" : "2022-12-09T23:50:03Z",
  "eventSource" : "notifications.amazonaws.com",
  "eventName" : "AssociateChannel",
  "awsRegion" : "us-east-1",
  "sourceIPAddress" : "10.24.34.3",
  "userAgent" : "aws-sdk-java/2.18.22 Linux/4.14.255-285-225.501.amzn2.x86_64 OpenJDK_64-Bit_Server_VM/11.0.14.1+10-LTS Java/11.0.14.1 kotlin/1.4.20-release-308 (1.4.20) vendor/Amazon.com_Inc. exec-env/AWS_Lambda_java11 io/sync http/UrlConnection cfg/retry-mode/legacy",
  "requestParameters" : {
    "notificationConfigurationArn" : "arn:aws:notifications::111122223333:configuration/a01gkwmqgt1341mdc6ptedbxpad",
    "arn" : "arn%3Aaws%3Anotifications-contacts%3A%3A111122223333%3Aconfiguration%2Ff4u7r2ic"
  },
  "responseElements" : null,
  "requestID" : "543db7ab-b4b2-11e9-8925-d139e92a1fe8",
  "eventID" : "5b2805a5-3e06-4437-a7a2-b5fdb5cbb4e2",
  "readOnly" : false,
  "eventType" : "AwsApiCall",
  "managementEvent" : true,
  "recipientAccountId" : "111122223333",
  "eventCategory" : "Management"
}
```
