**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Working with Argo CD

With Argo CD, you define applications in Git repositories and Argo CD automatically syncs them to your Kubernetes clusters.
This enables declarative, version-controlled application deployment with automated drift detection.

## Prerequisites

Before working with Argo CD, you need:

- An EKS cluster with the Argo CD capability created (see [Create an Argo CD capability](create-argocd-capability.md "create-argocd-capability.md"))
- A Git repository containing Kubernetes manifests
- `kubectl` configured to communicate with your cluster

## Common tasks

The following topics guide you through common Argo CD tasks:

**[Configure repository access](argocd-configure-repositories.md "argocd-configure-repositories.md")** - Configure Argo CD to access your Git repositories using AWS Secrets Manager, AWS CodeConnections, or Kubernetes Secrets.

**[Register target clusters](argocd-register-clusters.md "argocd-register-clusters.md")** - Register target clusters where Argo CD will deploy applications.

**[Working with Argo CD Projects](argocd-projects.md "argocd-projects.md")** - Organize applications and enforce security boundaries using Projects for multi-tenant environments.

**[Create Applications](argocd-create-application.md "argocd-create-application.md")** - Create Applications that deploy from Git repositories with automated or manual sync policies.

**[Use ApplicationSets](argocd-applicationsets.md "argocd-applicationsets.md")** - Use ApplicationSets to deploy applications across multiple environments or clusters using templates and generators.

## Access the Argo CD UI

Access the Argo CD UI through the EKS console:

1. Open the Amazon EKS console
2. Select your cluster
3. Choose the **Capabilities** tab
4. Choose **Argo CD**
5. Choose **Open Argo CD UI**

The UI provides visual application topology, sync status and history, resource health and events, manual sync controls, and application management.

## Upstream documentation

For detailed information about Argo CD features:

- [Argo CD Documentation](https://argo-cd.readthedocs.io/ "https://argo-cd.readthedocs.io/") - Complete user guide
- [Application Spec](https://argo-cd.readthedocs.io/en/stable/user-guide/application-specification/ "https://argo-cd.readthedocs.io/en/stable/user-guide/application-specification/") - Full Application API reference
- [ApplicationSet Guide](https://argo-cd.readthedocs.io/en/stable/user-guide/application-set/ "https://argo-cd.readthedocs.io/en/stable/user-guide/application-set/") - ApplicationSet patterns and examples
- [Argo CD GitHub](https://github.com/argoproj/argo-cd "https://github.com/argoproj/argo-cd") - Source code and examples
