# AWS Batch information in

CloudTrail

CloudTrail is enabled on your AWS account when you create the account. When activity occurs in AWS Batch,
that activity is recorded in a CloudTrail event along with other AWS service events in **Event
history**. You can view, search, and download recent events in your AWS account. For more information, see
[Viewing Events with CloudTrail Event History](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").

For an ongoing record of events in your AWS account, including events for AWS Batch, create a trail.
A _trail_ enables CloudTrail to deliver log files to an Amazon S3 bucket. By default, when you create a trail
in the console, the trail applies to all AWS Regions. The trail logs events from all Regions in the AWS partition
and delivers the log files to the Amazon S3 bucket that you specify. Additionally, you can configure other AWS services
to further analyze and act upon the event data collected in CloudTrail logs. For more information, see the
following:

- [Overview
  for Creating a Trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [CloudTrail Supported Services and Integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations")
- [Configuring
  Amazon SNS Notifications for CloudTrail](../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md "../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md")
- [Receiving CloudTrail Log Files from Multiple Regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md") and [Receiving CloudTrail Log Files from Multiple Accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")
  All AWS Batch actions are logged by CloudTrail and are documented in the https://docs.aws.amazon.com/batch/latest/APIReference/. For example,
  calls to the `SubmitJob`, `ListJobs` and `DescribeJobs` sections generate entries in the
  CloudTrail log files.

Every event or log entry contains information about who generated the request. The identity information
helps you determine the following:

- Whether the request was made with root or IAM user credentials.
- Whether the request was made with temporary security credentials for a role or federated user.
- Whether the request was made by another AWS service.
  For more information, see the [CloudTrail userIdentity
  Element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md").
