

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Starting an OS process on a managed node using Fleet Manager
<a name="fleet-manager-start-process"></a>

You can use Fleet Manager to start a process on a managed node.

**To start a process with Fleet Manager**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Fleet Manager**.

1. Select the link of the managed node you want to start a process on.

1. Choose **Tools, Processes**.

1. Select **Start new process**.

1. For **Process name or full path**, enter the name of the process or the full path to the executable.

1. (Optional) For **Working directory**, enter the directory path where you want the process to run.