

# Example: Manage IGMP configurations using AWS Transit Gateway
<a name="multicast-configurations-igmp"></a>

This example shows at least one host that uses the IGMP protocol for multicast traffic. AWS automatically creates the multicast group when it receives an IGMP `JOIN` message from an instance, and then adds the instance as a member in this group. You can also statically add non-IGMP hosts as members to a group using the AWS CLI. Any instances that are in subnets associated with the multicast domain can send traffic, and the group members receive the multicast traffic.

 Use the following steps to complete the configuration:

1. Create a VPC. For more information, see [Create a VPC](https://docs.aws.amazon.com/vpc/latest/userguide/create-vpc.html) in the *Amazon VPC User Guide*.

1. Create a subnet in the VPC. For more information, see [Create a subnet](https://docs.aws.amazon.com/vpc/latest/userguide/create-subnets.html) in the *Amazon VPC User Guide*.

1. Create a transit gateway configured for multicast traffic. For more information, see [Create a transit gateway in AWS Transit Gateway](create-tgw.md).

1. Create a VPC attachment. For more information, see [Create a VPC attachment in AWS Transit Gateway](create-vpc-attachment.md).

1. Create a multicast domain configured for IGMP support. For more information, see [Create an IGMP multicast domain in AWS Transit Gateway](create-tgw-igmp-domain.md). 

   Use the following settings:
   + Enable **IGMPv2 support**.
   + Disable **Static sources support**.

1. Create an association between subnets in the transit gateway VPC attachment and the multicast domain. For more information see [Associating VPC attachments and subnets with a multicast domain in AWS Transit Gateway](associate-attachment-to-domain.md). 

1. The default IGMP version for EC2 is IGMPv3. You need to change the version for all IGMP group members. You can run the following command:

   ```
   sudo sysctl net.ipv4.conf.eth0.force_igmp_version=2
   ```

1. Add the members that do not use the IGMP protocol to the multicast group. For more information, see [Register members with a multicast group in AWS Transit Gateway](add-members-multicast-group.md).