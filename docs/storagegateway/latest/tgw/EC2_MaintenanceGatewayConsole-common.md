

# Running Storage Gateway commands on the local console
<a name="EC2_MaintenanceGatewayConsole-common"></a>

The AWS Storage Gateway console helps provide a secure environment for configuring and diagnosing issues with your gateway. Using the console commands, you can perform maintenance tasks such as saving routing tables or connecting to Support. 

**To run a configuration or diagnostic command**

1. Log in to your gateway's local console. For instructions, see [Logging In to Your Amazon EC2 Gateway Local Console](EC2_MaintenanceConsoleWindow-common.md).

1. From the **AWS Appliance Activation - Configuration** main menu, enter the corresponding numeral to select **Gateway Console**.

1. From the gateway console command prompt, enter `h`.

   The console displays the **AVAILABLE COMMANDS** menu, which lists the available commands:


<table>
<thead>
  <tr><th>Command</th><th>Function</th></tr>
</thead>
<tbody>
  <tr><td>dig</td><td>Collect output from dig for DNS troubleshooting.</td></tr>
  <tr><td>exit</td><td>Return to Configuration menu.</td></tr>
  <tr><td>h</td><td>Display available command list.</td></tr>
  <tr><td>ifconfig</td><td>View or configure network interfaces.  We recommend configuring network or IP settings using the Storage Gateway console or the dedicated local console menu option. </td></tr>
  <tr><td>ip</td><td>Show / manipulate routing, devices, and tunnels.  We recommend configuring network or IP settings using the Storage Gateway console or the dedicated local console menu option. </td></tr>
  <tr><td>iptables</td><td>Administration tool for IPv4 packet filtering and NAT.</td></tr>
  <tr><td>ip6tables</td><td>Administration tool for IPv6 packet filtering and NAT.</td></tr>
  <tr><td>ncport</td><td>Test connectivity to a specific TCP port on a network.</td></tr>
  <tr><td>nping</td><td>Collect output from nping for network troubleshooting.</td></tr>
  <tr><td>open-support-channel</td><td>Connect to AWS Support.</td></tr>
  <tr><td>save-iptables</td><td>Persist IP tables.</td></tr>
  <tr><td>save-routing-table</td><td>Save newly added routing table entry.</td></tr>
  <tr><td>sslcheck</td><td>Check SSL validity for network troubleshooting.</td></tr>
  <tr><td>tcptraceroute</td><td>Collect traceroute output on TCP traffic to a destination.</td></tr>
</tbody>
</table>


1. From the gateway console command prompt, enter the corresponding command for the function you want to use, and follow the instructions.

To learn about a command, enter the command name followed by the `-h` option, for example: `sslcheck -h`.