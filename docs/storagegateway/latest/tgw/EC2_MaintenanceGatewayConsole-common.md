# Running Storage Gateway commands on

the local console

The AWS Storage Gateway console helps provide a secure environment for configuring and
diagnosing issues with your gateway. Using the console commands, you can perform
maintenance tasks such as saving routing tables or connecting to Support.

###### To run a configuration or diagnostic command

1. Log in to your gateway's local console. For instructions, see [Logging In to Your Amazon EC2 Gateway
   Local Console](EC2_MaintenanceConsoleWindow-common.md "EC2_MaintenanceConsoleWindow-common.md").
2. From the **AWS Appliance Activation - Configuration** main
   menu, enter the corresponding numeral to select **Gateway
   Console**.
3. From the gateway console command prompt, enter `h`.

The console displays the **AVAILABLE COMMANDS** menu, which
lists the available commands:

| Command              | Function                                                                                                                                                                                 |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| dig                  | Collect output from dig for DNS troubleshooting.                                                                                                                                         |
| exit                 | Return to Configuration menu.                                                                                                                                                            |
| h                    | Display available command list.                                                                                                                                                          |
| ifconfig             | View or configure network interfaces. NoteWe recommend configuring network or IP settings using<br>the Storage Gateway console or the dedicated local console menu<br>option.            |
| ip                   | Show / manipulate routing, devices, and tunnels. NoteWe recommend configuring network or IP settings using<br>the Storage Gateway console or the dedicated local console menu<br>option. |
| iptables             | Administration tool for IPv4 packet filtering and<br>NAT.                                                                                                                                |
| ip6tables            | Administration tool for IPv6 packet filtering and<br>NAT.                                                                                                                                |
| ncport               | Test connectivity to a specific TCP port on a<br>network.                                                                                                                                |
| nping                | Collect output from nping for network<br>troubleshooting.                                                                                                                                |
| open-support-channel | Connect to AWS Support.                                                                                                                                                                  |
| save-iptables        | Persist IP tables.                                                                                                                                                                       |
| save-routing-table   | Save newly added routing table entry.                                                                                                                                                    |
| sslcheck             | Check SSL validity for network troubleshooting.                                                                                                                                          |
| tcptraceroute        | Collect traceroute output on TCP traffic to a<br>destination.                                                                                                                            |

4. From the gateway console command prompt, enter the corresponding command for
   the function you want to use, and follow the instructions.
   To learn about a command, enter the command name followed by the `-h`
   option, for example: `sslcheck -h`.
