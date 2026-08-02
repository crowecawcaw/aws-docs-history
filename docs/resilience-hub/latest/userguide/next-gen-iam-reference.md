# IAM roles and permissions reference

**IAM role for assessment and resilience testing**

To run an assessment or a resilience test, the next generation of Resilience Hub needs to be able to assume an
IAM role. Assessments require read-only permissions to discover and understand the
configuration of your AWS resources. Resilience testing additionally requires permissions to
start and manage AWS Fault Injection Service (AWS FIS) experiments on your behalf.

You can create an IAM role in the AWS IAM console. Choose **Custom trust
policy** and use a trust policy like this:

```

{
  "Version": "2012-10-17",
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

For permissions, attach the
`AWSResilienceHubV2AssessmentExecutionPolicy` managed policy. This policy
grants read-only access to AWS services for resilience discovery, assessment, and
management.

###### Note

The `AWSResilienceHubV2AssessmentExecutionPolicy` replaces the previous
`AWSResilienceHubAsssessmentExecutionPolicy` for use with the next generation of Resilience Hub. For
details about the permissions included in this policy, see [AWSResilienceHubV2AssessmentExecutionPolicy](next-gen-security-iam-awsmanpol.md#next-gen-security_iam_aws-v2-assessment-policy "next-gen-security-iam-awsmanpol.md#next-gen-security_iam_aws-v2-assessment-policy").

If you use resilience testing, also attach the
`AWSResilienceHubResilienceTestingPolicy` managed policy. This policy grants
Resilience Hub the AWS FIS permissions needed to start and manage experiments on your
behalf.

###### Note

If the managed policy is not available in your account, create an inline policy with the
same permissions. For the policy contents, see [AWSResilienceHubResilienceTestingPolicy](next-gen-security-iam-awsmanpol.md#next-gen-security_iam_aws-resilience-testing-policy "next-gen-security-iam-awsmanpol.md#next-gen-security_iam_aws-resilience-testing-policy").

**IAM Service-Linked Role**

Next generation Resilience Hub automatically creates a Service-Linked Role with the
`AWSResilienceHubServiceRolePolicy` managed policy.

**Terraform state file access permissions**

If you are including Terraform state files into your Next generation Resilience Hub service, provide
permissions to read the Terraform files from your Amazon S3 bucket with a policy like this:

```

{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::`s3-bucket-name`/`path-to-state-file`"
    },
    {
      "Effect": "Allow",
      "Action": "s3:ListBucket",
      "Resource": "arn:aws:s3:::`s3-bucket-name`"
    }
  ]
}

```

**IAM execution role for resilience testing**

Resilience tests run under an IAM role that AWS Fault Injection Service assumes to inject faults into your
resources. The required permissions depend on the test template, and single-account and
multi-account tests use different role structures. For the trust and permissions policies for
each test, see [IAM execution roles for resilience testing](next-gen-resilience-testing-iam.md "next-gen-resilience-testing-iam.md").

**Amazon EKS Permissions**

If you are including Amazon EKS clusters into your Next generation Resilience Hub service, follow the
following 3-step process to provide Next generation Resilience Hub permissions to read configuration data for
your Amazon EKS clusters using Kubernetes role-based access control (RBAC).

**Step 1: Apply the following to your Amazon EKS cluster**

This grants Next generation Resilience Hub read-only access to the Kubernetes resources it needs across
all namespaces:

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

**Step 2: Map the IAM role to the Kubernetes group**

Map the IAM role you created to the
`resilience-hub-eks-access-group` Kubernetes group. You can use either
Amazon EKS access entries (recommended) or the `aws-auth` ConfigMap.

**Option A: Using EKS access entries (recommended)**

EKS access entries are the preferred method for managing cluster authentication.
Your cluster must use `API` or `API_AND_CONFIG_MAP`
authentication mode.

```

aws eks create-access-entry \
  --cluster-name `cluster-name` \
  --principal-arn arn:aws:iam::`ACCOUNT-ID`:role/ResilienceHubRole \
  --type STANDARD \
  --kubernetes-groups '["resilience-hub-eks-access-group"]'

```

**Option B: Using aws-auth ConfigMap**

If your cluster uses `CONFIG_MAP` or `API_AND_CONFIG_MAP`
authentication mode, you can edit the aws-auth ConfigMap instead:

Using eksctl:

```

eksctl create iamidentitymapping \
  --cluster `cluster-name` \
  --region `region` \
  --arn arn:aws:iam::`ACCOUNT-ID`:role/ResilienceHubRole \
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
  rolearn: arn:aws:iam::`ACCOUNT-ID`:role/ResilienceHubRole
  username: AwsResilienceHubAssessmentEKSAccessRole

```

**Step 3: Verify**

Confirm the RBAC resources exist and the role mapping is in place:

```

kubectl get clusterrole resilience-hub-eks-access-cluster-role
kubectl describe clusterrolebinding resilience-hub-eks-access-cluster-role-binding

```

If using access entries (Option A):

```

aws eks describe-access-entry \
  --cluster-name `cluster-name` \
  --principal-arn arn:aws:iam::`ACCOUNT-ID`:role/ResilienceHubRole

```

If using aws-auth ConfigMap (Option B):

```

kubectl get configmap aws-auth -n kube-system -o yaml | grep -A 3 "ResilienceHubRole"

```
