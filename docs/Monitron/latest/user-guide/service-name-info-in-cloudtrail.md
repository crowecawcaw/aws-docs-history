Amazon Monitron is no longer open to new customers. Existing customers can
continue to use the service as normal. For capabilities similar to Amazon
Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron "https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron").

# Amazon Monitron information in

CloudTrail

CloudTrail is enabled for your AWS users when you create your account. When supported
event activity occurs in Amazon Monitron, that activity is recorded in a CloudTrail event along
with other AWS service events in **Event history**. You can view,
search, and download recent events in your AWS account. For more information, see
[Viewing Events with CloudTrail Event
History](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").

For an ongoing record of events in your AWS account, including events for
Amazon Monitron, create a trail. A _trail_ enables CloudTrail to deliver log
files to an Amazon S3 bucket. By default, when you create a trail in the console, the trail
applies to all AWS Regions. The trail logs events from all Regions in the AWS
partition and delivers the log files to the Amazon S3 bucket that you specify. Additionally,
you can configure other AWS services to further analyze and act upon the event data
collected in CloudTrail logs. For more information, see the following:

- [Overview
  for Creating a Trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [CloudTrail Supported Services and Integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations")
- [Configuring
  Amazon SNS Notifications for CloudTrail](../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md "../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md")
- [Receiving CloudTrail Log Files from Multiple Regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md") and [Receiving CloudTrail Log Files from Multiple Accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")
  Amazon Monitron supports logging a number of actions as events. Although the operations
  are publicly accessible through the AWS console or the Amazon Monitron mobile app, the
  APIs themselves are not public and are subject to change. They are meant for logging
  purposes only, and applications should not be built with them.

Amazon Monitron supports the following actions as events in CloudTrail log files:

- [CreateProject](mp-creating-project.md "mp-creating-project.md")
- [UpdateProject](mp-updating-project.md "mp-updating-project.md")
- [DeleteProject](mp-delete-project.md "mp-delete-project.md")
- [GetProject](mp-project-tasks.md "mp-project-tasks.md")
- [ListProjects](mp-project-tasks.md "mp-project-tasks.md")
- [AssociateProjectAdminUser](mu-adding-user.md "mu-adding-user.md")
- [DisassociateProjectAdminUser](mu-remove-project-admin.md "mu-remove-project-admin.md")
- [ListProjectAdminUsers](user-management-chapter.md "user-management-chapter.md")
- [GetProjectAdminUser](user-management-chapter.md "user-management-chapter.md")
- [TagResource](tagging.md#tag-original-1 "tagging.md#tag-original-1")
- [UntagResource](tagging.md#modify-tag-1 "tagging.md#modify-tag-1")
- [ListTagsForResource](tagging.md "tagging.md")
- [CreateSensor](as-add-sensors.md "as-add-sensors.md")
- [UpdateSensor](as-edit-sensorposition.md "as-edit-sensorposition.md")
- [DeleteSensor](as-delete-sensor.md "as-delete-sensor.md")
- [CreateGateway](adding-gateway.md "adding-gateway.md")
- [DeleteGateway](deleting-gateway.md "deleting-gateway.md")
- [CreateSite](SM-creating-site.md "SM-creating-site.md")
- [UpdateSite](SM-editing-site.md "SM-editing-site.md")
- [DeleteSite](SM-deleting-site.md "SM-deleting-site.md")
- [CreateAsset](as-add-assets.md "as-add-assets.md")
- [UpdateAsset](as-edit-assets.md "as-edit-assets.md")
- [DeleteAsset](as-delete-assets.md "as-delete-assets.md")
- [CreateAssetStateTransition](as-assets.md "as-assets.md")
- [CreateUserAccessRoleAssociation](what-is-monitron.md "what-is-monitron.md")
- [UpdateUserAccessRoleAssociation](what-is-monitron.md "what-is-monitron.md")
- [DeleteUserAccessRoleAssociation](what-is-monitron.md "what-is-monitron.md")
- [FinishSensorCommissioning](as-add-sensors.md "as-add-sensors.md")
- [StartSensorCommissioning](adding-position.md "adding-position.md")
  Every event or log entry contains information about who generated the request. This
  contains details about the type of IAM identity that made the request, and which
  credentials were used. If temporary credentials were used, the element shows how the
  credentials were obtained. The identity information helps you determine the following:

- Whether the request was made with root or AWS Identity and Access Management (IAM) user credentials
- Whether the request was made with temporary security credentials for a role or
  federated user
- Whether the request was made by another AWS service
  For more information, see the [CloudTrail userIdentity
  Element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md") in the _AWS CloudTrail User Guide_.
