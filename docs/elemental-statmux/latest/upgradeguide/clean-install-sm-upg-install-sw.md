

This is version 2.20 of the AWS Elemental Statmux documentation. This is the latest version. For prior versions, see the *Previous Versions* section of [AWS Elemental Statmux and AWS Elemental Live Documentation](https://docs.aws.amazon.com/elemental-live).

# Step D: Install the AWS Elemental Software
<a name="clean-install-sm-upg-install-sw"></a>

These steps must be performed on each system where you are installing AWS Elemental software, either directly at the machine or from your workstation via SSH. Make sure that you use the `.run` file that corresponds to the `.iso` file that you used to reinstall the operating system.

1. At the Linux command line, log in with the *elemental* user credentials.

   Run the installer as follows. Use the actual filename of your .run file, rather than the example below.

   ```
   [elemental@hostname ~]$ sudo sh ./elemental_production_statmux_dg_version_short;.nnnnn.run -l -z -t
   ```

   where -l is a letter, not a number.

1. You are prompted as described in the table below.



<table>
<thead>
  <tr><th>Prompt</th><th>Action</th></tr>
</thead>
<tbody>
  <tr><td><code>Do you agree to these terms?</code></td><td>This prompt appears after you have paged through the EULA (End User License Agreement).<br />Enter <b>Yes</b> or <b>No</b>. (You must enter Yes to continue.)</td></tr>
  <tr><td><code>Enter this server’s Hostname</code></td><td>Type the hostname of this hardware unit. For example, <b>statmux-01</b></td></tr>
  <tr><td><code>Is eth0 a management interface?</code></td><td>Type <b>Yes</b>.</td></tr>
  <tr><td><code>Does eth0 use DHCP to get its IP address?</code></td><td>Type <b>Yes</b> to use DHCP or type <b>No</b> to enter a static IP address.</td></tr>
  <tr><td><code>Enter eth0's IP address: </code></td><td>If you chose static, type the IP address for this hardware unit.</td></tr>
  <tr><td><code>Enter eth0's NETMASK:</code></td><td>If you chose static, type the netmask for this hardware unit.</td></tr>
  <tr><td><code>Enter eth0's Gateway (or type none):</code></td><td>If you chose static, type <b>none</b> or type the gateway for this hardware unit.</td></tr>
  <tr><td><code>Keep this configured nameserver?</code></td><td>Skip; you set up a nameserver in the next phase of configuration.</td></tr>
  <tr><td><code>Would you like to configure eth1?</code></td><td>Type <b>No</b>; you can configure eth1 in the next phase of the configuration.</td></tr>
  <tr><td><code>The firewall for this system is currently disabled. Would you like to enable it?</code></td><td>Skip; you set up the firewall in the next phase of configuration.</td></tr>
  <tr><td><code>For security purposes, we require that you change the default password.</code></td><td>This prompt is shown if you are still using the default password.</td></tr>
  <tr><td><code>Is this machine a part of or intended to be a part of a Conductor Live 3 cluster?</code></td><td>Type <b>No</b>.</td></tr>
  <tr><td><code>Is this a Statmux machine, or intended to be linked to a Statmux machine?</code></td><td>Type <b>Yes</b>.</td></tr>
  <tr><td><code>Will this machine require use of SNMP alerts?</code></td><td>If applicable, type <b>Yes</b> to open the related port.</td></tr>
  <tr><td><code>Will this machine be ingesting RTMP?</code></td><td>If applicable, type <b>Yes</b> to open the related port.</td></tr>
  <tr><td><code>Will this machine ingest MPEG-TS over UDP? (ports 5000-5100)</code></td><td>If applicable, type <b>Yes</b> to open the related port.</td></tr>
  <tr><td><code>Is this machine licensed as part of a licensing pool?</code></td><td>If applicable, type <b>Yes</b> to open the related port.</td></tr>
  <tr><td><code>Will this machine serve files using Windows file-sharing (Samba/CIFS)?</code></td><td>If applicable, type <b>Yes</b> to open the related port.</td></tr>
  <tr><td><code>Will this machine be an NTP server?</code></td><td>If applicable, type <b>Yes</b> to open the related port.</td></tr>
  <tr><td><code>Select time zone ('n' for more)</code></td><td>Enter the time zone you want to show on the web interface of the nodes. This setting does not affect activity via SSH or via the REST API.</td></tr>
  <tr><td><code>Would you like to start the Elemental service now?</code></td><td>Type <b>Yes</b>.</td></tr>
</tbody>
</table>


   Then the software will be installed. Finally, this message will appear:

   ```
   Installation and configuration complete!
     Please open a web browser and point it to http://xxx.xxx.xxx.xxx to get to the web
     interface.
     Enjoy!
   ```

1. Start a web browser and start the AWS Elemental Statmux web interface by typing the following:

   ```
   http://<hostname>
   ```

   Make sure the web interface displays.