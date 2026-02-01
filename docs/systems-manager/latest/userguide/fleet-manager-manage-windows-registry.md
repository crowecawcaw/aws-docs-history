• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Managing the Windows

registry on managed nodes

You can use Fleet Manager, a tool in AWS Systems Manager, to manage the registry on your Windows Server
managed nodes. From the Fleet Manager console you can create, copy, update, and delete
registry entries and values.

###### Important

We recommend creating a backup of the registry, or taking a snapshot of the
root Amazon Elastic Block Store (Amazon EBS) volume attached to your managed node, before you modify
the registry. Serious problems can occur if you modify the registry incorrectly.
These problems might require you to reinstall the operating system, or restore
the root volume of your node from a snapshot. AWS doesn't guarantee that these
problems can be solved. Modify the registry at your own risk. You're responsible
for all registry changes, and ensuring you have backups.

## Create a Windows registry key

or entry

###### To create a Windows registry key with Fleet Manager

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Fleet Manager**.
3. Choose the button next to the managed node you want to create a
   registry key on.
4. Choose **View details**.
5. Choose **Tools, Windows registry**.
6. Choose the hive you want to create a new registry key in by selecting
   the **Registry name**.
7. Choose **Create, Create registry key**.
8. Choose the button next to the registry entry you want to create a new
   key in.
9. Choose **Create registry key**.
10. Enter a value for the **Name** of the new registry
    key, and select **Submit**.

###### To create a Windows registry entry with Fleet Manager

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Fleet Manager**.
3. Choose the button next to the instance you want to create a registry
   entry on.
4. Choose **View details**.
5. Choose **Tools, Windows registry**.
6. Choose the hive, and subsequent registry key you want to create a new
   registry entry in by selecting the **Registry
   name**.
7. Choose **Create, Create registry entry**.
8. Enter a value for the **Name** of the new registry
   entry.
9. Choose the **Type** of value you want to create for
   the registry entry. For more information about registry value types, see
   [Registry value types](https://docs.microsoft.com/en-us/windows/win32/sysinfo/registry-value-types "https://docs.microsoft.com/en-us/windows/win32/sysinfo/registry-value-types").
10. Enter a value for the **Value** of the new registry
    entry.

## Update a Windows registry

entry

###### To update a Windows registry entry with Fleet Manager

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Fleet Manager**.
3. Choose the button next to the managed node you want to update a
   registry entry on.
4. Choose **View details**.
5. Choose **Tools, Windows registry**.
6. Choose the hive, and subsequent registry key you want to update by
   selecting the **Registry name**.
7. Choose the button next to the registry entry you want to
   update.
8. Choose **Actions, Update registry entry**.
9. Enter the new value for the **Value** of the registry
   entry.
10. Choose **Update**.

## Delete a Windows registry entry

or key

###### To delete a Windows registry key with Fleet Manager

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Fleet Manager**.
3. Choose the button next to the managed node you want to delete a
   registry key on.
4. Choose **Tools, Windows registry**.
5. Choose the hive, and subsequent registry key you want to delete by
   selecting the **Registry name**.
6. Choose the button next to the registry key you want to delete.
7. Choose **Actions, Delete registry key**.

###### To delete a Windows registry entry with Fleet Manager

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Fleet Manager**.
3. Choose the button next to the managed node you want to delete a
   registry entry on.
4. Choose **View details**.
5. Choose **Tools, Windows registry**.
6. Choose the hive, and subsequent registry key containing the entry you
   want to delete by selecting the **Registry
   name**.
7. Choose the button next to the registry entry you want to
   delete.
8. Choose **Actions, Delete registry entry**.
