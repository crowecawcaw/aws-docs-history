# NAT instances

A NAT instance provides network address translation (NAT). You can use a NAT instance to allow
resources in a private subnet to communicate with destinations outside the virtual private cloud (VPC),
such as the internet or an on-premises network. The resources in the private subnet can initiate
outbound IPv4 traffic to the internet, but they can't receive inbound traffic initiated on the internet.

###### Important

NAT AMI is built on the last version of the Amazon Linux AMI, 2018.03, which reached the end of
standard support on December 31, 2020 and end of maintenance support on December 31, 2023. For
more information, see the following blog post: [Amazon Linux AMI end of
life](https://aws.amazon.com/blogs/aws/update-on-amazon-linux-ami-end-of-life/ "https://aws.amazon.com/blogs/aws/update-on-amazon-linux-ami-end-of-life/").

If you use an existing NAT AMI, AWS recommends that you [migrate to a NAT gateway](vpc-nat-comparison.md#nat-instance-migrate "vpc-nat-comparison.md#nat-instance-migrate"). NAT gateways provide better availability, higher bandwidth,
and requires less administrative effort. For more information, see [Compare NAT gateways and NAT instances](vpc-nat-comparison.md "vpc-nat-comparison.md").

If NAT instances are a better match for your use case than NAT gateways, you can create
your own NAT AMI from a current version of Amazon Linux as described in [3. Create a NAT AMI](work-with-nat-instances.md#create-nat-ami "work-with-nat-instances.md#create-nat-ami").

###### Contents

- [NAT instance basics](#basics "#basics")
- [Enable private resources to communicate outside the VPC](work-with-nat-instances.md "work-with-nat-instances.md")

## NAT instance basics

The following figure illustrates the NAT instance basics. The route table associated with
the private subnet sends internet traffic from the instances in the private subnet to the NAT
instance in the public subnet. The NAT instance then sends the traffic to the internet
gateway. The traffic is attributed to the public IP address of the NAT instance. The NAT
instance specifies a high port number for the response; if a response comes back, the NAT
instance sends it to an instance in the private subnet based on the port number for the
response.

The NAT instance must have internet access, so it must be in a public subnet (a subnet
that has a route table with a route to the internet gateway), and it must have a public IP
address or an Elastic IP address.

![Diagram showing the setup of a NAT instance in a VPC](images/nat-instance_updated.png)

To get started with NAT instances, create a NAT AMI, create a security group for the
NAT instance, and launch the NAT instance into your VPC.

Your NAT instance quota depends on your instance quota for the Region. For more information,
see [Amazon EC2 service quotas](../../../general/latest/gr/ec2-service.md#limits_ec2 "../../../general/latest/gr/ec2-service.md#limits_ec2") in the
_AWS General Reference_.
