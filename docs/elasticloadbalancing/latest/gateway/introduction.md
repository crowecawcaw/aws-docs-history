# What is a Gateway Load Balancer?

ELB automatically distributes your incoming traffic across multiple targets, in one or more Availability Zones. It monitors the
health of its registered targets, and routes traffic only to the healthy targets. ELB
scales your load balancer as your incoming traffic changes over time. It can automatically
scale to the vast majority of workloads.

ELB supports the following load balancers: Application Load Balancers, Network Load Balancers, Gateway Load Balancers, and
Classic Load Balancers. You can select the type of load balancer that best suits your needs. This guide
discusses Gateway Load Balancers. For more information about the other load balancers, see the
[User Guide for Application Load Balancers](../application.md "../application.md"), the [User Guide for Network Load Balancers](../network.md "../network.md"), and the [User Guide for Classic Load Balancers](../classic.md "../classic.md").

## Gateway Load Balancer overview

Gateway Load Balancers enable you to deploy, scale, and manage virtual appliances, such as firewalls,
intrusion detection and prevention systems, and deep packet inspection systems. It combines a
transparent network gateway (that is, a single entry and exit point for all traffic) and
distributes traffic while scaling your virtual appliances with the demand.

A Gateway Load Balancer operates at the third layer of the Open Systems Interconnection (OSI) model, the
network layer. It listens for all IP packets across all ports and forwards traffic to the target
group that's specified in the listener rule. It maintains [flow
stickiness](edit-target-group-attributes.md#flow-stickiness "edit-target-group-attributes.md#flow-stickiness") to a specific target appliance using 5-tuple (default), 3-tuple, or 2-tuple.
The Gateway Load Balancer and its registered virtual appliance instances exchange application traffic using the
[GENEVE](https://datatracker.ietf.org/doc/html/rfc8926 "https://datatracker.ietf.org/doc/html/rfc8926") protocol on port 6081.

Gateway Load Balancers use Gateway Load Balancer endpoints to securely exchange traffic across VPC boundaries. A Gateway Load Balancer endpoint is a VPC
endpoint that provides private connectivity between virtual appliances in the service provider VPC
and application servers in the service consumer VPC. You deploy the Gateway Load Balancer in the same VPC as the
virtual appliances. You register the virtual appliances with a target group for the Gateway Load Balancer.

Traffic to and from a Gateway Load Balancer endpoint is configured using route tables. Traffic flows from the service
consumer VPC over the Gateway Load Balancer endpoint to the Gateway Load Balancer in the service provider VPC, and then returns to the
service consumer VPC. You must create the Gateway Load Balancer endpoint and the application servers in different subnets.
This enables you to configure the Gateway Load Balancer endpoint as the next hop in the route table for the application
subnet.

For more information, see [Access virtual appliances through AWS PrivateLink](../../../vpc/latest/privatelink/vpce-gateway-load-balancer.md "../../../vpc/latest/privatelink/vpce-gateway-load-balancer.md") in the _AWS PrivateLink Guide_.

## Appliance vendors

You are responsible for choosing and qualifying software from appliance vendors. You must
trust the appliance software to inspect or modify traffic from the load balancer. The appliance
vendors listed as [ELB
Partners](https://aws.amazon.com/elasticloadbalancing/partners/ "https://aws.amazon.com/elasticloadbalancing/partners/") have integrated and qualified their appliance software with AWS. You can
place a higher degree of trust in the appliance software from vendors in this list. However,
AWS does not guarantee the security or reliability of software from these vendors.

## Getting started

To create a Gateway Load Balancer using the AWS Management Console, see [Getting started](getting-started.md "getting-started.md"). To create a Gateway Load Balancer using the AWS Command Line Interface, see [Getting started using the CLI](getting-started-cli.md "getting-started-cli.md").

## Pricing

With your load balancer, you pay only for what you use. For more information, see [ELB pricing](https://aws.amazon.com/elasticloadbalancing/pricing/ "https://aws.amazon.com/elasticloadbalancing/pricing/").
