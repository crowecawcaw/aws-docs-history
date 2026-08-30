# AWS Direct Connect and Transit Gateway Connect Attachments

Publication date: **August 17, 2022 ([Diagram history](#hc7-diagram-history "#hc7-diagram-history"))**

This architecture shows how to use [AWS Transit Gateway](../../../vpc/latest/tgw/what-is-transit-gateway.md "../../../vpc/latest/tgw/what-is-transit-gateway.md") Connect attachments to simplify your route management across hybrid cloud environments. This design allows the creation of several Connect attachments over the same [AWS Direct Connect](../../../directconnect/latest/UserGuide/Welcome.md "../../../directconnect/latest/UserGuide/Welcome.md") link to achieve the logical separation of traffic.

## AWS Direct Connect with Transit Gateway Connect attachments architecture

![Architecture diagram showing AWS Direct Connect with Transit Gateway Connect attachments using GRE tunneling and BGP for simplified route management.](images/hybrid-connectivity-transit-gateway-7.png)

The following steps describe the AWS to on-premises traffic flow:

1. Traffic initiated from an instance in the **spoke VPC A** and destined to the corporate data center is routed to the TGW ENI as per the **spoke VPC A** route table.
2. Traffic is forwarded to the Transit Gateway. As per the **spoke VPC route table**, the traffic is routed to the corporate data center through the Transit Gateway Connect attachment.
3. The Transit Gateway Connect attachment uses the Direct Connect connection as transport, and connects the Transit Gateway to the corporate data center device using Generic Routing Encapsulation (GRE) tunneling and BGP.

The following steps describe the on-premises to AWS traffic flow:

1. Traffic from the corporate data center destined to the **spoke VPC B** is forwarded to the Transit Gateway through the GRE tunnel of the Transit Gateway Connect attachment, over the Direct Connect link.
2. As per the **Transit Gateway Connect route table**, the traffic is forwarded to the **spoke VPC B** attachment.
3. The TGW ENI of the **spoke VPC B** forwards the traffic to the destination.

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
| [Initial publication](hybrid-dx.md#hc2-diagram-history "hybrid-dx.md#hc2-diagram-history")                                       | Reference architecture diagram first published. | August 17, 2022 |
| [Initial publication](hybrid-vpn-primary-backup.md#hc3-diagram-history "hybrid-vpn-primary-backup.md#hc3-diagram-history")       | Reference architecture diagram first published. | August 17, 2022 |
| [Initial publication](hybrid-dx-primary-vpn-backup.md#hc4-diagram-history "hybrid-dx-primary-vpn-backup.md#hc4-diagram-history") | Reference architecture diagram first published. | August 17, 2022 |
| [Initial publication](hybrid-dx-active-passive.md#hc5-diagram-history "hybrid-dx-active-passive.md#hc5-diagram-history")         | Reference architecture diagram first published. | August 17, 2022 |
| [Initial publication](hybrid-vpn-over-dx.md#hc6-diagram-history "hybrid-vpn-over-dx.md#hc6-diagram-history")                     | Reference architecture diagram first published. | August 17, 2022 |
| Initial publication                                                                                                              | Reference architecture diagram first published. | August 17, 2022 |
| [Initial publication](hybrid-dx-private-vif.md#hc8-diagram-history "hybrid-dx-private-vif.md#hc8-diagram-history")               | Reference architecture diagram first published. | August 17, 2022 |

###### Note

To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.
