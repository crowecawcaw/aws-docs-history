

# East-West Inspection with AWS Network Firewall and AWS Transit Gateway
<a name="nwfw-east-west"></a>

Publication date: **March 16, 2022 ([Diagram history](#nwfw3-diagram-history))**

This architecture shows how to use [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) to centralize the traffic inspection between several VPCs, both in the same Region or between Regions, using [AWS Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html).

## East-west centralized inspection with Network Firewall architecture
<a name="nwfw3-diagram1"></a>

![Architecture diagram showing east-west centralized inspection using AWS Network Firewall and AWS Transit Gateway for traffic between VPCs.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/network-firewall-inspection-models/images/network-firewall-inspection-models-3.png)


The following steps describe the east-west traffic flow in this architecture:

1. Any traffic leaving a spoke VPC is routed to AWS Transit Gateway (TGW). The Transit Gateway route table associated with the VPCs and Transit Gateway peering forwards the traffic to the **Inspection VPC**.

1. The **Inspection VPC** route table forwards all the traffic to the firewall endpoint. The allowed traffic is forwarded back to the Transit Gateway.

1. The Transit Gateway route table associated with the **Inspection VPC** attachment has all the routes within the network.

1. In this particular example, the traffic is destined to **Spoke VPC B**.

1. In **Spoke VPC B**, the **TGW subnet** route table routes the traffic to the destination instance.

The following steps describe the return traffic flow:

1. Traffic from an instance in **Spoke VPC B** to **Spoke VPC A** first reaches the Transit Gateway endpoint in the **TGW subnet**. The traffic is routed to the Transit Gateway.

1. The Transit Gateway route table sends the traffic to the **Inspection VPC**, where it is routed to the firewall endpoint for inspection.

1. Allowed traffic comes back to the Transit Gateway. The route table associated with the **Inspection VPC** forwards the traffic to **Spoke VPC A**.

**Note**  
It is recommended to use Transit Gateway appliance mode in the **Inspection VPC** Transit Gateway attachment to maintain flow symmetry.

For more information about deployment models with AWS Network Firewall and AWS Transit Gateway, see [Deployment Models for AWS Network Firewall](https://aws.amazon.com/blogs/networking-and-content-delivery/deployment-models-for-aws-network-firewall/) on the AWS Blog.

## Further reading
<a name="nwfw3-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="nwfw3-diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](nwfw-single-vpc.md#nwfw1-diagram-history) | Reference architecture diagram first published. | March 16, 2022 | 
| [Initial publication](nwfw-intra-vpc.md#nwfw2-diagram-history) | Reference architecture diagram first published. | March 16, 2022 | 
| [Initial publication](#nwfw3-diagram-history) | Reference architecture diagram first published. | March 16, 2022 | 
| [Initial publication](nwfw-north-south.md#nwfw4-diagram-history) | Reference architecture diagram first published. | March 16, 2022 | 
| [Initial publication](nwfw-combined.md#nwfw5-diagram-history) | Reference architecture diagram first published. | March 16, 2022 | 
| [Initial publication](nwfw-multi-region.md#nwfw6-diagram-history) | Reference architecture diagram first published. | March 16, 2022 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.