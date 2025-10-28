# Configuring an HTTP proxy

File Gateways support configuration of an HTTP proxy.

###### Note

The only proxy configuration that File Gateways support is HTTP.

If your gateway must use a proxy server to communicate to the internet, then you need
to configure the HTTP proxy settings for your gateway. You do this by specifying an IP
address and port number for the host running your proxy. After you do so, Storage Gateway routes
all AWS endpoint traffic through your proxy server. Communications between the gateway
and endpoints is encrypted, even when using the HTTP proxy. For information about
network requirements for your gateway, see [Network and firewall requirements](Requirements.md#networks "Requirements.md#networks").

###### To configure an HTTP proxy for a File Gateway

1. Log in to your gateway's local console:
   - For more information on logging in to the VMware ESXi local console,
     see [Accessing the Gateway Local
     Console with VMware ESXi](accessing-local-console.md#MaintenanceConsoleWindowVMware-common "accessing-local-console.md#MaintenanceConsoleWindowVMware-common").
   - For more information on logging in to the Microsoft Hyper-V local
     console, see [Access the Gateway Local Console
     with Microsoft Hyper-V](accessing-local-console.md#MaintenanceConsoleWindowHyperV-common "accessing-local-console.md#MaintenanceConsoleWindowHyperV-common").
   - For more information on logging in to the local console for the Linux
     Kernel-Based Virtual Machine (KVM), see [Accessing the Gateway Local Console
     with Linux KVM](accessing-local-console.md#MaintenanceConsoleWindowKVM-common "accessing-local-console.md#MaintenanceConsoleWindowKVM-common").

2. From the **AWS Appliance Activation - Configuration** main
   menu, enter the corresponding numeral to select **Configure HTTP
   Proxy**.
3. From the **AWS Appliance Activation HTTP Proxy
   Configuration** menu, enter the corresponding numeral for the task
   you want to perform:
   - **Configure HTTP proxy** - You will need to supply a
     host name and port to complete configuration.
   - **View current HTTP proxy configuration** - If an
     HTTP proxy is not configured, the message `HTTP Proxy not
configured` is displayed. If an HTTP proxy is configured,
     the host name and port of the proxy are displayed.
   - **Remove an HTTP proxy configuration** - The message
     `HTTP Proxy Configuration Removed` is
     displayed.

4. Restart your VM to apply your HTTP configuration settings.
