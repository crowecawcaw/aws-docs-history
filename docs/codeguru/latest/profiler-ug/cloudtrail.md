# Logging Amazon CodeGuru Profiler API calls with AWS CloudTrail

Amazon CodeGuru Profiler is integrated with AWS CloudTrail, a service that provides a record of actions taken by
a user, role, or an AWS service in CodeGuru Profiler. CloudTrail captures most API calls for CodeGuru Profiler as events,
including calls from the CodeGuru Profiler console and from code calls to the CodeGuru Profiler APIs. If you create a
trail, you can enable continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for
CodeGuru Profiler. If you don't configure a trail, you can still view the most recent events in the CloudTrail
console in **Event history**. Using the information collected by CloudTrail, you can
determine the request that was made to CodeGuru Profiler, the IP address from which the request was made,
who made the request, when it was made, and additional details.

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").

## Amazon CodeGuru Profiler information in CloudTrail

CloudTrail is enabled on your AWS account when you create the account. When activity occurs in
CodeGuru Profiler, that activity is recorded in a CloudTrail event with other AWS service events in
**Event history**. You can view, search, and download recent events in your
AWS account. For more information, see [Viewing events with CloudTrail event history](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md") in the _AWS CloudTrail User Guide_.

For an ongoing record of events in your AWS account, including events for CodeGuru Profiler, create
a trail. A trail enables CloudTrail to deliver log files to an Amazon S3 bucket. By default, when you
create a trail in the console, the trail applies to all AWS Regions. The trail logs events
from all Regions in the AWS partition and delivers the log files to the S3 bucket that you
specify. You can configure other AWS services to further analyze and act on the event data
collected in CloudTrail logs. For more information, see the following:

- [Overview for Creating a Trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [CloudTrail supported services and integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations")
- [Configuring Amazon SNS
  notifications for CloudTrail](../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md "../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md")
- [Receiving CloudTrail log files from multiple Regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md") and [Receiving CloudTrail
  log files from multiple accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")

All CodeGuru Profiler actions are logged by CloudTrail. CodeGuru Profiler actions are documented in the [Amazon CodeGuru Profiler API Reference](../../../codebuild/latest/APIReference.md "../../../codebuild/latest/APIReference.md"). For example, calls to the
`CreateProfilingGroup` (in the AWS CLI, `create-profiling-group`) and
`UpdateProfilingGroup` (in the AWS CLI, `update-profiling-group`)
actions generate entries in the CloudTrail log files. CodeGuru Profiler agent APIs (`ConfigureAgent`
and `PostAgentProfile`) are data plane operations and are not logged by default. To
log data events, see [Logging data
events](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md") in the _AWS CloudTrail User Guide_.

Every event or log entry contains information about who generated the request. The
identity information helps you determine the following:

- Whether the request was made with root or IAM user credentials
- Whether the request was made with temporary security credentials for a role or
  federated user
- Whether the request was made by another AWS service

For more information, see the [CloudTrail userIdentity
element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md") in the _AWS CloudTrail User Guide_.

## Understanding Amazon CodeGuru Profiler log file

entries

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket
that you specify. CloudTrail log files contain one or more log entries. An event represents a single
request from any source and includes information about the requested action, the date and time
of the action, request parameters, and so on. CloudTrail log files are not an ordered stack trace of
the public API calls, so they don't appear in any specific order.

### Example: A log entry for calling the DescribeProfilingGroup API

A log entry created by [`DescribeProfilingGroup`](../profiler-api/API_DescribeProfilingGroup.md "../profiler-api/API_DescribeProfilingGroup.md")
includes the name of the proﬁle group in the `requestParameters` ﬁeld.

```
{
  "eventVersion": "1.05",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AIDACKCEVSQ6C2EXAMPLE:i-1234567890abcdef0",
    "arn": "arn:aws:sts::`123456789012`:assumed-role/`user-name`",
    "accountId": "`123456789012`",
    "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AIDACKCEVSQ6C2EXAMPLE",
        "arn": "arn:aws:iam::`123456789012`:role/`user-name`",
        "accountId": "`123456789012`",
        "userName": "user-name"
      },
      "webIdFederationData": {},
      "attributes": {
        "mfaAuthenticated": "false",
        "creationDate": "2020-05-06T16:56:59Z"
      },
      "ec2RoleDelivery": "1.0"
    }
  },
  "eventTime": "2020-05-06T18:51:49Z",
  "eventSource": "codeguru-profiler.amazonaws.com",
  "eventName": "DescribeProfilingGroup",
  "awsRegion": "us-west-2",
  "sourceIPAddress": "203.0.113.12",
  "userAgent": "aws-sdk-java/2.9.17 Linux/4.14.154-128.181.amzn2.x86_64 OpenJDK_64- Bit_Server_VM/25.252-b09 Java/1.8.0_252 vendor/Amazon.com_Inc. io/sync http/Apache",
  "requestParameters": {
    "profilingGroupName": "`ExampleProfilingGroup`"
  },
  "responseElements": null,
  "requestID": "cb8c167e-EXAMPLE",
  "eventID": "e3c6f4ce-EXAMPLE",
  "readOnly": false,
  "eventType": "AwsApiCall",
  "recipientAccountId": "`123456789012`"
}
```

### Example: A log entry for getting a proﬁle

A log entry created by [`GetProfile`](../profiler-api/API_GetProfile.md "../profiler-api/API_GetProfile.md")
includes the name of the proﬁle group and the period in the `requestParameters` ﬁeld.

```
{
  "eventVersion": "1.05",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AIDACKCEVSQ6C2EXAMPLE:i-1234567890abcdef0",
    "arn": "arn:aws:sts::`123456789012`:assumed-role/`user-name`",
    "accountId": "`123456789012`",
    "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AIDACKCEVSQ6C2EXAMPLE",
        "arn": "arn:aws:iam::`123456789012`:role/`user-name`",
        "accountId": "`123456789012`",
        "userName": "`user-name`"
      },
      "webIdFederationData": {},
      "attributes": {
        "mfaAuthenticated": "false",
        "creationDate": "2020-05-06T16:56:59Z"
      },
      "ec2RoleDelivery": "1.0"
    }
  },
  "eventTime": "2020-05-06T18:51:49Z",
  "eventSource": "codeguru-profiler.amazonaws.com",
  "eventName": "GetProfile",
  "awsRegion": "us-west-2",
  "sourceIPAddress": "203.0.113.12",
  "userAgent": "aws-sdk-java/2.9.17 Linux/4.14.154-128.181.amzn2.x86_64 OpenJDK_64- Bit_Server_VM/25.252-b09 Java/1.8.0_252 vendor/Amazon.com_Inc. io/sync http/Apache",
  "requestParameters": {
    "period": "PT5M",
    "profilingGroupName": "`ExampleProfilingGroup`"
  },
  "responseElements": null,
  "requestID": "cb8c167e-EXAMPLE",
  "eventID": "e3c6f4ce-EXAMPLE",
  "readOnly": false,
  "eventType": "AwsApiCall",
  "recipientAccountId": "`123456789012`"
}
```
