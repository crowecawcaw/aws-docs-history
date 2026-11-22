

# Plan your network

Amazon Elastic VMware Service deploys your environment into a VPC that you provide, and creates the VLAN subnets for VMware Cloud Foundation (VCF) in that VPC. You can’t change the VPC CIDR block, add VLAN subnets, or change the VLAN subnet CIDR blocks after you create the environment. Make the following decisions before you create the environment, in this order.

1. Size the VPC CIDR block, the service access subnet, and the 10 VLAN subnets. For more information, see [Plan your VPC and VLAN subnets](plan-network-sizing.md).

1. Check which connections to other VPCs, to on-premises networks, and to the internet Amazon EVS supports. For more information, see [Supported network configurations](plan-network-supported.md).

1. Plan the NSX Edge cluster, the Tier-0 gateway, and the BGP peering with Amazon VPC Route Server. For more information, see [Plan NSX Edge and VPC Route Server design](plan-nsx-design.md).

1. If you plan to migrate workloads with VMware HCX, choose private or internet connectivity. For more information, see [Plan HCX connectivity](plan-hcx-connectivity.md).

Record your values in the [Deployment prerequisite checklist](evs-deployment-prereq-checklist.md). When you are ready to build the network, see [Build the network foundation](network-foundation.md).

**Topics**
+ [Plan your VPC and VLAN subnets](plan-network-sizing.md)
+ [Supported network configurations](plan-network-supported.md)
+ [Plan NSX Edge and VPC Route Server design](plan-nsx-design.md)
+ [Plan HCX connectivity](plan-hcx-connectivity.md)