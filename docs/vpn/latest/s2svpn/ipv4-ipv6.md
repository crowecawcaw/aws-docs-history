# IPv4 and IPv6 traffic in AWS Site-to-Site VPN

Your Site-to-Site VPN connection on a transit gateway can support either IPv4 traffic or IPv6
traffic inside the VPN tunnels. By default, a Site-to-Site VPN connection supports IPv4 traffic
inside the VPN tunnels. You can configure a new Site-to-Site VPN connection to support IPv6 traffic
inside the VPN tunnels. Then, if your VPC and your on-premises network are configured
for IPv6 addressing, you can send IPv6 traffic over the VPN connection.

If you enable IPv6 for the VPN tunnels for your Site-to-Site VPN connection, each tunnel has two
CIDR blocks. One is a size /30 IPv4 CIDR block, and the other is a size /126 IPv6 CIDR
block.

## IPv4 and IPv6 support

Site-to-Site VPN VPN connections support the following IP configurations:

- **IPv4 outer tunnel with IPv4 inner packets** - The basic IPv4 VPN capability supported on virtual private gateways, transit gateways, and Cloud WAN.
- **IPv4 outer tunnel with IPv6 inner packets** - Allows IPv6 applications/transport within the VPN tunnel. Supported on transit gateways and Cloud WAN. This is not supported for virtual private gateways.
- **IPv6 outer tunnel with IPv6 inner packets** - Allows full IPv6 migration with IPv6 addresses for both outer tunnel IPs and inner packet IPs. Supported for both transit gateways and Cloud WAN.
- **IPv6 outer tunnel with IPv4 inner packets** - Allows IPv6 outer tunnel addressing while supporting legacy IPv4 applications within the tunnel. Supported for both transit gateways and Cloud WAN.

The following rules apply:

- IPv6 addresses for outer tunnel IPs are supported only on Site-to-Site VPN connections that
  are terminated on a transit gateway or Cloud WAN. Site-to-Site VPN connections on a virtual
  private gateways do not support IPv6 for outer tunnel IPs.
- When using IPv6 for outer tunnel IPs, you must assign IPv6 addresses on both the AWS side of the VPN connection and your customer gateway for both VPN tunnels.
- You cannot enable IPv6 support for an existing Site-to-Site VPN connection. You must delete the existing connection and create a new one.
- A Site-to-Site VPN connection cannot support both IPv4 and IPv6 traffic simultaneously. The
  inner encapsulated packets can be either IPv6 or IPv4, but not both. You need
  separate Site-to-Site VPN connections to transport IPv4 and IPv6 packets.
- Private IP VPNs do not support IPv6 addresses for outer tunnel IPs. They use either RFC 1918 or CGNAT addresses. For more information about RFC 1918, see [RFC 1918 - Address Allocation for Private Internets](https://datatracker.ietf.org/doc/html/rfc1918 "https://datatracker.ietf.org/doc/html/rfc1918").
- IPv6 VPNs support the same throughput (Gbps and PPS), MTU, and route limits as IPv4 VPNs.
- The IPSec encryption and key exchange work the same way for both IPv4 and IPv6 VPNs.
  For more information about creating a VPN connection with IPv6 support, see [Create a VPN connection](SetUpVPNConnections.md#vpn-create-vpn-connection "SetUpVPNConnections.md#vpn-create-vpn-connection") in Get Started with Site-to-Site VPN.
