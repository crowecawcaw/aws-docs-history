# AWS Identity and Access Management for SageMaker HyperPod

AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely control access
to AWS resources. IAM administrators control who can be _authenticated_ (signed in) and _authorized_
(have permissions) to use Amazon EKS resources. IAM is an AWS service that you can use with
no additional charge.

###### Important

Custom IAM policies that allow Amazon SageMaker Studio or Amazon SageMaker Studio Classic to create Amazon SageMaker
resources must also grant permissions to add tags to those resources. The permission to
add tags to resources is required because Studio and Studio Classic automatically tag
any resources they create. If an IAM policy allows Studio and Studio Classic to
create resources but does not allow tagging, "AccessDenied" errors can occur when
trying to create resources. For more information, see [Provide permissions for tagging SageMaker AI
resources](security_iam_id-based-policy-examples.md#grant-tagging-permissions "security_iam_id-based-policy-examples.md#grant-tagging-permissions").

[AWS managed policies for Amazon SageMaker AI](security-iam-awsmanpol.md "security-iam-awsmanpol.md")
that give permissions to create SageMaker resources already include permissions to add tags
while creating those resources.

Let's assume that there are two main layers of SageMaker HyperPod users: _cluster admin
users_ and _data scientist users_.

- **Cluster admin users** – Are responsible for
  creating and managing SageMaker HyperPod clusters. This includes configuring the
  HyperPod clusters and managing user access to them.
  - Create and configure SageMaker HyperPod clusters with Slurm or Amazon EKS.
  - Create and configure IAM roles for data scientist users and
    HyperPod cluster resources.
  - For SageMaker HyperPod orchestration with Amazon EKS, create and configure [EKS
    access entries](../../../eks/latest/userguide/access-entries.md "../../../eks/latest/userguide/access-entries.md"), [role-based access control
    (RBAC)](sagemaker-hyperpod-eks-setup-rbac.md "sagemaker-hyperpod-eks-setup-rbac.md"), and Pod Identity to fulfill data science use
    cases.

- **Data scientist users** – Focus on ML model
  training. They use the open-source orchestrator or the SageMaker HyperPod CLI to submit
  and manage training jobs.

      + Assume and use the IAM Role provided by cluster admin users.
      + Interact with the open-source orchestrator CLIs supported by SageMaker HyperPod
       (Slurm or Kubernetes) or the SageMaker HyperPod CLI to check clusters capacity,
       connect to cluster, and submit workloads.

  Set up IAM roles for cluster admins by attaching the right permissions or policies to
  operate SageMaker HyperPod clusters. Cluster admins also should create IAM roles to provide to
  SageMaker HyperPod resources to assume to run and communicate with necessary AWS resources, such
  as Amazon S3, Amazon CloudWatch, and AWS Systems Manager (SSM). Finally, the AWS account admin or the cluster
  admins should grant scientists permissions to access the SageMaker HyperPod clusters and run ML
  workloads.

Depending on which orchestrator you choose, permissions needed for the cluster admin and
scientists may vary. You can also control the scope of permissions for various actions in
the roles using the condition keys per service. Use the following Service Authorization
References for adding detailed scope for the services related to SageMaker HyperPod.

- [Amazon Elastic Compute Cloud](../../../service-authorization/latest/reference/list_amazonec2.md "../../../service-authorization/latest/reference/list_amazonec2.md")
- [Amazon Elastic Container Registry](../../../service-authorization/latest/reference/list_amazonelasticcontainerregistry.md "../../../service-authorization/latest/reference/list_amazonelasticcontainerregistry.md") (for SageMaker HyperPod cluster orchestration with Amazon EKS)
- [Amazon Elastic Kubernetes Service](../../../service-authorization/latest/reference/list_amazonelastickubernetesservice.md "../../../service-authorization/latest/reference/list_amazonelastickubernetesservice.md") (for SageMaker HyperPod cluster orchestration with Amazon EKS)
- [Amazon FSx](../../../service-authorization/latest/reference/list_amazonfsx.md "../../../service-authorization/latest/reference/list_amazonfsx.md")
- [AWS IAM Identity Center (successor to AWS Single Sign-On)](../../../service-authorization/latest/reference/list_awsiamidentitycentersuccessortoawssinglesign-on.md "../../../service-authorization/latest/reference/list_awsiamidentitycentersuccessortoawssinglesign-on.md")
- [AWS Identity and Access Management (IAM)](../../../service-authorization/latest/reference/list_awsidentityandaccessmanagementiam.md "../../../service-authorization/latest/reference/list_awsidentityandaccessmanagementiam.md")
- [Amazon Simple Storage Service](../../../service-authorization/latest/reference/list_amazons3.md "../../../service-authorization/latest/reference/list_amazons3.md")
- [Amazon SageMaker AI](../../../service-authorization/latest/reference/list_amazonsagemaker.md "../../../service-authorization/latest/reference/list_amazonsagemaker.md")
- [AWS Systems Manager](../../../service-authorization/latest/reference/list_awssystemsmanager.md "../../../service-authorization/latest/reference/list_awssystemsmanager.md")

###### Topics

- [IAM permissions for cluster creation](#sagemaker-hyperpod-prerequisites-iam-cluster-creation "#sagemaker-hyperpod-prerequisites-iam-cluster-creation")
- [IAM users for
  cluster admin](#sagemaker-hyperpod-prerequisites-iam-cluster-admin "#sagemaker-hyperpod-prerequisites-iam-cluster-admin")
- [IAM users for
  scientists](#sagemaker-hyperpod-prerequisites-iam-cluster-user "#sagemaker-hyperpod-prerequisites-iam-cluster-user")
- [IAM role for
  SageMaker HyperPod](#sagemaker-hyperpod-prerequisites-iam-role-for-hyperpod "#sagemaker-hyperpod-prerequisites-iam-role-for-hyperpod")

## IAM permissions for cluster creation

Creating HyperPod clusters requires the IAM permissions outlined in the
following policy example. If your AWS account has [`AdministratorAccess`](../../../aws-managed-policy/latest/reference/AdministratorAccess.md "../../../aws-managed-policy/latest/reference/AdministratorAccess.md") permissions, these permissions are
granted by default.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "sagemaker:CreateCluster",
                "sagemaker:DeleteCluster",
                "sagemaker:UpdateCluster"
            ],
            "Resource": "arn:aws:sagemaker:*:*:cluster/*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "sagemaker:AddTags"
            ],
            "Resource": "arn:aws:sagemaker:*:*:cluster/*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "sagemaker:ListTags",
                "sagemaker:ListClusters",
                "sagemaker:ListClusterNodes",
                "sagemaker:ListComputeQuotas",
                "sagemaker:ListTrainingPlans",
                "sagemaker:DescribeCluster",
                "sagemaker:DescribeClusterNode"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "cloudformation:CreateStack",
                "cloudformation:UpdateStack",
                "cloudformation:DeleteStack",
                "cloudformation:ContinueUpdateRollback",
                "cloudformation:SetStackPolicy",
                "cloudformation:ValidateTemplate",
                "cloudformation:DescribeStacks",
                "cloudformation:DescribeStackEvents",
                "cloudformation:Get*",
                "cloudformation:List*"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": "arn:aws:iam::*:role/sagemaker-*",
            "Condition": {
                "StringEquals": {
                    "iam:PassedToService": [
                        "sagemaker.amazonaws.com",
                        "eks.amazonaws.com",
                        "lambda.amazonaws.com"
                    ]
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": [
                "iam:PassRole",
                "iam:GetRole"
            ],
            "Resource": "arn:aws:iam::*:role/*"
        },
        {
            "Sid": "AmazonVPCFullAccess",
            "Effect": "Allow",
            "Action": [
                "ec2:AcceptVpcPeeringConnection",
                "ec2:AcceptVpcEndpointConnections",
                "ec2:AllocateAddress",
                "ec2:AssignIpv6Addresses",
                "ec2:AssignPrivateIpAddresses",
                "ec2:AssociateAddress",
                "ec2:AssociateDhcpOptions",
                "ec2:AssociateRouteTable",
                "ec2:AssociateSecurityGroupVpc",
                "ec2:AssociateSubnetCidrBlock",
                "ec2:AssociateVpcCidrBlock",
                "ec2:AttachClassicLinkVpc",
                "ec2:AttachInternetGateway",
                "ec2:AttachNetworkInterface",
                "ec2:AttachVpnGateway",
                "ec2:AuthorizeSecurityGroupEgress",
                "ec2:AuthorizeSecurityGroupIngress",
                "ec2:CreateCarrierGateway",
                "ec2:CreateCustomerGateway",
                "ec2:CreateDefaultSubnet",
                "ec2:CreateDefaultVpc",
                "ec2:CreateDhcpOptions",
                "ec2:CreateEgressOnlyInternetGateway",
                "ec2:CreateFlowLogs",
                "ec2:CreateInternetGateway",
                "ec2:CreateLocalGatewayRouteTableVpcAssociation",
                "ec2:CreateNatGateway",
                "ec2:CreateNetworkAcl",
                "ec2:CreateNetworkAclEntry",
                "ec2:CreateNetworkInterface",
                "ec2:CreateNetworkInterfacePermission",
                "ec2:CreateRoute",
                "ec2:CreateRouteTable",
                "ec2:CreateSecurityGroup",
                "ec2:CreateSubnet",
                "ec2:CreateTags",
                "ec2:CreateVpc",
                "ec2:CreateVpcEndpoint",
                "ec2:CreateVpcEndpointConnectionNotification",
                "ec2:CreateVpcEndpointServiceConfiguration",
                "ec2:CreateVpcPeeringConnection",
                "ec2:CreateVpnConnection",
                "ec2:CreateVpnConnectionRoute",
                "ec2:CreateVpnGateway",
                "ec2:DeleteCarrierGateway",
                "ec2:DeleteCustomerGateway",
                "ec2:DeleteDhcpOptions",
                "ec2:DeleteEgressOnlyInternetGateway",
                "ec2:DeleteFlowLogs",
                "ec2:DeleteInternetGateway",
                "ec2:DeleteLocalGatewayRouteTableVpcAssociation",
                "ec2:DeleteNatGateway",
                "ec2:DeleteNetworkAcl",
                "ec2:DeleteNetworkAclEntry",
                "ec2:DeleteNetworkInterface",
                "ec2:DeleteNetworkInterfacePermission",
                "ec2:DeleteRoute",
                "ec2:DeleteRouteTable",
                "ec2:DeleteSecurityGroup",
                "ec2:DeleteSubnet",
                "ec2:DeleteTags",
                "ec2:DeleteVpc",
                "ec2:DeleteVpcEndpoints",
                "ec2:DeleteVpcEndpointConnectionNotifications",
                "ec2:DeleteVpcEndpointServiceConfigurations",
                "ec2:DeleteVpcPeeringConnection",
                "ec2:DeleteVpnConnection",
                "ec2:DeleteVpnConnectionRoute",
                "ec2:DeleteVpnGateway",
                "ec2:DescribeAccountAttributes",
                "ec2:DescribeAddresses",
                "ec2:DescribeAvailabilityZones",
                "ec2:DescribeCarrierGateways",
                "ec2:DescribeClassicLinkInstances",
                "ec2:DescribeCustomerGateways",
                "ec2:DescribeDhcpOptions",
                "ec2:DescribeEgressOnlyInternetGateways",
                "ec2:DescribeFlowLogs",
                "ec2:DescribeInstances",
                "ec2:DescribeInternetGateways",
                "ec2:DescribeIpv6Pools",
                "ec2:DescribeLocalGatewayRouteTables",
                "ec2:DescribeLocalGatewayRouteTableVpcAssociations",
                "ec2:DescribeKeyPairs",
                "ec2:DescribeMovingAddresses",
                "ec2:DescribeNatGateways",
                "ec2:DescribeNetworkAcls",
                "ec2:DescribeNetworkInterfaceAttribute",
                "ec2:DescribeNetworkInterfacePermissions",
                "ec2:DescribeNetworkInterfaces",
                "ec2:DescribePrefixLists",
                "ec2:DescribeRouteTables",
                "ec2:DescribeSecurityGroupReferences",
                "ec2:DescribeSecurityGroupRules",
                "ec2:DescribeSecurityGroups",
                "ec2:DescribeSecurityGroupVpcAssociations",
                "ec2:DescribeStaleSecurityGroups",
                "ec2:DescribeSubnets",
                "ec2:DescribeTags",
                "ec2:DescribeVpcAttribute",
                "ec2:DescribeVpcClassicLink",
                "ec2:DescribeVpcClassicLinkDnsSupport",
                "ec2:DescribeVpcEndpointConnectionNotifications",
                "ec2:DescribeVpcEndpointConnections",
                "ec2:DescribeVpcEndpoints",
                "ec2:DescribeVpcEndpointServiceConfigurations",
                "ec2:DescribeVpcEndpointServicePermissions",
                "ec2:DescribeVpcEndpointServices",
                "ec2:DescribeVpcPeeringConnections",
                "ec2:DescribeVpcs",
                "ec2:DescribeVpnConnections",
                "ec2:DescribeVpnGateways",
                "ec2:DetachClassicLinkVpc",
                "ec2:DetachInternetGateway",
                "ec2:DetachNetworkInterface",
                "ec2:DetachVpnGateway",
                "ec2:DisableVgwRoutePropagation",
                "ec2:DisableVpcClassicLink",
                "ec2:DisableVpcClassicLinkDnsSupport",
                "ec2:DisassociateAddress",
                "ec2:DisassociateRouteTable",
                "ec2:DisassociateSecurityGroupVpc",
                "ec2:DisassociateSubnetCidrBlock",
                "ec2:DisassociateVpcCidrBlock",
                "ec2:EnableVgwRoutePropagation",
                "ec2:EnableVpcClassicLink",
                "ec2:EnableVpcClassicLinkDnsSupport",
                "ec2:GetSecurityGroupsForVpc",
                "ec2:ModifyNetworkInterfaceAttribute",
                "ec2:ModifySecurityGroupRules",
                "ec2:ModifySubnetAttribute",
                "ec2:ModifyVpcAttribute",
                "ec2:ModifyVpcEndpoint",
                "ec2:ModifyVpcEndpointConnectionNotification",
                "ec2:ModifyVpcEndpointServiceConfiguration",
                "ec2:ModifyVpcEndpointServicePermissions",
                "ec2:ModifyVpcPeeringConnectionOptions",
                "ec2:ModifyVpcTenancy",
                "ec2:MoveAddressToVpc",
                "ec2:RejectVpcEndpointConnections",
                "ec2:RejectVpcPeeringConnection",
                "ec2:ReleaseAddress",
                "ec2:ReplaceNetworkAclAssociation",
                "ec2:ReplaceNetworkAclEntry",
                "ec2:ReplaceRoute",
                "ec2:ReplaceRouteTableAssociation",
                "ec2:ResetNetworkInterfaceAttribute",
                "ec2:RestoreAddressToClassic",
                "ec2:RevokeSecurityGroupEgress",
                "ec2:RevokeSecurityGroupIngress",
                "ec2:UnassignIpv6Addresses",
                "ec2:UnassignPrivateIpAddresses",
                "ec2:UpdateSecurityGroupRuleDescriptionsEgress",
                "ec2:UpdateSecurityGroupRuleDescriptionsIngress"
            ],
            "Resource": "*"
        },
        {
            "Sid": "CloudWatchPermissions",
            "Effect": "Allow",
            "Action": [
                "cloudwatch:*",
                "logs:*",
                "sns:CreateTopic",
                "sns:ListSubscriptions",
                "sns:ListSubscriptionsByTopic",
                "sns:ListTopics",
                "sns:Subscribe",
                "iam:GetPolicy",
                "iam:GetPolicyVersion",
                "iam:GetRole",
                "oam:ListSinks",
                "rum:*",
                "synthetics:*",
                "xray:*"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:CreateBucket",
                "s3:DeleteBucket",
                "s3:PutBucketPolicy",
                "s3:PutBucketTagging",
                "s3:PutBucketPublicAccessBlock",
                "s3:PutBucketLogging",
                "s3:DeleteBucketPolicy",
                "s3:PutObject",
                "s3:DeleteObject",
                "s3:PutEncryptionConfiguration",
                "s3:AbortMultipartUpload",
                "s3:Get*",
                "s3:List*"
            ],
            "Resource": [
                "arn:aws:s3:::*",
                "arn:aws:s3:::*/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "eks:CreateCluster",
                "eks:DeleteCluster",
                "eks:CreateNodegroup",
                "eks:DeleteNodegroup",
                "eks:UpdateNodegroupConfig",
                "eks:UpdateNodegroupVersion",
                "eks:UpdateClusterConfig",
                "eks:UpdateClusterVersion",
                "eks:CreateFargateProfile",
                "eks:DeleteFargateProfile",
                "eks:CreateAddon",
                "eks:DeleteAddon",
                "eks:UpdateAddon",
                "eks:CreateAccessEntry",
                "eks:DeleteAccessEntry",
                "eks:UpdateAccessEntry",
                "eks:AssociateAccessPolicy",
                "eks:AssociateIdentityProviderConfig",
                "eks:DisassociateIdentityProviderConfig",
                "eks:TagResource",
                "eks:UntagResource",
                "eks:AccessKubernetesApi",
                "eks:Describe*",
                "eks:List*"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "ssm:GetParameter",
                "ssm:PutParameter",
                "ssm:DeleteParameter",
                "ssm:DescribeParameters"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "kms:Decrypt",
                "kms:GenerateDataKey"
            ],
            "Resource": "*",
            "Condition": {
                "StringLike": {
                    "kms:ViaService": [
                        "sagemaker.*.amazonaws.com",
                        "ec2.*.amazonaws.com",
                        "s3.*.amazonaws.com",
                        "eks.*.amazonaws.com"
                    ]
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": [
                "lambda:CreateFunction",
                "lambda:DeleteFunction",
                "lambda:GetFunction",
                "lambda:UpdateFunctionCode",
                "lambda:UpdateFunctionConfiguration",
                "lambda:AddPermission",
                "lambda:RemovePermission",
                "lambda:PublishLayerVersion",
                "lambda:DeleteLayerVersion",
                "lambda:InvokeFunction",
                "lambda:Get*",
                "lambda:List*",
                "lambda:TagResource"
            ],
            "Resource": [
                "arn:aws:lambda:*:*:function:*",
                "arn:aws:lambda:*:*:layer:*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "iam:DeleteRole",
                "iam:DeleteRolePolicy"
            ],
            "Resource": [
                "arn:aws:iam::*:role/*sagemaker*",
                "arn:aws:iam::*:role/*eks*",
                "arn:aws:iam::*:role/*hyperpod*",
                "arn:aws:iam::*:policy/*sagemaker*",
                "arn:aws:iam::*:policy/*hyperpod*",
                "arn:aws:iam::*:role/*LifeCycleScriptStack*",
                "arn:aws:iam::*:role/*LifeCycleScript*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "iam:CreateRole",
                "iam:TagRole",
                "iam:PutRolePolicy",
                "iam:Get*",
                "iam:List*",
                "iam:AttachRolePolicy",
                "iam:DetachRolePolicy"
            ],
            "Resource": [
                "arn:aws:iam::*:role/*",
                "arn:aws:iam::*:policy/*"
            ]
        },
        {
            "Sid": "FullAccessToFSx",
            "Effect": "Allow",
            "Action": [
                "fsx:AssociateFileGateway",
                "fsx:AssociateFileSystemAliases",
                "fsx:CancelDataRepositoryTask",
                "fsx:CopyBackup",
                "fsx:CopySnapshotAndUpdateVolume",
                "fsx:CreateAndAttachS3AccessPoint",
                "fsx:CreateBackup",
                "fsx:CreateDataRepositoryAssociation",
                "fsx:CreateDataRepositoryTask",
                "fsx:CreateFileCache",
                "fsx:CreateFileSystem",
                "fsx:CreateFileSystemFromBackup",
                "fsx:CreateSnapshot",
                "fsx:CreateStorageVirtualMachine",
                "fsx:CreateVolume",
                "fsx:CreateVolumeFromBackup",
                "fsx:DetachAndDeleteS3AccessPoint",
                "fsx:DeleteBackup",
                "fsx:DeleteDataRepositoryAssociation",
                "fsx:DeleteFileCache",
                "fsx:DeleteFileSystem",
                "fsx:DeleteSnapshot",
                "fsx:DeleteStorageVirtualMachine",
                "fsx:DeleteVolume",
                "fsx:DescribeAssociatedFileGateways",
                "fsx:DescribeBackups",
                "fsx:DescribeDataRepositoryAssociations",
                "fsx:DescribeDataRepositoryTasks",
                "fsx:DescribeFileCaches",
                "fsx:DescribeFileSystemAliases",
                "fsx:DescribeFileSystems",
                "fsx:DescribeS3AccessPointAttachments",
                "fsx:DescribeSharedVpcConfiguration",
                "fsx:DescribeSnapshots",
                "fsx:DescribeStorageVirtualMachines",
                "fsx:DescribeVolumes",
                "fsx:DisassociateFileGateway",
                "fsx:DisassociateFileSystemAliases",
                "fsx:ListTagsForResource",
                "fsx:ManageBackupPrincipalAssociations",
                "fsx:ReleaseFileSystemNfsV3Locks",
                "fsx:RestoreVolumeFromSnapshot",
                "fsx:TagResource",
                "fsx:UntagResource",
                "fsx:UpdateDataRepositoryAssociation",
                "fsx:UpdateFileCache",
                "fsx:UpdateFileSystem",
                "fsx:UpdateSharedVpcConfiguration",
                "fsx:UpdateSnapshot",
                "fsx:UpdateStorageVirtualMachine",
                "fsx:UpdateVolume"
            ],
            "Resource": "*"
        }
    ]
}
```

## IAM users for

cluster admin

Cluster administrators (admins) operate and configure SageMaker HyperPod clusters,
performing the tasks in [SageMaker HyperPod Slurm cluster operations](sagemaker-hyperpod-operate-slurm.md "sagemaker-hyperpod-operate-slurm.md"). The following
policy example includes the minimum set of permissions for cluster administrators to run
the SageMaker HyperPod core APIs and manage SageMaker HyperPod clusters within your AWS
account.

###### Note

IAM users with cluster admin roles can use condition keys to provide granular
access control when managing SageMaker HyperPod cluster resources specifically for the
`CreateCluster` and `UpdateCluster` actions. To find the
condition keys supported for these actions, search for `CreateCluster` or
`UpdateCluster` in the [Actions defined by SageMaker AI](../../../service-authorization/latest/reference/list_amazonsagemaker.md#amazonsagemaker-actions-as-permissions "../../../service-authorization/latest/reference/list_amazonsagemaker.md#amazonsagemaker-actions-as-permissions").

Slurm
JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "sagemaker:CreateCluster",
 "sagemaker:ListClusters"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "sagemaker:DeleteCluster",
 "sagemaker:DescribeCluster",
 "sagemaker:DescribeClusterNode",
 "sagemaker:ListClusterNodes",
 "sagemaker:UpdateCluster",
 "sagemaker:UpdateClusterSoftware",
 "sagemaker:BatchDeleteClusterNodes"
 ],
 "Resource": "arn:aws:sagemaker:`us-east-1`:`111122223333`:cluster/*"
 }
 ]
}`

```

Amazon EKS

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": `<execution-role-arn>`
        },
        {
            "Effect": "Allow",
            "Action": [
                "sagemaker:CreateCluster",
                "sagemaker:DeleteCluster",
                "sagemaker:DescribeCluster",
                "sagemaker:DescribeCluterNode",
                "sagemaker:ListClusterNodes",
                "sagemaker:ListClusters",
                "sagemaker:UpdateCluster",
                "sagemaker:UpdateClusterSoftware",
                "sagemaker:BatchAddClusterNodes",
                "sagemaker:BatchDeleteClusterNodes",
                "sagemaker:ListComputeQuotas",
                "sagemaker:ListClusterSchedulerConfig",
                "sagemaker:DeleteClusterSchedulerConfig",
                "sagemaker:DeleteComputeQuota",
                "eks:DescribeCluster",
                "eks:CreateAccessEntry",
                "eks:DescribeAccessEntry",
                "eks:DeleteAccessEntry",
                "eks:AssociateAccessPolicy",
                "iam:CreateServiceLinkedRole"
            ],
            "Resource": "*"
        }
    ]
}
```

To grant permissions to access the SageMaker AI console, use the sample policy provided at
[Permissions required to use the Amazon SageMaker AI console](security_iam_id-based-policy-examples.md#console-permissions "security_iam_id-based-policy-examples.md#console-permissions").

To grant permissions to access the Amazon EC2 Systems Manager console, use the sample policy provided
at [Using the AWS Systems Manager console](../../../systems-manager/latest/userguide/security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-console "../../../systems-manager/latest/userguide/security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-console") in the _AWS Systems Manager User
Guide_.

You might also consider attaching the [AmazonSageMakerFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonSageMakerFullAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonSageMakerFullAccess") policy to the role; however, note
that the `AmazonSageMakerFullAccess` policy grants permissions to the entire
SageMaker API calls, features, and resources.

For guidance on IAM users in general, see [IAM users](../../../IAM/latest/UserGuide/id_users.md "../../../IAM/latest/UserGuide/id_users.md") in the
_AWS Identity and Access Management User Guide_.

## IAM users for

scientists

Scientists log into and run ML workloads on SageMaker HyperPod cluster nodes provisioned by
cluster admins. For scientists in your AWS account, you should grant the permission
`"ssm:StartSession"` to run the SSM `start-session` command.
The following is a policy example for IAM users.

Slurm
Add the following policy to grant SSM session permissions to connect to
an SSM target for all resources. This allows you to access HyperPod
clusters.

JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ssm:StartSession",
 "ssm:TerminateSession"
 ],
 "Resource": "*"
 }
 ]
}`

```

Amazon EKS
Grant the following IAM role permissions for data scientists to run
`hyperpod list-clusters` and `hyperpod
 connect-cluster` commands among the HyperPod CLI commands. To
learn more about the HyperPod CLI, see [Running jobs on SageMaker HyperPod clusters
orchestrated by Amazon EKS](sagemaker-hyperpod-eks-run-jobs.md "sagemaker-hyperpod-eks-run-jobs.md"). It also includes SSM
session permissions to connect to an SSM target for all resources. This
allows you to access HyperPod clusters.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "DescribeHyerpodClusterPermissions",
            "Effect": "Allow",
            "Action": [
                "sagemaker:DescribeCluster"
            ],
            "Resource": "<hyperpod-cluster-arn>"
        },
        {
            "Sid": "UseEksClusterPermissions",
            "Effect": "Allow",
            "Action": [
                "eks:DescribeCluster",
            ],
            "Resource": "<eks-cluster-arn>"
        },
        {
            "Sid": "ListClustersPermission",
            "Effect": "Allow",
            "Action": [
                "sagemaker:ListClusters"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "ssm:StartSession",
                "ssm:TerminateSession"
            ],
            "Resource": "*"
        }
    ]
}
```

To grant data scientists IAM users or roles access to Kubernetes APIs in
the cluster, see also [Grant IAM users and
roles access to Kubernetes APIs](../../../eks/latest/userguide/grant-k8s-access.md "../../../eks/latest/userguide/grant-k8s-access.md") in the _Amazon EKS User
Guide_.

## IAM role for

SageMaker HyperPod

For SageMaker HyperPod clusters to run and communicate with necessary AWS resources, you
need create an IAM role for HyperPod cluster to assume.

Start with attaching the managed role [AWS
managed policy: AmazonSageMakerHyperPodServiceRolePolicy](security-iam-awsmanpol-AmazonSageMakerHyperPodServiceRolePolicy.md "security-iam-awsmanpol-AmazonSageMakerHyperPodServiceRolePolicy.md"). Given
this AWS managed policy, SageMaker HyperPod cluster instance groups assume the role to
communicate with Amazon CloudWatch, Amazon S3, and AWS Systems Manager Agent (SSM Agent). This managed policy
is the minimum requirement for SageMaker HyperPod resources to run properly, so you must
provide an IAM role with this policy to all instance groups.

###### Tip

Depending on your preference on designing the level of permissions for multiple
instance groups, you can also set up multiple IAM roles and attach them to
different instance groups. When you set up your cluster user access to specific
SageMaker HyperPod cluster nodes, the nodes assume the role with the selective permissions
you manually attached.

When you set up the access for scientists to specific cluster nodes through [AWS Systems Manager](https://aws.amazon.com/systems-manager/ "https://aws.amazon.com/systems-manager/") (see also [Setting up AWS Systems Manager and Run As
for cluster user access control](sagemaker-hyperpod-prerequisites.md#sagemaker-hyperpod-prerequisites-ssm "sagemaker-hyperpod-prerequisites.md#sagemaker-hyperpod-prerequisites-ssm")), the cluster nodes assume the
role with the selective permissions you manually attach.

After you are done with creating IAM roles, make notes of their names and ARNs. You
use the roles when creating a SageMaker HyperPod cluster, granting the correct permissions
required for each instance group to communicate with necessary AWS resources.

Slurm
For HyperPod orchestrated with Slurm, you must attach the following
managed policy to the SageMaker HyperPod IAM role.

- [AmazonSageMakerClusterInstanceRolePolicy](../../../aws-managed-policy/latest/reference/AmazonSageMakerClusterInstanceRolePolicy.md "../../../aws-managed-policy/latest/reference/AmazonSageMakerClusterInstanceRolePolicy.md")

**(Optional) Additional permissions for using
SageMaker HyperPod with Amazon Virtual Private Cloud**

If you want to use your own Amazon Virtual Private Cloud (VPC) instead of the default SageMaker AI
VPC, you should add the following additional permissions to the IAM role
for SageMaker HyperPod.

```
{
    "Effect": "Allow",
    "Action": [
        "ec2:CreateNetworkInterface",
        "ec2:CreateNetworkInterfacePermission",
        "ec2:DeleteNetworkInterface",
        "ec2:DeleteNetworkInterfacePermission",
        "ec2:DescribeNetworkInterfaces",
        "ec2:DescribeVpcs",
        "ec2:DescribeDhcpOptions",
        "ec2:DescribeSubnets",
        "ec2:DescribeSecurityGroups",
        "ec2:DetachNetworkInterface"
    ],
    "Resource": "*"
}
{
    "Effect": "Allow",
    "Action": "ec2:CreateTags",
    "Resource": [
        "arn:aws:ec2:*:*:network-interface/*"
    ]
}
```

The following list breaks down which permissions are needed to enable
SageMaker HyperPod cluster functionalities when you configure the cluster with
your own Amazon VPC.

- The following `ec2` permissions are required to enable
  configuring a SageMaker HyperPod cluster with your VPC.

```
{
    "Effect": "Allow",
    "Action": [
        "ec2:CreateNetworkInterface",
        "ec2:CreateNetworkInterfacePermission",
        "ec2:DeleteNetworkInterface",
        "ec2:DeleteNetworkInterfacePermission",
        "ec2:DescribeNetworkInterfaces",
        "ec2:DescribeVpcs",
        "ec2:DescribeDhcpOptions",
        "ec2:DescribeSubnets",
        "ec2:DescribeSecurityGroups"
    ],
    "Resource": "*"
}
```

- The following `ec2` permission is required to enable
  the [SageMaker HyperPod auto-resume functionality](sagemaker-hyperpod-resiliency-slurm-auto-resume.md "sagemaker-hyperpod-resiliency-slurm-auto-resume.md").

```
{
    "Effect": "Allow",
    "Action": [
        "ec2:DetachNetworkInterface"
    ],
    "Resource": "*"
}
```

- The following `ec2` permission allows SageMaker HyperPod to
  create tags on the network interfaces within your account.

```
{
    "Effect": "Allow",
    "Action": "ec2:CreateTags",
    "Resource": [
        "arn:aws:ec2:*:*:network-interface/*"
    ]
}
```

Amazon EKS
For HyperPod orchestrated with Amazon EKS, you must attach the following
managed policies to the SageMaker HyperPod IAM role.

- [AmazonSageMakerClusterInstanceRolePolicy](../../../aws-managed-policy/latest/reference/AmazonSageMakerClusterInstanceRolePolicy.md "../../../aws-managed-policy/latest/reference/AmazonSageMakerClusterInstanceRolePolicy.md")

In addition to the managed policies, attach the following permission
policy to the role.

JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ec2:AssignPrivateIpAddresses",
 "ec2:AttachNetworkInterface",
 "ec2:CreateNetworkInterface",
 "ec2:CreateNetworkInterfacePermission",
 "ec2:DeleteNetworkInterface",
 "ec2:DeleteNetworkInterfacePermission",
 "ec2:DescribeInstances",
 "ec2:DescribeInstanceTypes",
 "ec2:DescribeNetworkInterfaces",
 "ec2:DescribeTags",
 "ec2:DescribeVpcs",
 "ec2:DescribeDhcpOptions",
 "ec2:DescribeSubnets",
 "ec2:DescribeSecurityGroups",
 "ec2:DetachNetworkInterface",
 "ec2:ModifyNetworkInterfaceAttribute",
 "ec2:UnassignPrivateIpAddresses",
 "ecr:BatchCheckLayerAvailability",
 "ecr:BatchGetImage",
 "ecr:GetAuthorizationToken",
 "ecr:GetDownloadUrlForLayer",
 "eks-auth:AssumeRoleForPodIdentity"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:CreateTags"
 ],
 "Resource": [
 "arn:aws:ec2:*:*:network-interface/*"
 ]
 }
 ]
}`

```

###### Note

The `"eks-auth:AssumeRoleForPodIdentity"` permission is
optional. It's required if you plan to use EKS Pod identity.

**SageMaker HyperPod service-linked role**

For Amazon EKS support in SageMaker HyperPod, HyperPod creates a
service-linked role with [AWS
managed policy: AmazonSageMakerHyperPodServiceRolePolicy](security-iam-awsmanpol-AmazonSageMakerHyperPodServiceRolePolicy.md "security-iam-awsmanpol-AmazonSageMakerHyperPodServiceRolePolicy.md") to monitor and support resiliency on your EKS cluster such as replacing
nodes and restarting jobs.

**Additional IAM policies for
Amazon EKS cluster with restricted instance group (RIG)**

Workloads running in restricted instance groups rely on the execution role
to load data from Amazon S3. You must add the additional Amazon S3 permissions to the
execution role so that customization jobs running in restricted instance
groups can properly fetch input data.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::`your-bucket-name`"      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject",
        "s3:DeleteObject",
      ],
      "Resource": [
        "arn:aws:s3:::`your-bucket-name`/*"
      ]
    }
  ]
}
```
