# Management Network Interface IP Address Range and Ports in Amazon AppStream 2.0

The management network interface IP address range is 198.19.0.0/16. The following
ports must be open on the management network interface of all streaming
instances:

- Inbound TCP on port 8300. This is used for establishment of the streaming
  connection.
- Inbound TCP on ports 8000 and 8443. These are used for management of the
  streaming instance by AppStream 2.0.
- Inbound UDP on port 8300. This is used for establishment of the streaming
  connection over UDP.
- Outbound TCP on port 1688. This is used for Microsoft license included
  application activation on fleet streaming instances.
  Limit the inbound range on the management network interface to
  198.19.0.0/16.

Under normal circumstances, AppStream 2.0 correctly configures these ports for your
streaming instances. If any security or firewall software is installed on a
streaming instance that blocks any of these ports, the streaming instance may not
function correctly or may be unreachable.

Do not disable IPv6. If you disable IPv6, AppStream 2.0 will not function correctly. For information about configuring IPv6 for Windows, see [Guidance for configuring IPv6 in Windows for advanced users](https://support.microsoft.com/en-us/help/929852/guidance-for-configuring-ipv6-in-windows-for-advanced-users "https://support.microsoft.com/en-us/help/929852/guidance-for-configuring-ipv6-in-windows-for-advanced-users").

###### Note

AppStream 2.0 relies on the DNS servers within your VPC to return a non-existent domain
(NXDOMAIN) response for local domain names that don’t exist. This enables the
AppStream 2.0-managed network interface to communicate with the management servers.

When you create a directory with Simple AD, AWS Directory Service creates two domain controllers that also function as DNS servers on your behalf. Because the domain controllers don't provide the
NXDOMAIN response, they can't be used with AppStream 2.0.
