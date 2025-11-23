# Troubleshooting with Amazon Q Developer

You can use [Amazon Q Developer](../../../amazonq/latest/qdeveloper-ug/what-is.md "../../../amazonq/latest/qdeveloper-ug/what-is.md") in the Amazon ECS console to help diagnose and resolve issues with your Amazon ECS resources. For certain errors and status messages on containers, tasks, services, deployments, and task definitions, the console shows an **Inspect with Amazon Q Developer** option. When you choose this option, Amazon Q Developer analyzes the issue in context and suggests possible causes and remediation steps.

## Required permissions

- Permissions to view the Amazon ECS resources you want to troubleshoot, such as clusters, services, tasks, and task definitions.
- [Permissions to use Amazon Q Developer](../../../amazonq/latest/qdeveloper-ug/security_iam_permissions.md "../../../amazonq/latest/qdeveloper-ug/security_iam_permissions.md") in the console.
- (Recommended) Permissions to view related logs and metrics, such as:
  - CloudWatch Logs
  - CloudWatch

## Procedure

1. Open the console at [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. Determine the resource that you want to troubleshoot.

| Resource                 | Steps                                                                                                                                                                                                        |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Tasks                    | 1. On the **Clusters\*<br>• page, choose the cluster.<br>2. Choose the **Tasks\*<br>• tab.<br>3. Choose the task that you want to investigate.                                                               |
| Containers               | 1. On the **Clusters\*<br>• page, choose the cluster.<br>2. Choose the **Tasks*<br>• tab, and then choose the task.<br>3. In the \*\*Containers*<br>• section, choose the container you want to investigate. |
| Services and deployments | 1. On the **Clusters\*<br>• page, choose the cluster.<br>2. Choose the **Services*<br>• tab.<br>3. Choose the service, and then review the \*\*Deployments*<br>• section.                                    |
| Task definitions         | 1. In the navigation pane, choose **Task definitions**.<br>2. Choose the task definition family, and then choose the revision that you want to investigate.                                                  |

3. On the resource details page, locate the status or health reason that describes the issue.
4. Click the status reason to open the popover.
5. If available, choose **Inspect with Amazon Q Developer**.
6. Review the explanation and suggested remediation steps that Amazon Q Developer provides. Apply configuration or operational changes as appropriate for your environment.

## Considerations

Consider the following when using Amazon Q Developer with Amazon ECS:

- **Button availability** - The "Inspect with Amazon Q Developer" button is only displayed for resources experiencing potential issues. This option is not available for healthy resources.
- **Read-only operations** - The Amazon Q Developer integration performs only read operations. It makes no mutating or write actions.
- **Cross-region processing** - Amazon Q Developer may process data across AWS regions to provide AI-powered analysis. For more information about cross-region processing, see [Cross-region processing in Amazon Q Developer](../../../amazonq/latest/qdeveloper-ug/cross-region-processing.md "../../../amazonq/latest/qdeveloper-ug/cross-region-processing.md").
- **Console only** - This integration is available only through the Console. It is not available through the AWS CLI, AWS APIs, or infrastructure as code tools.

## Learn more

For more information about using Amazon Q Developer, see [Chatting with Amazon Q Developer about AWS](../../../amazonq/latest/qdeveloper-ug/chat-with-q.md "../../../amazonq/latest/qdeveloper-ug/chat-with-q.md").
