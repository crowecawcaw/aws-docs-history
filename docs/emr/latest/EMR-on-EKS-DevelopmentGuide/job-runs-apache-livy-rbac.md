# Setting up the Apache Livy and Spark application permissions with role-based access control (RBAC)

To deploy Livy, Amazon EMR on EKS creates a server service account and role and a Spark service
account and role. These roles must have the necessary RBAC permissions to finish setup and run Spark applications.

**RBAC permissions for the server service account and role**

Amazon EMR on EKS creates the Livy server service account and role to manage Livy sessions for Spark jobs and routing
traffic to and from the ingress and other resources.

The default name for this service account is `emr-containers-sa-livy`. It must have the following permissions.

```
rules:
- apiGroups:
  - ""
  resources:
  - "namespaces"
  verbs:
  - "get"
- apiGroups:
  - ""
  resources:
  - "serviceaccounts"
    "services"
    "configmaps"
    "events"
    "pods"
    "pods/log"
  verbs:
  - "get"
    "list"
    "watch"
    "describe"
    "create"
    "edit"
    "delete"
    "deletecollection"
    "annotate"
    "patch"
    "label"
 - apiGroups:
   - ""
   resources:
   - "secrets"
   verbs:
   - "create"
     "patch"
     "delete"
     "watch"
 - apiGroups:
   - ""
   resources:
   - "persistentvolumeclaims"
   verbs:
   - "get"
     "list"
     "watch"
     "describe"
     "create"
     "edit"
     "delete"
     "annotate"
     "patch"
     "label"
```

**RBAC permissions for the spark service account and role**

A Spark driver pod needs a Kubernetes service account in the same namespace as the pod.
This service account needs permissions to manage executor pods and any resources required by the driver pod.
Unless the default service account in the namespace has the required permissions,
the driver fails and exits. The following RBAC permissions are required.

```
rules:
- apiGroups:
  - ""
    "batch"
    "extensions"
    "apps"
  resources:
  - "configmaps"
    "serviceaccounts"
    "events"
    "pods"
    "pods/exec"
    "pods/log"
    "pods/portforward"
    "secrets"
    "services"
    "persistentvolumeclaims"
    "statefulsets"
  verbs:
  - "create"
    "delete"
    "get"
    "list"
    "patch"
    "update"
    "watch"
    "describe"
    "edit"
    "deletecollection"
    "patch"
    "label"
```
