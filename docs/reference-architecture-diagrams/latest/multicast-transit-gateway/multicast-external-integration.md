

# Integrating External Multicast Services and AWS
<a name="multicast-external-integration"></a>

Publication date: **May 5, 2022 ([Diagram history](#mext-diagram-history))**

This architecture integrates external multicast services with AWS by deploying third-party multicast-routing-capable appliances in an [Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html). It uses [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) with multicast enabled and GRE tunnels to deliver multicast packets between AWS and the corporate data center.

## Integrating external multicast services architecture
<a name="mext-diagram1"></a>

![Architecture diagram showing integration of external multicast services with AWS using Transit Gateway and GRE tunnels to on-premises multicast routers.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/multicast-transit-gateway/images/multicast-transit-gateway-3.png)


The following steps describe the data flow in this architecture:

1. The multicast source sends traffic to a multicast group through its ENI.

1. AWS Transit Gateway with the multicast domain configuration and registered source and members forwards the packet to the virtual router.

1. The virtual router deployed in the Amazon VPC receives the multicast packets.

1. The virtual routers deliver the multicast packets between network segments using Protocol Independent Multicast (PIM). The packets forward through a Generic Routing Encapsulation (GRE) tunnel between the virtual routers in AWS and the multicast router in the corporate data center.

1. The on-premises router receives packets through the tunnel and decapsulates them.

1. Decapsulated packets send over the downstream multicast interface to the receivers.

For more information about integrating external multicast services with AWS, see [Integrating external multicast services with AWS](https://aws.amazon.com/blogs/networking-and-content-delivery/integrating-external-multicast-services-with-aws/).

## Further reading
<a name="mext-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="mext-diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](multicast-single-vpc.md#msvpc-diagram-history) | Reference architecture diagram first published. | May 5, 2022 | 
| [Initial publication](multicast-multi-account.md#mmulti-diagram-history) | Reference architecture diagram first published. | May 5, 2022 | 
| [Initial publication](#mext-diagram-history) | Reference architecture diagram first published. | May 5, 2022 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.