# Centralized Internet Egress with NAT Gateway

Publication date: **October 20, 2021 ([Diagram history](#diagram-history "#diagram-history"))**

This architecture uses NAT Gateway and [AWS Transit Gateway](../../../vpc/latest/tgw/what-is-transit-gateway.md "../../../vpc/latest/tgw/what-is-transit-gateway.md") to create a highly available centralized internet egress for all [Amazon VPCs](../../../vpc/latest/userguide/what-is-amazon-vpc.md "../../../vpc/latest/userguide/what-is-amazon-vpc.md") while isolating inter-VPC traffic.

## Centralized Internet Egress with NAT Gateway architecture

![Architecture diagram showing centralized internet egress using NAT Gateway and AWS Transit Gateway with inter-VPC traffic isolation.](images/centralized-egress-nat-gateway.png)

The following steps describe the data flow in this architecture:

1. Traffic from the [Amazon Elastic Compute Cloud](../../../AWSEC2/latest/UserGuide/concepts.md "../../../AWSEC2/latest/UserGuide/concepts.md") instance in the **workload subnet** reaches the internet. The subnet route table routes to AWS Transit Gateway through the default route (**0.0.0.0/0**).
2. Traffic enters AWS Transit Gateway on the VPC-Transit Gateway attachment. The Transit Gateway route table routes the traffic to the **egress VPC** through the default route.
3. Traffic enters the **egress VPC** on the **Transit Gateway attachment subnet**. This subnet route table routes the traffic to the NAT Gateway in that Availability Zone through the default route.
4. Traffic enters the NAT Gateway, and the source IP changes to the NAT Gateway IP.
5. When exiting the NAT Gateway, the traffic looks up the **public subnet route table** and routes to the internet gateway.
6. The traffic leaves for the internet.

## Further reading

For additional information, see the following resources:

- [Creating a single internet exit point from multiple VPCs using AWS Transit Gateway](https://aws.amazon.com/blogs/networking-and-content-delivery/creating-a-single-internet-exit-point-from-multiple-vpcs-using-aws-transit-gateway/ "https://aws.amazon.com/blogs/networking-and-content-delivery/creating-a-single-internet-exit-point-from-multiple-vpcs-using-aws-transit-gateway/") (blog post)
- [AWS Architecture Icons](https://aws.amazon.com/architecture/icons "https://aws.amazon.com/architecture/icons")
- [AWS Architecture Center](https://aws.amazon.com/architecture "https://aws.amazon.com/architecture")
- [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected "https://aws.amazon.com/architecture/well-architected")

## Diagram history

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change              | Description                                     | Date             |
| ------------------- | ----------------------------------------------- | ---------------- |
| Initial publication | Reference architecture diagram first published. | October 20, 2021 |

###### Note

To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.
