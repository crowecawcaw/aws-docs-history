# Logging AWS IoT TwinMaker API calls with

AWS CloudTrail

AWS IoT TwinMaker is integrated with AWS CloudTrail, a service that provides a record of actions
taken by a user, role, or an AWS service in AWS IoT TwinMaker. CloudTrail captures API calls for
AWS IoT TwinMaker as events. The calls captured include calls from the AWS IoT TwinMaker console and
code calls to the AWS IoT TwinMaker API operations. If you create a trail, you can enable
continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for AWS IoT TwinMaker. If
you don't configure a trail, you can still view the most recent events in the CloudTrail console in
**Event history**. Using the information collected by CloudTrail, you can
determine the request that was made to AWS IoT TwinMaker, the IP address from which the request
was made, who made the request, when it was made, and additional details.

For more information about CloudTrail, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").

## AWS IoT TwinMaker information in CloudTrail

When you create your AWS account, CloudTrail is automatically enabled. CloudTrail records
support event activity that occurs in AWS IoT TwinMaker, along with other AWS service events
in **Event history**. You can view, search, and download recent
events in your AWS account. For more information, see [Viewing events with CloudTrail event
history](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").

For an ongoing record of events in your AWS account, including events for
AWS IoT TwinMaker, create a trail. A _trail_ enables CloudTrail to deliver log
files to an Amazon S3 bucket. By default, when you create a trail in the console, the
trail applies to all AWS Regions. CloudTrail
logs
events from all Regions in the AWS partition and delivers the log files to the
Amazon S3 bucket that you specify. Additionally, you can configure other AWS services
to further analyze and act upon the event data collected in CloudTrail logs. For more
information, see the following:

- [Overview for
  creating a trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [CloudTrail supported services and integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations")
- [Configuring Amazon SNS
  notifications for CloudTrail](../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md "../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md")
- [Receiving CloudTrail log files from multiple Regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md") and [Receiving CloudTrail
  log files from multiple accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")

Most AWS IoT TwinMaker operations are logged by CloudTrail and are documented in the [AWS IoT TwinMaker API Reference](../apireference/Welcome.md "../apireference/Welcome.md").

The following data plane operations aren't logged by CloudTrail:

- [GetPropertyValue](../apireference/API_GetPropertyValue.md "../apireference/API_GetPropertyValue.md")
- [GetPropertyValueHistory](../apireference/API_GetPropertyValueHistory.md "../apireference/API_GetPropertyValueHistory.md")
- [BatchPutPropertyValues](../apireference/API_BatchPutPropertyValues.md "../apireference/API_BatchPutPropertyValues.md")

Every event or log entry contains information about who generated the request. The
identity information helps you determine the following:

- Whether the request was made with root or user credentials.
- Whether the request was made with temporary security credentials for a role or
  federated user.
- Whether the request was made by another AWS service.

For more information, see the [CloudTrail userIdentity
element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md").
