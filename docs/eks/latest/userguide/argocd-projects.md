

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Working with Argo CD Projects
<a name="argocd-projects"></a>

Argo CD Projects (AppProject) provide logical grouping and access control for Applications. Projects define which Git repositories, target clusters, and namespaces Applications can use, enabling multi-tenancy and security boundaries in shared Argo CD instances.

## When to use projects
<a name="_when_to_use_projects"></a>

Use Projects to:
+ Separate applications by team, environment, or business unit
+ Restrict which repositories teams can deploy from
+ Limit which clusters and namespaces teams can deploy to
+ Enforce resource quotas and allowed resource types
+ Provide self-service application deployment with guardrails

## Default project
<a name="_default_project"></a>

Every Argo CD capability includes a `default` project that allows access to all repositories, clusters, and namespaces. While useful for initial testing, create dedicated projects with explicit restrictions for production use.

For details on the default project configuration and how to restrict it, see [The Default Project](https://argo-cd.readthedocs.io/en/stable/user-guide/projects/#the-default-project) in the Argo CD documentation.

## Create a project
<a name="_create_a_project"></a>

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


  # Source namespaces (required for EKS capability)
  sourceNamespaces:
    - argocd
    - team-a-dev
    - team-a-prod

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
<a name="_project_configuration"></a>

### Source repositories
<a name="_source_repositories"></a>

Control which Git repositories Applications in this project can use:

```
spec:
  sourceRepos:
    - 'https://github.com/my-org/app-*'  # Wildcard pattern
    - 'https://github.com/my-org/infra'  # Specific repo
```

You can use wildcards and negation patterns (`!` prefix) to allow or deny specific repositories. For details, see [Managing Projects](https://argo-cd.readthedocs.io/en/stable/user-guide/projects/#managing-projects) in the Argo CD documentation.

### Source namespaces
<a name="_source_namespaces"></a>

When using the EKS Argo CD capability, the `spec.sourceNamespaces` field is **required** in your custom AppProject definition. This field specifies which namespaces can contain Applications or ApplicationSets that reference this project:

**Important**  
This is a required field for EKS Argo CD capability, which differs from OSS Argo CD where this field is optional.

#### Default AppProject behavior
<a name="_default_appproject_behavior"></a>

The `default` AppProject automatically includes the `argocd` namespace in `sourceNamespaces`. If you need to create Applications or ApplicationSets in additional namespaces, modify the `sourceNamespaces` field to add those namespaces:

```
apiVersion: argoproj.io/v1alpha1
kind: AppProject
metadata:
  name: default
  namespace: argocd
spec:
  sourceNamespaces:
    - argocd           # Already included by default
    - team-a-apps      # Add additional namespaces as needed
    - team-b-apps
```

#### Custom AppProject configuration
<a name="_custom_appproject_configuration"></a>

When creating a custom AppProject, you must manually include the `argocd` system namespace and any other namespaces where you plan to create Applications or ApplicationSets:

```
apiVersion: argoproj.io/v1alpha1
kind: AppProject
metadata:
  name: team-a-project
  namespace: argocd
spec:
  description: Applications for Team A

  # Required: Manually specify all namespaces
  sourceNamespaces:
    - argocd           # ArgoCD system namespace (required)
    - team-a-dev       # Custom namespace for dev Applications
    - team-a-prod      # Custom namespace for prod Applications

  # Source repositories this project can deploy from
  sourceRepos:
    - 'https://github.com/my-org/team-a-*'

  # Destination restrictions
  destinations:
    - namespace: 'team-a-*'
      server: arn:aws:eks:us-west-2:111122223333:cluster/my-cluster  # Use cluster ARN from: aws eks describe-cluster
```

**Note**  
If you omit a namespace from `sourceNamespaces`, Applications or ApplicationSets created in that namespace will not be able to reference this project, resulting in deployment failures.

### Destination restrictions
<a name="_destination_restrictions"></a>

Limit where Applications can deploy:

```
spec:
  destinations:
    - name: prod-cluster  # Specific cluster by name
      namespace: production
    - name: '*'  # Any cluster
      namespace: team-a-*  # Namespace pattern
```

**Important**  
Use specific cluster names and namespace patterns rather than wildcards for production Projects. This prevents accidental deployments to unauthorized clusters or namespaces.

You can use wildcards and negation patterns to control destinations. For details, see [Managing Projects](https://argo-cd.readthedocs.io/en/stable/user-guide/projects/#managing-projects) in the Argo CD documentation.

### Resource restrictions
<a name="_resource_restrictions"></a>

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

## Assign applications to projects
<a name="_assign_applications_to_projects"></a>

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
<a name="_project_roles_and_rbac"></a>

Projects can define custom roles for fine-grained access control. Map project roles to AWS Identity Center users and groups in your capability configuration to control who can sync, update, or delete applications.

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

For details on project roles, JWT tokens for CI/CD pipelines, and RBAC configuration, see [Project Roles](https://argo-cd.readthedocs.io/en/stable/user-guide/projects/#project-roles) in the Argo CD documentation.

## Common patterns
<a name="_common_patterns"></a>

### Environment-based Projects
<a name="_environment_based_projects"></a>

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
<a name="_team_based_projects"></a>

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
<a name="_multi_cluster_projects"></a>

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
<a name="_best_practices"></a>

 **Start with restrictive Projects**: Begin with narrow permissions and expand as needed rather than starting with broad access.

 **Use namespace patterns**: Leverage wildcards in namespace restrictions (like `team-a-*`) to allow flexibility while maintaining boundaries.

 **Separate production Projects**: Use dedicated Projects for production with stricter controls and manual sync policies.

 **Document Project purposes**: Use the `description` field to explain what each Project is for and who should use it.

 **Review Project permissions regularly**: Audit Projects periodically to ensure restrictions still align with team needs and security requirements.

## Additional resources
<a name="_additional_resources"></a>
+  [Configure Argo CD permissions](argocd-permissions.md) - Configure RBAC and Identity Center integration
+  [Create Applications](argocd-create-application.md) - Create Applications within Projects
+  [Use ApplicationSets](argocd-applicationsets.md) - Use ApplicationSets with Projects for multi-cluster deployments
+  [Argo CD Projects Documentation](https://argo-cd.readthedocs.io/en/stable/user-guide/projects/) - Complete upstream reference