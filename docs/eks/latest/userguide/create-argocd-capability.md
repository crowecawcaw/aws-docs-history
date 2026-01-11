**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Create an Argo CD capability

This topic explains how to create an Argo CD capability on your Amazon EKS cluster.

## Prerequisites

Before creating an Argo CD capability, ensure you have:

- An existing Amazon EKS cluster running a supported Kubernetes version (all versions in standard and extended support are supported)
- **AWS Identity Center configured** - Required for Argo CD authentication (local users are not supported)
- An IAM Capability Role with permissions for Argo CD
- Sufficient IAM permissions to create capability resources on EKS clusters
- `kubectl` configured to communicate with your cluster
- (Optional) The Argo CD CLI installed for easier cluster and repository management
- (For CLI/eksctl) The appropriate CLI tool installed and configured

For instructions on creating the IAM Capability Role, see [Amazon EKS capability IAM role](capability-role.md "capability-role.md").
For Identity Center setup, see [Getting started with AWS Identity Center](../../../singlesignon/latest/userguide/getting-started.md "../../../singlesignon/latest/userguide/getting-started.md").

###### Important

The IAM Capability Role you provide determines which AWS resources Argo CD can access.
This includes Git repository access via CodeConnections and secrets in Secrets Manager.
For guidance on creating an appropriate role with least-privilege permissions, see [Amazon EKS capability IAM role](capability-role.md "capability-role.md") and [Security considerations for EKS Capabilities](capabilities-security.md "capabilities-security.md").

## Choose your tool

You can create an Argo CD capability using the AWS Management Console, AWS CLI, or eksctl:

- [Create an Argo CD capability using the Console](argocd-create-console.md "argocd-create-console.md") - Use the Console for a guided experience
- [Create an Argo CD capability using the AWS CLI](argocd-create-cli.md "argocd-create-cli.md") - Use the AWS CLI for scripting and automation
- [Create an Argo CD capability using eksctl](argocd-create-eksctl.md "argocd-create-eksctl.md") - Use eksctl for a Kubernetes-native experience

## What happens when you create an Argo CD capability

When you create an Argo CD capability:

1. EKS creates the Argo CD capability service in the AWS control plane
2. Custom Resource Definitions (CRDs) are installed in your cluster
3. Argo CD begins watching for its custom resources (Applications, ApplicationSets, AppProjects)
4. The capability status changes from `CREATING` to `ACTIVE`
5. The Argo CD UI becomes accessible through its URL

Once active, you can create Argo CD Applications in your cluster to deploy from your declarative sources.

## Next steps

After creating the Argo CD capability:

- [Argo CD concepts](argocd-concepts.md "argocd-concepts.md") - Learn about GitOps principles, sync policies, and multi-cluster patterns
- [Working with Argo CD](working-with-argocd.md "working-with-argocd.md") - Configure repository access, register target clusters, and create Applications
- [Argo CD considerations](argocd-considerations.md "argocd-considerations.md") - Explore multi-cluster architecture patterns and advanced configuration
