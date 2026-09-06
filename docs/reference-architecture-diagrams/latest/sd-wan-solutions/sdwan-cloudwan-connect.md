

# SD-WAN Connectivity with AWS Cloud WAN Connect Attachments
<a name="sdwan-cloudwan-connect"></a>

Publication date: **December 28, 2024 ([Diagram history](#sdwan2-diagram-history))**

This architecture shows how to use Connect attachments to connect your SD-WAN to AWS Cloud WAN, and simplify your route management across hybrid cloud environments. The SD-WAN headend peers with Cloud WAN's Core Network Edges (CNEs) over a GRE tunnel, allowing this design to take advantage of the higher BGP prefix limit of [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html). Additionally, with a single Transit Gateway Connect attachment, you can scale horizontally the bandwidth of your connection up to 20 Gbps.

## SD-WAN connectivity with AWS Cloud WAN Connect architecture
<a name="sdwan2-diagram1"></a>

![Architecture diagram showing SD-WAN connectivity using AWS Cloud WAN Connect attachments with GRE tunneling and BGP peering across multiple Regions.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/sd-wan-solutions/images/sd-wan-solutions-2.png)


The following steps describe the AWS to on-premises traffic flow:

1. Traffic initiated from an Amazon Elastic Compute Cloud instance in a [Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) in Region A and destined for the corporate data center is forwarded to the Core Network. The Amazon VPC attachment is associated to the prod segment.

1. As per the Core Network policy, traffic arriving to the prod segment destined to the corporate data center should be forwarded to the Connect attachment in Region B. The Connect attachment uses the Amazon VPC attachment as transport, and connects the Core Network to the third-party appliance in the appliance Amazon VPC using GRE tunneling and BGP.

1. The third-party virtual appliance encapsulates the traffic, which uses the SD-WAN overlay (on top of the [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html) link) to reach the corporate data center.

The following steps describe the on-premises to AWS traffic flow:

1. Traffic from branches outside AWS destined to a Amazon VPC in Region A reaches the internet gateway of the appliance Amazon VPC through the SD-WAN overlay - on top of the internet.

1. The third-party virtual appliance in the Connect Amazon VPC forwards the traffic to the Core Network through the Connect attachment. The Connect attachment is associated to the on-prem segment.

1. As per the Core Network policy, the traffic is forwarded to the corresponding Amazon VPC, forwarding the traffic to the destination.

## Further reading
<a name="sdwan2-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="sdwan2-diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](sdwan-tgw-connect.md#sdwan1-diagram-history) | Reference architecture diagram first published. | December 28, 2024 | 
| [Initial publication](#sdwan2-diagram-history) | Reference architecture diagram first published. | December 28, 2024 | 
| [Initial publication](sdwan-cloudwan-tunnelless.md#sdwan3-diagram-history) | Reference architecture diagram first published. | December 28, 2024 | 
| [Initial publication](sdwan-vpn-tgw.md#sdwan4-diagram-history) | Reference architecture diagram first published. | December 28, 2024 | 
| [Initial publication](sdwan-vpn-cloudwan.md#sdwan5-diagram-history) | Reference architecture diagram first published. | December 28, 2024 | 
| [Initial publication](sdwan-dx-tgw.md#sdwan6-diagram-history) | Reference architecture diagram first published. | December 28, 2024 | 
| [Initial publication](sdwan-dx-cloudwan.md#sdwan7-diagram-history) | Reference architecture diagram first published. | December 28, 2024 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.