

# Example: Manage static group member configurations in AWS Transit Gateway
<a name="multicast-configurations-no-igmp-source"></a>

This example shows statically adding multicast members to a group. Hosts cannot use the IGMP protocol to join or leave multicast groups. Any instances that are in subnets associated with the multicast domain can send multicast traffic, and the group members receive the multicast traffic.

 Use the following steps to complete the configuration:

1. Create a VPC. For more information, see [Create a VPC](https://docs.aws.amazon.com/vpc/latest/userguide/create-vpc.html) in the *Amazon VPC User Guide*.

1. Create a subnet in the VPC. For more information, see [Create a subnet](https://docs.aws.amazon.com/vpc/latest/userguide/create-subnets.html) in the *Amazon VPC User Guide*.

1. Create a transit gateway configured for multicast traffic. For more information, see [Create a transit gateway in AWS Transit Gateway](create-tgw.md).

1. Create a VPC attachment. For more information, see [Create a VPC attachment in AWS Transit Gateway](create-vpc-attachment.md).

1. Create a multicast domain configured for no IGMP support, and support for statically adding sources. For more information, see [Create a static source multicast domain in AWS Transit Gateway](create-tgw-domain.md). 

   Use the following settings:
   + Disable **IGMPv2 support**.
   + Disable **Static sources support**.

1. Create an association between subnets in the transit gateway VPC attachment and the multicast domain. For more information see [Associating VPC attachments and subnets with a multicast domain in AWS Transit Gateway](associate-attachment-to-domain.md).

1. Add the members to the multicast group. For more information, see [Register members with a multicast group in AWS Transit Gateway](add-members-multicast-group.md).