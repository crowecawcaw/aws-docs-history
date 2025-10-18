# Peerings in AWS Cloud WAN

AWS Cloud WAN peering connections allow you to interconnect your core network edge with an
 AWS Transit Gateway in the same Region. Peering connections between Cloud WAN and
 transit gateways support dynamic routing with automatic exchange of routes using BGP. You can use
 route table attachments on the peering connection to selectively exchange routes between a
 specific transit gateway route table and a Cloud WAN network segment for end-to-end segmentation and
 network isolation.

The peering connection supports policy-based routing to implement segment isolation across
 peering connections. Using this capability, routes are selectively propagated between a
 route table in transit gateway and a core network segment. You first need to create the peering
 connection and associate a policy table to the transit gateway peering attachment. A policy table
 contains rules for matching network traffic by a specific route table or segment, and then
 maps traffic that matches the rule to a target route table for determining routing behavior. 

 When you create a peering connection, you can either create a new policy table or use an
 existing policy table for association with the peering attachment. As you create your route
 table attachments, the policy table is populated automatically with the policy rules that
 match network traffic by a segment or routing domain, and then maps the traffic that matches
 the rule to a target route table. For more information about transit gateway peering, see [Transit gateway peering
 attachments](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-peering.html "https://docs.aws.amazon.com/vpc/latest/tgw/tgw-peering.html") in the *AWS Transit Gateway
 Guide*.


## Peering limitations


Limits apply when creating a transit gateway peering connection between your transit gateways in AWS Cloud WAN. 


The following limitations apply when creating a peering: 



* A transit gateway used for peering must be in the same Region as the
 core network.
* The Autonomous System Number (ASN) of a transit gateway and the core network must be
 different.
* A transit gateway connection to Cloud WAN only supports dynamically propagated routes.
 An error is returned if you try to add a static route.

###### Topics

* [Create a peering](cloudwan-peerings-create.md "cloudwan-peerings-create.md")
* [View peering details](cloudwan-peerings-view.md "cloudwan-peerings-view.md")
* [Delete a peering](cloudwan-peerings-delete.md "cloudwan-peerings-delete.md")
* [Edit peering tags](cloudwan-peerings-edit.md "cloudwan-peerings-edit.md")
