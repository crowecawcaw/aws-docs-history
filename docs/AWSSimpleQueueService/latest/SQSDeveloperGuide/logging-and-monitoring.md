# Logging and monitoring in Amazon SQS

Amazon Simple Queue Service is integrated with [AWS CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md"), a service
that provides a record of actions taken by a user, role, or an AWS service. CloudTrail captures
all
API calls for Amazon SQS as events. The calls captured include calls from the Amazon SQS console
and code calls to the Amazon SQS API operations. Using the information collected by CloudTrail, you can
determine the request that was made to Amazon SQS, the IP address from which the request was
made, when it was made, and additional details.

Every event or log entry contains information about who generated the request. The identity
information helps you determine the following:

- Whether the request was made with root user or user credentials.
- Whether the request was made on behalf of an IAM Identity Center user.
- Whether the request was made with temporary security credentials for a role or federated
  user.
- Whether the request was made by another AWS service.
  CloudTrail is active in your AWS account when you create the account and you automatically have
  access to the CloudTrail **Event history**. The CloudTrail **Event
  history** provides a viewable, searchable, downloadable, and immutable record of the
  past 90 days of recorded management events in an AWS Region. For more information, see [Working
  with CloudTrail Event history](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md") in the _AWS CloudTrail User Guide_. There are no CloudTrail
  charges for viewing the **Event history**.

For an ongoing record of events in your AWS account past 90 days, create a trail or a
[CloudTrail
Lake](../../../awscloudtrail/latest/userguide/cloudtrail-lake.md "../../../awscloudtrail/latest/userguide/cloudtrail-lake.md") event data store.

**Amazon CloudWatch Alarms**

Monitor a single metric over a time period you specify, and take one or more actions
based on the metric's value relative to a defined threshold over several periods. For
example, you can configure a CloudWatch alarm to send a notification to an Amazon SNS topic or
trigger an action to send a message to an Amazon SQS queue. CloudWatch alarms don't perform actions
simply because they are in a specific state; the state must change and remain in that
state for a defined number of periods.

For more information, see [Creating CloudWatch alarms for Amazon SQS
metrics](set-cloudwatch-alarms-for-metrics.md "set-cloudwatch-alarms-for-metrics.md") and [Creating alarms for dead-letter
queues using Amazon CloudWatch](dead-letter-queues-alarms-cloudwatch.md "dead-letter-queues-alarms-cloudwatch.md").

**Amazon CloudWatch Logs**

Monitor, store, and access log files related to Amazon SQS by configuring your applications
or Lambda functions that process messages to send logs to CloudWatch Logs. You can use these logs to
analyze message processing, debug issues, and monitor the performance of your Amazon SQS
workflows.

For more information, see [Logging Amazon Simple Queue Service API calls using
AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md").

**Amazon CloudWatch Events**

Use Amazon CloudWatch Events to detect changes or specific events in your AWS environment and route
them to an Amazon SQS queue. This allows you to capture event data, trigger workflows, or store
events for processing later.

For more information, see [Automating notifications from AWS services
to Amazon SQS using Amazon EventBridge](sqs-automating-using-eventbridge.md "sqs-automating-using-eventbridge.md") in this guide and [EventBridge is the
evolution of Amazon CloudWatch Events](../../../eventbridge/latest/userguide/eb-cwe-now-eb.md "../../../eventbridge/latest/userguide/eb-cwe-now-eb.md") in the _Amazon EventBridge User Guide_.

**AWS CloudTrail Logs**

CloudTrail captures a detailed record of actions performed on Amazon SQS by users, roles, or
AWS services. These logs let you track API calls, such as [`SendMessage`](../APIReference/API_SendMessage.md "../APIReference/API_SendMessage.md"), [`ReceiveMessage`](../APIReference/API_ReceiveMessage.md "../APIReference/API_ReceiveMessage.md"), or [`DeleteQueue`](../APIReference/API_DeleteQueue.md "../APIReference/API_DeleteQueue.md"), and provide key details such as who made the
request, when it occurred, and the originating IP address.

For more information, see [Logging Amazon Simple Queue Service API calls using
AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md").

**AWS Trusted Advisor**

Trusted Advisor uses best practices developed from serving AWS customers to help optimize
your Amazon SQS usage. It reviews your Amazon SQS queues and provides actionable recommendations to
enhance security, improve message processing reliability, and reduce costs. For example,
it may suggest enabling dead-letter queues or to improve your queue access policies to
ensure secure operations.

For more information, see [AWS Trusted Advisor](../../../awssupport/latest/user/getting-started.md#trusted-advisor "../../../awssupport/latest/user/getting-started.md#trusted-advisor") in the
_Support User Guide_.

**CloudTrail trails**

A _trail_ enables CloudTrail to deliver log files to an Amazon S3 bucket. All trails created using the AWS Management Console are multi-Region. You can create a single-Region or a multi-Region trail by using the AWS CLI. Creating a multi-Region trail is recommended because you capture activity in all AWS Regions in your account. If you create a single-Region trail, you can view only the events logged in the trail's AWS Region. For more information about trails, see [Creating a trail for your AWS account](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md") and [Creating a trail for an organization](../../../awscloudtrail/latest/userguide/creating-trail-organization.md "../../../awscloudtrail/latest/userguide/creating-trail-organization.md") in the _AWS CloudTrail User Guide_.

You can deliver one copy of your ongoing management events to your Amazon S3 bucket at no charge from CloudTrail by creating a trail, however, there are Amazon S3 storage charges. For more information about CloudTrail pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/"). For information about Amazon S3 pricing, see [Amazon S3 Pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").

**CloudTrail Lake event data stores**

_CloudTrail Lake_ lets you run SQL-based queries on your events. CloudTrail Lake converts existing events in row-based JSON format to [Apache ORC](https://orc.apache.org/ "https://orc.apache.org/") format. ORC is a columnar storage format that is optimized for fast retrieval of data. Events are aggregated into _event data stores_, which are immutable collections of events based on criteria that you select by applying [advanced event selectors](../../../awscloudtrail/latest/userguide/cloudtrail-lake-concepts.md#adv-event-selectors "../../../awscloudtrail/latest/userguide/cloudtrail-lake-concepts.md#adv-event-selectors"). The selectors that you apply to an event data store control which events persist and are available for you to query. For more information about CloudTrail Lake, see [Working with AWS CloudTrail Lake](../../../awscloudtrail/latest/userguide/cloudtrail-lake.md "../../../awscloudtrail/latest/userguide/cloudtrail-lake.md") in the _AWS CloudTrail User Guide_.

CloudTrail Lake event data stores and queries incur costs. When you create an event data store, you choose the [pricing option](../../../awscloudtrail/latest/userguide/cloudtrail-lake-manage-costs.md#cloudtrail-lake-manage-costs-pricing-option "../../../awscloudtrail/latest/userguide/cloudtrail-lake-manage-costs.md#cloudtrail-lake-manage-costs-pricing-option") you want to use for the event data store. The pricing option determines the cost for ingesting and storing events, and the default and maximum retention period for the event data store. For more information about CloudTrail pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/").
