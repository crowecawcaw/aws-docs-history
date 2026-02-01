• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Assign targets to a maintenance

window using the console

In this procedure, you register a target with a maintenance window. In other
words, you specify which resources the maintenance window performs actions
on.

###### Note

If a single maintenance window task is registered with multiple targets, its
task invocations occur sequentially and not in parallel. If your task must run
on multiple targets at the same time, register a task for each target
individually and assign each task the same priority level.

###### To assign targets to a maintenance window using the console

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Maintenance Windows**.
3. In the list of maintenance windows, choose the maintenance window to add
   targets to.
4. Choose **Actions**, and then choose **Register
   targets**.
5. (Optional) For **Target name**, enter a name for the
   targets.
6. (Optional) For **Description**, enter a
   description.
7. (Optional) For **Owner information**, specify information
   to include in any Amazon EventBridge event raised while running tasks for these
   targets in this maintenance window.

For information about using EventBridge to monitor Systems Manager events, see [Monitoring Systems Manager events with
Amazon EventBridge](monitoring-eventbridge-events.md "monitoring-eventbridge-events.md"). 8. In the **Targets** area, choose one of the options
described in the following table.

| Option                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Specify instance<br>tags**     | For the **Specify instance tags**<br>boxes, specify one or more tag keys and (optional)<br>values that have been or will be added to managed nodes<br>in your account. When the maintenance window runs, it<br>attempts to perform tasks on all of the managed nodes to<br>which these tags have been added.<br>If you specify more than one tag key, a node must be<br>tagged with \*all<br>• the<br>tag keys and values you specify to be included in the<br>target group.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **Choose instances<br>manually** | From the list, select the box for each node that you<br>want to include in the maintenance window target.<br>The list includes all nodes in your account that are<br>configured for use with Systems Manager.<br>If a managed node you expect to see isn't listed, see [Troubleshooting managed<br>node availability](fleet-manager-troubleshooting-managed-nodes.md "fleet-manager-troubleshooting-managed-nodes.md") for troubleshooting<br>tips. For edge devices and<br>on-premises servers and virtual machines (VMs), see<br>[Managing nodes in hybrid and multicloud<br>environments with Systems Manager](systems-manager-hybrid-multicloud.md "systems-manager-hybrid-multicloud.md")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **Choose a resource<br>group**   | For **Resource group**, choose the<br>name of an existing resource group in your account from<br>the list.<br>For information about creating and working with<br>resource groups, see the following topics:<br>• [What are resource groups?](../../../ARG/latest/userguide/resource-groups.md "../../../ARG/latest/userguide/resource-groups.md") in the<br>_AWS Resource Groups User Guide_<br>• [Resource<br>Groups and Tagging for AWS](https://aws.amazon.com/blogs/aws/resource-groups-and-tagging/ "https://aws.amazon.com/blogs/aws/resource-groups-and-tagging/") in the<br>_AWS News<br>Blog_<br>(Optional) For **Resource types**,<br>select up to five available resource types, or choose<br>**All resource types**.<br>If the tasks you assign to the maintenance window<br>don't act on one of the resource types you added to the<br>target, the system might report an error. Tasks for<br>which a supported resource type is found continue to run<br>despite these errors.<br>For example, suppose you add the following resource<br>types to this target:<br>• `AWS::S3::Bucket`<br>• `AWS::DynamoDB::Table`<br>• `AWS::EC2::Instance`<br>But later, when you add tasks to the maintenance<br>window, you include only tasks that perform actions on<br>nodes, such as applying a patch baseline or rebooting a<br>node. In the maintenance window log, an error might be<br>reported for no Amazon Simple Storage Service (Amazon S3) buckets or Amazon DynamoDB<br>tables being found. However, the maintenance window<br>still runs tasks on the nodes in your resource<br>group. |

9. Choose **Register target**.
   If you want to assign more targets to this maintenance window, choose the
   **Targets** tab, and then choose **Register
   target**. With this option, you can choose a different means of
   targeting. For example, if you previously targeted nodes by node ID, you can
   register new targets and target nodes by specifying tags applied to managed nodes or
   choosing resource types from a resource group.
