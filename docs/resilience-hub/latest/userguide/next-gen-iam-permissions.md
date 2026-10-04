

# Required IAM permissions and roles
<a name="next-gen-iam-permissions"></a>

**AWS managed policy**

You can attach the `AWSResilienceHubV2AssessmentExecutionPolicy` to your IAM identities. While running an assessment, this policy grants read-only access permissions to other AWS services for resilience discovery, assessment, and management. For details about the permissions included in this policy, see [AWSResilienceHubV2AssessmentExecutionPolicy](next-gen-security-iam-awsmanpol.md#next-gen-security_iam_aws-v2-assessment-policy).

**Note**  
The `AWSResilienceHubV2AssessmentExecutionPolicy` replaces the previous `AWSResilienceHubAsssessmentExecutionPolicy` for use with the next generation of Resilience Hub.

If you use resilience testing, also attach the `AWSResilienceHubResilienceTestingPolicy` managed policy. This policy grants Resilience Hub the AWS Fault Injection Service (AWS FIS) permissions needed to start and manage experiments on your behalf. For details about the permissions included in this policy, see [AWSResilienceHubResilienceTestingPolicy](next-gen-security-iam-awsmanpol.md#next-gen-security_iam_aws-resilience-testing-policy).

**Note**  
If the managed policy is not available in your account, create an inline policy with the same permissions. For the policy contents, see [AWSResilienceHubResilienceTestingPolicy](next-gen-security-iam-awsmanpol.md#next-gen-security_iam_aws-resilience-testing-policy).

**IAM role for assessment and resilience testing**

To run an assessment or a resilience test, the next generation of Resilience Hub must assume an IAM role with the required permissions. This role discovers and reads the configuration of your AWS resources, and — when resilience testing is enabled — starts and manages AWS FIS experiments on your behalf.

There are two ways to create or configure this role:
+ **Create a new service role (recommended)** – When you create or edit a service in the Next generation Resilience Hub console, you can choose **Create new role** under **Permission model**. The console automatically creates an IAM role with the correct trust policy and attaches the `AWSResilienceHubV2AssessmentExecutionPolicy` managed policy.
+ **Use an existing service role** – If you already have a role configured, or if you prefer to create roles outside of the console, choose **Use an existing service role**. Then choose the role from the list and make sure that the role has the required trust policy and permissions described below.

To create the role manually, open the IAM console. Choose **Custom trust policy** and use a trust policy like this:

```
{
  "Version": "2012-10-17"		 	 	 ,
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "resiliencehub.amazonaws.com"
      },
      "Action": "sts:AssumeRole",
      "Condition": {}
    }
  ]
}
```

For permissions, attach the `AWSResilienceHubV2AssessmentExecutionPolicy` managed policy. If you use resilience testing, also attach the `AWSResilienceHubResilienceTestingPolicy` managed policy.

**IAM Service-Linked Role**

Next generation Resilience Hub automatically creates a Service-Linked Role with the `AWSResilienceHubServiceRolePolicy` managed policy.

**Terraform state file access permissions**

If you are including Terraform state files into your Next generation Resilience Hub service, provide permissions to read the Terraform files from your Amazon S3 bucket with a policy like this:

```
{
  "Version": "2012-10-17"		 	 	 ,
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::{{s3-bucket-name}}/{{path-to-state-file}}"
    },
    {
      "Effect": "Allow",
      "Action": "s3:ListBucket",
      "Resource": "arn:aws:s3:::{{s3-bucket-name}}"
    }
  ]
}
```

**Amazon EKS Permissions**

If you are including Amazon EKS clusters into your Next generation Resilience Hub service, follow the following 3-step process to provide Next generation Resilience Hub permissions to read configuration data for your Amazon EKS clusters using Kubernetes role-based access control (RBAC).

Each step also has a part labeled **(Optional) Resilience testing**. Complete these parts only if you run resilience tests that inject faults into Amazon EKS pods. Three test templates do this when they block dependencies: **Dependency validation**, **Multi-Region: isolation**, and **Multi-Region: recovery**. The Amazon EKS pod actions in these templates need setup inside your cluster that you can't configure from the next generation of Resilience Hub. This setup includes a Kubernetes service account with fault-injection permissions. It also includes cluster access for the test execution role. If your service has no Amazon EKS pods, or you don't use resilience testing, skip these parts.

The resilience testing setup is separate from, and in addition to, the discovery setup. Discovery grants a read-only cluster role to a Kubernetes group that your service role maps to. Resilience testing grants fault-injection permissions to a Kubernetes service account and to a Kubernetes user that your test execution role maps to. A cluster that you both assess and test needs both.

**Important**  
Because the resilience testing setup lives inside your cluster, the next generation of Resilience Hub can't validate it when you create a test or start a test run. Setup problems surface only when the test runs.  
If the service account is missing, or the execution role lacks cluster access, the test run still starts. The Amazon EKS pod action then fails during fault injection with a Kubernetes authorization error.

**(Optional) Resilience testing: Prerequisites**

Before you complete the resilience testing parts of the following steps, make sure that:
+ Your cluster runs Amazon EKS version 1.30 or later.
+ Your target pods run on Amazon EC2 nodes. The packet loss action that these tests use isn't supported on AWS Fargate.
+ The `securityContext` of your target pods sets `readOnlyRootFilesystem: false`. Amazon EKS pod actions fail without it.
+ You have `kubectl` configured for the cluster, and permissions to create RBAC resources in the namespaces you want to test.

**Note**  
In addition to the cluster setup, the test execution role needs `eks:DescribeCluster` on the cluster, along with the other permissions for the test template you're using. The permissions policies in [IAM execution roles for resilience testing](next-gen-resilience-testing-iam.md) already include these for the templates that support Amazon EKS pods.

**Step 1: Apply the following to your Amazon EKS cluster**

This grants Next generation Resilience Hub read-only access to the Kubernetes resources it needs across all namespaces:

```
cat << EOF | kubectl apply -f -
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: resilience-hub-eks-access-cluster-role
rules:
- apiGroups:
    - ""
  resources:
    - pods
    - replicationcontrollers
    - nodes
    - services
  verbs:
    - get
    - list
- apiGroups:
    - apps
  resources:
    - deployments
    - replicasets
  verbs:
    - get
    - list
- apiGroups:
    - policy
  resources:
    - poddisruptionbudgets
  verbs:
    - get
    - list
- apiGroups:
    - autoscaling.k8s.io
  resources:
    - verticalpodautoscalers
  verbs:
    - get
    - list
- apiGroups:
    - autoscaling
  resources:
    - horizontalpodautoscalers
  verbs:
    - get
    - list
- apiGroups:
    - karpenter.sh
  resources:
    - provisioners
    - nodepools
  verbs:
    - get
    - list
- apiGroups:
    - karpenter.k8s.aws
  resources:
    - awsnodetemplates
    - ec2nodeclasses
  verbs:
    - get
    - list
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: resilience-hub-eks-access-cluster-role-binding
subjects:
  - kind: Group
    name: resilience-hub-eks-access-group
    apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: resilience-hub-eks-access-cluster-role
  apiGroup: rbac.authorization.k8s.io
---
EOF
```

**(Optional) Resilience testing: Create the Kubernetes service account**

Resilience tests run Amazon EKS pod actions as a Kubernetes service account named exactly `resilience-testing-service-account`. You can't change this name—the next generation of Resilience Hub uses it for every test run.

**Important**  
Service accounts are scoped to a namespace. Create `resilience-testing-service-account` in every namespace that contains pods you want to test. If a test targets pods in a namespace where the service account doesn't exist, the Amazon EKS pod action fails for those pods.

The following manifest creates the service account, a role granting the permissions that AWS FIS needs to inject faults, and a role binding that ties them together. Replace {{namespace}} with your target namespace.

```
kind: ServiceAccount
apiVersion: v1
metadata:
  namespace: {{namespace}}
  name: resilience-testing-service-account

---
kind: Role
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  namespace: {{namespace}}
  name: resilience-testing-role
rules:
- apiGroups: [""]
  resources: ["configmaps"]
  verbs: ["get", "create", "patch", "delete"]
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["create", "list", "get", "delete", "deletecollection"]
- apiGroups: [""]
  resources: ["pods/ephemeralcontainers"]
  verbs: ["update"]
- apiGroups: [""]
  resources: ["pods/exec"]
  verbs: ["create"]
- apiGroups: ["apps"]
  resources: ["deployments"]
  verbs: ["get"]

---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: resilience-testing-role-binding
  namespace: {{namespace}}
subjects:
- kind: ServiceAccount
  name: resilience-testing-service-account
  namespace: {{namespace}}
- apiGroup: rbac.authorization.k8s.io
  kind: User
  name: resilience-testing-user
roleRef:
  kind: Role
  name: resilience-testing-role
  apiGroup: rbac.authorization.k8s.io
```

Save the manifest as `rbac.yaml` and apply it:

```
kubectl apply -f rbac.yaml
```

The role binding has two subjects. The service account is what the fault-injection pod runs as. The Kubernetes user is the identity that your test execution role maps to in Step 2. You choose the user name—`resilience-testing-user` in this example—but it must match the user name you use in Step 2.

Repeat this part for each namespace you want to test. The role and role binding names can be the same in every namespace. Only the service account name is fixed by the next generation of Resilience Hub.

**Step 2: Map the IAM role to the Kubernetes group**

Map the IAM role you created to the `resilience-hub-eks-access-group` Kubernetes group. You can use either Amazon EKS access entries (recommended) or the `aws-auth` ConfigMap.

**Option A: Using EKS access entries (recommended)**

EKS access entries are the preferred method for managing cluster authentication. Your cluster must use `API` or `API_AND_CONFIG_MAP` authentication mode.

```
aws eks create-access-entry \
  --cluster-name {{cluster-name}} \
  --principal-arn arn:aws:iam::{{ACCOUNT-ID}}:role/ResilienceHubRole \
  --type STANDARD \
  --kubernetes-groups '["resilience-hub-eks-access-group"]'
```

**Option B: Using aws-auth ConfigMap**

If your cluster uses `CONFIG_MAP` or `API_AND_CONFIG_MAP` authentication mode, you can edit the aws-auth ConfigMap instead:

Using eksctl:

```
eksctl create iamidentitymapping \
  --cluster {{cluster-name}} \
  --region {{region}} \
  --arn arn:aws:iam::{{ACCOUNT-ID}}:role/ResilienceHubRole \
  --group resilience-hub-eks-access-group \
  --username AwsResilienceHubAssessmentEKSAccessRole
```

Or manually edit the ConfigMap:

```
kubectl edit -n kube-system configmap/aws-auth
```

Add this under `mapRoles` in the data section:

```
- groups:
    - resilience-hub-eks-access-group
  rolearn: arn:aws:iam::{{ACCOUNT-ID}}:role/ResilienceHubRole
  username: AwsResilienceHubAssessmentEKSAccessRole
```

**(Optional) Resilience testing: Grant the execution role access to the cluster**

For resilience testing, you map a different IAM role and a different Kubernetes identity than you do for discovery. Map your *test execution role*—not the service role you mapped above—to the Kubernetes *user* in the role binding from Step 1, so that AWS FIS can create the fault-injection pod. Don't add the execution role to the `resilience-hub-eks-access-group` group. As with discovery, use an Amazon EKS access entry (recommended) or the `aws-auth` ConfigMap. The same authentication mode requirements apply: access entries need `API` or `API_AND_CONFIG_MAP`, and the `aws-auth` ConfigMap needs `CONFIG_MAP` or `API_AND_CONFIG_MAP`.

**Important**  
Map the execution role from the account that contains the Amazon EKS cluster. For a multi-account test, this is the *target account* role, not the orchestrator account role. Mapping the orchestrator role is a common mistake. It leaves the test failing with a Kubernetes authorization error. The role that actually reaches the cluster is the one AWS FIS assumes in the target account. For more information about multi-account execution roles, see [Multi-account execution roles](next-gen-resilience-testing-iam-multi-account.md).

Using an access entry (Option A):

```
aws eks create-access-entry \
  --cluster-name {{cluster-name}} \
  --principal-arn arn:aws:iam::{{cluster-account-id}}:role/{{execution-role-name}} \
  --username resilience-testing-user
```

Using the aws-auth ConfigMap with eksctl (Option B):

```
eksctl create iamidentitymapping \
  --cluster {{cluster-name}} \
  --region {{region}} \
  --arn arn:aws:iam::{{cluster-account-id}}:role/{{execution-role-name}} \
  --username resilience-testing-user
```

Or, if you edit the ConfigMap manually, add this under `mapRoles`:

```
- rolearn: arn:aws:iam::{{cluster-account-id}}:role/{{execution-role-name}}
  username: resilience-testing-user
```

**Note**  
Entries in the `aws-auth` ConfigMap don't support a path component in the role ARN. Use `arn:aws:iam::{{cluster-account-id}}:role/{{execution-role-name}}`, not `arn:aws:iam::{{cluster-account-id}}:role/service-role/{{execution-role-name}}`.

**Step 3: Verify**

Confirm the RBAC resources exist and the role mapping is in place:

```
kubectl get clusterrole resilience-hub-eks-access-cluster-role
kubectl describe clusterrolebinding resilience-hub-eks-access-cluster-role-binding
```

If using access entries (Option A):

```
aws eks describe-access-entry \
  --cluster-name {{cluster-name}} \
  --principal-arn arn:aws:iam::{{ACCOUNT-ID}}:role/ResilienceHubRole
```

If using aws-auth ConfigMap (Option B):

```
kubectl get configmap aws-auth -n kube-system -o yaml | grep -A 3 "ResilienceHubRole"
```

**(Optional) Resilience testing: Verify the service account and execution role mapping**

Confirm the service account and role binding exist in each namespace you plan to test:

```
kubectl get serviceaccount resilience-testing-service-account -n {{namespace}}
kubectl describe rolebinding resilience-testing-role-binding -n {{namespace}}
```

If you created an access entry for the execution role (Option A), confirm the mapping:

```
aws eks describe-access-entry \
  --cluster-name {{cluster-name}} \
  --principal-arn arn:aws:iam::{{cluster-account-id}}:role/{{execution-role-name}}
```

If you used the aws-auth ConfigMap (Option B):

```
kubectl get configmap aws-auth -n kube-system -o yaml | grep -A 3 "{{execution-role-name}}"
```

**Important**  
Check that the user name in the access entry or ConfigMap entry matches a `User` subject in the role binding. Both halves of the setup can look correct on their own: the cluster authenticates the execution role, and the RBAC resources exist. If the two names differ, the Amazon EKS pod action fails at injection time with a Kubernetes authorization error. A mismatch here is the most common cause of Amazon EKS pod actions failing.