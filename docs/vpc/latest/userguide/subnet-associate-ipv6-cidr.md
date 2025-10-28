# Add or remove an IPv6 CIDR block from your subnet

You can associate an IPv6 CIDR block with an existing subnet in your VPC. The
subnet must not have an existing IPv6 CIDR block associated with it.

If you no longer want IPv6 support in your subnet, but you want to continue
to use your subnet to create and communicate with IPv4 resources, you can
remove the IPv6 CIDR block.

Before you can remove an IPv6 CIDR block, you must first unassign any IPv6 addresses
that are assigned to any instances in your subnet.

###### To add or remove an IPv6 CIDR block to a subnet

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Subnets**.
3. Select your subnet and choose **Actions**,
   **Edit IPv6 CIDRs**.
4. To add a CIDR, choose **Add IPv6 CIDR**, choose a **VPC CIDR block**, enter a **Subnet CIDR
   block**, and choose a netmask length that's equal to or more
   specific than the netmask length of the VPC CIDR. For example, if the VPC pool
   CIDR is /50, you can choose a netmask length between **/50** to
   **/64** for the subnet. Possible IPv6 netmask lengths are
   between **/44** and **/64** in increments of
   /4.
5. To remove a CIDR, find the IPv6 CIDR block and choose **Remove**.
6. Choose **Save**.

###### To associate an IPv6 CIDR block with a subnet using the AWS CLI

Use the [associate-subnet-cidr-block](../../../cli/latest/reference/ec2/associate-subnet-cidr-block.md "../../../cli/latest/reference/ec2/associate-subnet-cidr-block.md") command.

###### To disassociate an IPv6 CIDR block from a subnet using the AWS CLI

Use the [disassociate-subnet-cidr-block](../../../cli/latest/reference/ec2/disassociate-subnet-cidr-block.md "../../../cli/latest/reference/ec2/disassociate-subnet-cidr-block.md") command.
