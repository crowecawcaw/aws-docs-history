# Shutting Down Your Gateway VM

You might need to shutdown or reboot your VM for maintenance, such as when applying a
patch to your hypervisor. Before you shutdown the VM, you must first stop the gateway.
Although this section focuses on starting and stopping your gateway using the Storage Gateway
Management Console, you can also start and stop your gateway by using your VM local console or
Storage Gateway API. When you power on your VM, remember to restart your gateway.

###### Important

If you stop and start an Amazon EC2 gateway that uses ephemeral storage, the gateway will
be permanently offline. This happens because the physical storage disk is replaced.
There is no work-around for this issue. The only resolution is to delete the gateway and
activate a new one on a new EC2 instance.

###### Note

If you stop your gateway while your backup software is writing or reading from a tape,
the write or read task might not succeed. Before you stop your gateway, you should check
your backup software and the backup schedule for any tasks in progress.

- Gateway VM local console—see [Logging in to the Tape Gateway local
  console](LocalConsole-login-common.md "LocalConsole-login-common.md").
- Storage Gateway API-—see [ShutdownGateway](../APIReference/API_ShutdownGateway.md "../APIReference/API_ShutdownGateway.md")

## Starting and Stopping a Tape Gateway

###### To stop a Tape Gateway

1. Open the Storage Gateway console at
   [https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/ "https://console.aws.amazon.com/storagegateway/").
2. In the navigation pane, choose **Gateways**, and then choose
   the gateway to stop. The status of the gateway is
   **Running**.
3. For **Actions**, choose **Stop gateway** and
   verify the id of the gateway from the dialog box, and then choose **Stop
   gateway**.

While the gateway is stopping, you might see a message that indicates the
status of the gateway. When the gateway shuts down, a message and a
**Start gateway** button appears in the
**Details** tab.

When you stop your gateway, the storage resources will not be accessible until you
start your storage. If the gateway was uploading data when it was stopped, the upload
will resume when you start the gateway.

###### To start a Tape Gateway

1. Open the Storage Gateway console at
   [https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/ "https://console.aws.amazon.com/storagegateway/").
2. In the navigation pane, choose **Gateways** and then choose
   the gateway to start. The status of the gateway is
   **Shutdown**.
3. Choose **Details**. and then choose **Start
   gateway**.
