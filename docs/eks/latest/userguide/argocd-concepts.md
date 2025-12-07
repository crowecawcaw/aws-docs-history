**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Argo CD concepts

Argo CD implements GitOps by treating Git as the single source of truth for your application deployments.
This topic walks through a practical example, then explains the core concepts you need to understand when working with the EKS Capability for Argo CD.

## Getting started with Argo CD

After creating the Argo CD capability (see [Create an Argo CD capability](create-argocd-capability.md "create-argocd-capability.md")), you can start deploying applications.
This example walks through registering a cluster and creating an Application.

### Step 1: Set up

**Register your cluster** (required)

Register the cluster where you want to deploy applications.
For this example, we’ll register the same cluster where Argo CD is running (you can use the name `in-cluster` for compatibility with most Argo CD examples):

```
# Get your cluster ARN
CLUSTER_ARN=$(aws eks describe-cluster \
  --name my-cluster \
  --query 'cluster.arn' \
  --output text)

# Register the cluster using Argo CD CLI
argocd cluster add $CLUSTER_ARN \
  --aws-cluster-name $CLUSTER_ARN \
  --name in-cluster \
  --project default
```

###### Note

For information about configuring the Argo CD CLI to work with the Argo CD capability in EKS, see [Using the Argo CD CLI with the managed capability](argocd-comparison.md#argocd-cli-configuration "argocd-comparison.md#argocd-cli-configuration").

Alternatively, register the cluster using a Kubernetes Secret (see [Register target clusters](argocd-register-clusters.md "argocd-register-clusters.md") for details).

**Configure repository access** (optional)

This example uses a public GitHub repository, so no repository configuration is required.
For private repositories, configure access using AWS Secrets Manager, CodeConnections, or Kubernetes Secrets (see [Configure repository access](argocd-configure-repositories.md "argocd-configure-repositories.md") for details).

For AWS services (ECR for Helm charts, CodeConnections, and CodeCommit), you can reference them directly in Application resources without creating a Repository.
The Capability Role must have the required IAM permissions.
See [Configure repository access](argocd-configure-repositories.md "argocd-configure-repositories.md") for details.

### Step 2: Create an Application

Create this Application manifest in `my-app.yaml`:

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
    syncOptions:
    - CreateNamespace=true
```

Apply the Application:

```
kubectl apply -f my-app.yaml
```

After applying this Application, Argo CD:

1. Syncs the application from Git to your cluster (initial deployment)
2. Monitors the Git repository for changes
3. Automatically syncs subsequent changes to your cluster
4. Detects and corrects any drift from the desired state
5. Provides health status and sync history in the UI

View the application status:

```
kubectl get application guestbook -n argocd
```

You can also view the application using the Argo CD CLI (`argocd app get guestbook`) or the Argo CD UI (accessible from the EKS console under your cluster’s Capabilities tab).

###### Note

Use the cluster name in `destination.name` (the name you used when registering the cluster).
The managed capability does not support the local in-cluster default (`kubernetes.default.svc`).

## Core concepts

### GitOps principles and source types

Argo CD implements GitOps, where your application source is the single source of truth for deployments:

- **Declarative** - Desired state is declared using YAML manifests, Helm charts, or Kustomize overlays
- **Versioned** - Every change is tracked with complete audit trail
- **Automated** - Argo CD continuously monitors sources and automatically syncs changes
- **Self-healing** - Detects and corrects drift between desired and actual cluster state

**Supported source types**:

- **Git repositories** - GitHub, GitLab, Bitbucket, CodeCommit (HTTPS, SSH, or CodeConnections)
- **Helm registries** - HTTP registries (like `https://aws.github.io/eks-charts`) and OCI registries (like `public.ecr.aws`)
- **OCI images** - Container images containing manifests or Helm charts (like `oci://registry-1.docker.io/user/my-app`)

This flexibility allows organizations to choose sources that meet their security and compliance requirements.
For example, organizations that restrict Git access from clusters can use ECR for Helm charts or OCI images.

For more information, see [Application Sources](https://argo-cd.readthedocs.io/en/stable/user-guide/application-sources/ "https://argo-cd.readthedocs.io/en/stable/user-guide/application-sources/") in the Argo CD documentation.

### Sync and reconciliation

Argo CD continuously monitors your sources and clusters to detect and correct differences:

1. Polls sources for changes (default: every 6 minutes)
2. Compares desired state with cluster state
3. Marks applications as `Synced` or `OutOfSync`
4. Syncs changes automatically (if configured) or waits for manual approval
5. Monitors resource health after sync

**Sync waves** control resource creation order using annotations:

```
metadata:
  annotations:
    argocd.argoproj.io/sync-wave: "0"  # Default if not specified
```

Resources are applied in wave order (lower numbers first, including negative numbers like `-1`).
This allows you to create dependencies like namespaces (wave `-1`) before deployments (wave `0`).

**Self-healing** automatically reverts manual changes:

```
spec:
  syncPolicy:
    automated:
      selfHeal: true
```

###### Note

The managed capability uses annotation-based resource tracking (not label-based) for better compatibility with Kubernetes conventions and other tools.

For detailed information about sync phases, hooks, and advanced patterns, see the [Argo CD sync documentation](https://argo-cd.readthedocs.io/en/stable/user-guide/sync-waves/ "https://argo-cd.readthedocs.io/en/stable/user-guide/sync-waves/").

### Application health

Argo CD monitors the health of all resources in your application:

**Health statuses**: \* **Healthy** - All resources running as expected \* **Progressing** - Resources being created or updated \* **Degraded** - Some resources not healthy (pods crashing, jobs failing) \* **Suspended** - Application intentionally paused \* **Missing** - Resources defined in Git not present in cluster

Argo CD has built-in health checks for common Kubernetes resources (Deployments, StatefulSets, Jobs, etc.) and supports custom health checks for CRDs.

Application health is determined by all its resources - if any resource is `Degraded`, the application is `Degraded`.

For more information, see [Resource Health](https://argo-cd.readthedocs.io/en/stable/operator-manual/health/ "https://argo-cd.readthedocs.io/en/stable/operator-manual/health/") in the Argo CD documentation.

### Multi-cluster patterns

Argo CD supports two main deployment patterns:

**Hub-and-spoke** - Run Argo CD on a dedicated management cluster that deploys to multiple workload clusters: \* Centralized control and visibility \* Consistent policies across all clusters \* One Argo CD instance to manage \* Clear separation between control plane and workloads

**Per-cluster** - Run Argo CD on each cluster, managing only that cluster’s applications: \* Cluster separation (one failure doesn’t affect others) \* Simpler networking (no cross-cluster communication) \* Easier initial setup (no cluster registration)

Choose hub-and-spoke for platform teams managing many clusters, or per-cluster for independent teams or when clusters must be fully isolated.

For detailed multi-cluster configuration, see [Argo CD considerations](argocd-considerations.md "argocd-considerations.md").

### Projects

Projects provide logical grouping and access control for Applications:

- **Source restrictions** - Limit which Git repositories can be used
- **Destination restrictions** - Limit which clusters and namespaces can be targeted
- **Resource restrictions** - Limit which Kubernetes resource types can be deployed
- **RBAC integration** - Map projects to AWS Identity Center user and group IDs

All Applications belong to a project. If not specified, they use the `default` project (which has no restrictions). For production, create projects with appropriate restrictions.

For project configuration and RBAC patterns, see [Configure Argo CD permissions](argocd-permissions.md "argocd-permissions.md").

### Repository organization

Most teams use directory-based organization with Kustomize overlays or Helm values files for different environments:

```
my-app/
├── base/
│   ├── deployment.yaml
│   └── service.yaml
└── overlays/
    ├── dev/
    │   └── kustomization.yaml
    ├── staging/
    │   └── kustomization.yaml
    └── prod/
        └── kustomization.yaml
```

This approach provides flexibility and clarity while keeping all environment configurations in a single repository.

For detailed repository structure patterns and best practices, see the [Argo CD best practices documentation](https://argo-cd.readthedocs.io/en/stable/user-guide/best_practices/ "https://argo-cd.readthedocs.io/en/stable/user-guide/best_practices/").

### Sync options

Fine-tune sync behavior with common options:

- `CreateNamespace=true` - Automatically create destination namespace
- `ServerSideApply=true` - Use server-side apply for better conflict resolution
- `SkipDryRunOnMissingResource=true` - Skip dry run when CRDs don’t exist yet (useful for kro instances)

```
spec:
  syncPolicy:
    syncOptions:
    - CreateNamespace=true
    - ServerSideApply=true
```

For a complete list of sync options, see the [Argo CD sync options documentation](https://argo-cd.readthedocs.io/en/stable/user-guide/sync-options/ "https://argo-cd.readthedocs.io/en/stable/user-guide/sync-options/").

## Next steps

- [Configure repository access](argocd-configure-repositories.md "argocd-configure-repositories.md") - Configure Git repository access
- [Register target clusters](argocd-register-clusters.md "argocd-register-clusters.md") - Register target clusters for deployment
- [Create Applications](argocd-create-application.md "argocd-create-application.md") - Create your first Application
- [Argo CD considerations](argocd-considerations.md "argocd-considerations.md") - EKS-specific patterns, Identity Center integration, and multi-cluster configuration
- [Argo CD Documentation](https://argo-cd.readthedocs.io/en/stable/ "https://argo-cd.readthedocs.io/en/stable/") - Comprehensive Argo CD documentation including sync hooks, health checks, and advanced patterns
