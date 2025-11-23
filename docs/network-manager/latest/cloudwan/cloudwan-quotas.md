# AWS Cloud WAN Quotas

Your AWS account has the quotas shown in the following table for AWS Cloud WAN.

The Service Quotas console also provides information about AWS Cloud WAN quotas. You can use the
Service Quotas console to view default quotas and [request quota increases](https://console.aws.amazon.com/servicequotas/home? "https://console.aws.amazon.com/servicequotas/home?") for
adjustable quotas. For more information, see [Requesting a quota
increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the _Service Quotas User Guide_.

## General

The following AWS Cloud WAN general quotas apply.

| Quota                                                                                     | Default                                                   | Adjustable                                                                                                                                                                                                           |
| ----------------------------------------------------------------------------------------- | --------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Global networks per AWS account                                                           | 5                                                         | [Yes](https://us-east-1.console.aws.amazon.com/servicequotas/home/services/networkmanager/quotas/L-2418390E "https://us-east-1.console.aws.amazon.com/servicequotas/home/services/networkmanager/quotas/L-2418390E") |
| Core networks per global network                                                          | 1                                                         | No                                                                                                                                                                                                                   |
| Edges per Region per core network                                                         | 1                                                         | No                                                                                                                                                                                                                   |
| Segments per core network                                                                 | 40                                                        | No                                                                                                                                                                                                                   |
| Retention duration (in seconds) for core network policies with<br>out-of-date change sets | 7776000                                                   | [Yes](https://us-east-1.console.aws.amazon.com/servicequotas/home/services/networkmanager/quotas/L-9C5C59A1 "https://us-east-1.console.aws.amazon.com/servicequotas/home/services/networkmanager/quotas/L-9C5C59A1") |
| Number of policy versions per core network                                                | 10,000                                                    | [Yes](https://us-east-1.console.aws.amazon.com/servicequotas/home/services/networkmanager/quotas/L-3DE56F60 "https://us-east-1.console.aws.amazon.com/servicequotas/home/services/networkmanager/quotas/L-3DE56F60") |
| Size of a core network policy                                                             | 1 MB                                                      | No                                                                                                                                                                                                                   |
| Number of policy versions                                                                 | 10000                                                     | [Yes](https://us-east-1.console.aws.amazon.com/servicequotas/home/services/networkmanager/quotas/L-3DE56F60 "https://us-east-1.console.aws.amazon.com/servicequotas/home/services/networkmanager/quotas/L-3DE56F60") |
| Number of attachments per core network                                                    | 5000                                                      | [Yes](https://us-east-1.console.aws.amazon.com/servicequotas/home/services/networkmanager/quotas/L-A2478D36 "https://us-east-1.console.aws.amazon.com/servicequotas/home/services/networkmanager/quotas/L-A2478D36") |
| Number of core network Connect attachments                                                | No limit, up to 5000 maximum attachments per core network | No                                                                                                                                                                                                                   |
| Number of core network attachments per VPC                                                | 5                                                         | No                                                                                                                                                                                                                   |
| Number of Connect peers per Connect attachment                                            | 4                                                         | No                                                                                                                                                                                                                   |
| Number of Connect peers per Tunnel-less Connect attachment                                | 4                                                         | No                                                                                                                                                                                                                   |
| Number of devices per global network                                                      | 200                                                       | [Yes](https://us-east-1.console.aws.amazon.com/servicequotas/home/services/networkmanager/quotas/L-C3B5632D "https://us-east-1.console.aws.amazon.com/servicequotas/home/services/networkmanager/quotas/L-C3B5632D") |
| Number of sites per global network                                                        | 200                                                       | [Yes](https://us-east-1.console.aws.amazon.com/servicequotas/home/services/networkmanager/quotas/L-DFE018A3 "https://us-east-1.console.aws.amazon.com/servicequotas/home/services/networkmanager/quotas/L-DFE018A3") |
| Number of links per global network                                                        | 200                                                       | [Yes](https://us-east-1.console.aws.amazon.com/servicequotas/home/services/networkmanager/quotas/L-6BD16053 "https://us-east-1.console.aws.amazon.com/servicequotas/home/services/networkmanager/quotas/L-6BD16053") |
| Number of connections per global network                                                  | 500                                                       | [Yes](https://us-east-1.console.aws.amazon.com/servicequotas/home/services/networkmanager/quotas/L-D30F0A50 "https://us-east-1.console.aws.amazon.com/servicequotas/home/services/networkmanager/quotas/L-D30F0A50") |
| Number of transit gateway peers                                                           | 50                                                        | [Yes](https://us-east-1.console.aws.amazon.com/servicequotas/home/services/networkmanager/quotas/L-D30F0A50 "https://us-east-1.console.aws.amazon.com/servicequotas/home/services/networkmanager/quotas/L-D30F0A50") |
| Number of transit gateway routing tables                                                  | No limit                                                  |                                                                                                                                                                                                                      |
| Maximum number of core network attachments per Direct Connect<br>gateway                  | 1                                                         | No                                                                                                                                                                                                                   |
| Maximum number of Direct Connect attachments per core network.                            | 40                                                        | Yes                                                                                                                                                                                                                  |
| Maximum number of prefix list entries per prefix list core network association            | 200                                                       | No                                                                                                                                                                                                                   |
| Maximum number of prefix list core network associations                                   | 100                                                       | No                                                                                                                                                                                                                   |

## Bandwidth

Your AWS account has the following bandwidth quotas for AWS Cloud WAN.

You can use equal-cost multipath routing (ECMP) to get higher VPN bandwidth by
aggregating multiple VPN tunnels. To use ECMP, the VPN connection must be configured for
dynamic routing. ECMP is not supported on VPN connections that use static
routing.

You can create up to four Connect peers per Connect attachment (up to 20 Gbps in total
bandwidth per Connect attachment). You can use ECMP to get higher bandwidth by scaling
horizontally across multiple Connect peers of the same Connect attachment or across
multiple Connect attachments. Core network cannot use ECMP between the BGP peerings of
the same Connect peer.

| Quota                                                                       | Default                              | Adjustable                                                                                          |
| --------------------------------------------------------------------------- | ------------------------------------ | --------------------------------------------------------------------------------------------------- |
| Bandwidth per VPC attachment per Availability Zone                          | Up to 100 Gbps                       | Contact your Solutions Architect (SA) or Technical Account Manager<br>(TAM) for further assistance. |
| Packets per second per core network VPC attachment per Availability<br>Zone | Up to 7,500,000                      | Contact your Solutions Architect (SA) or Technical Account Manager<br>(TAM) for further assistance. |
| Maximum bandwidth per VPN tunnel                                            | Up to 1.25 Gbps                      | No                                                                                                  |
| Maximum bandwidth per Connect peer (GRE tunnel) per Connect<br>attachment   | Up to 5 Gbps                         | No                                                                                                  |
| Maximum bandwidth per Connect peer (Tunnel-less) per Connect<br>attachment  | Up to 100 Gbps per availability zone | Contact your Solutions Architect (SA) or Technical Account Manager<br>(TAM) for further assistance. |

## Routing

Your AWS account has the following routing quotas for AWS Cloud WAN.

| Quota                                                                                                                                                                                                                                                                                                                                                                                                                                              | Default                     | Adjustable |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- | ---------- |
| Routes per core network, across all segments                                                                                                                                                                                                                                                                                                                                                                                                       | 10,000                      | No         |
| Routes advertised over VPN to core network                                                                                                                                                                                                                                                                                                                                                                                                         | 1,000                       | No         |
| Routes advertised from core network over VPN                                                                                                                                                                                                                                                                                                                                                                                                       | 5,000                       | No         |
| Routes advertised over Connect peer to core network                                                                                                                                                                                                                                                                                                                                                                                                | 1,000                       | No         |
| Routes advertised from core network over Connect peer                                                                                                                                                                                                                                                                                                                                                                                              | 5,000                       | No         |
| Maximum number of Tunnel-less Connect routes                                                                                                                                                                                                                                                                                                                                                                                                       | 5,000 outbound1,000 inbound | No         |
| Maximum number of outbound routes per Direct Connect gateway<br>attachmentQuotas applicable to Direct Connect resources<br>(virtual interfaces and Direct Connect gateways) behave in the same<br>way when used with a Cloud WAN core network. For more information, see<br>see [Direct Connect quotas](../../../directconnect/latest/UserGuide/limits.md "../../../directconnect/latest/UserGuide/limits.md") in the _Direct Connect User Guide_. | 5000                        | Yes        |

## Routing Policy

Your AWS account has the following routing policy quotas for AWS Cloud WAN.

| Quota                                                                                                                                 | Default | Adjustable |
| ------------------------------------------------------------------------------------------------------------------------------------- | ------- | ---------- |
| Maximum number of match conditions in a core network routing policy rule                                                              | 5       | No         |
| Maximum number of rules in a core network routing policy                                                                              | 10      | No         |
| Maximum number of routing policies per core network routing policy association type (attachments, segment shares, edge to edge peers) | 5       | No         |

## Maximum transmission unit (MTU)

Your AWS account has the following MTU quotas for AWS Cloud WAN:

- The MTU of a network connection is the size, in bytes, of the largest
  permissible packet that can be passed over the connection. The larger the MTU of
  a connection, the more data that can be passed in a single packet. A Cloud WAN
  core network supports an MTU of 8500 bytes for traffic between VPCs, including
  transit gateway peering and Tunnel-less Connect VPC attachments. Traffic over
  VPN connections can have an MTU of 1500 bytes.
- Packets with a size larger than 8500 bytes that arrive at the core network are
  dropped.
- The core network enforces Maximum Segment Size (MSS) clamping for all packets.
  For more information, see [RFC879](https://tools.ietf.org/html/rfc879 "https://tools.ietf.org/html/rfc879").
- Cloud WAN supports Path MTU Discovery (PMTUD) for traffic ingressing on VPC
  attachments. Transit gateway generates the `FRAG_NEEDED` for ICMPv4
  packets and `Packet Too Big (PTB)` for ICMPv6 packets. Cloud WAN
  does not support PMTUD on Connect, Site-to-site VPN, Direct Connect and Peering
  attachments. For more information about Path MTU Discovery, see [Path
  MTU Discovery](../../../vpc/latest/userguide/path_mtu_discovery.md "../../../vpc/latest/userguide/path_mtu_discovery.md") in the _Amazon VPC User Guide_
