

This is version 2.18 of the AWS Elemental Server documentation. This is the latest version. For prior versions, see the *Previous Versions* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server/).

# Step C: Install the AWS Elemental Software
<a name="install-srvr-ig-install-sw"></a>

These steps must be performed on each node where you are installing AWS Elemental software, either directly at the machine or from your workstation via SSH. 

Make sure that you use the .run file that corresponds to the .iso file that you used to set up the operating system on the node. That is, install AWS Elemental Conductor File software on the nodes that you kickstarted with the AWS Elemental Conductor File .iso and worker software on nodes that you kickstarted with the worker .iso.

**To install the software**

1. At the Linux command line, log in with the *elemental* user credentials.

1. Run the installer as follows. Use the actual filename of your .run file, rather than the example below.

   For GPU and CPU versions of the software.

   ```
   [elemental@hostname ~]$ sudo sh ./elemental_production_server_2.18.n.nnnnn.run -l -z -t
   ```

   For CPU-only versions of the software.

   ```
   [elemental@hostname ~]$ sudo sh ./elemental_production_server_cpu_2.18.n.nnnnn.run -l -z -t
   ```

   Where -l is a letter, not a number.

1. You are prompted as described in the table below.



<table>
<thead>
  <tr><th>Prompt</th><th>Action</th></tr>
</thead>
<tbody>
  <tr><td><code>Do you agree to these terms?</code></td><td>This prompt appears after you have paged through the EULA (End User License Agreement).<br />Enter <b>Yes</b> or <b>No</b>. (You must enter Yes to continue.)</td></tr>
  <tr><td><code>Enter this server’s Hostname</code></td><td>Type the hostname of this hardware unit. For example, <b>server-01</b></td></tr>
  <tr><td><code>Is eth0 a management interface?</code></td><td>Type <b>Yes</b>.</td></tr>
  <tr><td><code>Does eth0 use DHCP to get its IP address?</code></td><td>Type <b>Yes</b> to use DHCP or type <b>No</b> to enter a static IP address.<br />If you plan to bond eth0 and eth1 (which you will set up in a later phase), we recommend that you enter a static IP address and set up eth0, eth1, and bond0 all on the same subnet.</td></tr>
  <tr><td><code>Enter eth0's IP address: </code></td><td>If you chose static, type the IP address for this hardware unit.</td></tr>
  <tr><td><code>Enter eth0's NETMASK:</code></td><td>If you chose static, type the netmask for this hardware unit.</td></tr>
  <tr><td><code>Enter eth0's Gateway (or type none):</code></td><td>If you chose static, type <b>none</b> or type the gateway for this hardware unit.</td></tr>
  <tr><td><code>Keep this configured nameserver: 10.6.16.10?</code></td><td>Skip; you set up a nameserver in the next phase of configuration.</td></tr>
  <tr><td><code>Would you like to configure eth1?</code></td><td>Type <b>No</b>; you can configure eth1 in the next phase of the configuration.</td></tr>
  <tr><td><code>The firewall for this system is currently disabled. Would you like to enable it?</code></td><td>Skip; you set up the firewall in the next phase of configuration.</td></tr>
  <tr><td><code>Select time zone ('n' for more)</code></td><td>Enter the time zone you want to show on the web interface of the nodes. This setting does not affect activity via SSH or via the REST API.</td></tr>
  <tr><td><code>Would you like to start the Elemental service now?</code></td><td>Type <b>Yes</b>.</td></tr>
</tbody>
</table>


   Then the software is installed. Finally, this message appears:

   ```
   Installation and configuration complete!
   Please open a web browser and point it to https://xxx.xxx.xxx.xxx to get to the web interface.
   Enjoy!
   ```

1. Start a web browser and start the AWS Elemental Server web interface by typing the following:

   ```
   https://<hostname>
   ```

   Make sure the web interface displays.