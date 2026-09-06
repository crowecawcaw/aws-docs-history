

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Argo CD concepts
<a name="argocd-concepts"></a>

Argo CD implements GitOps by treating Git as the single source of truth for your application deployments. This topic walks through a practical example, then explains the core concepts you need to understand when working with the EKS Capability for Argo CD.

## Getting started with Argo CD
<a name="_getting_started_with_argo_cd"></a>

After creating the Argo CD capability (see [Create an Argo CD capability](create-argocd-capability.md)), you can start deploying applications. This example walks through registering a cluster and creating an Application.

### Step 1: Set up
<a name="_step_1_set_up"></a>

 **Register your cluster** (required)

Register the cluster where you want to deploy applications. For this example, we’ll register the same cluster where Argo CD is running (you can use the name `in-cluster` for compatibility with most Argo CD examples):

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

**Note**  
For information about configuring the Argo CD CLI to work with the Argo CD capability in EKS, see [Using the Argo CD CLI with the managed capability](argocd-comparison.md#argocd-cli-configuration).

Alternatively, register the cluster using a Kubernetes Secret (see [Register target clusters](argocd-register-clusters.md) for details).

 **Configure repository access** (optional)

This example uses a public GitHub repository, so no repository configuration is required. For private repositories, configure access using AWS Secrets Manager, CodeConnections, or Kubernetes Secrets (see [Configure repository access](argocd-configure-repositories.md) for details).

For AWS services (ECR for Helm charts, CodeConnections, and CodeCommit), you can reference them directly in Application resources without creating a Repository. The Capability Role must have the required IAM permissions. See [Configure repository access](argocd-configure-repositories.md) for details.

### Step 2: Create an Application
<a name="_step_2_create_an_application"></a>

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

After applying this Application, Argo CD: 1. Syncs the application from Git to your cluster (initial deployment) 2. Monitors the Git repository for changes 3. Automatically syncs subsequent changes to your cluster 4. Detects and corrects any drift from the desired state 5. Provides health status and sync history in the UI

View the application status:

```
kubectl get application guestbook -n argocd
```

You can also view the application using the Argo CD CLI or the Argo CD UI (accessible from the EKS console under your cluster’s Capabilities tab).

**Note**  
When using the Argo CD CLI with the managed capability, specify applications with the namespace prefix: `argocd app get argocd/guestbook`.

**Note**  
Use the cluster name in `destination.name` (the name you used when registering the cluster). The managed capability does not support the local in-cluster default (`kubernetes.default.svc`).

## Core concepts
<a name="_core_concepts"></a>

### GitOps principles and source types
<a name="_gitops_principles_and_source_types"></a>

Argo CD implements GitOps, where your application source is the single source of truth for deployments:
+  **Declarative** - Desired state is declared using YAML manifests, Helm charts, or Kustomize overlays
+  **Versioned** - Every change is tracked with complete audit trail
+  **Automated** - Argo CD continuously monitors sources and automatically syncs changes
+  **Self-healing** - Detects and corrects drift between desired and actual cluster state

 **Supported source types**:
+  **Git repositories** - GitHub, GitLab, Bitbucket, CodeCommit (HTTPS, SSH, or CodeConnections)
+  **Helm registries** - HTTP registries (like `https://aws.github.io/eks-charts`) and OCI registries (like `public.ecr.aws`)
+  **OCI images** - Container images containing manifests or Helm charts (like `oci://registry-1.docker.io/user/my-app`)

This flexibility allows organizations to choose sources that meet their security and compliance requirements. For example, organizations that restrict Git access from clusters can use ECR for Helm charts or OCI images.

For more information, see [Application Sources](https://argo-cd.readthedocs.io/en/stable/user-guide/application-sources/) in the Argo CD documentation.

### Sync and reconciliation
<a name="_sync_and_reconciliation"></a>

Argo CD continuously monitors your sources and clusters to detect and correct differences:

1. Polls sources for changes (default: every 6 minutes)

1. Compares desired state with cluster state

1. Marks applications as `Synced` or `OutOfSync` 

1. Syncs changes automatically (if configured) or waits for manual approval

1. Monitors resource health after sync

 **Sync waves** control resource creation order using annotations:

```
metadata:
  annotations:
    argocd.argoproj.io/sync-wave: "0"  # Default if not specified
```

Resources are applied in wave order (lower numbers first, including negative numbers like `-1`). Wave `0` is the default if not specified. This allows you to create dependencies like namespaces (wave `-1`) before deployments (wave `0`) before services (wave `1`).

 **Self-healing** automatically reverts manual changes:

```
spec:
  syncPolicy:
    automated:
      selfHeal: true
```

**Note**  
The managed capability uses annotation-based resource tracking (not label-based) for better compatibility with Kubernetes conventions and other tools.

For detailed information about sync phases, hooks, and advanced patterns, see the [Argo CD sync documentation](https://argo-cd.readthedocs.io/en/stable/user-guide/sync-waves/).

### Application health
<a name="_application_health"></a>

Argo CD monitors the health of all resources in your application:

 **Health statuses**: \* **Healthy** - All resources running as expected \* **Progressing** - Resources being created or updated \* **Degraded** - Some resources not healthy (pods crashing, jobs failing) \* **Suspended** - Application intentionally paused \* **Missing** - Resources defined in Git not present in cluster

Argo CD has built-in health checks for common Kubernetes resources (Deployments, StatefulSets, Jobs, etc.) and supports custom health checks for CRDs.

Application health is determined by all its resources - if any resource is `Degraded`, the application is `Degraded`.

For more information, see [Resource Health](https://argo-cd.readthedocs.io/en/stable/operator-manual/health/) in the Argo CD documentation.

### Multi-cluster patterns
<a name="_multi_cluster_patterns"></a>

Argo CD supports two main deployment patterns:

 **Hub-and-spoke** - Run Argo CD on a dedicated management cluster that deploys to multiple workload clusters: \* Centralized control and visibility \* Consistent policies across all clusters \* One Argo CD instance to manage \* Clear separation between control plane and workloads

 **Per-cluster** - Run Argo CD on each cluster, managing only that cluster’s applications: \* Cluster separation (one failure doesn’t affect others) \* Simpler networking (no cross-cluster communication) \* Easier initial setup (no cluster registration)

Choose hub-and-spoke for platform teams managing many clusters, or per-cluster for independent teams or when clusters must be fully isolated.

For detailed multi-cluster configuration, see [Argo CD considerations](argocd-considerations.md).

### Projects
<a name="_projects"></a>

Projects provide logical grouping and access control for Applications:
+  **Source restrictions** - Limit which Git repositories can be used
+  **Destination restrictions** - Limit which clusters and namespaces can be targeted
+  **Resource restrictions** - Limit which Kubernetes resource types can be deployed
+  **RBAC integration** - Map projects to AWS Identity Center user and group IDs

Applications belong to a single project. If not specified, they use the `default` project, which has no restrictions by default. For production use, edit the `default` project to restrict access and create new projects with appropriate restrictions.

For project configuration and RBAC patterns, see [Configure Argo CD permissions](argocd-permissions.md).

### Sync options
<a name="_sync_options"></a>

Fine-tune sync behavior with common options:
+  `CreateNamespace=true` - Automatically create destination namespace
+  `ServerSideApply=true` - Use server-side apply for better conflict resolution
+  `SkipDryRunOnMissingResource=true` - Skip dry run when CRDs don’t exist yet (useful for kro instances)

```
spec:
  syncPolicy:
    syncOptions:
    - CreateNamespace=true
    - ServerSideApply=true
    - SkipDryRunOnMissingResource=true
```

For a complete list of sync options, see the [Argo CD sync options documentation](https://argo-cd.readthedocs.io/en/stable/user-guide/sync-options/).

## Next steps
<a name="_next_steps"></a>
+  [Configure repository access](argocd-configure-repositories.md) - Configure Git repository access
+  [Register target clusters](argocd-register-clusters.md) - Register target clusters for deployment
+  [Create Applications](argocd-create-application.md) - Create your first Application
+  [Argo CD considerations](argocd-considerations.md) - EKS-specific patterns, Identity Center integration, and multi-cluster configuration
+  [Argo CD Documentation](https://argo-cd.readthedocs.io/en/stable/) - Comprehensive Argo CD documentation including sync hooks, health checks, and advanced patterns