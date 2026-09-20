

This is version 2.20 of the AWS Elemental Statmux documentation. This is the latest version. For prior versions, see the *Previous Versions* section of [AWS Elemental Statmux and AWS Elemental Live Documentation](https://docs.aws.amazon.com/elemental-live).

# Step B: Install (Kickstart) the Operating System Software
<a name="install-sm-ig-install-ks"></a>

**To kickstart the system**

1. Insert the USB thumb drive into the hardware unit.

1. Restart the system using the following command.

   ```
   [elemental@hostname ~]$ sudo reboot
   ```

1. Use the arrow keys to select each option and complete the field, using the instructions in the following table as a guide.



<table>
<thead>
  <tr><th>Menu Option</th><th>Instructions</th></tr>
</thead>
<tbody>
  <tr><td><code>Set Hostname</code></td><td>Change the hostname to a useful name such as <b>statmux-01</b> or <b>statmux-chicago-01</b>.<br />Do not use localhost as the hostname!<br />Do not use periods or underscores in the hostname.</td></tr>
  <tr><td><code>Disk layout: Auto-detect</code></td><td>Leave this set at Auto-detect.</td></tr>
  <tr><td><code>Set Key</code></td><td>Arrow down to skip this option.</td></tr>
  <tr><td><code>Install and configure base operating system</code></td><td>Press Enter to begin the OS installation.</td></tr>
</tbody>
</table>


   The operating system is installed.

1. For the changes to take effect, reboot the system by pressing **Enter** at the prompt `Press return to quit`.