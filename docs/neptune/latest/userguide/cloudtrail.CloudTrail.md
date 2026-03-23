# Neptune Information in CloudTrail

CloudTrail is enabled on your AWS account when you create the account. When activity occurs in
Amazon Neptune, that activity is recorded in a CloudTrail event along with other AWS service events
in **Event history**. You can view, search, and download recent events in
your AWS account. For more information, see [Viewing Events with CloudTrail Event
History](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").

For an ongoing record of events in your AWS account, including events for
Neptune, create a trail. A trail enables CloudTrail to deliver log files to an Amazon S3
bucket. By default, when you create a trail in the console, the trail applies to all
Regions. The trail logs events from all Regions in the AWS partition and delivers the
log files to the Amazon S3 bucket that you specify. Additionally, you can configure other
AWS services to further analyze and act upon the event data collected in CloudTrail logs.
For more information, see:

- [Overview for Creating a Trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [CloudTrail Supported Services and Integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations")
- [Configuring Amazon SNS Notifications
  for CloudTrail](../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md "../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md")
- [Receiving CloudTrail Log
  Files from Multiple Regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md") and [Receiving CloudTrail Log
  Files from Multiple Accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")
  If an action is taken on behalf of your AWS account using the Neptune console, the
  Neptune command line interface, or the Neptune SDK APIs, AWS CloudTrail logs the action as
  calls made to the Amazon RDS API. For example, if you use the Neptune console to modify a
  DB instance or call the AWS CLI [modify-db-instance](../../../cli/latest/reference/neptune/modify-db-instance.md "../../../cli/latest/reference/neptune/modify-db-instance.md") command, the AWS CloudTrail log shows a call to the Amazon RDS API
  [ModifyDBInstance](API_ModifyDBInstance.md "API_ModifyDBInstance.md") action. For a list
  of the Neptune API actions that are logged by AWS CloudTrail, see the [Neptune API Reference](neptune-api-reference.md "neptune-api-reference.md").

###### Note

AWS CloudTrail only logs events for Neptune Management API calls, such as creating an
instance or cluster. If you want to audit changes to your graph, you can use audit
logs. For more information, see [Using Audit Logs with Amazon Neptune Clusters](auditing.md "auditing.md").

Every event or log entry contains information about who generated the request. The
identity information helps you determine the following:

- Whether the request was made with root or IAM user credentials.
- Whether the request was made with temporary security credentials for a role or
  federated user.
- Whether the request was made by another AWS service.
  For more information, see the [CloudTrail userIdentity
  Element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md").
