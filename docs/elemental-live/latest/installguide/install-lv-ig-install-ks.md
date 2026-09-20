

# Step B: Install (kickstart) the operating system software
<a name="install-lv-ig-install-ks"></a>

Install the operating system on the node. This action is known as *kickstarting* the system.

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
  <tr><td><code>Set Hostname</code></td><td>Change the hostname to a useful name such as <b>live-01</b> or <b>live-chicago-01</b>.<br />Do not use <b>localhost</b> as the hostname.<br />Do not use periods or underscores in the hostname.</td></tr>
  <tr><td><code>Disk layout: Auto-detect</code></td><td>Keep this set at Auto-detect.</td></tr>
  <tr><td><code>Set Key</code></td><td>Arrow down to skip this option.</td></tr>
  <tr><td><code>Install and configure base operating system</code></td><td>Press Enter to begin the OS installation.</td></tr>
</tbody>
</table>


   The operating system is installed.

1. At the `Press return to quit` prompt, press **Enter** to reboot the system.