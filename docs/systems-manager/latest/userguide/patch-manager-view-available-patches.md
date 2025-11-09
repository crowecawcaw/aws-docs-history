AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Viewing available

patches

With Patch Manager, a tool in AWS Systems Manager, you can view all available patches for a
specified operating system and, optionally, a specific operating system
version.

###### Tip

To generate a list of available patches and save them to a file, you can use
the [describe-available-patches](../../../cli/latest/reference/ssm/describe-available-patches.md "../../../cli/latest/reference/ssm/describe-available-patches.md") command and specify your preferred
[output](../../../cli/latest/reference/ssm/cli-usage-output.md "../../../cli/latest/reference/ssm/cli-usage-output.md").

###### To view available patches

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Patch Manager**.
3. Choose the **Patches** tab.

-or-

If you are accessing Patch Manager for the first time in the current
AWS Region, choose **Start with an overview**, and then
choose the **Patches** tab.

###### Note

For Windows Server, the **Patches** tab displays updates
that are available from Windows Server Update Service (WSUS). 4. For **Operating system**, choose the operating system for
which you want to view available patches, such as `Windows` or
`Amazon Linux`. 5. (Optional) For **Product**, choose an OS version, such as
`WindowsServer2019` or
`AmazonLinux2018.03`. 6. (Optional) To add or remove information columns for your results, choose
the configure button (
![The icon to view configuration settings.](images/configure-button.png)
) at the top right of the **Patches**
list. (By default, the **Patches** tab displays columns for
only some of the available patch metadata.)

For information about the types of metadata you can add to your view, see
[Patch](../APIReference/API_Patch.md "../APIReference/API_Patch.md")
in the _AWS Systems Manager API Reference_.
