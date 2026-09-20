

# Performing maintenance on your agent
<a name="local-console-vm"></a>

While AWS manages your AWS DataSync agent once it's deployed and activated, there might be cases where you need to change your agent's settings or troubleshoot an issue. Here are some examples of why you'd work with your agent through its local console:
+ Manually assign an IP address to the agent.
+ Check your agent's system resources.

**Important**  
You don't need to use the agent's local console for standard DataSync functionality.

## Accessing your agent's local console
<a name="local-console-login"></a>

How you access the local console depends on the type of agent you're using. 

### Accessing the local console (VMware ESXi, Linux KVM, Nutanix AHV, or Microsoft Hyper-V)
<a name="local-console-login-agent-vm"></a>

For security reasons, you can't remotely connect to the local console of the DataSync agent virtual machine (VM). You must access the local console from your hypervisor management interface.
+ If this is your first time using the local console, log in with the temporary credentials. The initial user name is **admin** and the temporary password is **password**. You must change the password on first log in.
**Note**  
Enhanced mode agents have the following password requirements:  
Must contain a minimum of 15 characters
Must contain at least one uppercase character
Must contain at least one lowercase character
Must contain at least one numeric character
Must contain at least one special character
At least 50% of the characters must change on password update
The password cannot be a dictionary word
**Note**  
After your initial password setup, you can change your password anytime. On the console main menu, enter the number next to **Command Prompt**, then run the `passwd` command to change the password.

### Accessing the local console (Amazon EC2)
<a name="local-console-login-agent-ec2"></a>

To connect to an Amazon EC2 agent's local console, you must use SSH.

**Before you begin**: Make sure that your EC2 instance's security group allows access with SSH (TCP port 22).

1. Open a terminal and copy the following `ssh` command:

   ```
   ssh -i {{/path/key-pair-name}}.pem {{instance-user-name}}@{{instance-public-ip-address}}
   ```
   + For {{/path/key-pair-name}}, specify the path and file name (`.pem`) of the private key required to connect to your instance.
   + For {{instance-user-name}}, specify `admin`.
   + For {{instance-public-ip-address}}, specify the public IP address of your instance.

1. Run the `ssh` command to connect to the instance.

Once connected, the main menu of the agent's local console displays.

## Configuring your agent's DHCP, DNS, and IP settings
<a name="network-configration"></a>

The default network configuration for the agent is Dynamic Host Configuration Protocol (DHCP). With DHCP, your agent is automatically assigned an IP address. In some cases, you might need to manually assign your agent's IP as a static IP address, as described following.

1. Log in to your agent's local console.

1. On the **AWS DataSync Activation - Configuration** main menu, enter **1** to begin configuring your network.

1. On the ** Network Configuration** menu, choose one of the following options.


<table>
<thead>
  <tr><th>To</th><th>Do this</th></tr>
</thead>
<tbody>
  <tr><td>Get information about your network adapter</td><td>Enter <b>1</b>.<br />A list of adapter names appears, and you are prompted to enter an adapter name—for example, <b>eth0</b>. If the adapter you specify is in use, network information for that adapter is displayed, as in the following example:<pre>IP Preference: IPv4<br />MAC address: 52:54:12:a4:f7:7d<br />									<br />IPv4 address: 192.168.100.482<br />Netmask: 255.255.255.0<br />Gateway: 192.168.100.4<br />DHCP enabled: Yes<br />									<br />IPv6 address: abcd:4444:e5ee:fd00::4daf<br />Prefix length: 128<br />Gateway: fe80::5021:ff:ff88:4acd<br />DHCPV6 enabled: Yes<br />									<br />DNS: abcd:4444:e5ee:fd00::1<br />DNS: 192.168.100.4</pre><br />You use the same adapter name when you configure a static IP address (option <b>3</b>) as when you set your agent's default route adapter (option <b>5</b>).</td></tr>
  <tr><td>Configure DHCP</td><td>Enter <b>2</b>.<br />Choose an IP version to use, and then configure the network interface to use DHCP.</td></tr>
  <tr><td>Configure a static IP address for your agent</td><td>Enter <b>3</b>.<br />You are prompted to choose the IP protocol to use, IPv4, IPv6, or both. Then you're prompted to enter the Network adapter name to configure a static IP address.  If your agent has already been activated, you must shut it down and restart it from the DataSync console for the settings to take effect. </td></tr>
  <tr><td>Reset all your agent's network configuration to DHCP</td><td>Enter <b>4</b>.<br />Choose the IP version to reset to DHCP. All network interfaces for the chosen IP version are set to use DHCP.<br />  If your agent has already been activated, you must shut down and restart your agent from the DataSync console for the settings to take effect. </td></tr>
  <tr><td>Set your agent's default route adapter</td><td>Enter <b>5</b>.<br />The available adapters for your agent are shown, and you are prompted to choose one of the adapters—for example, <b>eth0</b>.</td></tr>
  <tr><td>Edit your agent's Domain Name System (DNS) configuration</td><td>Enter <b>6</b>.The available adapters of the primary and secondary DNS servers are displayed. You are prompted to provide the new IP address. </td></tr>
  <tr><td>View your agent's DNS configuration</td><td>Enter <b>7</b>.<br />The available adapters of the primary and secondary DNS servers are displayed.For some versions of the VMware hypervisor, you can edit the adapter configuration in this menu.</td></tr>
  <tr><td>View routing tables</td><td>Enter <b>8</b>.<br />Choose the IP version (IPv4, IPv6, or both) to view the default route table for your agent.</td></tr>
  <tr><td>View your agent's IP version for data transfers</td><td>Enter <b>9</b>.<br />The agent's IP version setting for data transfers displays, either <code>IPv4</code>, <code>IPv6</code>, <code>IPv4 (auto)</code>, or <code>IPv6 (auto)</code>.</td></tr>
  <tr><td>Edit your agent's IP protocol for data transfers</td><td>Enter <b>10</b>.<br />The available IP version settings for data transfers display. You can choose either <code>IPv4</code>, <code>IPv6</code>, <code>IPv4 (auto)</code>, or <code>IPv6 (auto)</code>. For more information about your agent's IP version setting for data transfers, see <a href="datasync-network.md#ipv6-support">IPv6 support</a>.</td></tr>
</tbody>
</table>


## Checking your agent's system resources
<a name="system-resource-check"></a>

When you log in to your agent console, virtual CPU cores, root volume size, and RAM are automatically checked. If there are any errors or warnings, they're flagged on the console menu display with a banner that provides details about those errors or warnings.

If there are no errors or warnings when the console starts, the menu displays white text. The **View System Resource Check** option will display `(0 Errors)`.

If there are errors or warnings, the console menu displays the number of errors and warnings, in red and yellow respectively, in a banner across the top of the menu. For example, `(1 ERROR, 1 WARNING)`.

**To check your agent's system resources**

1. Log in to your agent's local console.

1. On the **AWS DataSync Activation - Configuration** main menu, enter **4** to view the results of the system resource check.

   The console displays an **[OK]**, **[WARNING]**, or **[FAIL]** message for each resource as described in the table following.

   For Amazon EC2 instances, the system resource check verifies that the instance type is one of the instances recommended for use with DataSync. If the instance type matches that list, a single result is displayed in green text, as follows.

   `[ OK ] Instance Type Check`

   If the Amazon EC2 instance is not on the recommended list, the system resource check verifies the following resources.
   + CPU cores check: At least four cores are required.
   + Disk size check: A minimum of 80 GB of available disk space is required.
   + RAM check:
     + 32 GB of RAM assigned to the instance for task executions working with up to 20 million files, objects, or directories.
     + 64 GB of RAM assigned to the instance for task executions working with more than 20 million files, objects, or directories.
   + CPU flags check: The agent VM CPU must have either SSSE3 or SSE4 instruction set flags.

   If the Amazon EC2 instance is not on the list of recommended instances for DataSync, but it has sufficient resources, the result of the system resource check displays four results, all in green text.

   The same resources are verified for agents deployed in Hyper-V, Linux Kernel-based Virtual Machine (KVM), and VMware VMs.

   VMware agents are also checked for supported version; unsupported versions cause a red banner error. Supported versions include VMware versions 6.5 and 6.7.

## View and manage agent system time server configuration
<a name="time-management"></a>

You can view and manage your agent's system time server configuration.

1. Log in to your agent's [local console](#local-console-login).

1. On the **AWS DataSync Activation - Configuration** main menu, enter the option for **System Time Management** (such as **5** for VMware agent).

1. On the **System Time Management** menu, do one of the following:


<table>
<thead>
  <tr><th>To</th><th>Do this</th></tr>
</thead>
<tbody>
  <tr><td>View system time and service status</td><td>Enter <b>1</b>.<br />View the current system time in UTC, time service status, active time servers, and synchronization status.</td></tr>
  <tr><td>Synchronize system time</td><td>Enter <b>2</b>.<br />A prompt displays to synchronize the time server immediately.<br />In some situations, an agent's time might drift. For example, there might be a prolonged network outage and your hypervisor host and agent don't get time updates, so your agent's time is different from the actual time. When there's a time drift like this, a discrepancy occurs between the stated times when operations (such as snapshots occur) and the actual times that the operations occur.</td></tr>
  <tr><td>Restart system time service</td><td>Enter <b>3</b>.<br />A prompt displays to restart the time synchronization service.</td></tr>
  <tr><td>Manage time server configuration</td><td>Enter <b>4</b>.<br />View and manage your time server settings. Add or remove time servers and server pools, and set preferred servers for precise synchronization.</td></tr>
</tbody>
</table>


## Running maintenance-related commands for your agent
<a name="command-prompts"></a>

In your DataSync agent's local console, you can perform some maintenance tasks and diagnose issues with your agent.

**To run a configuration or diagnostic command in your agent's local console**

1. Log in to your [agent's local console](#local-console-login).

1. On the **AWS DataSync Activation - Configuration** main menu, enter **5** (or **6** for a VMware VM) for the **Command Prompt**.

1. Use the following commands to perform the following tasks with your agent.


<table>
<thead>
  <tr><th>Command</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td><b>dig</b></td><td>Look up DNS information about the host.</td></tr>
  <tr><td><b>diskclean</b></td><td>Perform disk cleanup.</td></tr>
  <tr><td><b>exit</b></td><td>Return to the console configuration menu.</td></tr>
  <tr><td><b>h</b></td><td>Display a list of available commands.</td></tr>
  <tr><td><b>ifconfig</b></td><td>Display or configure network interfaces.</td></tr>
  <tr><td><b>ip</b></td><td>Display or configure routing, devices, and tunnels.</td></tr>
  <tr><td><b>iptables</b></td><td>Set up and maintain IPv4 packet filtering and NAT.</td></tr>
  <tr><td><b>ip6tables</b></td><td>Set up and maintain IPv6 packet filtering and NAT.</td></tr>
  <tr><td><b>ncport</b></td><td>Test connectivity to a specific network TCP port.</td></tr>
  <tr><td><b>nping</b></td><td>Get information to troubleshoot network issues.</td></tr>
  <tr><td><b>passwd</b></td><td>Change user password.</td></tr>
  <tr><td><b>save-iptables</b></td><td>Save IPv4 table firewall rules permanently.</td></tr>
  <tr><td><b>save-ip6tables</b></td><td>Save IPv6 table firewall rules permanently.</td></tr>
  <tr><td><b>save-routing-table</b></td><td>Save a newly added routing table entry.</td></tr>
  <tr><td><b>sslcheck</b></td><td>Verify whether an SSL certificate is valid.</td></tr>
  <tr><td><b>tcptraceroute</b></td><td>Collect <code>traceroute</code> output on TCP traffic to a destination. </td></tr>
</tbody>
</table>


1. Follow the onscreen instructions.