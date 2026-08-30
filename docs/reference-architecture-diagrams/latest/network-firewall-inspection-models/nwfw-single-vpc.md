# Traffic Inspection with AWS Network Firewall

Publication date: **March 16, 2022 ([Diagram history](#nwfw1-diagram-history "#nwfw1-diagram-history"))**

This architecture shows how to inspect inbound and outbound traffic using [AWS Network Firewall](../../../network-firewall/latest/developerguide/what-is-aws-network-firewall.md "../../../network-firewall/latest/developerguide/what-is-aws-network-firewall.md") in a single Amazon VPC deployment. Traffic from the internet destined for an Application Load Balancer is transparently inspected by Network Firewall, while outbound traffic from instances is also inspected before reaching the internet through a NAT gateway.

## Single Amazon VPC inspection with Network Firewall architecture

![Architecture diagram showing single VPC traffic inspection with AWS Network Firewall for both inbound and outbound traffic flows.](images/network-firewall-inspection-models-1.png)

The following steps describe the inbound traffic flow in this architecture:

1. Traffic initiated from a client on the internet and destined to the public IP of the Application Load Balancer arrives at the internet gateway.
2. In accordance with the **internet gateway ingress table**, traffic is sent to the firewall endpoint.
3. Traffic is transparently inspected by AWS Network Firewall. Allowed traffic is sent back to the firewall endpoint.
4. According to the **inspection subnet route table**, traffic is sent to the Application Load Balancer.
5. As per the **protected subnet route table**, the Application Load Balancer forwards the traffic to the target group (workload on Amazon Elastic Compute Cloud).
6. Response traffic is returned back to the Application Load Balancer according to the **private subnet route table**.
7. In accordance with the **protected subnet route table**, traffic is sent to the firewall endpoint.
8. Traffic is sent to AWS Network Firewall. Traffic that complies with firewall rules is sent back to the firewall endpoint.
9. As per the **inspection subnet route table**, traffic is sent to the internet gateway.
10. Traffic is sent back to the internet.

The following steps describe the outbound traffic flow:

1. Traffic initiated from an instance and directed to the internet is forwarded to the NAT gateway, in accordance with the **private subnet route table**.
2. Source IP of traffic is changed to the IP of the NAT gateway, and the traffic is forwarded to the firewall endpoint as per the **protected subnet route table**.
3. Traffic is sent to AWS Network Firewall for inspection. Traffic that complies with firewall rules is sent back to the firewall endpoint.
4. According to the **inspection subnet route table**, traffic is forwarded to the internet gateway.
5. Traffic is sent out to the internet.

## Further reading

For additional information, see the following resources:

- [AWS Architecture Icons](https://aws.amazon.com/architecture/icons "https://aws.amazon.com/architecture/icons")
- [AWS Architecture Center](https://aws.amazon.com/architecture "https://aws.amazon.com/architecture")
- [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected "https://aws.amazon.com/architecture/well-architected")

## Diagram history

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change                                                                                                         | Description                                     | Date           |
| -------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- | -------------- |
| Initial publication                                                                                            | Reference architecture diagram first published. | March 16, 2022 |
| [Initial publication](nwfw-intra-vpc.md#nwfw2-diagram-history "nwfw-intra-vpc.md#nwfw2-diagram-history")       | Reference architecture diagram first published. | March 16, 2022 |
| [Initial publication](nwfw-east-west.md#nwfw3-diagram-history "nwfw-east-west.md#nwfw3-diagram-history")       | Reference architecture diagram first published. | March 16, 2022 |
| [Initial publication](nwfw-north-south.md#nwfw4-diagram-history "nwfw-north-south.md#nwfw4-diagram-history")   | Reference architecture diagram first published. | March 16, 2022 |
| [Initial publication](nwfw-combined.md#nwfw5-diagram-history "nwfw-combined.md#nwfw5-diagram-history")         | Reference architecture diagram first published. | March 16, 2022 |
| [Initial publication](nwfw-multi-region.md#nwfw6-diagram-history "nwfw-multi-region.md#nwfw6-diagram-history") | Reference architecture diagram first published. | March 16, 2022 |

###### Note

To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.
