For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Logging Timestream for InfluxDB API calls with AWS CloudTrail

Timestream for InfluxDB is integrated with AWS CloudTrail, a service that provides a record of actions taken by a
user, role, or an AWS service in Timestream for InfluxDB. CloudTrail captures Data Definition Language (DDL) API calls
for Timestream for InfluxDB as events. The calls that are captured include calls from the Timestream for InfluxDB console and code calls
to the Timestream for InfluxDB API operations. If you create a trail, you can enable continuous delivery of CloudTrail
events to an Amazon Simple Storage Service (Amazon S3) bucket, including events for Timestream for InfluxDB. If you don't configure a trail,
you can still view the most recent events on the CloudTrail console in **Event
history**. Using the information collected by CloudTrail, you can determine the request
that was made to Timestream for InfluxDB, the IP address from which the request was made, who made the request, when
it was made, and additional details.

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").

## Timestream for InfluxDB information in CloudTrail

CloudTrail is enabled on your AWS account when you create the account. When activity occurs in
Timestream for InfluxDB, that activity is recorded in a CloudTrail event along with other AWS service events in
**Event history**. You can view, search, and download recent events in your
AWS account. For more information, see [Viewing Events with CloudTrail Event History](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").

For an ongoing record of events in your AWS account, including events for Timestream for InfluxDB, create a
trail. A _trail_ enables CloudTrail to deliver log files to an Amazon S3 bucket. By
default, when you create a trail in the console, the trail applies to all AWS Regions. The
trail logs events from all Regions in the AWS partition and delivers the log files to the
Amazon S3 bucket that you specify. Additionally, you can configure other AWS services to further
analyze and act upon the event data collected in CloudTrail logs.

For more information, see the following topics in the
_AWS CloudTrail User Guide_:

- [Overview for
  Creating a Trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [CloudTrail Supported Services and Integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations")
- [Configuring Amazon SNS
  Notifications for CloudTrail](../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md "../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md")
- [Receiving CloudTrail Log Files from Multiple Regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md")
- [Receiving CloudTrail Log Files from Multiple Accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")
- [Logging data events](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md")

Every event or log entry contains information about who generated the request. The
identity information helps you determine the following:

- Whether the request was made with root or AWS Identity and Access Management (IAM) user credentials
- Whether the request was made with temporary security credentials for a role or
  federated user
- Whether the request was made by another AWS service

For more information, see the [CloudTrail userIdentity
Element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md").
