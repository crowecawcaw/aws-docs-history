# Moving your data to a new gateway

You can move data between gateways as your data and performance needs grow, or if you
receive an AWS notification to migrate your gateway. The following are some reasons for
doing this:

- Move your data to better host platforms or newer Amazon EC2 instances.
- Refresh the underlying hardware for your server.
  The steps that you follow to move your data to a new gateway depend on the gateway type
  that you have.

###### Important

Data can only be moved between the same gateway types.

The following migration instructions can only be used for gateway appliances running version 2.x. You can't use them
to migrate gateway appliances running lower versions.

## Moving stored volumes to a new stored

Volume Gateway

###### To move your stored volume to a new stored Volume Gateway

1. Stop any applications that are writing to the old stored
   Volume Gateway.
2. Use the following steps to create a snapshot of your volume, and then wait for
   the snapshot to complete.
   1. Open the Storage Gateway console at
      [https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/ "https://console.aws.amazon.com/storagegateway/").
   2. In the navigation pane, choose **Volumes**, and then
      choose the volume that you want to create the snapshot from.
   3. For **Actions**, choose **Create
      snapshot**.
   4. In the **Create snapshot** dialog box, enter a
      snapshot description, and then choose **Create
      snapshot**.

   You can verify that the snapshot was created using the console. If
   data is still uploading to the volume, wait until the upload is complete
   before you go to the next step. To see the snapshot status and validate
   that none are pending, select the snapshot links on the volumes.

3. Use the following steps to stop the old stored Volume Gateway:
   1. In the navigation pane, choose **Gateways**, and then
      choose the old stored Volume Gateway that you want to stop. The status
      of the gateway is **Running**.
   2. For **Actions**, choose **Stop
      gateway**. Verify the ID of the gateway from the dialog
      box, and then choose **Stop gateway**.

   While the gateway is stopping, you might see a message that indicates
   the status of the gateway. When the gateway shuts down, a message and a
   **Start gateway** button appear in the
   **Details** tab. When the gateway shuts down, the
   status of the gateway is **Shutdown**. 3. Shut down the VM using the hypervisor controls.For more information about stopping a gateway, see [Starting and Stopping a Volume Gateway](MaintenanceShutDown-common.md#start-stop-classic "MaintenanceShutDown-common.md#start-stop-classic").

4. Detach the storage disks associated with your stored volumes from the gateway
   VM. This excludes the root disk of the VM.
5. Activate a new stored Volume Gateway with a new hypervisor VM image available
   from the Storage Gateway console at [https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/ "https://console.aws.amazon.com/storagegateway/").
6. Attach the physical storage disks that you detached from the old stored
   Volume Gateway VM in step 5.
7. To preserve existing data on the disk, use the following steps to create
   stored volumes.
   1. On the Storage Gateway console, choose **Create
      volume**.
   2. In the **Create volume** dialog box, select the
      stored Volume Gateway that you created in step 5.
   3. Choose a **Disk ID** value from the list.
   4. For **Volume content**, select the **Preserve
      existing data on the disk** option.For more information about creating volumes, see [Creating a storage volume](GettingStartedCreateVolumes.md "GettingStartedCreateVolumes.md").

8. (Optional) In the **Configure CHAP authentication** wizard
   that appears, enter the **Initiator name**, **Initiator
   secret**, and **Target secret**, and then choose
   **Save**.

For more information about working with Challenge-Handshake Authentication
Protocol (CHAP) authentication, see [Configuring CHAP Authentication
for Your iSCSI Targets](ConfiguringiSCSIClientInitiatorCHAP.md "ConfiguringiSCSIClientInitiatorCHAP.md"). 9. Start the application that writes to your stored volume. 10. When you have confirmed that your new stored Volume Gateway is working
correctly, you can delete the old stored Volume Gateway.

###### Important

Before you delete a gateway, be sure that no applications are currently
writing to that gateway's volumes. If you delete a gateway while it is in
use, data loss can occur.

Use the following steps to delete the old stored Volume Gateway:

###### Warning

When a gateway is deleted, there is no way to recover it.

    1. In the navigation pane, choose **Gateways**, and then
     choose the old stored Volume Gateway that you want to delete.
    2. For **Actions**, choose **Delete
     gateway**.
    3. In the confirmation dialog box that appears, select the check box to
     confirm your deletion. Make sure that the gateway ID listed specifies
     the old stored Volume Gateway that you want to delete, and then choose
     **Delete**.

11. Delete the old gateway VM. For information about deleting a VM, see the
    documentation for your hypervisor.

## Moving cached volumes to a new gateway

virtual machine

###### To move your cached volumes to a new cached Volume Gateway virtual machine

(VM)

1. Stop any applications that are writing to the old cached
   Volume Gateway.
2. Use the following steps to update the gateway to the latest version
   1. Open the Storage Gateway console at
      [https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/ "https://console.aws.amazon.com/storagegateway/").
   2. In the navigation pane, choose **Gateways**, and then choose the old cached Volume Gateway that you want to migrate.
   3. Click **Update Now** if available. If not, your gateway is already on the latest version.

3. Verify that the `CachePercentDirty` metric on the **Monitoring** tab for
   the existing Cached Gateway is `0`.
4. Unmount or disconnect iSCSI volumes from any clients that are using them. This
   helps keep data on those volumes consistent by preventing clients from changing
   or adding data to those volumes.
5. Use the following steps to create a snapshot of your volume, and then wait for
   the snapshot to complete.
   1. Open the Storage Gateway console at
      [https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/ "https://console.aws.amazon.com/storagegateway/").
   2. In the navigation pane, choose **Volumes**, and then
      choose the volume that you want to create the snapshot from.
   3. For **Actions**, choose **Create
      EBS snapshot**.
   4. In the **Create snapshot** dialog box, enter a
      snapshot description, and then choose **Create
      snapshot**.

   You can verify that the snapshot was created using the console. If
   data is still uploading to the volume, wait until the upload is complete
   before you go to the next step. To see the snapshot status and validate
   that none are pending, select the snapshot links on the volumes.

   For more information about checking volume status in the console, see
   [Understanding Volume Statuses and
   Transitions](StorageVolumeStatuses.md "StorageVolumeStatuses.md"). For information about
   cached volume status, see [Understanding Cached Volume Status
   Transitions](StorageVolumeStatuses.md#CachedVolumeStatusTransition "StorageVolumeStatuses.md#CachedVolumeStatusTransition") .

6. Use the following steps to stop the old cached Volume Gateway:
   1. In the navigation pane, choose **Gateways**, and then
      choose the old cached Volume Gateway that you want to stop.
   2. For **Actions**, choose **Stop
      gateway**. Verify the ID of the gateway from the dialog
      box, and then choose **Stop gateway**. Make a note of
      the gateway ID, as it is needed in a later step.

   While the old gateway is stopping, you might see a message that
   indicates the status of the gateway. When the old gateway shuts down, a
   message and a **Start gateway** button appear in the
   **Details** tab. When the gateway shuts down, the
   status of the gateway is **Shutdown**. 3. Shut down the old VM using the hypervisor controls. For more
   information about shutting down an Amazon EC2 instance, see [Stopping and starting your instances](../../../AWSEC2/latest/WindowsGuide/Stop_Start.md#starting-stopping-instances "../../../AWSEC2/latest/WindowsGuide/Stop_Start.md#starting-stopping-instances") in the
   _Amazon EC2 User Guide_. For more information about
   shutting down a KVM, VMware, or Hyper-V VM, see your hypervisor
   documentation.For more information about stopping a gateway, see [Starting and Stopping a Volume Gateway](MaintenanceShutDown-common.md#start-stop-classic "MaintenanceShutDown-common.md#start-stop-classic").

7. Detach all disks, including the root disk, cache disks, and upload buffer
   disks, from the old gateway VM.

###### Note

Make a note of the root disk's volume ID, as well as the gateway ID
associated with that root disk. You use this disk in later steps.

If you are using an Amazon EC2 instance as the VM for your cached Volume Gateway,
see [Detaching an Amazon EBS
volume from a Linux instance](../../../AWSEC2/latest/UserGuide/ebs-detaching-volume.md "../../../AWSEC2/latest/UserGuide/ebs-detaching-volume.md") in the
_Amazon EC2 User Guide_. For information about detaching disks
from a KVM, VMware, or Hyper-V VM, see the documentation for your
hypervisor. 8. Create a new Storage Gateway hypervisor VM instance, but don't activate it as
a gateway. For more information about creating a new Storage Gateway hypervisor
VM, see [Set up a Volume Gateway](create-volume-gateway.md#set-up-gateway-volume "create-volume-gateway.md#set-up-gateway-volume"). This new gateway will assume the
identity of the old gateway.

###### Note

Do not add disks for cache or upload buffer to the new VM. Your new VM
will use the same cache disks and upload buffer disks that were used by the
old VM. 9. Your new Storage Gateway hypervisor VM instance should use the same network
configuration as the old VM. The default network configuration for the gateway
is Dynamic Host Configuration Protocol (DHCP). With DHCP, your gateway is
automatically assigned an IP address.

If you need to manually configure a static IP address for your new VM, see
[Configuring Your Gateway
Network](MaintenanceConfiguringStaticIP-common.md "MaintenanceConfiguringStaticIP-common.md") for more details. If
your gateway must use a Socket Secure version 5 (SOCKS5) proxy to connect to the
internet, see [Configuring a SOCKS5 proxy for your
on-premises gateway](MaintenanceRoutingProxy-common.md "MaintenanceRoutingProxy-common.md") for more details. 10. Start the new VM. 11. Attach the disks that you detached from the old cached Volume Gateway VM in
step 7, to the new cached Volume Gateway. Attach them in the same order to the
new gateway VM as they are on the old gateway VM.

All disks must make the transition unchanged. Do not change volume sizes, as
that will cause metadata to become inconsistent. 12. Initiate the gateway migration process by either connecting to the new gateway VM’s local console,
or making web requests to the new gateway VM's IP address (described below).

    1. To use the local console, select the option for **Migrate Gateway** and provide
     your existing gateway ID when prompted. You will be provided prompts to copy previously applied
     settings on old gateway to the new gateway. You may choose to apply them or manually configure them later.
     See [Accessing
     the Gateway Local Console](accessing-local-console.md "accessing-local-console.md").
    2. Alternatively, you can initiate the gateway migration process by connecting to the new VM with a URL
     that uses the following format.



    ```
    http://`your-VM-IP-address`/migrate?gatewayId=`your-gateway-ID`
    ```

    You can re-use the same IP address for the new gateway VM as you used for the
     old gateway VM. Your URL should look similar to the example following.



    ```
    http://198.51.100.123/migrate?gatewayId=sgw-12345678
    ```

    Use this URL from a browser, or from the command line using `curl`,
     to initiate the migration process.


    When the gateway migration process is successfully completed, you will see
     a message confirming successful migration.

13. Detach the old gateway's root disk, whose volume ID you noted in step
14.
15. Start the gateway.

Use the following steps to start the new cached Volume Gateway:

    1. Open the Storage Gateway console at
     [https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/ "https://console.aws.amazon.com/storagegateway/").
    2. In the navigation pane, choose **Gateways** and then
     choose the new gateway you want to start. The status of the gateway is
     **Shutdown**.
    3. Choose **Details**, and then choose **Start
     gateway**.For more information about starting a gateway, see [Starting and Stopping a Volume Gateway](MaintenanceShutDown-common.md#start-stop-classic "MaintenanceShutDown-common.md#start-stop-classic").

15. Your volumes should now be available to your applications through the new gateway VM's network interfaces.
    The migration success message includes details about the updated mapping between each volume and the new
    gateway’s network interface. For more information about the IP address associated with each network interface,
    visit the main page of the gateway’s local console. See [Accessing
    the Gateway Local Console](accessing-local-console.md "accessing-local-console.md").
16. Confirm that your volumes are available, and delete the old gateway VM. For
    information about deleting a VM, see the documentation for your
    hypervisor.
