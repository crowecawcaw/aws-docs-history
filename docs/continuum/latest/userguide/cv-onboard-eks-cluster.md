

# Connecting an Amazon EKS cluster to AWS Continuum
<a name="cv-onboard-eks-cluster"></a>

For read-only Kubernetes inventory collection, connect your Amazon EKS cluster to AWS Continuum. The onboarding takes about 10 minutes for each cluster. This task requires Amazon EKS administrator permissions and `kubectl` cluster-admin access. If you don't have these permissions, ask your administrator to perform these steps or grant you the required access.

**Topics**
+ [Understanding how AWS Continuum accesses your cluster](#cv-onboard-eks-cluster-how-it-works)
+ [Gathering prerequisites](#cv-onboard-eks-cluster-prereqs)
+ [Creating the reader IAM role in the AWS Continuum console](#cv-onboard-eks-cluster-create-role)
+ [Enabling access entries in Amazon EKS](#cv-onboard-eks-cluster-enable-access-entries)
+ [Mapping the role into your cluster](#cv-onboard-eks-cluster-map-role)
+ [Granting read-only RBAC](#cv-onboard-eks-cluster-grant-rbac)
+ [Verifying access to your cluster](#cv-onboard-eks-cluster-verify)
+ [Resolving role and RBAC errors for EKS cluster onboarding](#cv-onboard-eks-cluster-troubleshooting)
+ [Understanding what AWS Continuum can and cannot see](#cv-onboard-eks-cluster-scope)

## Understanding how AWS Continuum accesses your cluster
<a name="cv-onboard-eks-cluster-how-it-works"></a>

AWS Continuum reads your cluster's Kubernetes state through the Amazon EKS cluster communication service (CCS). There is no public endpoint, no VPC peering, and no agent to install. You control access with three elements:
+ A trust-only AWS Identity and Access Management (IAM) role that the AWS Continuum collector can assume. The role grants no AWS permissions of its own.
+ An Amazon EKS access entry that maps that role to a Kubernetes group.
+ A read-only role-based access control (RBAC) binding that lets the group read resources. The binding never grants write access and never grants access to Secrets.

You can revoke access at any time by deleting the role or the access entry.

With AWS Enhanced Zero-Click Role Creation, you create only the reader IAM role. You set up the Amazon EKS access entry and the in-cluster RBAC yourself, because those use Amazon EKS and Kubernetes APIs instead of IAM.

## Gathering prerequisites
<a name="cv-onboard-eks-cluster-prereqs"></a>

Before you begin, make sure that you have the following:
+ You have access to the AWS Continuum console Kubernetes collection, which lets you create the reader IAM role, enable the AWS collector, and turn on Kubernetes collection.
+ You have Amazon EKS administrator permissions in the account.
+ You have `kubectl` cluster-admin access to the cluster, which you use to grant read-only RBAC.
+ You have your cluster name and AWS Region.
+ If the cluster is private-only (no public endpoint), you have a host with a network path to the cluster endpoint from which to run `kubectl`.

## Creating the reader IAM role in the AWS Continuum console
<a name="cv-onboard-eks-cluster-create-role"></a>

Complete this procedure one time for each account to create the reader IAM role. For more information about IAM roles, see [IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) in the *IAM User Guide*.

**To create the reader IAM role**

1. Open the AWS Continuum console at [https://console.aws.amazon.com/continuum/](https://console.aws.amazon.com/continuum/) and sign in to the AWS account that contains the EKS cluster to collect.

1. Choose **Set up Kubernetes collection**.

1. Turn on **Kubernetes collection**.

1. Choose **Create default role**.

1. Choose **Create role**, and then save. Role creation completes in a few minutes.

If role creation fails, verify that you have the IAM permissions to create roles, and then try again.

The console creates an IAM role named `ContinuumKubernetesReader-{{collector-id}}`, which has no permissions policy attached. The procedures later in this topic decide what the role can actually read.

## Enabling access entries in Amazon EKS
<a name="cv-onboard-eks-cluster-enable-access-entries"></a>

Complete this procedure one time for each cluster. Your cluster must use the `API` or `API_AND_CONFIG_MAP` authentication mode, and the modern default is `API_AND_CONFIG_MAP`.

The authentication mode changes in one direction only. Run the following command only when the cluster is currently in `CONFIG_MAP` mode. If the cluster is already in `API` or `API_AND_CONFIG_MAP` mode, skip this procedure. For more information about access entries, see [Manage access entries](https://docs.aws.amazon.com/eks/latest/userguide/access-entries.html) in the *Amazon EKS User Guide*.

The following AWS Command Line Interface (AWS CLI) command updates the cluster configuration. Replace {{region}} with your AWS Region and {{cluster}} with your cluster name:

```
PROMPT> aws eks update-cluster-config \
    --region {{region}} \
    --name {{cluster}} \
    --access-config authenticationMode=API_AND_CONFIG_MAP
```

If the command returns an access denied error, verify that you have Amazon EKS administrator permissions, and then try again.

## Mapping the role into your cluster
<a name="cv-onboard-eks-cluster-map-role"></a>

Complete this procedure one time for each cluster. Before you begin, create the reader IAM role in [Creating the reader IAM role in the AWS Continuum console](#cv-onboard-eks-cluster-create-role), and make sure that you have Amazon EKS administrator permissions. The command maps the reader IAM role to the Kubernetes group `continuum:readers`. You reference this group when you grant read-only RBAC.

Map the reader IAM role to the Kubernetes group by running the following AWS CLI command. Replace {{region}}, {{cluster}}, {{account-id}}, and {{collector-id}} with your values:

```
PROMPT> aws eks create-access-entry \
    --region {{region}} \
    --cluster-name {{cluster}} \
    --principal-arn arn:aws:iam::{{account-id}}:role/ContinuumKubernetesReader-{{collector-id}} \
    --kubernetes-groups continuum:readers \
    --type STANDARD
```

If the command fails because the role is missing or can't be assumed, see [Resolving role and RBAC errors for EKS cluster onboarding](#cv-onboard-eks-cluster-troubleshooting).

## Granting read-only RBAC
<a name="cv-onboard-eks-cluster-grant-rbac"></a>

Complete this procedure one time for each cluster. This procedure requires `kubectl` cluster-admin access. If you don't have cluster-admin access, ask your administrator to perform these steps. With this manifest, you grant read-only access (`get`, `list`, and `watch`) on the resources that AWS Continuum collects, while you exclude Secrets.

Apply the following Kubernetes RBAC YAML manifest with `kubectl`:

```
PROMPT> kubectl apply -f - <<'EOF'
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: continuum-reader
  labels:
    app.kubernetes.io/managed-by: continuum-k8s-collection
rules:
  # Core API group (list-only; secrets deliberately excluded).
  - apiGroups: [""]
    resources:
      - pods
      - services
      - nodes
      - namespaces
      - serviceaccounts
    verbs: ["get", "list", "watch"]

  # Workloads.
  - apiGroups: ["apps"]
    resources: ["deployments", "statefulsets", "daemonsets"]
    verbs: ["get", "list", "watch"]
  - apiGroups: ["batch"]
    resources: ["jobs"]
    verbs: ["get", "list", "watch"]

  # Core networking and policy.
  - apiGroups: ["networking.k8s.io"]
    resources: ["ingresses", "networkpolicies"]
    verbs: ["get", "list", "watch"]

  # RBAC.
  - apiGroups: ["rbac.authorization.k8s.io"]
    resources: ["roles", "rolebindings", "clusterroles", "clusterrolebindings"]
    verbs: ["get", "list", "watch"]

  # Admission webhooks.
  - apiGroups: ["admissionregistration.k8s.io"]
    resources: ["mutatingwebhookconfigurations", "validatingwebhookconfigurations"]
    verbs: ["get", "list", "watch"]

  # Kubernetes Gateway API (CRD).
  - apiGroups: ["gateway.networking.k8s.io"]
    resources: ["*"]
    verbs: ["get", "list", "watch"]

  # CNI network policies (CRD).
  - apiGroups: ["cilium.io"]
    resources: ["*"]
    verbs: ["get", "list", "watch"]
  - apiGroups: ["crd.projectcalico.org"]
    resources: ["*"]
    verbs: ["get", "list", "watch"]

  # Istio service mesh (CRD).
  - apiGroups: ["install.istio.io", "networking.istio.io", "security.istio.io"]
    resources: ["*"]
    verbs: ["get", "list", "watch"]

  # Kyverno policy engine (CRD).
  - apiGroups: ["kyverno.io"]
    resources: ["*"]
    verbs: ["get", "list", "watch"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: continuum-reader-binding
  labels:
    app.kubernetes.io/managed-by: continuum-k8s-collection
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: continuum-reader
subjects:
  - apiGroup: rbac.authorization.k8s.io
    kind: Group
    name: continuum:readers # MUST match the access entry group.
EOF
```

If some resources return a `forbidden` error, confirm that the access entry group and the binding both use `continuum:readers`.

For a private-only cluster, run `kubectl` from a host that has a network path to the cluster endpoint, such as an in-VPC host.

**Note**  
You grant read-only RBAC one time. The AWS Continuum collector never uses `kubectl`. The collector reaches your cluster only over CCS for read-only collection.

## Verifying access to your cluster
<a name="cv-onboard-eks-cluster-verify"></a>

From a cluster-admin context, confirm that the reader group can list nodes but cannot list Secrets. The following `kubectl` commands return `yes` for nodes and `no` for Secrets:

```
PROMPT> kubectl auth can-i list nodes --as-group=continuum:readers --as=continuum-check
yes

PROMPT> kubectl auth can-i list secrets --as-group=continuum:readers --as=continuum-check
no
```

## Resolving role and RBAC errors for EKS cluster onboarding
<a name="cv-onboard-eks-cluster-troubleshooting"></a>

Use the following table to resolve common issues.


| Symptom | Likely cause | Fix | 
| --- | --- | --- | 
| AWS Continuum can't assume the role. | The role is missing or its trust policy changed. | In the AWS Continuum console, repeat the procedure in [Creating the reader IAM role in the AWS Continuum console](#cv-onboard-eks-cluster-create-role) to recreate the role and its trust policy correctly. | 
| Some resources are missing or return a `forbidden` error. | You didn't apply the RBAC, or the group name doesn't match. | Repeat the procedure in [Granting read-only RBAC](#cv-onboard-eks-cluster-grant-rbac). Make sure that the access entry group and the binding both use `continuum:readers`. | 
| `kubectl` can't reach a private cluster. | The cluster has a private-only endpoint. | Run `kubectl` from a host that has a network path to the cluster endpoint, such as an in-VPC host. | 

## Understanding what AWS Continuum can and cannot see
<a name="cv-onboard-eks-cluster-scope"></a>

The following list describes what the AWS Continuum collector can and cannot see:
+ The collector reads the following resources: namespaces, nodes, pods, services, workloads (deployments, daemonsets, statefulsets, and jobs), ingresses, network policies, RBAC objects, admission webhooks, and common networking and service mesh CRDs.
+ The collector does not read Secrets and performs no write operations.