**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Working with Argo CD Projects

Argo CD Projects (AppProject) provide logical grouping and access control for Applications.
Projects define which Git repositories, target clusters, and namespaces Applications can use, enabling multi-tenancy and security boundaries in shared Argo CD instances.

## When to use Projects

Use Projects to:

- Separate applications by team, environment, or business unit
- Restrict which repositories teams can deploy from
- Limit which clusters and namespaces teams can deploy to
- Enforce resource quotas and allowed resource types
- Provide self-service application deployment with guardrails

## Default Project

Every Argo CD capability includes a `default` project that allows access to all repositories, clusters, and namespaces.
While useful for initial testing, create dedicated projects with explicit restrictions for production use.

For details on the default project configuration and how to restrict it, see [The Default Project](https://argo-cd.readthedocs.io/en/stable/user-guide/projects/#the-default-project "https://argo-cd.readthedocs.io/en/stable/user-guide/projects/#the-default-project") in the Argo CD documentation.

## Create a Project

Create a Project by applying an `AppProject` resource to your cluster.

**Example: Team-specific Project**

```
 apiVersion: argoproj.io/v1alpha1
kind: AppProject
metadata:
  name: team-a
  namespace: argocd
spec:
  description: Applications for Team A

  # Source repositories this project can deploy from
  sourceRepos:
    - 'https://github.com/my-org/team-a-*'
    - 'https://github.com/my-org/shared-libs'

  # Destination clusters and namespaces
  destinations:
    - name: dev-cluster
      namespace: team-a-dev
    - name: prod-cluster
      namespace: team-a-prod

  # Allowed resource types
  clusterResourceWhitelist:
    - group: ''
      kind: Namespace

  namespaceResourceWhitelist:
    - group: 'apps'
      kind: Deployment
    - group: ''
      kind: Service
    - group: ''
      kind: ConfigMap
```

Apply the Project:

```
 kubectl apply -f team-a-project.yaml
```

## Project configuration

### Source repositories

Control which Git repositories Applications in this project can use:

```
 spec:
  sourceRepos:
    - 'https://github.com/my-org/app-*'  # Wildcard pattern
    - 'https://github.com/my-org/infra'  # Specific repo
```

You can use wildcards and negation patterns (`!` prefix) to allow or deny specific repositories.
For details, see [Managing Projects](https://argo-cd.readthedocs.io/en/stable/user-guide/projects/#managing-projects "https://argo-cd.readthedocs.io/en/stable/user-guide/projects/#managing-projects") in the Argo CD documentation.

### Destination restrictions

Limit where Applications can deploy:

```
 spec:
  destinations:
    - name: prod-cluster  # Specific cluster by name
      namespace: production
    - name: '*'  # Any cluster
      namespace: team-a-*  # Namespace pattern
```

###### Important

Use specific cluster names and namespace patterns rather than wildcards for production Projects.
This prevents accidental deployments to unauthorized clusters or namespaces.

You can use wildcards and negation patterns to control destinations.
For details, see [Managing Projects](https://argo-cd.readthedocs.io/en/stable/user-guide/projects/#managing-projects "https://argo-cd.readthedocs.io/en/stable/user-guide/projects/#managing-projects") in the Argo CD documentation.

### Resource restrictions

Control which Kubernetes resource types can be deployed:

**Cluster-scoped resources**:

```
 spec:
  clusterResourceWhitelist:
    - group: ''
      kind: Namespace
    - group: 'rbac.authorization.k8s.io'
      kind: Role
```

**Namespace-scoped resources**:

```
 spec:
  namespaceResourceWhitelist:
    - group: 'apps'
      kind: Deployment
    - group: ''
      kind: Service
    - group: ''
      kind: ConfigMap
    - group: 's3.services.k8s.aws'
      kind: Bucket
```

Use blacklists to deny specific resources:

```
 spec:
  namespaceResourceBlacklist:
    - group: ''
      kind: Secret  # Prevent direct Secret creation
```

## Assign Applications to Projects

When creating an Application, specify the project in the `spec.project` field:

```
 apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: my-app
  namespace: argocd
spec:
  project: team-a  # Assign to team-a project
  source:
    repoURL: https://github.com/my-org/my-app
    path: manifests
  destination:
    name: prod-cluster
    namespace: team-a-prod
```

Applications without a specified project use the `default` project.

## Project roles and RBAC

Projects can define custom roles for fine-grained access control.
Map project roles to AWS Identity Center users and groups in your capability configuration to control who can sync, update, or delete applications.

**Example: Project with developer and admin roles**

```
 apiVersion: argoproj.io/v1alpha1
kind: AppProject
metadata:
  name: team-a
  namespace: argocd
spec:
  sourceRepos:
    - '*'
  destinations:
    - name: '*'
      namespace: 'team-a-*'

  roles:
    - name: developer
      description: Developers can sync applications
      policies:
        - p, proj:team-a:developer, applications, sync, team-a/*, allow
        - p, proj:team-a:developer, applications, get, team-a/*, allow
      groups:
        - team-a-developers

    - name: admin
      description: Admins have full access
      policies:
        - p, proj:team-a:admin, applications, *, team-a/*, allow
      groups:
        - team-a-admins
```

For details on project roles, JWT tokens for CI/CD pipelines, and RBAC configuration, see [Project Roles](https://argo-cd.readthedocs.io/en/stable/user-guide/projects/#project-roles "https://argo-cd.readthedocs.io/en/stable/user-guide/projects/#project-roles") in the Argo CD documentation.

## Common patterns

### Environment-based Projects

Create separate projects for each environment:

```
 apiVersion: argoproj.io/v1alpha1
kind: AppProject
metadata:
  name: production
  namespace: argocd
spec:
  sourceRepos:
    - 'https://github.com/my-org/*'
  destinations:
    - name: prod-cluster
      namespace: '*'
  # Strict resource controls for production
  clusterResourceWhitelist: []
  namespaceResourceWhitelist:
    - group: 'apps'
      kind: Deployment
    - group: ''
      kind: Service
```

### Team-based Projects

Isolate teams with dedicated projects:

```
 apiVersion: argoproj.io/v1alpha1
kind: AppProject
metadata:
  name: platform-team
  namespace: argocd
spec:
  sourceRepos:
    - 'https://github.com/my-org/platform-*'
  destinations:
    - name: '*'
      namespace: 'platform-*'
  # Platform team can manage cluster resources
  clusterResourceWhitelist:
    - group: '*'
      kind: '*'
```

### Multi-cluster Projects

Deploy to multiple clusters with consistent policies:

```
 apiVersion: argoproj.io/v1alpha1
kind: AppProject
metadata:
  name: global-app
  namespace: argocd
spec:
  sourceRepos:
    - 'https://github.com/my-org/global-app'
  destinations:
    - name: us-west-cluster
      namespace: app
    - name: eu-west-cluster
      namespace: app
    - name: ap-south-cluster
      namespace: app
```

## Best practices

**Start with restrictive Projects**: Begin with narrow permissions and expand as needed rather than starting with broad access.

**Use namespace patterns**: Leverage wildcards in namespace restrictions (like `team-a-*`) to allow flexibility while maintaining boundaries.

**Separate production Projects**: Use dedicated Projects for production with stricter controls and manual sync policies.

**Document Project purposes**: Use the `description` field to explain what each Project is for and who should use it.

**Review Project permissions regularly**: Audit Projects periodically to ensure restrictions still align with team needs and security requirements.

## Additional resources

- [Configure Argo CD permissions](argocd-permissions.md "argocd-permissions.md") - Configure RBAC and Identity Center integration
- [Create Applications](argocd-create-application.md "argocd-create-application.md") - Create Applications within Projects
- [Use ApplicationSets](argocd-applicationsets.md "argocd-applicationsets.md") - Use ApplicationSets with Projects for multi-cluster deployments
- [Argo CD Projects Documentation](https://argo-cd.readthedocs.io/en/stable/user-guide/projects/ "https://argo-cd.readthedocs.io/en/stable/user-guide/projects/") - Complete upstream reference
