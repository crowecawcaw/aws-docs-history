# Turn maintenance updates on or off

When maintenance updates are turned on, your gateway automatically applies these
updates according to the configured maintenance window schedule. For more information,
see .

If maintenance updates are turned off, the gateway will not apply these updates
automatically, but you can always apply them manually using the Storage Gateway console, API, or
CLI. Urgent updates will sometimes be applied during your configured maintenance window,
regardless of this setting.

###### Note

The following procedure describes how to turn gateway updates on or off using the
Storage Gateway console. To change this setting programmatically using the API, see [UpdateMaintenanceStartTime](../APIReference/API_UpdateMaintenanceStartTime.md "../APIReference/API_UpdateMaintenanceStartTime.md") in the _Storage Gateway API
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
