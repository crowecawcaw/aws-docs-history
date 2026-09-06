

# Identity-based policies for Oracle Database@AWS
<a name="security_iam_id-based-policy-examples"></a>

By default, users and roles don't have permission to create or modify Oracle Database@AWS resources. To grant users permission to perform actions on the resources that they need, an IAM administrator can create IAM policies.

To learn how to create an IAM identity-based policy by using these example JSON policy documents, see [Create IAM policies (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) in the *IAM User Guide*.

For details about actions and resource types defined by Oracle Database@AWS, including the format of the ARNs for each of the resource types, see [Actions, Resources, and Condition Keys for Oracle Database@AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_your_service.html) in the *Service Authorization Reference*.

**Topics**
+ [Policy best practices](#security_iam_service-with-iam-policy-best-practices)
+ [Using the Oracle Database@AWS console](#security_iam_id-based-policy-examples-console)
+ [Allow users to provision Oracle Database@AWS resources](#security_iam_id-based-policy-examples-full-access)
+ [Allow users to view their own permissions](#security_iam_id-based-policy-examples-view-own-permissions)

## Policy best practices
<a name="security_iam_service-with-iam-policy-best-practices"></a>

Identity-based policies determine whether someone can create, access, or delete Oracle Database@AWS resources in your account. These actions can incur costs for your AWS account. When you create or edit identity-based policies, follow these guidelines and recommendations:
+ **Get started with AWS managed policies and move toward least-privilege permissions** – To get started granting permissions to your users and workloads, use the *AWS managed policies* that grant permissions for many common use cases. They are available in your AWS account. We recommend that you reduce permissions further by defining AWS customer managed policies that are specific to your use cases. For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) or [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html) in the *IAM User Guide*.
+ **Apply least-privilege permissions** – When you set permissions with IAM policies, grant only the permissions required to perform a task. You do this by defining the actions that can be taken on specific resources under specific conditions, also known as *least-privilege permissions*. For more information about using IAM to apply permissions, see [ Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) in the *IAM User Guide*.
+ **Use conditions in IAM policies to further restrict access** – You can add a condition to your policies to limit access to actions and resources. For example, you can write a policy condition to specify that all requests must be sent using SSL. You can also use conditions to grant access to service actions if they are used through a specific AWS service, such as CloudFormation. For more information, see [ IAM JSON policy elements: Condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) in the *IAM User Guide*.
+ **Use IAM Access Analyzer to validate your IAM policies to ensure secure and functional permissions** – IAM Access Analyzer validates new and existing policies so that the policies adhere to the IAM policy language (JSON) and IAM best practices. IAM Access Analyzer provides more than 100 policy checks and actionable recommendations to help you author secure and functional policies. For more information, see [Validate policies with IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-validation.html) in the *IAM User Guide*.
+ **Require multi-factor authentication (MFA)** – If you have a scenario that requires IAM users or a root user in your AWS account, turn on MFA for additional security. To require MFA when API operations are called, add MFA conditions to your policies. For more information, see [ Secure API access with MFA](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.html) in the *IAM User Guide*.

For more information about best practices in IAM, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the *IAM User Guide*.

## Using the Oracle Database@AWS console
<a name="security_iam_id-based-policy-examples-console"></a>

To access the Oracle Database@AWS console, you must have a minimum set of permissions. These permissions must allow you to list and view details about the Oracle Database@AWS resources in your AWS account. If you create an identity-based policy that is more restrictive than the minimum required permissions, the console won't function as intended for entities (users or roles) with that policy.

You don't need to allow minimum console permissions for users that are making calls only to the AWS CLI or the AWS API. Instead, allow access to only the actions that match the API operation that they're trying to perform.

## Allow users to provision Oracle Database@AWS resources
<a name="security_iam_id-based-policy-examples-full-access"></a>

This policy allows users full access to provision Oracle Database@AWS resources. To set up DNS resolution from your VPC, create an outbound Route 53 resolver. Add rules to forward DNS traffic with the OCI domain name to OCI DNS listener IP.

Before you use this policy, replace the example account ID, role ARN, AWS Key Management Service key ARN, and secret ARN. Several of the statements grant permissions that aren't included in the Oracle Database@AWS managed policies and apply only to specific features; remove any that your use case doesn't require. For example, remove the `AllowResourceSharing` statement if you don't use cross-account resource sharing, the `AllowKmsKeyAccess` statement if you don't use customer-managed encryption keys, or the `AllowSecretsManagerAccess` statement if you don't reference a Secrets Manager secret. The `AllowLicenseManagerReceivedGrants` statement is required only if you receive shared Oracle Database@AWS entitlements from another account; otherwise, remove it.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "AllowODBActions",
            "Effect": "Allow",
            "Action": [
                "odb:GetOciOnboardingStatus",
                "odb:InitializeService",
                "odb:CreateCloudExadataInfrastructure",
                "odb:GetCloudExadataInfrastructure",
                "odb:UpdateCloudExadataInfrastructure",
                "odb:GetCloudExadataInfrastructureUnallocatedResources",
                "odb:DeleteCloudExadataInfrastructure",
                "odb:ListCloudExadataInfrastructures",
                "odb:CreateCloudVmCluster",
                "odb:GetCloudVmCluster",
                "odb:DeleteCloudVmCluster",
                "odb:ListCloudVmClusters",
                "odb:CreateCloudAutonomousVmCluster",
                "odb:GetCloudAutonomousVmCluster",
                "odb:DeleteCloudAutonomousVmCluster",
                "odb:ListCloudAutonomousVmClusters",
                "odb:CreateExascaleDbStorageVault",
                "odb:GetExascaleDbStorageVault",
                "odb:UpdateExascaleDbStorageVault",
                "odb:DeleteExascaleDbStorageVault",
                "odb:ListExascaleDbStorageVaults",
                "odb:CreateExadbVmCluster",
                "odb:GetExadbVmCluster",
                "odb:UpdateExadbVmCluster",
                "odb:DeleteExadbVmCluster",
                "odb:ListExadbVmClusters",
                "odb:AssociateVirtualMachinesToExadbVmCluster",
                "odb:DisassociateVirtualMachinesFromExadbVmCluster",
                "odb:ListGiMinorVersions",
                "odb:CreateAutonomousDatabase",
                "odb:GetAutonomousDatabase",
                "odb:UpdateAutonomousDatabase",
                "odb:DeleteAutonomousDatabase",
                "odb:ListAutonomousDatabases",
                "odb:ListAutonomousDatabaseClones",
                "odb:ListAutonomousDatabasePeers",
                "odb:StartAutonomousDatabase",
                "odb:StopAutonomousDatabase",
                "odb:RebootAutonomousDatabase",
                "odb:ShrinkAutonomousDatabase",
                "odb:SwitchoverAutonomousDatabase",
                "odb:FailoverAutonomousDatabase",
                "odb:RestoreAutonomousDatabase",
                "odb:CreateAutonomousDatabaseWallet",
                "odb:GetAutonomousDatabaseWalletDetails",
                "odb:CreateAutonomousDatabaseBackup",
                "odb:GetAutonomousDatabaseBackup",
                "odb:UpdateAutonomousDatabaseBackup",
                "odb:DeleteAutonomousDatabaseBackup",
                "odb:ListAutonomousDatabaseBackups",
                "odb:CreateDbNode",
                "odb:GetDbNode",
                "odb:RebootDbNode",
                "odb:StartDbNode",
                "odb:StopDbNode",
                "odb:DeleteDbNode",
                "odb:ListDbNodes",
                "odb:GetDbServer",
                "odb:ListDbServers",
                "odb:AssociateIamRoleToResource",
                "odb:DisassociateIamRoleFromResource",
                "odb:CreateOdbNetwork",
                "odb:GetOdbNetwork",
                "odb:UpdateOdbNetwork",
                "odb:DeleteOdbNetwork",
                "odb:ListOdbNetworks",
                "odb:CreateOdbPeeringConnection",
                "odb:GetOdbPeeringConnection",
                "odb:UpdateOdbPeeringConnection",
                "odb:DeleteOdbPeeringConnection",
                "odb:ListOdbPeeringConnections",
                "odb:ListAutonomousVirtualMachines",
                "odb:ListDbSystemShapes",
                "odb:ListFlexComponents",
                "odb:ListGiVersions",
                "odb:ListSystemVersions",
                "odb:ListAutonomousDatabaseVersions",
                "odb:ListAutonomousDatabaseCharacterSets",
                "odb:PutResourcePolicy",
                "odb:GetResourcePolicy",
                "odb:DeleteResourcePolicy",
                "odb:CreateGrantShare",
                "odb:UpdateGrantShare",
                "odb:DeleteGrantShare",
                "odb:CreateOutboundIntegration",
                "odb:UpdateOutboundIntegration",
                "odb:TagResource",
                "odb:UntagResource",
                "odb:ListTagsForResource"
            ],
            "Resource": "*"
        },
        {
            "Sid": "AllowEC2DescribeActions",
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeAvailabilityZones",
                "ec2:DescribeVpcs",
                "ec2:DescribeRouteTables"
            ],
            "Resource": "*"
        },
        {
            "Sid": "AllowOdbNetworkPeeringActions",
            "Effect": "Allow",
            "Action": [
                "ec2:CreateOdbNetworkPeering",
                "ec2:ModifyOdbNetworkPeering",
                "ec2:DeleteOdbNetworkPeering"
            ],
            "Resource": "*"
        },
        {
            "Sid": "AllowServiceLinkedRoleCreation",
            "Effect": "Allow",
            "Action": [
                "iam:CreateServiceLinkedRole"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "iam:AWSServiceName": [
                        "odb.amazonaws.com",
                        "vpc-lattice.amazonaws.com"
                    ]
                }
            }
        },
        {
            "Sid": "AllowEc2VpcEndpointManagement",
            "Effect": "Allow",
            "Action": [
                "ec2:CreateVpcEndpoint",
                "ec2:DeleteVpcEndpoints",
                "ec2:DescribeVpcEndpoints",
                "ec2:DescribeVpcEndpointAssociations"
            ],
            "Resource": "*"
        },
        {
            "Sid": "AllowEc2PlacementGroupManagement",
            "Effect": "Allow",
            "Action": [
                "ec2:CreatePlacementGroup",
                "ec2:AttachResourcesToPlacementGroup",
                "ec2:DeletePlacementGroup",
                "ec2:DetachResourcesFromPlacementGroup"
            ],
            "Resource": "*"
        },
        {
            "Sid": "AllowEc2NetworkRouteManagement",
            "Effect": "Allow",
            "Action": [
                "ec2:CreateRoute",
                "ec2:DeleteRoute",
                "ec2:CreateTags"
            ],
            "Resource": "*"
        },
        {
            "Sid": "AllowVpcLatticeManagement",
            "Effect": "Allow",
            "Action": [
                "vpc-lattice:CreateServiceNetwork",
                "vpc-lattice:DeleteServiceNetwork",
                "vpc-lattice:GetServiceNetwork",
                "vpc-lattice:CreateServiceNetworkResourceAssociation",
                "vpc-lattice:DeleteServiceNetworkResourceAssociation",
                "vpc-lattice:GetServiceNetworkResourceAssociation",
                "vpc-lattice:CreateResourceGateway",
                "vpc-lattice:DeleteResourceGateway",
                "vpc-lattice:GetResourceGateway",
                "vpc-lattice:CreateServiceNetworkVpcEndpointAssociation"
            ],
            "Resource": "*"
        },
        {
            "Sid": "AllowResourceSharing",
            "Effect": "Allow",
            "Action": [
                "ram:CreateResourceShare",
                "ram:AssociateResourceShare",
                "ram:DisassociateResourceShare"
            ],
            "Resource": "*",
            "Condition": {
                "StringEqualsIfExists": {
                    "ram:RequestedResourceType": [
                        "odb:CloudExadataInfrastructure",
                        "odb:OdbNetwork"
                    ]
                }
            }
        },
        {
            "Sid": "AllowPassRoleForOdb",
            "Effect": "Allow",
            "Action": [
                "iam:PassRole"
            ],
            "Resource": "arn:aws:iam::123456789012:role/ExampleODBRole",
            "Condition": {
                "StringEquals": {
                    "iam:PassedToService": "odb.amazonaws.com"
                }
            }
        },
        {
            "Sid": "AllowKmsKeyAccess",
            "Effect": "Allow",
            "Action": [
                "kms:DescribeKey"
            ],
            "Resource": "arn:aws:kms:us-east-1:123456789012:key/1234abcd-12ab-34cd-56ef-1234567890ab"
        },
        {
            "Sid": "AllowSecretsManagerAccess",
            "Effect": "Allow",
            "Action": [
                "secretsmanager:DescribeSecret"
            ],
            "Resource": "arn:aws:secretsmanager:us-east-1:123456789012:secret:ExampleODBSecret-a1b2c3"
        },
        {
            "Sid": "AllowLicenseManagerReceivedGrants",
            "Effect": "Allow",
            "Action": [
                "license-manager:ListReceivedGrants"
            ],
            "Resource": "*"
        }
    ]
}
```

------

## Allow users to view their own permissions
<a name="security_iam_id-based-policy-examples-view-own-permissions"></a>

This example shows how you might create a policy that allows IAM users to view the inline and managed policies that are attached to their user identity. This policy includes permissions to complete this action on the console or programmatically using the AWS CLI or AWS API.

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "ViewOwnUserInfo",
            "Effect": "Allow",
            "Action": [
                "iam:GetUserPolicy",
                "iam:ListGroupsForUser",
                "iam:ListAttachedUserPolicies",
                "iam:ListUserPolicies",
                "iam:GetUser"
            ],
            "Resource": ["arn:aws:iam::*:user/${aws:username}"]
        },
        {
            "Sid": "NavigateInConsole",
            "Effect": "Allow",
            "Action": [
                "iam:GetGroupPolicy",
                "iam:GetPolicyVersion",
                "iam:GetPolicy",
                "iam:ListAttachedGroupPolicies",
                "iam:ListGroupPolicies",
                "iam:ListPolicyVersions",
                "iam:ListPolicies",
                "iam:ListUsers"
            ],
            "Resource": "*"
        }
    ]
}
```