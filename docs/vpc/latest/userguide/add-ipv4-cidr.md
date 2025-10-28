# Add or remove a CIDR block from your VPC

This section describes how to add or remove IPv4 and IPv6 CIDR blocks from a VPC.

###### Important

- Your VPC can have up to five IPv4 and five IPv6 CIDR blocks by default,
  but this limit is adjustable. For more information, see [Amazon VPC quotas](amazon-vpc-limits.md "amazon-vpc-limits.md"). For
  information about restrictions on CIDR blocks for a VPC, see [VPC CIDR blocks](vpc-cidr-blocks.md "vpc-cidr-blocks.md").
- If your VPC has more than one IPv4 CIDR block associated with it, you can
  remove an IPv4 CIDR block from the VPC. You cannot remove the primary IPv4
  CIDR block. You must remove an entire CIDR block; you cannot remove a subset
  of a CIDR block or a merged range of CIDR blocks. You must first delete all
  subnets in the CIDR block.
- If you no longer want IPv6 support in your VPC, but you want to continue
  using your VPC to create and communicate with IPv4 resources, you can remove
  the IPv6 CIDR block.
- To remove an IPv6 CIDR block, you must first unassign any IPv6 addresses
  that are assigned to any instances in your subnet.
- Removing an IPv6 CIDR block does not automatically delete any security
  group rules, network ACL rules, or route table routes that you've configured
  for IPv6 networking. You must manually modify or delete these rules or
  routes.

###### To add or remove a CIDR block from a VPC using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Your VPCs**.
3. Select the VPC, and then choose **Actions**, **Edit
   CIDRs**.
4. To remove a CIDR, choose **Remove** next to the CIDR.
5. To add a CIDR, choose **Add new IPv4 CIDR** or **Add new IPv6
   CIDR**.
6. To add a CIDR for **IPv4 CIDR block**, do one of the following:
   - Choose **IPv4 CIDR manual input** and enter an IPv4
     CIDR block.
   - Choose **IPAM-allocated IPv4 CIDR** and select a CIDR
     from an IPv4 IPAM pool.
   - Choose **Save**.

7. To add a CIDR for **IPv6 CIDR block**, do the following:
   - Choose **IPAM-allocated IPv6 CIDR block** if you are using Amazon VPC IP Address Manager and you want to provision a IPv6 CIDR from an IPAM pool. You have two options for provisioning an IP address
     range to the VPC under **CIDR block**:
     - **Netmask length**: Choose this option to select a netmask length for
       the CIDR. Do one of the following:
       - If there is a default netmask length selected for the IPAM pool, you can choose
         **Default to IPAM netmask length** to use
         the default netmask length set for the IPAM pool by the IPAM
         administrator. For more information about the optional default
         netmask length allocation rule, see [Create a
         Regional IPv6 pool](../ipam/create-ipv6-reg-pool.md "../ipam/create-ipv6-reg-pool.md") in the
         _Amazon VPC IPAM User Guide_.
       - If there is no default netmask length selected for the IPAM pool, choose a netmask length
         that's more specific than the netmask length of the IPAM
         pool CIDR. For example, if the IPAM pool CIDR is /50,
         you can choose a netmask length between
         **/52** to **/60**
         for the VPC. Possible netmask lengths are between
         **/44** and
         **/60** in increments of /4.

     - **Select a CIDR**: Choose this option to manually enter an IPv6 address. You
       can only choose a netmask length that's more specific than the
       netmask length of the IPAM pool CIDR. For example, if the IPAM
       pool CIDR is /50, you can choose a netmask length between
       **/52** to **/60** for the
       VPC. Possible IPv6 netmask lengths are between
       **/44** and **/60** in
       increments of /4.

   - Choose **Amazon-provided IPv6 CIDR block** to
     request an IPv6 CIDR block from an Amazon pool of IPv6 addresses.
     For **Network Border Group**, select the group
     from which AWS advertises IP addresses. Amazon provides a fixed
     IPv6 CIDR block size of **/56**.
   - Choose **IPv6 CIDR owned by me** to provision an IPv6 CIDR that you have
     already brought to AWS. For more information, see [Bring your own IP addresses
     (BYOIP) to Amazon EC2](../../../AWSEC2/latest/UserGuide/ec2-byoip.md "../../../AWSEC2/latest/UserGuide/ec2-byoip.md") in the _Amazon EC2 User Guide_.
     You have two options for provisioning an IP address range to the VPC under
     **CIDR block**:
     - **No preference**: Choose this option to use netmask length of
       **/56**.
     - **Select a CIDR**: Choose this option to manually enter an IPv6
       address and choose a netmask length that's more specific than
       the size of BYOIP CIDR. For example, if the BYOIP pool CIDR is
       /50, you can choose a netmask length between
       **/52** to **/60** for the
       VPC. Possible IPv6 netmask lengths are between
       **/44** and **/60** in
       increments of /4.
     - Choose **Select CIDR** when you're done.

8. Choose **Close**.
9. If you've added a CIDR block to your VPC, you can create subnets that use the new CIDR
   block. For more information, see [Create a subnet](create-subnets.md "create-subnets.md").

###### To associate or disassociate a CIDR block from a VPC using the AWS CLI

Use the [associate-vpc-cidr-block](../../../cli/latest/reference/ec2/associate-vpc-cidr-block.md "../../../cli/latest/reference/ec2/associate-vpc-cidr-block.md") and [disassociate-vpc-cidr-block](../../../cli/latest/reference/ec2/disassociate-vpc-cidr-block.md "../../../cli/latest/reference/ec2/disassociate-vpc-cidr-block.md") commands.
