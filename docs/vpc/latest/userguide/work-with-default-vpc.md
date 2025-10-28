# Work with your default VPC and default subnets

This section describes how to work with default VPCs and default subnets.

###### Contents

- [View your default VPC and default subnets](#view-default-vpc "#view-default-vpc")
- [Create a default VPC](#create-default-vpc "#create-default-vpc")
- [Create a default subnet](#create-default-subnet "#create-default-subnet")
- [Delete your default subnets and default VPC](#deleting-default-vpc "#deleting-default-vpc")

## View your default VPC and default subnets

You can view your default VPC and subnets using the Amazon VPC console or the command
line.

###### To view your default VPC and subnets using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Your VPCs**.
3. In the **Default VPC** column, look for a value of
   **Yes**. Take note of the ID of the default VPC.
4. In the navigation pane, choose **Subnets**.
5. In the search bar, type the ID of the default VPC. The returned subnets are
   subnets in your default VPC.
6. To verify which subnets are default subnets, look for a value of
   **Yes** in the **Default Subnet** column.

###### To describe your default VPC using the command line

- Use the [describe-vpcs](../../../cli/latest/reference/ec2/describe-vpcs.md "../../../cli/latest/reference/ec2/describe-vpcs.md")
  (AWS CLI)
- Use the [Get-EC2Vpc](../../../powershell/latest/reference/items/Get-EC2Vpc.md "../../../powershell/latest/reference/items/Get-EC2Vpc.md")
  (AWS Tools for Windows PowerShell)

Use the commands with the `isDefault` filter and set the filter value to
`true`.

###### To describe your default subnets using the command line

- Use the [describe-subnets](../../../cli/latest/reference/ec2/describe-subnets.md "../../../cli/latest/reference/ec2/describe-subnets.md") (AWS CLI)
- Use the [Get-EC2Subnet](../../../powershell/latest/reference/items/Get-EC2Subnet.md "../../../powershell/latest/reference/items/Get-EC2Subnet.md") (AWS Tools for Windows PowerShell)

Use the commands with the `vpc-id` filter and set the filter value to the ID
of the default VPC. In the output, the `DefaultForAz` field is set to
`true` for default subnets.

## Create a default VPC

If you delete your default VPC, you can create a new one. You cannot restore a previous
default VPC that you deleted, and you cannot mark an existing nondefault VPC as a
default VPC.

When you create a default VPC, it is created with the standard [components](default-vpc-components.md "default-vpc-components.md") of a default VPC, including a
default subnet in each Availability Zone. You cannot specify your own components. The
subnet CIDR blocks of your new default VPC may not map to the same Availability Zones as
your previous default VPC. For example, if the subnet with CIDR block
`172.31.0.0/20` was created in `us-east-2a` in your previous
default VPC, it may be created in `us-east-2b` in your new default
VPC.

If you already have a default VPC in the Region, you cannot create another one.

###### To create a default VPC using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Your VPCs**.
3. Choose **Actions**, **Create Default VPC**.
4. Choose **Create**. Close the confirmation screen.

###### To create a default VPC using the command line

You can use the [create-default-vpc](../../../cli/latest/reference/ec2/create-default-vpc.md "../../../cli/latest/reference/ec2/create-default-vpc.md") AWS CLI command. This command does not have any input
parameters.

```
aws ec2 create-default-vpc
```

The following is example output.

```
{
    "Vpc": {
        "VpcId": "vpc-3f139646",
        "InstanceTenancy": "default",
        "Tags": [],
        "Ipv6CidrBlockAssociationSet": [],
        "State": "pending",
        "DhcpOptionsId": "dopt-61079b07",
        "CidrBlock": "172.31.0.0/16",
        "IsDefault": true
    }
}
```

Alternatively, you can use the [New-EC2DefaultVpc](../../../powershell/latest/reference/items/New-EC2DefaultVpc.md "../../../powershell/latest/reference/items/New-EC2DefaultVpc.md") Tools for Windows PowerShell command or the [CreateDefaultVpc](../../../AWSEC2/latest/APIReference/API_CreateDefaultVpc.md "../../../AWSEC2/latest/APIReference/API_CreateDefaultVpc.md") Amazon EC2 API action.

## Create a default subnet

###### Note

You cannot create a default subnet using the AWS Management Console.

You can create a default subnet in an Availability Zone that does not have one. For
example, you might want to create a default subnet if you have deleted a default subnet,
or if AWS has added a new Availability Zone and did not automatically create a default
subnet for that zone in your default VPC.

When you create a default subnet, it is created with a size `/20` IPv4 CIDR
block in the next available contiguous space in your default VPC. The following rules
apply:

- You cannot specify the CIDR block yourself.
- You cannot restore a previous default subnet that you deleted.
- You can have only one default subnet per Availability Zone.
- You cannot create a default subnet in a nondefault VPC.

If there is not enough address space in your default VPC to create a size
`/20` CIDR block, the request fails. If you need more address space, you
can [add an IPv4 CIDR block to your VPC](vpc-cidr-blocks.md#vpc-resize "vpc-cidr-blocks.md#vpc-resize").

If you've associated an IPv6 CIDR block with your default VPC, the new default subnet
does not automatically receive an IPv6 CIDR block. Instead, you can associate an IPv6
CIDR block with the default subnet after you create it. For more information, see [Add or remove an IPv6 CIDR block from your subnet](subnet-associate-ipv6-cidr.md "subnet-associate-ipv6-cidr.md").

###### To create a default subnet using the AWS CLI

Use the [create-default-subnet](../../../cli/latest/reference/ec2/create-default-subnet.md "../../../cli/latest/reference/ec2/create-default-subnet.md") AWS CLI
command and specify the Availability Zone in which to create the subnet.

```
aws ec2 create-default-subnet --availability-zone us-east-2a
```

The following is example output.

```
{
    "Subnet": {
        "AvailabilityZone": "us-east-2a",
        "Tags": [],
        "AvailableIpAddressCount": 4091,
        "DefaultForAz": true,
        "Ipv6CidrBlockAssociationSet": [],
        "VpcId": "vpc-1a2b3c4d",
        "State": "available",
        "MapPublicIpOnLaunch": true,
        "SubnetId": "subnet-1122aabb",
        "CidrBlock": "172.31.32.0/20",
        "AssignIpv6AddressOnCreation": false
    }
}
```

For more information about setting up the AWS CLI, see the [AWS Command Line Interface User Guide](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md").

Alternatively, you can use the [New-EC2DefaultSubnet](../../../powershell/latest/reference/items/New-EC2DefaultSubnet.md "../../../powershell/latest/reference/items/New-EC2DefaultSubnet.md") Tools for Windows PowerShell command or the [CreateDefaultSubnet](../../../AWSEC2/latest/APIReference/API_CreateDefaultSubnet.md "../../../AWSEC2/latest/APIReference/API_CreateDefaultSubnet.md")
Amazon EC2 API action.

## Delete your default subnets and default VPC

You can delete a default subnet or default VPC just as you can delete any other subnet or
VPC. However, if you delete your default subnets or default VPC, you must explicitly
specify a subnet in one of your VPCs when you launch instances. If you do not have
another VPC, you must create a VPC with a subnet in at least one Availability Zone. For more
information, see [Create a VPC](create-vpc.md "create-vpc.md").

If you delete your default VPC, you can create a new one. For more information, see
[Create a default VPC](#create-default-vpc "#create-default-vpc").

If you delete a default subnet, you can create a new one. For more information, see [Create a default subnet](#create-default-subnet "#create-default-subnet"). To ensure
that your new default subnet behaves as expected, modify the subnet attribute to assign
public IP addresses to instances that are launched in that subnet. For more information,
see [Modify the IP addressing attributes of your subnet](subnet-public-ip.md "subnet-public-ip.md"). You can only
have one default subnet per Availability Zone. You cannot create a default subnet in a
nondefault VPC.
