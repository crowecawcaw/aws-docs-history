

# Troubleshooting with Amazon Q Developer
<a name="troubleshooting-with-Q"></a>

You can use [Amazon Q Developer](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/what-is.html) in the Amazon ECS console to help diagnose and resolve issues with your Amazon ECS resources. For certain errors and status messages on containers, tasks, services, deployments, and task definitions, the console shows an **Inspect with Amazon Q Developer** option. When you choose this option, Amazon Q Developer analyzes the issue in context and suggests possible causes and remediation steps.

## Required permissions
<a name="troubleshooting-with-Q-permissions"></a>
+ Permissions to view the Amazon ECS resources you want to troubleshoot, such as clusters, services, tasks, and task definitions.
+ [Permissions to use Amazon Q Developer](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_permissions.html) in the console.
+ (Recommended) Permissions to view related logs and metrics, such as:
  + CloudWatch Logs
  + CloudWatch

## Procedure
<a name="troubleshooting-with-Q-procedure"></a>

1. Open the console at [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2).

1. Determine the resource that you want to troubleshoot.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/troubleshooting-with-Q.html)

1. On the resource details page, locate the status or health reason that describes the issue.

1. Click the status reason to open the popover.

1. If available, choose **Inspect with Amazon Q Developer**.

1. Review the explanation and suggested remediation steps that Amazon Q Developer provides. Apply configuration or operational changes as appropriate for your environment.

## Considerations
<a name="troubleshooting-with-Q-considerations"></a>

Consider the following when using Amazon Q Developer with Amazon ECS:
+ **Button availability** - The "Inspect with Amazon Q Developer" button is only displayed for resources experiencing potential issues. This option is not available for healthy resources.
+ **Read-only operations** - The Amazon Q Developer integration performs only read operations. It makes no mutating or write actions.
+ **Cross-region processing** - Amazon Q Developer may process data across AWS regions to provide AI-powered analysis. For more information about cross-region processing, see [Cross-region processing in Amazon Q Developer](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/cross-region-processing.html).
+ ** Console only** - This integration is available only through the Console. It is not available through the AWS CLI, AWS APIs, or infrastructure as code tools.

## Learn more
<a name="troubleshooting-with-Q-learn-more"></a>

For more information about using Amazon Q Developer, see [Chatting with Amazon Q Developer about AWS](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/chat-with-q.html).