# `AWSSupport-TroubleshootEbsCsiDriversForEks`

**Description**

The `AWSSupport-TroubleshootEbsCsiDriversForEks` runbook helps troubleshoot
issues with Amazon Elastic Block Store volume mounts in Amazon Elastic Kubernetes Service (Amazon EKS) and Amazon EBS Container Storage
Interface (CSI) driver issues

###### Important

Currently the Amazon EBS CSI Driver running on AWS Fargate is not supported.

**How does it work?**

The runbook `AWSSupport-TroubleshootEbsCsiDriversForEks` performs the
following high-level steps:

- Verifies if the target Amazon EKS cluster exists and is in active state.
- Deploys necessary authentication resources for making Kubernetes API calls based
  on whether the addon is Amazon EKS-managed or self-managed.
- Performs Amazon EBS CSI controller health checks and diagnostics.
- Runs IAM permissions checks on node roles and service account roles.
- Diagnoses persistent volume creation issues for the specified application
  pod.
- Checks node-to-pod scheduling and examines pod events.
- Collects relevant Kubernetes and application logs, uploading them to the specified
  Amazon S3 bucket.
- Performs node health checks and verifies connectivity with Amazon EC2 endpoints.
- Reviews persistent volume block device attachments and mounting status.
- Cleans up the authentication infrastructure created during troubleshooting.
- Generates a comprehensive troubleshooting report combining all diagnostic
  results.

###### Note

- The Amazon EKS cluster's authentication mode must be set to either `API`
  or `API_AND_CONFIG_MAP`. We recommend using Amazon EKS Access entry. The
  runbook requires Kubernetes Role-based access control (RBAC) permissions to
  perform the necessary API calls.
- If you don't specify an IAM role for the Lambda function
  (`LambdaRoleArn` parameter), the automation creates a role named
  `Automation-K8sProxy-Role-<ExecutionId>` in your account.
  This role includes the managed policies `AWSLambdaBasicExecutionRole`
  and `AWSLambdaVPCAccessExecutionRole`.
- Some diagnostic steps require the Amazon EKS worker nodes to be Systems Manager managed
  instances. If the nodes aren't Systems Manager managed instances, steps that require Systems Manager
  access are skipped, but other checks continue.
- The automation includes a cleanup step that removes authentication
  infrastructure resources. This cleanup step runs even when previous steps fail,
  which helps prevent orphaned resources in your AWS account.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootEbsCsiDriversForEks "https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootEbsCsiDriversForEks")

**Document type**

Automation

**Owner**

Amazon

**Platforms**

/

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ec2:DescribeIamInstanceProfileAssociations`
- `ec2:DescribeInstanceStatus`
- `ec2:GetEbsEncryptionByDefault`
- `eks:DescribeAddon`
- `eks:DescribeAddonVersions`
- `eks:DescribeCluster`
- `iam:GetInstanceProfile`
- `iam:GetOpenIDConnectProvider`
- `iam:GetRole`
- `iam:ListOpenIDConnectProviders`
- `iam:SimulatePrincipalPolicy`
- `s3:GetBucketLocation`
- `s3:GetBucketPolicyStatus`
- `s3:GetBucketPublicAccessBlock`
- `s3:GetBucketVersioning`
- `s3:ListBucket`
- `s3:ListBucketVersions`
- `ssm:DescribeInstanceInformation`
- `ssm:GetAutomationExecution`
- `ssm:GetDocument`
- `ssm:ListCommandInvocations`
- `ssm:ListCommands`
- `ssm:SendCommand`
- `ssm:StartAutomationExecution`

**Instructions**

Follow these steps to configure the automation:

1. Create a SSM automation role
   `TroubleshootEbsCsiDriversForEks-SSM-Role` in your account. Verify
   that the trust relationship contains the following policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "",
 "Effect": "Allow",
 "Principal": {
 "Service": "ssm.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

2. Attach the policy below to the IAM role to grant the required permissions to
   perform the specified actions on the specified resources.
   - If you are expecting to upload execution and resources logs to Amazon S3 bucket
     in same AWS region, replace
     `arn:{partition}:s3:::BUCKET_NAME/*` as yours in
     `OptionalRestrictPutObjects`.
     - The Amazon S3 bucket should point to the correct Amazon S3 bucket if you
       will select `S3BucketName` in SSM execution.
     - This permission is optional if you don't specify
       `S3BucketName`
     - The Amazon S3 bucket must be private and in the same AWS region where
       you execute the SSM automation.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "OptionalRestrictPutObjects",
 "Effect": "Allow",
 "Action": [
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-bucket`/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeIamInstanceProfileAssociations",
 "ec2:DescribeInstanceStatus",
 "ec2:GetEbsEncryptionByDefault",
 "eks:DescribeAddon",
 "eks:DescribeAddonVersions",
 "eks:DescribeCluster",
 "iam:GetInstanceProfile",
 "iam:GetOpenIDConnectProvider",
 "iam:GetRole",
 "iam:ListOpenIDConnectProviders",
 "iam:SimulatePrincipalPolicy",
 "s3:GetBucketLocation",
 "s3:GetBucketPolicyStatus",
 "s3:GetBucketPublicAccessBlock",
 "s3:GetBucketVersioning",
 "s3:ListBucket",
 "s3:ListBucketVersions",
 "ssm:DescribeInstanceInformation",
 "ssm:GetAutomationExecution",
 "ssm:GetDocument",
 "ssm:ListCommandInvocations",
 "ssm:ListCommands",
 "ssm:SendCommand",
 "ssm:StartAutomationExecution"
 ],
 "Resource": "*"
 },
 {
 "Sid": "SetupK8sApiProxyForEKSActions",
 "Effect": "Allow",
 "Action": [
 "cloudformation:CreateStack",
 "cloudformation:DeleteStack",
 "cloudformation:DescribeStacks",
 "cloudformation:UpdateStack",
 "ec2:CreateNetworkInterface",
 "ec2:DeleteNetworkInterface",
 "ec2:DescribeNetworkInterfaces",
 "ec2:DescribeRouteTables",
 "ec2:DescribeSecurityGroups",
 "ec2:DescribeSubnets",
 "ec2:DescribeVpcs",
 "eks:DescribeCluster",
 "iam:CreateRole",
 "iam:DeleteRole",
 "iam:GetRole",
 "iam:TagRole",
 "iam:UntagRole",
 "lambda:CreateFunction",
 "lambda:DeleteFunction",
 "lambda:GetFunction",
 "lambda:InvokeFunction",
 "lambda:ListTags",
 "lambda:TagResource",
 "lambda:UntagResource",
 "lambda:UpdateFunctionCode",
 "logs:CreateLogGroup",
 "logs:CreateLogStream",
 "logs:DescribeLogGroups",
 "logs:DescribeLogStreams",
 "logs:ListTagsForResource",
 "logs:PutLogEvents",
 "logs:PutRetentionPolicy",
 "logs:TagResource",
 "logs:UntagResource",
 "ssm:DescribeAutomationExecutions",
 "tag:GetResources",
 "tag:TagResources"
 ],
 "Resource": "*"
 },
 {
 "Sid": "PassRoleToAutomation",
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": [
 "arn:aws:iam::*:role/TroubleshootEbsCsiDriversForEks-SSM-Role",
 "arn:aws:iam::*:role/Automation-K8sProxy-Role-*"
 ],
 "Condition": {
 "StringLikeIfExists": {
 "iam:PassedToService": [
 "lambda.amazonaws.com",
 "ssm.amazonaws.com"
 ]
 }
 }
 },
 {
 "Sid": "AttachRolePolicy",
 "Effect": "Allow",
 "Action": [
 "iam:AttachRolePolicy",
 "iam:DetachRolePolicy"
 ],
 "Resource": "*",
 "Condition": {
 "StringLikeIfExists": {
 "iam:ResourceTag/AWSSupport-SetupK8sApiProxyForEKS": "true"
 }
 }
 }
 ]
}`

```

3. Grant the required permissions for Amazon EKS cluster RBAC (Role-Based Access Control).
   The recommended approach is to create an Access Entry in your Amazon EKS cluster.

In the Amazon EKS console, navigate to your cluster. For Amazon EKS access entries, verify
your access configuration is set to `API_AND_CONFIG_MAP` or
`API`. For steps to configure authentication mode for access entries,
see [Setting up access
entries](../../../eks/latest/userguide/setting-up-access-entries.md "../../../eks/latest/userguide/setting-up-access-entries.md").

Choose **Create access entry**.

    * For *IAM principal ARN*, select the IAM role you
     created for SSM automation in the previous step.
    * For *Type*, select `Standard`.

4.  Add an access policy:

        * For *Access scope*, select `Cluster`.
        * For *Policy name*, select
         `AmazonEKSAdminViewPolicy`.

    Choose **Add policy**.

If you are not using access entries to manage Kubernetes API permissions, you must
update the `aws-auth` ConfigMap and create a role binding between your
IAM user or role. Ensure your IAM entity has the following read-only Kubernetes
API permissions:

    * GET
     `/apis/apps/v1/namespaces/{namespace}/deployments/{name}`
    * GET
     `/apis/apps/v1/namespaces/{namespace}/replicasets/{name}`
    * GET
     `/apis/apps/v1/namespaces/{namespace}/daemonsets/{name}`
    * GET `/api/v1/nodes/{name}`
    * GET
     `/api/v1/namespaces/{namespace}/serviceaccounts/{name}`
    * GET
     `/api/v1/namespaces/{namespace}/persistentvolumeclaims/{name}`
    * GET `/api/v1/persistentvolumes/{name}`
    * GET `/apis/storage.k8s.io/v1/storageclasses/{name}`
    * GET `/api/v1/namespaces/{namespace}/pods/{name}`
    * GET `/api/v1/namespaces/{namespace}/pods`
    * GET `/api/v1/namespaces/{namespace}/pods/{name}/log`
    * GET `/api/v1/events`

5.  Run the automation [AWSSupport-TroubleshootEbsCsiDriversForEks (console)](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootEbsCsiDriversForEks/description "https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootEbsCsiDriversForEks/description")
6.  Select **Execute automation**.
7.  For the input parameters, enter the following:

        * **AutomationAssumeRole (Optional):**




        	+ Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management
        	 (IAM) role that allows SSM Automation to perform the actions on
        	 your behalf. The role needs to be added to your Amazon EKS cluster access
        	 entry or RBAC permission to allow Kubernetes API calls.
        	+ Type: `AWS::IAM::Role::Arn`
        	+ Example:
        	 `TroubleshootEbsCsiDriversForEks-SSM-Role`
        * **EksClusterName:**




        	+ Description: The name of the target Amazon Elastic Kubernetes Service (Amazon EKS)
        	 cluster.
        	+ Type: `String`
        * **ApplicationPodName:**




        	+ Description: The name of the Kubernetes application pod having
        	 issues with the Amazon EBS CSI driver.
        	+ Type: `String`
        * **ApplicationNamespace:**




        	+ Description: The Kubernetes namespace for the application pod
        	 having issues with the Amazon EBS CSI driver.
        	+ Type: `String`
        * **EbsCsiControllerDeploymentName
         (Optional):**




        	+ Description: (Optional) The deployment name for the Amazon EBS CSI
        	 controller pod.
        	+ Type: `String`
        	+ Default: `ebs-csi-controller`
        * **EbsCsiControllerNamespace
         (Optional):**




        	+ Description: (Optional) The Kubernetes namespace for the Amazon EBS CSI
        	 controller pod.
        	+ Type: `String`
        	+ Default: `kube-system`
        * **S3BucketName (Optional):**




        	+ Description: (Optional) The target Amazon S3 bucket name where the
        	 troubleshooting logs will be uploaded.
        	+ Type: `AWS::S3::Bucket::Name`
        * **LambdaRoleArn (Optional):**




        	+ Description: (Optional) The ARN of the IAM role that allows
        	 the AWS Lambda function to access the required AWS services and
        	 resources.
        	+ Type: `AWS::IAM::Role::Arn`

    Select **Execute**.

8.  After completed, review the _Outputs_ section for the detailed
    results of the execution.
    **References**

Systems Manager Automation

- [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootEbsCsiDriversForEks/description "https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootEbsCsiDriversForEks/description")
- [Run an
  automation](../../../systems-manager/latest/userguide/automation-working-executing.md "../../../systems-manager/latest/userguide/automation-working-executing.md")
- [Setting up an
  Automation](../../../systems-manager/latest/userguide/automation-setup.md "../../../systems-manager/latest/userguide/automation-setup.md")
- [Support Automation
  Workflows](https://aws.amazon.com/premiumsupport/technology/saw/ "https://aws.amazon.com/premiumsupport/technology/saw/")
  For more information on Amazon EBS CSI Driver, see [Amazon EBS CSI Driver](../../../eks/latest/userguide/ebs-csi.md "../../../eks/latest/userguide/ebs-csi.md").
