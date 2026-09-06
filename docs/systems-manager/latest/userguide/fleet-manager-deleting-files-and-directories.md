

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Deleting OS files and directories using Fleet Manager
<a name="fleet-manager-deleting-files-and-directories"></a>

You can use Fleet Manager to delete files and directories on a managed node in your account.

**To delete files or directories using Fleet Manager**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Fleet Manager**.

1. Select the link of the managed node with the files or directories you want to delete.

1. Choose **Tools, File system**.

1. To delete a file, select the **File name** of the directory that contains the file you want to delete. To delete a directory, choose the button next to the directory that you want to delete and then proceed to step 7.

1. Choose the button next to the file with the content you want to delete.

1. Choose **Actions, Delete**.