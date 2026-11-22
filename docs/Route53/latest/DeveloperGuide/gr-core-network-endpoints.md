

# Connecting a global resolver to a core network

A *core network endpoint* connects a global resolver to an AWS Cloud WAN (Cloud WAN) core network. After you connect the core network, you can use the core network's segments as access sources for DNS resolution. Clients that reach the global resolver from those segments are authorized the same way as other access sources that you configure.

A core network endpoint connects one global resolver to one Cloud WAN core network. At this time, a global resolver supports a single core network endpoint. For more information about Cloud WAN and core networks, see the [AWS Cloud WAN section of the *AWS Network Manager User Guide*](https://docs.aws.amazon.com/network-manager/latest/cloudwan/what-is-cloudwan.html).

**Note**  
Core networks use an attached core network policy. To enable closest-Region routing so that clients get the most out of a global resolver that you connect to a Cloud WAN core network, update your core network policy to version `2026.10`. For more information, see [Core network policy versions](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-policies-json.html#cloudwan-version-json).

**Note**  
When you connect a core network, the segments of that core network become available as access sources for every AWS Region where your global resolver runs. Only connect core networks that you trust as sources of DNS traffic.

Note the following:

**Segments are used as access sources**  
After you connect a core network, its segments can be used as access sources for DNS resolution. You reference a segment as an access source in the same way that you reference an IP-based access source. For more information about access sources, see [Managing access controls with access sources and tokens in Route 53 Global Resolver](gr-managing-access-controls.md).

**One endpoint connects one core network**  
Each core network endpoint connects one global resolver to one Cloud WAN core network.

**Deleting a core network endpoint**  
When you delete a core network endpoint, the core network's segments are no longer available as access sources for the global resolver. Clients that relied on those segments for authorization can no longer resolve DNS queries through the global resolver. Update your access source configuration before you delete an endpoint that is in use.

**Quotas**  
Core network endpoints are subject to Route 53 Global Resolver quotas. For current quotas, see [Quotas for Route 53 Global Resolver](gr-load-balancer-limits.md).