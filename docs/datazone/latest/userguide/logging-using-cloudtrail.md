# Logging Amazon DataZone API calls using AWS CloudTrail

Amazon DataZone is integrated with AWS CloudTrail, a service that provides a record of actions taken by
a user, role, or an AWS service in Amazon DataZone. CloudTrail captures all API calls for Amazon DataZone as
events. The calls captured include calls from the Amazon DataZone console and code calls to the
Amazon DataZone API operations. If you create a trail, you can enable continuous delivery of CloudTrail
events to an Amazon S3 bucket, including events for Amazon DataZone. If you don't configure a trail, you
can still view the most recent events in the CloudTrail console in **Event history**.
Using the information collected by CloudTrail, you can determine the request that was made to
Amazon DataZone, the IP address from which the request was made, who made the request, when it was
made, and additional details.

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md").

## Amazon DataZone information in CloudTrail

CloudTrail is enabled on your AWS account when you create the account. When activity occurs in
the Amazon DataZone management console, that activity is recorded in a CloudTrail event along with other
AWS service events in **Event history**. You can view, search, and download
recent events in your AWS account. For more information, see [Viewing events with CloudTrail Event history](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").

For an ongoing record of events in your AWS account, including events for Amazon DataZone,
create a trail. A _trail_ enables CloudTrail to deliver log files to an Amazon S3
bucket. By default, when you create a trail in the console, the trail applies to all
AWS Regions. The trail logs events from all Regions in the AWS partition and delivers the
log files to the Amazon S3 bucket that you specify. Additionally, you can configure other AWS
services to further analyze and act upon the event data collected in CloudTrail logs. For more
information, see the following:

- [Overview for creating a trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [CloudTrail supported services and integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md")
- [Configuring Amazon SNS notifications for CloudTrail](../../../awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.md "../../../awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.md")
- [Receiving CloudTrail log files from multiple regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md") and [Receiving CloudTrail log files from multiple accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")

All Amazon DataZone actions are logged by CloudTrail.
