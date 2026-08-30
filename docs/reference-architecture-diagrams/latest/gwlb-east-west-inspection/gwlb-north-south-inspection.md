# Gateway Load Balancer North/South Inspection

Publication date: **April 8, 2021 ([Diagram history](#ns-diagram-history "#ns-diagram-history"))**

This architecture uses [Gateway Load Balancer](../../../elasticloadbalancing/latest/userguide/what-is-load-balancing.md "../../../elasticloadbalancing/latest/userguide/what-is-load-balancing.md") to create a highly available and scalable bump-in-the-wire solution for North/South traffic inspection between [Amazon VPC](../../../vpc/latest/userguide/what-is-amazon-vpc.md "../../../vpc/latest/userguide/what-is-amazon-vpc.md") resources and the internet.

## Gateway Load Balancer North/South Inspection architecture

![Architecture diagram showing Gateway Load Balancer for North/South traffic inspection between VPC resources and the internet.](images/gwlb-north-south-inspection.png)

The following steps describe the outbound data flow in this architecture:

1. Traffic from resources in the **APP subnet** destined for the internet routes to the Gateway Load Balancer endpoint in the same VPC.
2. The Gateway Load Balancer endpoint connects to the endpoint service for Gateway Load Balancer in the **Security VPC**. Gateway Load Balancer encapsulates and forwards traffic to the backend security appliances.
3. After the security appliances inspect the traffic, it returns to Gateway Load Balancer and then to the Gateway Load Balancer endpoint.
4. Traffic returns to the origin VPC, follows the **Egress Subnet Route Table**, and routes to the internet gateway.
5. The internet gateway sends the traffic to the internet.

The following steps describe the inbound data flow:

1. Traffic from the internet arrives at the internet gateway.
2. The **Ingress Route Table** routes the traffic to the Gateway Load Balancer endpoint.
3. The Gateway Load Balancer endpoint connects to the endpoint service for Gateway Load Balancer in the **Security VPC**. Gateway Load Balancer encapsulates and forwards traffic to the backend security appliances.
4. After the security appliances inspect the traffic, it returns to Gateway Load Balancer and then to the Gateway Load Balancer endpoint.
5. Traffic arrives in the **App VPC** from the Gateway Load Balancer endpoint and routes locally to the resources in the **App subnet**.

## Related reference architecture

For the complementary East/West inspection pattern, see [Gateway Load Balancer East/West Inspection](gwlb-east-west-chapter.md "gwlb-east-west-chapter.md").

## Further reading

For additional information, see the following resources:

- [AWS Architecture Icons](https://aws.amazon.com/architecture/icons "https://aws.amazon.com/architecture/icons")
- [AWS Architecture Center](https://aws.amazon.com/architecture "https://aws.amazon.com/architecture")
- [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected "https://aws.amazon.com/architecture/well-architected")

## Diagram history

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change                                                                                                       | Description                                     | Date          |
| ------------------------------------------------------------------------------------------------------------ | ----------------------------------------------- | ------------- |
| [Initial publication](gwlb-east-west-chapter.md#diagram-history "gwlb-east-west-chapter.md#diagram-history") | Reference architecture diagram first published. | April 8, 2021 |
| Initial publication                                                                                          | Reference architecture diagram first published. | April 8, 2021 |

###### Note

To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.
