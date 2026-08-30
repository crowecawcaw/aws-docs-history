# Hybrid Connectivity to AWS Transit Gateway with AWS Direct Connect

Publication date: **August 17, 2022 ([Diagram history](#hc2-diagram-history "#hc2-diagram-history"))**

You can use a Transit VIF and a [Direct Connect](../../../directconnect/latest/UserGuide/Welcome.md "../../../directconnect/latest/UserGuide/Welcome.md") gateway to connect your on-premises environments to AWS. With this, you can benefit from the connectivity to multiple VPCs without the need of several Direct Connect connections. It is recommended to use a second connection (Direct Connect or VPN) for high availability.

## Hybrid connectivity with AWS Direct Connect architecture

![Architecture diagram showing hybrid connectivity to AWS Transit Gateway using AWS Direct Connect with a Transit VIF and Direct Connect gateway.](images/hybrid-connectivity-transit-gateway-2.png)

The following steps describe the on-premises to AWS traffic flow:

1. Traffic from the corporate data center destined to the **spoke VPC A** is forwarded to AWS Transit Gateway through the AWS Direct Connect (DX) link. The Transit Gateway is connected to the Direct Connect link by using a Transit virtual interface (VIF) and a Direct Connect Gateway.
2. As per the **Transit Gateway on-premises route table**, the traffic is forwarded to the **spoke VPC A** attachment.
3. The Transit Gateway ENI of the **spoke VPC A** forwards the traffic to the destination.

The following steps describe the AWS to on-premises traffic flow:

1. Traffic initiated from an Amazon Elastic Compute Cloud instance in the **spoke VPC B** and destined to the corporate data center is routed to the Transit Gateway ENI as per the **spoke VPC B** route table.
2. Traffic is forwarded to the AWS Transit Gateway. As per the **spoke VPC route table**, the traffic is routed to the office branch through the AWS Direct Connect Gateway attachment.
3. The traffic is routed to the destination through the AWS Direct Connect link.

For more information about how to create an AWS Direct Connect connection, see [Create a Direct Connect dedicated connection](../../../directconnect/latest/UserGuide/create-connection.md "../../../directconnect/latest/UserGuide/create-connection.md").

## Further reading

For additional information, see the following resources:

- [AWS Architecture Icons](https://aws.amazon.com/architecture/icons "https://aws.amazon.com/architecture/icons")
- [AWS Architecture Center](https://aws.amazon.com/architecture "https://aws.amazon.com/architecture")
- [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected "https://aws.amazon.com/architecture/well-architected")

## Diagram history

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change                                                                                                                           | Description                                     | Date            |
| -------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- | --------------- |
| [Initial publication](hybrid-vpn.md#hc1-diagram-history "hybrid-vpn.md#hc1-diagram-history")                                     | Reference architecture diagram first published. | August 17, 2022 |
| Initial publication                                                                                                              | Reference architecture diagram first published. | August 17, 2022 |
| [Initial publication](hybrid-vpn-primary-backup.md#hc3-diagram-history "hybrid-vpn-primary-backup.md#hc3-diagram-history")       | Reference architecture diagram first published. | August 17, 2022 |
| [Initial publication](hybrid-dx-primary-vpn-backup.md#hc4-diagram-history "hybrid-dx-primary-vpn-backup.md#hc4-diagram-history") | Reference architecture diagram first published. | August 17, 2022 |
| [Initial publication](hybrid-dx-active-passive.md#hc5-diagram-history "hybrid-dx-active-passive.md#hc5-diagram-history")         | Reference architecture diagram first published. | August 17, 2022 |
| [Initial publication](hybrid-vpn-over-dx.md#hc6-diagram-history "hybrid-vpn-over-dx.md#hc6-diagram-history")                     | Reference architecture diagram first published. | August 17, 2022 |
| [Initial publication](hybrid-dx-tgw-connect.md#hc7-diagram-history "hybrid-dx-tgw-connect.md#hc7-diagram-history")               | Reference architecture diagram first published. | August 17, 2022 |
| [Initial publication](hybrid-dx-private-vif.md#hc8-diagram-history "hybrid-dx-private-vif.md#hc8-diagram-history")               | Reference architecture diagram first published. | August 17, 2022 |

###### Note

To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.
