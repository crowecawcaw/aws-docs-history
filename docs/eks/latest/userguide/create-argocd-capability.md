

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Create an Argo CD capability
<a name="create-argocd-capability"></a>

This topic explains how to create an Argo CD capability on your Amazon EKS cluster.

## Prerequisites
<a name="_prerequisites"></a>

Before creating an Argo CD capability, ensure you have:
+ An existing Amazon EKS cluster running a supported Kubernetes version (all versions in standard and extended support are supported)
+  ** AWS Identity Center configured** - Required for Argo CD authentication (local users are not supported)
+ An IAM Capability Role with permissions for Argo CD
+ Sufficient IAM permissions to create capability resources on EKS clusters
+  `kubectl` configured to communicate with your cluster
+ (Optional) The Argo CD CLI installed for easier cluster and repository management
+ (For CLI/eksctl) The appropriate CLI tool installed and configured

For instructions on creating the IAM Capability Role, see [Amazon EKS capability IAM role](capability-role.md). For Identity Center setup, see [Getting started with AWS Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/getting-started.html).

**Important**  
The IAM Capability Role you provide determines which AWS resources Argo CD can access. This includes Git repository access via CodeConnections and secrets in Secrets Manager. For guidance on creating an appropriate role with least-privilege permissions, see [Amazon EKS capability IAM role](capability-role.md) and [Security considerations for EKS Capabilities](capabilities-security.md).

## Choose your tool
<a name="_choose_your_tool"></a>

You can create an Argo CD capability using the AWS Management Console, AWS CLI, or eksctl:
+  [Create an Argo CD capability using the Console](argocd-create-console.md) - Use the Console for a guided experience
+  [Create an Argo CD capability using the AWS CLI](argocd-create-cli.md) - Use the AWS CLI for scripting and automation
+  [Create an Argo CD capability using eksctl](argocd-create-eksctl.md) - Use eksctl for a Kubernetes-native experience

## What happens when you create an Argo CD capability
<a name="_what_happens_when_you_create_an_argo_cd_capability"></a>

When you create an Argo CD capability:

1. EKS creates the Argo CD capability service in the AWS control plane

1. Custom Resource Definitions (CRDs) are installed in your cluster

1. An access entry is automatically created for your IAM Capability Role with capability-specific access entry policies that grant baseline Kubernetes permissions (see [Security considerations for EKS Capabilities](capabilities-security.md))

1. Argo CD begins watching for its custom resources (Applications, ApplicationSets, AppProjects)

1. The capability status changes from `CREATING` to `ACTIVE` 

1. The Argo CD UI becomes accessible through its URL

Once active, you can create Argo CD Applications in your cluster to deploy from your declarative sources.

**Note**  
The automatically created access entry does not grant permissions to deploy applications to clusters. To deploy applications, you must configure additional Kubernetes RBAC permissions for each target cluster. See [Register target clusters](argocd-register-clusters.md) for details on registering clusters and configuring access.

## Next steps
<a name="_next_steps"></a>

After creating the Argo CD capability:
+  [Argo CD concepts](argocd-concepts.md) - Learn about GitOps principles, sync policies, and multi-cluster patterns
+  [Working with Argo CD](working-with-argocd.md) - Configure repository access, register target clusters, and create Applications
+  [Argo CD considerations](argocd-considerations.md) - Explore multi-cluster architecture patterns and advanced configuration