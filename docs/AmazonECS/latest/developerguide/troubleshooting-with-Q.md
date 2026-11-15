

# Troubleshooting with AWS assistant
<a name="troubleshooting-with-Q"></a>

You can use the [AWS assistant](https://docs.aws.amazon.com/assistant/latest/userguide/what-is.html) in the Amazon ECS console to help diagnose and resolve issues with your Amazon ECS resources. For certain errors and status messages on containers, tasks, services, deployments, and task definitions, the console shows an **Inspect with AWS assistant** option. When you choose this option, the AWS assistant analyzes the issue in context and suggests possible causes and remediation steps.

## Required permissions
<a name="troubleshooting-with-Q-permissions"></a>
+ Permissions to view the Amazon ECS resources you want to troubleshoot, such as clusters, services, tasks, and task definitions.
+ [Permissions to use AWS assistant](https://docs.aws.amazon.com/assistant/latest/userguide/getting-started.html#permissions-overview) in the console.
+ (Recommended) Permissions to view related logs and metrics, such as:
  + CloudWatch Logs
  + CloudWatch

## Procedure
<a name="troubleshooting-with-Q-procedure"></a>

1. Open the console at [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2).

1. Determine the resource that you want to troubleshoot.


<table>
<thead>
  <tr><th>Resource</th><th>Steps</th></tr>
</thead>
<tbody>
  <tr><td>Tasks</td><td> <ol><li> On the <b>Clusters</b> page, choose the cluster. </li><li> Choose the <b>Tasks</b> tab. </li><li> Choose the task that you want to investigate. </li></ol> </td></tr>
  <tr><td>Containers</td><td> <ol><li> On the <b>Clusters</b> page, choose the cluster. </li><li> Choose the <b>Tasks</b> tab, and then choose the task. </li><li> In the <b>Containers</b> section, choose the container you want to investigate. </li></ol> </td></tr>
  <tr><td>Services and deployments</td><td> <ol><li> On the <b>Clusters</b> page, choose the cluster. </li><li> Choose the <b>Services</b> tab. </li><li> Choose the service, and then review the <b>Deployments</b> section. </li></ol> </td></tr>
  <tr><td>Task definitions</td><td> <ol><li> In the navigation pane, choose <b>Task definitions</b>. </li><li> Choose the task definition family, and then choose the revision that you want to investigate. </li></ol> </td></tr>
</tbody>
</table>


1. On the resource details page, locate the status or health reason that describes the issue.

1. Click the status reason to open the popover.

1. If available, choose **Inspect with AWS assistant**.

1. Review the explanation and suggested remediation steps that the AWS assistant provides. Apply configuration or operational changes as appropriate for your environment.

## Considerations
<a name="troubleshooting-with-Q-considerations"></a>

Consider the following when using the AWS assistant with Amazon ECS:
+ **Button availability** - The "Inspect with AWS assistant" button is only displayed for resources experiencing potential issues. This option is not available for healthy resources.
+ **Read-only operations** - The AWS assistant integration performs only read operations. It makes no mutating or write actions.
+ **Cross-region processing** - The AWS assistant may process data across AWS regions to provide AI-powered analysis. For more information about cross-region processing, see [Cross-Region processing in AWS assistant](https://docs.aws.amazon.com/assistant/latest/userguide/cross-region-processing.html).
+ ** Console only** - This integration is available only through the Console. It is not available through the AWS CLI, AWS APIs, or infrastructure as code tools.

## Learn more
<a name="troubleshooting-with-Q-learn-more"></a>

For more information about using the AWS assistant, see [Using AWS assistant](https://docs.aws.amazon.com/assistant/latest/userguide/using-assistant.html).