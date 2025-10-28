**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Log Amazon Pinpoint API calls with AWS CloudTrail

Amazon Pinpoint is integrated with AWS CloudTrail, which is a service that provides a record of actions
taken by a user, role, or AWS service in Amazon Pinpoint. CloudTrail captures API calls for Amazon Pinpoint as
events. The calls that are captured include calls from the Amazon Pinpoint console and code calls to
Amazon Pinpoint API operations.

If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon Simple Storage Service
(Amazon S3) bucket, including events for Amazon Pinpoint. If you don't configure a trail, you can still
view the most recent events by using **Event history** on the CloudTrail console.
Using the information collected by CloudTrail, you can determine the request that was made to
Amazon Pinpoint, the IP address that the request was made from, who made the request, when it was
made, and additional details.

To learn more about CloudTrail, including how to configure and enable it, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").

## Amazon Pinpoint information in CloudTrail

CloudTrail is enabled on your AWS account when you create the account. When supported
event activity occurs in Amazon Pinpoint, that activity is recorded in a CloudTrail event along with
other AWS service events in **Event history**. You can view, search,
and download recent events in your AWS account. For more information, see [Viewing events with CloudTrail event
history](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").

For an ongoing record of events in your AWS account, including events for Amazon Pinpoint,
create a trail. A _trail_ enables CloudTrail to deliver log files to an
Amazon S3 bucket. By default, when you create a trail in the console, the trail applies to
all AWS Regions. The trail logs events from all Regions in the AWS partition and
delivers the log files to the Amazon S3 bucket that you specify. Additionally, you can
configure other AWS services to further analyze and act upon the event data collected
in CloudTrail logs. For more information, see the following:

- [Overview
  for creating a trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [CloudTrail supported services and integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations")
- [Configuring
  Amazon SNS notifications for CloudTrail](../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md "../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md")
- [Receiving CloudTrail log files from multiple regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md") and [Receiving CloudTrail log files from multiple accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")

Every event or log entry contains information about who generated the request. The
identity information helps you determine:

- Whether the request was made with root or AWS Identity and Access Management user
  credentials.
- Whether the request was made with temporary security credentials for a role or
  federated user.
- Whether the request was made by another AWS service.

For more information, see [CloudTrail userIdentity
element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md").

You can create a trail and store your log files in your Amazon S3 bucket for as long as you
want. Also, you can define Amazon S3 lifecycle rules to archive or delete log files
automatically. By default, your log files are encrypted with Amazon S3 server-side encryption
(SSE).

To be notified of log file delivery, configure CloudTrail to publish Amazon SNS notifications
when new log files are delivered. For more information, see [Configuring Amazon SNS
notifications for CloudTrail](../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md "../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md").

You can also aggregate Amazon Pinpoint log files from multiple AWS Regions and multiple AWS
accounts into a single Amazon S3 bucket. For more information, see [Receiving
CloudTrail log files from multiple regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md") and [Receiving
CloudTrail log files from multiple accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md").

You can use CloudTrail to log actions for the following Amazon Pinpoint APIs:

- [Amazon Pinpoint API](pinpoint-cloudtrail-actions.md "pinpoint-cloudtrail-actions.md")
- [Amazon Pinpoint SMS and Voice
  API](pinpoint-sms-voice-cloudtrail-actions.md "pinpoint-sms-voice-cloudtrail-actions.md")
