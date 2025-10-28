# Cloning a cached volume from a recovery point

You can create a new volume from any existing cached volume in the same AWS Region.
The new volume is created from the most recent recovery point of the selected volume. A
_volume recovery point_ is a point in time at which all data of
the volume is consistent. To clone a volume, you choose the **Clone from last
recovery point** option in the **Create volume** dialog
box, then select the volume to use as the source.

Cloning from an existing volume is faster and more cost-effective than creating an
Amazon EBS snapshot. Cloning does a byte-to-byte copy of your data from the source volume to
the new volume, using the most recent recovery point from the source volume.
Storage Gateway automatically creates recovery points for your cached volumes. To see when
the last recovery point was created, check the `TimeSinceLastRecoveryPoint`
metric in Amazon CloudWatch.

The cloned volume is independent of the source volume. That is, changes made to either
volume after cloning have no effect on the other. For example, if you delete the source
volume, it has no effect on the cloned volume. You can clone a source volume while
initiators are connected and it is in active use. Doing so doesn't affect the
performance of the source volume. For information about how to clone a volume, see [Creating a storage volume](GettingStartedCreateVolumes.md "GettingStartedCreateVolumes.md").

You can also use the cloning process in recovery scenarios. For more information, see
[Your Cached Gateway is Unreachable
And You Want to Recover Your Data](troubleshoot-volume-issues.md#RecoverySnapshotTroubleshooting "troubleshoot-volume-issues.md#RecoverySnapshotTroubleshooting").

The following procedure shows you how to clone a volume from a volume recovery point
and use that volume.

###### To clone and use a volume from an unreachable gateway

1. Open the Storage Gateway console at
   [https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/ "https://console.aws.amazon.com/storagegateway/").
2. On the Storage Gateway console, choose **Create volume**.
3. In the **Create volume** dialog box, choose a gateway for
   **Gateway**.
4. For **Capacity**, type the capacity for your volume. The
   capacity must be at least the same size as the source volume.
5. Choose **Clone from last recovery point** and select a volume
   ID for **Source volume**. The source volume can be any cached
   volume in the selected AWS Region.
6. Type a name for **iSCSI target name**.

The target name can contain lowercase letters, numbers, periods (.), and
hyphens (-). This target name appears as the **iSCSI target
node** name in the **Targets** tab of the
**iSCSI Microsoft initiator** UI after discovery. For
example, the name `target1` appears as
`iqn.1007-05.com.amazon:target1`. Ensure that the target name is
globally unique within your storage area network (SAN). 7. Verify that the **Network interface** setting is the IP
address of your gateway, or choose an IP address for **Network
interface**.

If you have defined your gateway to use multiple network adapters, choose the
IP address that your storage applications use to access the volume. Each network
adapter defined for a gateway represents one IP address that you can
choose.

If the gateway VM is configured for more than one network adapter, the
**Create volume** dialog box displays a list for
**Network interface**. In this list, one IP address appears
for each adapter configured for the gateway VM. If the gateway VM is configured
for only one network adapter, no list appears because there's only one IP
address. 8. Choose **Create volume**. The **Configure CHAP
Authentication** dialog box appears. You can configure CHAP later.
For information, see [Configuring CHAP Authentication
for Your iSCSI Targets](ConfiguringiSCSIClientInitiatorCHAP.md "ConfiguringiSCSIClientInitiatorCHAP.md").
The next step is to connect your volume to your client. For more information, see
[Connecting your volumes to your client](GettingStartedAccessVolumes.md "GettingStartedAccessVolumes.md").
