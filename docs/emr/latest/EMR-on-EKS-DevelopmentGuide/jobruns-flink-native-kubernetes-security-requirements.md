# Flink JobManager service

account security requirements for Native Kubernetes

The Flink JobManager pod uses a Kubernetes service account to access the Kubernetes API server to create and watch TaskManager pods.
The JobManager service account must have appropriate permissions to create/delete TaskManager pods and allow the
TaskManager to watch leader ConfigMaps to retrieve the address of JobManager and ResourceManager in your cluster.

The following rules apply to this service account.

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
  - "apps"
  resources:
  - deployments
  verbs:
  - "*"
```
