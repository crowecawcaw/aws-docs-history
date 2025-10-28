AWS Data Pipeline is no longer available to new customers. Existing customers of AWS Data Pipeline can continue to use the service as normal. [Learn more](https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/ "https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/")

# Logging and Monitoring in AWS Data Pipeline

AWS Data Pipeline is integrated with AWS CloudTrail, a service that provides a record of actions taken by a
user, role, or an AWS service in AWS Data Pipeline. CloudTrail captures all API calls for AWS Data Pipeline as events.
The calls captured include calls from the AWS Data Pipeline console and code calls to the AWS Data Pipeline API
operations. If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon S3
bucket, including events for AWS Data Pipeline. If you don't configure a trail, you can still view the
most recent events in the CloudTrail console in **Event history**. Using the
information collected by CloudTrail, you can determine the request that was made to AWS Data Pipeline, the IP
address from which the request was made, who made the request, when it was made, and additional
details.

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").

## AWS Data Pipeline Information in CloudTrail

CloudTrail is enabled on your AWS account when you create the account. When activity occurs in
AWS Data Pipeline, that activity is recorded in a CloudTrail event along with other AWS service events in
**Event history**. You can view, search, and download recent events in your
AWS account. For more information, see [Viewing Events with CloudTrail Event History](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").

For an ongoing record of events in your AWS account, including events for AWS Data Pipeline,
create a trail. A _trail_ enables CloudTrail to deliver log files to an Amazon S3
bucket. By default, when you create a trail in the console, the trail applies to all AWS
Regions. The trail logs events from all Regions in the AWS partition and delivers the log
files to the Amazon S3 bucket that you specify. Additionally, you can configure other AWS
services to further analyze and act upon the event data collected in CloudTrail logs. For more
information, see the following:

- [Overview for Creating a Trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [CloudTrail Supported Services and Integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations")
- [Configuring Amazon SNS Notifications
  for CloudTrail](../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md "../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md")
- [Receiving CloudTrail Log
  Files from Multiple Regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md") and [Receiving CloudTrail Log
  Files from Multiple Accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")

All of the AWS Data Pipeline actions are logged by CloudTrail and are documented in the [AWS Data Pipeline API Reference Actions
chapter](../APIReference/API_Operations.md "../APIReference/API_Operations.md"). For example, calls to the **CreatePipeline** action
generate entries in the CloudTrail log files.

Every event or log entry contains information about who generated the request. The
identity information helps you determine the following:

- Whether the request was made with root or IAM role credentials.
- Whether the request was made with temporary security credentials for a role or
  federated user.
- Whether the request was made by another AWS service.

For more information, see the [CloudTrail userIdentity
Element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md").

## Understanding AWS Data Pipeline Log File

Entries

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket
that you specify. CloudTrail log files contain one or more log entries. An event represents a single
request from any source and includes information about the requested action, the date and time
of the action, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of
the public API calls, so they don't appear in any specific order.

The following example shows a CloudTrail log entry that demonstrates the
`CreatePipeline` operation:

```

      {
  "Records": [
    {
      "eventVersion": "1.02",
      "userIdentity": {
        "type": "Root",
        "principalId": "123456789012",
        "arn": "arn:aws:iam::aws-account-id:role/role-name",
        "accountId": "role-account-id",
        "accessKeyId": "role-access-key"
      },
      "eventTime": "2014-11-13T19:15:15Z",
      "eventSource": "datapipeline.amazonaws.com",
      "eventName": "CreatePipeline",
      "awsRegion": "us-east-1",
      "sourceIPAddress": "72.21.196.64",
      "userAgent": "aws-cli/1.5.2 Python/2.7.5 Darwin/13.4.0",
      "requestParameters": {
        "name": "testpipeline",
        "uniqueId": "sounique"
      },
      "responseElements": {
        "pipelineId": "df-06372391ZG65EXAMPLE"
      },
      "requestID": "65cbf1e8-6b69-11e4-8816-cfcbadd04c45",
      "eventID": "9f99dce0-0864-49a0-bffa-f72287197758",
      "eventType": "AwsApiCall",
      "recipientAccountId": "role-account-id"
    },
      ...additional entries
  ]
}
```
