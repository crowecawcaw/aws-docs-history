# Connections to Your VPC for WorkSpaces Pools

To enable WorkSpaces Pools connectivity to network resources and the internet, configure
your WorkSpaces as follows.

## Network Interfaces

Each WorkSpaces in WorkSpaces Pools has the following network interfaces:

- The customer network interface provides connectivity to the resources
  within your VPC, as well as the internet, and is used to join the WorkSpaces to
  your directory.
- The management network interface is connected to a secure WorkSpaces Pools
  management network. It is used for interactive streaming of the WorkSpace to
  a user's device, and to allow WorkSpaces Pools to manage the WorkSpace.

WorkSpaces Pools selects the IP address for the management network interface from the
following private IP address range: 198.19.0.0/16. Do not use this range for your
VPC CIDR or peer your VPC with another VPC with this range, as this might create a
conflict and cause WorkSpaces to be unreachable. Also, do not modify or delete any of the
network interfaces attached to a WorkSpace, as this might also cause the WorkSpace
to become unreachable.

## Management Network Interface IP Address

Range and Ports

The management network interface IP address range is 198.19.0.0/16. The following
ports must be open on the management network interface of all WorkSpaces:

- Inbound TCP on port 8300. This is used for establishment of the streaming
  connection.
- Outbound TCP on port 3128. This is used for management of WorkSpaces.
- Inbound TCP on ports 8000 and 8443. These are used for management of the
  WorkSpaces.
- Inbound UDP on port 8300. This is used for establishment of the streaming
  connection over UDP.

Limit the inbound range on the management network interface to
198.19.0.0/16.

###### Note

For Amazon DCV BYOL Windows WorkSpaces Pools, the 10.0.0.0/8 IP address ranges are used in
all AWS Regions. These IP ranges are in addition to the /16 CIDR block that you
choose for management traffic in your BYOL WorkSpaces Pools.

Under normal circumstances, WorkSpaces Pools correctly configures these ports for your
WorkSpaces. If any security or firewall software is installed on a WorkSpace that blocks
any of these ports, the WorkSpaces might not function correctly or might be
unreachable.

Do not disable IPv6. If you disable IPv6, WorkSpaces Pools will not function correctly.
For information about configuring IPv6 for Windows, see [Guidance for configuring IPv6 in Windows for advanced users](https://support.microsoft.com/en-us/help/929852/guidance-for-configuring-ipv6-in-windows-for-advanced-users "https://support.microsoft.com/en-us/help/929852/guidance-for-configuring-ipv6-in-windows-for-advanced-users").

###### Note

WorkSpaces Pools relies on the DNS servers within your VPC to return a non-existent
domain (NXDOMAIN) response for local domain names that don’t exist. This enables
the WorkSpaces Pools-managed network interface to communicate with the management
servers.

When you create a directory with Simple AD, AWS Directory Service creates two domain
controllers that also function as DNS servers on your behalf. Because the domain
controllers don't provide the NXDOMAIN response, they can't be used with
WorkSpaces Pools.

## Customer Network Interface Ports

- For internet connectivity, the following ports must be open to all
  destinations. If you are using a modified or custom security group, you need
  to add the required rules manually. For more information, see
  [Security Group Rules](../../../vpc/latest/userguide/VPC_SecurityGroups.md#SecurityGroupRules "../../../vpc/latest/userguide/VPC_SecurityGroups.md#SecurityGroupRules") in the _Amazon VPC User Guide_.
  - TCP 80 (HTTP)
  - TCP 443 (HTTPS)
  - UDP 4195

- If you join your WorkSpaces to a directory, the following ports must be open
  between your WorkSpaces Pools VPC and your directory controllers.

      + TCP/UDP 53 - DNS
      + TCP/UDP 88 - Kerberos authentication
      + UDP 123 - NTP
      + TCP 135 - RPC
      + UDP 137-138 - Netlogon
      + TCP 139 - Netlogon
      + TCP/UDP 389 - LDAP
      + TCP/UDP 445 - SMB
      + TCP 1024-65535 - Dynamic ports for RPC

  For a complete list of ports, see [Active Directory and Active Directory Domain Services Port
  Requirements](<https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd772723(v=ws.10)> "https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd772723(v=ws.10)") in the Microsoft documentation.

- All WorkSpaces require that port 80 (HTTP) be open to IP address
  `169.254.169.254` to allow access to the EC2 metadata
  service. The IP address range `169.254.0.0/16` is reserved for
  WorkSpaces Pools service usage for management traffic. Failure to exclude this
  range might result in streaming issues.
