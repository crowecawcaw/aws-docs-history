

# Using AWS Direct Connect
<a name="govcloud-direct-connect"></a>

Publication date: **November 22, 2024 ([Diagram history](#gdx-diagram-history))**

This architecture connects AWS GovCloud (US) and commercial Regions using [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html). You can use transit VIFs or private VIFs, depending on whether you connect Transit Gateways or VPCs, and hairpin traffic through your termination device in the datacenter.

## GovCloud hybrid connectivity with AWS Direct Connect architecture
<a name="gdx-diagram1"></a>

![Architecture diagram showing hybrid connectivity between AWS GovCloud and commercial Regions using AWS Direct Connect with transit gateways and a datacenter for traffic hairpinning.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/govcloud-hybrid-connectivity/images/govcloud-hybrid-connectivity-3.png)


The following steps describe the data flow in this architecture:

1. Traffic from an Amazon EC2 instance in **VPC A** flows to AWS Transit Gateway following the VPC route tables.

1. The **Transit Gateway spoke VPC route table** forwards the traffic through AWS Direct Connect to the datacenter. The datacenter advertises a supernet, while the Direct Connect gateways advertise the Region VPC CIDRs using the allowed prefixes feature.

1. The datacenter routes the traffic back to the more specific Direct Connect route, and it arrives at the GovCloud Transit Gateway.

1. The **Transit Gateway spoke VPC route table** forwards traffic to **VPC B**, and to the destination using the VPC route table. Return traffic follows the same path in reverse order.

For more information about associating the Direct Connect gateway, see [Hybrid connectivity to AWS GovCloud (US) and commercial Regions using AWS Direct Connect](https://aws.amazon.com/blogs/publicsector/aws-hybrid-connectivity-sharing-aws-direct-connect-aws-govcloud-us-commercial-regions/).

For more information about how AWS Direct Connect differs for AWS GovCloud (US), see [How AWS Direct Connect differs for AWS GovCloud (US)](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-dc.html).

## Further reading
<a name="gdx-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="gdx-diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](govcloud-public-ip.md#gpub-diagram-history) | Reference architecture diagram first published. | November 22, 2024 | 
| [Initial publication](govcloud-site-to-site-vpn.md#gvpn-diagram-history) | Reference architecture diagram first published. | November 22, 2024 | 
| [Initial publication](#gdx-diagram-history) | Reference architecture diagram first published. | November 22, 2024 | 
| [Initial publication](govcloud-tgw-connect.md#gtgw-diagram-history) | Reference architecture diagram first published. | November 22, 2024 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.