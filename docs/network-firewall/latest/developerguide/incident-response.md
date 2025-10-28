# AWS logging and monitoring tools

This section provides an overview of the tools available for logging and monitoring in
AWS Network Firewall for standard AWS security purposes. For more information about logging
and monitoring in Network Firewall see [Logging and monitoring in AWS Network Firewall](logging-monitoring.md "logging-monitoring.md").

Monitoring is an important part of maintaining the reliability, availability, and
performance of Network Firewall and your AWS solutions. You should collect monitoring data from all
parts of your AWS solution so that you can more easily debug a multi-point failure if one
occurs. AWS provides several tools for monitoring your Network Firewall resources and responding to
potential incidents:

**Amazon CloudWatch Alarms**
Using CloudWatch alarms, you watch a single metric over a time period that you specify. If the
metric exceeds a given threshold, CloudWatch sends a notification to an Amazon SNS topic or
AWS Auto Scaling policy. For more information, see [AWS Network Firewall metrics in Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").

**AWS CloudTrail Logs**
CloudTrail provides a record of actions taken by a user, role, or an AWS service in Network Firewall. Using the information collected by CloudTrail, you can determine the request that was made to Network Firewall, the IP address from which the request was made, who made the request, when it was made, and additional details. For more information, see [Logging calls to the AWS Network Firewall API with
AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md").

**AWS Trusted Advisor**
Trusted Advisor draws upon best practices learned from serving hundreds of thousands of AWS customers. Trusted Advisor inspects your AWS environment and then makes recommendations when opportunities exist to save money, improve system availability and performance, or help close security gaps. All AWS customers have access to five Trusted Advisor checks. Customers with a Business or Enterprise support plan can view all Trusted Advisor checks. For more information, see [AWS Trusted Advisor](../../../awssupport/latest/user/getting-started.md#trusted-advisor "../../../awssupport/latest/user/getting-started.md#trusted-advisor").
