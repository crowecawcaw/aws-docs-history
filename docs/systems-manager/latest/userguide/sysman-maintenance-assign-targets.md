

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Assign targets to a maintenance window using the console
<a name="sysman-maintenance-assign-targets"></a>

In this procedure, you register a target with a maintenance window. In other words, you specify which resources the maintenance window performs actions on.

**Note**  
If a single maintenance window task is registered with multiple targets, its task invocations occur sequentially and not in parallel. If your task must run on multiple targets at the same time, register a task for each target individually and assign each task the same priority level.

**To assign targets to a maintenance window using the console**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Maintenance Windows**. 

1. In the list of maintenance windows, choose the maintenance window to add targets to.

1. Choose **Actions**, and then choose **Register targets**.

1. (Optional) For **Target name**, enter a name for the targets.

1. (Optional) For **Description**, enter a description.

1. (Optional) For **Owner information**, specify information to include in any Amazon EventBridge event raised while running tasks for these targets in this maintenance window.

   For information about using EventBridge to monitor Systems Manager events, see [Monitoring Systems Manager events with Amazon EventBridge](monitoring-eventbridge-events.md).

1. In the **Targets** area, choose one of the options described in the following table.


<table>
<thead>
  <tr><th>Option</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td><b>Specify instance tags</b></td><td>For the <b>Specify instance tags</b> boxes, specify one or more tag keys and (optional) values that have been or will be added to managed nodes in your account. When the maintenance window runs, it attempts to perform tasks on all of the managed nodes to which these tags have been added.<br />If you specify more than one tag key, a node must be tagged with <i>all</i> the tag keys and values you specify to be included in the target group.</td></tr>
  <tr><td><b>Choose instances manually</b></td><td>From the list, select the box for each node that you want to include in the maintenance window target. <br />The list includes all nodes in your account that are configured for use with Systems Manager.<br />If a managed node you expect to see isn't listed, see <a href="fleet-manager-troubleshooting-managed-nodes.md">Troubleshooting managed node availability</a> for troubleshooting tips.<br />For edge devices and on-premises servers and virtual machines (VMs), see <a href="systems-manager-hybrid-multicloud.md">Managing nodes in hybrid and multicloud environments with Systems Manager</a></td></tr>
  <tr><td><b>Choose a resource group</b></td><td>For <b>Resource group</b>, choose the name of an existing resource group in your account from the list.<br />For information about creating and working with resource groups, see the following topics:<ul><li> <a href="https://docs.aws.amazon.com/ARG/latest/userguide/resource-groups.html">What are resource groups?</a> in the <i>AWS Resource Groups User Guide</i> </li><li> <a href="https://aws.amazon.com/blogs/aws/resource-groups-and-tagging/">Resource Groups and Tagging for AWS</a> in the <i>AWS News Blog</i> </li></ul><br />(Optional) For <b>Resource types</b>, select up to five available resource types, or choose <b>All resource types</b>.<br />If the tasks you assign to the maintenance window don't act on one of the resource types you added to the target, the system might report an error. Tasks for which a supported resource type is found continue to run despite these errors.<br />For example, suppose you add the following resource types to this target:<ul><li> <code>AWS::S3::Bucket</code> </li><li> <code>AWS::DynamoDB::Table</code> </li><li> <code>AWS::EC2::Instance</code> </li></ul><br />But later, when you add tasks to the maintenance window, you include only tasks that perform actions on nodes, such as applying a patch baseline or rebooting a node. In the maintenance window log, an error might be reported for no Amazon Simple Storage Service (Amazon S3) buckets or Amazon DynamoDB tables being found. However, the maintenance window still runs tasks on the nodes in your resource group.</td></tr>
</tbody>
</table>


1. Choose **Register target**.

If you want to assign more targets to this maintenance window, choose the **Targets** tab, and then choose **Register target**. With this option, you can choose a different means of targeting. For example, if you previously targeted nodes by node ID, you can register new targets and target nodes by specifying tags applied to managed nodes or choosing resource types from a resource group.