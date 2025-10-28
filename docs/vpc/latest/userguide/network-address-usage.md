# Network Address Usage for your VPC

Network Address Usage (NAU) is a metric applied to resources in your virtual network
to help you plan for and monitor the size of your VPC. Each NAU unit contributes to a
total that represents the size of your VPC.

It's important to understand the total number of units that make up the NAU of
your VPC because the following VPC quotas limit the size of a VPC:

- [Network Address Usage](amazon-vpc-limits.md#vpc-size-limits "amazon-vpc-limits.md#vpc-size-limits") –
  The maximum number of NAU units that a single VPC can have. Each VPC can have
  up to 64,000 NAU units by default. You can request a quota increase up to
  256,000.
- [Peered Network Address Usage](amazon-vpc-limits.md#vpc-size-limits "amazon-vpc-limits.md#vpc-size-limits") –
  The maximum number of NAU units for a VPC and all of its peered VPCs. If a
  VPC is peered with other VPCs in the same Region, the VPCs combined can have
  up to 128,000 NAU units by default. You can request a quota increase up to
  512,000. VPCs that are peered across different Regions do not contribute to
  this limit.
  You can use the NAU in the following ways:

- Before you create your virtual network, calculate the NAU units to help
  you decide if you should spread workloads across multiple VPCs.
- After you’ve created your VPC, use Amazon CloudWatch to monitor the NAU usage of
  the VPC so that it doesn't grow beyond the NAU quota limits. For more information,
  see [CloudWatch metrics for your VPCs](vpc-cloudwatch.md "vpc-cloudwatch.md").

## How NAU is calculated

If you understand how NAU is calculated, it can help you plan for the scaling
of your VPCs.

The following table explains which resources make up the NAU count in a VPC and
how many NAU units each resource uses. Some AWS resources are represented as
single NAU units and some resources are represented as multiple NAU units. You
can use the table to learn how NAU is calculated.

| Resource                                                                                                         | NAU units |
| ---------------------------------------------------------------------------------------------------------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Each private or public IPv4 and each IPv6 address assigned to a network interface for an EC2 instance in the VPC | 1         |
| Additional network interfaces attached to an EC2 instance                                                        | 1         |
| Prefix assigned to a network interface                                                                           | 1         |
| Network Load Balancer per AZ                                                                                     | 6         |
| Gateway Load Balancer per AZ                                                                                     | 6         |
| VPC endpoint per AZ                                                                                              | 6         |
| Transit gateway attachment                                                                                       | 6         |
| Lambda function                                                                                                  | 6         |
| NAT gateway                                                                                                      | 6         |
| EFS mount target                                                                                                 | 6         |
| EFA interface (EFA with an ENA device) or an EFA-only interface                                                  | 1         |
| Amazon EKS pod                                                                                                   | 1         | ## NAU examples The following examples show how to calculate NAU. ###### Example 1 - Two VPCs connected using VPC peering Peered VPCs in the same Region contribute to a combined NAU quota. <br>• VPC 1 + 50 Network Load Balancers in 2 subnets in separate Availability Zones - 600 NAU units + 5,000 instances (each with an IPv4 address and IPv6 address) in one subnet and 5,000 instances (each with an IPv4 address and IPv6 address) in another subnet - 20,000 units + 100 Lambda functions - 600 NAU units <br>• VPC 2 + 50 Network Load Balancers in 2 subnets in separate Availability Zones - 600 NAU units + 5,000 instances (each with an IPv4 address and IPv6 address) in one subnet and 5,000 instances (each with an IPv4 address and IPv6 address) in another subnet - 20,000 units + 100 Lambda functions - 600 NAU units <br>• Total peering NAU count: 42,400 units <br>• Default peering NAU quota: 128,000 units ###### Example 2 - Two VPCs connected using a transit gateway VPCs that are connected using a transit gateway do not contribute to a combined NAU quota as they do for peered VPCs. <br>• VPC 1 + 50 Network Load Balancers in 2 subnets in separate Availability Zones - 600 NAU units + 5,000 instances (each with an IPv4 address and IPv6 address) in one subnet and 5,000 instances (each with an IPv4 address and IPv6 address) in another subnet - 20,000 units + 100 Lambda functions - 600 NAU units <br>• VPC 2 + 50 Network Load Balancers in 2 subnets in separate Availability Zones - 600 NAU units + 5,000 instances (each with an IPv4 address and IPv6 address) in one subnet and 5,000 instances (each with an IPv4 address and IPv6 address) in another subnet - 20,000 units + 100 Lambda functions - 600 NAU units <br>• Total NAU count per VPC: 21,200 units <br>• Default NAU quota per VPC: 64,000 units |
