End of support notice: On May 20, 2026, AWS will end support for
AWS IoT Events. After May 20, 2026, you will no longer be able to access the AWS IoT Events console or AWS IoT Events
resources. For more information, see [AWS IoT Events end of
support](iotevents-end-of-support.md "iotevents-end-of-support.md").

# Logging AWS IoT Events API calls with AWS CloudTrail

AWS IoT Events is integrated with AWS CloudTrail, a service that provides a record of actions taken by a
user, role, or an AWS service in AWS IoT Events. CloudTrail captures all API calls for AWS IoT Events as events,
including calls from the AWS IoT Events console and from code calls to the AWS IoT Events APIs.

If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon S3
bucket, including events for AWS IoT Events. If you don't configure a trail, you can still view the
most recent events in the CloudTrail console in **Event history**. Using the
information collected by CloudTrail, you can determine the request that was made to AWS IoT Events, the IP
address from which the request was made, who made the request, when it was made, and
additional details.

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").

## AWS IoT Events information in CloudTrail

CloudTrail is enabled on your AWS account when you create the account. When activity occurs
in AWS IoT Events, that activity is recorded in a CloudTrail event with other AWS service events in
**Event history**. You can view, search, and download recent events in
your AWS account. For more information, see [Working with CloudTrail Event
history](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").

For an ongoing record of events in your AWS account, including events for AWS IoT Events,
create a trail. A trail enables CloudTrail to deliver log files to an Amazon S3 bucket. By default,
when you create a trail in the console, the trail applies to all AWS Regions. The trail
logs events from all Regions in the AWS partition and delivers the log files to the Amazon S3
bucket that you specify. Additionally, you can configure other AWS services to further
analyze and act on the event data collected in CloudTrail logs. For more information, see:

- [Creating a trail for your AWS account](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [CloudTrail
  supported services and integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md")
- [Configuring Amazon SNS notifications for CloudTrail](../../../awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.md "../../../awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.md")
- [Receiving CloudTrail log files from multiple regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md") and [Receiving CloudTrail log files from multiple accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")

Every event or log entry contains information about who generated the request. The
identity information helps you determine the following:

- Whether the request was made with root or IAM user credentials.
- Whether the request was made with temporary security credentials for a role or
  federated user.
- Whether the request was made by another AWS service.

For more information, see the [CloudTrail
userIdentity element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md"). AWS IoT Events actions are documented in the [AWS IoT Events API
reference](../apireference/Welcome.md "../apireference/Welcome.md").
