# Moving Your Volumes to a Different

Gateway

As your data and performance needs grow, you might want to move your volumes to a
different Volume Gateway. To do so, you can detach and attach a volume by using the
Storage Gateway console or API.

By detaching and attaching a volume, you can do the following:

- Move your volumes to better host platforms or newer Amazon EC2 instances.
- Refresh the underlying hardware for your server.
- Move your volumes between hypervisor types.
  When you detach a volume, your gateway uploads and stores the volume data and metadata
  to the Storage Gateway service in AWS. You can easily attach a detached volume to a gateway on
  any supported host platform later.

###### Note

A detached volume is billed at the standard volume storage rate until you delete
it. For information about how to reduce your bill, see [Reducing the amount of billed storage on a volume](best-practices.md#reduce-bill-volume "best-practices.md#reduce-bill-volume").

###### Note

There are some limitations for attaching and detaching volumes:

- Detaching a volume can take a long time. When you detach a volume, the
  gateway uploads all the data on the volume to AWS before the volume is
  detached. The time it takes for the upload to complete depends on how much
  data needs to be uploaded and your network connectivity into AWS.
- If you detach a cached volume, you can't reattach it as a stored
  volume.
- If you detach a stored volume, you can't reattach it as a cached
  volume.
- A detached volume can't be used until it is attached to a gateway.
- When you attach a stored volume, it needs to fully restore before you can
  attach it to a gateway.
- When you start attaching or detaching a volume, you need to wait till the
  operation completed before you use the volume.
- Currently, forcibly deleting a volume is only supported in the API.
- If you delete a gateway while your volume is detaching from that gateway,
  it results in data loss. Wait until the volume detach operation is complete
  before you delete the gateway.
- If a stored gateway is in restoring state, you can't detach a volume from
  it.
  The following steps show you how to detach and attach a volume using the Storage Gateway
  console. For more information about doing this using the API, see [DetachVolume](../APIReference/API_DetachVolume.md "../APIReference/API_DetachVolume.md") or [AttachVolume](../APIReference/API_AttachVolume.md "../APIReference/API_AttachVolume.md") in the _AWS Storage Gateway API Reference._

###### To detach a volume from a gateway

1. Open the Storage Gateway console at
   [https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/ "https://console.aws.amazon.com/storagegateway/").
2. Choose **Volumes**, the select one or more volumes to
   detach.
3. For **Actions**, choose **Detach volume**.
   The confirmation dialog box appears.
4. Verify that you want to detach the specified volumes, then type the word
   _detach_ in the confirmation box and choose
   **Detach**.

###### Note

If a volume that you detach has a lot of data on it, it transitions from
**Attached** to **Detaching** status
until it finishes uploading all the data. Then the status changes to
**Detached**. For small amounts of data, you might not
see the **Detaching** status. If the volume doesn't have
data on it, the status changes from **Attached** to
**Detached**.
You can now attach the volume to a different gateway.

###### To attach a volume to a gateway

1. Open the Storage Gateway console at
   [https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/ "https://console.aws.amazon.com/storagegateway/").
2. On the navigation pane, choose **Volumes**. The status of
   each volume that is detached shows as **Detached**.
3. From the list of detached volumes, choose the volume that you want to attach.
   You can attach only one volume at a time.
4. For **Actions**, choose **Attach volume**.
5. In the **Attach Volume** dialog box, choose the gateway that
   you want to attach the volume to, and then enter the iSCSI target that you want
   to connect the volume to.

If you are attaching a stored volume, enter its disk identifier for
**Disk ID**. 6. Choose **Attach volume**. If a volume that you attach has a
lot of data on it, it transitions from **Detached** to
**Attached** if the `AttachVolume` operation
succeeds. 7. In the Configure CHAP authentication wizard that appears, enter the
**Initiator name**, **Initiator secret**,
and **Target secret**, and then choose
**Save**. For more information about working with
Challenge-Handshake Authentication Protocol (CHAP) authentication, see [Configuring CHAP Authentication
for Your iSCSI Targets](ConfiguringiSCSIClientInitiatorCHAP.md "ConfiguringiSCSIClientInitiatorCHAP.md").
