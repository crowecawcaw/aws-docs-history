**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Create Applications

Applications represent deployments in target clusters.
Each Application defines a source (Git repository) and destination (cluster and namespace).
When applied, Argo CD will create the resources specified by manifests in the Git repository to the namespace in the cluster.
Applications often specify workload deployments, but they can manage any Kubernetes resources available in the destination cluster.

## Prerequisites

- An EKS cluster with the Argo CD capability created
- Repository access configured (see [Configure repository access](argocd-configure-repositories.md "argocd-configure-repositories.md"))
- Target cluster registered (see [Register target clusters](argocd-register-clusters.md "argocd-register-clusters.md"))
- `kubectl` configured to communicate with your cluster

## Create a basic Application

Define an Application that deploys from a Git repository:

```
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: guestbook
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/argoproj/argocd-example-apps
    targetRevision: HEAD
    path: guestbook
  destination:
    name: in-cluster
    namespace: default
```

###### Note

Use `destination.name` with the cluster name you used when registering the cluster (like `in-cluster` for the local cluster).
The `destination.server` field also works with EKS cluster ARNs, but using cluster names is recommended for better readability.

Apply the Application:

```
kubectl apply -f application.yaml
```

View the Application status:

```
kubectl get application guestbook -n argocd
```

## Source configuration

**Git repository**:

```
spec:
  source:
    repoURL: https://github.com/example/my-app
    targetRevision: main
    path: kubernetes/manifests
```

**Specific Git tag or commit**:

```
spec:
  source:
    targetRevision: v1.2.0  # or commit SHA
```

**Helm chart**:

```
spec:
  source:
    repoURL: https://github.com/example/helm-charts
    targetRevision: main
    path: charts/my-app
    helm:
      valueFiles:
      - values.yaml
      parameters:
      - name: image.tag
        value: v1.2.0
```

**Helm chart with values from external Git repository** (multi-source pattern):

```
spec:
  sources:
  - repoURL: https://github.com/example/helm-charts
    targetRevision: main
    path: charts/my-app
    helm:
      valueFiles:
      - $values/environments/production/values.yaml
  - repoURL: https://github.com/example/config-repo
    targetRevision: main
    ref: values
```

For more information, see [Helm Value Files from External Git Repository](https://argo-cd.readthedocs.io/en/stable/user-guide/multiple_sources/#helm-value-files-from-external-git-repository "https://argo-cd.readthedocs.io/en/stable/user-guide/multiple_sources/#helm-value-files-from-external-git-repository") in the Argo CD documentation.

**Helm chart from ECR**:

```
spec:
  source:
    repoURL: oci://`account-id`.dkr.ecr.`region`.amazonaws.com/`repository-name`
    targetRevision: `chart-version`
    chart: `chart-name`

```

If the Capability Role has the required ECR permissions, the repository is used directly and no Repository configuration is required.
See [Configure repository access](argocd-configure-repositories.md "argocd-configure-repositories.md") for details.

**Git repository from CodeCommit**:

```
spec:
  source:
    repoURL: https://git-codecommit.`region`.amazonaws.com/v1/repos/`repository-name`
    targetRevision: main
    path: kubernetes/manifests
```

If the Capability Role has the required CodeCommit permissions, the repository is used directly and no Repository configuration is required.
See [Configure repository access](argocd-configure-repositories.md "argocd-configure-repositories.md") for details.

**Git repository from CodeConnections**:

```
spec:
  source:
    repoURL: https://codeconnections.`region`.amazonaws.com/git-http/`account-id`/`region`/`connection-id`/`owner`/`repository`.git
    targetRevision: main
    path: kubernetes/manifests
```

The repository URL format is derived from the CodeConnections connection ARN.
If the Capability Role has the required CodeConnections permissions and a connection is configured, the repository is used directly and no Repository configuration is required.
See [Configure repository access](argocd-configure-repositories.md "argocd-configure-repositories.md") for details.

**Kustomize**:

```
spec:
  source:
    repoURL: https://github.com/example/kustomize-app
    targetRevision: main
    path: overlays/production
    kustomize:
      namePrefix: prod-
```

## Sync policies

Control how Argo CD syncs applications.

**Manual sync (default)**:

Applications require manual approval to sync:

```
spec:
  syncPolicy: {}  # No automated sync
```

Manually trigger sync:

```
kubectl patch application guestbook -n argocd \
  --type merge \
  --patch '{"operation": {"initiatedBy": {"username": "admin"}, "sync": {}}}'
```

**Automatic sync**:

Applications automatically sync when Git changes are detected:

```
spec:
  syncPolicy:
    automated: {}
```

**Self-healing**:

Automatically revert manual changes to the cluster:

```
spec:
  syncPolicy:
    automated:
      selfHeal: true
```

When enabled, Argo CD reverts any manual changes made directly to the cluster, ensuring Git remains the source of truth.

**Pruning**:

Automatically delete resources removed from Git:

```
spec:
  syncPolicy:
    automated:
      prune: true
```

###### Warning

Pruning will delete resources from your cluster.
Use with caution in production environments.

**Combined automated sync**:

```
spec:
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
    syncOptions:
    - CreateNamespace=true
```

**Retry configuration**:

Configure retry behavior for failed syncs:

```
spec:
  syncPolicy:
    retry:
      limit: 5  # Number of failed sync attempts; unlimited if less than 0
      backoff:
        duration: 5s  # Amount to back off (default unit: seconds, also supports "2m", "1h")
        factor: 2  # Factor to multiply the base duration after each failed retry
        maxDuration: 3m  # Maximum amount of time allowed for the backoff strategy
```

This is particularly useful for resources that depend on CRDs being created first, or when working with kro instances where the CRD may not be immediately available.

## Sync options

Additional sync configuration:

**Create namespace if it doesn’t exist**:

```
spec:
  syncPolicy:
    syncOptions:
    - CreateNamespace=true
```

**Skip dry run for missing resources**:

Useful when applying resources that depend on CRDs that don’t exist yet (like kro instances):

```
spec:
  syncPolicy:
    syncOptions:
    - SkipDryRunOnMissingResource=true
```

This can also be applied to specific resources using a label on the resource itself.

**Validate resources before applying**:

```
spec:
  syncPolicy:
    syncOptions:
    - Validate=true
```

**Apply out of sync only**:

```
spec:
  syncPolicy:
    syncOptions:
    - ApplyOutOfSyncOnly=true
```

## Advanced sync features

Argo CD supports advanced sync features for complex deployments:

- **Sync waves** - Control resource creation order with `argocd.argoproj.io/sync-wave` annotations
- **Sync hooks** - Run jobs before or after sync with `argocd.argoproj.io/hook` annotations (PreSync, PostSync, SyncFail)
- **Resource health assessment** - Custom health checks for application-specific resources

For details, see [Sync Waves](https://argo-cd.readthedocs.io/en/stable/user-guide/sync-waves/ "https://argo-cd.readthedocs.io/en/stable/user-guide/sync-waves/") and [Resource Hooks](https://argo-cd.readthedocs.io/en/stable/user-guide/resource_hooks/ "https://argo-cd.readthedocs.io/en/stable/user-guide/resource_hooks/") in the Argo CD documentation.

## Ignore differences

Prevent Argo CD from syncing specific fields that are managed by other controllers (like HPA managing replicas):

```
spec:
  ignoreDifferences:
  - group: apps
    kind: Deployment
    jsonPointers:
    - /spec/replicas
```

For details on ignore patterns and field exclusions, see [Diffing Customization](https://argo-cd.readthedocs.io/en/stable/user-guide/diffing/ "https://argo-cd.readthedocs.io/en/stable/user-guide/diffing/") in the Argo CD documentation.

## Multi-environment deployment

Deploy the same application to multiple environments:

**Development**:

```
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: my-app-dev
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/example/my-app
    targetRevision: develop
    path: overlays/development
  destination:
    name: dev-cluster
    namespace: my-app
```

**Production**:

```
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: my-app-prod
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/example/my-app
    targetRevision: main
    path: overlays/production
  destination:
    name: prod-cluster
    namespace: my-app
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
```

## Monitor and manage Applications

**View Application status**:

```
kubectl get application my-app -n argocd
```

**Access the Argo CD UI**:

Open the Argo CD UI through the EKS console to view application topology, sync status, resource health, and deployment history.
See [Working with Argo CD](working-with-argocd.md "working-with-argocd.md") for UI access instructions.

**Rollback Applications**:

Rollback to a previous revision using the Argo CD UI, the Argo CD CLI, or by updating the `targetRevision` in the Application spec to a previous Git commit or tag.

Using the Argo CD CLI:

```
argocd app rollback argocd/my-app <revision-id>
```

###### Note

When using the Argo CD CLI with the managed capability, specify applications with the namespace prefix: `namespace/appname`.

For more information, see [argocd app rollback](https://argo-cd.readthedocs.io/en/stable/user-guide/commands/argocd_app_rollback/ "https://argo-cd.readthedocs.io/en/stable/user-guide/commands/argocd_app_rollback/") in the Argo CD documentation.

## Additional resources

- [Working with Argo CD Projects](argocd-projects.md "argocd-projects.md") - Organize applications with Projects for multi-tenant environments
- [Use ApplicationSets](argocd-applicationsets.md "argocd-applicationsets.md") - Deploy to multiple clusters with templates
- [Application Specification](https://argo-cd.readthedocs.io/en/stable/user-guide/application-specification/ "https://argo-cd.readthedocs.io/en/stable/user-guide/application-specification/") - Complete Application API reference
- [Sync Options](https://argo-cd.readthedocs.io/en/stable/user-guide/sync-options/ "https://argo-cd.readthedocs.io/en/stable/user-guide/sync-options/") - Advanced sync configuration
