# Customizing iSCSI Settings

After you set up your initiator, we highly recommend that you customize your iSCSI
settings to prevent the initiator from disconnecting from targets.

By increasing the iSCSI timeout values as shown in the following steps, you make your
application better at dealing with write operations that take a long time and other
transient issues such as network interruptions.

###### Note

Before making changes to the registry, you should make a backup copy of the registry.
For information on making a backup copy and other best practices to follow when working
with the registry, see [Registry best
practices](<http://technet.microsoft.com/en-us/library/cc780921(WS.10).aspx> "http://technet.microsoft.com/en-us/library/cc780921(WS.10).aspx") in the _Microsoft TechNet Library_.

###### Topics

- [Customizing Your Windows iSCSI
  Settings](#CustomizeWindowsiSCSISettings "#CustomizeWindowsiSCSISettings")
- [Customizing Your Linux iSCSI
  Settings](#CustomizeLinuxiSCSISettings "#CustomizeLinuxiSCSISettings")
- [Customizing Your Linux Disk Timeout
  Settings for Volume Gateways](#CustomizeLinuxDiskTimeoutSettings "#CustomizeLinuxDiskTimeoutSettings")

## Customizing Your Windows iSCSI

Settings

When using a Windows client, you use the Microsoft iSCSI initiator to
connect to your gateway volume. For instructions on how to connect to your volumes, see
[Connecting your volumes to your client](GettingStartedAccessVolumes.md "GettingStartedAccessVolumes.md").

###### To customize your Windows iSCSI settings

1. Increase the maximum time for which requests are queued.
   1. Start Registry Editor (`Regedit.exe`).
   2. Navigate to the globally unique identifier (GUID) key for the device
      class that contains iSCSI controller settings, shown following.

   ###### Warning

   Make sure that you are working in the
   **CurrentControlSet** subkey and not another
   control set, such as **ControlSet001** or
   **ControlSet002**.

   ```
   HKEY_Local_Machine\SYSTEM\CurrentControlSet\Control\Class\{4D36E97B-E325-11CE-BFC1-08002BE10318}
   ```

   3. Find the subkey for the Microsoft iSCSI initiator, shown following as
      `[<Instance Number]`.

   The key is represented by a four-digit number, such as
   `0000`.

   ```
   HKEY_Local_Machine\SYSTEM\CurrentControlSet\Control\Class\{4D36E97B-E325-11CE-BFC1-08002BE10318}\`[<Instance Number]`
   ```

   Depending on what is installed on your computer, the Microsoft iSCSI
   initiator might not be the subkey `0000`. You can ensure that
   you have selected the correct subkey by verifying that the string
   `DriverDesc` has the value `Microsoft iSCSI
 Initiator`. 4. To show the iSCSI settings, choose the **Parameters**
   subkey. 5. Open the context (right-click) menu for the
   **MaxRequestHoldTime** DWORD (32-bit) value, choose
   **Modify**, and then change the value to
   `600`.

   **MaxRequestHoldTime** specifies how many seconds
   Microsoft iSCSI initiator should hold and retry outstanding commands
   for, before notifying the upper layer of a `Device Removal`
   event. This value represents a hold time of 600 seconds.

2. You can increase the maximum amount of data that can be sent in iSCSI packets
   by modifying the following parameters:
   - **FirstBurstLength** controls the maximum amount of
     data that can be transmitted in an unsolicited write request. Set this
     value to `262144` or the Windows OS default,
     whichever is higher.
   - **MaxBurstLength** is similar to
     **FirstBurstLength**, but it sets the maximum
     amount of data that can be transmitted in solicited write sequences. Set
     this value to `1048576` or the Windows OS default,
     whichever is higher.
   - **MaxRecvDataSegmentLength** controls the maximum
     data segment size that is associated with a single protocol data unit
     (PDU). Set this value to `262144` or the Windows OS
     default, whichever is higher.

###### Note

Different backup software can be optimized to work best using different
iSCSI settings. To verify which values for these parameters will provide the
best performance, see the documentation for your backup software. 3. Increase the disk timeout value, as shown following:

    1. Start Registry Editor (`Regedit.exe`), if you
     haven't already.
    2. Navigate to the **Disk** subkey in the
     **Services** subkey of the
     **CurrentControlSet**, shown following.



    ```
    HKEY_Local_Machine\SYSTEM\CurrentControlSet\Services\Disk
    ```
    3. Open the context (right-click) menu for the
     **TimeOutValue** DWORD (32-bit) value, choose
     **Modify**, and then change the value to
     `600`.


    **TimeOutValue** specifies how many seconds iSCSI
     initiator will wait for a response from the target before it attempts
     session recovery by dropping and re-establishing the connection. This
     value represents a timeout period of 600 seconds.

4. To ensure that the new configuration values take effect, restart your
   system.

Before restarting, you must make sure that the results of all write operations
to volumes are flushed. To do this, take any mapped storage volume disks offline
before restarting.

## Customizing Your Linux iSCSI

Settings

After setting up the initiator for your gateway, we highly recommend that you
customize your iSCSI settings to prevent the initiator from disconnecting from targets.
By increasing the iSCSI timeout values as shown following, you make your application
better at dealing with write operations that take a long time and other transient issues
such as network interruptions.

###### Note

Commands might be slightly different for other types of Linux. The following
examples are based on Red Hat Linux.

###### To customize your Linux iSCSI settings

1. Increase the maximum time for which requests are queued.
   1. Open the `/etc/iscsi/iscsid.conf` file and find the
      following lines.

   ```
   node.session.timeo.replacement_timeout = `[replacement_timeout_value]`
   node.conn[0].timeo.noop_out_interval = `[noop_out_interval_value]`
   node.conn[0].timeo.noop_out_timeout = `[noop_out_timeout_value]`
   ```

   2. Set the `[replacement_timeout_value]` value
      to `600`.

   Set the `[noop_out_interval_value]` value to
   `60`.

   Set the `[noop_out_timeout_value]` value to
   `600`.

   All three values are in seconds.

   ###### Note

   The `iscsid.conf` settings must be made before
   discovering the gateway. If you have already discovered your gateway
   or logged in to the target, or both, you can delete the entry from
   the discovery database using the following command. Then you can
   rediscover or log in again to pick up the new configuration.

   ```
   iscsiadm -m discoverydb -t sendtargets -p `[GATEWAY_IP]`:3260 -o delete
   ```

2. Increase the maximum values for the amount of data that can be transmitted in
   each response.
   1. Open the `/etc/iscsi/iscsid.conf` file and find the
      following lines.

   ```
   node.session.iscsi.FirstBurstLength = `[replacement_first_burst_length_value]`
   node.session.iscsi.MaxBurstLength = `[replacement_max_burst_length_value]`
   node.conn[0].iscsi.MaxRecvDataSegmentLength = `[replacement_segment_length_value]`
   ```

   2. We recommend the following values to achieve better performance. Your
      backup software might be optimized to use different values, so see your
      backup software documentation for best results.

   Set the
   `[replacement_first_burst_length_value]`
   value to `262144` or the Linux OS default,
   whichever is higher.

   Set the
   `[replacement_max_burst_length_value]`
   value to `1048576` or the Linux OS default,
   whichever is higher.

   Set the `[replacement_segment_length_value]`
   value to `262144` or the Linux OS default,
   whichever is higher.

   ###### Note

   Different backup software can be optimized to work best using
   different iSCSI settings. To verify which values for these
   parameters will provide the best performance, see the documentation
   for your backup software.

3. Restart your system to ensure that the new configuration values take
   effect.

Before restarting, make sure that the results of all write operations to your
tapes are flushed. To do this, unmount tapes before restarting.

## Customizing Your Linux Disk Timeout

Settings for Volume Gateways

If you are using a Volume Gateway, you can customize the following Linux disk timeout
settings in addition to the iSCSI settings described in the preceding section.

###### To customize your Linux disk timeout settings

1. Increase the disk timeout value in the rules file.
   1. If you are using the RHEL 5 initiator, open the
      `/etc/udev/rules.d/50-udev.rules` file, and find
      the following line.

   ```
   ACTION=="add", SUBSYSTEM=="scsi" , SYSFS{type}=="0|7|14", \
   RUN+="/bin/sh -c 'echo `[timeout]` > /sys$$DEVPATH/timeout'"
   ```

   This rules file does not exist in RHEL 6 or 7 initiators, so you must
   create it using the following rule.

   ```
   ACTION=="add", SUBSYSTEMS=="scsi" , ATTRS{model}=="Storage Gateway",
   RUN+="/bin/sh -c 'echo `[timeout]` > /sys$$DEVPATH/timeout'"
   ```

   To modify the timeout value in RHEL 6, use the following command, and
   then add the lines of code shown preceding.

   ```
   sudo vim /etc/udev/rules.d/50-udev.rules
   ```

   To modify the timeout value in RHEL 7, use the following command, and
   then add the lines of code shown preceding.

   ```
   sudo su -c "echo 600 > /sys/block/[device name]/device/`timeout`"
   ```

   2. Set the `[timeout]` value to
      `600`.

   This value represents a timeout of 600 seconds.

2. Restart your system to ensure that the new configuration values take
   effect.

Before restarting, make sure that the results of all write operations to your
volumes are flushed. To do this, unmount storage volumes before
restarting. 3. You can test the configuration by using the following command.

```
udevadm test `[PATH_TO_ISCSI_DEVICE]`
```

This command shows the udev rules that are applied to the iSCSI device.
