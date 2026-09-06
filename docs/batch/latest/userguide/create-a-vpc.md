

# Create a VPC
<a name="create-a-vpc"></a>

With Amazon Virtual Private Cloud (Amazon VPC), you can launch AWS resources into a virtual network that you've defined. We strongly recommend that you launch your container instances in a VPC. 

If you have a default VPC, you also can skip this section and move to the next task [Create a security group](create-a-base-security-group.md). To determine whether you have a default VPC, see [Supported Platforms in the Amazon EC2 Console](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-supported-platforms.html#console-updates) in the *Amazon EC2 User Guide*

For information about how to create an Amazon VPC, see [Create a VPC only](https://docs.aws.amazon.com/vpc/latest/userguide/working-with-vpcs.html#create-vpc-vpc-only) in the *Amazon VPC User Guide*. Refer to the following table to determine what options to select.


| Option | Value | 
| --- | --- | 
| Resources to create | VPC only | 
| Name | Optionally provide a name for your VPC. | 
| IPv4 CIDR block | IPv4 CIDR manual input<br />The CIDR block size must have a size between /16 and /28. | 
| IPv6 CIDR block | No IPv6 CIDR block | 
| Tenancy | Default | 

For more information about Amazon VPC, see [What is Amazon VPC?](https://docs.aws.amazon.com/vpc/latest/userguide/) in the *Amazon VPC User Guide*.