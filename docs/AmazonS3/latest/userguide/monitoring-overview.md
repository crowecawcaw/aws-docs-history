# Logging and monitoring in Amazon S3

Monitoring is an important part of maintaining the reliability, availability, and
performance of Amazon S3 and your AWS solutions. We recommend collecting monitoring
data from all of the parts of your AWS solution so that you can more easily debug a
multipoint failure if one occurs. Before you start monitoring Amazon S3, create a
monitoring plan that includes answers to the following questions:

- What are your monitoring goals?
- What resources will you monitor?
- How often will you monitor these resources?
- What monitoring tools will you use?
- Who will perform the monitoring tasks?
- Who should be notified when something goes wrong?
  For more information about logging and monitoring in Amazon S3, see the following
  topics.

###### Note

For more information about using the Amazon S3 Express One Zone storage class with directory buckets, see [S3 Express One Zone](directory-bucket-high-performance.md#s3-express-one-zone "directory-bucket-high-performance.md#s3-express-one-zone") and [Working with directory buckets](directory-buckets-overview.md "directory-buckets-overview.md").

Monitoring is an important part of maintaining the reliability, availability, and
performance of Amazon S3 and your AWS solutions. You should collect monitoring data from all of
the parts of your AWS solution so that you can more easily debug a multi-point failure if
one occurs. AWS provides several tools for monitoring your Amazon S3 resources and responding
to potential incidents.

**Amazon CloudWatch Alarms**

Using Amazon CloudWatch alarms, you watch a single metric over a time period that you
specify. If the metric exceeds a given threshold, a notification is sent to an
Amazon SNS topic or AWS Auto Scaling policy. CloudWatch alarms do not invoke actions because they
are in a particular state. Rather the state must have changed and been
maintained for a specified number of periods. For more information, see [Monitoring metrics with Amazon CloudWatch](cloudwatch-monitoring.md "cloudwatch-monitoring.md").

**AWS CloudTrail Logs**

CloudTrail provides a record of actions taken by a user, role, or an AWS service
in Amazon S3. Using the information collected by CloudTrail, you can determine the request
that was made to Amazon S3, the IP address from which the request was made, who made
the request, when it was made, and additional details. For more information, see
[Logging Amazon S3 API calls using AWS CloudTrail](cloudtrail-logging.md "cloudtrail-logging.md").

**Amazon GuardDuty**

[Amazon GuardDuty](../../../guardduty/latest/ug/what-is-guardduty.md "../../../guardduty/latest/ug/what-is-guardduty.md") is a threat detection service that continuously monitors
your accounts, containers, workloads, and the data within your AWS environment
to identify potential threats or security risks to your S3 buckets. GuardDuty also
provides rich context about the threats that it detects. GuardDuty monitors AWS CloudTrail
management logs for threats and surfaces security relevant information. For
example, GuardDuty will include factors of an API request, such as the user that
made the request, the location the request was made from, and the specific API
requested, that could be unusual in your environment. [GuardDuty S3
Protection](../../../guardduty/latest/ug/s3-protection.md "../../../guardduty/latest/ug/s3-protection.md") monitors the S3 data events collected by CloudTrail and
identifies potentially anomalous and malicious behavior in all the S3 buckets in
your environment.

**Amazon S3 Access Logs**

Server access logs provide detailed records about requests that are made to a
bucket. Server access logs are useful for many applications. For example, access
log information can be useful in security and access audits. For more
information, see [Logging requests with server access logging](ServerLogs.md "ServerLogs.md").

**AWS Trusted Advisor**

Trusted Advisor draws upon best practices learned from serving hundreds of thousands
of AWS customers. Trusted Advisor inspects your AWS environment and then makes
recommendations when opportunities exist to save money, improve system
availability and performance, or help close security gaps. All AWS customers
have access to five Trusted Advisor checks. Customers with a Business or Enterprise
support plan can view all Trusted Advisor checks.

Trusted Advisor has the following Amazon S3-related checks:

- Logging configuration of Amazon S3 buckets.
- Security checks for Amazon S3 buckets that have open access
  permissions.
- Fault tolerance checks for Amazon S3 buckets that don't have versioning
  enabled, or have versioning suspended.

For more information, see
[AWS Trusted Advisor](../../../awssupport/latest/user/getting-started.md#trusted-advisor "../../../awssupport/latest/user/getting-started.md#trusted-advisor") in the _Support User Guide_.

**Amazon S3 Storage Lens**

Amazon S3 Storage Lens is a cloud-storage analytics feature that you can use to gain
organization-wide visibility into object-storage usage and activity. You can use
S3 Storage Lens metrics to generate summary insights, such as finding out how
much storage you have across your entire organization or which are the
fastest-growing buckets and prefixes. You can also use S3 Storage Lens metrics
to identify cost-optimization opportunities, implement data-protection and
security best practices, and improve the performance of application
workloads.

S3 Storage Lens aggregates your metrics and displays the information in the
Account snapshot section on the Amazon S3 console **Buckets** page.
S3 Storage Lens also provides an interactive dashboard that you can use to visualize
insights and trends, flag outliers, and receive recommendations for optimizing
storage costs and applying data-protection best practices. Your dashboard has
drill-down options to generate and visualize insights at the organization,
account, AWS Region, storage class, bucket, prefix, or Storage Lens group
level. For more information, see [Understanding
Amazon S3 Storage Lens](storage_lens_basics_metrics_recommendations.md "storage_lens_basics_metrics_recommendations.md").

**Amazon S3 Inventory**

Amazon S3 Inventory generates a list of objects and metadata that you can use to query and manage
your objects. You can use this inventory report to generate granular data such
as object size, last modified date, encryption status and other fields. Those
reports are available daily or weekly to automatically give the latest list.

For example, you can
use Amazon S3 Inventory to audit and report on the replication and encryption status of your
objects for business, compliance, and regulatory needs. You can also use Amazon S3 Inventory to simplify
and speed up business workflows and big data jobs, which
provides a scheduled alternative to the Amazon S3 synchronous `List` API
operations. Amazon S3 Inventory doesn't use the `List` API operations to
audit your objects and does not affect the request rate of your bucket. For more
information, see [Cataloging and analyzing your data with S3 Inventory](storage-inventory.md "storage-inventory.md").

**Amazon S3 Event Notifications**

With the Amazon S3 Event Notifications feature, you receive notifications
when certain events happen in your S3 bucket. To enable notifications, add a
notification configuration that identifies the events that you want Amazon S3 to
publish. For more information, see [Amazon S3 Event Notifications](EventNotifications.md "EventNotifications.md").

**Amazon S3 and AWS X-Ray**

AWS X-Ray integrates with Amazon S3 to trace upstream requests to update your
application's S3 buckets. If a service traces requests by using the X-Ray SDK,
Amazon S3 can send the tracing headers to downstream event subscribers such as
Λ, Amazon SQS, and Amazon SNS. X-Ray enables trace messages for Amazon S3
event notifications. You can use the X-Ray trace map to view the connections
between Amazon S3 and other services that your application uses. For more
information, see [Amazon S3 and
X-Ray](../../../xray/latest/devguide/xray-services-s3.md "../../../xray/latest/devguide/xray-services-s3.md").

The following security best practices also address logging and monitoring:

- [Identify and audit all your Amazon S3 buckets](security-best-practices.md#audit "security-best-practices.md#audit")
- [Implement monitoring using Amazon Web Services monitoring tools](security-best-practices.md#tools "security-best-practices.md#tools")
- [Enable AWS Config](security-best-practices.md#config "security-best-practices.md#config")
- [Enable Amazon S3 server access logging](security-best-practices.md#serverlog "security-best-practices.md#serverlog")
- [Use CloudTrail](security-best-practices.md#objectlog "security-best-practices.md#objectlog")
- [Monitor Amazon Web Services security advisories](security-best-practices.md#advisories "security-best-practices.md#advisories")

###### Topics

- [Monitoring tools](monitoring-automated-manual.md "monitoring-automated-manual.md")
- [Logging options for Amazon S3](logging-with-S3.md "logging-with-S3.md")
- [Logging Amazon S3 API calls using AWS CloudTrail](cloudtrail-logging.md "cloudtrail-logging.md")
- [Logging requests with server access logging](ServerLogs.md "ServerLogs.md")
- [Monitoring metrics with Amazon CloudWatch](cloudwatch-monitoring.md "cloudwatch-monitoring.md")
- [Amazon S3 Event Notifications](EventNotifications.md "EventNotifications.md")
- [Monitoring your storage activity and usage with
  Amazon S3 Storage Lens](storage_lens.md "storage_lens.md")
- [Cataloging and analyzing your data with S3 Inventory](storage-inventory.md "storage-inventory.md")
