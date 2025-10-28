# Connect attachments and Connect peers in AWS Cloud WAN

You can create a transit gateway Connect attachment to establish a connection between a
core network edge and third-party virtual appliances (such as SD-WAN appliances) running in
Amazon VPC. A Connect attachment supports both the Generic Routing Encapsulation (GRE) tunnel
protocol and Tunnel-less connect protocol for high performance, and the Border Gateway
Protocol (BGP) for dynamic routing. After you create a Connect attachment, you can create
one or more GRE or Tunnel-less Connect tunnels (also referred to as Transit Gateway Connect
peers) on the Connect attachment to connect the core network edge and the third-party
appliance. You establish two BGP sessions over the tunnel to exchange routing information.
The two BGP sessions are for redundancy. A Connect attachment uses an existing VPC
attachment as the underlying transport mechanism. This is referred to as the transport
attachment.

The Core Network Edge identifies matched GRE packets from the third-party appliance as
traffic from the Connect attachment. It treats any other packets, including GRE packets with
incorrect source or destination information, as traffic from the transport
attachment.

You can create a Connect attachment through either the AWS Network Manager console or using the
CLI/SDK.

###### Note

A Connect attachment must be created in the same AWS account that owns the core
network.

## Tunnel-less Connect

AWS Cloud WAN supports Tunnel-less Connect for VPC Connect attachments. Tunnel-less Connect provides a simpler way to
build a global SD-WAN using AWS. Third-party SD-WAN appliances can peer with Cloud WAN
using Border Gateway Protocol (BGP) without needing to deploy IPsec or GRE-based tunnels
between the appliance and Cloud WAN. This allows you to deploy a Cloud WAN core network
across multiple AWS Regions and to connect one or more of your third-party SD-WAN
appliances to core network edges in each Region. Because Tunnel-less Connect has no
tunneling overhead, it provides better performance and peak bandwidth on TLC
attachments. IPSec provides 1.25G, allowing you to combine up to eight tunnels while
providing up to the entire VPC attachment bandwidth. GRE supports only 5G, which means
you'd need to deploy specialized techniques, such as ECMP (Equal Cost Multi-pathing),
for scaling bandwidth across tunnels.

You can use the console or API to specify the Tunnel-less Connect protocol.

In order to use Tunnel-less Connect, note the following:

- Your SD-WAN appliance must support BGP. The appliance must be deployed in a
  VPC and use a Connect attachment enabled for the tunnel-less operation in order
  to connect your SD-WAN appliance to a core network edge.
- Attachment policy tags or resource names are used to associate the Tunnel-less Connect
  attachment to the SD-WAN segment.
- Both Connect (GRE) and Connect (Tunnel-less) attachments can co-exist in the
  same VPC. There is a maximum of single Connect (Tunnel-less) attachment per VPC.
- Tunnel-less Connect and any underlying transport VPC attachments must be
  associated to the same core network segment.
- Inside CIDR blocks is not an input when creating a Tunnel-less Connect
  peer, but is instead taken from the connecting core network edge

## Routing

Tunnel-less Connect uses BGP for dynamic routing. Therefore, any third-party SD-WAN appliance
you want to use for Tunnel-less Connect must support BGP. SD-WAN appliances peer with a core
network using the Connect attachment functioning in a tunnel-less manner. It uses
native BGP to dynamically exchange routing and reachability information between
SD-WAN appliance in the VPC and the core network edge. We recommend using a
different autonomous number (ASN) on your SD-WAN appliance from the one configured
on the core network edge.

Tunnel-less Connect also supports Multiprotocol extension for BGP (MP- BGP) in
order to support both IPv4/IPv6 address families.

You'll need to configure the following in the VPC route table used for
Tunnel-less Connect:

- The core network edge BGP IP address. This is necessary to bring up the
  BGP session between the core network edge and the SD-WAN appliance.
- If your third-party appliance is in a different subnet from the VPC
  attachment, you'll need to add all destination prefixes.

For more information about route tables, see [Configure route tables](../../../vpc/latest/userguide/VPC_Route_Tables.md "../../../vpc/latest/userguide/VPC_Route_Tables.md")
in the _Amazon VPC User Guide_.

## Third-party appliance limitations

An AWS Cloud WAN tunnel-less attachment peer (third-party appliance) can be located in
the same subnet as the VPC attachment (transport attachment) subnet or a different
subnet. The following limitations apply if your third-party appliance is located
either in the same subnet as the Cloud WAN VPC attachment or in different subnets.

**For third-party appliances in the same subnet as the Cloud WAN VPC
attachment:**

- When the third-party appliance is in the same subnet as the VPC
  attachment, routes are dynamically exchanged using BGP with the core network
  edge. For the dataplane to function correctly, no VPC route table
  modifications are required except for adding the core network BGP addresses
  to establish BGP peering.
- The BGP IPv4 prefixes advertised by the core network edge to your
  third-party appliance will have the core network attachment's Elastic
  Network Interface's (ENI) IPv4 address as the next-hop address, which
  differs from the core network BGP address peering.
- The BGP IPv6 prefixes advertised by the core network edge to your
  third-party appliance will use the EUI-64 Address of the core network
  attachment's ENI as the next-hop.

**For third-party appliances in a different subnets from the Cloud WAN VPC
attachment:**

- If the third-party appliance is in a different subnet from the VPC
  attachment, you can still establish dynamic route exchange the core network
  edge using BGP. However, in addition to adding the core network BGP
  addresses for peering, you must modify the VPC route table for the dataplane
  to function correctly. This includes adding the prefixes received from the
  core network edge BGP peer into the route table. You can create a summary
  route that encompasses the longest prefixes advertised by the core network
  edge.
- The BGP IPv4 prefixes advertised by the core network edge to your
  third-party appliance will have the core network BGP address as the
  next-hop.
- The BGP IPv6 prefixes advertised by the core network edge to your
  third-party appliance will use IPv4-mapped IPv6 addresses of the core
  network BGP address as the next-hop.

It's recommended that you place your third-party appliance in the same subnet as
the Cloud WAN VPC attachment for more seamless integration with Tunnel-less
connect.

###### Topics

- [Create a Connect attachment](cloudwan-connect-attachment-add.md "cloudwan-connect-attachment-add.md")
- [View or edit a Connect attachment](cloudwan-attachments-viewing-editing-connect.md "cloudwan-attachments-viewing-editing-connect.md")
- [Add a Connect peer](cloudwan-connect-peer-attachment.md "cloudwan-connect-peer-attachment.md")
