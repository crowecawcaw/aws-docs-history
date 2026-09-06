

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Tailing OS files using Fleet Manager
<a name="fleet-manager-tailing-os-files"></a>

You can use Fleet Manager to tail a file on a managed node.

**To tail OS files with Fleet Manager**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Fleet Manager**.

1. Select the link of the managed node with the files you want to tail.

1. Choose **Tools, File system**.

1. Select the **File name** of the directory that contains the file you want to tail.

1. Choose the button next to the file whose content you want to tail.

1. Choose **Actions, Tail file**.