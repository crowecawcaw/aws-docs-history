# Routing your gateway deployed on

EC2 through an HTTP proxy

Storage Gateway supports the configuration of a Socket Secure version 5 (SOCKS5) proxy between
your gateway deployed on Amazon EC2 and AWS.

If your gateway must use a proxy server to communicate to the internet, then you need
to configure the HTTP proxy settings for your gateway. You do this by specifying an IP
address and port number for the host running your proxy. After you do so, Storage Gateway routes
all AWS endpoint traffic through your proxy server. Communications between the gateway
and endpoints is encrypted, even when using the HTTP proxy.

###### To route your gateway internet traffic through a local proxy server

1. Log in to your gateway's local console. For instructions, see [Logging In to Your Amazon EC2 Gateway
   Local Console](EC2_MaintenanceConsoleWindow-common.md "EC2_MaintenanceConsoleWindow-common.md").
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
