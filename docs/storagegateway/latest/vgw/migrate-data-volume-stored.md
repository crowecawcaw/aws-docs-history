

# Moving stored volumes to a new stored Volume Gateway
<a name="migrate-data-volume-stored"></a>



**To move your stored volume to a new stored Volume Gateway**

1. Stop any applications that are writing to the old stored Volume Gateway.

1. Use the following steps to create a snapshot of your volume, and then wait for the snapshot to complete.

   1. Open the Storage Gateway console at [https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/).

   1. In the navigation pane, choose **Volumes**, and then choose the volume that you want to create the snapshot from.

   1. For **Actions**, choose **Create snapshot**.

   1. In the **Create snapshot** dialog box, enter a snapshot description, and then choose **Create snapshot**.

      You can verify that the snapshot was created using the console. If data is still uploading to the volume, wait until the upload is complete before you go to the next step. To see the snapshot status and validate that none are pending, select the snapshot links on the volumes.

1. Use the following steps to stop the old stored Volume Gateway:

   1. In the navigation pane, choose **Gateways**, and then choose the old stored Volume Gateway that you want to stop. The status of the gateway is **Running**.

   1. For **Actions**, choose **Stop gateway**. Verify the ID of the gateway from the dialog box, and then choose **Stop gateway**.

      While the gateway is stopping, you might see a message that indicates the status of the gateway. When the gateway shuts down, a message and a **Start gateway** button appear in the **Details** tab. When the gateway shuts down, the status of the gateway is **Shutdown**.

   1. Shut down the VM using the hypervisor controls.

   For more information about stopping a gateway, see [Starting and Stopping a Volume Gateway](MaintenanceShutDown-common.md#start-stop-classic).

1. Detach the storage disks associated with your stored volumes from the gateway VM. This excludes the root disk of the VM.

1. Activate a new stored Volume Gateway with a new hypervisor VM image available from the Storage Gateway console at [https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/).

1. Attach the physical storage disks that you detached from the old stored Volume Gateway VM in step 5.

1. To preserve existing data on the disk, use the following steps to create stored volumes.

   1. On the Storage Gateway console, choose **Create volume**.

   1. In the **Create volume** dialog box, select the stored Volume Gateway that you created in step 5.

   1. Choose a **Disk ID** value from the list.

   1. For **Volume content**, select the **Preserve existing data on the disk** option.

   For more information about creating volumes, see [Creating a storage volume](GettingStartedCreateVolumes.md).

1. (Optional) In the **Configure CHAP authentication** wizard that appears, enter the **Initiator name**, **Initiator secret**, and **Target secret**, and then choose **Save**.

   For more information about working with Challenge-Handshake Authentication Protocol (CHAP) authentication, see [Configuring CHAP Authentication for Your iSCSI Targets](ConfiguringiSCSIClientInitiatorCHAP.md).

1. Start the application that writes to your stored volume.

1. When you have confirmed that your new stored Volume Gateway is working correctly, you can delete the old stored Volume Gateway.
**Important**  
Before you delete a gateway, be sure that no applications are currently writing to that gateway's volumes. If you delete a gateway while it is in use, data loss can occur.

   Use the following steps to delete the old stored Volume Gateway:
**Warning**  
When a gateway is deleted, there is no way to recover it.

   1. In the navigation pane, choose **Gateways**, and then choose the old stored Volume Gateway that you want to delete.

   1. For **Actions**, choose **Delete gateway**.

   1. In the confirmation dialog box that appears, select the check box to confirm your deletion. Make sure that the gateway ID listed specifies the old stored Volume Gateway that you want to delete, and then choose **Delete**.

1. Delete the old gateway VM. For information about deleting a VM, see the documentation for your hypervisor.