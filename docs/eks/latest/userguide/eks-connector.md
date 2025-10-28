**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Connect a Kubernetes cluster to an Amazon EKS Management Console with Amazon EKS Connector

You can use Amazon EKS Connector to register and connect any conformant Kubernetes cluster to AWS and visualize it in the Amazon EKS console. After a cluster is connected, you can see the status, configuration, and workloads for that cluster in the Amazon EKS console. You can use this feature to view connected clusters in Amazon EKS console, but you can’t manage them. The Amazon EKS Connector requires an agent that is an [open source project on Github](https://github.com/aws/amazon-eks-connector "https://github.com/aws/amazon-eks-connector"). For additional technical content, including frequently asked questions and troubleshooting, see [Troubleshoot Amazon EKS Connector issues](troubleshooting-connector.md "troubleshooting-connector.md").

The Amazon EKS Connector can connect the following types of Kubernetes clusters to Amazon EKS.

- On-premises Kubernetes clusters
- Self-managed clusters that are running on Amazon EC2
- Managed clusters from other cloud providers

## Amazon EKS Connector considerations

Before you use Amazon EKS Connector, understand the following:

- You must have administrative privileges to the Kubernetes cluster to connect the cluster to Amazon EKS.
- The Kubernetes cluster must have Linux 64-bit (x86) worker nodes present before connecting. ARM worker nodes aren’t supported.
- You must have worker nodes in your Kubernetes cluster that have outbound access to the `ssm.` and `ssmmessages.` Systems Manager endpoints. For more information, see [Systems Manager endpoints](../../../general/latest/gr/ssm.md "../../../general/latest/gr/ssm.md") in the _AWS General Reference_.
- By default, you can connect up to 10 clusters in a Region. You can request an increase through the [service quota console](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md"). See [Requesting a quota increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") for more information.
- Only the Amazon EKS `RegisterCluster`, `ListClusters`, `DescribeCluster`, and `DeregisterCluster` APIs are supported for external Kubernetes clusters.
- You must have the following permissions to register a cluster:
  - eks:RegisterCluster
  - ssm:CreateActivation
  - ssm:DeleteActivation
  - iam:PassRole

- You must have the following permissions to deregister a cluster:
  - eks:DeregisterCluster
  - ssm:DeleteActivation
  - ssm:DeregisterManagedInstance

## Required IAM roles for Amazon EKS Connector

Using the Amazon EKS Connector requires the following two IAM roles:

- The [Amazon EKS Connector](using-service-linked-roles-eks-connector.md "using-service-linked-roles-eks-connector.md") service-linked role is created when you register a cluster for the first time.
- You must create the Amazon EKS Connector agent IAM role. See [Amazon EKS connector IAM role](connector-iam-role.md "connector-iam-role.md") for details.

To enable cluster and workload view permission for [IAM principals](../../../IAM/latest/UserGuide/id_roles.md#iam-term-principal "../../../IAM/latest/UserGuide/id_roles.md#iam-term-principal"), apply the `eks-connector` and Amazon EKS Connector cluster roles to your cluster. Follow the steps in [Grant access to view Kubernetes cluster resources on an Amazon EKS console](connector-grant-access.md "connector-grant-access.md").
