# AWS Transit Gateway Quotas

Your AWS account has the following quotas (previously referred to as
_limits_) related to transit gateways. Unless otherwise noted, each quota
is Region-specific.

The Service Quotas console provides information about the quotas for your account. You can use
the Service Quotas console to view default quotas and [request quota increases](https://console.aws.amazon.com/servicequotas/home? "https://console.aws.amazon.com/servicequotas/home?") for
adjustable quotas. For more information, see [Requesting a quota
increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the _Service Quotas User Guide_.

If an adjustable quota is not yet available in Service Quotas, you can open a support case.

## General

| Name                            | Default | Adjustable                                                                                                                                                                 |
| ------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Transit gateways per account    | 5       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-A2478D36 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-A2478D36") |
| CIDR blocks per transit gateway | 5       | No                                                                                                                                                                         |

The CIDR blocks are used in the [Connect attachments and Connect peers in
AWS Transit Gateway](tgw-connect.md "tgw-connect.md") feature.

## Routing

| Name                                                                                               | Default | Adjustable                                                                                                                                                                 |
| -------------------------------------------------------------------------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Transit gateway route tables per transit gateway                                                   | 20      | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-43872EB7 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-43872EB7") |
| Total combined routes (dynamic and static) across all route tables<br>for a single transit gateway | 10,000  | Contact your Solutions Architect (SA) or Technical Account Manager<br>(TAM) for further assistance.                                                                        |
| Dynamic routes advertised from a virtual router appliance to a Connect peer                        | 1,000   | Contact your Solutions Architect (SA) or Technical Account Manager<br>(TAM) for further assistance.                                                                        |
| Routes advertised from a Connect peer on a transit gateway to a virtual router<br>appliance        | 5,000   | No                                                                                                                                                                         |
| Static routes for a prefix to a single attachment                                                  | 1       | No                                                                                                                                                                         |

Advertised routes come from the route table that's associated with the Connect attachment.

## Transit gateway attachments

A transit gateway cannot have more than one VPC attachment to the same VPC.

| Name                                                                                                                       | Default | Adjustable                                                                                                                                                                 |
| -------------------------------------------------------------------------------------------------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Attachments per transit gateway                                                                                            | 5,000   | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-E0233F82 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-E0233F82") |
| Transit gateways per VPC                                                                                                   | 5       | No                                                                                                                                                                         |
| Peering attachments per transit gateway                                                                                    | 50      | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-A1B5A36F "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-A1B5A36F") |
| Pending peering attachments per transit gateway                                                                            | 10      | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-62499967 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-62499967") |
| Peering attachments between two transit gateways or between one transit gateway and a<br>Cloud WAN core network edge (CNE) | 1       | No                                                                                                                                                                         |
| Connect peers (GRE tunnels) per Connect attachment                                                                         | 4       | No                                                                                                                                                                         |
| VPN Concentrators per transit gateway                                                                                      | 5       | No                                                                                                                                                                         |
| VPN connections per VPN Concentrator                                                                                       | 100     | No                                                                                                                                                                         |

## Bandwidth

There are many factors that can affect realized bandwidth through a Site-to-Site VPN connection,
including but not limited to: packet size, traffic mix (TCP/UDP), shaping or throttling
policies on intermediate networks, internet weather, and specific application
requirements. For VPC attachments, Direct Connect gateways, or peered transit gateway attachments, we
will attempt to provide additional bandwidth beyond the default value.

| Name                                                                                                                                        | Default                                                                    | Adjustable                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| Bandwidth per VPC attachment per Availability Zone                                                                                          | Up to 100 Gbps each direction (i.e., 100 Gbps ingress and 100 Gbps egress) | Contact your Solutions Architect (SA) or Technical Account Manager<br>(TAM) for further assistance. |
| Packets per second per transit gateway VPC attachment per Availability<br>Zone                                                              | Up to 7,500,000                                                            | Contact your Solutions Architect (SA) or Technical Account Manager<br>(TAM) for further assistance. |
| Bandwidth for Direct Connect gateway or peered transit gateway connection<br>per available Availability Zone in the Region                  | Up to 100 Gbps each direction (i.e., 100 Gbps ingress and 100 Gbps egress) | Contact your Solutions Architect (SA) or Technical Account Manager<br>(TAM) for further assistance. |
| Packets per second per transit gateway attachment (Direct Connect and<br>peering attachments) per available Availability Zone in the Region | Up to 7,500,000                                                            | Contact your Solutions Architect (SA) or Technical Account Manager<br>(TAM) for further assistance. |
| Maximum bandwidth per Connect peer (GRE tunnel) per Connect attachment                                                                      | Up to 5 Gbps                                                               | No                                                                                                  |
| Maximum packets per second per Connect peer                                                                                                 | Up to 300,000                                                              | No                                                                                                  |

You can use equal-cost multipath routing (ECMP) to get
higher VPN bandwidth by aggregating multiple VPN tunnels. To use ECMP, the VPN
connection must be configured for dynamic routing. ECMP is not supported on VPN
connections that use static routing.

You can create up to 4 Connect peers per Connect
attachment (up to 20 Gbps in total bandwidth per Connect attachment), as long
as the underlying transport (VPC or Direct Connect) attachment supports the required
bandwidth. You can use ECMP to get higher bandwidth by scaling horizontally
across multiple Connect peers of the same Connect attachment or across
multiple Connect attachments on the same transit gateway. The transit gateway cannot use ECMP
between the BGP peerings of the same Connect peer.

For bandwidth and packet limits with VPN tunnel, please refer to
[VPN bandwidth and throughput](../../../vpn/latest/s2svpn/vpn-limits.md#vpn-quotas-bandwidth "../../../vpn/latest/s2svpn/vpn-limits.md#vpn-quotas-bandwidth") .

## Direct Connect gateways

| Name                                        | Default | Adjustable |
| ------------------------------------------- | ------- | ---------- |
| Direct Connect gateways per transit gateway | 20      | No         |
| Transit gateways per Direct Connect gateway | 6       | No         |

## Maximum transmission unit (MTU)

- The MTU of a network connection is the size, in bytes, of the largest
  permissible packet that can be passed over the connection. The larger the MTU of
  a connection, the more data that can be passed in a single packet. A transit gateway
  supports an MTU of 8500 bytes for traffic between VPCs, Direct Connect, Transit
  Gateway Connect, and peering attachments (intra-Region, inter-Region, and Cloud
  WAN peering attachments). Traffic over VPN connections can have an MTU of 1500
  bytes.
- When migrating from VPC peering to use a transit gateway, an MTU size mismatch between
  VPC peering and the transit gateway might result in some asymmetric traffic packets
  dropping. Update both VPCs at the same time to avoid jumbo packets dropping due
  to a size mismatch.
- The transit gateway enforces Maximum Segment Size (MSS) clamping for all packets. For
  more information, see [RFC879](https://tools.ietf.org/html/rfc879 "https://tools.ietf.org/html/rfc879").
- For details about Site-to-Site VPN quotas for MTU, see [Maximum transmission unit (MTU)](../../../vpn/latest/s2svpn/vpn-limits.md#vpn-quotas-mtu "../../../vpn/latest/s2svpn/vpn-limits.md#vpn-quotas-mtu") in the _AWS Site-to-Site VPN User Guide_.
- Transit gateways support Path MTU Discovery (PMTUD) for traffic ingressing on
  VPC and Connect attachments. Transit gateway generates the
  `FRAG_NEEDED` for ICMPv4 packets and `Packet Too Big
(PTB)` for ICMPv6 packets. Transit gateways does not support PMTUD on
  Site-to-site VPN, Direct Connect, and Peering attachments. For more information
  about Path MTU Discovery, see [Path MTU
  Discovery](../userguide/path_mtu_discovery.md "../userguide/path_mtu_discovery.md") in the _Amazon VPC User Guide_

## Multicast

###### Note

Transit gateway multicast may not be suitable for high-frequency trading or
performance-sensitive applications. We strongly recommend that you review the
following multicast limits. Contact your account or Solution Architect team for a
detailed review of your performance requirements.

| Name                                                                             | Default   | Adjustable                                                                                          |
| -------------------------------------------------------------------------------- | --------- | --------------------------------------------------------------------------------------------------- |
| Multicast domains per transit gateway                                            | 20        | Contact your Solutions Architect (SA) or Technical Account Manager<br>(TAM) for further assistance. |
| Multicast network interfaces per transit gateway                                 | 10,000    | Contact your Solutions Architect (SA) or Technical Account Manager<br>(TAM) for further assistance. |
| Multicast domain associations per VPC                                            | 20        | Contact your Solutions Architect (SA) or Technical Account Manager<br>(TAM) for further assistance. |
| Static and IGMPv2 multicast group members and sources per transit gateway        | 10,000    | No                                                                                                  |
| Static and IGMPv2 multicast group members per transit gateway multicast<br>group | 100       | No                                                                                                  |
| Maximum multicast throughput per flow                                            | 1 Gbps    | No                                                                                                  |
| Maximum aggregate multicast throughput per Availability Zone                     | 20 Gbps   | No                                                                                                  |
| Maximum packets per second per flow (less than 10 receivers)                     | 75,000    | No                                                                                                  |
| Maximum packets per second per flow (greater than 10<br>receivers)               | 15,000    | No                                                                                                  |
| Maximum aggregate packets per second (less than 10 receivers)                    | 2,500,000 | No                                                                                                  |
| Maximum aggregate packets per second (greater than 10<br>receivers)              | 500,000   | No                                                                                                  |

## AWS Network Manager

| Name                            | Default | Adjustable |
| ------------------------------- | ------- | ---------- |
| Global networks per AWS account | 5       | Yes        |
| Devices per global network      | 200     | Yes        |
| Links per global network        | 200     | Yes        |
| Sites per global network        | 200     | Yes        |
| Connections per global network  | 500     | No         |

## Additional quota resources

For more information, see the following:

- [Site-to-Site VPN quotas](../../../vpn/latest/s2svpn/vpn-limits.md "../../../vpn/latest/s2svpn/vpn-limits.md") in the
  _AWS Site-to-Site VPN User Guide_
- [Amazon VPC quotas](../userguide/amazon-vpc-limits.md "../userguide/amazon-vpc-limits.md") in the
  _Amazon VPC User Guide_
- [Direct Connect
  quotas](../../../directconnect/latest/UserGuide/limits.md "../../../directconnect/latest/UserGuide/limits.md") in the _AWS Direct Connect User Guide_
