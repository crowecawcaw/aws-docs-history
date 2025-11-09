# Connect attachments and Connect peers in

AWS Transit Gateway

You can create a _Transit Gateway Connect attachment_ to
establish a connection between a transit gateway and third-party virtual appliances (such as SD-WAN
appliances) running in a VPC. A Connect attachment supports the Generic Routing
Encapsulation (GRE) tunnel protocol for high performance, and Border Gateway Protocol (BGP)
for dynamic routing. After you create a Connect attachment, you can create one or more GRE
tunnels (also referred to as _Transit Gateway Connect peers_) on the Connect attachment
to connect the transit gateway and the third-party appliance. You establish two BGP sessions over the
GRE tunnel to exchange routing information.

###### Important

A Transit Gateway Connect peer consists of two BGP peering sessions terminating on AWS-managed
infrastructure. The two BGP peering sessions provide routing plane redundancy, ensuring
that losing one BGP peering session does not impact your routing operation. The routing
information received from both BGP sessions is accumulated for the given
Connect peer. The two BGP peering sessions also protect against any AWS
infrastructure operations such as routine maintenance, patching, hardware upgrades, and
replacements. If your Connect peer is operating without the recommended dual BGP
peering session configured for redundancy, it might experience a momentary loss of
connectivity during AWS infrastructure operations. We strongly recommend that you
configure both the BGP peering sessions on your Connect peer. If you have
configured multiple Connect peers to support high availability on the appliance
side, we recommend that you configure both the BGP peering sessions on each of your
Connect peers.

A Connect attachment uses an existing VPC or Direct Connect attachment as the underlying
transport mechanism. This is referred to as the _transport attachment_.
The transit gateway identifies matched GRE packets from the third-party appliance as traffic from the
Connect attachment. It treats any other packets, including GRE packets with incorrect
source or destination information, as traffic from the transport attachment.

###### Note

To use a Direct Connect attachment as a transport mechanism, you'll first need to integrate
Direct Connect with AWS Transit Gateway. For the steps to create this integration, see [Integrate SD-WAN devices with AWS Transit Gateway and AWS Direct Connect](https://aws.amazon.com/blogs/networking-and-content-delivery/integrate-sd-wan-devices-with-aws-transit-gateway-and-aws-direct-connect/ "https://aws.amazon.com/blogs/networking-and-content-delivery/integrate-sd-wan-devices-with-aws-transit-gateway-and-aws-direct-connect/").

## Connect peers

A Connect peer (GRE tunnel) consists of the following components.

**Inside CIDR blocks (BGP addresses)**

The inside IP addresses that are used for BGP peering. You must specify a /29
CIDR block from the `169.254.0.0/16` range for IPv4. You can
optionally specify a /125 CIDR block from the `fd00::/8` range
for IPv6. The following CIDR blocks are reserved and cannot be used:

- 169.254.0.0/29
- 169.254.1.0/29
- 169.254.2.0/29
- 169.254.3.0/29
- 169.254.4.0/29
- 169.254.5.0/29
- 169.254.169.248/29

You must configure the first address from the IPv4 range on the appliance
as the BGP IP address. When you use IPv6, if your inside CIDR block is
fd00::/125, then you must configure the first address in this range
(fd00::1) on the tunnel interface of the appliance.

The BGP addresses must be unique across all tunnels on a transit gateway.

**Peer IP address**

The peer IP address (GRE outer IP address) on the appliance side of the
Connect peer. This can be any IP address. The IP address can be an IPv4 or
IPv6 address, but it must be the same IP address family as the transit gateway
address.

**Transit gateway address**

The peer IP address (GRE outer IP address) on the transit gateway side of the
Connect peer. The IP address must be specified from the transit gateway CIDR block,
and must be unique across Connect attachments on the transit gateway. If you don't
specify an IP address, we use the first available address from the transit gateway
CIDR block.

You can add a transit gateway CIDR block when you [create](create-tgw.md "create-tgw.md") or [modify](tgw-modifying.md "tgw-modifying.md") a
transit gateway.

The IP address can be an IPv4 or IPv6 address, but it must be the same IP
address family as the peer IP address.

The peer IP address and transit gateway address are used to uniquely identify the GRE tunnel. You
can reuse either address across multiple tunnels, but not both in the same
tunnel.

Transit Gateway Connect for the BGP peering only supports Multiprotocol BGP (MP-BGP), where
IPv4 Unicast addressing is required to also establish a BGP session for IPv6 Unicast.
You can use both IPv4 and IPv6 addresses for the GRE outer IP addresses.

The following example shows a Connect attachment between a transit gateway and an appliance in a
VPC.

![Transit gateway Connect attachment and Connect peer](images/transit-gateway-connect-peer.png)

| Diagram component                                                      | Description               |
| ---------------------------------------------------------------------- | ------------------------- |
| Shows how VPC attachments are represented in the example diagram.      | VPC attachment            |
| Shows how Connect attachments are represented in the example diagram.  | Connect attachment        |
| Shows how GRE tunnels are represented in the example diagram.          | GRE tunnel (Connect peer) |
| Shows how BGP peering sessions are represented in the example diagram. | BGP peering session       |

In the preceding example, a Connect attachment is created on an existing VPC
attachment (the transport attachment). A Connect peer is created on the
Connect attachment to establish a connection to an appliance in the VPC. The transit gateway
address is `192.0.2.1`, and the range of BGP addresses is
`169.254.6.0/29`. The first IP address in the range
(`169.254.6.1`) is configured on the appliance as the peer BGP IP
address.

The subnet route table for VPC C has a route that points traffic destined for the transit gateway
CIDR block to the transit gateway.

| Destination   | Target   |
| ------------- | -------- |
| 172.31.0.0/16 | Local    |
| 192.0.2.0/24  | _tgw-id_ |

## Requirements and considerations

The following are the requirements and considerations for a Connect attachment.

- For information about what Regions support Connect attachments, see the [AWS Transit Gateways FAQ](https://aws.amazon.com/transit-gateway/faqs/ "https://aws.amazon.com/transit-gateway/faqs/").
- The third-party appliance must be configured to send and receive traffic over
  a GRE tunnel to and from the transit gateway using the Connect attachment.
- The third-party appliance must be configured to use BGP for dynamic route
  updates and health checks.
- The following types of BGP are supported:
  - Exterior BGP (eBGP): Used for connecting to routers that are in a
    different autonomous system than the transit gateway. If you use eBGP, you must
    configure ebgp-multihop with a time-to-live (TTL) value of 2.
  - Interior BGP (iBGP): Used for connecting to routers that are in the
    same autonomous system as the transit gateway. The transit gateway will not
    install routes from an iBGP peer (third-party appliance), unless the
    routes are originated from an eBGP peer and should have next-hop-self
    configured. The routes advertised by third-party appliance over the iBGP
    peering must have an ASN.
  - MP-BGP (multiprotocol extensions for BGP): Used for supporting
    multiple protocol types, such as IPv4 and IPv6 address families.

- The default BGP keep-alive timeout is 10 seconds and the default hold timer is
  30 seconds.
- IPv6 BGP peering is not supported; only IPv4-based BGP peering is supported.
  IPv6 prefixes are exchanged over IPv4 BGP peering using MP-BGP.
- Bidirectional Forwarding Detection (BFD) is not supported.
- BGP graceful restart is not supported.
- When you create a transit gateway peer, if you do not specify a peer ASN number, we pick
  the transit gateway ASN number. This means that your appliance and transit gateway will be in the
  same autonomous system doing iBGP.
- A Connect peer using the BGP AS-PATH attribute is the
  preferred route when you have two Connect peers.

To use equal-cost multi-path (ECMP) routing between multiple appliances, you
must configure the appliance to advertise the same prefixes to the transit gateway with
the same BGP AS-PATH attribute. For the transit gateway to choose all of the available
ECMP paths, the AS-PATH and Autonomous System Number (ASN) must match. The transit gateway
can use ECMP between Connect peers for the same Connect attachment or between
Connect attachments on the same transit gateway. The transit gateway cannot use ECMP between both
of the redundant BGP peerings a single peer establishes to it.

- With a Connect attachment, the routes are propagated to a transit gateway
  route table by default.
- Static routes are not supported.
- Configure the GRE tunnel MTU to be smaller than the external interface MTU by
  subtracting the GRE header (24 bytes) and outer IP header (20 bytes) overhead.
  For example, if your external interface MTU is 1500 bytes, set the GRE tunnel
  MTU to 1456 bytes (1500 - 24 - 20 = 1456) to prevent packet
  fragmentation.

###### Tasks

- [Create a Connect attachment](create-tgw-connect-attachment.md "create-tgw-connect-attachment.md")
- [Create a Connect peer](create-tgw-connect-peer.md "create-tgw-connect-peer.md")
- [View Connect attachments and
  Connect peers](view-tgw-connect-attachments.md "view-tgw-connect-attachments.md")
- [Modify Connect attachment and Connect peer tags](modify-connect-attachment-tag.md "modify-connect-attachment-tag.md")
- [Delete a Connect peer](delete-tgw-connect-peer.md "delete-tgw-connect-peer.md")
- [Delete a Connect attachment](delete-tgw-connect-attachment.md "delete-tgw-connect-attachment.md")
