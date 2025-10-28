**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Amazon EKS Hybrid Nodes overview

With _Amazon EKS Hybrid Nodes_, you can use your on-premises and edge infrastructure as nodes in Amazon EKS clusters. AWS manages the AWS-hosted Kubernetes control plane of the Amazon EKS cluster, and you manage the hybrid nodes that run in your on-premises or edge environments. This unifies Kubernetes management across your environments and offloads Kubernetes control plane management to AWS for your on-premises and edge applications.

Amazon EKS Hybrid Nodes works with any on-premises hardware or virtual machines, bringing the efficiency, scalability, and availability of Amazon EKS to wherever your applications need to run. You can use a wide range of Amazon EKS features with Amazon EKS Hybrid Nodes including Amazon EKS add-ons, Amazon EKS Pod Identity, cluster access entries, cluster insights, and extended Kubernetes version support. Amazon EKS Hybrid Nodes natively integrates with AWS services including AWS Systems Manager, AWS IAM Roles Anywhere, Amazon Managed Service for Prometheus, and Amazon CloudWatch for centralized monitoring, logging, and identity management.

With Amazon EKS Hybrid Nodes, there are no upfront commitments or minimum fees, and you are charged per hour for the vCPU resources of your hybrid nodes when they are attached to your Amazon EKS clusters. For more pricing information, see [Amazon EKS Pricing](https://aws.amazon.com/eks/pricing/ "https://aws.amazon.com/eks/pricing/").

## Features

EKS Hybrid Nodes has the following high-level features:

- **Managed Kubernetes control plane**: AWS manages the AWS-hosted Kubernetes control plane of the EKS cluster, and you manage the hybrid nodes that run in your on-premises or edge environments. This unifies Kubernetes management across your environments and offloads Kubernetes control plane management to AWS for your on-premises and edge applications. By moving the Kubernetes control plane to AWS, you can conserve on-premises capacity for your applications and trust that the Kubernetes control plane scales with your workloads.
- **Consistent EKS experience**: Most EKS features are supported with EKS Hybrid Nodes for a consistent EKS experience across your on-premises and cloud environments including EKS add-ons, EKS Pod Identity, cluster access entries, cluster insights, extended Kubernetes version support, and more. See [Configure add-ons for hybrid nodes](hybrid-nodes-add-ons.md "hybrid-nodes-add-ons.md") for more information on the EKS add-ons supported with EKS Hybrid Nodes.
- **Centralized observability and identity management**: EKS Hybrid Nodes natively integrates with AWS services including AWS Systems Manager, AWS IAM Roles Anywhere, Amazon Managed Service for Prometheus, and Amazon CloudWatch for centralized monitoring, logging, and identity management.
- **Burst-to-cloud or add on-premises capacity**: A single EKS cluster can be used to run hybrid nodes and nodes in AWS Regions, AWS Local Zones, or AWS Outposts to burst-to-cloud or add on-premises capacity to your EKS clusters. See [Considerations for mixed mode clusters](hybrid-nodes-webhooks.md#hybrid-nodes-considerations-mixed-mode "hybrid-nodes-webhooks.md#hybrid-nodes-considerations-mixed-mode") for more information.
- **Flexible infrastructure**: EKS Hybrid Nodes follows a _bring your own infrastructure_ approach and is agnostic to the infrastructure you use for hybrid nodes. You can run hybrid nodes on physical or virtual machines, and x86 and ARM architectures, making it possible to migrate on-premises workloads running on hybrid nodes across different infrastructure types.
- **Flexible networking**: With EKS Hybrid Nodes, communication between the EKS control plane and hybrid nodes is routed through the VPC and subnets you pass during cluster creation, which builds on the [existing mechanism](../best-practices/subnets.md "../best-practices/subnets.md") in EKS for control plane to node networking. This is flexible to your preferred method of connecting your on-premises networks to a VPC in AWS. There are several [documented options](../../../whitepapers/latest/aws-vpc-connectivity-options/network-to-amazon-vpc-connectivity-options.md "../../../whitepapers/latest/aws-vpc-connectivity-options/network-to-amazon-vpc-connectivity-options.md") available including AWS Site-to-Site VPN, AWS Direct Connect, or your own VPN solution, and you can choose the method that best fits your use case.

## Limits

- Up to 15 CIDRs for Remote Node Networks and 15 CIDRs for Remote Pod Networks per cluster are supported.

## Considerations

- EKS Hybrid Nodes can be used with new or existing EKS clusters.
- EKS Hybrid Nodes is available in all AWS Regions, except the AWS GovCloud (US) Regions and the AWS China Regions.
- EKS Hybrid Nodes must have a reliable connection between your on-premises environment and AWS. EKS Hybrid Nodes is not a fit for disconnected, disrupted, intermittent or limited (DDIL) environments. If you are running in a DDIL environment, consider [Amazon EKS Anywhere](https://aws.amazon.com/eks/eks-anywhere/ "https://aws.amazon.com/eks/eks-anywhere/"). Reference the [Best Practices for EKS Hybrid Nodes](../best-practices/hybrid-nodes-network-disconnections.md "../best-practices/hybrid-nodes-network-disconnections.md") for information on how hybrid nodes behave during network disconnection scenarios.
- Running EKS Hybrid Nodes on cloud infrastructure, including AWS Regions, AWS Local Zones, AWS Outposts, or in other clouds, is not supported. You will be charged the hybrid nodes fee if you run hybrid nodes on Amazon EC2 instances.
- Billing for hybrid nodes starts when the nodes join the EKS cluster and stops when the nodes are removed from the cluster. Be sure to remove your hybrid nodes from your EKS cluster if you are not using them.

## Additional resources

- [**EKS Hybrid Nodes workshop**](https://www.eksworkshop.com/docs/networking/eks-hybrid-nodes/ "https://www.eksworkshop.com/docs/networking/eks-hybrid-nodes/"): Step-by-step instructions for deploying EKS Hybrid Nodes in a demo environment.
- [**AWS re:Invent: EKS Hybrid Nodes**](https://www.youtube.com/watch?v=ZxC7SkemxvU "https://www.youtube.com/watch?v=ZxC7SkemxvU"): AWS re:Invent session introducing the EKS Hybrid Nodes launch with a customer showing how they are using EKS Hybrid Nodes in their environment.
- [**AWS re:Post: Cluster networking for EKS Hybrid Nodes**](https://repost.aws/articles/ARL44xuau6TG2t-JoJ3mJ5Mw/unpacking-the-cluster-networking-for-amazon-eks-hybrid-nodes "https://repost.aws/articles/ARL44xuau6TG2t-JoJ3mJ5Mw/unpacking-the-cluster-networking-for-amazon-eks-hybrid-nodes"): Article explaining various methods for setting up networking for EKS Hybrid Nodes.
- [**AWS blog: Run GenAI inference across environments with EKS Hybrid Nodes**](https://aws.amazon.com/blogs/containers/run-genai-inference-across-environments-with-amazon-eks-hybrid-nodes/ "https://aws.amazon.com/blogs/containers/run-genai-inference-across-environments-with-amazon-eks-hybrid-nodes/"): Blog post showing how to run GenAI inference across environments with EKS Hybrid Nodes.
