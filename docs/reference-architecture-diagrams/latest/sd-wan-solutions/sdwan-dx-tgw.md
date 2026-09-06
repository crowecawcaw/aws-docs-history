

# SD-WAN Devices Integration with AWS Transit Gateway and AWS Direct Connect
<a name="sdwan-dx-tgw"></a>

Publication date: **December 28, 2024 ([Diagram history](#sdwan6-diagram-history))**

This architecture shows how to use [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) Connect attachments and [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html) to extend and segment your SD-WAN traffic to AWS without adding extra infrastructure. Each Transit Gateway Connect Peer can have its own Transit Gateway Route Table and BGP peer to extend an on-premises VRF if required.

## SD-WAN devices integration with AWS Transit Gateway and AWS Direct Connect architecture
<a name="sdwan6-diagram1"></a>

![Architecture diagram showing SD-WAN devices integration with AWS Transit Gateway Connect attachments and AWS Direct Connect using GRE tunneling over Direct Connect.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/sd-wan-solutions/images/sd-wan-solutions-6.png)


The following steps describe the AWS to on-premises traffic flow:

1. Traffic initiated from an instance in the Spoke [Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) A and destined to the corporate data center SD-WAN device is routed to the TGW ENI as per the Spoke Amazon VPC A Route Table.

1. Traffic is forwarded to the Transit Gateway. As per the **Spoke VPC route table**, the traffic is routed to the corporate data center through the Transit Gateway Connect attachment.

1. The Transit Gateway Connect attachment uses the Direct Connect connection as transport, and connects the Transit Gateway to the corporate data center SD-WAN device using GRE tunneling and BGP.

The following steps describe the on-premises to AWS traffic flow:

1. Traffic from the corporate data center SD-WAN device destined to the **Spoke VPC B** is forwarded to the Transit Gateway through the GRE tunnel of the Transit Gateway attachment, over the Direct Connect link.

1. As per the **Transit Gateway Connect route table**, the traffic is forwarded to the **Spoke VPC B** attachment.

1. The TGW ENI of the **Spoke VPC B** forwards the traffic to the destination.

For more information about how to integrate your on-premises SD-WAN devices using AWS Transit Gateway and AWS Direct Connect, see [Integrate SD-WAN devices with AWS Transit Gateway and AWS Direct Connect](https://aws.amazon.com/blogs/networking-and-content-delivery/integrate-sd-wan-devices-with-aws-transit-gateway-and-aws-direct-connect/).

## Further reading
<a name="sdwan6-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="sdwan6-diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](sdwan-tgw-connect.md#sdwan1-diagram-history) | Reference architecture diagram first published. | December 28, 2024 | 
| [Initial publication](sdwan-cloudwan-connect.md#sdwan2-diagram-history) | Reference architecture diagram first published. | December 28, 2024 | 
| [Initial publication](sdwan-cloudwan-tunnelless.md#sdwan3-diagram-history) | Reference architecture diagram first published. | December 28, 2024 | 
| [Initial publication](sdwan-vpn-tgw.md#sdwan4-diagram-history) | Reference architecture diagram first published. | December 28, 2024 | 
| [Initial publication](sdwan-vpn-cloudwan.md#sdwan5-diagram-history) | Reference architecture diagram first published. | December 28, 2024 | 
| [Initial publication](#sdwan6-diagram-history) | Reference architecture diagram first published. | December 28, 2024 | 
| [Initial publication](sdwan-dx-cloudwan.md#sdwan7-diagram-history) | Reference architecture diagram first published. | December 28, 2024 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.