

# Gateway Load Balancer Centralized Egress Inspection
<a name="gwlb-centralized-egress-inspection"></a>

Publication date: **February 15, 2022 ([Diagram history](#diagram-history))**

This architecture uses [Gateway Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html) to build highly available and scalable centralized egress environments with traffic inspection. It combines [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) with Gateway Load Balancer endpoints and NAT Gateway for a complete inspection solution.

## Gateway Load Balancer Centralized Egress Inspection architecture
<a name="diagram1"></a>

![Architecture diagram showing Gateway Load Balancer centralized egress inspection with AWS Transit Gateway and NAT Gateway.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/gwlb-centralized-egress-inspection/images/gwlb-centralized-egress-inspection.png)


The following steps describe the egress data flow in this architecture:

1. Internet traffic from the [Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) instance in the **Application VPC** routes through AWS Transit Gateway through the VPC-TGW spoke attachment. The **TGW spoke route table** routes traffic to the **Inspection VPC**.

1. Traffic enters the **Inspection VPC** on the Transit Gateway attachment subnet.

1. The **TGW attachment subnet route table** routes the traffic to the Gateway Load Balancer endpoint in the same Availability Zone.

1. The Gateway Load Balancer endpoint forwards the traffic to Gateway Load Balancer. Gateway Load Balancer encapsulates the traffic in Generic Network Virtualization Encapsulation (GENEVE).

1. GENEVE-encapsulated traffic routes to the security appliance for inspection.

1. After inspection completes, the traffic returns to Gateway Load Balancer and then to the Gateway Load Balancer endpoint.

1. Gateway Load Balancer routes the inspected traffic to the NAT Gateway in the same Availability Zone. The source IP changes to the NAT Gateway IP.

1. The NAT Gateway routes internet traffic to the internet gateway. Traffic leaves for the internet through the internet gateway.

The following steps describe the return data flow:

1. Return traffic from the internet routes to the NAT Gateway by the internet gateway.

1. The NAT Gateway sends return traffic to the Gateway Load Balancer endpoint in accordance with the **NAT Gateway route table**.

1. The Gateway Load Balancer endpoint sends the return traffic to Gateway Load Balancer, which encapsulates traffic in GENEVE.

1. GENEVE-encapsulated return traffic routes to the security appliance for inspection.

1. After the return traffic inspection completes, it returns to Gateway Load Balancer and then to the Gateway Load Balancer endpoint.

1. Return traffic routes to the Transit Gateway attachment following the **Security Appliance route table**.

1. Return traffic routes back to **App VPC 1** through the **TGW inspection route table**.

1. Return traffic arrives in **App VPC 1** from AWS Transit Gateway and routes locally to the source Amazon EC2 instance.

## Further reading
<a name="further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | February 15, 2022 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.