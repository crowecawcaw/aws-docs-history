

# Step C: Install the AWS Elemental Software
<a name="install-vm-cl3-ig-install-sw"></a>

1. Use SCP to move each AWS Elemental software installer (`.run` file) to the `/home/elemental` directory on the appropriate virtual machine (VM). Use the *elemental* user credentials.

1. From the VMware vSPhere client, choose **Open Console** and access the VM with the elemental username and default password.

   You are logged in at the home directory (/home/elemental).

1. Run the installer as follows. When you do this use the actual file name of your `.run` file, rather than the file name in the example below.

   ```
   [elemental@hostname ~]$ sudo sh ./{{<product>}} -xeula -l -z
   ```

   Where:
   + {{<product>}} is the file name of the file that you downloaded. For example, `elemental_production_conductor_live247_3.25.5.12345.run`.
   + -l is a letter, not a number. 

1. You are prompted as described in the table below.



<table>
<thead>
  <tr><th>Prompt</th><th>Action</th></tr>
</thead>
<tbody>
  <tr><td><code>Enter this server’s Hostname</code></td><td>Accept the suggestion, which is the value that you entered when you installed the OVA.</td></tr>
  <tr><td><code>Does eth0 use DHCP to get its IP address?</code></td><td>Accept the suggestion.</td></tr>
  <tr><td><code>Enter eth0's IP address: </code></td><td>If the prompt appears, accept the suggestion.</td></tr>
  <tr><td><code>Enter eth0's NETMASK:</code></td><td>If the prompt appears, accept the suggestion.</td></tr>
  <tr><td><code>Enter eth0's Gateway (or type none):</code></td><td>If the prompt appears, accept the suggestion.</td></tr>
  <tr><td><code>Keep this configured nameserver?</code></td><td>Skip; you set up a nameserver in the next phase of configuration.</td></tr>
  <tr><td><code>Would you like to configure eth1?</code></td><td>Type <b>No</b>; you can configure eth1 in the next phase of the configuration.</td></tr>
  <tr><td><code>The firewall for this system is currently disabled. Would you like to enable it?</code></td><td>Skip; you set up the firewall in the next phase of configuration.</td></tr>
  <tr><td><code>For security purposes, we require that you change the default password.</code></td><td>This prompt is shown if you are still using the default password.</td></tr>
  <tr><td><code>Would you like to start the Elemental service now?</code></td><td>Type <b>Yes</b>.</td></tr>
</tbody>
</table>


   The software is installed. This message confirms both installation and configuration are complete:

   ```
   Installation and configuration complete!
   Please open a web browser and point it to https://xxx.xxx.xxx.xxx to get to the web interface.
   Enjoy!
   ```

1. Take a snapshot of the VM as described in the CentOS 7 Virtual Manager online help.

1. Start a web browser and start the Conductor Live web interface by typing:

   ```
   https://<hostname>
   ```

   Make sure the web interface displays.