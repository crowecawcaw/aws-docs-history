

# North-South Inspection with AWS Network Firewall and AWS Transit Gateway
<a name="nwfw-north-south"></a>

Publication date: **March 16, 2022 ([Diagram history](#nwfw4-diagram-history))**

This architecture shows how to use [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) to centralize the traffic inspection from and to the internet, or from and to on-premises facilities connected through [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html) or AWS Site-to-Site VPN, using [AWS Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html).

## North-south centralized inspection with Network Firewall architecture
<a name="nwfw4-diagram1"></a>

![Architecture diagram showing north-south centralized inspection using AWS Network Firewall and AWS Transit Gateway for traffic between VPCs and the internet or on-premises.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/network-firewall-inspection-models/images/network-firewall-inspection-models-4.png)


The following steps describe the egress traffic flow in this architecture:

1. Traffic from the instance in **Spoke VPC A** destined to the internet is routed to the Transit Gateway. The Transit Gateway route table associated with the attachment sends all the traffic (**0.0.0.0/0**) to the **Inspection VPC**.

1. The **Inspection VPC** **TGW subnet** route table sends all the traffic to the firewall endpoint. The allowed traffic is forwarded back to the Transit Gateway.

1. The Transit Gateway route table associated with the **Inspection VPC** attachment has all the routes within the network.

1. In this particular use case, as the traffic needs to be routed to the internet, the Transit Gateway will forward the traffic to the **Central Egress VPC**.

1. The **TGW subnet** route table of the **Central Egress VPC** sends the traffic to the NAT gateway, so the private IP of the client can be translated to the private IP of the NAT gateway, and in turn, translated to the public IP by the internet gateway.

The following steps describe the ingress traffic flow:

1. Traffic coming from the internet reaches the **Central Ingress VPC**. In this example, an Application Load Balancer sends the request to the target group of configured IP addresses through the Transit Gateway.

1. The traffic is forwarded to the **Inspection VPC** in accordance with the **Pre-inspection route table** in Transit Gateway.

1. As with the egress traffic, the **Inspection VPC** **TGW subnet** route table sends all the traffic to the firewall endpoint. Allowed traffic is forwarded back to the Transit Gateway and subsequently to the destination VPC (**Spoke VPC A**).

1. The Transit Gateway route table associated with the **Inspection VPC** forwards the traffic to the **Spoke VPC A**.

1. The **Spoke VPC A** route table sends the traffic to the desired instance.

**Note**  
It is recommended to use Transit Gateway appliance mode in the **Inspection VPC** Transit Gateway attachment to maintain flow symmetry.

## Further reading
<a name="nwfw4-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="nwfw4-diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](nwfw-single-vpc.md#nwfw1-diagram-history) | Reference architecture diagram first published. | March 16, 2022 | 
| [Initial publication](nwfw-intra-vpc.md#nwfw2-diagram-history) | Reference architecture diagram first published. | March 16, 2022 | 
| [Initial publication](nwfw-east-west.md#nwfw3-diagram-history) | Reference architecture diagram first published. | March 16, 2022 | 
| [Initial publication](#nwfw4-diagram-history) | Reference architecture diagram first published. | March 16, 2022 | 
| [Initial publication](nwfw-combined.md#nwfw5-diagram-history) | Reference architecture diagram first published. | March 16, 2022 | 
| [Initial publication](nwfw-multi-region.md#nwfw6-diagram-history) | Reference architecture diagram first published. | March 16, 2022 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.