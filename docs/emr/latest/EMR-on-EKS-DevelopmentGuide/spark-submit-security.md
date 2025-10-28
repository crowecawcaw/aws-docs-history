# Verify Spark driver service account security requirements

for spark-submit

The Spark driver pod uses a Kubernetes service account to access the Kubernetes API
server to create and watch executor pods. Driver service account must have appropriate
permissions to list, create, edit, patch and delete pods in your cluster. You can verify
that you can list these resources by running the following command:

```
kubectl auth can-i `list|create|edit|delete|patch` pods
```

Verify that you have the necessary permissions by running each command.

```
kubectl auth can-i list pods
kubectl auth can-i create pods
kubectl auth can-i edit pods
kubectl auth can-i delete pods
kubectl auth can-i patch pods
```

The following rules apply to this service role:

```
 rules:
- apiGroups:
  - ""
  resources:
  - pods
  verbs:
  - "*"
- apiGroups:
  - ""
  resources:
  - services
  verbs:
  - "*"
- apiGroups:
  - ""
  resources:
  - configmaps
  verbs:
  - "*"
- apiGroups:
  - ""
  resources:
  - persistentvolumeclaims
  verbs:
  - "*"
```
