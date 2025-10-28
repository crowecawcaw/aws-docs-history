# AppStream 2.0 Information in CloudTrail

CloudTrail is enabled on your AWS account when you create the account. When supported event
activity occurs in AppStream 2.0, that activity is recorded in a CloudTrail event along with other
AWS service events in **Event history**. You can view, search, and download
recent events in your AWS account. For more information, see [Viewing Events with CloudTrail Event
History](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").

For an ongoing record of events in your AWS account, including events for AppStream 2.0,
create a trail. A _trail_ enables CloudTrail to deliver log files to an Amazon S3 bucket.
By default, when you create a trail in the console, the trail applies to all AWS Regions. The trail logs events
from all Regions in the AWS partition and delivers the log files to the Amazon S3 bucket that you
specify. Additionally, you can configure other AWS services to further analyze and act upon
the event data collected in CloudTrail logs. For more information, see the following:

- [Overview for
  Creating a Trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [CloudTrail Supported Services and Integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations")
- [Configuring Amazon SNS
  Notifications for CloudTrail](../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md "../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md")
- [Receiving CloudTrail Log Files from Multiple Regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md") and [Receiving CloudTrail
  Log Files from Multiple Accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")
  AppStream 2.0 supports logging the following actions as events in CloudTrail log files:

- [AssociateFleet](../APIReference/API_AssociateFleet.md "../APIReference/API_AssociateFleet.md")
- [BatchAssociateUserStack](../APIReference/API_BatchAssociateUserStack.md "../APIReference/API_BatchAssociateUserStack.md")
- [BatchDisassociateUserStack](../APIReference/API_BatchDisassociateUserStack.md "../APIReference/API_BatchDisassociateUserStack.md")
- [CopyImage](../APIReference/API_CopyImage.md "../APIReference/API_CopyImage.md")
- [CreateDirectoryConfig](../APIReference/API_CreateDirectoryConfig.md "../APIReference/API_CreateDirectoryConfig.md")
- [CreateFleet](../APIReference/API_CreateFleet.md "../APIReference/API_CreateFleet.md")
- [CreateImageBuilder](../APIReference/API_CreateImageBuilder.md "../APIReference/API_CreateImageBuilder.md")
- [CreateImageBuilderStreamingURL](../APIReference/API_CreateImageBuilderStreamingURL.md "../APIReference/API_CreateImageBuilderStreamingURL.md")
- [CreateStack](../APIReference/API_CreateStack.md "../APIReference/API_CreateStack.md")
- [CreateStreamingURL](../APIReference/API_CreateStreamingURL.md "../APIReference/API_CreateStreamingURL.md")
- [DeleteDirectoryConfig](../APIReference/API_DeleteDirectoryConfig.md "../APIReference/API_DeleteDirectoryConfig.md")
- [DeleteFleet](../APIReference/API_DeleteFleet.md "../APIReference/API_DeleteFleet.md")
- [DeleteImage](../APIReference/API_DeleteImage.md "../APIReference/API_DeleteImage.md")
- [DeleteImageBuilder](../APIReference/API_DeleteImageBuilder.md "../APIReference/API_DeleteImageBuilder.md")
- [DeleteImagePermissions](../APIReference/API_DeleteImagePermissions.md "../APIReference/API_DeleteImagePermissions.md")
- [DeleteStack](../APIReference/API_DeleteStack.md "../APIReference/API_DeleteStack.md")
- [DescribeDirectoryConfigs](../APIReference/API_DescribeDirectoryConfigs.md "../APIReference/API_DescribeDirectoryConfigs.md")
- [DescribeFleets](../APIReference/API_DescribeFleets.md "../APIReference/API_DescribeFleets.md")
- [DescribeImageBuilders](../APIReference/API_DescribeImageBuilders.md "../APIReference/API_DescribeImageBuilders.md")
- [DescribeImagePermissions](../APIReference/API_DescribeImagePermissions.md "../APIReference/API_DescribeImagePermissions.md")
- [DescribeImages](../APIReference/API_DescribeImages.md "../APIReference/API_DescribeImages.md")
- [DescribeSessions](../APIReference/API_DescribeSessions.md "../APIReference/API_DescribeSessions.md")
- [DescribeStacks](../APIReference/API_DescribeStacks.md "../APIReference/API_DescribeStacks.md")
- [DescribeUserStackAssociations](../APIReference/API_DescribeUserStackAssociations.md "../APIReference/API_DescribeUserStackAssociations.md")
- [ExpireSession](../APIReference/API_ExpireSession.md "../APIReference/API_ExpireSession.md")
- [ListAssociatedFleets](../APIReference/API_ListAssociatedFleets.md "../APIReference/API_ListAssociatedFleets.md")
- [ListAssociatedStacks](../APIReference/API_ListAssociatedStacks.md "../APIReference/API_ListAssociatedStacks.md")
- [ListTagsForResource](../APIReference/API_ListTagsForResource.md "../APIReference/API_ListTagsForResource.md")
- [StartFleet](../APIReference/API_StartFleet.md "../APIReference/API_StartFleet.md")
- [StartImageBuilder](../APIReference/API_StartImageBuilder.md "../APIReference/API_StartImageBuilder.md")
- [StopFleet](../APIReference/API_StopFleet.md "../APIReference/API_StopFleet.md")
- [StopImageBuilder](../APIReference/API_StopImageBuilder.md "../APIReference/API_StopImageBuilder.md")
- [TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md")
- [UntagResource](../APIReference/API_UntagResource.md "../APIReference/API_UntagResource.md")
- [UpdateDirectoryConfig](../APIReference/API_UpdateDirectoryConfig.md "../APIReference/API_UpdateDirectoryConfig.md")
- [UpdateFleet](../APIReference/API_UpdateFleet.md "../APIReference/API_UpdateFleet.md")
- [UpdateImagePermissions](../APIReference/API_UpdateImagePermissions.md "../APIReference/API_UpdateImagePermissions.md")
- [UpdateStack](../APIReference/API_UpdateStack.md "../APIReference/API_UpdateStack.md")
  Every event or log entry contains information about who generated the request. The
  identity information helps you determine the following:

- Whether the request was made with root or IAM user credentials.
- Whether the request was made with temporary security credentials for a role or
  federated user.
- Whether the request was made by another AWS service.
  For more information, see the [CloudTrail userIdentity
  Element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md").
