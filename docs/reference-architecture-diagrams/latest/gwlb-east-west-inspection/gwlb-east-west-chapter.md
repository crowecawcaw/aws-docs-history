

# Gateway Load Balancer East/West Inspection
<a name="gwlb-east-west-chapter"></a>

Publication date: **April 8, 2021 ([Diagram history](#diagram-history))**

This architecture uses [Gateway Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html) and [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) to create a highly available and scalable bump-in-the-wire solution for East/West traffic inspection between [Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) workloads.

## Gateway Load Balancer East/West Inspection architecture
<a name="diagram1"></a>

![Architecture diagram showing Gateway Load Balancer with AWS Transit Gateway for East/West traffic inspection between VPCs.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/gwlb-east-west-inspection/images/gwlb-east-west-inspection.png)


The following steps describe the data flow in this architecture:

1. Traffic from IP **10.0.1.10** in **App1 VPC** targets IP **10.1.2.20** in **App2 VPC**. The subnet route table routes traffic to AWS Transit Gateway through the default route (**0.0.0.0/0**).

1. **App1 VPC** associates with the **TGW RT APP** route table in AWS Transit Gateway. This table forwards all traffic (**0.0.0.0/0**) through the **Security VPC** attachment.

1. The Transit Gateway ENI in the **Security VPC** uses its subnet route table to forward all traffic to **Gateway Load Balancer endpoint 1**.

1. The Gateway Load Balancer endpoint forwards the traffic to Gateway Load Balancer.

1. Gateway Load Balancer sends encapsulated traffic to a security appliance instance for inspection.

1. After inspection completes, the security appliance returns the traffic to Gateway Load Balancer.

1. Gateway Load Balancer forwards the inspected traffic back to the Gateway Load Balancer endpoint.

1. The Gateway Load Balancer endpoint uses its subnet route table to forward all non-local traffic to AWS Transit Gateway through the Transit Gateway attachment.

1. Traffic reaches AWS Transit Gateway and uses the **TGW RT Sec** route table associated with the **Security VPC** to find the destination through the **App2 VPC** attachment.

1. Traffic arrives at the **App2 VPC** route table. The destination (**10.1.2.20**) is a local address, so the traffic routes to the destination instance.

## Related reference architecture
<a name="see-also"></a>

For the complementary North/South inspection pattern, see [Gateway Load Balancer North/South Inspection](gwlb-north-south-inspection.md).

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
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | April 8, 2021 | 
| [Initial publication](gwlb-north-south-inspection.md#ns-diagram-history) | Reference architecture diagram first published. | April 8, 2021 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.