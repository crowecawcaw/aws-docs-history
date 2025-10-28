# Creating a recovery snapshot

The following procedure shows you how to create a recovery snapshot from a volume
recovery point for a gateway, and where to find that snapshot in the Storage Gateway console
after you create it. You can take recovery snapshots on a one time, ad hoc basis or you
can set up a snapshot schedule to take recurring snapshots of the volume at regular
intervals that you specify.

###### To create and use a recovery snapshot of a volume from an existing

gateway

1. Open the Storage Gateway console at
   [https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/ "https://console.aws.amazon.com/storagegateway/").
2. In the navigation pane on the left side of the console page, choose
   **Gateways**.
3. Choose the gateway for which you want to create a snapshot, and then choose
   the **Details** tab.

The **Details** tab displays a recovery snapshot message for
the selected gateway. 4. Choose **Create recovery snapshot** to open the
**Create recovery snapshot** dialog box. 5. From the list of volumes that appears, choose the volume that you want to
recover, and then choose **Create snapshots**.

Storage Gateway initiates the snapshot process for the specified volume. When the
snapshot process is complete, you can find the snapshot listed in the
**Snapshots** column when viewing the volume on the
**Volumes** page of the Storage Gateway console.
