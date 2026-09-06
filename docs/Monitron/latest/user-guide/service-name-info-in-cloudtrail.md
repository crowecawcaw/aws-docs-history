

Amazon Monitron is no longer open to new customers. Existing customers can continue to use the service as normal. For capabilities similar to Amazon Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron).

# Amazon Monitron information in CloudTrail
<a name="service-name-info-in-cloudtrail"></a>

CloudTrail is enabled for your AWS users when you create your account. When supported event activity occurs in Amazon Monitron, that activity is recorded in a CloudTrail event along with other AWS service events in **Event history**. You can view, search, and download recent events in your AWS account. For more information, see [Viewing Events with CloudTrail Event History](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html). 

For an ongoing record of events in your AWS account, including events for Amazon Monitron, create a trail. A *trail* enables CloudTrail to deliver log files to an Amazon S3 bucket. By default, when you create a trail in the console, the trail applies to all AWS Regions. The trail logs events from all Regions in the AWS partition and delivers the log files to the Amazon S3 bucket that you specify. Additionally, you can configure other AWS services to further analyze and act upon the event data collected in CloudTrail logs. For more information, see the following: 
+ [Overview for Creating a Trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html)
+ [CloudTrail Supported Services and Integrations](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.html#cloudtrail-aws-service-specific-topics-integrations)
+ [Configuring Amazon SNS Notifications for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/getting_notifications_top_level.html)
+ [Receiving CloudTrail Log Files from Multiple Regions](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.html) and [Receiving CloudTrail Log Files from Multiple Accounts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.html)

Amazon Monitron supports logging a number of actions as events. Although the operations are publicly accessible through the AWS console or the Amazon Monitron mobile app, the APIs themselves are not public and are subject to change. They are meant for logging purposes only, and applications should not be built with them.

Amazon Monitron supports the following actions as events in CloudTrail log files:
+ [CreateProject](https://docs.aws.amazon.com/Monitron/latest/user-guide/mp-creating-project.html)
+ [UpdateProject](https://docs.aws.amazon.com/Monitron/latest/user-guide/mp-updating-project.html)
+ [DeleteProject](https://docs.aws.amazon.com/Monitron/latest/user-guide/mp-delete-project.html)
+ [GetProject](https://docs.aws.amazon.com/Monitron/latest/user-guide/mp-project-tasks.html)
+ [ListProjects](https://docs.aws.amazon.com/Monitron/latest/user-guide/mp-project-tasks.html)
+ [AssociateProjectAdminUser](https://docs.aws.amazon.com/Monitron/latest/user-guide/mu-adding-user.html)
+ [DisassociateProjectAdminUser](https://docs.aws.amazon.com/Monitron/latest/user-guide/mu-remove-project-admin.html)
+ [ListProjectAdminUsers](https://docs.aws.amazon.com/Monitron/latest/user-guide/user-management-chapter.html)
+ [GetProjectAdminUser](https://docs.aws.amazon.com/Monitron/latest/user-guide/user-management-chapter.html)
+ [TagResource](https://docs.aws.amazon.com/Monitron/latest/user-guide/tagging.html#tag-original-1)
+ [UntagResource](https://docs.aws.amazon.com/Monitron/latest/user-guide/tagging.html#modify-tag-1)
+ [ListTagsForResource](https://docs.aws.amazon.com/Monitron/latest/user-guide/tagging.html)
+ [CreateSensor](https://docs.aws.amazon.com/Monitron/latest/user-guide/as-add-sensors.html)
+ [UpdateSensor](https://docs.aws.amazon.com/Monitron/latest/user-guide/as-edit-sensorposition.html)
+ [DeleteSensor](https://docs.aws.amazon.com/Monitron/latest/user-guide/as-delete-sensor.html)
+ [CreateGateway](https://docs.aws.amazon.com/Monitron/latest/user-guide/adding-gateway.html)
+ [DeleteGateway](https://docs.aws.amazon.com/Monitron/latest/user-guide/deleting-gateway.html)
+ [CreateSite](https://docs.aws.amazon.com/Monitron/latest/user-guide/SM-creating-site.html)
+ [UpdateSite](https://docs.aws.amazon.com/Monitron/latest/user-guide/SM-editing-site.html)
+ [DeleteSite](https://docs.aws.amazon.com/Monitron/latest/user-guide/SM-deleting-site.html)
+ [CreateAsset](https://docs.aws.amazon.com/Monitron/latest/user-guide/as-add-assets.html)
+ [UpdateAsset](https://docs.aws.amazon.com/Monitron/latest/user-guide/as-edit-assets.html)
+ [DeleteAsset](https://docs.aws.amazon.com/Monitron/latest/user-guide/as-delete-assets.html)
+ [CreateAssetStateTransition](https://docs.aws.amazon.com/Monitron/latest/user-guide/as-assets.html)
+ [CreateUserAccessRoleAssociation](https://docs.aws.amazon.com/Monitron/latest/user-guide/what-is-monitron.html)
+ [UpdateUserAccessRoleAssociation](https://docs.aws.amazon.com/Monitron/latest/user-guide/what-is-monitron.html)
+ [DeleteUserAccessRoleAssociation](https://docs.aws.amazon.com/Monitron/latest/user-guide/what-is-monitron.html)
+ [FinishSensorCommissioning](https://docs.aws.amazon.com/Monitron/latest/user-guide/as-add-sensors.html)
+ [StartSensorCommissioning](https://docs.aws.amazon.com/Monitron/latest/user-guide/adding-position.html)

Every event or log entry contains information about who generated the request. This contains details about the type of IAM identity that made the request, and which credentials were used. If temporary credentials were used, the element shows how the credentials were obtained. The identity information helps you determine the following: 
+ Whether the request was made with root or AWS Identity and Access Management (IAM) user credentials 
+ Whether the request was made with temporary security credentials for a role or federated user
+ Whether the request was made by another AWS service

For more information, see the [CloudTrail userIdentity Element](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html) in the *AWS CloudTrail User Guide*.