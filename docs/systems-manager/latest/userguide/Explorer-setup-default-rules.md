

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Understanding default EventBridge rules created by Integrated Setup
<a name="Explorer-setup-default-rules"></a>

During the integrated setup process for Explorer and OpsCenter, you can choose to enable several default rules that are based on events detected by Amazon EventBridge. When these events are detected, the system automatically creates OpsItems in AWS Systems Manager OpsCenter. 

For example, the rule `SSMOpsItems-Autoscaling-instance-termination-failure` results in an OpsItem being created when the termination of an EC2 auto scaling instance fails.

The rule `SSMOpsItems-SSM-maintenance-window-execution-failed` results in an OpsItem being created when a Systems Manager maintenace window fails to complete successfully.

For setup instructions and descriptions of all the EventBridge rules you can enable during the setup process, see [Set up OpsCenter](OpsCenter-setup.md).

If you don't want EventBridge to create OpsItems for these events, you can choose not to enable this option in Integrated Setup. If you prefer, you can specify OpsCenter as the target of specific EventBridge events. For more information, see [Configure EventBridge rules to create OpsItems](OpsCenter-automatically-create-OpsItems-2.md). 

You can disable a default rule or change its category and severity level in the OpsCenter **Settings** page by choosing **OpsCenter, Settings**, and then choosing **Edit** in the **OpsItem rules** area. 

You can also edit the category or severity assigned to an individual OpsItem created from these rules in the Systems Manager console. For information, see [Editing an OpsItem](OpsCenter-working-with-OpsItems-editing-details.md). 

![Default rules for creating OpsItems in Systems Manager Explorer](http://docs.aws.amazon.com/systems-manager/latest/userguide/images/explorer-default-rules.png)
