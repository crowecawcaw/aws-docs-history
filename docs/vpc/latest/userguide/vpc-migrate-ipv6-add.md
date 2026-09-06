

# Add IPv6 support for your VPC
<a name="vpc-migrate-ipv6-add"></a>

The following table provides an overview of the process to enable IPv6 for your VPC.

**Topics**
+ [Step 1: Associate an IPv6 CIDR block with your VPC and subnets](#vpc-migrate-ipv6-cidr)
+ [Step 2: Update your route tables](#vpc-migrate-ipv6-routes)
+ [Step 3: Update your security group rules](#vpc-migrate-ipv6-sg-rules)
+ [Step 4: Assign IPv6 addresses to your instances](#vpc-migrate-assign-ipv6-address)


| Step | Notes | 
| --- | --- | 
| [Step 1: Associate an IPv6 CIDR block with your VPC and subnets](#vpc-migrate-ipv6-cidr) | Associate an Amazon-provided or BYOIP IPv6 CIDR block with your VPC and with your subnets. | 
| [Step 2: Update your route tables](#vpc-migrate-ipv6-routes) | Update your route tables to route your IPv6 traffic. For a public subnet, create a route that routes all IPv6 traffic from the subnet to the internet gateway. For a private subnet, create a route that routes all internet-bound IPv6 traffic from the subnet to an egress-only internet gateway. | 
| [Step 3: Update your security group rules](#vpc-migrate-ipv6-sg-rules) | Update your security group rules to include rules for IPv6 addresses. This enables IPv6 traffic to flow to and from your instances. If you've created custom network ACL rules to control the flow of traffic to and from your subnet, you must include rules for IPv6 traffic. | 
| [Step 4: Assign IPv6 addresses to your instances](#vpc-migrate-assign-ipv6-address) | Assign IPv6 addresses to your instances from the IPv6 address range of your subnet. | 

## Step 1: Associate an IPv6 CIDR block with your VPC and subnets
<a name="vpc-migrate-ipv6-cidr"></a>

You can associate an IPv6 CIDR block with your VPC, and then associate a `/64` CIDR block from that range with each subnet.

**To associate an IPv6 CIDR block with a VPC**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Your VPCs**.

1. Select your VPC.

1. Choose **Actions**, **Edit CIDRs** and then choose **Add new IPv6 CIDR**.

1. Select one of the following options, and then choose **Select CIDR**:
   + **Amazon-provided IPv6 CIDR block** – Use an IPv6 CIDR block from Amazon's pool of IPv6 addresses. For **Network Border Group**, choose the group from which AWS advertises IP addresses.
   + **IPAM-allocated IPv6 CIDR block** – Use an IPv6 CIDR block from an [IPAM pool](https://docs.aws.amazon.com/vpc/latest/ipam/how-it-works-ipam.html). Choose the IPAM pool and the IPv6 CIDR block.
   + **IPv6 CIDR owned by me** – Use an IPv6 CIDR block from your IPv6 address pool ([BYOIP](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-byoip.html)). Choose the IPv6 address pool and the IPv6 CIDR block.

1. Choose **Close**.

**To associate an IPv6 CIDR block with a subnet**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Subnets**.

1. Select a subnet.

1. Choose **Actions**, **Edit IPv6 CIDRs** and then choose **Add IPv6 CIDR**.

1. Edit the CIDR block as needed (for example, replace the `00`).

1. Choose **Save**.

1. Repeat this procedure for any other subnets in your VPC.

For more information, see [IPv6 VPC CIDR blocks](vpc-cidr-blocks.md#vpc-sizing-ipv6).

## Step 2: Update your route tables
<a name="vpc-migrate-ipv6-routes"></a>

When you associate an IPv6 CIDR block with your VPC, we automatically add a local route to each route table for the VPC to allow IPv6 traffic within the VPC.

You must update the route tables for your public subnets to enable instances (such as web servers) to use the internet gateway for IPv6 traffic. You must also update the route tables for your private subnets to enable instances (such as database instances) to use an egress-only internet gateway for IPv6 traffic, because NAT gateways do not support IPv6.

**To update the route table for a public subnet**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Subnets**. Select the public subnet. On the **Route table** tab, choose the route table ID to open the details page for the route table.

1. Select the route table. On the **Routes** tab, choose **Edit routes**.

1. Choose **Add route**. Choose `::/0` for **Destination**. Choose the ID of the internet gateway for **Target**.

1. Choose **Save changes**.

**To update the route table for a private subnet**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Egress-only internet gateways**. Choose **Create egress only internet gateway**. Choose your VPC from **VPC**, and then choose **Create egress only internet gateway**.

   For more information, see [Enable outbound IPv6 traffic using an egress-only internet gateway](egress-only-internet-gateway.md).

1. In the navigation pane, choose **Subnets**. Select the private subnet. On the **Route table** tab, choose the route table ID to open the details page for the route table.

1. Select the route table. On the **Routes** tab, choose **Edit routes**.

1. Choose **Add route**. Choose `::/0` for **Destination**. Choose the ID of the egress-only internet gateway for **Target**.

1. Choose **Save changes**.

**Note**  
A route table cannot have the same destination (::/0) pointing to both an internet gateway and an egress-only internet gateway simultaneously. If you receive an error message stating "There are existing ipv6 routes with next hop as internet Gateway" when configuring an egress-only internet gateway, you must first remove the existing IPv6 route to the internet gateway before adding the route to the egress-only internet gateway.

For more information, see [Example routing options](route-table-options.md).

## Step 3: Update your security group rules
<a name="vpc-migrate-ipv6-sg-rules"></a>

To enable your instances to send and receive traffic over IPv6, you must update your security group rules to include rules for IPv6 addresses. For example, in the example above, you can update the web server security group (`sg-11aa22bb11aa22bb1`) to add rules that allow inbound HTTP, HTTPS, and SSH access from IPv6 addresses. You don't need to make any changes to the inbound rules for your database security group; the rule that allows all communication from `sg-11aa22bb11aa22bb1` includes IPv6 communication.

**To update your inbound security group rules**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Security groups** and select your web server security group.

1. In the **Inbound rules** tab, choose **Edit inbound rules**.

1. For each rule that allows IPv4 traffic, choose **Add rule** and configure the rule to allow the corresponding IPv6 traffic. For example, to add a rule that allows all HTTP traffic over IPv6, choose **HTTP** for **Type** and `::/0` for **Source**.

1. When you are finished adding rules, choose **Save rules**.

**Update your outbound security group rules**  
When you associate an IPv6 CIDR block with your VPC, we automatically add an outbound rule to the security groups for the VPC that allows all IPv6 traffic. However, if you modified the original outbound rules for your security group, this rule is not automatically added, and you must add equivalent outbound rules for IPv6 traffic.
<a name="vpc-migrate-ipv6-nacl-rules"></a>
**Update your network ACL rules**  
When you associate an IPv6 CIDR block with a VPC, we automatically add rules to the default network ACL to allow IPv6 traffic. However, if you modified your default network ACL or if you've created a custom network ACL, you must manually add rules for IPv6 traffic. For more information, see [Add and delete rules](create-network-acl.md#Rules).

## Step 4: Assign IPv6 addresses to your instances
<a name="vpc-migrate-assign-ipv6-address"></a>

All current generation instance types support IPv6. If your instance type does not support IPv6, you must resize the instance to a supported instance type before you can assign an IPv6 address. The process that you'll use depends on whether the new instance type that you choose is compatible with the current instance type. For more information, see [Change the instance type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-resize.html) in the *Amazon EC2 User Guide*. If you must launch an instance from a new AMI to support IPv6, you can assign an IPv6 address to your instance during launch.

After you've verified that your instance type supports IPv6, you can assign an IPv6 address to your instance using the Amazon EC2 console. The IPv6 address is assigned to the primary network interface (for example, eth0) for the instance. For more information, see [Assign an IPv6 address to an instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-instance-addressing.html#assign-ipv6-address) in the *Amazon EC2 User Guide*.

You can connect to an instance using its IPv6 address. For more information, see [Connect to your Linux instance using an SSH client](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-linux-inst-ssh.html#connect-linux-inst-sshClient) in the *Amazon EC2 User Guide*.

If you launched your instance using an AMI for a current version of your operating system, your instance is configured for IPv6. If you can't ping an IPv6 address from your instance, refer to the documentation for your operating system to configure IPv6.