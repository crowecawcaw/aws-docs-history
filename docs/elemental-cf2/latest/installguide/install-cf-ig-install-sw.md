

This is version 2.18 of the AWS Elemental Conductor File documentation. This is the latest version. For prior versions, see the *Archive* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server).

# Step C: Install the AWS Elemental Software
<a name="install-cf-ig-install-sw"></a>

These steps must be performed on each node where you are installing AWS Elemental software, either directly at the machine or from your workstation via SSH. 

Make sure that you use the `.run` file that corresponds to the .iso file that you used to set up the operating system on the node. That is, install Conductor File software on the nodes that you kickstarted with the Conductor File `.iso` and worker software on nodes that you kickstarted with the worker `.iso`.

**To install the software**

1. At the Linux command line, log in with the *elemental* user credentials.

1. Run the installer as follows. Use the actual filename of your `.run` file, rather than the example below.

   ```
   [elemental@hostname ~]$ sudo sh ./elemental_production_conductor_file_2.11.nnnnn.run -l -z -t
   ```

   where -l is a letter, not a number.

1. You are prompted as described in the table below.



<table>
<thead>
  <tr><th>Prompt</th><th>Action</th></tr>
</thead>
<tbody>
  <tr><td><code>Enter this server’s Hostname</code></td><td>Accept the suggestion, which is the value that you entered when you installed the .</td></tr>
  <tr><td><code>Is eth0 a management interface?</code></td><td>Type <b>Yes</b>.</td></tr>
  <tr><td><code>Does eth0 use DHCP to get its IP address?</code></td><td>Accept the suggestion.</td></tr>
  <tr><td><code>Enter eth0's IP address: </code></td><td>If the prompt appears, accept the suggestion.</td></tr>
  <tr><td><code>Enter eth0's NETMASK:</code></td><td>If the prompt appears, accept the suggestion.</td></tr>
  <tr><td><code>Enter eth0's Gateway (or type none):</code></td><td>If the prompt appears, accept the suggestion.</td></tr>
  <tr><td><code>Keep this configured nameserver: 10.6.16.10?</code></td><td>Skip; you set up a nameserver in the next phase of configuration.</td></tr>
  <tr><td><code>Would you like to configure eth1?</code></td><td>Type <b>No</b>; you can configure eth1 in the next phase of the configuration.</td></tr>
  <tr><td><code>The firewall for this system is currently disabled. Would you like to enable it?</code></td><td>Skip; you set up the firewall in the next phase of configuration.</td></tr>
  <tr><td><code>Select time zone ('n' for more)</code></td><td>Enter the time zone you want to show on the web interface of the nodes. This setting does not affect activity via SSH or via the REST API.</td></tr>
  <tr><td><code>Would you like to start the Elemental service now?</code></td><td>Type <b>Yes</b>.</td></tr>
</tbody>
</table>


   Then the software will be installed. Finally, this message appears when installation and configuration are complete:

   ```
   Installation and configuration complete!
   Please open a web browser and point it to https://xxx.xxx.xxx.xxx to get to the web interface.
   Enjoy!
   ```

1. Start a web browser and start the AWS Elemental Conductor File web interface by typing the following:

   ```
   https://<hostname>
   ```

   Make sure the web interface displays.