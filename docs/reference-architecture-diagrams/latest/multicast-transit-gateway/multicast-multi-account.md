

# Multicast Traffic in Multi-Account Environments
<a name="multicast-multi-account"></a>

Publication date: **May 5, 2022 ([Diagram history](#mmulti-diagram-history))**

This architecture uses [AWS Resource Access Manager (RAM)](https://docs.aws.amazon.com/ram/latest/userguide/what-is.html) to share multicast domains to other AWS accounts. Consumers can associate or disassociate subnets to the multicast domain and register or deregister group members or sources.

## Multicast traffic in multi-account environments architecture
<a name="mmulti-diagram1"></a>

![Architecture diagram showing multicast traffic across multiple AWS accounts using shared Transit Gateway multicast domains.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/multicast-transit-gateway/images/multicast-transit-gateway-2.png)


The following steps describe the data flow in this architecture:

1. All subnets in VPCs from both accounts associate to the multicast domain. Instances in **Account 1** VPCs use the **224.0.0.100** multicast group. Those instances use IGMP to dynamically join, leave, and send messages within the group.

1. Any multicast message sent by any instance in the group reaches all other members, using AWS Transit Gateway as the multicast router.

For cross-account communication:

1. The Amazon EC2 instance in **Account 2** VPC joins the multicast group **224.0.0.251** using a static source group membership configuration. It can only receive traffic in this mode.

1. An instance in **VPC B** sends multicast traffic to the **224.0.0.251** group using AWS Transit Gateway as the multicast router. If IGMPv2 is enabled for the domain, any Nitro instance can also send traffic.

For more information about using IGMP to join multicast groups, see [Automating service discovery using AWS Transit Gateway Multicast with IGMP](https://aws.amazon.com/blogs/networking-and-content-delivery/automating-service-discovery-using-aws-transit-gateway-multicast-with-igmp/).

## Further reading
<a name="mmulti-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="mmulti-diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](multicast-single-vpc.md#msvpc-diagram-history) | Reference architecture diagram first published. | May 5, 2022 | 
| [Initial publication](#mmulti-diagram-history) | Reference architecture diagram first published. | May 5, 2022 | 
| [Initial publication](multicast-external-integration.md#mext-diagram-history) | Reference architecture diagram first published. | May 5, 2022 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.