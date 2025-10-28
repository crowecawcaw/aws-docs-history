Amazon FSx File Gateway is no longer available to new customers. Existing
customers of FSx File Gateway can continue to use the service normally. For capabilities
similar to FSx File Gateway, visit [this blog post](https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/ "https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/").

# Performing tasks on the virtual machine local

console

For a File Gateway deployed on-premises, you can perform the following maintenance tasks
using the VM host's local console. These tasks are common to VMware, Microsoft Hyper-V,
and Linux Kernel-based Virtual Machine (KVM) hypervisors.

**Topics**

- [Logging in to the File Gateway local console](LocalConsole-login-fgw.md "LocalConsole-login-fgw.md") -
  Learn how to login to the local console where you can configure gateway network
  settings and change the default password.
- [Configuring an HTTP proxy](MaintenanceRoutingProxy-fgw.md "MaintenanceRoutingProxy-fgw.md") - Learn how to configure Storage Gateway
  to route all AWS endpoint traffic through a proxy server.
- [Configuring your gateway network
  settings](MaintenanceConfiguringStaticIP-fgw.md "MaintenanceConfiguringStaticIP-fgw.md") - Learn how to configure
  your gateway to use DHCP or a static IP address.
- [Testing your gateway's network
  connectivity](MaintenanceTestGatewayConnectivity-fgw.md "MaintenanceTestGatewayConnectivity-fgw.md") - Learn how to use the
  gateway local console to test network connectivity.
- [Viewing your gateway system resource
  status](system-resource-check-fgw.md "system-resource-check-fgw.md") - Learn how to check your gateway's
  virtual CPU cores, root volume size, and RAM.
- [Configuring a Network Time Protocol (NTP)
  server for your gateway](MaintenanceTimeSync-fgw.md "MaintenanceTimeSync-fgw.md")

* Learn how to view and edit Network Time Protocol (NTP) server configurations and
  synchronize the time on your gateway with your hypervisor host.

- [Running Storage Gateway commands on the
  local console](MaintenanceGatewayConsole-fgw.md "MaintenanceGatewayConsole-fgw.md") - Learn how to run local console
  commands to perform tasks such as saving routing tables, connecting to Support, and
  more.
