# Logging your quantum tasks with CloudTrail

Amazon Braket is integrated with AWS CloudTrail, a service that provides a record of actions
taken by a user, role, or an AWS service in Amazon Braket. CloudTrail captures all API
calls for Amazon Braket as events. The calls captured include calls from the Amazon Braket console
and code calls to the Amazon Braket operations. If you create a trail, you can enable continuous
delivery of CloudTrail events to an Amazon S3 bucket, including events for Amazon Braket. If you do not configure
a trail, you can still view the most recent events in the CloudTrail console in
**Event history**. Using the information collected by CloudTrail, you can
determine the request that was made to Amazon Braket, the IP address from which the request was made,
who made the request, when it was made, and additional details.

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").

###### In this section:

- [Amazon Braket information in CloudTrail](#braket-ct-logs-info "#braket-ct-logs-info")
- [Understanding Amazon Braket log file entries](#understanding-braket-entries "#understanding-braket-entries")

## Amazon Braket information in CloudTrail

CloudTrail is enabled on your AWS account when you create the account. When activity occurs in
Amazon Braket, that activity is recorded in a CloudTrail event along with other AWS service events in
**Event history**. You can view, search, and download recent events
in your AWS account. For more information, see
[Viewing Events with CloudTrail Event History](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").

For an ongoing record of events in your AWS account, including events for Amazon Braket,
create a trail. A _trail_ enables CloudTrail to deliver log files to an Amazon S3 bucket.
By default, when you create a trail in the console, the trail applies to all AWS Regions. The
trail logs events from all Regions in the AWS partition and delivers the log files to the Amazon S3
bucket that you specify. Additionally, you can configure other AWS services to further analyze
and act upon the event data collected in CloudTrail logs. For more information, see the following:

- [Overview for Creating a Trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [CloudTrail Supported Services and Integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations")
- [Configuring Amazon SNS Notifications for CloudTrail](../../../awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.md "../../../awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.md")
- [Receiving CloudTrail Log Files from Multiple Regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md") and [Receiving CloudTrail Log Files from Multiple Accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")

All Amazon
Braket actions are logged by CloudTrail. For example, calls to the `GetQuantumTask` or `GetDevice` actions generate entries in the CloudTrail log files.

Every event or log entry contains information about who generated the request. The identity information helps you determine the following:

- Whether the request was made with temporary security credentials for a role or federated user.
- Whether the request was made by another AWS service.

For more information, see the [CloudTrail userIdentity Element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md").

## Understanding Amazon Braket log file entries

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket that
you specify. CloudTrail log files contain one or more log entries. An event represents a single request
from any source and includes information about the requested action, the date and time of the action,
request parameters, and so on. CloudTrail log files are not an ordered stack trace of the public
API calls, so they don't appear in any specific order.

The following example is a log entry for the `GetQuantumTask` action, which gets the
details of a quantum task.

```
{
  "eventVersion": "1.05",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "foobar",
    "arn": "foobar",
    "accountId": "foobar",
    "accessKeyId": "foobar",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "foobar",
        "arn": "foobar",
        "accountId": "foobar",
        "userName": "foobar"
      },
      "webIdFederationData": {},
      "attributes": {
        "mfaAuthenticated": "false",
        "creationDate": "2020-08-07T00:56:57Z"
      }
    }
  },
  "eventTime": "2020-08-07T01:00:08Z",
  "eventSource": "braket.amazonaws.com",
  "eventName": "GetQuantumTask",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "foobar",
  "userAgent": "aws-cli/1.18.110 Python/3.6.10 Linux/4.9.184-0.1.ac.235.83.329.metal1.x86_64 botocore/1.17.33",
  "requestParameters": {
    "quantumTaskArn": "foobar"
  },
  "responseElements": null,
  "requestID": "20e8000c-29b8-4137-9cbc-af77d1dd12f7",
  "eventID": "4a2fdb22-a73d-414a-b30f-c0797c088f7c",
  "readOnly": true,
  "eventType": "AwsApiCall",
  "recipientAccountId": "foobar"
}
```

The following shows a log entry for the `GetDevice` action, which returns the details of a device event.

```
{
  "eventVersion": "1.05",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "foobar",
    "arn": "foobar",
    "accountId": "foobar",
    "accessKeyId": "foobar",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "foobar",
        "arn": "foobar",
        "accountId": "foobar",
        "userName": "foobar"
      },
      "webIdFederationData": {},
      "attributes": {
        "mfaAuthenticated": "false",
        "creationDate": "2020-08-07T00:46:29Z"
      }
    }
  },
  "eventTime": "2020-08-07T00:46:32Z",
  "eventSource": "braket.amazonaws.com",
  "eventName": "GetDevice",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "foobar",
  "userAgent": "Boto3/1.14.33 Python/3.7.6 Linux/4.14.158-129.185.amzn2.x86_64 exec-env/AWS_ECS_FARGATE Botocore/1.17.33",
  "errorCode": "404",
  "requestParameters": {
    "deviceArn": "foobar"
  },
  "responseElements": null,
  "requestID": "c614858b-4dcf-43bd-83c9-bcf9f17f522e",
  "eventID": "9642512a-478b-4e7b-9f34-75ba5a3408eb",
  "readOnly": true,
  "eventType": "AwsApiCall",
  "recipientAccountId": "foobar"
}
```
