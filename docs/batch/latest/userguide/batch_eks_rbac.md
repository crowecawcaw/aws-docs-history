# RBAC permissions or bindings aren't configured properly

If you experience any RBAC permissions or binding issues, verify that the
`aws-batch` Kubernetes role can access the Kubernetes namespace:

```
`$` `kubectl get namespace `namespace` --as=aws-batch`
```

```
`$` `kubectl auth can-i get ns --as=aws-batch`
```

You can also use the `kubectl describe` command to view the
authorizations for a cluster role or Kubernetes namespace.

```
`$` `kubectl describe clusterrole `aws-batch-cluster-role``
```

The following is example output.

```
`Name: aws-batch-cluster-role
Labels: <none>
Annotations: <none>
PolicyRule:
 Resources Non-Resource URLs Resource Names Verbs
 --------- ----------------- -------------- -----
 configmaps [] [] [get list watch]
 nodes [] [] [get list watch]
 pods [] [] [get list watch]
 daemonsets.apps [] [] [get list watch]
 deployments.apps [] [] [get list watch]
 replicasets.apps [] [] [get list watch]
 statefulsets.apps [] [] [get list watch]
 clusterrolebindings.rbac.authorization.k8s.io [] [] [get list]
 clusterroles.rbac.authorization.k8s.io [] [] [get list]
 namespaces [] [] [get]
 events [] [] [list]`
```

```
`$` `kubectl describe role `aws-batch-compute-environment-role` -n `my-aws-batch-namespace``
```

The following is example output.

```
`Name: aws-batch-compute-environment-role
Labels: <none>
Annotations: <none>
PolicyRule:
 Resources Non-Resource URLs Resource Names Verbs
 --------- ----------------- -------------- -----
 pods [] [] [create get list watch delete patch]
 serviceaccounts [] [] [get list]
 rolebindings.rbac.authorization.k8s.io [] [] [get list]
 roles.rbac.authorization.k8s.io [] [] [get list]`
```

To resolve this issue, re-apply the RBAC permissions and `rolebinding` commands.
For more information, see [Step 2: Prepare your Amazon EKS cluster for
AWS Batch](getting-started-eks.md#getting-started-eks-step-1 "getting-started-eks.md#getting-started-eks-step-1").
