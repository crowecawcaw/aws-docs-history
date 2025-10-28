# AWS Service Integrations with AWS Config

AWS Config supports integrations with several other AWS services. This list is non-exhaustive.

## AWS Organizations

You can use AWS Organizations to define the accounts
to use for AWS Config’s multi-account, multi-Region data aggregation capability.
AWS Organizations is an account management service that helps you consolidate multiple
AWS accounts into an organization that you create and centrally manage.
By providing your AWS Organizations details, you can monitor the compliance status across your organization.
For more information, [AWS Config and AWS Organizations](../../../organizations/latest/userguide/services-that-can-integrate-config.md "../../../organizations/latest/userguide/services-that-can-integrate-config.md")
in the _AWS Organizations User Guide_.

## AWS Control Tower

AWS Control Tower enables AWS Config on all enrolled accounts,
so that it can monitor compliance through detective controls, record resource changes, and deliver resource change logs to the log archive account.
For more information, see [Monitor resource changes with AWS Config](../../../controltower/latest/userguide/monitoring-with-config.md "../../../controltower/latest/userguide/monitoring-with-config.md")
in the _AWS Control Tower User Guide_.

## AWS CloudTrail

AWS Config integrates with AWS CloudTrail to correlate configuration changes to particular events in your account.
You can use the CloudTrail logs to obtain the details of the event that invoked the change, including who made the request,
at what time, and from which IP address. You can navigate to the AWS Config timeline from the CloudTrail console
to view the configuration changes related to your AWS API activities.

For more information, see [Logging AWS Config API Calls with AWS CloudTrail](log-api-calls.md "log-api-calls.md") in the _AWS Config Developer Guide_
and [Create an event data store for AWS Config configuration items with the console](../../../awscloudtrail/latest/userguide/query-event-data-store-config.md "../../../awscloudtrail/latest/userguide/query-event-data-store-config.md") in the _AWS CloudTrail User Guide_.

## AWS Security Hub

AWS Security Hub centralizes security checks from other AWS services,
including AWS Config rules. Security Hub enables and controls
AWS Config rules to verify your resource configurations are aligned to best practices.
Enable AWS Config on all accounts in all
Regions where Security Hub is to run security checks on your environment’s resources.
For more information,
see [AWS services that send findings to Security Hub](../../../securityhub/latest/userguide/securityhub-internal-providers.md#integrations-internal-send "../../../securityhub/latest/userguide/securityhub-internal-providers.md#integrations-internal-send") in the _AWS Security Hub User Guide_.

###### Some Security Hub-related rules are periodic and do not depend on configuration items

Some Security Hub-related rules are periodic. These rule can run without the configuration recorder being enabled and do not depend on
configuration items (CI).

This means that if you view the rule page, there is no listed CI or supported resource. If you select the resource ID, you will see the following error:
`The provided resource ID and resource type cannot be found`. This is expected behavior.

## AWS Trusted Advisor

AWS Config managed rules power a set of Trusted Advisor checks across all categories. When you enable certain managed rules, the corresponding Trusted Advisor checks are automatically enabled.
To see which Trusted Advisor checks are powered by specific AWS Config managed rules, see [AWS Trusted Advisor check reference](../../../awssupport/latest/user/trusted-advisor-check-reference.md "../../../awssupport/latest/user/trusted-advisor-check-reference.md") in the _AWS Support User Guide_.

The AWS Config powered checks are available to customers with [AWS Business Support](https://aws.amazon.com/premiumsupport/plans/business/ "https://aws.amazon.com/premiumsupport/plans/business/"), [AWS Enterprise On-Ramp](https://aws.amazon.com/premiumsupport/plans/enterprise-onramp/ "https://aws.amazon.com/premiumsupport/plans/enterprise-onramp/"), and [AWS Enterprise Support](https://aws.amazon.com/premiumsupport/plans/enterprise/ "https://aws.amazon.com/premiumsupport/plans/enterprise/") plans. If you enable AWS Config and you have one of these AWS Support plans, then you automatically see recommendations powered by corresponding deployed AWS Config managed rules.

###### Refresh requests are not allowed and resources cannot be excluded

Results for these checks are automatically refreshed based on change-triggered updates to AWS Config managed rules. Refresh requests are not allowed. Currently, you can’t exclude resources from these checks.

For more information,
see [View Trusted Advisor checks powered by AWS Config](../../../systems-manager/latest/userguide/integrations-aws.md#integrations-aws-management-governance "../../../systems-manager/latest/userguide/integrations-aws.md#integrations-aws-management-governance") in the _AWS Support User Guide_.

## AWS Audit Manager

You can use Audit Manager to capture AWS Config evaluations as evidence for audits. When you create
or edit a custom control, you can specify one or more AWS Config rules as a data source
mapping for evidence collection. AWS Config performs compliance checks based on these rules,
and Audit Manager reports the results as compliance check evidence.
For more information,
see [AWS Config Rules supported by AWS Audit Manager](../../../audit-manager/latest/userguide/control-data-sources-config.md "../../../audit-manager/latest/userguide/control-data-sources-config.md") in the _AWS Audit Manager User Guide_.

## AWS Systems Manager

AWS Config integrates with Systems Manager to record configuration
changes to software on your Amazon EC2 instances and servers in your on-premises environment.
With this integration, you can gain visibility into operating system (OS) configurations,
system-level updates, installed applications, network configuration, and more.
AWS Config also provides a history of OS and system-level configuration
changes alongside infrastructure configuration changes recorded for Amazon EC2 instances.
You can navigate to the AWS Config timeline from the Systems Manager
console to view the configuration changes of your managed Amazon EC2 instances.
You can use AWS Config to view Systems Manager inventory history and
track changes for all your managed instances.

For more information,
see [Integration with AWS services | Management and Governance](../../../systems-manager/latest/userguide/integrations-aws.md#integrations-aws-management-governance "../../../systems-manager/latest/userguide/integrations-aws.md#integrations-aws-management-governance"),
[AWS Config configuration recorder](../../../systems-manager/latest/userguide/quick-setup-config.md "../../../systems-manager/latest/userguide/quick-setup-config.md"),
and [AWS Config conformance pack deployment](../../../systems-manager/latest/userguide/quick-setup-cpack.md "../../../systems-manager/latest/userguide/quick-setup-cpack.md")
in the _AWS Systems Manager User Guide_.

## AWS Firewall Manager

To use Firewall Manager, you must enable AWS Config for each of your AWS Organizations member accounts.
When new applications are created, Firewall Manager is the single service to build firewall rules,
create security policies, and enforce them consistently. For more information, see
[Enable AWS Config](../../../waf/latest/developerguide/enable-config.md "../../../waf/latest/developerguide/enable-config.md")
in the _AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide_.

###### Note

Firewall Manager depends on continuous recording to monitor your resources. If you are using Firewall Manager,
it is recommended that you set the recording frequency to Continuous. For more information on continuous recording and daily recording, see
[Recording Frequency](select-resources.md#select-resources-recording-frequency "select-resources.md#select-resources-recording-frequency").

## Amazon EC2 Dedicated Hosts

AWS Config integrates with Amazon EC2 Dedicated Hosts to assess license compliance.
AWS Config records when instances are launched, stopped, or shut down on a Dedicated Host,
and pairs this information with host and instance level information relevant to software licensing,
such as Host ID, Amazon Machine Image (AMI) IDs, number of sockets, and physical cores.
This helps you use AWS Config as a data source for your license reporting.
You can navigate to the AWS Config timeline from the Amazon EC2 Dedicated Hosts console
to view the configuration changes of your Amazon EC2 Dedicated Hosts.

For more information, see
[Track configuration changes](../../../AWSEC2/latest/UserGuide/dedicated-hosts-aws-config.md "../../../AWSEC2/latest/UserGuide/dedicated-hosts-aws-config.md")
in the _Amazon Elastic Compute Cloud User Guide for Linux Instances_
or [Track configuration changes](../../../AWSEC2/latest/WindowsGuide/dedicated-hosts-aws-config.md "../../../AWSEC2/latest/WindowsGuide/dedicated-hosts-aws-config.md")
in the _Amazon Elastic Compute Cloud User Guide for Windows Instances_.

## Application Load Balancers

AWS Config integrates with the Elastic Load Balancing (ELB)
service to record configuration changes to Application Load Balancers.
AWS Config also includes relationships with associated Amazon EC2 security groups, VPCs, and subnets.
You can use this information for security analysis and troubleshooting.
For example, you can check which security groups are associated with your Application Load Balancer at any point in time.
You can navigate to the AWS Config timeline from the ELB console to view the configuration changes of your Application Load Balancers.

## AWS CodeBuild

AWS Configprovides an inventory of your AWS resources and a history of configuration changes to these resources.
AWS Config supports AWS CodeBuild; as an AWS resource, which means the service can track your CodeBuild projects. For more information, see
[Use AWS Config with CodeBuild sample](../../../codebuild/latest/userguide/how-to-integrate-config.md "../../../codebuild/latest/userguide/how-to-integrate-config.md")
in the _AWS CodeBuild User Guide_.

## AWS X-Ray

AWS X-Ray integrates with AWS Config to record configuration changes made to your X-Ray encryption resources.
You can use AWS Config to inventory X-Ray encryption resources, audit the X-Ray configuration history,
and send notifications based on resource changes. For more information, see
[Tracking X-Ray encryption configuration changes with AWS Config](../../../xray/latest/devguide/xray-api-config.md "../../../xray/latest/devguide/xray-api-config.md")
in the _AWS X-Ray Developer Guide_.

## AWS Service Management Connector

The AWS Service Management Connector for ServiceNow can synchronize AWS Config data from multiple accounts and Regions using an Aggregator. For more information, see
[Integrating AWS Config in ServiceNow](../../../smc/latest/ag/sn-configue-config.md "../../../smc/latest/ag/sn-configue-config.md")
in the _AWS Service Management Connector Administrator Guide_.

## Amazon API Gateway

You can use AWS Config to record configuration changes made to your API Gateway API resources and send notifications based on resource changes.
Maintaining a configuration change history for API Gateway resources is useful for operational troubleshooting, audit, and compliance use cases.
For more information, see
[Monitoring API Gateway API configuration with AWS Config](../../../apigateway/latest/developerguide/apigateway-config.md "../../../apigateway/latest/developerguide/apigateway-config.md")
in the _API Gateway Developer Guide_.
