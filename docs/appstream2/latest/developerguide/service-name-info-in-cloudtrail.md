

# WorkSpaces Applications Information in CloudTrail
<a name="service-name-info-in-cloudtrail"></a>

CloudTrail is enabled on your AWS account when you create the account. When supported event activity occurs in WorkSpaces Applications, that activity is recorded in a CloudTrail event along with other AWS service events in **Event history**. You can view, search, and download recent events in your AWS account. For more information, see [Viewing Events with CloudTrail Event History](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html). 

For an ongoing record of events in your AWS account, including events for WorkSpaces Applications, create a trail. A *trail* enables CloudTrail to deliver log files to an Amazon S3 bucket. By default, when you create a trail in the console, the trail applies to all AWS Regions. The trail logs events from all Regions in the AWS partition and delivers the log files to the Amazon S3 bucket that you specify. Additionally, you can configure other AWS services to further analyze and act upon the event data collected in CloudTrail logs. For more information, see the following: 
+ [Overview for Creating a Trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html)
+ [CloudTrail Supported Services and Integrations](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.html#cloudtrail-aws-service-specific-topics-integrations)
+ [Configuring Amazon SNS Notifications for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/getting_notifications_top_level.html)
+ [Receiving CloudTrail Log Files from Multiple Regions](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.html) and [Receiving CloudTrail Log Files from Multiple Accounts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.html)

WorkSpaces Applications supports logging the following actions as events in CloudTrail log files:
+ [AssociateFleet](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_AssociateFleet.html)
+ [BatchAssociateUserStack](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_BatchAssociateUserStack.html)
+ [BatchDisassociateUserStack](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_BatchDisassociateUserStack.html)
+ [CopyImage](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_CopyImage.html)
+ [CreateDirectoryConfig](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_CreateDirectoryConfig.html)
+ [CreateFleet](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_CreateFleet.html)
+ [CreateImageBuilder](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_CreateImageBuilder.html)
+ [CreateImageBuilderStreamingURL](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_CreateImageBuilderStreamingURL.html)
+ [CreateStack](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_CreateStack.html)
+ [CreateStreamingURL](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_CreateStreamingURL.html)
+ [DeleteDirectoryConfig](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DeleteDirectoryConfig.html)
+ [DeleteFleet](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DeleteFleet.html)
+ [DeleteImage](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DeleteImage.html)
+ [DeleteImageBuilder](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DeleteImageBuilder.html)
+ [DeleteImagePermissions](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DeleteImagePermissions.html)
+ [DeleteStack](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DeleteStack.html)
+ [DescribeDirectoryConfigs](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DescribeDirectoryConfigs.html)
+ [DescribeFleets](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DescribeFleets.html)
+ [DescribeImageBuilders](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DescribeImageBuilders.html)
+ [DescribeImagePermissions](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DescribeImagePermissions.html)
+ [DescribeImages](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DescribeImages.html)
+ [DescribeSessions](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DescribeSessions.html)
+ [DescribeStacks](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DescribeStacks.html)
+ [DescribeUserStackAssociations](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DescribeUserStackAssociations.html)
+ [ExpireSession](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_ExpireSession.html)
+ [ListAssociatedFleets](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_ListAssociatedFleets.html)
+ [ListAssociatedStacks](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_ListAssociatedStacks.html)
+ [ListTagsForResource](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_ListTagsForResource.html)
+ [StartFleet](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_StartFleet.html)
+ [StartImageBuilder](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_StartImageBuilder.html)
+ [StopFleet](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_StopFleet.html)
+ [StopImageBuilder](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_StopImageBuilder.html)
+ [TagResource](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_TagResource.html)
+ [UntagResource](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_UntagResource.html)
+ [UpdateDirectoryConfig](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_UpdateDirectoryConfig.html)
+ [UpdateFleet](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_UpdateFleet.html)
+ [UpdateImagePermissions](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_UpdateImagePermissions.html)
+ [UpdateStack](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_UpdateStack.html)

Every event or log entry contains information about who generated the request. The identity information helps you determine the following: 
+ Whether the request was made with root or IAM user credentials.
+ Whether the request was made with temporary security credentials for a role or federated user.
+ Whether the request was made by another AWS service.

For more information, see the [CloudTrail userIdentity Element](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html).