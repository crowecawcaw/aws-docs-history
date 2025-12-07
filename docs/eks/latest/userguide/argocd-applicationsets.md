**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Use ApplicationSets

ApplicationSets generate multiple Applications from templates, enabling you to deploy the same application across multiple clusters, environments, or namespaces with a single resource definition.

## Prerequisites

- An EKS cluster with the Argo CD capability created
- Multiple target clusters registered (see [Register target clusters](argocd-register-clusters.md "argocd-register-clusters.md"))
- Repository access configured (see [Configure repository access](argocd-configure-repositories.md "argocd-configure-repositories.md"))
- `kubectl` configured to communicate with your cluster

## How ApplicationSets work

ApplicationSets use generators to produce parameters, then apply those parameters to an Application template.
Each set of generated parameters creates one Application.

Common generators for EKS deployments:

- **List generator** - Explicitly define clusters and parameters for each environment
- **Cluster generator** - Automatically deploy to all registered clusters
- **Git generator** - Generate Applications from repository structure
- **Matrix generator** - Combine generators for multi-dimensional deployments

For complete generator reference, see [ApplicationSet Documentation](https://argo-cd.readthedocs.io/en/stable/user-guide/application-set/ "https://argo-cd.readthedocs.io/en/stable/user-guide/application-set/").

## List generator

Deploy to multiple clusters with explicit configuration:

```
apiVersion: argoproj.io/v1alpha1
kind: ApplicationSet
metadata:
  name: guestbook-all-clusters
  namespace: argocd
spec:
  generators:
  - list:
      elements:
      - cluster: arn:aws:eks:us-west-2:111122223333:cluster/dev-cluster
        environment: dev
        replicas: "2"
      - cluster: arn:aws:eks:us-west-2:111122223333:cluster/staging-cluster
        environment: staging
        replicas: "3"
      - cluster: arn:aws:eks:us-west-2:111122223333:cluster/prod-cluster
        environment: prod
        replicas: "5"
  template:
    metadata:
      name: 'guestbook-{{environment}}'
    spec:
      project: default
      source:
        repoURL: https://github.com/example/guestbook
        targetRevision: HEAD
        path: 'overlays/{{environment}}'
      destination:
        server: '{{cluster}}'
        namespace: guestbook
      syncPolicy:
        automated:
          prune: true
          selfHeal: true
```

###### Note

Use EKS cluster ARNs in the `server` field when targeting registered EKS clusters.
You can also use cluster names with `destination.name` instead of `destination.server`.

This creates three Applications: `guestbook-dev`, `guestbook-staging`, and `guestbook-prod`.

## Cluster generator

Deploy to all registered clusters automatically:

```
apiVersion: argoproj.io/v1alpha1
kind: ApplicationSet
metadata:
  name: cluster-addons
  namespace: argocd
spec:
  generators:
  - clusters: {}
  template:
    metadata:
      name: '{{name}}-addons'
    spec:
      project: default
      source:
        repoURL: https://github.com/example/cluster-addons
        targetRevision: HEAD
        path: addons
      destination:
        server: '{{server}}'
        namespace: kube-system
      syncPolicy:
        automated:
          prune: true
          selfHeal: true
```

This automatically creates an Application for each registered cluster.

**Filter clusters**:

```
spec:
  generators:
  - clusters:
      selector:
        matchLabels:
          environment: production
```

## Git generators

Git generators create Applications based on repository structure:

- **Directory generator** - Deploy each directory as a separate Application (useful for microservices)
- **File generator** - Generate Applications from parameter files (useful for multi-tenant deployments)

**Example: Microservices deployment**

```
apiVersion: argoproj.io/v1alpha1
kind: ApplicationSet
metadata:
  name: microservices
  namespace: argocd
spec:
  generators:
  - git:
      repoURL: https://github.com/example/microservices
      revision: HEAD
      directories:
      - path: services/*
  template:
    metadata:
      name: '{{path.basename}}'
    spec:
      project: default
      source:
        repoURL: https://github.com/example/microservices
        targetRevision: HEAD
        path: '{{path}}'
      destination:
        server: arn:aws:eks:us-west-2:111122223333:cluster/my-cluster
        namespace: '{{path.basename}}'
      syncPolicy:
        automated:
          prune: true
          selfHeal: true
        syncOptions:
        - CreateNamespace=true
```

For details on Git generators and file-based configuration, see [Git Generator](https://argo-cd.readthedocs.io/en/stable/operator-manual/applicationset/Generators-Git/ "https://argo-cd.readthedocs.io/en/stable/operator-manual/applicationset/Generators-Git/") in the Argo CD documentation.

## Matrix generator

Combine multiple generators to deploy across multiple dimensions (environments × clusters):

```
apiVersion: argoproj.io/v1alpha1
kind: ApplicationSet
metadata:
  name: multi-env-multi-cluster
  namespace: argocd
spec:
  generators:
  - matrix:
      generators:
      - list:
          elements:
          - environment: dev
          - environment: staging
          - environment: prod
      - clusters:
          selector:
            matchLabels:
              region: us-west-2
  template:
    metadata:
      name: 'app-{{environment}}-{{name}}'
    spec:
      project: default
      source:
        repoURL: https://github.com/example/app
        targetRevision: HEAD
        path: 'overlays/{{environment}}'
      destination:
        server: '{{server}}'
        namespace: 'app-{{environment}}'
```

For details on combining generators, see [Matrix Generator](https://argo-cd.readthedocs.io/en/stable/operator-manual/applicationset/Generators-Matrix/ "https://argo-cd.readthedocs.io/en/stable/operator-manual/applicationset/Generators-Matrix/") in the Argo CD documentation.

## Progressive rollout

Deploy to environments sequentially with different sync policies:

```
apiVersion: argoproj.io/v1alpha1
kind: ApplicationSet
metadata:
  name: progressive-rollout
  namespace: argocd
spec:
  generators:
  - list:
      elements:
      - environment: dev
        autoSync: "true"
      - environment: staging
        autoSync: "true"
      - environment: prod
        autoSync: "false"
  template:
    metadata:
      name: 'app-{{environment}}'
    spec:
      project: default
      source:
        repoURL: https://github.com/example/app
        targetRevision: HEAD
        path: 'overlays/{{environment}}'
      destination:
        server: arn:aws:eks:us-west-2:111122223333:cluster/{{environment}}-cluster
        namespace: app
      syncPolicy:
        automated:
          prune: true
          selfHeal: '{{autoSync}}'
```

Dev and staging sync automatically, while production requires manual approval.

## Multi-region deployment

Deploy to clusters across multiple regions:

```
apiVersion: argoproj.io/v1alpha1
kind: ApplicationSet
metadata:
  name: global-app
  namespace: argocd
spec:
  generators:
  - list:
      elements:
      - cluster: arn:aws:eks:us-west-2:111122223333:cluster/prod-us-west
        region: us-west-2
      - cluster: arn:aws:eks:us-east-1:111122223333:cluster/prod-us-east
        region: us-east-1
      - cluster: arn:aws:eks:eu-west-1:111122223333:cluster/prod-eu-west
        region: eu-west-1
  template:
    metadata:
      name: 'app-{{region}}'
    spec:
      project: default
      source:
        repoURL: https://github.com/example/app
        targetRevision: HEAD
        path: kubernetes
        helm:
          parameters:
          - name: region
            value: '{{region}}'
      destination:
        server: '{{cluster}}'
        namespace: app
      syncPolicy:
        automated:
          prune: true
          selfHeal: true
```

## Manage ApplicationSets

**View ApplicationSets and generated Applications**:

```
kubectl get applicationsets -n argocd
kubectl get applications -n argocd -l argocd.argoproj.io/application-set-name=<applicationset-name>
```

**Update an ApplicationSet**:

Modify the ApplicationSet spec and reapply.
Argo CD automatically updates all generated Applications:

```
kubectl apply -f applicationset.yaml
```

**Delete an ApplicationSet**:

```
kubectl delete applicationset <name> -n argocd
```

###### Warning

Deleting an ApplicationSet deletes all generated Applications.
If those Applications have `prune: true`, their resources will also be deleted from target clusters.

## Additional resources

- [Working with Argo CD Projects](argocd-projects.md "argocd-projects.md") - Organize ApplicationSets with Projects
- [Create Applications](argocd-create-application.md "argocd-create-application.md") - Understand Application configuration
- [ApplicationSet Documentation](https://argo-cd.readthedocs.io/en/stable/user-guide/application-set/ "https://argo-cd.readthedocs.io/en/stable/user-guide/application-set/") - Complete generator reference and patterns
- [Generator Reference](https://argo-cd.readthedocs.io/en/stable/operator-manual/applicationset/Generators/ "https://argo-cd.readthedocs.io/en/stable/operator-manual/applicationset/Generators/") - Detailed generator specifications
