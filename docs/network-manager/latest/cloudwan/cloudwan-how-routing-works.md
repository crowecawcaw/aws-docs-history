

# How routing works in AWS Cloud WAN

Understanding how AWS Cloud WAN routes traffic helps you design segmentation that isolates the right workloads, predict which path traffic takes between Regions, and troubleshoot connectivity when a destination isn't reachable. This section describes how Cloud WAN builds and uses route tables, how routes propagate through your core network, and where you can influence routing behavior. The behavior described here applies to every attachment type.

For the steps to create segments, attachments, and policy versions, see [Attachments in AWS Cloud WAN](cloudwan-create-attachment.md) and [Core network policy versions in AWS Cloud WAN](cloudwan-create-policy-version.md). This section assumes you are familiar with BGP concepts such as AS\_PATH, MED, and BGP communities.

## Core network edges
<a name="cloudwan-how-routing-works-cne"></a>

When you add a Region to your core network policy, Cloud WAN creates a core network edge (CNE) in that Region. A CNE is the Region-local routing hub of the core network, similar to a transit gateway in a Region. Attachments in the Region connect to the CNE, the CNE holds the segment route tables for that Region, and it peers with the CNEs in every other Region of your core network. In the console and in the policy document, the Region itself is called an *edge location*.

## Route tables in the core network
<a name="cloudwan-how-routing-works-route-tables"></a>

Cloud WAN does not maintain a single global route table. Each CNE maintains a separate route table for every segment in that CNE's Region. Network function groups also have route tables, which are read-only.

In your core network policy, you specify the edge locations where each segment is available. If you do not specify any, the segment is available at every edge location in the core network. A CNE holds a route table for each segment available at that edge location. Two CNEs in the same core network can hold different route tables, depending on how you scope your segments.

A segment is a routing domain. When you define a segment in your core network policy, Cloud WAN instantiates that segment's route table at every CNE where the segment is available, and keeps the contents of those tables consistent with your policy. By default, segments are isolated from each other: an attachment in one segment cannot reach an attachment in another unless your policy shares routes between them.

By default, attachments in the same segment can reach each other. You can set `isolate-attachments` to `true` so that attachments within a segment cannot reach each other directly. They can then reach only the routes shared into the segment from elsewhere, such as a shared services segment, or any traffic that a service insertion action routes through a network function group. For details, see [Add a segment to an AWS Cloud WAN core network policy version](cloudwan-policy-segments.md).

Every attachment connects to the CNE in its Region and is associated with exactly one segment. The segment determines which route table the attachment's routes are propagated into and which routes the attachment can use to send traffic.

For example, consider a core network that spans three Regions and has three segments: **Production segment**, **Development segment**, and **Hybrid segment**. The example contains the following elements:
+ **CNEs** – Each Region has a CNE. The three CNEs peer with each other over **CNE BGP peering (full mesh)**, and each CNE holds a route table for each of the three segments.
+ **VPC attachments** – Each Region has two VPCs. One VPC attachment connects to the **Production segment** and the other connects to the **Development segment**.
+ **Segment isolation** – The **Production segment** and the **Development segment** don't share routes, so VPCs in one segment can't reach VPCs in the other, in the same Region or in a different Region.
+ **Hybrid connectivity** – An **AWS Direct Connect Gateway** is attached to the **Hybrid segment**. It reaches **On-premises location 1 Sydney** and **On-premises location 2 Virginia** over separate **Transit VIFs**. Routes learned from the on-premises locations enter the **Hybrid segment** route table and are advertised to the other CNEs where that segment is available.

The following figure shows the example core network: three CNEs that peer in a full BGP mesh, VPC attachments in the isolated **Production segment** and **Development segment**, and a Direct Connect gateway that connects the **Hybrid segment** to two on-premises locations.

![Core network with Production, Development, and Hybrid segments across three Regions, connected to two on-premises locations.](https://docs.aws.amazon.com/network-manager/latest/cloudwan/images/cloudwan-baseline-three-segments.png)


**Note**  
The core network never modifies your VPC route tables. Routes that the core network learns are installed in segment route tables at the CNEs, not in your VPCs. To send traffic from a VPC into the core network, add routes to the VPC route tables that point to the core network attachment.

The segment route tables work together as one system. A prefix learned by an attachment is propagated into its segment's route table at the local CNE, advertised from there to every other CNE where the segment is available, and installed in the segment route tables of those CNEs. Traffic from a VPC enters the core network through a static route in the VPC route table, and from that point the CNE forwards it using the segment's table.

## Route sources
<a name="cloudwan-how-routing-works-enter"></a>

Routes appear in a segment's route table in four ways.

### Propagated routes
<a name="cloudwan-how-routing-works-propagated"></a>

When an attachment is associated with a segment, its routes are propagated into that segment's route table at the local CNE. A VPC attachment propagates the VPC's CIDR ranges. Attachments that support BGP, such as Direct Connect gateway, Site-to-Site VPN, Connect, and transit gateway route table attachments over peering, propagate the routes they learn from the other side of the session. Routes propagated at one CNE are also advertised to the other CNEs where the segment is available, as described in [Cross-Region route propagation](#cloudwan-how-routing-works-regions). Each attachment type propagates routes differently, and the BGP attributes propagated vary by attachment type. For the behavior of each type, see [Attachments in AWS Cloud WAN](cloudwan-create-attachment.md).

### Static routes
<a name="cloudwan-how-routing-works-static"></a>

You can define static routes for a segment in the core network policy, including blackhole routes that drop matching traffic. Static routes belong to the segment that you define them in. When segments share routes with each other, Cloud WAN doesn't share static routes, so you must define them again in each segment that needs them. For details, see [Add segment actions in an AWS Cloud WAN core network policy version](cloudwan-policy-network-actions-routes.md).

### Shared routes
<a name="cloudwan-how-routing-works-shared"></a>

Segments are isolated by default. Segment actions in the core network policy can share routes between segments, for example, so that every segment can access a shared services segment. What lands in each table when segments share, and the order in which sharing is resolved, is covered in [Add segment actions in an AWS Cloud WAN core network policy version](cloudwan-policy-network-actions-routes.md).

### Service insertion routes
<a name="cloudwan-how-routing-works-service-insertion"></a>

When you add a service insertion action to a segment, Cloud WAN installs routes in the segment's route table that point to the network function group instead of to the destination attachment. A `send-via` action does this for traffic between the same or different segments. A `send-to` action installs a default route toward the network function group. For details, see [AWS Cloud WAN service insertion](cloudwan-policy-service-insertion.md).

## Cross-Region route propagation
<a name="cloudwan-how-routing-works-regions"></a>

Each CNE has its own Autonomous System Number (ASN), taken from the ASN range you configure in the core network policy. All CNEs in a core network peer with each other in a full mesh using external BGP over the AWS global network.

When a route is installed in a segment's route table at one CNE, that CNE advertises the route to every other CNE where the segment is available, unless a routing policy filters it. The receiving CNEs install the route in their copy of the segment's route table. Traffic between Regions travels over the AWS global network using redundant paths.

Because peering between CNEs uses BGP, routes carry the transitive BGP attributes that Cloud WAN supports as they cross the core network. Attribute support varies by attachment type.

Routes are automatically advertised for every route in a segment's route table. By default, Cloud WAN doesn't advertise a route from one segment to another. To have Cloud WAN bring in another segment's routes for you, use a segment action that shares the two segments, or a service insertion action, where Cloud WAN installs routes toward a network function group. A static route is the manual alternative for reaching a destination in another segment.

Sharing is bidirectional by default, so each segment receives the other's routes. If you use a deny filter to share routes in one direction only, traffic reaches the destination and the return traffic is dropped. Static routes are an exception to sharing. Cloud WAN does not share them between segments, so a static route that another segment needs must be defined again in that segment.

Routes shared into a segment are advertised between CNEs like any other route in that segment, so a destination in a different segment and a different Region needs no additional configuration beyond the sharing or service insertion action itself.

## Route selection
<a name="cloudwan-how-routing-works-selection"></a>

When a CNE forwards a packet, it looks up the destination in the route table of the sending attachment's segment at that CNE. The most specific matching prefix wins.

When the same prefix is reachable through more than one route, the CNE applies a fixed evaluation order. Static routes are preferred first, then VPC-propagated routes in the same Region, then dynamic routes ranked by their BGP attributes and by attachment type. If identical routes remain, one attachment is chosen in a deterministically random manner. This happens separately for each segment and each network function group, so the same prefix can resolve to different destinations across segments.

For the complete order, see [Route evaluation](cloudwan-route-evaluation.md).

## Routing controls
<a name="cloudwan-how-routing-works-influence"></a>

The core network policy gives you three places to change routing behavior.

### Attachment policies
<a name="cloudwan-how-routing-works-attachment-policies"></a>

Attachment policies decide which segment an attachment is associated with, either by explicit assignment or by matching attachment tags against rules, optionally requiring manual acceptance. Because the segment determines the routing domain, attachment policies are the first routing decision made about any attachment. For more information, see [Create an attachment policy in an AWS Cloud WAN core network policy version](cloudwan-policy-attachments.md).

### Segment actions
<a name="cloudwan-how-routing-works-segment-actions"></a>

Most of the routing configuration for each segment lives in segment actions, which cover the following four areas of configuration:
+ Static routes for the segment, including blackhole routes.
+ Sharing routes with other segments.
+ Directing traffic between or within segments through inspection using service insertion and network function groups.
+ Associating routing policies with the route propagations that cross between two edge locations where the segment is available.

Service insertion changes what appears in the segment route tables, which is why sharing two segments directly is not the same as connecting them through inspection. For more information, see [Add segment actions in an AWS Cloud WAN core network policy version](cloudwan-policy-network-actions-routes.md) and [AWS Cloud WAN service insertion](cloudwan-policy-service-insertion.md).

### Routing policies
<a name="cloudwan-how-routing-works-routing-policies"></a>

Routing policies act on route propagations themselves. You can filter routes, summarize them, and modify BGP attributes such as AS\_PATH, local preference, MED, and communities. A routing policy does nothing until it is associated with a propagation, and there are three scopes to associate at: routes propagated on an attachment, routes propagated between two segments, and routes propagated between two edge locations within a segment. You configure the last two as segment actions, so a policy that shapes what one Region advertises to another applies to a specific segment and a specific pair of edge locations, not to the core network as a whole. To associate a routing policy with an attachment, you add a routing policy label to the attachment, as described in [Create an AWS Cloud WAN attachment routing policy](cloudwan-policy-attachment-routing.md).

Routing policies act before evaluation: they change which routes exist and what attributes they carry, and the evaluation order then ranks what remains. For more information, see [Create an AWS Cloud WAN route policy and rule](cloudwan-route-policy.md).