# Customer Network Interface Ports in Amazon AppStream 2.0

Follow the guidance below for customer network interface ports.

- For internet connectivity, the following ports must be open to all
  destinations. If you are using a modified or custom security group, you need
  to add the required rules manually. For more information, see
  [Security Group Rules](../../../vpc/latest/userguide/VPC_SecurityGroups.md#SecurityGroupRules "../../../vpc/latest/userguide/VPC_SecurityGroups.md#SecurityGroupRules") in the _Amazon VPC User Guide_.
  - TCP 80 (HTTP)
  - TCP 443 (HTTPS)
  - UDP 8433

- If you join your streaming instances to a directory, the following ports must be
  open between your AppStream 2.0 VPC and your directory controllers.

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

- All streaming instances require that port 80 (HTTP) be open to IP address
  `169.254.169.254` to allow access to the EC2 metadata
  service. The IP address range `169.254.0.0/16` is reserved for
  AppStream 2.0 service usage for management traffic. Failure to exclude this range
  might result in streaming issues.
