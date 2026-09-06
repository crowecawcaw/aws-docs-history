

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# AWS Systems Manager Automation
<a name="systems-manager-automation"></a>

Automation simplifies common maintenance, deployment, and remediation tasks for AWS services like Amazon Elastic Compute Cloud (Amazon EC2), Amazon Relational Database Service (Amazon RDS), Amazon Redshift, Amazon Simple Storage Service (Amazon S3), and many more. To get started with Automation, open the [Systems Manager console](https://console.aws.amazon.com/systems-manager/automation). In the navigation pane, choose **Automation**. 

This section includes the following topics.
+ [Implement change controls for Automation](automation-change-calendar-integration.md)
+ [Setting up identity based policies examples](automation-setup-identity-based-policies.md)
+ [Create service roles for Automation by using CloudFormation](automation-setup-cloudformation.md)
+ [Learn about statuses returned by Systems Manager Automation](automation-statuses.md)
+ [Schedule automations with maintenance windows](scheduling-automations-maintenance-windows.md)
+ [Using Document Builder to create runbooks](automation-document-builder.md)
+ [Run an automation that requires approvals](running-automations-require-approvals.md)
+ [Running automations in multiple AWS Regions and accounts](running-automations-multiple-accounts-regions.md)
+ [Run automations based on EventBridge events](running-automations-event-bridge.md)
+ [Run an automation step by step](automation-working-executing-manually.md)
+ [Using scripts in runbooks](automation-document-script-considerations.md)
+ [Using conditional statements in runbooks](automation-branch-condition.md)
+ [Using action outputs as inputs](automation-action-outputs-inputs.md)
+ [Creating webhook integrations for Automation](creating-webhook-integrations.md)
+ [Updating AMIs](automation-tutorial-update-ami.md)
+ [Updating AMIs using Automation and Jenkins](automation-tutorial-update-patch-ami-jenkins-integration.md)
+ [Updating AMIs for Auto Scaling groups](automation-tutorial-update-patch-windows-ami-autoscaling.md)
+ [Run the EC2Rescue tool on unreachable instances](automation-ec2rescue.md)
+ [Passing data to Automation using input transformers](automation-tutorial-eventbridge-input-transformers.md)

Automation helps you to build automated solutions to deploy, configure, and manage AWS resources at scale. With Automation, you have granular control over the concurrency of your automations. This means you can specify how many resources to target concurrently, and how many errors can occur before an automation is stopped. 

To help you get started with Automation, AWS develops and maintains several pre-defined runbooks. Depending on your use case, you can use these pre-defined runbooks that perform a variety of tasks, or create your own custom runbooks that might better suit your needs. To monitor the progress and status of your automations, you can use the Systems Manager Automation console, or your preferred command line tool. Automation also integrates with Amazon EventBridge to help you build event-driven architecture at scale.

**Note**  
For customers who are new to Systems Manager Automation as of August 14, 2025, the Automation free tier is not available. For customers already using Automation, the free tier of service ends on December 31, 2025. For information about current service costs, see [AWS Systems Manager pricing](https://aws.amazon.com/systems-manager/pricing/).

## How can Automation benefit my organization?
<a name="automation-benefits"></a>

Automation offers these benefits:
+ **Scripting support in runbook content**

  Using the `aws:executeScript` action, you can run custom Python and PowerShell functions directly from your runbooks. This provides you greater flexibility in creating your custom runbooks because you can complete various tasks that other Automation actions don't support. You also have greater control over the logic of the runbook. For an example of how this action can be used and how it can help to improve an existing automated solution, see [Authoring Automation runbooks](automation-authoring-runbooks.md).
+  **Run automations across multiple AWS accounts and AWS Regions from a centralized location** 

  Administrators can run automations on resources across multiple accounts and Regions from the Systems Manager console.
+  **Enhanced operations security** 

  Administrators have a centralized place to grant and revoke access to runbooks. Using only AWS Identity and Access Management (IAM) policies, you can control which individual users or groups in your organization can use Automation and which runbooks they can access.
+  **Automate common IT tasks** 

  Automating common tasks can help improve operational efficiency, enforce organizational standards, and reduce operator errors. For example, you can use the `AWS-UpdateCloudFormationStackWithApproval` runbook to update resources that were deployed by using an AWS CloudFormation template. The update applies a new template. You can configure the Automation to request approval by one or more users before the update begins.
+  **Safely perform disruptive tasks in bulk** 

  Automation includes features, like rate controls, that allow you to control the deployment of an automation across your fleet by specifying a concurrency value and an error threshold. For more information about working with rate controls, see [Run automated operations at scale](running-automations-scale.md).
+ **Streamline complex tasks**

  Automation provides pre-defined runbooks that streamline complex and time-consuming tasks such as creating golden Amazon Machine Images (AMIs). For example, you can use the `AWS-UpdateLinuxAmi` and `AWS-UpdateWindowsAmi` runbooks to create golden AMIs from a source AMI. Using these runbooks, you can run custom scripts before and after updates are applied. You can also include or exclude specific software packages from being installed. For examples of how to use these runbooks, see [Tutorials](automation-tutorials.md).
+ **Define constraints for inputs**

  You can define constraints in custom runbooks to limit the values that Automation will accept for a particular input parameter. For example, `allowedPattern` will only accept values for an input parameter that match the regular expression you define. If you specify `allowedValues` for an input parameter, only the values you've specified in the runbook are accepted.
+  **Log automation action output to Amazon CloudWatch Logs** 

  To meet operational or security requirements in your organization, you might need to provide a record of the scripts run during a runbook. With CloudWatch Logs, you can monitor, store, and access log files from various AWS services. You can send output from the `aws:executeScript` action to a CloudWatch Logs log group for debugging and troubleshooting purposes. Log data can be sent to your log group with or without AWS KMS encryption using your KMS key. For more information, see [Logging Automation action output with CloudWatch Logs](automation-action-logging.md).
+  **Amazon EventBridge integration** 

  Automation is supported as a *target* type in Amazon EventBridge rules. This means you can trigger runbooks by using events. For more information, see [Monitoring Systems Manager events with Amazon EventBridge](monitoring-eventbridge-events.md) and [Reference: Amazon EventBridge event patterns and types for Systems Manager](reference-eventbridge-events.md).
+ **Share organizational best practices**

  You can define best practices for resource management, operations tasks, and more in runbooks that you share across accounts and Regions.

## Who should use Automation?
<a name="automation-who"></a>
+ Any AWS customer who wants to improve their operational efficiency at scale, reduce errors associated with manual intervention, and reduce time to resolution of common issues.
+ Infrastructure experts who want to automate deployment and configuration tasks.
+ Administrators who want to reliably resolve common issues, improve troubleshooting efficiency, and reduce repetitive operations.
+ Users who want to automate a task they normally perform manually.

## What is an automation?
<a name="what-is-an-automation"></a>

An *automation* consists of all of the tasks that are defined in a runbook, and are performed by the Automation service. Automation uses the following components to run automations.



| Concept | Details | 
| --- | --- | 
| Automation runbook | A Systems Manager Automation runbook defines the automation (the actions that Systems Manager performs on your managed nodes and AWS resources). Automation includes several pre-defined runbooks that you can use to perform common tasks like restarting one or more Amazon EC2 instances or creating an Amazon Machine Image (AMI). You can create your own runbooks as well. Runbooks use YAML or JSON, and they include steps and parameters that you specify. Steps run in sequential order. For more information, see [Creating your own runbooks](automation-documents.md).<br />Runbooks are Systems Manager documents of type `Automation`, as opposed to `Command`, `Policy`, `Session` documents. Runbooks support schema version 0.3. Command documents use schema version 1.2, 2.0, or 2.2. Policy documents use schema version 2.0 or later. | 
| Automation action | The automation defined in a runbook includes one or more steps. Each step is associated with a particular action. The action determines the inputs, behavior, and outputs of the step. Steps are defined in the `mainSteps` section of your runbook. Automation supports 20 distinct action types. For more information, see the [Systems Manager Automation actions reference](automation-actions.md). | 
| Automation quota | Each AWS account can run 100 automations simultaneously. This includes child automations (automations that are started by another automation), and rate control automations. If you attempt to run more automations than this, Systems Manager adds the additional automations to a queue and displays a status of Pending. This quota can be adjusted using adaptive concurrency. For more information, see [Allowing Automation to adapt to your concurrency needs](adaptive-concurrency.md).For more information about running automations, see [Run an automated operation powered by Systems Manager Automation](running-simple-automations.md). | 
| Automation queue quota | If you attempt to run more automations than the concurrent automation limit, subsequent automations are added to a queue. Each AWS account can queue 5,000 automations. When an automation is complete (or reaches a terminal state), the first automation in the queue is started. | 
| Rate control automation quota | Each AWS account can run 25 rate control automations simultaneously. If you attempt to run more rate control automations than the concurrent rate control automation limit, Systems Manager adds the subsequent rate control automations to a queue and displays a status of Pending. For more information about running rate control automations, see [Run automated operations at scale](running-automations-scale.md). | 
| Rate control automation queue quota | If you attempt to run more automations than the concurrent rate control automation limit, subsequent automations are added to a queue. Each AWS account can queue 1,000 rate control automations. When an automation is complete (or reaches a terminal state), the first automation in the queue is started. | 