# Connecting your VTL devices

Following, you can find instructions about how to connect your virtual tape library (VTL)
devices to your Microsoft Windows or Red Hat Enterprise Linux (RHEL) client.

###### Topics

- [Connecting to a Microsoft Windows Client](#iscsi-vtl-windows "#iscsi-vtl-windows")
- [Connecting to a Linux Client](#iscsi-vtl-linux "#iscsi-vtl-linux")

## Connecting to a Microsoft Windows Client

The following procedure shows a summary of the steps that you follow to connect to a
Windows client.

###### To connect your VTL devices to a Windows client

1. Start `iscsicpl.exe`.

###### Note

You must have administrator rights on the client computer to run the iSCSI
initiator. 2. Start the Microsoft iSCSI initiator service. 3. In the **iSCSI Initiator Properties** dialog box, choose the
**Discovery** tab, and then choose **Discover
Portal**. 4. Provide the IP address of your Tape Gateway for **IP address or DNS
name**. 5. Choose the **Targets** tab, and then choose
**Refresh**. All 10 tape drives and the medium changer
appear in the **Discovered targets** box. The status for the
targets is **Inactive**. 6. Choose the first device and connect it. You connect the devices one at a time. 7. Connect all of the targets.

On a Windows client, the driver provider for the tape drive must be Microsoft. Use the
following procedure to verify the driver provider, and update the driver and provider if
necessary:

###### To verify and update the driver and provider

1. On your Windows client, start Device Manager.
2. Expand **Tape drives**, open the context (right-click) menu
   for a tape drive, and choose **Properties**.
3. In the **Driver** tab of the **Device
   Properties** dialog box, verify **Driver
   Provider** is Microsoft.
4. If **Driver Provider** is not Microsoft, set the value as
   follows:
   1. Choose **Update Driver**.
   2. In the **Update Driver Software** dialog box, choose
      **Browse my computer for driver software**.
   3. In the **Update Driver Software** dialog box, choose
      **Let me pick from a list of device drivers on my
      computer**.
   4. Choose **LTO Tape drive** and choose
      **Next**.

5. Choose **Close** to close the **Update
   Driver Software** window, and verify that the **Driver
   Provider** value is now set to Microsoft.
6. Repeat the steps to update driver and provider for all the tape
   drives.

## Connecting to a Linux Client

The following procedure shows a summary of the steps that you follow to connect to an
RHEL client.

###### To connect a Linux client to VTL devices

1. Install the `iscsi-initiator-utils` RPM package.

You can use the following command to install the package.

```
sudo yum install iscsi-initiator-utils
```

2. Make sure that the iSCSI daemon is running.

For RHEL 8 or 9, use the following command.

```
sudo service iscsid status
```

3. Discover the volume or VTL device targets defined for a gateway. Use the
   following discovery command.

```
sudo /sbin/iscsiadm --mode discovery --type sendtargets --portal `[GATEWAY_IP]`:3260
```

The output of the discovery command looks like the following example
output.

For Volume Gateways: ``[GATEWAY_IP]`:3260, 1
iqn.1997-05.com.amazon:myvolume`

For Tape Gateways:
`iqn.1997-05.com.amazon:`[GATEWAY_IP]`-tapedrive-01` 4. Connect to a target.

Be sure to specify the correct `[GATEWAY_IP]` and IQN
in the connect command.

Use the following command.

```
sudo /sbin/iscsiadm --mode node --targetname iqn.1997-05.com.amazon:`[ISCSI_TARGET_NAME]` --portal `[GATEWAY_IP]`:3260,1 --login
```

5. Verify that the volume is attached to the client machine (the initiator). To
   do so, use the following command.

```
ls -l /dev/disk/by-path
```

The output of the command should look like the following example
output.

`lrwxrwxrwx. 1 root root 9 Apr 16 19:31
 ip-`[GATEWAY_IP]`:3260-iscsi-iqn.1997-05.com.amazon:myvolume-lun-0
 -> ../../sda`

For Volume Gateways, we highly recommend that after you set up your
initiator, you customize your iSCSI settings as discussed in [Customizing Your Linux iSCSI
Settings](recommendediSCSISettings.md#CustomizeLinuxiSCSISettings "recommendediSCSISettings.md#CustomizeLinuxiSCSISettings").

Verify that the VTL device is attached to the client machine (the initiator).
To do so, use the following command.

```
ls -l /dev/tape/by-path
```

The output of the command should look like the following example
output.

```

total 0
lrwxrwxrwx 1 root root 10 Sep 8 11:20 ip-10.6.56.90:3260-iscsi-iqn.1997-05.com.amazon:sgw-9999999c-mediachanger-lun-0-changer -> ../../sg20
lrwxrwxrwx 1 root root 9 Sep 8 11:19 ip-10.6.56.90:3260-iscsi-iqn.1997-05.com.amazon:sgw-9999999c-tapedrive-01-lun-0 -> ../../st6
lrwxrwxrwx 1 root root 10 Sep 8 11:19 ip-10.6.56.90:3260-iscsi-iqn.1997-05.com.amazon:sgw-9999999c-tapedrive-01-lun-0-nst -> ../../nst6
lrwxrwxrwx 1 root root 9 Sep 8 11:20 ip-10.6.56.90:3260-iscsi-iqn.1997-05.com.amazon:sgw-9999999c-tapedrive-02-lun-0 -> ../../st7
lrwxrwxrwx 1 root root 10 Sep 8 11:20 ip-10.6.56.90:3260-iscsi-iqn.1997-05.com.amazon:sgw-9999999c-tapedrive-02-lun-0-nst -> ../../nst7
lrwxrwxrwx 1 root root 9 Sep 8 11:20 ip-10.6.56.90:3260-iscsi-iqn.1997-05.com.amazon:sgw-9999999c-tapedrive-03-lun-0 -> ../../st8
lrwxrwxrwx 1 root root 10 Sep 8 11:20 ip-10.6.56.90:3260-iscsi-iqn.1997-05.com.amazon:sgw-9999999c-tapedrive-03-lun-0-nst -> ../../nst8
lrwxrwxrwx 1 root root 9 Sep 8 11:20 ip-10.6.56.90:3260-iscsi-iqn.1997-05.com.amazon:sgw-9999999c-tapedrive-04-lun-0 -> ../../st9
lrwxrwxrwx 1 root root 10 Sep 8 11:20 ip-10.6.56.90:3260-iscsi-iqn.1997-05.com.amazon:sgw-9999999c-tapedrive-04-lun-0-nst -> ../../nst9
lrwxrwxrwx 1 root root 10 Sep 8 11:20 ip-10.6.56.90:3260-iscsi-iqn.1997-05.com.amazon:sgw-9999999c-tapedrive-05-lun-0 -> ../../st10
lrwxrwxrwx 1 root root 11 Sep 8 11:20 ip-10.6.56.90:3260-iscsi-iqn.1997-05.com.amazon:sgw-9999999c-tapedrive-05-lun-0-nst -> ../../nst10
lrwxrwxrwx 1 root root 10 Sep 8 11:20 ip-10.6.56.90:3260-iscsi-iqn.1997-05.com.amazon:sgw-9999999c-tapedrive-06-lun-0 -> ../../st11
lrwxrwxrwx 1 root root 11 Sep 8 11:20 ip-10.6.56.90:3260-iscsi-iqn.1997-05.com.amazon:sgw-9999999c-tapedrive-06-lun-0-nst -> ../../nst11
lrwxrwxrwx 1 root root 10 Sep 8 11:20 ip-10.6.56.90:3260-iscsi-iqn.1997-05.com.amazon:sgw-9999999c-tapedrive-07-lun-0 -> ../../st12
lrwxrwxrwx 1 root root 11 Sep 8 11:20 ip-10.6.56.90:3260-iscsi-iqn.1997-05.com.amazon:sgw-9999999c-tapedrive-07-lun-0-nst -> ../../nst12
lrwxrwxrwx 1 root root 10 Sep 8 11:20 ip-10.6.56.90:3260-iscsi-iqn.1997-05.com.amazon:sgw-9999999c-tapedrive-08-lun-0 -> ../../st13
lrwxrwxrwx 1 root root 11 Sep 8 11:20 ip-10.6.56.90:3260-iscsi-iqn.1997-05.com.amazon:sgw-9999999c-tapedrive-08-lun-0-nst -> ../../nst13
lrwxrwxrwx 1 root root 10 Sep 8 11:20 ip-10.6.56.90:3260-iscsi-iqn.1997-05.com.amazon:sgw-9999999c-tapedrive-09-lun-0 -> ../../st14
lrwxrwxrwx 1 root root 11 Sep 8 11:20 ip-10.6.56.90:3260-iscsi-iqn.1997-05.com.amazon:sgw-9999999c-tapedrive-09-lun-0-nst -> ../../nst14
lrwxrwxrwx 1 root root 10 Sep 8 11:20 ip-10.6.56.90:3260-iscsi-iqn.1997-05.com.amazon:sgw-9999999c-tapedrive-10-lun-0 -> ../../st15
lrwxrwxrwx 1 root root 11 Sep 8 11:20 ip-10.6.56.90:3260-iscsi-iqn.1997-05.com.amazon:sgw-9999999c-tapedrive-10-lun-0-nst -> ../../nst15
lrwxrwxrwx 1 root root 9 Aug 19 10:15 pci-0000:12:00.0-fc-0x0000000000000012-lun-0-changer -> ../../sg6
lrwxrwxrwx 1 root root 9 Aug 19 10:15 pci-0000:12:00.0-fc-0x000000000000001c-lun-0 -> ../../st0
lrwxrwxrwx 1 root root 10 Aug 19 10:15 pci-0000:12:00.0-fc-0x000000000000001c-lun-0-nst -> ../../nst0
lrwxrwxrwx 1 root root 9 Aug 19 10:15 pci-0000:12:00.0-fc-0x000000000000001f-lun-0 -> ../../st1
lrwxrwxrwx 1 root root 10 Aug 19 10:15 pci-0000:12:00.0-fc-0x000000000000001f-lun-0-nst -> ../../nst1
lrwxrwxrwx 1 root root 9 Aug 19 10:15 pci-0000:12:00.0-fc-0x0000000000000022-lun-0 -> ../../st2
lrwxrwxrwx 1 root root 10 Aug 19 10:15 pci-0000:12:00.0-fc-0x0000000000000022-lun-0-nst -> ../../nst2
lrwxrwxrwx 1 root root 9 Aug 19 10:15 pci-0000:12:00.1-fc-0x0000000000000025-lun-0 -> ../../st5
lrwxrwxrwx 1 root root 10 Aug 19 10:15 pci-0000:12:00.1-fc-0x0000000000000025-lun-0-nst -> ../../nst5
lrwxrwxrwx 1 root root 9 Aug 19 10:15 pci-0000:12:00.1-fc-0x0000000000000028-lun-0 -> ../../st3
lrwxrwxrwx 1 root root 10 Aug 19 10:15 pci-0000:12:00.1-fc-0x0000000000000028-lun-0-nst -> ../../nst3
lrwxrwxrwx 1 root root 9 Aug 19 10:15 pci-0000:12:00.1-fc-0x000000000000002b-lun-0 -> ../../st4
lrwxrwxrwx 1 root root 10 Aug 19 10:15 pci-0000:12:00.1-fc-0x000000000000002b-lun-0-nst -> ../../nst4

```

**Next Step**

[Using Your Backup
Software to Test Your Gateway Setup](GettingStartedTestGatewayVTL.md "GettingStartedTestGatewayVTL.md")
