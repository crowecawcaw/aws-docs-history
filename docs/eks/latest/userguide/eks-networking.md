**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Configure networking for Amazon EKS clusters

Your Amazon EKS cluster is created in a VPC. Pod networking is provided by the Amazon VPC Container Network Interface (CNI) plugin for nodes that run on AWS infrastructure. If you are running nodes on your own infrastructure, see [Configure CNI for hybrid nodes](hybrid-nodes-cni.md "hybrid-nodes-cni.md"). This chapter includes the following topics for learning more about networking for your cluster.

###### Topics

- [Add an existing VPC Subnet to an Amazon EKS cluster from the management console](#add-existing-subnet "#add-existing-subnet")
- [View Amazon EKS networking requirements for VPC and subnets](network-reqs.md "network-reqs.md")
- [Create an Amazon VPC for your Amazon EKS cluster](creating-a-vpc.md "creating-a-vpc.md")
- [View Amazon EKS security group requirements for clusters](sec-group-reqs.md "sec-group-reqs.md")
- [Manage networking add-ons for Amazon EKS clusters](eks-networking-add-ons.md "eks-networking-add-ons.md")

## Add an existing VPC Subnet to an Amazon EKS cluster from the management console

1. Navigate to your cluster in the management console
2. From the **Networking** tab select **Manage VPC Resources**
3. From the **Subnets** dropdown, select additional subnets from the VPC of your cluster.

To create a new VPC Subnet:

- [Review EKS Subnet Requirements](network-reqs.md#network-requirements-subnets "network-reqs.md#network-requirements-subnets")
- See [Create a Subnet](../../../vpc/latest/userguide/create-subnets.md "../../../vpc/latest/userguide/create-subnets.md") in the Amazon Virtual Private Cloud User Guide.
