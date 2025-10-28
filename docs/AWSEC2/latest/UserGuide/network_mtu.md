# Network maximum transmission unit (MTU) for your EC2 instance

The maximum transmission unit (MTU) of a network connection is the size, in bytes, of the
largest permissible packet that can be passed over the connection. The larger the MTU of a
connection, the more data that can be passed in a single packet. Ethernet frames consist of
the packet, or the actual data you are sending, and the network overhead information that
surrounds it.

Ethernet frames can come in different formats, and the most common format is the standard
Ethernet v2 frame format. It supports 1500 MTU, which is the largest Ethernet packet size
supported over most of the internet. The maximum supported MTU for an instance depends on
its instance type.

All EC2 instance types support 1500 MTU.

###### Contents

- [Jumbo frames (9001 MTU)](#jumbo_frame_instances "#jumbo_frame_instances")
- [Path MTU Discovery](#path_mtu_discovery "#path_mtu_discovery")
- [Set the MTU for your Amazon EC2 instances](ec2-instance-mtu.md "ec2-instance-mtu.md")
- [Troubleshoot](#mtu-troubleshooting "#mtu-troubleshooting")

## Jumbo frames (9001 MTU)

With jumbo frames, you can increase the payload size per packet, thereby increasing
the percentage of the packet that is not packet overhead. With jumbo frames, fewer
packets are needed to send the same amount of usable data. However, certain types
of traffic are subject to the following maximum payloads:

**MTU limit 1500 bytes**

- Traffic over an internet gateway
- Traffic over VPN connections
- Traffic between AWS Regions, unless a transit gateway is used

**MTU limit 8500 bytes**

- Traffic over an inter-region VPC peering connection

If packets are over their MTU limit, they are fragmented, or they are dropped if the
`Don't Fragment` flag is set in the IP header.

Jumbo frames should be used with caution for internet-bound traffic or any traffic
that leaves a VPC. Packets are fragmented by intermediate systems, which slows down this
traffic. To use jumbo frames inside a VPC and not slow traffic that's bound for outside
the VPC, you can configure the MTU size by route, or use multiple elastic network
interfaces with different MTU sizes and different routes.

For instances that are collocated inside a cluster placement group, jumbo frames help to
achieve the maximum network throughput possible, and they are recommended in this case.
For more information, see [Placement groups for your Amazon EC2 instances](placement-groups.md "placement-groups.md").

You can use jumbo frames for traffic between your VPCs and your on-premises networks
over AWS Direct Connect. For more information, and for how to verify Jumbo Frame capability, see
[MTU for private virtual interfaces or transit virtual interfaces](../../../directconnect/latest/UserGuide/WorkingWithVirtualInterfaces.md#set-jumbo-frames-vif.html "../../../directconnect/latest/UserGuide/WorkingWithVirtualInterfaces.md#set-jumbo-frames-vif.html")
in the _AWS Direct Connect User Guide_.

All [current generation](../../../ec2/latest/instancetypes/instance-types.md#current-gen-instances "../../../ec2/latest/instancetypes/instance-types.md#current-gen-instances")
instance types support jumbo frames.
The following [previous generation](../../../ec2/latest/instancetypes/instance-types.md#previous-gen-instances "../../../ec2/latest/instancetypes/instance-types.md#previous-gen-instances")
instance types support jumbo frames:
A1, C3, I2, M3, and R3.

###### Related resources

- For NAT gateways, see [NAT gateway
  basics](../../../vpc/latest/userguide/nat-gateway-basics.md "../../../vpc/latest/userguide/nat-gateway-basics.md") in the _Amazon VPC User Guide_.
- For transit gateways, see [Maximum transmission unit](../../../vpc/latest/tgw/transit-gateway-quotas.md#mtu-quotas "../../../vpc/latest/tgw/transit-gateway-quotas.md#mtu-quotas")
  in the _Amazon VPC Transit Gateways User Guide_.
- For Local Zones, see [Considerations](../../../local-zones/latest/ug/how-local-zones-work.md#considerations "../../../local-zones/latest/ug/how-local-zones-work.md#considerations")
  in the _AWS Local Zones User Guide_.
- For AWS Wavelength, see [Maximum transmission unit](../../../wavelength/latest/developerguide/how-wavelengths-work.md#mtu "../../../wavelength/latest/developerguide/how-wavelengths-work.md#mtu") in the _AWS Wavelength User Guide_.
- For Outposts see [Service link maximum transmission unit requirements](../../../outposts/latest/userguide/region-connectivity.md#sl-max-mtu-requirements "../../../outposts/latest/userguide/region-connectivity.md#sl-max-mtu-requirements") in the _AWS Outposts User Guide_.

## Path MTU Discovery

Path MTU Discovery (PMTUD) is used to determine the path MTU between two devices. The
path MTU is the maximum packet size that's supported on the path between the originating
host and the receiving host. When there is a difference in the MTU size in the network
between two hosts, PMTUD enables the receiving host to respond to the originating host
with an ICMP message. This ICMP message instructs the originating host to use the lowest
MTU size along the network path and to resend the request. Without this negotiation,
packet drop can occur because the request is too large for the receiving host to accept.

For IPv4, when a host sends a packet that's larger than the MTU of the receiving host
or that's larger than the MTU of a device along the path, the receiving host or device
drops the packet, and then returns the following ICMP message: `Destination
 Unreachable: Fragmentation Needed and Don't Fragment was Set` (Type 3, Code
4). This instructs the transmitting host to split the payload into multiple smaller
packets, and then retransmit them.

The IPv6 protocol does not support fragmentation in the network. When a host sends a
packet that's larger than the MTU of the receiving host or that's larger than the MTU of
a device along the path, the receiving host or device drops the packet, and then returns
the following ICMP message: `ICMPv6 Packet Too Big (PTB)` (Type 2). This
instructs the transmitting host to split the payload into multiple smaller packets, and
then retransmit them.

Connections made through some components, like NAT gateways and load balancers, are [automatically tracked](security-group-connection-tracking.md#automatic-tracking "security-group-connection-tracking.md#automatic-tracking"). This means that [security group tracking](security-group-connection-tracking.md "security-group-connection-tracking.md") is automatically enabled for your outbound connection attempts. If connections are automatically tracked or if your security group rules allow inbound ICMP traffic, you can receive PMTUD responses.

Note that ICMP traffic can be blocked even if the traffic is allowed at the security group level, such as if you have a network access control list entry that denies ICMP traffic to the subnet.

###### Important

Path MTU Discovery does not guarantee that jumbo frames will not be dropped by
some routers. An internet gateway in your VPC will forward packets up to 1500 bytes
only. 1500 MTU packets are recommended for internet traffic.

For MTU rules over NAT gateways, see [Maximum transmission unit
(MTU)](../../../vpc/latest/userguide/amazon-vpc-limits.md#ngw-mtus "../../../vpc/latest/userguide/amazon-vpc-limits.md#ngw-mtus") in the _Amazon VPC User Guide_. For MTU rules over
Transit gateways, see [Maximum transmission
unit (MTU)](../../../vpc/latest/tgw/transit-gateway-quotas.md#mtu-quotas "../../../vpc/latest/tgw/transit-gateway-quotas.md#mtu-quotas") in the _AWS Transit Gateway User
Guide_.

## Troubleshoot

If you experience connectivity issues between your EC2 instance and an Amazon Redshift cluster
when using jumbo frames, see [Queries appear to hang and sometimes fail to reach the cluster](../../../redshift/latest/mgmt/troubleshooting-connections.md#connecting-drop-issues "../../../redshift/latest/mgmt/troubleshooting-connections.md#connecting-drop-issues")
in the _Amazon Redshift Management Guide_.
