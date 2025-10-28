# Connecting your VTL devices to

a Linux client

###### Topics

When using Red Hat Enterprise Linux (RHEL), you use the
`iscsi-initiator-utils` RPM package to connect to your gateway
iSCSI targets (volumes or VTL devices).

###### To connect a Linux client to the iSCSI targets

1. Install the `iscsi-initiator-utils` RPM package, if it
   isn't already installed on your client.

You can use the following command to install the package.

```
sudo yum install iscsi-initiator-utils
```

2. Ensure that the iSCSI daemon is running.
   1. Verify that the iSCSI daemon is running using one of the following
      commands.

   For RHEL 8 or 9, use the following command.

   ```
   sudo service iscsid status
   ```

   2. If the status command doesn't return a status of
      _running_, start the daemon using one of the
      following commands.

   For RHEL 8 or 9, use the following command. You usually don't need to
   explicitly start the `iscsid` service.

   ```
   sudo service iscsid start
   ```

3. To discover the volume or VTL device targets defined for a gateway, use the
   following discovery command.

```
sudo /sbin/iscsiadm --mode discovery --type sendtargets --portal `[GATEWAY_IP]`:3260
```

Substitute your gateway's IP address for the
`[GATEWAY_IP]` variable in the preceding command.
You can find the gateway IP in the **iSCSI Target Info**
properties of a volume on the Storage Gateway console.

The output of the discovery command will look like the following example
output.

For Volume Gateways: ``[GATEWAY_IP]`:3260, 1
iqn.1997-05.com.amazon:myvolume`

For Tape Gateways:
`iqn.1997-05.com.amazon:`[GATEWAY_IP]`-tapedrive-01`

Your iSCSI qualified name (IQN) will be different than what is shown
preceding, because IQN values are unique to an organization. The name of the
target is the name that you specified when you created the volume. You can also
find this target name in the **iSCSI Target Info** properties
pane when you select a volume on the Storage Gateway console. 4. To connect to a target, use the following command.

Note that you need to specify the correct
`[GATEWAY_IP]` and IQN in the connect
command.

###### Warning

For gateways that are deployed on an Amazon EC2 instance, accessing the gateway
over a public internet connection is not supported. The Elastic IP address
of the Amazon EC2 instance cannot be used as the target address.

```
sudo /sbin/iscsiadm --mode node --targetname iqn.1997-05.com.amazon:`[ISCSI_TARGET_NAME]` --portal `[GATEWAY_IP]`:3260,1 --login
```

5. To verify that the volume is attached to the client machine (the initiator),
   use the following command.

```
ls -l /dev/disk/by-path
```

The output of the command will look like the following example output.

`lrwxrwxrwx. 1 root root 9 Apr 16 19:31
 ip-`[GATEWAY_IP]`:3260-iscsi-iqn.1997-05.com.amazon:myvolume-lun-0
 -> ../../sda`

We highly recommend that after you set up your initiator, you customize your
iSCSI settings as discussed in [Customizing Your Linux iSCSI
Settings](recommendediSCSISettings.md#CustomizeLinuxiSCSISettings "recommendediSCSISettings.md#CustomizeLinuxiSCSISettings").
