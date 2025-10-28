# Modify the gateway maintenance

window schedule

If maintenance updates are turned on, your gateway automatically applies these updates
according the maintenance window schedule. Urgent updates will sometimes be applied
during your configured maintenance window, regardless of the maintenance updates
setting.

###### Note

The following procedure describes how to modify the maintenance window schedule
using the Storage Gateway console. To change this setting programmatically using the API,
see [UpdateMaintenanceStartTime](https://amazonaws.com/storagegateway/latest/APIReference/API_UpdateMaintenanceStartTime.html "https://amazonaws.com/storagegateway/latest/APIReference/API_UpdateMaintenanceStartTime.html") in the _Storage Gateway API
Reference_.

###### To modify the maintenance window schedule using the Storage Gateway console:

1. Open the Storage Gateway console at
   [https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/ "https://console.aws.amazon.com/storagegateway/").
2. On the navigation pane, choose **Gateways**, and then choose
   the gateway for which you want to configure maintenance updates.
3. Choose **Actions**, and then choose **Edit
   maintenance settings**.
4. Under **Maintenance window start time**, do the
   following:
   1. For **Schedule**, choose **Weekly**
      or **Monthly** to set the maintenance window
      cadence.
   2. If you choose **Weekly**, modify the values for
      **Day of the week** and **Time**
      to set the specific point during each week when the maintenance window
      will begin.

   If you choose **Monthly**, modify the values for
   **Day of the month** and **Time**
   to set the specific point during each month when the maintenance window
   will begin.

   ###### Note

   The maximum value that can be set for day of the month is 28. It
   is not possible to set the maintenance schedule to start on days 29
   through 31.

   If you receive an error while configuring this setting, it might
   mean that your gateway software is out of date. Considering updating
   your gateway manually first, and then attempt to configure the
   maintenance window schedule again.

5. Choose **Save changes** when finished.
   You can verify the updated settings on the **Details** tab for the
   selected gateway in the Storage Gateway console.
