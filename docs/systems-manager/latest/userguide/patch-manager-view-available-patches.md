

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Viewing available patches
<a name="patch-manager-view-available-patches"></a>

With Patch Manager, you can view all available patches for a specified operating system and, optionally, a specific operating system version.

**Tip**  
To generate a list of available patches and save them to a file, you can use the [describe-available-patches](https://docs.aws.amazon.com/cli/latest/reference/ssm/describe-available-patches.html) command and specify your preferred [output](https://docs.aws.amazon.com/cli/latest/reference/ssm/cli-usage-output.html).

**To view available patches**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Patch Manager**.

1. Choose the **Patches** tab.

   -or-

   If you are accessing Patch Manager for the first time in the current AWS Region, choose **Start with an overview**, and then choose the **Patches** tab.
**Note**  
For Windows Server, the **Patches** tab displays updates that are available from Windows Server Update Service (WSUS).

1. For **Operating system**, choose the operating system for which you want to view available patches, such as `Windows` or `Amazon Linux`.

1. (Optional) For **Product**, choose an OS version, such as `WindowsServer2019` or `AmazonLinux2018.03`.

1. (Optional) To add or remove information columns for your results, choose the configure button (![The icon to view configuration settings.](http://docs.aws.amazon.com/systems-manager/latest/userguide/images/configure-button.png)) at the top right of the **Patches** list. (By default, the **Patches** tab displays columns for only some of the available patch metadata.)

   For information about the types of metadata you can add to your view, see [Patch](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_Patch.html) in the *AWS Systems Manager API Reference*.