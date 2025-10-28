# Deployment options

This chapter covers using eksctl to manage EKS clusters deployed to alternate environments.

For the most accurate information about EKS deployment options, see [Deploy Amazon EKS clusters across cloud and on-premises environments](../userguide/eks-deployment-options.md "../userguide/eks-deployment-options.md") in the _EKS User Guide_.

## Topics:

- [EKS Anywhere](eksctl-anywhere.md "eksctl-anywhere.md")
  - Use eksctl with Amazon EKS Anywhere clusters.
  - Amazon EKS Anywhere is container management software built by AWS that makes it easier to run and manage Kubernetes on-premises and at the edge.

- [AWS Outposts Support](outposts.md "outposts.md")
  - Use eksctl with EKS clusters on AWS Outposts.
  - AWS Outposts is a family of fully managed solutions delivering AWS infrastructure and services to virtually any on-premises or edge location for a truly consistent hybrid experience.
  - AWS Outposts support in eksctl lets you create local clusters with the entire Kubernetes cluster, including the EKS control plane and worker nodes, running locally on AWS Outposts.

- [EKS Hybrid Nodes](hybrid-nodes.md "hybrid-nodes.md")
  - Run on-premises and edge applications on customer-managed infrastructure with the same AWS EKS clusters, features, and tools you use in the AWS Cloud.
