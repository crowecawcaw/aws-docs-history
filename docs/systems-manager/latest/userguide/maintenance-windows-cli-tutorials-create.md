

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Tutorial: Create and configure a maintenance window using the AWS CLI
<a name="maintenance-windows-cli-tutorials-create"></a>

This tutorial demonstrates how to use the AWS Command Line Interface (AWS CLI) to create and configure a maintenance window, its targets, and its tasks. The main path through the tutorial consists of simple steps. You create a single maintenance window, identify a single target, and set up a simple task for the maintenance window to run. Along the way, we provide information you can use to try more complicated scenarios.

As you follow the steps in this tutorial, replace the values in italicized {{red}} text with your own options and IDs. For example, replace the maintenance window ID {{mw-0c50858d01EXAMPLE}} and the instance ID {{i-02573cafcfEXAMPLE}} with IDs of resources you create.

**Topics**
+ [Step 1: Create the maintenance window using the AWS CLI](mw-cli-tutorial-create-mw.md)
+ [Step 2: Register a target node with the maintenance window using the AWS CLI](mw-cli-tutorial-targets.md)
+ [Step 3: Register a task with the maintenance window using the AWS CLI](mw-cli-tutorial-tasks.md)