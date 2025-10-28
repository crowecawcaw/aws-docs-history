# Create a VPC

With Amazon Virtual Private Cloud (Amazon VPC), you can launch AWS resources into a virtual network that you've defined. We strongly
recommend that you launch your container instances in a VPC.

If you have a default VPC, you also can skip this section and move to the next task [Create a security group](create-a-base-security-group.md "create-a-base-security-group.md"). To determine whether you have
a default VPC, see [Supported Platforms in the
Amazon EC2 Console](../../../AWSEC2/latest/UserGuide/ec2-supported-platforms.md#console-updates "../../../AWSEC2/latest/UserGuide/ec2-supported-platforms.md#console-updates") in the _Amazon EC2 User Guide_

For information about how to create an Amazon VPC, see [Create a VPC only](../../../vpc/latest/userguide/working-with-vpcs.md#create-vpc-vpc-only "../../../vpc/latest/userguide/working-with-vpcs.md#create-vpc-vpc-only") in the _Amazon VPC User Guide_. Refer to the following table to determine what options to select.

| Option              | Value                                                                            |
| ------------------- | -------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Resources to create | VPC only                                                                         |
| Name                | Optionally provide a name for your VPC.                                          |
| IPv4 CIDR block     | IPv4 CIDR manual input The CIDR block size must have a size between /16 and /28. |
| IPv6 CIDR block     | No IPv6 CIDR block                                                               |
| Tenancy             | Default                                                                          | For more information about Amazon VPC, see [What is Amazon VPC?](../../../vpc/latest/userguide.md "../../../vpc/latest/userguide.md") in the _Amazon VPC User Guide_. |
