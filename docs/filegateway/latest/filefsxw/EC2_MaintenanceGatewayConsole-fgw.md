Amazon FSx File Gateway is no longer available to new customers. Existing
customers of FSx File Gateway can continue to use the service normally. For capabilities
similar to FSx File Gateway, visit [this blog post](https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/ "https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/").

# Running Storage Gateway commands on the

local console for an Amazon EC2 gateway

The AWS Storage Gateway console helps provide a secure environment for configuring and
diagnosing issues with your gateway. Using the console commands, you can perform
maintenance tasks such as saving routing tables or connecting to Support.

###### To run a configuration or diagnostic command

1. Log in to your gateway's local console. For instructions, see [Logging in to your Amazon EC2 gateway
   local console](EC2_MaintenanceConsoleWindow-fgw.md "EC2_MaintenanceConsoleWindow-fgw.md").
2. From the **AWS Appliance Activation - Configuration** main
   menu, enter the corresponding numeral to select **Gateway
   Console**.
3. From the gateway console command prompt, enter
   `h`.

The console displays the **AVAILABLE COMMANDS** menu, which
lists the available commands:

| Command              | Function                                                                                                                                                                                                                                                                                                                                                                                          |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| dig                  | Collect output from dig for DNS troubleshooting.                                                                                                                                                                                                                                                                                                                                                  |
| exit                 | Return to Configuration menu.                                                                                                                                                                                                                                                                                                                                                                     |
| h                    | Display available command list.                                                                                                                                                                                                                                                                                                                                                                   |
| ifconfig             | View or configure network interfaces. NoteWe recommend configuring network or IP settings using<br>the Storage Gateway console or the dedicated local console menu<br>option. For instructions, see [Configuring your gateway network<br>settings](ec2-local-console-fwg.md#EC2-MaintenanceConfiguringStaticIP-fgw "ec2-local-console-fwg.md#EC2-MaintenanceConfiguringStaticIP-fgw").            |
| ip                   | Show / manipulate routing, devices, and tunnels. NoteWe recommend configuring network or IP settings using<br>the Storage Gateway console or the dedicated local console menu<br>option. For instructions, see [Configuring your gateway network<br>settings](ec2-local-console-fwg.md#EC2-MaintenanceConfiguringStaticIP-fgw "ec2-local-console-fwg.md#EC2-MaintenanceConfiguringStaticIP-fgw"). |
| iptables             | Administration tool for IPv4 packet filtering and<br>NAT.                                                                                                                                                                                                                                                                                                                                         |
| ncport               | Test connectivity to a specific TCP port on a<br>network.                                                                                                                                                                                                                                                                                                                                         |
| nping                | Collect output from nping for network<br>troubleshooting.                                                                                                                                                                                                                                                                                                                                         |
| open-support-channel | Connect to AWS Support.                                                                                                                                                                                                                                                                                                                                                                           |
| save-iptables        | Persist IP tables.                                                                                                                                                                                                                                                                                                                                                                                |
| save-routing-table   | Save newly added routing table entry.                                                                                                                                                                                                                                                                                                                                                             |
| tcptraceroute        | Collect traceroute output on TCP traffic to a<br>destination.                                                                                                                                                                                                                                                                                                                                     |

4. From the gateway console command prompt, enter the corresponding command for
   the function you want to use, and follow the instructions.
   To learn about a command, enter `man` + `command
 name` at the command prompt.
