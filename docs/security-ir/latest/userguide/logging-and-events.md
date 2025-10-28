# Logging and events

[**AWS CloudTrail**](https://aws.amazon.com/cloudtrail/ "https://aws.amazon.com/cloudtrail/") – AWS CloudTrail service
enabling governance, compliance, operational auditing, and risk auditing of AWS accounts. With CloudTrail,
you can log, continuously monitor, and retain account activity related to actions across AWS services. CloudTrail
provides event history of your AWS account activity, including actions taken through the AWS Management Console,
AWS SDKs, command line tools, and other AWS services. This event history simplifies security analysis,
resource change tracking, and troubleshooting. CloudTrail logs two different types of AWS API actions:

- **CloudTrail management events** (also known as control plane
  operations) show management operations that are performed on resources in your AWS
  account. This includes actions such as creating an Amazon S3 bucket and setting up
  logging.
- **CloudTrail data events** (also known as data plane
  operations) show the resource operations performed on or within a resource in your AWS
  account. These operations are often high-volume activities. This includes actions such as
  Amazon S3 object-level API activity (for example, `GetObject`, `DeleteObject`, and `PutObject`
  API operations) and Lambda function invocation activity.

[**AWS Config**](https://aws.amazon.com/config/ "https://aws.amazon.com/config/") – AWS Config is a
service enabling customers assess, audit, and evaluate the configurations of your AWS resources. AWS Config
continuously monitors and records your AWS resource configurations and enables you to automate the
evaluation of recorded configurations against desired configurations. With AWS Config, customers
can review changes in configurations and relationships between AWS resources, manually or
automatically, detailed resource configuration history, and determine overall compliance
against the configurations specified in customer’s guidelines. This enables simplification of
compliance auditing, security analysis, change management, and operational troubleshooting.

[**Amazon EventBridge**](https://aws.amazon.com/eventbridge/ "https://aws.amazon.com/eventbridge/") – Amazon EventBridge delivers a
near real-time stream of system events that describe changes in AWS resources, or when
API calls are published by AWS CloudTrail. Using simple rules that you can quickly set up, you can
match events and route them to one or more target functions or streams. EventBridge becomes aware of operational
changes as they occur. EventBridge can respond to these operational changes and take corrective action as
necessary, by sending messages to respond to the environment, activating functions, making changes,
and capturing state information. Some security services, such as Amazon GuardDuty, produce their output in the form of EventBridge events.
Many security services also provide an option to send their outputs to Amazon S3.

**Amazon S3 access logs** – If sensitive information is stored in an Amazon S3
bucket, customers can enable Amazon S3 access logs to record every upload, download, and modification
to that data. This log is separate from, and in addition to, the CloudTrail logs that record
changes to the bucket itself (such as changing access policies and lifecycle policies).
It’s worth noting that access log records are delivered on a best effort basis. Most requests
for a bucket that is properly configured for logging result in a delivered log record.
The completeness and timeliness of server logging is not guaranteed.

[**Amazon CloudWatch Logs**](../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md "../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md") – Customers can use Amazon CloudWatch Logs to monitor, store, and
access log files originating from operating systems, applications, and other sources running in Amazon EC2 instances with a CloudWatch Logs
agent. CloudWatch Logs can be a destination for AWS CloudTrail, Route 53 DNS Queries, VPC Flow Logs, Lambda functions, and others.
Customers can then retrieve the associated log data from CloudWatch Logs.

[**Amazon VPC Flow Logs**](../../../vpc/latest/userguide/flow-logs.md "../../../vpc/latest/userguide/flow-logs.md") – VPC Flow Logs enables customers to capture information about
IP traffic going to and from network interfaces in VPCs. After enabling flow logs, they can be streamed to
Amazon CloudWatch Logs and Amazon S3. VPC Flow Logs helps customers with a number of tasks such as troubleshooting why
specific traffic is not reaching an instance, diagnosing overly restrictive security group rules,
and using it as a security tool to monitor the traffic to EC2 instances. Use the most current
version of VPC flow logging to get the most robust fields.

[**AWS WAF Logs**](https://aws.amazon.com/waf/ "https://aws.amazon.com/waf/") – AWS WAF supports full logging of all web requests inspected by the
service. Customers can store these in Amazon S3 to fulfill compliance and auditing requirements,
as well as debugging and forensics. These logs help customers determine the root cause of initiated
rules and blocked web requests. Logs can be integrated with third-party SIEM and log analysis tools.

[**Route 53 Resolver query logs**](../../../Route53/latest/DeveloperGuide/resolver-query-logs.md "../../../Route53/latest/DeveloperGuide/resolver-query-logs.md") – Route 53 Resolver query logs will let you log all
DNS queries made by resources within Amazon Virtual Private Cloud (Amazon VPC). Whether it’s an Amazon EC2 instance, an AWS Lambda function,
or a container, if it lives in your Amazon VPC and makes a DNS query, then this feature will log it;
you are then able to explore and better understand how your applications are operating.

**Other AWS logs** – AWS continuously releases service features and
capabilities for customers with new logging and monitoring capabilities. For information about
features available for each AWS service, refer to our public documentation.
