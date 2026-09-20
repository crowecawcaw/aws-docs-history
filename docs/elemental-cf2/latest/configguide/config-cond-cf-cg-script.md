

This is version 2.18 of the AWS Elemental Conductor File documentation. This is the latest version. For prior versions, see the *Archive* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server).

# Run the Configuration Script for AWS Elemental Conductor File
<a name="config-cond-cf-cg-script"></a>

Perform this procedure if one of these applies:
+ You have two Conductor File nodes.
+ You want to require users to enter login credentials when working with the cluster (user authentication).

**Getting Ready**  
If you have a redundant Conductor File configuration, designate one of the nodes as the primary Conductor File node and the other as the secondary Conductor File node.

**Configuring AWS Elemental Conductor File**  
If you have a redundant Conductor File configuration, perform this procedure on both nodes: first the primary, and then the secondary. If you have a non-redundant configuration, perform this procedure on the one Conductor File node.

1. From a Linux prompt, log in with the *elemental* user credentials. Once you're logged in, the initial directory is `/home/elemental`.

1. Change to the directory where the configuration script is located:

   ```
   [elemental@hostname ~]$ cd /opt/elemental_se
   ```

1. Run the configuration script as follows:

   ```
   [elemental@hostname elemental_se]$ sudo ./configure
   ```

1. The following prompts appear. Complete each prompt as follows.



<table>
<thead>
  <tr><th>Prompt</th><th>Action</th></tr>
</thead>
<tbody>
  <tr><td><code>Enter this server’s Hostname</code></td><td>This is already set to the value that you entered or accepted during node installation. For more information, see <a href="https://docs.aws.amazon.com/elemental-server/latest/configguide">AWS Elemental Server Configuration Guide</a>.<br />Change the value only if you realize that you have given the same hostname to more than one hardware unit in the cluster.</td></tr>
  <tr><td><code>Is eth0 a management interface?</code></td><td>This is already set to the value that you entered or accepted during node installation. For more information, see <a href="https://docs.aws.amazon.com/elemental-server/latest/configguide">AWS Elemental Server Configuration Guide</a>.</td></tr>
  <tr><td><code>Does eth0 use DHCP to get its IP address?</code></td><td>This is already set to the value that you entered or accepted during node installation. For more information, see <a href="https://docs.aws.amazon.com/elemental-server/latest/configguide">AWS Elemental Server Configuration Guide</a>.</td></tr>
  <tr><td><code>Enter eth0's IP address: </code></td><td>This is already set to the value that you entered or accepted during node installation. For more information, see <a href="https://docs.aws.amazon.com/elemental-server/latest/configguide">AWS Elemental Server Configuration Guide</a>.</td></tr>
  <tr><td><code>Enter eth0's NETMASK:</code></td><td>This is already set to the value that you entered or accepted during node installation. For more information, see <a href="https://docs.aws.amazon.com/elemental-server/latest/configguide">AWS Elemental Server Configuration Guide</a>.</td></tr>
  <tr><td><code>Enter eth0's Gateway (or type none):</code></td><td>This is already set to the value that you entered or accepted during node installation. For more information, see <a href="https://docs.aws.amazon.com/elemental-server/latest/configguide">AWS Elemental Server Configuration Guide</a>.</td></tr>
  <tr><td><code>Keep this configured nameserver: 10.6.16.10?</code></td><td>Skip; you will set up a nameserver on the web interface.</td></tr>
  <tr><td><code>Would you like to configure eth1?</code></td><td>Skip; you will set up more Ethernet devices on the web interface.</td></tr>
  <tr><td><code>The firewall for this system is currently disabled. Would you like to enable it?</code></td><td>Skip; you can set up the firewall on the web interface.</td></tr>
  <tr><td><code>Configure this node as the secondary node?</code></td><td>See the following section <i>Configuring the Conductor Nodes</i>.</td></tr>
  <tr><td><code>Select time zone ('n' for more)</code></td><td>Change the time zone as appropriate. This impacts only the web interface.</td></tr>
  <tr><td><code>Would you like to start the Elemental service now?</code></td><td>Type <b>Yes</b>.</td></tr>
</tbody>
</table>


**Configuring the Conductor File Nodes**  
Take the appropriate action:
+ If you have a redundant configuration and the node that you are configuring is the primary Conductor File node, type **No**.
+ If you have a redundant configuration and the node that you are configuring is the secondary Conductor File node, type **Yes**. At the next prompt, enter the IP address or hostname of the primary node.
+ If you have a non-redundant configuration (only one Conductor File node), type **No**.