# VPC and subnet best practices for EMR Studio

Use the following best practices to set up an Amazon Virtual Private Cloud (Amazon VPC) with subnets for
EMR Studio:

- You can specify a maximum of five subnets in your VPC to associate with the
  Studio. We recommend that you provide multiple subnets in different Availability
  Zones in order to support Workspace availability and give Studio users
  access to clusters across different Availability Zones. To learn more about working with
  VPCs, subnets, and Availability Zones, see [VPCs and subnets](../../../vpc/latest/userguide/VPC_Subnets.md "../../../vpc/latest/userguide/VPC_Subnets.md") in the _Amazon Virtual Private Cloud User Guide_.
- The subnets that you specify should be able to communicate with each other.
- To let users link a Workspace to publicly hosted Git repositories, you should
  specify only private subnets that have access to the internet through Network Address
  Translation (NAT). For more information about setting up a private subnet for Amazon EMR, see
  [Private subnets](emr-clusters-in-a-vpc.md#emr-vpc-private-subnet "emr-clusters-in-a-vpc.md#emr-vpc-private-subnet").
- When you use Amazon EMR on EKS with EMR Studio, there must be _at
  least one subnet in common_ between your Studio and the Amazon EKS cluster
  that you use to register a virtual cluster. Otherwise, your managed endpoint won't appear
  as an option in Studio Workspaces. You can create an Amazon EKS cluster and
  associate it with a subnet that belongs to the Studio, or create a Studio
  and specify your EKS cluster's subnets.
- If you plan to use Amazon Amazon EMR on EKS with EMR Studio, choose the same VPC as your
  Amazon EKS cluster worker nodes.
