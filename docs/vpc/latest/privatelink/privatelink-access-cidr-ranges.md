

# Access network segments through AWS PrivateLink
<a name="privatelink-access-cidr-ranges"></a>

You can privately access a network segment in another VPC using a tunnel VPC endpoint (tunnel endpoint). A tunnel endpoint lets you privately and securely access resources located within a set of CIDR ranges in another network. A CIDR range represents a network segment, so a consumer application can reach any resource within that network segment, without the provider having to enumerate each resource. This is useful when the resources are ephemeral or not known in advance. Tunnel endpoints require you to tunnel into another VPC using GENEVE encapsulation.

**Pricing**  
When you access a network segment using a tunnel endpoint, you are billed for each hour that your tunnel endpoint is provisioned. You are also billed per GB of data processed when you access the network segment. For more information, see [AWS PrivateLink pricing](https://aws.amazon.com/privatelink/pricing/). When you share your network segment using resource configurations and resource gateways, you are billed per GB of data processed by your resource gateways. For more information, see [Amazon VPC Lattice pricing](https://aws.amazon.com/vpc/lattice/pricing/).

**Topics**
+ [Overview](#cidr-endpoint-overview)
+ [GENEVE encapsulation](#cidr-endpoint-geneve)
+ [DNS hostnames](#cidr-endpoint-dns)
+ [DNS resolution](#cidr-endpoint-dns-resolution)
+ [Private DNS](#cidr-endpoint-private-dns)
+ [Subnets and Availability Zones](#cidr-endpoint-subnets-zones)
+ [IP address types](#cidr-endpoint-ip-address-type)
+ [Create a tunnel endpoint](use-cidr-endpoint.md)

## Overview
<a name="cidr-endpoint-overview"></a>

You can access network segments in your account or those that have been shared with you from another account. To access a network segment, you first create a tunnel endpoint, which establishes a connection between your VPC and a resource gateway in the VPC from which the network segment is shared. You then encapsulate application traffic using GENEVE and send it to the tunnel endpoint. The endpoint removes the GENEVE header and sends the inner packet to its destination in the other VPC. When doing so, it checks whether the destination lies within the network segment that was shared with you from the other VPC. If it lies outside, the endpoint doesn't allow access to it.

### Considerations
<a name="cidr-endpoint-considerations"></a>
+ The subnets of the tunnel endpoint must be in Availability Zones that overlap with the Availability Zones of the subnets in which the resource gateway is.
+ Network connections can only be initiated from the VPC that has the tunnel endpoint, and not the VPC that is sharing the network segments. The network segment VPC can't initiate network connections into the endpoint VPC.

## GENEVE encapsulation
<a name="cidr-endpoint-geneve"></a>

Application traffic must be encapsulated in GENEVE. GENEVE traffic must use UDP and port 6081 on the tunnel endpoint. The VNI must be set to `0`. The inner packet must be a layer 3 IP packet. In the inner packet, UDP is supported only for DNS queries. Regular application traffic in the inner packet must be TCP.

## DNS hostnames
<a name="cidr-endpoint-dns"></a>

A tunnel endpoint has a regional DNS name. It resolves to IPs in the subnets where the tunnel endpoint is created. These IPs should be the target of your GENEVE-encapsulated traffic, not the application traffic. Private DNS names are not supported for tunnel endpoints.

## DNS resolution
<a name="cidr-endpoint-dns-resolution"></a>

A tunnel endpoint lets you resolve DNS in the context of the VPC that is sharing the network segment. You can resolve a domain through the tunnel endpoint against the DNS resolver of the remote VPC. To do so, you use `169.254.168.253` as the name server. You set it as the destination of the DNS query in the inner packet, and encapsulate it in GENEVE like you do for application traffic. DNS resolution looks the same as it would for a client in the remote VPC. It is based on the remote VPC's configured DHCP option set. It respects Route 53 private hosted zones or custom resolvers configured in the remote VPC.

## Private DNS
<a name="cidr-endpoint-private-dns"></a>

Private DNS names are not supported for tunnel endpoints.

## Subnets and Availability Zones
<a name="cidr-endpoint-subnets-zones"></a>

You can configure your tunnel endpoint with one subnet per Availability Zone. Elastic network interfaces are created for the endpoint in those subnets. An IP address is assigned to each ENI from its subnet, based on the IP address type of the endpoint. In a production environment, for high availability and resiliency, we recommend configuring at least two Availability Zones for each endpoint. The subnets of the endpoint must be in Availability Zones that overlap with the Availability Zones of the subnets in which the resource gateway is.

## IP address types
<a name="cidr-endpoint-ip-address-type"></a>

The outer and inner packets can have differing IP types. The following combinations are supported: IPv4 over IPv4, IPv6 over IPv4, IPv4 over IPv6, and IPv6 over IPv6.

The tunnel endpoint's IP type decides the IP type of the outer GENEVE packet. The remote VPC's IP type decides the inner packet's IP type. A network segment that is shared can have both IPv4 and IPv6 ranges.

Tunnel endpoints support IPv4, IPv6, or dualstack addresses. The IP address type of a tunnel endpoint must be compatible with the subnets for the tunnel endpoint, as described here:
+ IPv4 – Assigns IPv4 addresses to the tunnel endpoint. Supported only if all of the endpoint's subnets have IPv4 ranges.
+ IPv6 – Assigns IPv6 addresses to the tunnel endpoint. Supported only if all of the endpoint's subnets have IPv6 ranges.
+ Dualstack – Assigns both IPv4 and IPv6 addresses to the tunnel endpoint. Supported only if all of the endpoint's subnets have both IPv4 and IPv6 ranges.

The endpoint's IPv6 addresses are unreachable from the internet. `denyAllIgwTraffic` is enabled on its network interfaces.