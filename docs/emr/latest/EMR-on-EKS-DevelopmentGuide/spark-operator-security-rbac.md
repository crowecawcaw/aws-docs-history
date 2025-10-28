# Setting up cluster access permissions

with role-based access control (RBAC)

To deploy the Spark operator, Amazon EMR on EKS creates two roles and service accounts for
the Spark operator and the Spark apps.

###### Topics

- [Operator service account and role](#spark-operator-sa-oper "#spark-operator-sa-oper")
- [Spark service account and role](#spark-operator-sa-spark "#spark-operator-sa-spark")

## Operator service account and role

Amazon EMR on EKS creates the **operator service account and
role** to manage `SparkApplications` for Spark jobs and for
other resources such as services.

The default name for this service account is
`emr-containers-sa-spark-operator`.

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
  - configmaps
  - secrets
  verbs:
  - create
  - get
  - delete
  - update
- apiGroups:
  - extensions
  - networking.k8s.io
  resources:
  - ingresses
  verbs:
  - create
  - get
  - delete
- apiGroups:
  - ""
  resources:
  - nodes
  verbs:
  - get
- apiGroups:
  - ""
  resources:
  - events
  verbs:
  - create
  - update
  - patch
- apiGroups:
  - ""
  resources:
  - resourcequotas
  verbs:
  - get
  - list
  - watch
- apiGroups:
  - apiextensions.k8s.io
  resources:
  - customresourcedefinitions
  verbs:
  - create
  - get
  - update
  - delete
- apiGroups:
  - admissionregistration.k8s.io
  resources:
  - mutatingwebhookconfigurations
  - validatingwebhookconfigurations
  verbs:
  - create
  - get
  - update
  - delete
- apiGroups:
  - sparkoperator.k8s.io
  resources:
  - sparkapplications
  - sparkapplications/status
  - scheduledsparkapplications
  - scheduledsparkapplications/status
  verbs:
  - "*"
  {{- if .Values.batchScheduler.enable }}
  # required for the `volcano` batch scheduler
- apiGroups:
  - scheduling.incubator.k8s.io
  - scheduling.sigs.dev
  - scheduling.volcano.sh
  resources:
  - podgroups
  verbs:
  - "*"
  {{- end }}
  {{ if .Values.webhook.enable }}
- apiGroups:
  - batch
  resources:
  - jobs
  verbs:
  - delete
  {{- end }}
```

## Spark service account and role

A Spark driver pod needs a Kubernetes service account in the same namespace as the
pod. This service account needs permissions to create, get, list, patch and delete
executor pods, and to create a Kubernetes headless service for the driver. The driver
fails and exits without the service account unless the default service account in the
pod's namespace has the required permissions.

The default name for this service account is
`emr-containers-sa-spark`.

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
