

# Configuring a SOCKS5 proxy for your on-premises gateway
<a name="MaintenanceRoutingProxy-common"></a>

Volume Gateways and Tape Gateways support configuration of a Socket Secure version 5 (SOCKS5) proxy between your on-premises gateway and AWS. 

**Note**  
The only supported proxy configuration is SOCKS5.

If your gateway must use a proxy server to communicate to the internet, then you need to configure the SOCKS proxy settings for your gateway. You do this by specifying an IP address and port number for the host running your proxy. After you do so, Storage Gateway routes all traffic through your proxy server. For information about network requirements for your gateway, see [Network and firewall requirements](Requirements.md#networks).

The following procedure shows you how to configure SOCKS proxy for Volume Gateway and Tape Gateway.<a name="socks-proxy"></a>

**To configure a SOCKS5 proxy for volume and Tape Gateways**

1. Log in to your gateway's local console.
   + VMware ESXi – for more information, see [Accessing the Gateway Local Console with VMware ESXi](accessing-local-console.md#MaintenanceConsoleWindowVMware-common).
   + Microsoft Hyper-V – for more information, see [Access the Gateway Local Console with Microsoft Hyper-V](accessing-local-console.md#MaintenanceConsoleWindowHyperV-common).
   + KVM – for more information, see [Accessing the Gateway Local Console with Linux KVM](accessing-local-console.md#MaintenanceConsoleWindowKVM-common).

1. From the **AWS Storage Gateway - Configuration** main menu, enter the corresponding numeral to select **SOCKS Proxy Configuration**.

1. From the **AWS Storage Gateway SOCKS Proxy Configuration** menu, enter the corresponding numeral to perform one of the following tasks:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/storagegateway/latest/tgw/MaintenanceRoutingProxy-common.html)

1. Restart your VM to apply your HTTP configuration.