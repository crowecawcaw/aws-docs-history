# Setting up Kubernetes role-based

access control

Cluster admin users also need to set up [Kubernetes
role-based access control (RBAC)](https://kubernetes.io/docs/reference/access-authn-authz/rbac/ "https://kubernetes.io/docs/reference/access-authn-authz/rbac/") for data scientist users to use the [SageMaker HyperPod CLI](https://github.com/aws/sagemaker-hyperpod-cli "https://github.com/aws/sagemaker-hyperpod-cli") to run
workloads on HyperPod clusters orchestrated with Amazon EKS.

## Option 1: Set up RBAC using

Helm chart

The SageMaker HyperPod service team provides a Helm sub-chart for setting up RBAC. To
learn more, see [Installing
packages on the Amazon EKS cluster using Helm](sagemaker-hyperpod-eks-install-packages-using-helm-chart.md "sagemaker-hyperpod-eks-install-packages-using-helm-chart.md").

## Option 2: Set up RBAC

manually

Create `ClusterRole` and `ClusterRoleBinding` with the
minimum privilege, and create `Role` and `RoleBinding` with
mutation permissions.

**To create `ClusterRole` &
`ClusterRoleBinding` for data scientist IAM
role**

Create a cluster-level configuration file `cluster_level_config.yaml`
as follows.

```
kind: ClusterRole
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: hyperpod-scientist-user-cluster-role
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["list"]
- apiGroups: [""]
  resources: ["nodes"]
  verbs: ["list"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: hyperpod-scientist-user-cluster-role-binding
subjects:
- kind: Group
  name: hyperpod-scientist-user-cluster-level
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: hyperpod-scientist-user-cluster-role # this must match the name of the Role or ClusterRole you wish to bind to
  apiGroup: rbac.authorization.k8s.io
```

Apply the configuration to the EKS cluster.

```
kubectl apply -f cluster_level_config.yaml
```

**To create Role and RoleBinding in
namespace**

This is the namespace training operator that run training jobs and Resiliency will
monitor by default. Job auto-resume can only support in `kubeflow`
namespace or namespace prefixed `aws-hyperpod`.

Create a role configuration file `namespace_level_role.yaml` as
follows. This example creates a role in the `kubeflow` namespace

```
kind: Role
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  namespace: kubeflow
  name: hyperpod-scientist-user-namespace-level-role
###
#  1) add/list/describe/delete pods
#  2) get/list/watch/create/patch/update/delete/describe kubeflow pytroch job
#  3) get pod log
###
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["create", "get"]
- apiGroups: [""]
  resources: ["nodes"]
  verbs: ["get", "list"]
- apiGroups: [""]
  resources: ["pods/log"]
  verbs: ["get", "list"]
- apiGroups: [""]
  resources: ["pods/exec"]
  verbs: ["get", "create"]
- apiGroups: ["kubeflow.org"]
  resources: ["pytorchjobs", "pytorchjobs/status"]
  verbs: ["get", "list", "create", "delete", "update", "describe"]
- apiGroups: [""]
  resources: ["configmaps"]
  verbs: ["create", "update", "get", "list", "delete"]
- apiGroups: [""]
  resources: ["secrets"]
  verbs: ["create", "get", "list", "delete"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  namespace: kubeflow
  name: hyperpod-scientist-user-namespace-level-role-binding
subjects:
- kind: Group
  name: hyperpod-scientist-user-namespace-level
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role
  name: hyperpod-scientist-user-namespace-level-role # this must match the name of the Role or ClusterRole you wish to bind to
  apiGroup: rbac.authorization.k8s.io
```

Apply the configuration to the EKS cluster.

```
kubectl apply -f namespace_level_role.yaml
```

## Create an access

entry for Kubernetes groups

After you have set up RBAC using one of the two options above, use the following
sample command replacing the necessary information.

```
aws eks create-access-entry \
    --cluster-name `<eks-cluster-name>` \
    --principal-arn arn:aws:iam::`<AWS_ACCOUNT_ID_SCIENTIST_USER>`:role/ScientistUserRole \
    --kubernetes-groups '["hyperpod-scientist-user-namespace-level","hyperpod-scientist-user-cluster-level"]'
```

For the `principal-arn` parameter, you need to use the [IAM users for
scientists](sagemaker-hyperpod-prerequisites-iam.md#sagemaker-hyperpod-prerequisites-iam-cluster-user "sagemaker-hyperpod-prerequisites-iam.md#sagemaker-hyperpod-prerequisites-iam-cluster-user").
