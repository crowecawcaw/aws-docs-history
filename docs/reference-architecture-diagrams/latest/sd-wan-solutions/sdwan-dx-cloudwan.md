# SD-WAN Devices Integration with AWS Cloud WAN and AWS Direct Connect through AWS Transit Gateway

Publication date: **December 28, 2024 ([Diagram history](#sdwan7-diagram-history "#sdwan7-diagram-history"))**

When extending your SD-WAN traffic to AWS through [AWS Direct Connect](../../../directconnect/latest/UserGuide/Welcome.md "../../../directconnect/latest/UserGuide/Welcome.md") to AWS Cloud WAN, you can make use of [AWS Transit Gateway](../../../vpc/latest/tgw/what-is-transit-gateway.md "../../../vpc/latest/tgw/what-is-transit-gateway.md") Connect attachments and a peering between Cloud WAN and Transit Gateway to achieve end-to-end dynamic routing. You can extend each VRF in your on-premises environment by using a different Transit Gateway Connect peer and route table, and Cloud WAN route table attachment and segment.

## SD-WAN devices integration with AWS Cloud WAN and AWS Direct Connect architecture

![Architecture diagram showing SD-WAN devices integration with AWS Cloud WAN and AWS Direct Connect through AWS Transit Gateway with peering between Cloud WAN and Transit Gateway.](images/sd-wan-solutions-7.png)

The following steps describe the AWS to on-premises traffic flow:

1. Traffic initiated from an instance in a [Amazon VPC](../../../vpc/latest/userguide/what-is-amazon-vpc.md "../../../vpc/latest/userguide/what-is-amazon-vpc.md") in Region A and destined to the corporate data center SD-WAN device is forwarded to the Core Network. The Amazon VPC attachment is associated to the prod segment.
2. As per the Core Network policy, traffic arriving to the prod segment destined to the corporate data center should be forwarded to the Transit Gateway route table attachment. The local attachment will be preferred. Traffic will be forwarded to the AWS Transit Gateway in Region A.
3. As per the Transit Gateway route table, traffic will be forwarded through the Transit Gateway Connect attachment A. This attachment uses the Direct Connect connection as transport, and connects the Transit Gateway to the corporate data center SD-WAN device using GRE tunneling and BGP.

The following steps describe the on-premises to AWS traffic flow:

1. Traffic from the corporate data center SD-WAN device destined to a Amazon VPC in Region B is forwarded to the Transit Gateway in Region B through the Transit Gateway Connect attachment B, over the Direct Connect link.
2. As per the Transit Gateway route table, the traffic is forwarded to the Core Network. The Transit Gateway route table attachment is associated to the on-prem segment.
3. The Core Network forwards the traffic to the corresponding Amazon VPC.

## Further reading

For additional information, see the following resources:

- [AWS Architecture Icons](https://aws.amazon.com/architecture/icons "https://aws.amazon.com/architecture/icons")
- [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected "https://aws.amazon.com/architecture/well-architected")

## Diagram history

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change                                                                                                                           | Description                                     | Date              |
| -------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- | ----------------- |
| [Initial publication](sdwan-tgw-connect.md#sdwan1-diagram-history "sdwan-tgw-connect.md#sdwan1-diagram-history")                 | Reference architecture diagram first published. | December 28, 2024 |
| [Initial publication](sdwan-cloudwan-connect.md#sdwan2-diagram-history "sdwan-cloudwan-connect.md#sdwan2-diagram-history")       | Reference architecture diagram first published. | December 28, 2024 |
| [Initial publication](sdwan-cloudwan-tunnelless.md#sdwan3-diagram-history "sdwan-cloudwan-tunnelless.md#sdwan3-diagram-history") | Reference architecture diagram first published. | December 28, 2024 |
| [Initial publication](sdwan-vpn-tgw.md#sdwan4-diagram-history "sdwan-vpn-tgw.md#sdwan4-diagram-history")                         | Reference architecture diagram first published. | December 28, 2024 |
| [Initial publication](sdwan-vpn-cloudwan.md#sdwan5-diagram-history "sdwan-vpn-cloudwan.md#sdwan5-diagram-history")               | Reference architecture diagram first published. | December 28, 2024 |
| [Initial publication](sdwan-dx-tgw.md#sdwan6-diagram-history "sdwan-dx-tgw.md#sdwan6-diagram-history")                           | Reference architecture diagram first published. | December 28, 2024 |
| Initial publication                                                                                                              | Reference architecture diagram first published. | December 28, 2024 |

###### Note

To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.
