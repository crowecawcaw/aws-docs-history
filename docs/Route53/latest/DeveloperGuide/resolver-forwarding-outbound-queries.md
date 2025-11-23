# Forwarding outbound DNS queries to your network

To forward DNS queries that originate on Amazon EC2 instances in one or more VPCs to your network, you create an
outbound endpoint and one or more rules:

**Outbound endpoint**
To forward DNS queries from your VPCs to your network, you create an outbound endpoint. An outbound endpoint specifies
the IP addresses that queries originate from. Those IP addresses, which you choose from the range of IP addresses available to your VPC,
aren't public IP addresses. This means that, for each outbound endpoint, you need to connect your VPC to your network using
Direct Connect connection, a VPN connection, or a network address translation (NAT) gateway. Note that you can use the same
outbound endpoint for multiple VPCs in the same Region, or you can create multiple outbound endpoints. If you want your outbound endpoint to use DNS64, you can enable DNS64 using Amazon Virtual Private Cloud. For more information, see [DNS64 and NAT64](../../../vpc/latest/userguide/vpc-nat-gateway.md#nat-gateway-nat64-dns64 "../../../vpc/latest/userguide/vpc-nat-gateway.md#nat-gateway-nat64-dns64") in the _Amazon VPC User
Guide_.

The target IP from the Route 53 Resolver rule is chosen at random by Resolver and there is no preference on choosing a particular target IP over the other.
If a target IP does not respond to the DNS request forwarded, the Resolver will retry to a random IP address among the target IPs.

Make sure that all the target IP addresses are reachable from the Resolver endpoints. If
Resolver is not able forward outbound DNS queries to any of the target IP, it
can lead to extended DNS resolution times.

**Rules**
To specify the domain names of the queries that you want to forward to DNS resolvers on your network, you create
one or more rules. Each forwarding rule specifies one domain name. You then associate rules with the VPCs for which you want
to forward queries to your network.

Outbound delegation rules follow specific delegation principles that differ from standard
forwarding rules. When you create a delegation rule, Route 53 Resolver
evaluates the delegation records in the rule against the NS records in DNS
responses to determine if delegation should occur. The Route 53 Resolver will
delegate authority to your on-premises resolvers only when there's a match
between the delegation rule configuration and the actual NS records returned
in the DNS response. Unlike forwarding rules that
redirect queries based on domain name matching, delegation rules respect the
DNS delegation chain and only activate when the authoritative name servers
in the response match the delegation configuration.

For more information, see the following topics:

- [Private hosted zones that have overlapping namespaces](hosted-zone-private-considerations.md#hosted-zone-private-considerations-private-overlapping "hosted-zone-private-considerations.md#hosted-zone-private-considerations-private-overlapping")
- [Private hosted zones and Route 53 Resolver rules](hosted-zone-private-considerations.md#hosted-zone-private-considerations-resolver-rules "hosted-zone-private-considerations.md#hosted-zone-private-considerations-resolver-rules")
