# Traffic Mirroring limitations

This section contains the limitations for Traffic Mirroring.

###### Contents

- [General limitations](#traffic-mirroring-network-limitations-gen "#traffic-mirroring-network-limitations-gen")
- [MTU and packet length limitations](#traffic-mirroring-mtu "#traffic-mirroring-mtu")
- [Traffic bandwidth and prioritization
  limitations](#traffic-mirroring-bandwidth "#traffic-mirroring-bandwidth")
- [Checksum offloading limitations](#traffic-checksum-offloading "#traffic-checksum-offloading")

## General limitations

This section contains general Traffic Mirroring limitations.

###### IPv6 traffic

Traffic Mirroring is not supported for IPv6-only subnets.

###### Traffic types

Traffic Mirroring can't mirror the following traffic types:

- ARP
- DHCP
- Instance metadata service
- NTP
- Windows activation

###### VPC Flow Logs

VPC Flow Logs do not capture mirrored traffic.

###### Shared VPCs and subnets

- Participants cannot describe, create, modify, or delete a traffic mirror
  session or target that belongs to the VPC owner. Participants can describe,
  create, modify, and delete a traffic mirror session or target that belongs to
  them.
- VPC owners cannot describe, create, modify, or delete a traffic mirror session
  or target that belongs to the participant.

For more information see, [Share your VPC with other
accounts](../userguide/vpc-sharing.md "../userguide/vpc-sharing.md") in the _Amazon VPC User Guide_.

###### Sources

You can only use [requester-managed
network interfaces](../../../AWSEC2/latest/UserGuide/requester-managed-eni.md "../../../AWSEC2/latest/UserGuide/requester-managed-eni.md") created by Amazon RDS or Amazon ElastiCache as a Traffic Mirroring source in a session.

## MTU and packet length limitations

We truncate the packet to the MTU value when both of the following are true:

- The traffic mirror target is a standalone instance.
- The mirrored traffic packet size is greater than the traffic mirror target MTU
  value.

For example, if an 8996 byte packet is mirrored, and the traffic mirror target MTU
value is 9001 bytes, the mirror encapsulation results in the mirrored packet being
greater than the MTU value. In this case, the mirror packet is truncated. To prevent
mirror packets from being truncated, set the traffic mirror source interface MTU value to
54 bytes less than the traffic mirror target MTU value for IPv4 and 74 bytes less than
the traffic mirror target MTU value when you use IPv6. Therefore, the maximum MTU value
supported by Traffic Mirroring with no packet truncation is 8947 bytes.

In addition, the packet length cannot be less than 35 bytes (for IPv4 traffic) and 55
bytes (for IPv6 traffic).

For more information about configuring the network MTU value, see [Network maximum transmission unit (MTU)](../../../AWSEC2/latest/UserGuide/network_mtu.md "../../../AWSEC2/latest/UserGuide/network_mtu.md")
in the _Amazon EC2 User Guide_.

## Traffic bandwidth and prioritization

limitations

Mirrored traffic counts toward instance bandwidth. For example, if you mirror a
network interface that has 1 Gbps of inbound traffic and 1 Gbps of outbound traffic, the
instance must handle 4 Gbps of traffic (1 Gbps inbound, 1 Gbps mirrored inbound, 1 Gbps
outbound, and 1 Gbps mirrored outbound) and your packet size should be equal to or
greater than 1500 Bytes. Note that [the per flow limit
for EC2 instances not in placement groups is 5 Gbps](../../../AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.md "../../../AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.md"). For instances not in
placement groups, the per flow throughput should be lower than 2.5 Gbps or mirrored
packets is dropped.

By default, each Gateway Load Balancer endpoint can support a bandwidth of up to 10 Gbps per
Availability Zone and automatically scales up to 100 Gbps. For more information, see
[AWS PrivateLink quotas](../privatelink/vpc-limits-endpoints.md "../privatelink/vpc-limits-endpoints.md") in the
_AWS PrivateLink Guide_.

If the network traffic exceeds the bandwidth or packet-per-second (PPS) limits of an
instance, mirrored traffic is dropped. This gives production traffic priority when there
is traffic congestion. However, if production traffic continues to exceed the bandwidth
or PPS limits, it is also dropped. Mirrored traffic might also be dropped at lower
bandwidths if the average packet size of your traffic is small.

## Checksum offloading limitations

The Elastic Network Adapter (ENA) provides checksum offloading capabilities. If a
packet is truncated, this might result in the packet checksum not being calculated for
the mirrored packet. The following checksums are not calculated when the mirrored packet
is truncated:

- If the mirror packet is truncated, the mirror packet L4 checksum is not
  calculated.
- If any part of the L3 header is truncated, the L3 checksum is not
  calculated.

If this causes issues, you can disable ENA checksum offloading on the ENA for the
source. For example, use the following commands on Amazon Linux 2:

```
`[ec2-user ~]$` sudo ethtool --offload eth0 tx off
`[ec2-user ~]$` sudo ethtool --show-offload eth0`Features for eth0:
rx-checksumming: on
tx-checksumming: off
 tx-checksum-ipv4: off
 tx-checksum-ip-generic: off [fixed]
 tx-checksum-ipv6: off [fixed]
 tx-checksum-fcoe-crc: off [fixed]
 tx-checksum-sctp: off [fixed]`
```
