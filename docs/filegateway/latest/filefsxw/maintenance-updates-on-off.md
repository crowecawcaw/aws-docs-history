Amazon FSx File Gateway is no longer available to new customers. Existing
customers of FSx File Gateway can continue to use the service normally. For capabilities
similar to FSx File Gateway, visit [this blog post](https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/ "https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/").

# Turn maintenance updates on or off

When maintenance updates are turned on, your gateway automatically applies these
updates according to the configured maintenance window schedule. For more information,
see [Modify the gateway maintenance window schedule](MaintenanceManagingUpdate-common.md#configure-maintenance-window-schedule "MaintenanceManagingUpdate-common.md#configure-maintenance-window-schedule").

If maintenance updates are turned off, the gateway will not apply these updates
automatically, but you can always apply them manually using the Storage Gateway console, API, or
CLI. Urgent updates will sometimes be applied during your configured maintenance window,
regardless of this setting.

###### Note

The following procedure describes how to turn gateway updates on or off using the
Storage Gateway console. To change this setting programmatically using the API, see [UpdateMaintenanceStartTime](../../../storagegateway/latest/APIReference/API_UpdateMaintenanceStartTime.md "../../../storagegateway/latest/APIReference/API_UpdateMaintenanceStartTime.md") in the _Storage Gateway API
Reference_.

###### To turn maintenance updates on or off using the Storage Gateway console:

1. Open the Storage Gateway console at
   [https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/ "https://console.aws.amazon.com/storagegateway/").
2. On the navigation pane, choose **Gateways**, and then choose
   the gateway for which you want to configure maintenance updates.
3. Choose **Actions**, and then choose **Edit
   maintenance settings**.
4. For **Maintenance updates**, select **On**
   or **Off**.
5. Choose **Save changes** when finished.
   You can verify the updated setting on the **Details** tab for the
   selected gateway in the Storage Gateway console.
