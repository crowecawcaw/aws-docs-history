Amazon FSx File Gateway is no longer available to new customers. Existing
customers of FSx File Gateway can continue to use the service normally. For capabilities
similar to FSx File Gateway, visit [this blog post](https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/ "https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/").

# Running Storage Gateway commands on the

local console

The VM local console in Storage Gateway helps provide a secure environment for
configuring and diagnosing issues with your gateway. Using the local console commands,
you can perform maintenance tasks such as saving routing tables, connecting to Support,
and so on.

###### To run a configuration or diagnostic command

1. Log in to your gateway's local console:
   - For more information on logging in to the VMware ESXi local console,
     see [Accessing the Gateway Local
     Console with VMware ESXi](accessing-local-console.md#MaintenanceConsoleWindowVMware-common "accessing-local-console.md#MaintenanceConsoleWindowVMware-common").
   - For more information on logging in to the Microsoft Hyper-V local
     console, see [Access the Gateway Local Console
     with Microsoft Hyper-V](accessing-local-console.md#MaintenanceConsoleWindowHyperV-common "accessing-local-console.md#MaintenanceConsoleWindowHyperV-common").
   - For more information on logging in to the KVM local console, see [Accessing the Gateway Local Console
     with Linux KVM](accessing-local-console.md#MaintenanceConsoleWindowKVM-common "accessing-local-console.md#MaintenanceConsoleWindowKVM-common").

2. From the **AWS Appliance Activation - Configuration** main
   menu, enter the corresponding numeral to select **Gateway
   Console**.
3. From the gateway console command prompt, enter
   `h`.

The console displays the **AVAILABLE COMMANDS** menu, which
lists the available commands:

| Command              | Function                                                                                                                                                                                                                                                                                                                                                                           |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| dig                  | Collect output from dig for DNS troubleshooting.                                                                                                                                                                                                                                                                                                                                   |
| exit                 | Return to Configuration menu.                                                                                                                                                                                                                                                                                                                                                      |
| h                    | Display available command list.                                                                                                                                                                                                                                                                                                                                                    |
| ifconfig             | View or configure network interfaces. NoteWe recommend configuring network or IP settings using the Storage Gateway console or the dedicated local console menu option. For instructions, see [Configuring your gateway network settings](manage-on-premises-fgw.md#MaintenanceConfiguringStaticIP-fgw "manage-on-premises-fgw.md#MaintenanceConfiguringStaticIP-fgw").            |
| ip                   | Show / manipulate routing, devices, and tunnels. NoteWe recommend configuring network or IP settings using the Storage Gateway console or the dedicated local console menu option. For instructions, see [Configuring your gateway network settings](manage-on-premises-fgw.md#MaintenanceConfiguringStaticIP-fgw "manage-on-premises-fgw.md#MaintenanceConfiguringStaticIP-fgw"). |
| iptables             | Administration tool for IPv4 packet filtering and NAT.                                                                                                                                                                                                                                                                                                                             |
| ncport               | Test connectivity to a specific TCP port on a network.                                                                                                                                                                                                                                                                                                                             |
| nping                | Collect output from nping for network troubleshooting.                                                                                                                                                                                                                                                                                                                             |
| open-support-channel | Connect to AWS Support. For instructions on how to turn on AWS support access, see [You want AWS Support to help troubleshoot your EC2 gateway](troubleshooting-EC2-gateway-issues.md#EC2-EnableAWSSupportAccess "troubleshooting-EC2-gateway-issues.md#EC2-EnableAWSSupportAccess").                                                                                              |
| passwd               | Update authentication tokens.                                                                                                                                                                                                                                                                                                                                                      |
| save-iptables        | Persist IP tables.                                                                                                                                                                                                                                                                                                                                                                 |
| save-routing-table   | Save newly added routing table entry.                                                                                                                                                                                                                                                                                                                                              |
| tcptraceroute        | Collect traceroute output on TCP traffic to a destination.                                                                                                                                                                                                                                                                                                                         |
| sslcheck             | Returns output with certificate issuerNoteStorage Gateway uses certificate issuer verification and does not support ssl inspection. If this command returns an issuer other than aws-appliance@amazon.com, then it is likely that an application performing an ssl inspection. In that case, we recommend bypassing ssl inspection for the Storage Gateway appliance.              | 4. From the gateway console command prompt, enter the corresponding command for the function you want to use, and follow the instructions. To learn about a command, enter `man` + `command name` at the command prompt. |
