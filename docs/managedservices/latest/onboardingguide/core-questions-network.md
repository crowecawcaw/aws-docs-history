# Network configuration

- Transit Gateway ASN Number

This is the Autonomous System Number (ASN) for the AWS side of a Border Gateway Protocol (BGP) session,
it must be unique and cannot be the same one used for your Direct Connect or VPN. 
The range is 64512 to 65534 (inclusive) for 16-bit ASNs.

- Your AMS multi-account landing zone infrastructure VPC CIDR ranges.

These CIDR ranges cannot overlap with your on-premise network

You can either include a /22 CIDR range, or provide each VPC CIDR individually. Note that only these CIDR ranges are allowed:

    + 10.0.0.0 - 10.255.255.255 (10/8 prefix)
    + 172.16.0.0 - 172.31.255.255 (172.16/12 prefix)
    + 192.168.0.0 - 192.168.255.255 (192.168/16 prefix)

Note that IP range 198.18.0.0/15 may not be used (it is reserved by AWS Directory Service).

    + Core Infrastructure VPC CIDR range (/22 range recommended)
    + Networking VPC CIDR range (/24 range recommended)
    + Shared Services VPC CIDR range (/23 range recommended)
    + DMZ VPC CIDR range (/25 range recommended)

- VPN ECMP (enable or disable)

For VPN ECMP support, choose enable if you need Equal Cost Multipath (ECMP) routing support between VPN connections.
If connections advertise the same CIDRs, the traffic is distributed equally between them.

## Network access control list (NACL)

A network access control list (NACL) is an optional layer of security for your VPC that
acts as a firewall for controlling traffic in and out of one or more subnets. You might
set up network ACLs with rules similar to your security groups in order to add an
additional layer of security to your VPC. For more information about the differences between security groups and network ACLs, see
[Comparison of security groups and network ACLs](../../../vpc/latest/userguide/VPC_Security.md#VPC_Security_Comparison "../../../vpc/latest/userguide/VPC_Security.md#VPC_Security_Comparison").

However, in AMS multi-account landing zone, in order for AMS to effectively manage and monitor Infrastructure, the use of NACLs is limited to following scope:

- NACLs are not supported in the multi-account landing zone core accounts: Management, Networking, Shared-services, Logging, and Security.
- NACLs are supported in multi-account landing zone Application accounts as long as they are only used as a "Deny" list.
  Additionally, they must have "Allow All" configured to ensure AMS monitoring and management operations.

In large scale multi-account environments, you can also leverage features like
centralized egress firewalls to control outbound traffic and/or AWS Transit Gateway routing tables
in AMS multi-account landing zone to segregate network traffic among VPCs.
