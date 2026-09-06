

# myApplications dashboard in AWS Console Home
<a name="myApp-app-dash"></a>

Each application you create or onboard has its own myApplications dashboard. The myApplications dashboard contains cost, security, and operational widgets that surface insights from multiple AWS services. Each widget can also be favorited, reordered, removed, or resized. For more information, see [Working with widgets in AWS Console Home](work-with-widgets.md).

**Topics**
+ [Application dashboard setup widget](#myApp-appdash-setup)
+ [Application summary widget](#myApp-summary)
+ [Compute widget](#myApp-comp)
+ [Cost and usage widget](#myApp-costusage)
+ [AWS Security widget](#myApp-sechub)
+ [AWS Resiliency widget](#myApp-reshub)
+ [Resources widget](#myApp-resources)
+ [DevOps widget](#myApp-devops)
+ [Monitoring and operations widget](#myApp-operations)
+ [Tags widget](#myApp-tags-widget)

## Application dashboard setup widget
<a name="myApp-appdash-setup"></a>

This widget contains a list of suggested getting started activities you can use to help you configure AWS services for managing application resources. 

## Application summary widget
<a name="myApp-summary"></a>

This widget shows the name, description, and [AWS application tag](https://docs.aws.amazon.com/servicecatalog/latest/arguide/overview-appreg.html#ar-user-tags) for your application. You can access and copy the application tag in Infrastructure as Code (IAC) to manually tag resources.

## Compute widget
<a name="myApp-comp"></a>

This widget displays information and metrics for compute resources, you add to your application. This includes total alarms and total compute resource types. The widget also shows resource performance metric trend charts from Amazon CloudWatch for Amazon EC2 instance CPU utilization and Lambda invocations.

### Configuring the Compute widget
<a name="configcomp-configure"></a>

 To populate data in the Compute widget, set up at least one Amazon EC2 instance or a Lambda function for your application. For more information, see the [Amazon Elastic Compute Cloud Documentation](https://docs.aws.amazon.com/ec2) and [Getting started with Lambda](https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html) in the *AWS Lambda Developer Guide*. 

## Cost and usage widget
<a name="myApp-costusage"></a>

This widget shows AWS cost and usage data for your application resources. You can use this data to compare monthly costs and view cost breakdowns by AWS service. This widget only summarizes costs for resources tagged with the AWS application tag, excluding taxes, fees, and other shared costs not directly associated with a resource. Costs shown are unblended and updated at least once every 24 hours. FOr more information, see [Analyzing your costs with AWS Resource Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html) in the *AWS Cost Management User Guide*.

### Configuring the Cost and usage widget
<a name="costusage-configure"></a>

 To configure the Cost and usage widget, enable AWS Cost Explorer Service for your application and account. This service is offered at no additional charge and there are no setup fees or upfront commitment. For more information, see [Enabling Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-enable.html) in the *AWS Cost Management User Guide*. 

## AWS Security widget
<a name="myApp-sechub"></a>

This widget displays security findings from AWS Security for your application. AWS Security provides a comprehensive view of security findings for your application in AWS. You can access recent priority findings by severity, monitor their security posture, access recent critical or high severity findings, and gain insight for next steps. For more information, see [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/).

### Configuring the AWS Security widget
<a name="sechub-configure"></a>

 To configure the AWS Security widget, set up AWS Security Hub CSPM for your application and account. For more information, see [What is AWS Security Hub CSPM?](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html#securityhub-free-trial) in the *AWS Security Hub CSPM User Guide*. For pricing information, see [AWS Security Hub CSPM free trial, usage, and pricing ](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html#securityhub-free-trial) in the *AWS Security Hub CSPM User Guide*. 

 AWS Security Hub CSPM requires you to configure AWS Config Recording. This service provides a detailed view of the resources associated with your AWS account. For more information, see [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/quick-setup-config.html) in the *AWS Systems Manager User Guide*. 

## AWS Resiliency widget
<a name="myApp-reshub"></a>

This widget displays resiliency details from AWS Resilience Hub for your applications. After initiating an assessment, AWS Resiliency Hub analyzes your applications' resiliency posture by evaluating their resources against a pre-defined resiliency policy. You can access metrics like resiliency score, policy breaches, policy drifts, resource drifts, and your resliency score history. Your applications are assessed daily for enhanced tracking, but you can disable this at any time. For more information, see [AWS Resilience Hub](https://aws.amazon.com/resilience-hub/). For pricing information, see [AWS Resilience Hub pricing](https://aws.amazon.com/resilience-hub/).

### Configuring the AWS Resiliency widget
<a name="reshub-configure"></a>

 To configure the AWS Resiliency widget, add an application. For more information, see [What is AWS Resilience Hub?](https://docs.aws.amazon.com/resilience-hub/latest/userguide/what-is.html) in the *AWS Resilience Hub User Guide*.

## Resources widget
<a name="myApp-resources"></a>

This widget uses AWS Resource Explorer to show resources you have added to your application within a view. You can also use this widget to search or filter your resources using resource metadata like names, tags, and IDs. For more information, see [AWS Resource Explorer](https://aws.amazon.com/resourceexplorer/).

### Configuring the Resources widget
<a name="reshub-configure"></a>

 To configure the resources widget, onboard with Resource Explorer. For more information, see [Getting started with Resource Explorer](https://docs.aws.amazon.com/resource-explorer/latest/userguide/getting-started.html) in the *AWS Resource Explorer User Guide*.

## DevOps widget
<a name="myApp-devops"></a>

This widget shows operational insights so you can assess compliance and take action for your application. These insights include:
+ Fleet management
+ State management
+ Patch management
+ Configuration and OpsItems management

### Configuring the DevOps widget
<a name="devops-configure"></a>

 To configure the DevOps widget, enable AWS Systems Manager OpsCenter for your application and account. For more information, see [Getting started with Systems Manager Explorer and OpsCenter](https://docs.aws.amazon.com/systems-manager/latest/userguide/Explorer-setup.html) in the *AWS Systems Manager User Guide*. Enabling OpsCenter allows AWS Systems Manager Explorer to configure AWS Config and Amazon CloudWatch so that their events automatically create OpsItems based on commonly-used rules and events. For more information, see [Set up OpsCenter](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-setup.html) in the *AWS Systems Manager User Guide*. 

 You can configure your instances for Systems Manager agents to run and apply permissions to enable patch scanning. For more information, see [AWS Systems Manager Quick Setup](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-quick-setup.html) in the *AWS Systems Manager User Guide*.

You can also set up automated patching of Amazon EC2 instances for your application by setting up AWS Systems Manager Patch Manager. For more information, see [Using Quick Setup patch policies](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-policies.html) in the *AWS Systems Manager User Guide*.

For pricing information, see [AWS Systems Manager pricing](https://aws.amazon.com/systems-manager/pricing/). 

## Monitoring and operations widget
<a name="myApp-operations"></a>

 This widget shows: 
+ Alarms and alerts for resources associated with your application
+ Application service level objectives (SLOs) and metrics
+ Available AWS Application Signals metrics

### Configuring the Monitoring and operations widget
<a name="operations-configure"></a>

 To configure the Monitoring and operations widget, create CloudWatch alarms and canaries in your AWS account. For more information, see [Using Amazon CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) and [Creating a canary](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Create.html) in the *Amazon CloudWatch User Guide*. For CloudWatch alarm and synthetic canary pricing, see [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/) and the [AWS Cloud Operations and Migrations Blog](https://aws.amazon.com/blogs/mt/managing-cloudwatch-synthetics-canaries-at-scale/) respectively. 

For more information about CloudWatch Application Signals, see [Enable Amazon CloudWatch Application Signals](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Signals-Enable.html) in the *Amazon CloudWatch User Guide*.

## Tags widget
<a name="myApp-tags-widget"></a>

This widget displays all tags associated with your application. You can use this widget to track and manage application metadata (criticality, environment, cost center). For more information, see [What are tags?](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/what-are-tags.html) in the *Best practices for Tagging AWS Resources AWS Whitepaper*.