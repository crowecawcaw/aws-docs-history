

# Step C: Install the Conductor Live software
<a name="install-cl3-ig-install-sw"></a>

Perform these on the Conductor Live appliance, either directly at the appliance or from your workstation via SSH. 

**To install the Conductor Live software**

1. At the Linux command line, log in with the *elemental* user credentials.

1. Run the installer with this command. Use the actual file name of your `.run` file rather than the example below.

   ```
   [elemental@hostname ~]$ sudo sh ./elemental_production_conductor_live247_3.25.5.12345.run -l -z -t
   ```

   where -l is a letter, not a number.

1. Follow the prompts:



<table>
<thead>
  <tr><th>Prompt</th><th>Action</th></tr>
</thead>
<tbody>
  <tr><td><code>Do you agree to these terms?</code></td><td>This prompt appears after you have paged through the EULA (End User License Agreement).<br />Enter <b>Yes</b> or <b>No</b>. (You must enter Yes to continue.)</td></tr>
  <tr><td><code>Enter this server’s Hostname</code></td><td>Type the hostname of this appliance. For example, <b>conductor-live-3-01</b> </td></tr>
  <tr><td><code>Does eth0 use DHCP to get its IP address?</code></td><td>Type <b>Yes</b> to use DHCP or type <b>No</b> to enter a static IP address.</td></tr>
  <tr><td><code>Enter eth0's IP address: </code></td><td>If you chose static, type the IP address for this hardware unit.</td></tr>
  <tr><td><code>Enter eth0's NETMASK:</code></td><td>If you chose static, type the netmask for this hardware unit.</td></tr>
  <tr><td><code>Enter eth0's Gateway (or type none):</code></td><td>If you chose static, type <b>none</b> or type the gateway for this appliance.</td></tr>
  <tr><td><code>Keep this configured nameserver?</code> </td><td>Skip; you set up a nameserver in the next phase of configuration.</td></tr>
  <tr><td><code>Would you like to configure eth1?</code></td><td>Type <b>No</b>; you can configure eth1 in the next phase of the configuration.</td></tr>
  <tr><td><code>The firewall for this system is currently disabled. Would you like to enable it?</code></td><td>Skip; you set up the firewall in the next phase of configuration.</td></tr>
  <tr><td><code>Would you like to start the Elemental service now?</code></td><td>Type <b>Yes</b>.</td></tr>
</tbody>
</table>


   Then the software is installed. Finally, this message appears:

   ```
   Installation and configuration complete!
   Please open a web browser and point it to https://xxx.xxx.xxx.xxx to get to the web interface.
   Enjoy!
   ```

1. Start a web browser and start the Conductor Live web interface by typing the following:

   ```
   https://<hostname>
   ```

   Make sure the web interface displays.