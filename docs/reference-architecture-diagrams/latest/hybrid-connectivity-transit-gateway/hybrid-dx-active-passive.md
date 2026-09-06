

# AWS Direct Connect in Active/Passive Configuration
<a name="hybrid-dx-active-passive"></a>

Publication date: **August 17, 2022 ([Diagram history](#hc5-diagram-history))**

You can use a Transit VIF and a [Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html) gateway to connect your on-premises environments to AWS. With this, you can benefit from the connectivity to multiple VPCs without the need of several Direct Connect connections. Having a secondary Direct Connect connection as backup line allows you to achieve high availability in the hybrid setup.

## AWS Direct Connect active/passive configuration architecture
<a name="hc5-diagram1"></a>

![Architecture diagram showing two AWS Direct Connect connections in active/passive configuration with AWS Transit Gateway.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/hybrid-connectivity-transit-gateway/images/hybrid-connectivity-transit-gateway-5.png)


The following steps describe the on-premises to AWS traffic flow:

1. Traffic from the office branch destined to the **spoke VPC B** is forwarded to the Transit Gateway through the active AWS Direct Connect link. The active/passive behavior in the Direct Connect links can be achieved by configuring the BGP configuration of each Transit VIF accordingly. The Transit Gateway is connected to Direct Connect by using a Transit VIF and a Direct Connect Gateway.

1. As per the **Transit Gateway on-premises route table**, the traffic is forwarded to the **spoke VPC B** attachment.

1. The TGW ENI of the **spoke VPC B** forwards the traffic to the destination.

The following steps describe the AWS to on-premises traffic flow:

1. Traffic initiated from an Amazon Elastic Compute Cloud instance in the **spoke VPC A** and destined to the office branch is routed to the Transit Gateway ENI as per the **spoke VPC A** route table.

1. As per the **Transit Gateway spoke VPC route table**, the traffic is forwarded to the Direct Connect gateway.

1. Because of the BGP configuration of both Direct Connect connections, the active link is the preferred one for the traffic from the Transit Gateway to the office branch.

For more information about how to configure active/passive configurations with AWS Direct Connect, see [Creating active/passive BGP connections over AWS Direct Connect](https://aws.amazon.com/blogs/networking-and-content-delivery/creating-active-passive-bgp-connections-over-aws-direct-connect/) on the AWS Blog.

## Further reading
<a name="hc5-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="hc5-diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](hybrid-vpn.md#hc1-diagram-history) | Reference architecture diagram first published. | August 17, 2022 | 
| [Initial publication](hybrid-dx.md#hc2-diagram-history) | Reference architecture diagram first published. | August 17, 2022 | 
| [Initial publication](hybrid-vpn-primary-backup.md#hc3-diagram-history) | Reference architecture diagram first published. | August 17, 2022 | 
| [Initial publication](hybrid-dx-primary-vpn-backup.md#hc4-diagram-history) | Reference architecture diagram first published. | August 17, 2022 | 
| [Initial publication](#hc5-diagram-history) | Reference architecture diagram first published. | August 17, 2022 | 
| [Initial publication](hybrid-vpn-over-dx.md#hc6-diagram-history) | Reference architecture diagram first published. | August 17, 2022 | 
| [Initial publication](hybrid-dx-tgw-connect.md#hc7-diagram-history) | Reference architecture diagram first published. | August 17, 2022 | 
| [Initial publication](hybrid-dx-private-vif.md#hc8-diagram-history) | Reference architecture diagram first published. | August 17, 2022 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.