

# Restricted internet browsing prerequisites for Amazon WorkSpaces Secure Browser
<a name="restricted-prerequisites"></a>

Before you get started, make sure that you meet the following prerequisites:
+ You need an already deployed VPC, with public and private subnets spreading over several Availability Zones (AZs). For more information about how to set up your VPC environment, see [Default VPCs](https://docs.aws.amazon.com/vpc/latest/userguide/default-vpc.html).
+ You need one single proxy endpoint that is accessible from private subnets, where WorkSpaces Secure Browser sessions live (for example, the network load balancer DNS name). If you want to use your existing proxy, make sure it also has a single endpoint that is accessible from your private subnets.