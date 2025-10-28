# WorkSpaces Secure Browser information in CloudTrail

CloudTrail is enabled on your AWS account when you create the account. When activity occurs in
Amazon WorkSpaces Secure Browser, that activity is recorded in a CloudTrail event along with other AWS service events in
**Event history**. In **Event history**, you can view,
search, and download recent events in your AWS account. For more information, see [Viewing events with CloudTrail Event history](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").

For an ongoing record of events in your AWS account, including events for Amazon WorkSpaces Secure Browser, you
can create a trail. A _trail_ enables CloudTrail to deliver log files to an Amazon S3
bucket. By default, when you create a trail in the console, the trail applies to all
AWSRegions. The trail logs events from all Regions in the AWS partition and delivers the
log files to the Amazon S3 bucket that you specify. Additionally, you can configure other AWS
services to further analyze and act upon the event data collected in CloudTrail logs. For more
information, see the following:

- [Overview for creating a trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [CloudTrail supported services and integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md")
- [Configuring Amazon SNS notifications
  for CloudTrail](../../../awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.md "../../../awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.md")
- [Receiving CloudTrail log
  files from multiple regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md") and [Receiving CloudTrail log
  files from multiple accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")
  All Amazon WorkSpaces Secure Browser actions are logged by CloudTrail and are documented in the _Amazon WorkSpaces API
  Reference_. For example, calls to the
  `CreatePortal`, `DeleteUserSettings` and
  `ListBrowserSettings` actions generate entries in the CloudTrail log files.

Every event or log entry contains information about who generated the request. The
identity information helps you determine the following:

- Whether the request was made with root or IAM user credentials.
- Whether the request was made with temporary security credentials for a role or
  federated user.
- Whether the request was made by another AWS service.
  For more information, see the [CloudTrail userIdentity
  element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md").
