

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Configure kro permissions
<a name="kro-permissions"></a>

Unlike ACK and Argo CD, kro does not require IAM permissions. kro operates entirely within your Kubernetes cluster and does not make AWS API calls. Control access to kro resources using standard Kubernetes RBAC.

## How permissions work with kro
<a name="_how_permissions_work_with_kro"></a>

kro uses two types of Kubernetes resources with different scopes:

 **ResourceGraphDefinitions**: Cluster-scoped resources that define custom APIs. Typically managed by platform teams who design and maintain organizational standards.

 **Instances**: Namespace-scoped custom resources created from ResourceGraphDefinitions. Can be created by application teams with appropriate RBAC permissions.

By default, the kro capability has permissions to manage ResourceGraphDefinitions and their instances through the `AmazonEKSKROPolicy` access entry policy. However, kro requires additional permissions to create and manage the underlying Kubernetes resources defined in your ResourceGraphDefinitions (such as Deployments, Services, or ACK resources). You must grant these permissions through access entry policies or Kubernetes RBAC. For details on granting these permissions, see [Create a kro capability using eksctl](kro-create-eksctl.md), [Create a kro capability using the AWS CLI](kro-create-cli.md), or [Create a kro capability using the Console](kro-create-console.md).

## Platform team permissions
<a name="_platform_team_permissions"></a>

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
<a name="_application_team_permissions"></a>

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

**Note**  
The API group in the Role (`kro.run` in this example) must match the `apiVersion` defined in your ResourceGraphDefinition’s schema.

## Read-only access
<a name="_read_only_access"></a>

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
<a name="_multi_namespace_access"></a>

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
<a name="_best_practices"></a>

 **Principle of least privilege**: Grant only the minimum permissions needed for each team’s responsibilities.

 **Use groups instead of individual users**: Bind roles to groups rather than individual users for easier management.

 **Separate platform and application concerns**: Platform teams manage ResourceGraphDefinitions, application teams manage instances.

 **Namespace isolation**: Use namespaces to isolate different teams or environments, with RBAC controlling access to each namespace.

 **Read-only access for auditing**: Provide read-only access to security and compliance teams for auditing purposes.

## Next steps
<a name="_next_steps"></a>
+  [kro concepts](kro-concepts.md) - Understand kro concepts and resource composition
+  [Security considerations for EKS Capabilities](capabilities-security.md) - Review security best practices for capabilities