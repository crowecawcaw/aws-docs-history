# Example: Manage static source

configurations in AWS Transit Gateway

This example statically adds multicast sources to a group. Hosts do not use the IGMP
protocol to join or leave multicast groups. You need to statically add the group members that
receive the multicast traffic.

Use the following steps to complete the configuration:

1. Create a VPC. For more information, see [Create a VPC](../userguide/create-vpc.md "../userguide/create-vpc.md")
   in the _Amazon VPC User Guide_.
2. Create a subnet in the VPC. For more information, see
   [Create a subnet](../userguide/create-subnets.md "../userguide/create-subnets.md")
   in the _Amazon VPC User Guide_.
3. Create a transit gateway configured for multicast traffic. For more information, see
   [Create a transit gateway in AWS Transit Gateway](create-tgw.md "create-tgw.md").
4. Create a VPC attachment. For more information, see [Create a VPC attachment in AWS Transit Gateway](create-vpc-attachment.md "create-vpc-attachment.md").
5. Create a multicast domain configured for no IGMP support, and support for statically
   adding sources. For more information, see [Create a static source multicast domain in AWS Transit Gateway](create-tgw-domain.md "create-tgw-domain.md").

Use the following settings:

    * Disable **IGMPv2 support**.
    * To manually add sources, enable **Static sources
     support**.


    The sources are the only resources that can send multicast traffic when the
     attribute is enabled. Otherwise, any instances that are in subnets associated with the
     multicast domain can send multicast traffic, and the group members receive the
     multicast traffic.

6. Create an association between subnets in the transit gateway VPC attachment and the
   multicast domain. For more information see [Associating VPC attachments and subnets with
   a multicast domain in AWS Transit Gateway](associate-attachment-to-domain.md "associate-attachment-to-domain.md").
7. If you enable **Static sources support**, add the source to the
   multicast group. For more information, see [Register sources with a multicast
   group in AWS Transit Gateway](add-source-multicast-group.md "add-source-multicast-group.md").
8. Add the members to the multicast group. For more information, see [Register members with a multicast
   group in AWS Transit Gateway](add-members-multicast-group.md "add-members-multicast-group.md").
