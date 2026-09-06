

# North/South Inbound Distributed Inspection
<a name="distributed-inbound-inspection"></a>

Publication date: **July 21, 2022 ([Diagram history](#dinb-diagram-history))**

This architecture uses [Gateway Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/introduction.html) to inspect inbound traffic in a distributed fashion. Multiple VPCs share the same backend security appliances in a centralized appliances VPC connected through [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html).

## North/South inbound distributed inspection architecture
<a name="dinb-diagram1"></a>

![Architecture diagram showing distributed inbound inspection with Gateway Load Balancer using shared security appliances across multiple VPCs.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/distributed-inspection-gwlb/images/distributed-inspection-gwlb-1.png)


The following steps describe the data flow in this architecture:

1. Traffic from the internet destined for the Application Load Balancer arrives at the internet gateway. The **ingress route table** forwards it to a Gateway Load Balancer endpoint.

1. The Gateway Load Balancer endpoint forwards the traffic to Gateway Load Balancer in the **appliances VPC** using AWS PrivateLink.

1. Gateway Load Balancer encapsulates the traffic in Generic Network Virtualization Encapsulation (GENEVE) and sends it to a security appliance for inspection.

1. The security appliance inspects the traffic and returns it to Gateway Load Balancer.

1. The traffic returns to the Gateway Load Balancer endpoint in the **inspect subnet**.

1. The Gateway Load Balancer endpoint uses the **inspect subnet route table** to forward the traffic to the Application Load Balancer in the **public subnet**.

1. The Application Load Balancer forwards the traffic to one of its healthy Amazon EC2 instances.

For best practices when deploying Gateway Load Balancer, see [Best practices for deploying Gateway Load Balancer](https://aws.amazon.com/blogs/networking-and-content-delivery/best-practices-for-deploying-gateway-load-balancer/).

For more information about implementing a distributed inspection architecture, see [Scaling network traffic inspection using AWS Gateway Load Balancer](https://aws.amazon.com/blogs/networking-and-content-delivery/scaling-network-traffic-inspection-using-aws-gateway-load-balancer/).

## Further reading
<a name="dinb-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="dinb-diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#dinb-diagram-history) | Reference architecture diagram first published. | July 21, 2022 | 
| [Initial publication](distributed-outbound-inspection.md#dout-diagram-history) | Reference architecture diagram first published. | July 21, 2022 | 
| [Initial publication](distributed-east-west-inspection.md#dew-diagram-history) | Reference architecture diagram first published. | July 21, 2022 | 
| [Initial publication](distributed-inspection-route-tables.md#drt-diagram-history) | Reference architecture diagram first published. | July 21, 2022 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.