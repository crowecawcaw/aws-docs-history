# About AWS CodeBuild information in

CloudTrail

CloudTrail is enabled on your AWS account when you create the account. When activity
occurs in CodeBuild, that activity is recorded in a CloudTrail event along with other AWS
service events in **Event history**. You can view, search, and download
recent events in your AWS account. For more information, see [Viewing events with CloudTrail event
history](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md") in the _AWS CloudTrail User Guide_.

For an ongoing record of events in your AWS account, including events for CodeBuild,
create a trail. A trail enables CloudTrail to deliver log files to an S3 bucket. By default,
when you create a trail in the console, the trail applies to all regions. The trail logs
events from all regions in the AWS partition and delivers the log files to the S3
bucket that you specify. You can configure other AWS services to further analyze and
act upon the event data collected in CloudTrail logs. For more information, see:

- [Overview
  for creating a trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [CloudTrail supported services and integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations")
- [Configuring
  Amazon SNS notifications for CloudTrail](../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md "../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md")
- [Receiving CloudTrail log files from multiple regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md") and [Receiving CloudTrail log files from multiple accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")
  All CodeBuild actions are logged by CloudTrail and are documented in the [CodeBuild API Reference](../APIReference.md "../APIReference.md"). For example, calls to the
  `CreateProject` (in the AWS CLI, `create-project`),
  `StartBuild` (in the AWS CLI, `start-project`), and
  `UpdateProject` (in the AWS CLI, `update-project`) actions
  generate entries in the CloudTrail log files.

Every event or log entry contains information about who generated the request. The
identity information helps you determine the following:

- Whether the request was made with root or user credentials.
- Whether the request was made with temporary security credentials for a role or
  federated user.
- Whether the request was made by another AWS service.
  For more information, see the [CloudTrail userIdentity
  element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md")in the _AWS CloudTrail User Guide_.
