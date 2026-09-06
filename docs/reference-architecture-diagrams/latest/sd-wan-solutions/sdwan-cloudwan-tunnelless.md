

# SD-WAN Connectivity with AWS Cloud WAN Tunnel-less Connect Attachments
<a name="sdwan-cloudwan-tunnelless"></a>

Publication date: **December 28, 2024 ([Diagram history](#sdwan3-diagram-history))**

This architecture shows how to use Tunnel-less Connect attachments to connect your SD-WAN to AWS Cloud WAN in a simpler and higher performance way using the AWS Global Network as a middle-mile transport network. The SD-WAN headend natively peers with Cloud WAN's Core Network Edges (CNEs) over BGP without using specialized tunneling protocols such as GRE, removing tunneling overhead and improving throughput performance, which uses the full Amazon VPC attachment bandwidth (up to 100 Gbps per Availability Zone).

## SD-WAN connectivity with AWS Cloud WAN Tunnel-less Connect architecture
<a name="sdwan3-diagram1"></a>

![Architecture diagram showing SD-WAN connectivity using AWS Cloud WAN Tunnel-less Connect attachments with native BGP peering across multiple Regions.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/sd-wan-solutions/images/sd-wan-solutions-3.png)


The following steps describe the AWS to on-premises traffic flow:

1. Traffic initiated from an Amazon Elastic Compute Cloud instance in a [Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) in Region A and destined for the corporate data center is forwarded to the Core Network. The Amazon VPC attachment is associated to the prod segment.

1. As per the Core Network policy, traffic arriving to the prod segment destined to the corporate data center should be forwarded to the Tunnel-less Connect attachment in Region B. The Tunnel-less Connect attachment uses the Amazon VPC attachment as transport, and connects the Core Network to the third-party appliance in the appliance Amazon VPC using native BGP.

1. The third-party virtual appliance encapsulates the traffic, which uses the SD-WAN overlay (on top of the [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html) link) to reach the corporate data center.

The following steps describe the on-premises to AWS traffic flow:

1. Traffic from branches outside AWS destined to a Amazon VPC in Region A reaches the internet gateway of the appliance Amazon VPC through the SD-WAN overlay - on top of the internet.

1. The third-party virtual appliance in the Connect Amazon VPC forwards the traffic to the Core Network through the Tunnel-less Connect attachment. The Tunnel-less Connect attachment is associated to the on-prem segment.

1. As per the Core Network policy, the traffic is forwarded to the corresponding Amazon VPC, forwarding the traffic to the destination.

## Further reading
<a name="sdwan3-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="sdwan3-diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](sdwan-tgw-connect.md#sdwan1-diagram-history) | Reference architecture diagram first published. | December 28, 2024 | 
| [Initial publication](sdwan-cloudwan-connect.md#sdwan2-diagram-history) | Reference architecture diagram first published. | December 28, 2024 | 
| [Initial publication](#sdwan3-diagram-history) | Reference architecture diagram first published. | December 28, 2024 | 
| [Initial publication](sdwan-vpn-tgw.md#sdwan4-diagram-history) | Reference architecture diagram first published. | December 28, 2024 | 
| [Initial publication](sdwan-vpn-cloudwan.md#sdwan5-diagram-history) | Reference architecture diagram first published. | December 28, 2024 | 
| [Initial publication](sdwan-dx-tgw.md#sdwan6-diagram-history) | Reference architecture diagram first published. | December 28, 2024 | 
| [Initial publication](sdwan-dx-cloudwan.md#sdwan7-diagram-history) | Reference architecture diagram first published. | December 28, 2024 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.