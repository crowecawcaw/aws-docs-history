

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Terminating an OS process using Fleet Manager
<a name="fleet-manager-terminate-process"></a>

**To terminate an OS process using Fleet Manager**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Fleet Manager**.

1. Select the link of the managed node you want to start a process on.

1. Choose **Tools, Processes**.

1. Choose the button next to the process you want to terminate.

1. Choose **Actions, Terminate process** or **Actions, Terminate process tree**. 
**Note**  
Terminating a process tree also terminates all processes and applications using that process.