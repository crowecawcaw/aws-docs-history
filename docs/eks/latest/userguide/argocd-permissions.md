**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Configure Argo CD permissions

The Argo CD managed capability integrates with AWS Identity Center for authentication and uses built-in RBAC roles for authorization.
This topic explains how to configure permissions for users and teams.

## How permissions work with Argo CD

The Argo CD capability uses AWS Identity Center for authentication and provides three built-in RBAC roles for authorization.

When a user accesses Argo CD:

1. They authenticate using AWS Identity Center (which can federate to your corporate identity provider)
2. AWS Identity Center provides user and group information to Argo CD
3. Argo CD maps users and groups to RBAC roles based on your configuration
4. Users see only the applications and resources they have permission to access

## Built-in RBAC roles

The Argo CD capability provides three built-in roles that you map to AWS Identity Center users and groups.

**ADMIN**

Full access to all applications and settings:

- Create, update, and delete applications and ApplicationSets
- Manage Argo CD configuration
- Register and manage deployment target clusters
- Configure repository access
- Manage projects
- View all application status and history
- List and access all clusters and repositories

**EDITOR**

Can create and modify applications but cannot change Argo CD settings:

- Create and update applications and ApplicationSets
- Sync and refresh applications
- View application status and history
- List and access all clusters and repositories
- Cannot delete applications
- Cannot change Argo CD configuration
- Cannot manage clusters or repositories

**VIEWER**

Read-only access to applications:

- View application status and history
- View application manifests and resources
- List all projects (including projects the user is not assigned to)
- Cannot list clusters or repositories
- Cannot make any changes
- Cannot sync or refresh applications

###### Note

The VIEWER role provides limited visibility: users can see all projects but cannot list clusters or repositories.
To grant access to specific applications, assign users to project-specific roles in addition to the global VIEWER role.

## Configure role mappings

Map AWS Identity Center users and groups to Argo CD roles when creating or updating the capability.

**Example role mapping**:

```
 {
  "rbacRoleMapping": {
    "ADMIN": ["AdminGroup", "alice@example.com"],
    "EDITOR": ["DeveloperGroup", "DevOpsTeam"],
    "VIEWER": ["ReadOnlyGroup", "bob@example.com"]
  }
}
```

###### Note

Role names are case-sensitive and must be uppercase (ADMIN, EDITOR, VIEWER).

###### Important

EKS Capabilities integration with AWS Identity Center supports up to 1,000 identities per Argo CD capability.
An identity can be a user or a group.

**Update role mappings**:

```
 aws eksfe update-capability \
  --region <replaceable>us-east-1</replaceable> \
  --cluster-name <replaceable>cluster</replaceable> \
  --capability-name <replaceable>capname</replaceable> \
  --endpoint "https://eks.<replaceable>ap-northeast-2</replaceable>.amazonaws.com" \
  --role-arn "arn:aws:iam::[.replaceable]<literal>111122223333</literal>:role/[.replaceable]`EKSCapabilityRole`" \
  --configuration '{
    "argoCd": {
      "rbacRoleMappings": {
        "addOrUpdateRoleMappings": [
          {
            "role": "ADMIN",
            "identities": [
              { "id": "686103e0-f051-7068-b225-e6392b959d9e", "type": "SSO_USER" }
            ]
          }
        ]
      }
    }
  }'
```

## Admin account usage

The admin account is designed for initial setup and administrative tasks like registering clusters and configuring repositories.

**When admin account is appropriate**:

- Initial capability setup and configuration
- Solo development or quick demonstrations
- Administrative tasks (cluster registration, repository configuration, project creation)

**Best practices for admin account**:

- Don’t commit account tokens to version control
- Rotate tokens immediately if exposed
- Limit account token usage to setup and administrative tasks
- Set short expiration times (maximum 12 hours)
- Only 5 account tokens can be created at any given time

**When to use project-based access instead**:

- Shared development environments with multiple users
- Any environment that resembles production
- When you need audit trails of who performed actions
- When you need to enforce resource restrictions or access boundaries

For production environments and multi-user scenarios, use project-based access control with dedicated RBAC roles mapped to AWS Identity Center groups.

## Project-based access control

Use Argo CD Projects (AppProject) to provide fine-grained access control and resource isolation for teams.

###### Important

Before assigning users or groups to project-specific roles, you must first map them to a global Argo CD role (ADMIN, EDITOR, or VIEWER) in the capability configuration.
Users cannot access Argo CD without a global role mapping, even if they’re assigned to project roles.

Consider mapping users to the VIEWER role globally, then grant additional permissions through project-specific roles.
This provides baseline access while allowing fine-grained control at the project level.

Projects provide:

- **Source restrictions**: Limit which Git repositories can be used
- **Destination restrictions**: Limit which clusters and namespaces can be targeted
- **Resource restrictions**: Limit which Kubernetes resource types can be deployed
- **RBAC integration**: Map projects to AWS Identity Center groups or Argo CD roles

**Example project for team isolation**:

```
 apiVersion: argoproj.io/v1alpha1
kind: AppProject
metadata:
  name: team-a
  namespace: argocd
spec:
  description: Team A applications

  # Required: Specify which namespaces this project watches for Applications
  sourceNamespaces:
  - argocd

  # Source restrictions
  sourceRepos:
  - https://github.com/myorg/team-a-apps

  # Destination restrictions
  destinations:
  - namespace: team-a-*
    server: arn:aws:eks:us-west-2:111122223333:cluster/production

  # Resource restrictions
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

###### Important

The managed capability requires AppProject resources to specify `.spec.sourceNamespaces` to define which namespaces the project can watch for Applications.
Typically, this should be set to the namespace you specified when creating the capability (usually `argocd`).

**Assign users to projects**:

Users with EDITOR or VIEWER roles can be restricted to specific projects.
ADMIN users have access to all projects.

```
 apiVersion: argoproj.io/v1alpha1
kind: AppProject
metadata:
  name: team-a
spec:
  # ... project configuration ...

  sourceNamespaces:
  - argocd

  # Map Identity Center groups or users to project roles
  roles:
  - name: developer
    description: Team A developers
    policies:
    - p, proj:team-a:developer, applications, *, team-a/*, allow
    groups:
    - 686103e0-f051-7068-b225-e6392b959d9e  # Identity Center group ID

  - name: viewer
    description: Team A viewers
    policies:
    - p, proj:team-a:viewer, applications, get, team-a/*, allow
    groups:
    - 786203e0-f051-7068-b225-e6392b959d9f  # Identity Center group ID
    - 886303e0-f051-7068-b225-e6392b959da0  # Identity Center user ID also works
```

###### Note

Use Identity Center group IDs (not group names) in the `groups` field.
You can also use Identity Center user IDs for individual user access.
Find these IDs in the AWS Identity Center console or using the AWS CLI.

## Common permission patterns

**Pattern 1: Admin team with full access**

```
 {
  "rbacRoleMapping": {
    "ADMIN": ["PlatformTeam", "SRETeam"]
  }
}
```

**Pattern 2: Developers can deploy, others can view**

```
 {
  "rbacRoleMapping": {
    "ADMIN": ["PlatformTeam"],
    "EDITOR": ["DevelopmentTeam", "DevOpsTeam"],
    "VIEWER": ["AllEmployees"]
  }
}
```

**Pattern 3: Team-based isolation with projects**

1. Map all developers to EDITOR role
2. Create separate AppProjects for each team
3. Use project roles to restrict access to team-specific applications

```
 {
  "rbacRoleMapping": {
    "ADMIN": ["PlatformTeam"],
    "EDITOR": ["AllDevelopers"]
  }
}
```

Then create projects with team-specific restrictions and role mappings.

## Best practices

**Use groups instead of individual users**: Map AWS Identity Center groups to Argo CD roles rather than individual users for easier management.

**Start with least privilege**: Begin with VIEWER access and grant EDITOR or ADMIN as needed.

**Use projects for team isolation**: Create separate AppProjects for different teams or environments to enforce boundaries.

**Leverage Identity Center federation**: Configure AWS Identity Center to federate with your corporate identity provider for centralized user management.

**Regular access reviews**: Periodically review role mappings and project assignments to ensure appropriate access levels.

**Limit cluster access**: Remember that Argo CD RBAC controls access to Argo CD resources and operations, but does not correspond to Kubernetes RBAC. Users with Argo CD access can deploy applications to clusters that Argo CD has access to. Limit which clusters Argo CD can access and use project destination restrictions to control where applications can be deployed.

## AWS service permissions

To use AWS services directly in Application resources (without creating Repository resources), attach the required IAM permissions to the Capability Role.

**ECR for Helm charts**:

```
 {
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ecr:GetAuthorizationToken",
        "ecr:BatchCheckLayerAvailability",
        "ecr:GetDownloadUrlForLayer",
        "ecr:BatchGetImage"
      ],
      "Resource": "*"
    }
  ]
}
```

**CodeCommit repositories**:

```
 {
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "codecommit:GitPull"
      ],
      "Resource": "arn:aws:codecommit:region:account-id:repository-name"
    }
  ]
}
```

**CodeConnections (GitHub, GitLab, Bitbucket)**:

```
 {
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "codeconnections:UseConnection"
      ],
      "Resource": "arn:aws:codeconnections:region:account-id:connection/connection-id"
    }
  ]
}
```

See [Configure repository access](argocd-configure-repositories.md "argocd-configure-repositories.md") for details on using these integrations.

## Next steps

- [Working with Argo CD](working-with-argocd.md "working-with-argocd.md") - Learn how to create applications and manage deployments
- [Argo CD concepts](argocd-concepts.md "argocd-concepts.md") - Understand Argo CD concepts including Projects
- [Security considerations for EKS Capabilities](capabilities-security.md "capabilities-security.md") - Review security best practices for capabilities
