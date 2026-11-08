

# `AWSSupport-TroubleshootEKSCNI`
<a name="automation-awssupport-troubleshootekscni"></a>

## Description
<a name="automation-awssupport-troubleshootekscni-description"></a>

The `AWSSupport-TroubleshootEKSCNI` runbook diagnoses issues with the Amazon Virtual Private Cloud (Amazon VPC) CNI plugin on Amazon Elastic Kubernetes Service (Amazon EKS) worker nodes. It runs comprehensive diagnostic checks including addon status, AWS Identity and Access Management (IAM) authentication, networking configuration, and connectivity.

The runbook performs the following diagnostic checks:
+ Amazon VPC CNI addon status (managed and self-managed), version compatibility, and pod readiness
+ IAM authentication (Pod Identity, IAM Roles for Service Accounts (IRSA), node IAM role, OpenID Connect (OIDC) provider)
+ Network connectivity to Amazon EKS API server and Amazon Elastic Compute Cloud endpoints
+ Node health, CNI configuration files, and system pod status
+ Networking configuration (IP family, custom networking, prefix delegation, pod density, subnet availability)
+ Security group configuration for pods
+ Log collection by using `eks-log-collector.sh` with optional Amazon Simple Storage Service upload

**Important**  
This runbook deploys temporary AWS Lambda (Lambda) resources and might incur associated charges. All temporary resources are cleaned up automatically at the end of execution.

## Run this runbook
<a name="automation-awssupport-troubleshootekscni-run"></a>

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootEKSCNI) 

## Document type
<a name="automation-awssupport-troubleshootekscni-type"></a>

Automation

## Owner
<a name="automation-awssupport-troubleshootekscni-owner"></a>

Amazon

## Platforms
<a name="automation-awssupport-troubleshootekscni-platforms"></a>

Linux

## Parameters
<a name="automation-awssupport-troubleshootekscni-parameters"></a>
+ `AutomationAssumeRole`

  Type: AWS::IAM::Role::Arn

  Description: (Optional) The Amazon Resource Name (ARN) of the IAM role that allows Systems Manager Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses the permissions of the user that starts this runbook.
+ `EksClusterName`

  Type: String

  Allowed pattern: `^[a-zA-Z0-9][a-zA-Z0-9_-]{0,99}$`

  Description: (Required) The name of the Amazon EKS cluster to troubleshoot.
+ `InstanceId`

  Type: AWS::EC2::Instance::Id

  Description: (Required) The Amazon Elastic Compute Cloud (Amazon EC2) instance ID of the worker node.
+ `S3BucketName`

  Type: AWS::S3::Bucket::Name

  Description: (Optional) The Amazon S3 bucket for detailed logs. The bucket must be secure (not public, encryption enabled).
+ `S3BucketOwnerAccount`

  Type: String

  Default: `{{ global:ACCOUNT_ID }}`

  Allowed pattern: `^$|^\{\{ global:ACCOUNT_ID \}\}$|^[0-9]{12}$`

  Description: (Optional) The AWS account that owns the Amazon S3 bucket. If you do not specify this parameter, the runbook assumes that the bucket is in this account.
+ `LambdaRoleArn`

  Type: AWS::IAM::Role::Arn

  Description: (Optional) The ARN of the IAM role for the Lambda function to authenticate against the Amazon EKS cluster. If not provided, the runbook creates a temporary role.

## Required IAM permissions
<a name="automation-awssupport-troubleshootekscni-permissions"></a>

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.

**Important**  
The `AutomationAssumeRole` must be mapped in the Amazon EKS cluster's access configuration to allow authenticated Kubernetes API calls. You can map the role through Amazon EKS access entries or the `aws-auth` ConfigMap. Without this mapping, the automation cannot verify node registration and fails with an authentication error.

**Amazon EKS permissions**
+ `eks:DescribeCluster`
+ `eks:DescribeAddon`
+ `eks:DescribeAddonVersions`
+ `eks:ListPodIdentityAssociations`
+ `eks:DescribePodIdentityAssociation`

**Amazon EC2 permissions**
+ `ec2:DescribeInstances`
+ `ec2:DescribeInstanceTypes`
+ `ec2:DescribeSubnets`
+ `ec2:DescribeNetworkInterfaces`
+ `ec2:DescribeVpcAttribute`
+ `ec2:DescribeRouteTables`
+ `ec2:DescribeVpcs`
+ `ec2:DescribeSecurityGroups`

**IAM permissions**
+ `iam:GetRole`
+ `iam:GetInstanceProfile`
+ `iam:ListAttachedRolePolicies`
+ `iam:GetRolePolicy`
+ `iam:GetPolicy`
+ `iam:GetPolicyVersion`
+ `iam:SimulatePrincipalPolicy`
+ `iam:ListOpenIDConnectProviders`
+ `iam:GetOpenIDConnectProvider`

**AWS Systems Manager permissions**
+ `ssm:StartAutomationExecution`
+ `ssm:SendCommand`
+ `ssm:GetCommandInvocation`
+ `ssm:GetAutomationExecution`
+ `ssm:DescribeAutomationExecutions`
+ `ssm:DescribeAutomationStepExecutions`
+ `ssm:DescribeInstanceInformation`

**Amazon S3 permissions (required only when `S3BucketName` parameter is provided)**
+ `s3:ListBucket`
+ `s3:GetBucketEncryption`
+ `s3:GetBucketAcl`
+ `s3:GetBucketPublicAccessBlock`
+ `s3:GetAccountPublicAccessBlock`
+ `s3:GetBucketPolicyStatus`
+ `s3:GetBucketLocation`
+ `s3:PutObject`

Because this runbook runs a child runbook under the same `AutomationAssumeRole`, that role must also have the permissions listed in [`AWSSupport-SetupK8sApiProxyForEKS`](automation-awssupport-setupk8sapiproxyforeks.md). If you don't specify `LambdaRoleArn`, the role must also have the additional statements described there for when the automation creates the Lambda execution role.

The following example shows a least-privilege IAM policy for the actions that this runbook calls directly:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "EKSReadOnly",
            "Effect": "Allow",
            "Action": [
                "eks:DescribeCluster",
                "eks:DescribeAddon",
                "eks:DescribeAddonVersions",
                "eks:ListPodIdentityAssociations",
                "eks:DescribePodIdentityAssociation"
            ],
            "Resource": [
                "arn:aws:eks:{{REGION}}:{{ACCOUNTID}}:cluster/{{CLUSTER_NAME}}",
                "arn:aws:eks:{{REGION}}:{{ACCOUNTID}}:addon/{{CLUSTER_NAME}}/*",
                "arn:aws:eks:{{REGION}}:{{ACCOUNTID}}:podidentityassociation/{{CLUSTER_NAME}}/*"
            ]
        },
        {
            "Sid": "EC2ReadOnly",
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeInstances",
                "ec2:DescribeInstanceTypes",
                "ec2:DescribeSubnets",
                "ec2:DescribeNetworkInterfaces",
                "ec2:DescribeVpcAttribute",
                "ec2:DescribeRouteTables",
                "ec2:DescribeVpcs",
                "ec2:DescribeSecurityGroups"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:RequestedRegion": "{{REGION}}"
                }
            }
        },
        {
            "Sid": "IAMReadOnly",
            "Effect": "Allow",
            "Action": [
                "iam:GetRole",
                "iam:GetInstanceProfile",
                "iam:ListAttachedRolePolicies",
                "iam:GetRolePolicy",
                "iam:GetPolicy",
                "iam:GetPolicyVersion",
                "iam:SimulatePrincipalPolicy",
                "iam:ListOpenIDConnectProviders",
                "iam:GetOpenIDConnectProvider"
            ],
            "Resource": [
                "arn:aws:iam::{{ACCOUNTID}}:role/*",
                "arn:aws:iam::{{ACCOUNTID}}:instance-profile/*",
                "arn:aws:iam::{{ACCOUNTID}}:policy/*",
                "arn:aws:iam::{{ACCOUNTID}}:oidc-provider/*"
            ]
        },
        {
            "Sid": "SSMAutomationRead",
            "Effect": "Allow",
            "Action": [
                "ssm:GetAutomationExecution",
                "ssm:DescribeAutomationExecutions",
                "ssm:DescribeAutomationStepExecutions"
            ],
            "Resource": "arn:aws:ssm:{{REGION}}:{{ACCOUNTID}}:automation-execution/*"
        },
        {
            "Sid": "SSMCommandExecution",
            "Effect": "Allow",
            "Action": [
                "ssm:SendCommand",
                "ssm:GetCommandInvocation"
            ],
            "Resource": [
                "arn:aws:ssm:{{REGION}}::document/AWS-RunShellScript",
                "arn:aws:ec2:{{REGION}}:{{ACCOUNTID}}:instance/{{INSTANCE_ID}}"
            ]
        },
        {
            "Sid": "SSMDescribeInstances",
            "Effect": "Allow",
            "Action": "ssm:DescribeInstanceInformation",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:RequestedRegion": "{{REGION}}"
                }
            }
        },
        {
            "Sid": "S3LogUpload",
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket",
                "s3:GetBucketEncryption",
                "s3:GetBucketAcl",
                "s3:GetBucketPublicAccessBlock",
                "s3:GetBucketPolicyStatus",
                "s3:GetBucketLocation",
                "s3:PutObject"
            ],
            "Resource": [
                "arn:aws:s3:::{{S3_BUCKET_NAME}}",
                "arn:aws:s3:::{{S3_BUCKET_NAME}}/*"
            ],
            "Condition": {
                "StringEquals": {
                    "s3:ResourceAccount": "{{ACCOUNTID}}"
                }
            }
        },
        {
            "Sid": "S3AccountPublicAccessBlock",
            "Effect": "Allow",
            "Action": "s3:GetAccountPublicAccessBlock",
            "Resource": "*"
        }
    ]
}
```

## Document steps
<a name="automation-awssupport-troubleshootekscni-steps"></a>

1. `CheckConcurrency` - Ensures there is only one execution of this runbook targeting the same AWS Region. If another execution is in progress, the runbook returns an error and ends.

1. `ValidatePrerequisites` - Validates all prerequisites including cluster state, instance status, Amazon EC2 Systems Manager connectivity, Amazon VPC DNS settings, and IAM permissions. If any prerequisite validation fails, the runbook skips to `GenerateReport`.

1. `BranchOnValidation` - Routes execution based on prerequisite validation results. If all prerequisites are valid, proceeds to `DeployK8sApiProxy`. Otherwise, skips to `GenerateReport`.

1. `DeployK8sApiProxy` - Deploys a Lambda function to make authenticated Kubernetes API calls to the Amazon EKS cluster by executing the `AWSSupport-SetupK8sApiProxyForEKS` child runbook.

1. `ValidateNodeInCluster` - Verifies that the Amazon EC2 instance is a registered node in the Amazon EKS cluster through the Kubernetes API. If the node is not found in the cluster, the runbook skips to `CleanupResources`.

1. `BranchOnNodeValidation` - Routes execution based on node validation results. If the node is valid, proceeds to `RunCNIChecks`. Otherwise, skips to `CleanupResources`.

1. `RunCNIChecks` - Executes all CNI diagnostic checks including addon status, IAM authentication, connectivity, node health, networking configuration, security groups, and log collection. Continues to the next step even if checks encounter errors.

1. `CleanupResources` - Cleans up the Lambda function and associated resources deployed during the diagnostic checks by executing the `AWSSupport-SetupK8sApiProxyForEKS` child runbook with the `Cleanup` operation.

1. `GenerateReport` - Generates a diagnostic report with human-readable messages and actionable recommendations for each finding.

## Outputs
<a name="automation-awssupport-troubleshootekscni-outputs"></a>

`GenerateReport.Report` - A comprehensive summary of all findings with error codes, messages, and actionable recommendations.