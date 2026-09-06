

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Grant the EKS Auto Mode load balancer controller access to a specific Secret
<a name="auto-managed-rbac-example"></a>

In this tutorial, you grant the Amazon EKS Auto Mode load balancer controller read access to a specific Kubernetes `Secret`. This unblocks OIDC authentication on an ALB `Ingress`. You use a namespace-scoped `Role` and `RoleBinding` targeted at the `eks:managed` group.

This tutorial takes approximately 15 minutes to complete. The Kubernetes RBAC objects you create do not incur AWS charges.

The Amazon EKS Auto Mode load balancer controller supports OIDC authentication on ALB `Ingress` objects. It uses the `alb.ingress.kubernetes.io/auth-type: oidc` annotation to enable this authentication. To resolve the OIDC configuration, the controller reads a Kubernetes `Secret` named in the `alb.ingress.kubernetes.io/auth-idp-oidc` annotation. Its managed access policy does not currently grant `get` on `Secret` objects, so the reconciler fails with a message similar to:

```
Failed build model due to ingress: <ns>/<name>:
  secrets "<secret>" is forbidden:
  User "arn:aws:sts::<acct>:assumed-role/AWSServiceRoleForAmazonEKS/<session>"
  cannot get resource "secrets" in API group "" in the namespace "<ns>"
```

Using the mechanism described in [Grant additional Kubernetes RBAC to EKS Auto Mode managed controllers](auto-managed-rbac.md), you can grant the managed controller `get` on exactly the OIDC `Secret` it needs.

## Prerequisites
<a name="_prerequisites"></a>

Before you begin, make sure you have:
+ An Amazon EKS Auto Mode cluster with the auto-created `AWSServiceRoleForAmazonEKS` access entry.
+  `kubectl` configured with cluster access.
+ The AWS CLI installed and configured with permissions for `aws sts get-caller-identity` and `aws eks describe-access-entry`.
+ An ALB `Ingress` that uses the `alb.ingress.kubernetes.io/auth-type: oidc` annotation, and the Kubernetes `Secret` it references.

## Step 1: Identify the Secret to add to the allow list
<a name="_step_1_identify_the_secret_to_add_to_the_allow_list"></a>

The OIDC configuration on an ALB `Ingress` looks like the following. Record the `Secret` name and the `Ingress` namespace — the RBAC objects must live in the same namespace as the `Secret`.

```
annotations:
  alb.ingress.kubernetes.io/auth-type: oidc
  alb.ingress.kubernetes.io/auth-idp-oidc: >
    {
      "issuer": "...",
      "authorizationEndpoint": "...",
      "tokenEndpoint": "...",
      "userInfoEndpoint": "...",
      "secretName": "oidc"
    }
```

The rest of this example uses namespace `monitoring` and `Secret` name `oidc`.

## Step 2: Apply a namespace-scoped Role and RoleBinding
<a name="_step_2_apply_a_namespace_scoped_role_and_rolebinding"></a>

This form grants exactly `get` on exactly the named `Secret` in exactly one namespace. Save the following as `eks-managed-oidc-secret-reader.yaml`:

```
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: eks-managed-oidc-secret-reader
  namespace: monitoring
rules:
- apiGroups: [""]
  resources: ["secrets"]
  resourceNames: ["oidc"]
  verbs: ["get"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: eks-managed-oidc-secret-reader
  namespace: monitoring
subjects:
- kind: Group
  name: eks:managed
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role
  name: eks-managed-oidc-secret-reader
  apiGroup: rbac.authorization.k8s.io
```

Apply it:

```
kubectl apply -f eks-managed-oidc-secret-reader.yaml
```

To add more `Secret` objects to the allow list later, append their names to the `Role’s `resourceNames` list and re-apply.

## Step 3: Confirm the Ingress recovers
<a name="_step_3_confirm_the_ingress_recovers"></a>

The load balancer controller re-reconciles the `Ingress` on its next pass (typically within a few minutes). When the grant is working, the previous `secrets "oidc" is forbidden` error stops appearing on the `Ingress` and the load balancer progresses. If the error persists, re-check the `Role’s `namespace`, `resourceNames`, and the `RoleBinding` subject.

## Removing the grant
<a name="_removing_the_grant"></a>

**Important**  
Keep the `Role` and `RoleBinding` in place for as long as the ALB `Ingress` uses `alb.ingress.kubernetes.io/auth-type: oidc`. Removing them re-breaks OIDC resolution on the `Ingress`.

If you stop using OIDC on the `Ingress`, remove the grant:

```
kubectl delete rolebinding eks-managed-oidc-secret-reader -n monitoring
kubectl delete role        eks-managed-oidc-secret-reader -n monitoring
```

## Related resources
<a name="_related_resources"></a>
+  [Grant additional Kubernetes RBAC to EKS Auto Mode managed controllers](auto-managed-rbac.md) — Conceptual overview of the `eks:managed` group and how to scope grants.
+  [Grant IAM users access to Kubernetes with EKS access entries](access-entries.md) — Amazon EKS access entries.
+  [Using RBAC Authorization](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) in the Kubernetes documentation.