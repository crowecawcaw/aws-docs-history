

# AWS Service Integrations with AWS Config
<a name="service-integrations"></a>

AWS Config supports integrations with several other AWS services. This list is non-exhaustive.

## AWS Organizations
<a name="service-integrations-organizations"></a>

You can use AWS Organizations to define the accounts to use for AWS Config’s multi-account, multi-Region data aggregation capability. AWS Organizations is an account management service that helps you consolidate multiple AWS accounts into an organization that you create and centrally manage. By providing your AWS Organizations details, you can monitor the compliance status across your organization. For more information, [AWS Config and AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-config.html) in the *AWS Organizations User Guide*. 

## AWS Control Tower
<a name="service-integrations-controltower"></a>

AWS Control Tower enables AWS Config on all enrolled accounts, so that it can monitor compliance through detective controls, record resource changes, and deliver resource change logs to the log archive account. For more information, see [Monitor resource changes with AWS Config](https://docs.aws.amazon.com/controltower/latest/userguide/monitoring-with-config.html) in the *AWS Control Tower User Guide*. 

## AWS CloudTrail
<a name="service-integrations-cloudtrail"></a>

AWS Config integrates with AWS CloudTrail to correlate configuration changes to particular events in your account. You can use the CloudTrail logs to obtain the details of the event that invoked the change, including who made the request, at what time, and from which IP address. You can navigate to the AWS Config timeline from the CloudTrail console to view the configuration changes related to your AWS API activities.

 For more information, see [Logging AWS Config API Calls with AWS CloudTrail](https://docs.aws.amazon.com/config/latest/developerguide/log-api-calls.html) in the *AWS Config Developer Guide* and [Create an event data store for AWS Config configuration items with the console](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-event-data-store-config.html) in the *AWS CloudTrail User Guide*. 

## AWS Security Hub CSPM
<a name="service-integrations-securityhub"></a>

AWS Security Hub CSPM centralizes security checks from other AWS services, including AWS Config rules. Security Hub enables and controls AWS Config rules to verify your resource configurations are aligned to best practices. Enable AWS Config on all accounts in all Regions where Security Hub CSPM is to run security checks on your environment’s resources. For more information, see [AWS services that send findings to Security Hub](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-internal-providers.html#integrations-internal-send) in the *AWS Security Hub CSPM User Guide*. 

**Some Security Hub CSPM-related rules are periodic and do not depend on configuration items**  
Some Security Hub CSPM-related rules are periodic. These rule can run without the configuration recorder being enabled and do not depend on configuration items (CI).  
This means that if you view the rule page, there is no listed CI or supported resource. If you select the resource ID, you will see the following error: `The provided resource ID and resource type cannot be found`. This is expected behavior.

## AWS Trusted Advisor
<a name="service-integrations-trustedadvisor"></a>

AWS Config managed rules power a set of Trusted Advisor checks across all categories. When you enable certain managed rules, the corresponding Trusted Advisor checks are automatically enabled. To see which Trusted Advisor checks are powered by specific AWS Config managed rules, see [AWS Trusted Advisor check reference](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor-check-reference.html) in the *AWS Support User Guide*.

The AWS Config powered checks are available to customers with [AWS Business Support](https://aws.amazon.com/premiumsupport/plans/business/), [AWS Enterprise On-Ramp](https://aws.amazon.com/premiumsupport/plans/enterprise-onramp/), and [AWS Enterprise Support](https://aws.amazon.com/premiumsupport/plans/enterprise/) plans. If you enable AWS Config and you have one of these AWS Support plans, then you automatically see recommendations powered by corresponding deployed AWS Config managed rules. 

**Refresh requests are not allowed and resources cannot be excluded**  
Results for these checks are automatically refreshed based on change-triggered updates to AWS Config managed rules. Refresh requests are not allowed. Currently, you can’t exclude resources from these checks.

For more information, see [View Trusted Advisor checks powered by AWS Config](https://docs.aws.amazon.com/systems-manager/latest/userguide/integrations-aws.html#integrations-aws-management-governance) in the *AWS Support User Guide*. 

## AWS Audit Manager
<a name="service-integrations-auditmanager"></a>

You can use Audit Manager to capture AWS Config evaluations as evidence for audits. When you create or edit a custom control, you can specify one or more AWS Config rules as a data source mapping for evidence collection. AWS Config performs compliance checks based on these rules, and Audit Manager reports the results as compliance check evidence. For more information, see [AWS Config Rules supported by AWS Audit Manager](https://docs.aws.amazon.com/audit-manager/latest/userguide/control-data-sources-config.html) in the *AWS Audit Manager User Guide*. 

## AWS Systems Manager
<a name="service-integrations-systemsmanager"></a>

AWS Config integrates with Systems Manager to record configuration changes to software on your Amazon EC2 instances and servers in your on-premises environment. With this integration, you can gain visibility into operating system (OS) configurations, system-level updates, installed applications, network configuration, and more. AWS Config also provides a history of OS and system-level configuration changes alongside infrastructure configuration changes recorded for Amazon EC2 instances. You can navigate to the AWS Config timeline from the Systems Manager console to view the configuration changes of your managed Amazon EC2 instances. You can use AWS Config to view Systems Manager inventory history and track changes for all your managed instances.

For more information, see [Integration with AWS services \| Management and Governance](https://docs.aws.amazon.com/systems-manager/latest/userguide/integrations-aws.html#integrations-aws-management-governance), [AWS Config configuration recorder](https://docs.aws.amazon.com/systems-manager/latest/userguide/quick-setup-config.html), and [AWS Config conformance pack deployment](https://docs.aws.amazon.com/systems-manager/latest/userguide/quick-setup-cpack.html) in the *AWS Systems Manager User Guide*. 

## AWS Firewall Manager
<a name="service-integrations-firewallmanager"></a>

To use Firewall Manager, you must enable AWS Config for each of your AWS Organizations member accounts. When new applications are created, Firewall Manager is the single service to build firewall rules, create security policies, and enforce them consistently. For more information, see [Enable AWS Config](https://docs.aws.amazon.com/waf/latest/developerguide/enable-config.html) in the *AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*. 

**Note**  
Firewall Manager depends on continuous recording to monitor your resources. If you are using Firewall Manager, it is recommended that you set the recording frequency to Continuous. For more information on continuous recording and daily recording, see [Recording Frequency](https://docs.aws.amazon.com/config/latest/developerguide/select-resources.html#select-resources-recording-frequency).

## Amazon EC2 Dedicated Hosts
<a name="service-integrations-ec2dedicatedhost"></a>

AWS Config integrates with Amazon EC2 Dedicated Hosts to assess license compliance. AWS Config records when instances are launched, stopped, or shut down on a Dedicated Host, and pairs this information with host and instance level information relevant to software licensing, such as Host ID, Amazon Machine Image (AMI) IDs, number of sockets, and physical cores. This helps you use AWS Config as a data source for your license reporting. You can navigate to the AWS Config timeline from the Amazon EC2 Dedicated Hosts console to view the configuration changes of your Amazon EC2 Dedicated Hosts.

For more information, see [Track configuration changes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-hosts-aws-config.html) in the *Amazon Elastic Compute Cloud User Guide for Linux Instances* or [Track configuration changes](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/dedicated-hosts-aws-config.html) in the *Amazon Elastic Compute Cloud User Guide for Windows Instances*. 

## Application Load Balancers
<a name="service-integrations-applicationloadbalancers"></a>

 AWS Config integrates with the Elastic Load Balancing (ELB) service to record configuration changes to Application Load Balancers. AWS Config also includes relationships with associated Amazon EC2 security groups, VPCs, and subnets. You can use this information for security analysis and troubleshooting. For example, you can check which security groups are associated with your Application Load Balancer at any point in time. You can navigate to the AWS Config timeline from the ELB console to view the configuration changes of your Application Load Balancers. 

## AWS CodeBuild
<a name="service-integrations-codebuild"></a>

AWS Configprovides an inventory of your AWS resources and a history of configuration changes to these resources. AWS Config supports AWS CodeBuild; as an AWS resource, which means the service can track your CodeBuild projects. For more information, see [Use AWS Config with CodeBuild sample](https://docs.aws.amazon.com/codebuild/latest/userguide/how-to-integrate-config.html) in the *AWS CodeBuild User Guide*.

## AWS X-Ray
<a name="service-integrations-xray"></a>

AWS X-Ray integrates with AWS Config to record configuration changes made to your X-Ray encryption resources. You can use AWS Config to inventory X-Ray encryption resources, audit the X-Ray configuration history, and send notifications based on resource changes. For more information, see [Tracking X-Ray encryption configuration changes with AWS Config](https://docs.aws.amazon.com/xray/latest/devguide/xray-api-config.html) in the *AWS X-Ray Developer Guide*.

## AWS Service Management Connector
<a name="service-integrations-servicemanagementconnector"></a>

The AWS Service Management Connector for ServiceNow can synchronize AWS Config data from multiple accounts and Regions using an Aggregator. For more information, see [Integrating AWS Config in ServiceNow](https://docs.aws.amazon.com/smc/latest/ag/sn-configue-config.html) in the *AWS Service Management Connector Administrator Guide*.

## Amazon API Gateway
<a name="service-integrations-apigateway"></a>

You can use AWS Config to record configuration changes made to your API Gateway API resources and send notifications based on resource changes. Maintaining a configuration change history for API Gateway resources is useful for operational troubleshooting, audit, and compliance use cases. For more information, see [Monitoring API Gateway API configuration with AWS Config](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-config.html) in the *API Gateway Developer Guide*.