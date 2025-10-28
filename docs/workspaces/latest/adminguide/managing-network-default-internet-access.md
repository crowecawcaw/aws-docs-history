# Configure a New or

Existing VPC with a Public Subnet

If you created your Amazon Web Services account after 2013-12-04, you have a [default VPC](default-vpc-with-public-subnet.md "default-vpc-with-public-subnet.md") in each AWS Region
that includes default public subnets. However, you may want to create your own
nondefault VPC or configure an existing VPC to use with your WorkSpaces Pool directory.
This topic describes how to configure a nondefault VPC and public subnet to use with
WorkSpaces Pools.

After you configure your VPC and public subnet, you can provide your WorkSpaces in
WorkSpaces Pools with access to the internet by enabling the **Default Internet
Access** option. When you enable this option, WorkSpaces Pools enables
internet connectivity by associating an [Elastic IP address](../../../AWSEC2/latest/WindowsGuide/elastic-ip-addresses-eip.md "../../../AWSEC2/latest/WindowsGuide/elastic-ip-addresses-eip.md")
to the network interface that is attached from the streaming instance to your public
subnet. An Elastic IP address is a public IPv4 address that is reachable from the
internet. For this reason, we recommend that you instead use a NAT gateway to
provide internet access to your WorkSpaces in WorkSpaces Pools. In addition, when
**Default Internet Access** is enabled, a maximum of 100 WorkSpaces
are supported. If your deployment must support more than 100 concurrent users, use
the [NAT gateway
configuration](managing-network-internet-NAT-gateway.md "managing-network-internet-NAT-gateway.md") instead.

For more information, see the steps in [Configure a VPC with Private
Subnets and a NAT Gateway](managing-network-internet-NAT-gateway.md "managing-network-internet-NAT-gateway.md"). For additional VPC
configuration recommendations, see [VPC Setup Recommendations for
WorkSpaces Pools](vpc-setup-recommendations.md "vpc-setup-recommendations.md").

###### Contents

- [Step 1: Configure a VPC with a Public
  Subnet](#vpc-with-public-subnet "#vpc-with-public-subnet")
- [Step 2: Enable
  Default Internet Access For Your WorkSpaces Pools](#managing-network-enable-default-internet-access "#managing-network-enable-default-internet-access")

## Step 1: Configure a VPC with a Public

Subnet

You can configure your own non-default VPC with a public subnet by using
either of the following methods:

- [Create a New VPC with a Single
  Public Subnet](#new-vpc-with-public-subnet "#new-vpc-with-public-subnet")
- [Configure an Existing
  VPC](#existing-vpc-with-public-subnet "#existing-vpc-with-public-subnet")

### Create a New VPC with a Single

Public Subnet

When you use the VPC wizard to create a new VPC, the wizard creates an
internet gateway and a custom route table that is associated with the public
subnet. The route table routes all traffic destined for an address outside
the VPC to the internet gateway. For more information about this
configuration, see [VPC with a
Single Public Subnet](../../../vpc/latest/userguide/VPC_Scenario1.md "../../../vpc/latest/userguide/VPC_Scenario1.md") in the _Amazon VPC User
Guide_.

1. Complete the steps in [Step 1: Create the VPC](../../../vpc/latest/userguide/getting-started-ipv4.md#getting-started-create-vpc "../../../vpc/latest/userguide/getting-started-ipv4.md#getting-started-create-vpc") in the _Amazon VPC User
   Guide_ to create your VPC.
2. To enable your WorkSpaces to access the internet, complete the steps in
   [Step 2: Enable
   Default Internet Access For Your WorkSpaces Pools](#managing-network-enable-default-internet-access "#managing-network-enable-default-internet-access").

### Configure an Existing

VPC

If you want to use an existing VPC that does not have a public subnet, you
can add a new public subnet. In addition to a public subnet, you must also
have an internet gateway attached to your VPC and a route table that routes
all traffic destined for an address outside the VPC to the internet gateway.
To configure these components, complete the following steps.

1. To add a public subnet, complete the steps in [Creating a Subnet in Your VPC](../../../vpc/latest/userguide/working-with-vpcs.md#AddaSubnet "../../../vpc/latest/userguide/working-with-vpcs.md#AddaSubnet"). Use the existing VPC
   that you plan to use with WorkSpaces Pools.

If your VPC is configured to support IPv6 addressing, the
**IPv6 CIDR block** list displays. Select
**Don't assign Ipv6**. 2. To create and attach an internet gateway to your VPC, complete the
steps in [Creating and Attaching an Internet Gateway](../../../vpc/latest/userguide/VPC_Internet_Gateway.md#Add_IGW_Attach_Gateway "../../../vpc/latest/userguide/VPC_Internet_Gateway.md#Add_IGW_Attach_Gateway"). 3. To configure your subnet to route internet traffic through the
internet gateway, complete the steps in [Creating a Custom Route Table](../../../vpc/latest/userguide/VPC_Internet_Gateway.md#Add_IGW_Routing "../../../vpc/latest/userguide/VPC_Internet_Gateway.md#Add_IGW_Routing"). In
step 5, for **Destination**, use IPv4 format
(`0.0.0.0/0`). 4. To enable your WorkSpaces and image builders to access the internet,
complete the steps in [Step 2: Enable
Default Internet Access For Your WorkSpaces Pools](#managing-network-enable-default-internet-access "#managing-network-enable-default-internet-access").

## Step 2: Enable

Default Internet Access For Your WorkSpaces Pools

You can enable internet access when you [create the
WorkSpaces Pool directory](create-directory-pools.md "create-directory-pools.md"). Choose the VPC with a public subnet when you
create the directory. Then select a public subnet for **Subnet
1** and, optionally, another public subnet for **Subnet
2**.

You can test your internet connectivity by starting your WorkSpaces Pool, and then
connecting to a WorkSpace in the pool and browsing to the internet.
