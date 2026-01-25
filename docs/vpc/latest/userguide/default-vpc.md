# Default VPCs

When you start using Amazon VPC, you have a default VPC
in each AWS Region. A default VPC comes with a public subnet in each Availability Zone, an
internet gateway, and settings to enable DNS resolution. Therefore, you can immediately
start launching Amazon EC2 instances into a default VPC. You can also use services such as
Elastic Load Balancing, Amazon RDS, and Amazon EMR in your default VPC.

A default VPC is suitable for getting started quickly and for launching public instances
such as a blog or simple website. You can modify the components of your default VPC as
needed.

You can add subnets to your default VPC. For more information, see [Create a subnet](create-subnets.md "create-subnets.md").

###### Contents

- [Default VPC components](default-vpc-components.md "default-vpc-components.md")
- [Default subnets](default-subnet.md "default-subnet.md")
- [Work with your default VPC and default subnets](work-with-default-vpc.md "work-with-default-vpc.md")
