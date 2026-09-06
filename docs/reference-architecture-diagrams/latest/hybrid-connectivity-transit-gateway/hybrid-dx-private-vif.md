

# Hybrid Connectivity with AWS Direct Connect Private VIFs and Inter-VPC with AWS Transit Gateway
<a name="hybrid-dx-private-vif"></a>

Publication date: **August 17, 2022 ([Diagram history](#hc8-diagram-history))**

When transitive communication is not needed in the connection between on-premises and AWS, you can be cost-effective by using VIFs and [Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html) Gateway to connect your corporate data center to your VPCs, and use [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) only for inter-VPC communication.

## Private VIFs for on-premises and AWS Transit Gateway for inter-VPC architecture
<a name="hc8-diagram1"></a>

![Architecture diagram showing AWS Direct Connect private VIFs for on-premises connectivity with AWS Transit Gateway used only for inter-VPC communication.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/hybrid-connectivity-transit-gateway/images/hybrid-connectivity-transit-gateway-8.png)


The following steps describe the AWS to AWS traffic flow:

1. Traffic initiated from an Amazon Elastic Compute Cloud instance in the **spoke VPC A** and destined to **spoke VPC B** is routed to the Transit Gateway ENI as per the **spoke VPC A** route table. Traffic is forwarded to the AWS Transit Gateway.

1. As per the **AWS Transit Gateway spoke VPC route table**, the traffic is routed to **spoke VPC B**. The Transit Gateway ENI in **spoke VPC B** forwards the traffic to the destination.

The following steps describe the on-premises to AWS traffic flow:

1. Traffic from the corporate data center destined to the **spoke VPC A** is forwarded to AWS through the AWS Direct Connect link. The corporate data center can communicate with both VPCs using one single private VIF thanks to the Direct Connect Gateway.

1. For this specific use case, the traffic is forwarded to the Virtual Private Gateway of the **spoke VPC A**.

1. As per the **spoke VPC A** route table, traffic is forwarded to the destination Amazon Elastic Compute Cloud instance.

## Further reading
<a name="hc8-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="hc8-diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](hybrid-vpn.md#hc1-diagram-history) | Reference architecture diagram first published. | August 17, 2022 | 
| [Initial publication](hybrid-dx.md#hc2-diagram-history) | Reference architecture diagram first published. | August 17, 2022 | 
| [Initial publication](hybrid-vpn-primary-backup.md#hc3-diagram-history) | Reference architecture diagram first published. | August 17, 2022 | 
| [Initial publication](hybrid-dx-primary-vpn-backup.md#hc4-diagram-history) | Reference architecture diagram first published. | August 17, 2022 | 
| [Initial publication](hybrid-dx-active-passive.md#hc5-diagram-history) | Reference architecture diagram first published. | August 17, 2022 | 
| [Initial publication](hybrid-vpn-over-dx.md#hc6-diagram-history) | Reference architecture diagram first published. | August 17, 2022 | 
| [Initial publication](hybrid-dx-tgw-connect.md#hc7-diagram-history) | Reference architecture diagram first published. | August 17, 2022 | 
| [Initial publication](#hc8-diagram-history) | Reference architecture diagram first published. | August 17, 2022 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.