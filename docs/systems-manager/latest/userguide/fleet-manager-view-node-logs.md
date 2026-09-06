

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Viewing logs on managed nodes
<a name="fleet-manager-view-node-logs"></a>

You can use Fleet Manager to view log data stored on your managed nodes. For Windows managed nodes, you can view Windows event logs and copy their details from the console. To help you search events, filter Windows event logs by **Event level**, **Event ID**, **Event source**, and **Time created**. You can also view other log data using the procedure to view the file system. For more information about viewing the file system with Fleet Manager, see [Working with OS file systems using Fleet Manager](fleet-manager-file-system-management.md).

**To view Windows event logs with Fleet Manager**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Fleet Manager**.

1. Choose the button next to the managed node whose event logs you want to view.

1. Choose **View details**.

1. Choose **Tools, Windows event logs**.

1. Choose the **Log name** that contains the events you want to view.

1. Choose the button next to the **Log name** you want to view, and then select **View events**.

1. Choose the button next to the event you want to view, and then select **View event details**.

1. (Optional) Select **Copy as JSON** to copy the event details to your clipboard.