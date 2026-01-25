**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Continuous Deployment with Argo CD

Argo CD is a declarative, GitOps continuous delivery tool for Kubernetes.
With Argo CD, you can automate the deployment and lifecycle management of your applications across multiple clusters and environments.
Argo CD supports multiple source types including Git repositories, Helm registries (HTTP and OCI), and OCI images—providing flexibility for organizations with different security and compliance requirements.

With EKS Capabilities, Argo CD is fully managed by AWS, eliminating the need to install, maintain, and scale Argo CD controllers and their dependencies on your clusters.

## How Argo CD Works

Argo CD follows the GitOps pattern, where your application source (Git repository, Helm registry, or OCI image) is the source of truth for defining the desired application state.
When you create an Argo CD `Application` resource, you specify the source containing your application manifests and the target Kubernetes cluster and namespace.
Argo CD continuously monitors both the source and the live state in the cluster, automatically synchronizing any changes to ensure the cluster state matches the desired state.

###### Note

With the EKS Capability for Argo CD, the Argo CD software runs in the AWS control plane, not on your worker nodes.
This means your worker nodes don’t need direct access to Git repositories or Helm registries—the capability handles source access from the AWS account.

Argo CD provides three primary resource types:

- **Application**: Defines a deployment from a Git repository to a target cluster
- **ApplicationSet**: Generates multiple Applications from templates for multi-cluster deployments
- **AppProject**: Provides logical grouping and access control for Applications

**Example: Creating an Argo CD Application**

The following example shows how to create an Argo CD `Application` resource:

```
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: guestbook
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/argoproj/argocd-example-apps.git
    targetRevision: HEAD
    path: guestbook
  destination:
    name: in-cluster
    namespace: guestbook
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
```

###### Note

Use `destination.name` with the cluster name you used when registering the cluster (like `in-cluster` for the local cluster).
The `destination.server` field also works with EKS cluster ARNs, but using cluster names is recommended for better readability.

## Benefits of Argo CD

Argo CD implements a GitOps workflow where you define your application configurations in Git repositories and Argo CD automatically syncs your applications to match the desired state.
This Git-centric approach provides a complete audit trail of all changes, enables easy rollbacks, and integrates naturally with your existing code review and approval processes.
Argo CD automatically detects and reconciles drift between the desired state in Git and the actual state in your clusters, ensuring your deployments remain consistent with your declared configuration.

With Argo CD, you can deploy and manage applications across multiple clusters from a single Argo CD instance, simplifying operations in multi-cluster and multi-region environments.
The Argo CD UI provides visualization and monitoring capabilities, allowing you to view the deployment status, health, and history of your applications.
The UI integrates with AWS Identity Center (formerly AWS SSO) for seamless authentication and authorization, enabling you to control access using your existing identity management infrastructure.

As part of EKS Managed Capabilities, Argo CD is fully managed by AWS, eliminating the need to install, configure, and maintain Argo CD infrastructure.
AWS handles scaling, patching, and operational management, allowing your teams to focus on application delivery rather than tool maintenance.

## Integration with AWS Identity Center

EKS Managed Capabilities provides direct integration between Argo CD and AWS Identity Center, enabling seamless authentication and authorization for your users.
When you enable the Argo CD capability, you can configure AWS Identity Center integration to map Identity Center groups and users to Argo CD RBAC roles, allowing you to control who can access and manage applications in Argo CD.

## Integration with Other EKS Managed Capabilities

Argo CD integrates with other EKS Managed Capabilities.

- **AWS Controllers for Kubernetes (ACK)**: Use Argo CD to manage the deployment of ACK resources across multiple clusters, enabling GitOps workflows for your AWS infrastructure.
- **kro (Kube Resource Orchestrator)**: Use Argo CD to deploy kro compositions across multiple clusters, enabling consistent resource composition across your Kubernetes estate.

## Getting Started with Argo CD

To get started with the EKS Capability for Argo CD:

1. Create and configure an IAM Capability Role with the necessary permissions for Argo CD to access your sources and manage applications.
2. [Create an Argo CD capability resource](create-argocd-capability.md "create-argocd-capability.md") on your EKS cluster through the AWS Console, AWS CLI, or your preferred infrastructure as code tool.
3. Configure repository access and register clusters for application deployment.
4. Create Application resources to deploy your applications from your declarative sources.
