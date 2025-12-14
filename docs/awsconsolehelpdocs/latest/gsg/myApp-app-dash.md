# myApplications dashboard in AWS Console Home

Each application you create or onboard has its own myApplications dashboard. The myApplications dashboard contains cost, security, and operational widgets that surface insights from multiple AWS services. Each widget can also be favorited, reordered, removed, or resized.
For more information, see [Working with widgets in AWS Console Home](work-with-widgets.md "work-with-widgets.md").

###### Topics

- [Application dashboard setup widget](#myApp-appdash-setup "#myApp-appdash-setup")
- [Application summary widget](#myApp-summary "#myApp-summary")
- [Compute widget](#myApp-comp "#myApp-comp")
- [Cost and usage widget](#myApp-costusage "#myApp-costusage")
- [AWS Security widget](#myApp-sechub "#myApp-sechub")
- [AWS Resiliency widget](#myApp-reshub "#myApp-reshub")
- [Resources widget](#myApp-resources "#myApp-resources")
- [DevOps widget](#myApp-devops "#myApp-devops")
- [Monitoring and operations widget](#myApp-operations "#myApp-operations")
- [Tags widget](#myApp-tags-widget "#myApp-tags-widget")

## Application dashboard setup widget

This widget contains a list of suggested getting started activities you can use to help you configure AWS services for managing application resources.

## Application summary widget

This widget shows the name, description, and [AWS application tag](../../../servicecatalog/latest/arguide/overview-appreg.md#ar-user-tags "../../../servicecatalog/latest/arguide/overview-appreg.md#ar-user-tags") for your application. You can access and copy the application tag in Infrastructure as Code (IAC) to manually tag resources.

## Compute widget

This widget displays information and metrics for compute resources, you add to your application. This includes total alarms and total compute resource types. The widget also shows resource performance metric trend charts from Amazon CloudWatch for Amazon EC2 instance CPU utilization and Lambda invocations.

### Configuring the Compute widget

To populate data in the Compute widget, set up at least one Amazon EC2 instance or a Lambda function for your application. For more information, see the [Amazon Elastic Compute Cloud Documentation](../../../ec2.md "../../../ec2.md") and
[Getting started with Lambda](../../../lambda/latest/dg/getting-started.md "../../../lambda/latest/dg/getting-started.md") in the _AWS Lambda Developer Guide_.

## Cost and usage widget

This widget shows AWS cost and usage data for your application resources. You can use this data to compare monthly costs and view cost breakdowns by AWS service.
This widget only summarizes costs for resources tagged with the AWS application tag, excluding taxes, fees, and other shared costs not directly associated with a resource.
Costs shown are unblended and updated at least once every 24 hours. FOr more information, see [Analyzing your costs with AWS Resource Explorer](../../../cost-management/latest/userguide/ce-what-is.md "../../../cost-management/latest/userguide/ce-what-is.md") in the _AWS Cost Management User Guide_.

### Configuring the Cost and usage widget

To configure the Cost and usage widget, enable AWS Cost Explorer Service for your application and account. This service is offered at no additional charge and there are no setup fees or upfront commitment. For more information, see [Enabling Cost Explorer](../../../cost-management/latest/userguide/ce-enable.md "../../../cost-management/latest/userguide/ce-enable.md") in the
_AWS Cost Management User Guide_.

## AWS Security widget

This widget displays security findings from AWS Security for your application. AWS Security provides a comprehensive view of security findings for your application in AWS. You can access recent priority findings by severity, monitor their security posture,
access recent critical or high severity findings, and gain insight for next steps. For more information, see [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/ "https://aws.amazon.com/security-hub/").

### Configuring the AWS Security widget

To configure the AWS Security widget, set up AWS Security Hub CSPM for your application and account. For more information, see [What is AWS Security Hub CSPM?](../../../securityhub/latest/userguide/what-is-securityhub.md#securityhub-free-trial "../../../securityhub/latest/userguide/what-is-securityhub.md#securityhub-free-trial") in the
_AWS Security Hub CSPM User Guide_. For pricing information, see [AWS Security Hub CSPM free trial, usage, and pricing](../../../securityhub/latest/userguide/what-is-securityhub.md#securityhub-free-trial "../../../securityhub/latest/userguide/what-is-securityhub.md#securityhub-free-trial") in the
_AWS Security Hub CSPM User Guide_.

AWS Security Hub CSPM requires you to configure AWS Config Recording. This service provides a detailed view of the resources associated with your AWS account. For more information, see [AWS Systems Manager](../../../systems-manager/latest/userguide/quick-setup-config.md "../../../systems-manager/latest/userguide/quick-setup-config.md") in the _AWS Systems Manager User Guide_.

## AWS Resiliency widget

This widget displays resiliency details from AWS Resilience Hub for your applications. After initiating an assessment, AWS Resiliency Hub analyzes your applications' resiliency posture by evaluating their resources against a pre-defined resiliency policy. You can access metrics like resiliency score, policy breaches, policy drifts, resource drifts, and your resliency score history. Your applications are assessed daily
for enhanced tracking, but you can disable this at any time. For more information, see [AWS Resilience Hub](https://aws.amazon.com/resilience-hub/ "https://aws.amazon.com/resilience-hub/"). For pricing information, see [AWS Resilience Hub pricing](https://aws.amazon.com/resilience-hub/ "https://aws.amazon.com/resilience-hub/").

### Configuring the AWS Resiliency widget

To configure the AWS Resiliency widget, add an application. For more information, see [What is AWS Resilience Hub?](../../../resilience-hub/latest/userguide/what-is.md "../../../resilience-hub/latest/userguide/what-is.md") in the
_AWS Resilience Hub User Guide_.

## Resources widget

This widget uses AWS Resource Explorer to show resources you have added to your application within a view. You can also use this widget to search or filter your resources using resource metadata like names, tags, and IDs. For more information, see [AWS Resource Explorer](https://aws.amazon.com/resourceexplorer/ "https://aws.amazon.com/resourceexplorer/").

### Configuring the Resources widget

To configure the resources widget, onboard with Resource Explorer. For more information, see [Getting started with Resource Explorer](../../../resource-explorer/latest/userguide/getting-started.md "../../../resource-explorer/latest/userguide/getting-started.md") in the
_AWS Resource Explorer User Guide_.

## DevOps widget

This widget shows operational insights so you can assess compliance and take action for your application. These insights include:

- Fleet management
- State management
- Patch management
- Configuration and OpsItems management

### Configuring the DevOps widget

To configure the DevOps widget, enable AWS Systems Manager OpsCenter for your application and account. For more information, see [Getting started with Systems Manager Explorer and OpsCenter](../../../systems-manager/latest/userguide/Explorer-setup.md "../../../systems-manager/latest/userguide/Explorer-setup.md") in the
_AWS Systems Manager User Guide_. Enabling OpsCenter allows AWS Systems Manager Explorer to configure AWS Config and Amazon CloudWatch so that their events automatically create OpsItems based on commonly-used rules and events. For more information, see [Set up OpsCenter](../../../systems-manager/latest/userguide/OpsCenter-setup.md "../../../systems-manager/latest/userguide/OpsCenter-setup.md") in the _AWS Systems Manager User Guide_.

You can configure your instances for Systems Manager agents to run and apply permissions to enable patch scanning. For more information, see
[AWS Systems Manager Quick Setup](../../../systems-manager/latest/userguide/systems-manager-quick-setup.md "../../../systems-manager/latest/userguide/systems-manager-quick-setup.md") in the _AWS Systems Manager User Guide_.

You can also set up automated patching of Amazon EC2 instances for your application by setting up AWS Systems Manager Patch Manager. For more information, see [Using Quick Setup patch policies](../../../systems-manager/latest/userguide/patch-manager-policies.md "../../../systems-manager/latest/userguide/patch-manager-policies.md") in the _AWS Systems Manager User Guide_.

For pricing information, see [AWS Systems Manager pricing](https://aws.amazon.com/systems-manager/pricing/ "https://aws.amazon.com/systems-manager/pricing/").

## Monitoring and operations widget

This widget shows:

- Alarms and alerts for resources associated with your application
- Application service level objectives (SLOs) and metrics
- Available AWS Application Signals metrics

### Configuring the Monitoring and operations widget

To configure the Monitoring and operations widget, create CloudWatch alarms and canaries in your AWS account. For more information, see [Using Amazon CloudWatch alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md") and [Creating a canary](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Create.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Create.md") in the
_Amazon CloudWatch User Guide_. For CloudWatch alarm and synthetic canary pricing, see [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/") and the [AWS Cloud Operations and Migrations Blog](https://aws.amazon.com/blogs/mt/managing-cloudwatch-synthetics-canaries-at-scale/ "https://aws.amazon.com/blogs/mt/managing-cloudwatch-synthetics-canaries-at-scale/") respectively.

For more information about CloudWatch Application Signals, see [Enable Amazon CloudWatch Application Signals](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Signals-Enable.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Signals-Enable.md") in the _Amazon CloudWatch User Guide_.

## Tags widget

This widget displays all tags associated with your application. You can use this widget to track and manage application metadata (criticality, environment, cost center). For more information, see [What are tags?](../../../whitepapers/latest/tagging-best-practices/what-are-tags.md "../../../whitepapers/latest/tagging-best-practices/what-are-tags.md") in the _Best practices for Tagging AWS Resources AWS Whitepaper_.
