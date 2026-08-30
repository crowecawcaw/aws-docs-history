# North/South Outbound Distributed Inspection

Publication date: **July 21, 2022 ([Diagram history](#dout-diagram-history "#dout-diagram-history"))**

This architecture uses [Gateway Load Balancer](../../../elasticloadbalancing/latest/gateway/introduction.md "../../../elasticloadbalancing/latest/gateway/introduction.md") to inspect outbound traffic in a distributed fashion. Multiple VPCs share the same backend security appliances through [AWS PrivateLink](../../../vpc/latest/privatelink/what-is-privatelink.md "../../../vpc/latest/privatelink/what-is-privatelink.md") for traffic destined to the internet.

## North/South outbound distributed inspection architecture

![Architecture diagram showing distributed outbound inspection with Gateway Load Balancer using shared security appliances for internet-bound traffic.](images/distributed-inspection-gwlb-2.png)

The following steps describe the data flow in this architecture:

1. Traffic from an Amazon EC2 instance destined for the internet arrives at NAT Gateway, which translates the source IP of the packets.
2. NAT Gateway forwards the translated packets to a Gateway Load Balancer endpoint using the **public subnet route table**.
3. The Gateway Load Balancer endpoint forwards the traffic to Gateway Load Balancer in the **appliances VPC** using AWS PrivateLink.
4. Gateway Load Balancer encapsulates the traffic in GENEVE and sends it to a security appliance for inspection.
5. The security appliance inspects the traffic and returns it to Gateway Load Balancer.
6. The traffic returns to the Gateway Load Balancer endpoint in the **inspect subnet**.
7. The Gateway Load Balancer endpoint uses the **inspect subnet route table** to forward the traffic to the internet gateway.

For best practices when deploying Gateway Load Balancer, see [Best practices for deploying Gateway Load Balancer](https://aws.amazon.com/blogs/networking-and-content-delivery/best-practices-for-deploying-gateway-load-balancer/ "https://aws.amazon.com/blogs/networking-and-content-delivery/best-practices-for-deploying-gateway-load-balancer/").

For more information about implementing a distributed inspection architecture, see [Scaling network traffic inspection using AWS Gateway Load Balancer](https://aws.amazon.com/blogs/networking-and-content-delivery/scaling-network-traffic-inspection-using-aws-gateway-load-balancer/ "https://aws.amazon.com/blogs/networking-and-content-delivery/scaling-network-traffic-inspection-using-aws-gateway-load-balancer/").

## Further reading

For additional information, see the following resources:

- [AWS Architecture Icons](https://aws.amazon.com/architecture/icons "https://aws.amazon.com/architecture/icons")
- [AWS Architecture Center](https://aws.amazon.com/architecture "https://aws.amazon.com/architecture")
- [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected "https://aws.amazon.com/architecture/well-architected")

## Diagram history

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change                                                                                                                                         | Description                                     | Date          |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- | ------------- |
| [Initial publication](distributed-inbound-inspection.md#dinb-diagram-history "distributed-inbound-inspection.md#dinb-diagram-history")         | Reference architecture diagram first published. | July 21, 2022 |
| Initial publication                                                                                                                            | Reference architecture diagram first published. | July 21, 2022 |
| [Initial publication](distributed-east-west-inspection.md#dew-diagram-history "distributed-east-west-inspection.md#dew-diagram-history")       | Reference architecture diagram first published. | July 21, 2022 |
| [Initial publication](distributed-inspection-route-tables.md#drt-diagram-history "distributed-inspection-route-tables.md#drt-diagram-history") | Reference architecture diagram first published. | July 21, 2022 |

###### Note

To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.
