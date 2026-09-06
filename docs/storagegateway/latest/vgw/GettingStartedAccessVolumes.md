

# Connecting your volumes to your client
<a name="GettingStartedAccessVolumes"></a>

You use the iSCSI initiator in your client to connect to your volumes. At the end of the following procedure, the volumes become available as local devices on your client.

**Important**  
With Storage Gateway, you can connect multiple hosts to the same volume if the hosts coordinate access by using Windows Server Failover Clustering (WSFC). You can't connect multiple hosts to the same volume without using WSFC, for example by sharing a nonclustered NTFS/ext4 file system. 

**Topics**
+ [Connecting to a Microsoft Windows client](#issci-windows)
+ [Connecting to a Red Hat Enterprise Linux client](#issci-rhel)

## Connecting to a Microsoft Windows client
<a name="issci-windows"></a>

The following procedure shows a summary of the steps that you follow to connect to a Windows client. For more information, see [Connecting iSCSI Initiators](initiator-connection-common.md).

**To connect to a Windows client**

1. Start iscsicpl.exe.

1. In the **iSCSI Initiator Properties** dialog box, choose the **Discovery** tab, and then choose **Discovery Portal**.

1. In the **Discover Target Portal** dialog box, type the IP address of your iSCSI target for IP address or DNS name. 

1. Connect the new target portal to the storage volume target on the gateway.

1. Choose the target, and then choose **Connect**.

1. In the **Targets** tab, make sure that the target status has the value **Connected**, indicating the target is connected, and then choose **OK**. 

## Connecting to a Red Hat Enterprise Linux client
<a name="issci-rhel"></a>

The following procedure shows a summary of the steps that you follow to connect to a Red Hat Enterprise Linux (RHEL) client. For more information, see [Connecting iSCSI Initiators](initiator-connection-common.md).

**To connect a Linux client to iSCSI targets**

1. Install the iscsi-initiator-utils RPM package.

   You can use the following command to install the package.

   ```
   sudo yum install iscsi-initiator-utils
   ```

1. Make sure that the iSCSI daemon is running.

   For RHEL 5 or 6, use the following command.

   ```
   sudo /etc/init.d/iscsi status
   ```

   For RHEL 7, 8, or 9, use the following command.

   ```
   sudo service iscsid status
   ```

1. Discover the volume or VTL device targets defined for a gateway. Use the following discovery command.

   ```
   sudo /sbin/iscsiadm --mode discovery --type sendtargets --portal {{[GATEWAY_IP]}}:3260
   ```

   The output of the discovery command should look like the following example output.

   For Volume Gateways: `{{[GATEWAY_IP]}}:3260, 1 iqn.1997-05.com.amazon:myvolume `

   For Tape Gateways: `iqn.1997-05.com.amazon:{{[GATEWAY_IP]}}-tapedrive-01`

1. Connect to a target. 

   Make sure to specify the correct {{[GATEWAY\_IP]}} and IQN in the connect command.

   Use the following command.

   ```
   sudo /sbin/iscsiadm --mode node --targetname iqn.1997-05.com.amazon:{{[ISCSI_TARGET_NAME]}} --portal {{[GATEWAY_IP]}}:3260,1 --login
   ```

1. Verify that the volume is attached to the client machine (the initiator). To do so, use the following command.

   ```
   ls -l /dev/disk/by-path
   ```

   The output of the command should look like the following example output.

   `lrwxrwxrwx. 1 root root 9 Apr 16 19:31 ip-{{[GATEWAY_IP]}}:3260-iscsi-iqn.1997-05.com.amazon:myvolume-lun-0 -> ../../sda`

   We highly recommend that after you set up your initiator you customize your iSCSI settings as discussed in [Customizing Your Linux iSCSI Settings](recommendediSCSISettings.md#CustomizeLinuxiSCSISettings).