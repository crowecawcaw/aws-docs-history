# Configuring a SOCKS5 proxy for your

on-premises gateway

Volume Gateways and Tape Gateways support configuration of a Socket Secure version 5
(SOCKS5) proxy between your on-premises gateway and AWS.

###### Note

The only supported proxy configuration is SOCKS5.

If your gateway must use a proxy server to communicate to the internet, then you need
to configure the SOCKS proxy settings for your gateway. You do this by specifying an IP
address and port number for the host running your proxy. After you do so, Storage Gateway routes
all traffic through your proxy server. For information about network requirements for
your gateway, see [Network and firewall requirements](Requirements.md#networks "Requirements.md#networks").

The following procedure shows you how to configure SOCKS proxy for Volume Gateway and
Tape Gateway.

###### To configure a SOCKS5 proxy for volume and

Tape Gateways

1. Log in to your gateway's local console.
   - VMware ESXi – for more information, see [Accessing the Gateway Local
     Console with VMware ESXi](accessing-local-console.md#MaintenanceConsoleWindowVMware-common "accessing-local-console.md#MaintenanceConsoleWindowVMware-common").
   - Microsoft Hyper-V – for more information, see [Access the Gateway Local Console
     with Microsoft Hyper-V](accessing-local-console.md#MaintenanceConsoleWindowHyperV-common "accessing-local-console.md#MaintenanceConsoleWindowHyperV-common").
   - KVM – for more information, see [Accessing the Gateway Local Console
     with Linux KVM](accessing-local-console.md#MaintenanceConsoleWindowKVM-common "accessing-local-console.md#MaintenanceConsoleWindowKVM-common").

2. From the **AWS Storage Gateway - Configuration** main menu, enter
   the corresponding numeral to select **SOCKS Proxy
   Configuration**.
3. From the **AWS Storage Gateway SOCKS Proxy Configuration** menu,
   enter the corresponding numeral to perform one of the following tasks:

| To Perform This Task                       | Do This                                                                                                                                                                                                                                                             |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| Configure a SOCKS proxy                    | Enter the corresponding numeral to select **Configure SOCKS Proxy**. You will need to supply a host name and port to complete configuration.                                                                                                                        |
| View the current SOCKS proxy configuration | Enter the corresponding numeral to select **View Current SOCKS Proxy Configuration**. If a SOCKS proxy is not configured, the message `SOCKS Proxy not configured` is displayed. If a SOCKS proxy is configured, the host name and port of the proxy are displayed. |
| Remove a SOCKS proxy configuration         | Enter the corresponding numeral to select **Remove SOCKS Proxy Configuration**. The message `SOCKS Proxy Configuration Removed` is displayed.                                                                                                                       | 4. Restart your VM to apply your HTTP configuration. |
