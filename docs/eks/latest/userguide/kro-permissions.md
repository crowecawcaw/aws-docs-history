**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Configure kro permissions

Unlike ACK and Argo CD, kro does not require IAM permissions.
kro operates entirely within your Kubernetes cluster and does not make AWS API calls.
Control access to kro resources using standard Kubernetes RBAC.

## How permissions work with kro

kro uses two types of Kubernetes resources with different scopes:

**ResourceGraphDefinitions**: Cluster-scoped resources that define custom APIs.
Typically managed by platform teams who design and maintain organizational standards.

**Instances**: Namespace-scoped custom resources created from ResourceGraphDefinitions.
Can be created by application teams with appropriate RBAC permissions.

By default, the kro capability has permissions to manage ResourceGraphDefinitions and their instances through the `AmazonEKSKROPolicy` access entry policy.
However, kro requires additional permissions to create and manage the underlying Kubernetes resources defined in your ResourceGraphDefinitions (such as Deployments, Services, or ACK resources).
You must grant these permissions through access entry policies or Kubernetes RBAC.
For details on granting these permissions, see [kro arbitrary resource permissions](capabilities-security.md#kro-resource-permissions "capabilities-security.md#kro-resource-permissions").

## Platform team permissions

Platform teams need permissions to create and manage ResourceGraphDefinitions.

**Example ClusterRole for platform teams**:

```
 apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: kro-platform-admin
rules:
- apiGroups: ["kro.run"]
  resources: ["resourcegraphdefinitions"]
  verbs: ["*"]
```

**Bind to platform team members**:

```
 apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: platform-team-kro-admin
subjects:
- kind: Group
  name: platform-team
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: kro-platform-admin
  apiGroup: rbac.authorization.k8s.io
```

## Application team permissions

Application teams need permissions to create instances of custom resources in their namespaces.

**Example Role for application teams**:

```
 apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: kro-app-developer
  namespace: my-app
rules:
- apiGroups: ["kro.run"]
  resources: ["webapps", "databases"]
  verbs: ["create", "get", "list", "update", "delete", "patch"]
```

**Bind to application team members**:

```
 apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: app-team-kro-developer
  namespace: my-app
subjects:
- kind: Group
  name: app-team
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role
  name: kro-app-developer
  apiGroup: rbac.authorization.k8s.io
```

###### Note

The API group in the Role (`kro.run` in this example) must match the `apiVersion` defined in your ResourceGraphDefinition’s schema.

## Read-only access

Grant read-only access to view ResourceGraphDefinitions and instances without modification permissions.

**Read-only ClusterRole**:

```
 apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: kro-viewer
rules:
- apiGroups: ["kro.run"]
  resources: ["resourcegraphdefinitions"]
  verbs: ["get", "list", "watch"]
```

**Read-only Role for instances**:

```
 apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: kro-instance-viewer
  namespace: my-app
rules:
- apiGroups: ["kro.run"]
  resources: ["webapps", "databases"]
  verbs: ["get", "list", "watch"]
```

## Multi-namespace access

Grant application teams access to multiple namespaces using ClusterRoles with RoleBindings.

**ClusterRole for multi-namespace access**:

```
 apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: kro-multi-namespace-developer
rules:
- apiGroups: ["kro.run"]
  resources: ["webapps"]
  verbs: ["create", "get", "list", "update", "delete"]
```

**Bind to specific namespaces**:

```
 apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: app-team-dev-access
  namespace: development
subjects:
- kind: Group
  name: app-team
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: kro-multi-namespace-developer
  apiGroup: rbac.authorization.k8s.io
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: app-team-staging-access
  namespace: staging
subjects:
- kind: Group
  name: app-team
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: kro-multi-namespace-developer
  apiGroup: rbac.authorization.k8s.io
```

## Best practices

**Principle of least privilege**: Grant only the minimum permissions needed for each team’s responsibilities.

**Use groups instead of individual users**: Bind roles to groups rather than individual users for easier management.

**Separate platform and application concerns**: Platform teams manage ResourceGraphDefinitions, application teams manage instances.

**Namespace isolation**: Use namespaces to isolate different teams or environments, with RBAC controlling access to each namespace.

**Read-only access for auditing**: Provide read-only access to security and compliance teams for auditing purposes.

## Next steps

- [kro concepts](kro-concepts.md "kro-concepts.md") - Understand kro concepts and resource composition
- [kro concepts](kro-concepts.md "kro-concepts.md") - Understand SimpleSchema, CEL expressions, and composition patterns
- [Security considerations for EKS Capabilities](capabilities-security.md "capabilities-security.md") - Review security best practices for capabilities
