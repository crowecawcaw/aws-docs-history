# Considerations when creating inbound and outbound endpoints

Before you create inbound and outbound Resolver endpoints in an AWS Region, consider the following issues.

###### Topics

- [Number of inbound and outbound endpoints in each Region](#resolver-considerations-number-of-endpoints "#resolver-considerations-number-of-endpoints")
- [Using the same VPC for inbound and outbound endpoints](#resolver-considerations-same-vpc-inbound-outbound "#resolver-considerations-same-vpc-inbound-outbound")
- [Inbound endpoints
  and private hosted zones](#resolver-considerations-inbound-endpoint-private-zone "#resolver-considerations-inbound-endpoint-private-zone")
- [VPC peering](#resolver-considerations-vpc-peering "#resolver-considerations-vpc-peering")
- [IP addresses in shared subnets](#resolver-considerations-shared-subnets "#resolver-considerations-shared-subnets")
- [Connection between your network and the VPCs that you create endpoints
  in](#resolver-considerations-connection-between-network-and-vpcs "#resolver-considerations-connection-between-network-and-vpcs")
- [When
  you share rules, you also share outbound endpoints](#resolver-considerations-share-rules-share-outbound-endpoints "#resolver-considerations-share-rules-share-outbound-endpoints")
- [Choosing protocols for the endpoints](#resolver-endpoint-protocol-considerations "#resolver-endpoint-protocol-considerations")
- [Using Resolver in VPCs that are configured for dedicated instance tenancy](#resolver-considerations-dedicated-instance-tenancy "#resolver-considerations-dedicated-instance-tenancy")

## Number of inbound and outbound endpoints in each Region

When you want to integrate DNS for the VPCs in an AWS Region with DNS for
your network, you typically need one Resolver inbound endpoint (for DNS
queries that you're forwarding to your VPCs) and one outbound endpoint (for
queries that you're forwarding from your VPCs to your network). You can
create multiple inbound endpoints and multiple outbound endpoints, but one
inbound or outbound endpoint is sufficient to handle the DNS queries for each respective direction. Note
the following:

- For each Resolver endpoint, you specify two or more IP addresses in
  different Availability Zones. Each IP address in an endpoint can
  handle a large number of DNS queries per second. (For the current
  maximum number of queries per second per IP address in an endpoint,
  see [Quotas on Route 53 Resolver](DNSLimitations.md#limits-api-entities-resolver "DNSLimitations.md#limits-api-entities-resolver").) If you need
  Resolver to handle more queries, you can add more IP addresses to your
  existing endpoint instead of adding another endpoint.
- Resolver pricing is based on the number of IP addresses in your
  endpoints and on the number of DNS queries that the endpoint
  processes. Each endpoint includes a minimum of two IP addresses. For
  more information about Resolver pricing, see [Amazon Route 53
  Pricing](https://aws.amazon.com/route53/pricing/ "https://aws.amazon.com/route53/pricing/").
- Each rule specifies the outbound endpoint that DNS queries are
  forwarded from. If you create multiple outbound endpoints in an AWS
  Region and you want to associate some or all Resolver rules with every
  VPC, you need to create multiple copies of those rules.

## Using the same VPC for inbound and outbound endpoints

You can create inbound and outbound endpoints in the same VPC or in
different VPCs in the same Region.

For more information, see [Best practices for Amazon Route 53](best-practices.md "best-practices.md").

## Inbound endpoints

and private hosted zones

If you want Resolver to resolve inbound DNS queries using records in a
private hosted zone, associate the private hosted zone with the VPC that you
created the inbound endpoint in. For information about associating private
hosted zones with VPCs, see [Working with private hosted zones](hosted-zones-private.md "hosted-zones-private.md").

## VPC peering

You can use any VPC in an AWS Region for an inbound or an outbound
endpoint regardless of whether the VPC that you choose is peered with other
VPCs. For more information, see [Amazon Virtual Private
Cloud VPC peering](../../../vpc/latest/peering/what-is-vpc-peering.md "../../../vpc/latest/peering/what-is-vpc-peering.md").

## IP addresses in shared subnets

When you create an inbound or outbound endpoint, you can specify an IP
address in a shared subnet only if the current account created the VPC. If
another account creates a VPC and shares a subnet in the VPC with your
account, you can't specify an IP address in that subnet. For more
information about shared subnets, see [Working with shared VPCs](../../../vpc/latest/userguide/vpc-sharing.md "../../../vpc/latest/userguide/vpc-sharing.md") in
the _Amazon VPC User Guide_.

## Connection between your network and the VPCs that you create endpoints

in

You must have one of the following connections between your network and
the VPCs that you create endpoints in:

- **Inbound endpoints** – You
  must set up either an [Direct Connect](../../../directconnect/latest/UserGuide/Welcome.md "../../../directconnect/latest/UserGuide/Welcome.md") connection or a [VPN connection](../../../vpc/latest/userguide/vpn-connections.md "../../../vpc/latest/userguide/vpn-connections.md")
  between your network and each VPC that you create an inbound
  endpoint for.
- **Outbound endpoints** – You
  must set up an [Direct Connect](../../../directconnect/latest/UserGuide/Welcome.md "../../../directconnect/latest/UserGuide/Welcome.md") connection, a [VPN connection](../../../vpc/latest/userguide/vpn-connections.md "../../../vpc/latest/userguide/vpn-connections.md"),
  or a [network address
  translation (NAT) gateway](../../../vpc/latest/userguide/vpc-nat-gateway.md "../../../vpc/latest/userguide/vpc-nat-gateway.md") between your network and each
  VPC that you create an outbound endpoint for.

## When

you share rules, you also share outbound endpoints

When you create a rule, you specify the outbound endpoint that you want
Resolver to use to forward DNS queries to your network. If you share the rule
with another AWS account, you also indirectly share the outbound endpoint
that you specify in the rule. If you used more than one AWS account to
create VPCs in an AWS Region, you can do the following:

- Create one outbound endpoint in the Region.
- Create rules using one AWS account.
- Share the rules with all the AWS accounts that created VPCs in the
  Region.

This allows you to use one outbound endpoint in a Region to forward DNS
queries to your network from multiple VPCs even if the VPCs were created
using different AWS accounts.

## Choosing protocols for the endpoints

Endpoint protocols determine how data is transmitted to an inbound endpoint and from an
outbound endpoint. Encrypting DNS queries for VPC traffic is not needed because every packet flow on the network is individually authorized against a rule to validate
the correct source and destination before it is transmitted and delivered. It is highly improbable for information to arbitrarily pass
between entities without specifically being authorized by both the transmitting and receiving entity.
If a packet is being routed to a destination without a rule that matches it, the packet is dropped. For more information, see
[VPC features](../../../whitepapers/latest/logical-separation/vpc-and-accompanying-features.md "../../../whitepapers/latest/logical-separation/vpc-and-accompanying-features.md").

The available protocols are:

- **Do53:** DNS over port 53. The data is relayed by using the
  Route 53 Resolver without additional encryption. While the data cannot be read by
  external parties, it can be viewed within the AWS networks. Uses
  either UDP or TCP to send the packets. Do53 is primarily used for
  traffic within and between Amazon VPCs. Currently, this is the only protocol
  available for delegation inbound endpoints.
- **DoH:** The data is transmitted over an encrypted HTTPS
  session. DoH adds an added level of security where data can't be
  decrypted by unauthorized users, and cannot be read by anyone except the
  intended recipient. Not available for delegation inbound
  endpoints.
- **DoH-FIPS:** The data is transmitted over an encrypted
  HTTPS session that is compliant with the FIPS 140-2 cryptographic
  standard. Supported for inbound endpoints only. For more information,
  see [FIPS PUB
  140-2](https://doi.org/10.6028/NIST.FIPS.140-2 "https://doi.org/10.6028/NIST.FIPS.140-2"). Not available for delegation inbound
  endpoints.

For an inbound endpoint of type **Forward**, you can apply the protocols as follows:

- Do53 and DoH in combination.
- Do53 and DoH-FIPS in combination.
- Do53 alone.
- DoH alone.
- DoH-FIPS alone.
- None, which is treated as Do53.

For an outbound endpoint you can apply the protocols as follows:

- Do53 and DoH in combination.
- Do53 alone.
- DoH alone.
- None, which is treated as Do53.

See also
[Values that you specify when you create or edit inbound endpoints](resolver-forwarding-inbound-queries-values.md "resolver-forwarding-inbound-queries-values.md") and
[Values that you specify when you create or edit
outbound endpoints](resolver-forwarding-outbound-queries-endpoint-values.md "resolver-forwarding-outbound-queries-endpoint-values.md").

## Using Resolver in VPCs that are configured for dedicated instance tenancy

When you create a Resolver endpoint, you can't specify a VPC that has the
[instance tenancy
attribute](../../../AWSEC2/latest/UserGuide/dedicated-instance.md "../../../AWSEC2/latest/UserGuide/dedicated-instance.md") set to `dedicated`. Resolver doesn't run on
single-tenant hardware.

You can still use Resolver to resolve DNS queries that originate in a VPC.
Create at least one VPC that has the instance tenancy attribute set to
`default`, and specify that VPC when you create inbound and
outbound endpoints.

When you create a forwarding rule, you can associate it with any VPC,
regardless of the setting for the instance tenancy attribute.
