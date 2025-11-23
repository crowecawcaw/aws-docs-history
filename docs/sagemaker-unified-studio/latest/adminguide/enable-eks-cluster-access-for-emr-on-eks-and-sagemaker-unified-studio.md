# Enable Amazon EKS cluster access for Amazon EMR on EKS and Amazon SageMaker Unified Studio

Amazon EMR on EKS and Amazon SageMaker Unified Studio require access to the Kubernetes service running on the Amazon EKS cluster.

## Amazon EKS cluster access for Amazon EMR on EKS

1. Create a Kubernetes cluster role for Amazon EMR on EKS.

```
kubectl apply -f - <<EOF
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: emr-containers
rules:
  - apiGroups: [""]
    resources: ["namespaces"]
    verbs: ["get"]
  - apiGroups: [""]
    resources: ["statefulsets", "event", "serviceaccounts", "services", "configmaps", "events", "pods", "pods/log", "pods/exec", "pods/portforward", "pods/secrets"]
    verbs: ["update", "get", "list", "watch", "describe", "create", "edit", "delete", "deletecollection", "annotate", "patch", "label"]
  - apiGroups: [""]
    resources: ["secrets"]
    verbs: ["list", "get", "create", "patch", "delete", "watch"]
  - apiGroups: ["apps"]
    resources: ["statefulsets", "deployments", "configmaps", "events", "persistentvolumeclaims", "pods", "pods/exec", "pods/log", "pods/portforward", "pods/secrets", "serviceaccounts", "services"]
    verbs: ["get", "list", "watch", "describe", "create", "edit", "delete", "annotate", "patch", "update", "label", "deletecollection"]
  - apiGroups: ["batch", "extensions"]
    resources: ["jobs", "configmaps", "events", "persistentvolumeclaims", "pods", "pods/exec", "pods/log", "pods/portforward", "pods/secrets", "serviceaccounts", "services", "statefulsets"]
    verbs: ["get", "describe", "create", "delete", "watch", "list", "patch", "update", "edit", "deletecollection", "label"]
  - apiGroups: ["extensions", "networking.k8s.io"]
    resources: ["ingresses"]
    verbs: ["get", "list", "watch", "describe", "create", "edit", "delete", "annotate", "patch", "label"]
  - apiGroups: ["rbac.authorization.k8s.io"]
    resources: ["clusterroles","clusterrolebindings","roles", "rolebindings"]
    verbs: ["get", "list", "watch", "describe", "create", "edit", "delete", "deletecollection", "annotate", "patch", "label"]
  - apiGroups: [""]
    resources: ["persistentvolumeclaims"]
    verbs: ["update", "get", "list", "watch", "describe", "create", "edit", "delete",  "deletecollection", "annotate", "patch", "label"]
EOF
```

2. Create a Kubernetes cluster role binding for Amazon EMR on EKS.

```
kubectl apply -f - <<EOF
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: emr-containers
subjects:
- kind: User
  name: emr-containers
  apiGroup: rbac.authorization.k8s.io
- kind: User
  name: EmrContainersUser
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: emr-containers
  apiGroup: rbac.authorization.k8s.io
EOF
```

3. Create a Amazon EKS IAM identity mapping binding the Kubernetes user "emr-containers"
   to the service-linked IAM role for EMR on EKS.

```
eksctl create iamidentitymapping \
    --cluster `{eks-cluster-name}` \
    --arn "arn:aws:iam::`{aws-account-id}`:role/AWSServiceRoleForAmazonEMRContainers" \
    --username emr-containers
```

###### Note

`AWSServiceRoleForAmazonEMRContainers` is a service-linked role managed by Amazon EMR on EKS. For more information, see
[Using service-linked roles for Amazon EMR on EKS](../../../emr/latest/EMR-on-EKS-DevelopmentGuide/using-service-linked-roles.md "../../../emr/latest/EMR-on-EKS-DevelopmentGuide/using-service-linked-roles.md").

## Amazon EKS cluster access for Amazon SageMaker Unified Studio

1. Create a Kubernetes cluster role for Amazon SageMaker Unified Studio.

```
kubectl apply -f - <<EOF
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: sagemaker-provisioning
rules:
  - apiGroups: [""]
    resources: ["namespaces"]
    verbs: ["create", "delete"]
EOF
```

2. Create a Kubernetes cluster role binding for Amazon SageMaker Unified Studio.

```
kubectl apply -f - <<EOF
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: sagemaker-provisioning
subjects:
- kind: Group
  name: sagemaker-provisioning
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: sagemaker-provisioning
  apiGroup: rbac.authorization.k8s.io
EOF
```

3. Create a Amazon EKS access entry binding the Kubernetes group "sagemaker-provisioning"
   to the IAM role designated as the provisioning role for your target domain.

```
aws eks create-access-entry \
    --cluster-name `{eks-cluster-name}` \
    --region `{aws-region-code}` \
    --principal-arn `{iam-provisioning-role-arn}` \
    --kubernetes-groups sagemaker-provisioning \
    --type STANDARD
```
