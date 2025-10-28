End of support notice: On November 13, 2025, AWS will discontinue support
for AWS Elemental MediaStore. After November 13, 2025, you will no longer be able to access the MediaStore console
or MediaStore resources. For more information, visit this
[blog post](https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/ "https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/").

# AWS Elemental MediaStore

information in CloudTrail

CloudTrail is enabled on your AWS account when you create the account. When supported
event activity occurs in AWS Elemental MediaStore, that activity is recorded in a CloudTrail
event along with other AWS service events in **Event history**.
You can view, search, and download recent events in your AWS account. For more
information, see [Viewing
Events with CloudTrail Event History](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").

For an ongoing record of events in your AWS account, including events for
MediaStore, create a trail. A trail enables CloudTrail to deliver log files to an Amazon S3
bucket. By default, when you create a trail in the console, the trail applies to all
AWS Regions. The trail logs events from all Regions in the AWS partition and
delivers the log files to the Amazon S3 bucket that you specify. Additionally, you can
configure other AWS services to further analyze and act upon the event data
collected in CloudTrail logs. For more information, see the following topics:

- [Overview for Creating a Trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [CloudTrail Supported Services and Integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations")
- [Configuring
  Amazon SNS Notifications for CloudTrail](../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md "../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md")
- [Receiving CloudTrail Log Files from Multiple Regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md") and [Receiving CloudTrail Log Files from Multiple Accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")
  AWS Elemental MediaStore supports logging the following operations as events in CloudTrail log
  files:

- [`CreateContainer`](../apireference/API_CreateContainer.md "../apireference/API_CreateContainer.md")
- [`DeleteContainer`](../apireference/API_DeleteContainer.md "../apireference/API_DeleteContainer.md")
- [`DeleteContainerPolicy`](../apireference/API_DeleteContainerPolicy.md "../apireference/API_DeleteContainerPolicy.md")
- [`DeleteCorsPolicy`](../apireference/API_API_DeleteCorsPolicy.md "../apireference/API_API_DeleteCorsPolicy.md")
- [`DescribeContainer`](../apireference/API_DescribeContainer.md "../apireference/API_DescribeContainer.md")
- [`GetContainerPolicy`](../apireference/API_GetContainerPolicy.md "../apireference/API_GetContainerPolicy.md")
- [`GetCorsPolicy`](../apireference/API_GetCorsPolicy.md "../apireference/API_GetCorsPolicy.md")
- [`ListContainers`](../apireference/API_ListContainers.md "../apireference/API_ListContainers.md")
- [`PutContainerPolicy`](../apireference/API_PutContainerPolicy.md "../apireference/API_PutContainerPolicy.md")
- [`PutCorsPolicy`](../apireference/API_PutCorsPolicy.md "../apireference/API_PutCorsPolicy.md")
  Every event or log entry contains information about who generated the request. The
  identity information helps you determine the following:

- Whether the request was made with root user or user credentials
- Whether the request was made with temporary security credentials for a
  role or federated user
- Whether the request was made by another AWS service
  For more information, see the [CloudTrail
  userIdentity Element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md").
