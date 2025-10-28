# Path MTU Discovery and network ACLs

Path MTU Discovery is used to determine the path MTU between two devices. The path MTU is
the maximum packet size that's supported on the path between the originating host and the
receiving host.

For IPv4, when a host sends a packet that's larger than the MTU of the receiving host or
that's larger than the MTU of a device along the path, the receiving host or device drops the
packet, and then returns the following ICMP message: `Destination Unreachable:
 Fragmentation Needed and Don't Fragment was Set` (Type 3, Code 4). This instructs the
transmitting host to split the payload into multiple smaller packets, and then retransmit
them.

The IPv6 protocol does not support fragmentation in the network. When a host sends a
packet that's larger than the MTU of the receiving host or that's larger than the MTU of a
device along the path, the receiving host or device drops the packet, and then returns the
following ICMP message: `ICMPv6 Packet Too Big (PTB)` (Type 2). This instructs the
transmitting host to split the payload into multiple smaller packets, and then retransmit
them.

If the maximum transmission unit (MTU) between hosts in your subnets is different, or your
instances communicate with peers over the internet, you must add the following network ACL
rule, both inbound and outbound. This ensures that Path MTU Discovery can function correctly
and prevent packet loss. Select **Custom ICMP Rule** for the type and
**Destination Unreachable**, **fragmentation required, and DF flag
set** for the port range (type 3, code 4). If you use traceroute, also add the
following rule: select **Custom ICMP Rule** for the type and **Time
Exceeded**, **TTL expired transit** for the port range (type 11,
code 0). For more information, see [Network maximum
transmission unit (MTU) for your EC2 instance](../../../AWSEC2/latest/UserGuide/network_mtu.md "../../../AWSEC2/latest/UserGuide/network_mtu.md") in the
_Amazon EC2 User Guide_.
