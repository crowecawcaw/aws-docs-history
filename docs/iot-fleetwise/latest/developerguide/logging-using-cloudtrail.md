# Log AWS IoT FleetWise API calls using AWS CloudTrail

AWS IoT FleetWise is integrated with AWS CloudTrail, a service that provides a record of actions taken
by a user, role, or an AWS service in AWS IoT FleetWise. CloudTrail captures all API calls for AWS IoT FleetWise as
events. The calls captured include calls from the AWS IoT FleetWise console and code calls to the
AWS IoT FleetWise API operations. If you create a trail, you can enable continuous delivery of CloudTrail
events to an Amazon S3 bucket, including events for AWS IoT FleetWise. If you don't configure a trail, you
can still view the most recent events in the CloudTrail console in **Event history**.
Using the information collected by CloudTrail, you can determine the request that was made to
AWS IoT FleetWise, the IP address from which the request was made, who made the request, when it was
made, and additional details.

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").

## AWS IoT FleetWise information in CloudTrail

CloudTrail is enabled on your AWS account when you create the account. When activity occurs in
AWS IoT FleetWise, that activity is recorded in a CloudTrail event along with other AWS service events in
**Event history**. You can view, search, and download recent events in your
AWS account. For more information, see [Viewing Events with CloudTrail Event History](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").

For an ongoing record of events in your AWS account, including events for AWS IoT FleetWise,
create a trail. A _trail_ enables CloudTrail to deliver log files to an Amazon S3
bucket. By default, when you create a trail in the console, the trail applies to all AWS
Regions. The trail logs events from all Regions in the AWS partition and delivers the log
files to the Amazon S3 bucket that you specify. Additionally, you can configure other AWS
services to further analyze and act upon the event data collected in CloudTrail logs. For more
information, see the following:

- [Overview for
  creating a trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [CloudTrail supported services and integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations")
- [Configuring Amazon SNS
  notifications for CloudTrail](../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md "../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md")
- [Receiving CloudTrail log files from multiple Regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md")
- [Receiving CloudTrail log files from multiple accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")

All AWS IoT FleetWise actions are logged by CloudTrail and are documented in the
[AWS IoT FleetWise API Reference](../APIReference.md "../APIReference.md"). For example, calls to the
`CreateCampaign`, `AssociateVehicleFleet`, and
`GetModelManifest` actions generate entries in the CloudTrail log files.

Every event or log entry contains information about who generated the request. The
identity information helps you determine the following:

- Whether the request was made with root or IAM user credentials.
- Whether the request was made with temporary security credentials for a role or
  federated user.
- Whether the request was made by another AWS service.

For more information, see the [CloudTrail userIdentity
element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md").
