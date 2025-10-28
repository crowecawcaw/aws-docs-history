# Create a subnet

Use the following procedure to create subnets for your virtual private cloud (VPC).
Depending on the connectivity that you need, you might also need to add gateways and
route tables.

###### Considerations

- You must specify an IPv4 CIDR block for the subnet from the range of your VPC.
  You can optionally specify an IPv6 CIDR block for a subnet if there is an
  IPv6 CIDR block associated with the VPC. For more information, see
  [IP addressing for your VPCs and subnets](vpc-ip-addressing.md "vpc-ip-addressing.md").
- If you create an IPv6-only subnet, be aware of the following. An EC2 instance
  launched in an IPv6-only subnet receives an IPv6 address but not an IPv4 address.
  Any instances that you launch into an IPv6-only subnet must be [instances built
  on the Nitro System](../../../ec2/latest/instancetypes/ec2-nitro-instances.md "../../../ec2/latest/instancetypes/ec2-nitro-instances.md").
- To create the subnet in a Local Zone or a Wavelength Zone, you must enable the
  Zone. For more information, see [Regions and Zones](../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md "../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md") in the _Amazon EC2 User Guide_.

###### To add a subnet to your VPC

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Subnets**.
3. Choose **Create subnet**.
4. Under **VPC ID**, choose the VPC for the subnet.
5. (Optional) For **Subnet name**, enter a name for
   your subnet. Doing so creates a tag with a key of `Name`
   and the value that you specify.
6. For **Availability Zone**, you can choose a Zone
   for your subnet, or leave the default **No Preference**
   to let AWS choose one for you.
7. For **IPv4 CIDR block**, select **Manual input** to enter
   an IPv4 CIDR block for your subnet (for example, `10.0.1.0/24`) or select
   **No IPv4 CIDR**. If you are using Amazon VPC IP Address Manager (IPAM) to
   plan, track, and monitor IP addresses for your AWS workloads, when you create a
   subnet you have the option to allocate a CIDR block from IPAM
   (**IPAM-allocated**). For more information on planning VPC IP
   address space for subnet IP allocations, see [Tutorial: Plan VPC IP
   address space for subnet IP allocations](../ipam/tutorials-subnet-planning.md "../ipam/tutorials-subnet-planning.md") in the
   _Amazon VPC IPAM User Guide_.
8. For **IPv6 CIDR block**, select **Manual input** to
   choose the VPC's IPv6 CIDR that you want to create a subnet in. This option is
   available only if the VPC has an associated IPv6 CIDR block. If you are using
   Amazon VPC IP Address Manager (IPAM) to plan, track, and monitor IP addresses for your AWS
   workloads, when you create a subnet you have the option to allocate a CIDR block
   from IPAM (**IPAM-allocated**). For more information on planning
   VPC IP address space for subnet IP allocations, see [Tutorial: Plan VPC IP
   address space for subnet IP allocations](../ipam/tutorials-subnet-planning.md "../ipam/tutorials-subnet-planning.md") in the
   _Amazon VPC IPAM User Guide_.
9. Choose an **IPv6 VPC CIDR block**.
10. For **IPv6 subnet CIDR block**, choose a CIDR for the subnet that's equal to
    or more specific than the VPC CIDR. For example, if the VPC pool CIDR is /50, you
    can choose a netmask length between **/50** to
    **/64** for the subnet. Possible IPv6 netmask lengths are
    between **/44** and **/64** in increments of
    /4.
11. Choose **Create subnet**.

###### To add a subnet to your VPC using the AWS CLI

Use the [create-subnet](../../../cli/latest/reference/ec2/create-subnet.md "../../../cli/latest/reference/ec2/create-subnet.md")
command.

###### Next steps

After you create a subnet, you can configure it as follows:

- Configure routing. You can then create a custom route table and route
  that send traffic to a gateway that's associated with the VPC, such as
  an internet gateway. For more information, see [Configure route tables](VPC_Route_Tables.md "VPC_Route_Tables.md").
- Modify the IP addressing behavior. You can specify whether instances launched
  in the subnet receive a public IPv4 address, an IPv6 address, or both.
  For more information, see [Modify the IP addressing attributes of your subnet](subnet-public-ip.md "subnet-public-ip.md").
- Modify the resource-based name (RBN) settings. For more information, see
  [Amazon EC2 instance hostname types](../../../AWSEC2/latest/UserGuide/ec2-instance-naming.md#instance-naming-modify-instances "../../../AWSEC2/latest/UserGuide/ec2-instance-naming.md#instance-naming-modify-instances").
- Create or modify your network ACLs. For more information,
  see [Control subnet traffic with network access control lists](vpc-network-acls.md "vpc-network-acls.md").
- Share the subnet with other accounts. For more information, see [Share a subnet](vpc-sharing-share-subnet-working-with.md#vpc-sharing-share-subnet "vpc-sharing-share-subnet-working-with.md#vpc-sharing-share-subnet").
