# Example: Manage IGMP configurations using

AWS Transit Gateway

This example shows at least one host that uses the IGMP protocol for multicast traffic.
AWS automatically creates the multicast group when it receives an IGMP `JOIN`
message from an instance, and then adds the instance as a member in this group. You can also
statically add non-IGMP hosts as members to a group using the AWS CLI. Any instances that are in
subnets associated with the multicast domain can send traffic, and the group members receive the
multicast traffic.

Use the following steps to complete the configuration:

1. Create a VPC. For more information, see [Create a VPC](../userguide/create-vpc.md "../userguide/create-vpc.md")
   in the _Amazon VPC User Guide_.
2. Create a subnet in the VPC. For more information, see
   [Create a subnet](../userguide/create-subnets.md "../userguide/create-subnets.md")
   in the _Amazon VPC User Guide_.
3. Create a transit gateway configured for multicast traffic. For more information, see
   [Create a transit gateway in AWS Transit Gateway](create-tgw.md "create-tgw.md").
4. Create a VPC attachment. For more information, see [Create a VPC attachment in AWS Transit Gateway](create-vpc-attachment.md "create-vpc-attachment.md").
5. Create a multicast domain configured for IGMP support. For more information,
   see [Create an IGMP multicast domain in AWS Transit Gateway](create-tgw-igmp-domain.md "create-tgw-igmp-domain.md").

Use the following settings:

    * Enable **IGMPv2 support**.
    * Disable **Static sources support**.

6. Create an association between subnets in the transit gateway VPC attachment and the multicast
   domain. For more information see [Associating VPC attachments and subnets with
   a multicast domain in AWS Transit Gateway](associate-attachment-to-domain.md "associate-attachment-to-domain.md").
7. The default IGMP version for EC2 is IGMPv3. You need to change the version for all
   IGMP group members. You can run the following command:

```
sudo sysctl net.ipv4.conf.eth0.force_igmp_version=2
```

8. Add the members that do not use the IGMP protocol to the multicast group. For more
   information, see [Register members with a multicast
   group in AWS Transit Gateway](add-members-multicast-group.md "add-members-multicast-group.md").
