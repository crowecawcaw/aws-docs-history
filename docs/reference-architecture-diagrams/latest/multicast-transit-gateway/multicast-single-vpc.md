

# Multicast Traffic in a Single VPC
<a name="multicast-single-vpc"></a>

Publication date: **May 5, 2022 ([Diagram history](#msvpc-diagram-history))**

This architecture uses [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) with multicast enabled to build multicast applications in a single Amazon VPC. You achieve segmentation by creating [multicast domains](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-multicast-overview.html) that define which subnets participate in multicast communication.

## Multicast traffic in a single VPC architecture
<a name="msvpc-diagram1"></a>

![Architecture diagram showing multicast traffic in a single VPC using AWS Transit Gateway with multicast domains and groups.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/multicast-transit-gateway/images/multicast-transit-gateway-1.png)


The following steps describe the configuration and data flow in this architecture:

1. A multicast domain defines the subnets that participate in multicast communication. Multicast association (domain membership) operates at the subnet level, and a single subnet can only associate with one multicast domain.

1. A multicast group defines the hosts that send or receive the same multicast traffic. You define multiple groups within the same multicast domain. A group IP address identifies each group, and individual ENIs define membership.

The following steps describe the data flow:

1. An ENI associated with a supported Amazon EC2 instance receives multicast traffic by being a multicast group member. Nitro instances can send and receive traffic in a static source group membership configuration. With IGMPv2 enabled, any Nitro instance can send traffic without static configuration.

1. An Amazon EC2 instance in Availability Zone B sends a multicast packet using the multicast group IP address 224.0.0.100.

1. The packet arrives at AWS Transit Gateway, which redirects it to the other instances in the same group located in Availability Zone A.

For more information about multicast on AWS Transit Gateway, see [Multicast on transit gateways](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-multicast-overview.html).

For more information about Nitro instances, see [Instances built on the Nitro System](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html).

## Further reading
<a name="msvpc-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="msvpc-diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#msvpc-diagram-history) | Reference architecture diagram first published. | May 5, 2022 | 
| [Initial publication](multicast-multi-account.md#mmulti-diagram-history) | Reference architecture diagram first published. | May 5, 2022 | 
| [Initial publication](multicast-external-integration.md#mext-diagram-history) | Reference architecture diagram first published. | May 5, 2022 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.