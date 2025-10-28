# Creating a new VPC for Amazon WorkSpaces Secure Browser

This section describes how to use the VPC wizard to create a VPC with one public
subnet and one private subnet. As part of this process, the wizard creates an internet
gateway and a NAT gateway. It also creates a custom route table associated with the public
subnet. It then updates the main route table associated with the private subnet. The NAT
gateway is automatically created in your VPC's public subnet.

After you use the wizard to create a VPC configuration, you'll add a second private
subnet. For more information about this configuration, see [VPC with public and private subnets
(NAT)](../../../vpc/latest/userguide/VPC_Scenario2.md "../../../vpc/latest/userguide/VPC_Scenario2.md").

###### Topics

- [Allocating an Elastic IP address](vpc-step1.md "vpc-step1.md")
- [Creating a new VPC](vpc-step2.md "vpc-step2.md")
- [Adding a second private subnet](vpc-step3.md "vpc-step3.md")
- [Verifying and naming your subnet route tables](vpc-step4.md "vpc-step4.md")
