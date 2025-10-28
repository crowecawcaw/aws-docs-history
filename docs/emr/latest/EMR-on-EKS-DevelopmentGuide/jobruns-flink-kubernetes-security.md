# Security role permissions for running a Flink application

This topic describes security roles for deploying and running a Flink application. There are two roles required to manage a deployment and to
create and manage jobs, the operator role and job role. This topic introduces them and
lists their permissions.

## Role based access control

To deploy the operator and run Flink jobs, we must create two Kubernetes roles: one
operator and one job role. Amazon EMR creates the two roles by default when you install the
operator.

## Operator role

We use the operator role to manage `flinkdeployments` to create and manage
the JobManager for each Flink job and other resources, like services.

The operator role's default name is `emr-containers-sa-flink-operator` and
requires the following permissions.

```
rules:
- apiGroups:
  - ""
  resources:
  - pods
  - services
  - events
  - configmaps
  - secrets
  - serviceaccounts
  verbs:
  - '*'
- apiGroups:
  - rbac.authorization.k8s.io
  resources:
  - roles
  - rolebindings
  verbs:
  - '*'
- apiGroups:
  - apps
  resources:
  - deployments
  - deployments/finalizers
  - replicasets
  verbs:
  - '*'
- apiGroups:
  - extensions
  resources:
  - deployments
  - ingresses
  verbs:
  - '*'
- apiGroups:
  - flink.apache.org
  resources:
  - flinkdeployments
  - flinkdeployments/status
  - flinksessionjobs
  - flinksessionjobs/status
  verbs:
  - '*'
- apiGroups:
  - networking.k8s.io
  resources:
  - ingresses
  verbs:
  - '*'
- apiGroups:
  - coordination.k8s.io
  resources:
  - leases
  verbs:
  - '*'
```

## Job role

The JobManager uses the job role to create and manage TaskManagers and ConfigMaps for
each job.

```
rules:
- apiGroups:
  - ""
  resources:
  - pods
  - configmaps
  verbs:
  - '*'
- apiGroups:
  - apps
  resources:
  - deployments
  - deployments/finalizers
  verbs:
  - '*'
```
