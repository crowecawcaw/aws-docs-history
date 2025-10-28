# Creating a storage volume

Previously, you allocated local disks that you added to the VM cache storage and upload
buffer. Now you create a storage volume to which your applications read and write data. The
gateway maintains the volume's recently accessed data locally in cache storage, and
asynchronously transferred data to Amazon S3. For stored volumes, you allocated local disks that
you added to the VM upload buffer and your application's data.

###### Note

You can use AWS Key Management Service (AWS KMS) to encrypt data written to a cached volume that is
stored in Amazon S3. Currently, you can do this by using the _AWS Storage Gateway API Reference_. For more information, see [CreateCachediSCSIVolume](../APIReference/API_CreateCachediSCSIVolume.md "../APIReference/API_CreateCachediSCSIVolume.md") or [create-cached-iscsi-volume](../../../cli/latest/reference/storagegateway/create-cached-iscsi-volume.md "../../../cli/latest/reference/storagegateway/create-cached-iscsi-volume.md").

###### To create a volume

1. Open the Storage Gateway console at
   [https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/ "https://console.aws.amazon.com/storagegateway/").
2. On the Storage Gateway console, choose **Create volume**.
3. In the **Create volume** dialog box, choose a gateway for
   **Gateway**.
4. For the cached volumes, enter the capacity in
   **Capacity**.

For stored volumes, choose a **Disk ID** value from the
list. 5. For **Volume content**, your choices depend on the type of
gateway that you're creating the volume for.

For cached volumes, you have the following options:

    * **Create a new empty volume**.
    * **Create a volume based on an Amazon EBS snapshot**. If you
     choose this option, provide a value for **EBS snapshot
     ID**.


    ###### Note

    Storage Gateway does not support creating cached volumes from snapshots of
     AWS Marketplace volumes.
    * **Clone from last volume recovery point**. If you choose
     this option, choose a volume ID for **Source volume**. If
     there are no volumes in the Region, this option doesn't appear.

For stored volumes, you have the following options:

    * **Create a new empty volume**.
    * **Create a volume based on a snapshot**. If you choose
     this option, provide a value for **EBS snapshot
     ID**.
    * **Preserve existing data on the disk**

6. Enter a name for **iSCSI target name**.

The target name can contain lowercase letters, numbers, periods (.), and hyphens
(-). This target name appears as the **iSCSI target node** name in
the **Targets** tab of the **iSCSI Microsoft
initiator** UI after discovery. For example, the name
`target1` appears as `iqn.1007-05.com.amazon:target1`.
Make sure that the target name is globally unique within your storage area network
(SAN). 7. Verify that the **Network interface** setting has IP address
selected, or choose an IP address for **Network interface**. For
**Network interface**, one IP address appears for each adapter
that is configured for the gateway VM. If the gateway VM is configured for only one
network adapter, no **Network interface** list appears because
there is only one IP address.

Your iSCSI target will be available on the network adapter you choose.

If you have defined your gateway to use multiple network adapters, choose the IP
address that your storage applications should use to access your volume. For
information about configuring multiple network adapters, see [Configuring Your Gateway for
Multiple NICs](NICConfiguring-common.md#MaintenanceMultiNIC-common "NICConfiguring-common.md#MaintenanceMultiNIC-common").

###### Note

After you choose a network adapter, you can't change this setting. 8. (Optional) For **Tags**, enter a key and value to add tags to
your volume. A tag is a case-sensitive key-value pair that helps you manage, filter,
and search for your volumes. 9. Choose **Create volume**.

If you have previously created volumes in this Region, you can see them listed on
the Storage Gateway console.

The **Configure CHAP Authentication** dialog box appears. At this
point, you can configure Challenge-Handshake Authentication Protocol (CHAP) for your
volume, or you can choose **Cancel** and configure CHAP later. For
more information about CHAP setup, see [Configure CHAP authentication for
your volumes](#GettingStartedConfigureChap-stored "#GettingStartedConfigureChap-stored").
If you don't want to set up CHAP, get started using your volume. For more information, see
[Connecting your volumes to your client](GettingStartedAccessVolumes.md "GettingStartedAccessVolumes.md").

## Configure CHAP authentication for

your volumes

CHAP provides protection against playback attacks by requiring authentication to
access your storage volume targets. In the **Configure CHAP
Authentication** dialog box, you provide information to configure CHAP for
your volumes.

###### To configure CHAP

1. Choose the volume for which you want to configure CHAP.
2. For **Actions**, choose **Configure CHAP
   authentication**.
3. For **Initiator Name**, enter the name of your
   initiator.
4. For **Initiator secret**, enter the secret phrase that you
   used to authenticate your iSCSI initiator.
5. For **Target secret**, enter the secret phrase used to
   authenticate your target for mutual CHAP.
6. Choose **Save** to save your entries.

For more information about setting up CHAP authentication, see [Configuring CHAP Authentication
for Your iSCSI Targets](ConfiguringiSCSIClientInitiatorCHAP.md "ConfiguringiSCSIClientInitiatorCHAP.md").

**Next step**

[Connecting your volumes to your client](GettingStartedAccessVolumes.md "GettingStartedAccessVolumes.md")
