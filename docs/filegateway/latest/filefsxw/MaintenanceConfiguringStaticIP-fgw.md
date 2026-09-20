

Amazon FSx File Gateway is no longer available to new customers. Existing customers of FSx File Gateway can continue to use the service normally. For capabilities similar to FSx File Gateway, visit [this blog post](https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/).

# Configuring your gateway network settings
<a name="MaintenanceConfiguringStaticIP-fgw"></a>

The default network configuration for the gateway is Dynamic Host Configuration Protocol (DHCP). With DHCP, your gateway is automatically assigned an IP address. In some cases, you might need to manually assign your gateway's IP as a static IP address, as described following.

**To configure your gateway to use static IP addresses**

1. Log in to your gateway's local console:
   + For more information on logging in to the VMware ESXi local console, see [Accessing the Gateway Local Console with VMware ESXi](accessing-local-console.md#MaintenanceConsoleWindowVMware-common).
   + For more information on logging in to the Microsoft Hyper-V local console, see [Access the Gateway Local Console with Microsoft Hyper-V](accessing-local-console.md#MaintenanceConsoleWindowHyperV-common).
   + For more information on logging in to the KVM local console, see [Accessing the Gateway Local Console with Linux KVM](accessing-local-console.md#MaintenanceConsoleWindowKVM-common).

1. From the **AWS Appliance Activation - Configuration** main menu, enter the corresponding numeral to select **Network Configuration**.

1. From the ** Network Configuration** menu, perform one of the following tasks:


<table>
<thead>
  <tr><th>To Perform This Task</th><th>Do This</th></tr>
</thead>
<tbody>
  <tr><td>Get information about your network adapter</td><td>Enter the corresponding numeral to select <b>Describe Adapter</b>.<br />A list of adapter names appears, and you are prompted to enter an adapter name—for example, <b>eth0</b>. If the adapter you specify is in use, the following information about the adapter is displayed: <ul><li> Media access control (MAC) address </li><li> IP address </li><li> Netmask </li><li> Gateway IP address </li><li> DHCP enabled status </li></ul><br />You use the adapter names listed here when you configure a static IP address or when you set your gateway's default adapter.</td></tr>
  <tr><td>Configure DHCP routing</td><td>Enter the corresponding numeral to select <b>Configure DHCP</b>.<br />You are prompted to configure the network interface to use DHCP.</td></tr>
  <tr><td>Configure a static IP address for your gateway</td><td>Enter the corresponding numeral to select <b>Configure Static IP</b>.<br />You are prompted to enter the following information to configure a static IP: <ul><li> Network adapter name </li><li> IP address </li><li> Netmask </li><li> Default gateway address </li><li> Primary Domain Name Service (DNS) address </li><li> Secondary DNS address </li></ul><br />  If your gateway has already been activated, you must shut it down and restart it from the Storage Gateway console for the settings to take effect. For more information, see <a href="MaintenanceShutDown-common.md">Shutting down your gateway VM</a>. <br />If your gateway uses more than one network interface, you must set all active interfaces to use DHCP or static IP addresses.<br />For example, suppose that your gateway VM uses two interfaces configured as DHCP. If you later set one interface to a static IP, the other interface is deactivated. To activate the interface in this case, you must set it to a static IP.<br />If both interfaces are initially set to use static IP addresses and you then set the gateway to use DHCP, both interfaces use DHCP.</td></tr>
  <tr><td>Configure a hostname for your gateway</td><td>Enter the corresponding numeral to select <b>Configure Hostname</b>.<br />You are prompted to choose whether the gateway will use a static hostname that you specify, or aquire one automatically through DCHP or rDNS.<br />If you select <b>Static</b>, you are prompted to provide a static hostname, such as <code>testgateway.example.com</code>. Enter <code>y</code> to apply the configuration. If you configure a static hostname for your gateway, ensure that the provided hostname is in the domain that gateway is joined to. You must also create an A record in your DNS system that points the gateway's IP address to its static hostname. </td></tr>
  <tr><td>View your gateway's hostname configuration</td><td>Enter the corresponding numeral to select <b>View Hostname Configuration</b>.<br />Your gateway's hostname, aquisition mode, domain, and Active Directory realm are displayed.</td></tr>
  <tr><td>Reset all your gateway's network configuration to DHCP</td><td>Enter the corresponding numeral to select <b>Reset all to DHCP</b>.<br />All network interfaces are set to use DHCP. If your gateway has already been activated, you must shut down and restart your gateway from the Storage Gateway console for the settings to take effect. For more information, see <a href="MaintenanceShutDown-common.md">Shutting down your gateway VM</a>. </td></tr>
  <tr><td>Set your gateway's default route adapter</td><td>Enter the corresponding numeral to select <b>Set Default Adapter</b>.<br />The available adapters for your gateway are shown, and you are prompted to choose one of the adapters—for example, <b>eth0</b>.</td></tr>
  <tr><td>Edit your gateway's DNS configuration</td><td>Enter the corresponding numeral to select <b>Edit DNS Configuration</b>.<br />The available adapters of the primary and secondary DNS servers are displayed. You are prompted to provide the new IP address.</td></tr>
  <tr><td>View your gateway's DNS configuration</td><td>Enter the corresponding numeral to select <b>View DNS Configuration</b>.<br />The available adapters of the primary and secondary DNS servers are displayed. For some versions of the VMware hypervisor, you can edit the adapter configuration in this menu. </td></tr>
  <tr><td>View routing tables</td><td>Enter the corresponding numeral to select <b>View Routes</b>.<br />The default route of your gateway is displayed.</td></tr>
</tbody>
</table>
