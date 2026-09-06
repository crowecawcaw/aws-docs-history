

AWS Chatbot is now Amazon Q Developer. [Learn more](service-rename.md)

# Monitoring AWS services using Amazon Q Developer in chat applications
<a name="related-services"></a>

You can use Amazon Q Developer in chat applications to monitor and receive notifications about other AWS services. Amazon Q Developer in chat applications works with a number of AWS services, including [Amazon CloudWatch](https://console.aws.amazon.com/cloudwatch/), [AWS Security Hub CSPM](https://console.aws.amazon.com/securityhub/), and [Amazon GuardDuty](https://console.aws.amazon.com/guardduty/). All services that work with Amazon Q Developer in chat applications use [Amazon SNS topics](https://docs.aws.amazon.com/sns/latest/dg/) as targets to send event and alarm notifications. You may already have established Amazon SNS topics that send notifications to DevOps and development personnel as emails. Because Amazon Q Developer in chat applications redirects those Amazon SNS topics' notifications to chat rooms, you can map those Amazon SNS topics to an Amazon Chime webhook, Microsoft Teams channel, or Slack channel in the Amazon Q Developer in chat applications console.

**Note**  
 Not all service messages sent via Amazon SNS are supported. For more information about supported services, see [Supported services for Amazon Q Developer in chat applications](chatbot-services.md). 

When you create a new Amazon SNS topic, your services will require additional configuration.

If you want to customize the message content of default service notifications or customize messages for your application events, you can use custom notifications. For more information, see [Custom notifications using Amazon Q Developer in chat applications](custom-notifs.md).

**Topics**
+ [AWS Billing and Cost Management](#aws-billing)
+ [AWS CloudFormation](#cloud-formation)
+ [Notifications for AWS developer tools](#codeserviceevents)
+ [Amazon CloudWatch alarms](#cloudwatch)
+ [Amazon EventBridge](#eventbridge)
+ [Tutorial: Creating an Amazon EventBridge rule that sends notifications to Amazon Q Developer in chat applications](create-eventbridge-rule.md)
+ [[AWS Config](https://console.aws.amazon.com/config/)](#aws-config)
+ [[Amazon GuardDuty](https://console.aws.amazon.com/guardduty/)](#aws-guardduty)
+ [[AWS Health](https://phd.aws.amazon.com/phd/home#/)](#aws-health)
+ [[AWS Security Hub CSPM](https://console.aws.amazon.com/securityhub/)](#security-hub)
+ [[AWS Systems Manager](https://console.aws.amazon.com/systems-manager/)](#system-manager)
+ [AWS Systems Manager Runbooks](#runbooks)
+ [AWS Systems Manager Incident Manager](#incidentManager)

You can set up the following AWS services to forward notifications to Amazon Chime, Microsoft Teams, or Slack chat rooms.

## AWS Billing and Cost Management
<a name="aws-billing"></a>

AWS Billing and Cost Management helps AWS account holders plan service usage, service costs, and instance reservations. You do this using several specific types of budgets, which track your unblended costs, subscriptions, refunds, and Reserved Instances. The service sends AWS Budget Alerts to an Amazon SNS topic. You then map the Amazon SNS topic in Amazon Q Developer in chat applications to send those notifications to your chat rooms.

For information about setting up Amazon SNS topics for AWS budgets, see [Creating an Amazon SNS Topic for Budget Notifications](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/budgets-sns-policy.html) in the* AWS Billing and Cost Management User Guide*.

## AWS CloudFormation
<a name="cloud-formation"></a>

AWS CloudFormation is an infrastructure management service that helps you model and set up Amazon Web Services resources so you can spend less time managing those resources and more time focusing on the applications that you run in AWS. You create a template that describes all of the AWS resources (for example, Amazon EC2 instances or Amazon RDS DB instances) that you want, and AWS CloudFormation provisions and configures those resources for you. 

Amazon Q Developer in chat applications supports CloudFormation notifications through Amazon SNS topics. You enable support for SNS topics that are enabled for use with Amazon Q Developer in chat applications by selecting them in each CloudFormation stack configuration. For more information, see [Setting AWS CloudFormation Stack Options](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-add-tags.html) in the *AWS CloudFormation User Guide*. 

## Notifications for AWS developer tools
<a name="codeserviceevents"></a>

AWS provides a suite of cloud-based developer tools for creating, managing, and working with software development projects. The AWS development tools suite includes AWS services such as CloudFormation stacks, AWS CodeBuild, AWS CodeCommit, AWS CodeDeploy, AWS CodePipeline, and more. You can redirect Amazon SNS topic subscriptions for these services to Amazon Q Developer in chat applications. For example, if you want notifications about events in an AWS CodeCommit repository or in a pipeline in AWS CodePipeline to appear in a Microsoft Teams or Slack channel for your development teams, you can set up notifications for those resources in the Developer Tools console, and then integrate the SNS topic used for those notifications with Amazon Q Developer in chat applications. For more information, see [Configure Integration Between Notifications and Amazon Q Developer in chat applications](https://docs.aws.amazon.com/codestar-notifications/latest/userguide/notifications-chatbot.html) in the *Developer Tools Console User Guide*.

## Amazon CloudWatch alarms
<a name="cloudwatch"></a>

To monitor performance and operating metrics for AWS services, and send notifications when thresholds are breached, you can create alarms in Amazon CloudWatch. CloudWatch sends an Amazon SNS notification or performs an action when the alarm changes state.

CloudWatch also features composite alarms. Composite alarms allow you to combine multiple alarms to reduce alarm noise and focus on critical operational issues. You can easily combine multiple alarms together into alarm hierarchies that only trigger once, when multiple alarms fire at the same time. Composite alarms are currently supported by Amazon Q Developer in chat applications.

**Note**  
Parent composite alarms can have multiple triggering children however, the Amazon Q Developer in chat applications notification will only display a maximum of 3 of the total triggering metric children's alarm states. For example, if you have 10 total children alarms and 5 are currently triggered, the Amazon Q Developer in chat applications notification will display 3 of those 5.

Any metric, for any AWS service, that CloudWatch alarm actions can report can also be shared by an SNS topic to chat rooms through Amazon Q Developer in chat applications. This includes alarms for services such as Amazon Elastic Compute Cloud (Amazon EC2). 

For information about setting up SNS topics to forward CloudWatch alarms, see [Set Up Amazon SNS Notifications](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/US_SetupSNS.html) in the *Amazon CloudWatch User Guide*.

Because CloudWatch alarms use SNS topics to forward alarm notifications, you need to map only the associated Amazon SNS topic to your Slack channel or Amazon Chime webhook configuration in Amazon Q Developer in chat applications.

Amazon Q Developer in chat applications also supports several AWS services through CloudWatch Events. For more information, see the following section.

## Amazon EventBridge
<a name="eventbridge"></a>

 Amazon Q Developer in chat applications supports multiple AWS services through [Amazon EventBridge rules](https://docs.aws.amazon.com/eventbridge/latest/userguide/create-eventbridge-rule.html). EventBridge uses rules to help manage AWS service events and how you respond to them. You can use these rules to associate an Amazon SNS topic (or other actions) with an event type from any AWS service.

You map the Amazon SNS topic to the EventBridge rule, and then map it to a chat channel or Amazon Chime webhook in the Amazon Q Developer in chat applications console. When a service event matches the rule, the rule's target Amazon SNS topic sends an event to the Amazon Q Developer in chat applications for processing. The Amazon Q Developer in chat applications then sends a notification to the chat room. You can also customize the content of your notifications by using the custom notifications event schema and EventBridge [InputTransformers](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-transform-target-input.html). For more information, see [Custom notifications using Amazon Q Developer in chat applications](custom-notifs.md) and [Creating an EventBridge Rule that sends notifications to Amazon Q Developer in chat applications](create-eventbridge-rule.md).

Amazon Q Developer in chat applications can process most AWS service events handled by EventBridge. This includes AWS Config, Amazon GuardDuty, AWS Health, AWS Security Hub CSPM, and AWS Systems Manager. Amazon Q Developer in chat applications only supports EventBridge events from AWS services. For an exhaustive list of supported service events, see [EventBridge Event Examples from Supported AWS Services](https://docs.aws.amazon.com/eventbridge/latest/userguide/event-types.html) in the *EventBridge User Guide*.

**Note**  
Event notifications from: CloudWatch Alarms, CodeBuild, CodeCommit, CodeDeploy, and CodePipeline are not currently supported via EventBridge rules. If you want to receive notifications for one of these services, you can go to its console, and configure Amazon SNS notifications that you can then map to your chat channel or Amazon Chime webhook configuration in Amazon Q Developer in chat applications. For more information, see [Amazon CloudWatch alarms ](#cloudwatch)or [Notifications for AWS developer tools](#codeserviceevents). 

## [AWS Config](https://console.aws.amazon.com/config/)
<a name="aws-config"></a>

AWS Config performs resource oversight and tracking for auditing and compliance, config change management, troubleshooting, and security analysis. It provides a detailed view of AWS resources configuration in your AWS account. The service also shows how resources relate to one another and how they were configured in the past, so you can see how configurations and relationships change over time. 

For AWS Config monitoring, [you configure Amazon CloudWatch Events rules](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/Create-CloudWatch-Events-Rule.html) to forward AWS Config events notifications to an Amazon SNS topic. You can then map that topic to Amazon Q Developer in chat applications to track those event notifications in chat rooms.

 For more information, see [ Notifications for AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/notifications-for-AWS-Config.html) in the *AWS Config Developer Guide*.

## [Amazon GuardDuty](https://console.aws.amazon.com/guardduty/)
<a name="aws-guardduty"></a>

Amazon GuardDuty is a security threat monitoring service that detects and reports on potential security threats in your AWS account. It uses threat intelligence feeds, such as lists of malicious IPs and domains, and machine learning to identify possible unauthorized and malicious activity in your AWS environment.

GuardDuty reports its security incidents and threats through *findings*. Findings appear in the GuardDuty console and automatically appear as CloudWatch Events. You then [create Amazon CloudWatch Events rules](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/Create-CloudWatch-Events-Rule.html), so these events appear as notifications to a selected SNS topic. You then map that SNS topic to a chat channel or Amazon Chime webhook in Amazon Q Developer in chat applications.

 For more information, see [Monitoring Amazon GuardDuty Findings with Amazon CloudWatch Events](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_findings_cloudwatch.html) in the *Amazon GuardDuty User Guide*.

## [AWS Health](https://phd.aws.amazon.com/phd/home#/)
<a name="aws-health"></a>

AWS Health provides visibility into the state of your AWS resources, services, and accounts. It provides information about the performance and availability of resources that affect your applications running on AWS and guidance for remediation. AWS Health provides this information in a console called the AWS Health Dashboard. 

AWS Health directly supports EventBridge notifications. You configure [CloudWatch Events rules](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/Create-CloudWatch-Events-Rule.html) for AWS Health, and specify an SNS topic mapped in Amazon Q Developer in chat applications. 

For more information, see [Monitoring AWS Health Events with Amazon CloudWatch Events](https://docs.aws.amazon.com/health/latest/ug/cloudwatch-events-health.html) in the *AWS Health User Guide*.

## [AWS Security Hub CSPM](https://console.aws.amazon.com/securityhub/)
<a name="security-hub"></a>

AWS Security Hub CSPM provides a comprehensive view of high-priority security alerts and compliance status across your AWS accounts. Security Hub CSPM aggregates, organizes, and prioritizes security findings from multiple AWS services, including Amazon GuardDuty, Amazon Inspector, and Amazon Macie. Security Hub CSPM reduces the effort of collecting and prioritizing security findings across accounts, from AWS services, and from AWS partner tools. 

Security Hub CSPM supports two types of integration with [CloudWatch Events rules](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/Create-CloudWatch-Events-Rule.html), both of which Amazon Q Developer in chat applications supports:
+ **Standard CloudWatch Events**. [Security Hub CSPM automatically sends all findings to CloudWatch Events](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-cloudwatch-events.html). You can define CloudWatch Events rules that automatically route generated findings to an Amazon Simple Storage Service (Amazon S3) bucket, a remediation workflow, or an SNS topic. Use this method to automatically send all Security Hub CSPM findings, or all findings with specific characteristics, to an SNS topic to which Amazon Q Developer in chat applications subscribes.
+ **Security Hub CSPM Custom Actions**.[ Define custom actions in Security Hub CSPM](https://aws.amazon.com/blogs/apn/how-to-enable-custom-actions-in-aws-security-hub/) and configure [CloudWatch Events rules](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/Create-CloudWatch-Events-Rule.html) to respond to those actions. The event rule uses its SNS topic setting to forward its notifications to the SNS topic to which Amazon Q Developer in chat applications subscribes. 

## [AWS Systems Manager](https://console.aws.amazon.com/systems-manager/)
<a name="system-manager"></a>

AWS Systems Manager lets you view and control your infrastructure on AWS. Using the Systems Manager console, you can view operational data from multiple AWS services and automate operational tasks across your AWS resources. Systems Manager helps you maintain security and compliance by scanning your managed instances, and reporting or taking corrective action on detected policy violations.

Amazon Q Developer in chat applications supports the following Systems Manager events.

**Configuration compliance**
+ Status change for association compliance.
+ Status change for instance patch compliance.

**Automation**
+ Status change for an automation execution.
+ Status change for a single step in an automation execution.

**Run command**
+ Status change for a command (applies to one or more instances).
+ Status change for a command invocation (applies to one instance only). 

**State manager**
+ Status change for an association.
+ Status change for an instance association.

**Parameter store**
+ A parameter is created.
+ A parameter is updated.
+ A parameter is deleted.

For information about monitoring Systems Manager events with CloudWatch, see [Monitoring Systems Manager Events with Amazon CloudWatch Events](https://docs.aws.amazon.com/systems-manager/latest/userguide/monitoring-cloudwatch-events.html) in the *AWS Systems Manager User Guide*. 

## AWS Systems Manager Runbooks
<a name="runbooks"></a>

SM runbooks define the actions that Systems Manager performs on your managed instances and other AWS resources when an automation runs. A runbook contains one or more steps that run in sequential order. The process of running these actions and their steps is called the automation. Amazon Q Developer in chat applications supports the ability to run SM runbooks directly from Microsoft Teams or Slack using CLI commands. You can type a command to list your runbooks and choose a runbook to run. Runbooks can require one or more input parameters before running (for example, Amazon EC2 instances can require inputs such as instance id). Once the runbook begins, it runs in its entirety. For an example of running a runbook using a CLI command, see [Run an Automation runbook](common-use-cases.md#run-book).

For more information about SM runbooks, see[ Working with runbooks](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-documents.html) in the *AWS Systems Manager User Guide*.

## AWS Systems Manager Incident Manager
<a name="incidentManager"></a>

AWS Systems Manager Incident Manager is an incident management console designed to help users mitigate and recover from incidents affecting their AWS-hosted applications. An incident is any unplanned interruption or reduction in quality of services.

Amazon Q Developer in chat applications allows you to communicate through chat channels and receive notifications and incident updates during an incident. You can also interact with the incident directly using chat commands. For more information, see [Chat channels](https://docs.aws.amazon.com/incident-manager/latest/userguide/chat.html) in the *Incident Manager User Guide*.