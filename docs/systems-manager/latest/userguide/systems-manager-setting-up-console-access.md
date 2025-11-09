AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Setting up Systems Manager console

access

To use AWS Systems Manager in the AWS Management Console, you must have the correct permissions
configured.

For more information about how to create AWS Identity and Access Management policies and attach them to IAM
identities, see [Create IAM policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in the
_IAM User Guide_

## Systems Manager onboarding

policy

You can create an IAM policy like the one shown in the following example, and attach
the policy to your IAM identities. This policy grants full access to onboard to and
configure Systems Manager.

**Permissions details**

This policy includes the following permissions.

- `ssm-quicksetup` – Allows principals to access all AWS Systems Manager Quick Setup
  actions.
- `ssm` – Allows principals access to Systems Manager Automation and
  Resource Explorer.
- `organizations` – Allows principals to read an organization's
  structure in AWS Organizations, and manage delegated administrators when they are onboarding to
  Systems Manager as an organization.
- `cloudformation` – Allows principals to manage their Quick Setup
  stacks.
- `iam` – Allows principals to manage IAM roles and policies that
  are required for Systems Manager onboarding.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "QuickSetupActions",
 "Effect": "Allow",
 "Action": [
 "ssm-quicksetup:*"
 ],
 "Resource": "*"
 },

 {
 "Sid": "SsmReadOnly",
 "Effect": "Allow",
 "Action": [
 "ssm:DescribeAutomationExecutions",
 "ssm:GetAutomationExecution",
 "ssm:ListAssociations",
 "ssm:DescribeAssociation",
 "ssm:ListDocuments",
 "ssm:ListResourceDataSync",
 "ssm:DescribePatchBaselines",
 "ssm:GetPatchBaseline",
 "ssm:DescribeMaintenanceWindows",
 "ssm:DescribeMaintenanceWindowTasks"
 ],
 "Resource": "*"
 },
 {
 "Sid": "SsmDocument",
 "Effect": "Allow",
 "Action": [
 "ssm:GetDocument",
 "ssm:DescribeDocument"
 ],
 "Resource": [
 "arn:aws:ssm:*:*:document/AWSQuickSetupType-*",
 "arn:aws:ssm:*:*:document/AWS-EnableExplorer"
 ]
 },
 {
 "Sid": "SsmEnableExplorer",
 "Effect": "Allow",
 "Action": "ssm:StartAutomationExecution",
 "Resource": "arn:aws:ssm:*:*:automation-definition/AWS-EnableExplorer:*"
 },
 {
 "Sid": "SsmExplorerRds",
 "Effect": "Allow",
 "Action": [
 "ssm:GetOpsSummary",
 "ssm:CreateResourceDataSync",
 "ssm:UpdateResourceDataSync"
 ],
 "Resource": "arn:aws:ssm:*:*:resource-data-sync/AWS-QuickSetup-*"
 },
 {
 "Sid": "OrgsReadOnly",
 "Effect": "Allow",
 "Action": [
 "organizations:DescribeAccount",
 "organizations:DescribeOrganization",
 "organizations:ListDelegatedAdministrators",
 "organizations:ListRoots",
 "organizations:ListParents",
 "organizations:ListOrganizationalUnitsForParent",
 "organizations:DescribeOrganizationalUnit",
 "organizations:ListAWSServiceAccessForOrganization"
 ],
 "Resource": "*"
 },
 {
 "Sid": "OrgsAdministration",
 "Effect": "Allow",
 "Action": [
 "organizations:EnableAWSServiceAccess",
 "organizations:RegisterDelegatedAdministrator",
 "organizations:DeregisterDelegatedAdministrator"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "organizations:ServicePrincipal": [
 "ssm.amazonaws.com",
 "ssm-quicksetup.amazonaws.com",
 "member.org.stacksets.cloudformation.amazonaws.com",
 "resource-explorer-2.amazonaws.com"
 ]
 }
 }
 },
 {
 "Sid": "CfnReadOnly",
 "Effect": "Allow",
 "Action": [
 "cloudformation:ListStacks",
 "cloudformation:DescribeStacks",
 "cloudformation:ListStackSets",
 "cloudformation:DescribeOrganizationsAccess"
 ],
 "Resource": "*"
 },
 {
 "Sid": "OrgCfnAccess",
 "Effect": "Allow",
 "Action": [
 "cloudformation:ActivateOrganizationsAccess"
 ],
 "Resource": "*"
 },
 {
 "Sid": "CfnStackActions",
 "Effect": "Allow",
 "Action": [
 "cloudformation:CreateStack",
 "cloudformation:DeleteStack",
 "cloudformation:DescribeStackResources",
 "cloudformation:DescribeStackEvents",
 "cloudformation:GetTemplate",
 "cloudformation:RollbackStack",
 "cloudformation:TagResource",
 "cloudformation:UntagResource",
 "cloudformation:UpdateStack"
 ],
 "Resource": [
 "arn:aws:cloudformation:*:*:stack/StackSet-AWS-QuickSetup-*",
 "arn:aws:cloudformation:*:*:stack/AWS-QuickSetup-*",
 "arn:aws:cloudformation:*:*:type/resource/*"
 ]
 },
 {
 "Sid": "CfnStackSetActions",
 "Effect": "Allow",
 "Action": [
 "cloudformation:CreateStackInstances",
 "cloudformation:CreateStackSet",
 "cloudformation:DeleteStackInstances",
 "cloudformation:DeleteStackSet",
 "cloudformation:DescribeStackInstance",
 "cloudformation:DetectStackSetDrift",
 "cloudformation:ListStackInstanceResourceDrifts",
 "cloudformation:DescribeStackSet",
 "cloudformation:DescribeStackSetOperation",
 "cloudformation:ListStackInstances",
 "cloudformation:ListStackSetOperations",
 "cloudformation:ListStackSetOperationResults",
 "cloudformation:TagResource",
 "cloudformation:UntagResource",
 "cloudformation:UpdateStackSet"
 ],
 "Resource": [
 "arn:aws:cloudformation:*:*:stackset/AWS-QuickSetup-*",
 "arn:aws:cloudformation:*:*:type/resource/*",
 "arn:aws:cloudformation:*:*:stackset-target/AWS-QuickSetup-*:*"
 ]
 },
 {
 "Sid": "ValidationReadonlyActions",
 "Effect": "Allow",
 "Action": [
 "iam:ListRoles",
 "iam:GetRole"
 ],
 "Resource": "*"
 },
 {
 "Sid": "IamRolesMgmt",
 "Effect": "Allow",
 "Action": [
 "iam:CreateRole",
 "iam:DeleteRole",
 "iam:GetRole",
 "iam:AttachRolePolicy",
 "iam:DetachRolePolicy",
 "iam:GetRolePolicy",
 "iam:ListRolePolicies"
 ],
 "Resource": [
 "arn:aws:iam::*:role/AWS-QuickSetup-*",
 "arn:aws:iam::*:role/service-role/AWS-QuickSetup-*"
 ]
 },
 {
 "Sid": "IamPassRole",
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": [
 "arn:aws:iam::*:role/AWS-QuickSetup-*",
 "arn:aws:iam::*:role/service-role/AWS-QuickSetup-*"
 ],
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": [
 "ssm.amazonaws.com",
 "ssm-quicksetup.amazonaws.com",
 "cloudformation.amazonaws.com"
 ]
 }
 }
 },
 {
 "Sid": "IamRolesPoliciesMgmt",
 "Effect": "Allow",
 "Action": [
 "iam:AttachRolePolicy",
 "iam:DetachRolePolicy"
 ],
 "Resource": [
 "arn:aws:iam::*:role/AWS-QuickSetup-*",
 "arn:aws:iam::*:role/service-role/AWS-QuickSetup-*"
 ],
 "Condition": {
 "ArnEquals": {
 "iam:PolicyARN": [
 "arn:aws:iam::aws:policy/AWSSystemsManagerEnableExplorerExecutionPolicy",
 "arn:aws:iam::aws:policy/AWSQuickSetupSSMDeploymentRolePolicy"
 ]
 }
 }
 },
 {
 "Sid": "CfnStackSetsSLR",
 "Effect": "Allow",
 "Action": [
 "iam:CreateServiceLinkedRole"
 ],
 "Resource": [
 "arn:aws:iam::*:role/aws-service-role/stacksets.cloudformation.amazonaws.com/AWSServiceRoleForCloudFormationStackSetsOrgAdmin",
 "arn:aws:iam::*:role/aws-service-role/ssm.amazonaws.com/AWSServiceRoleForAmazonSSM",
 "arn:aws:iam::*:role/aws-service-role/accountdiscovery.ssm.amazonaws.com/AWSServiceRoleForAmazonSSM_AccountDiscovery",
 "arn:aws:iam::*:role/aws-service-role/ssm-quicksetup.amazonaws.com/AWSServiceRoleForSSMQuickSetup",
 "arn:aws:iam::*:role/aws-service-role/resource-explorer-2.amazonaws.com/AWSServiceRoleForResourceExplorer"
 ]
 }
 ]
 }`

```

## AWS Systems Manager console operator

policy

You can create an IAM policy like the one shown in the following example, and attach
the policy to your IAM identities. This policy grants full access to operate Systems Manager, and
allow Systems Manager to run Automation documents for diagnosis and remediation.

**Permissions details**

This policy includes the following permissions.

- `ssm` – Allows principals to access all Systems Manager APIs.
- `ssm-quicksetup` – Allows principals to manage their Quick Setup
  configurations.
- `ec2` – Allows Systems Manager to determine your enabled AWS Regions and
  Amazon EC2 instance status.
- `cloudformation` – Allows principals to read their Quick Setup
  stacks.
- `organizations` – Allows principals to read an organization's
  structure in AWS Organizations, and manage delegated administrators when they are onboarding to
  Systems Manager as an organization.
- `s3` – Allows principals to list and get objects in an Amazon S3 bucket
  for diagnosis, which is created during the Systems Manager onboarding process.
- `iam:PassRole` – Allows principals to pass roles to be assumed to
  Systems Manager when they run automations for diagnosis and remediation of unmanaged nodes.
- `iam:GetRole` – Allows principals to get specific role information
  for Quick Setup roles when they are working in Systems Manager.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ssm:*",
 "ssm-quicksetup:*"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowEC2DescribeActions",
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeInstanceStatus",
 "ec2:DescribeInstances",
 "ec2:DescribeRegions"
 ],
 "Resource": "*"
 },
 {
 "Sid": "CfnAccess",
 "Effect": "Allow",
 "Action": [
 "cloudformation:ListStacks",
 "cloudformation:ListStackSets",
 "cloudformation:ListStackInstances",
 "cloudformation:ListStackSetOperations",
 "cloudformation:ListStackSetOperationResults",
 "cloudformation:DescribeStacks",
 "cloudformation:DescribeStackSet",
 "cloudformation:DescribeStackSetOperation",
 "cloudformation:DescribeOrganizationsAccess",
 "cloudformation:DescribeStackInstance",
 "cloudformation:DetectStackSetDrift",
 "cloudformation:ListStackInstanceResourceDrifts"
 ],
 "Resource": "*"
 },
 {
 "Sid": "OrgsReadOnly",
 "Effect": "Allow",
 "Action": [
 "organizations:DescribeAccount",
 "organizations:DescribeOrganization",
 "organizations:ListDelegatedAdministrators",
 "organizations:ListRoots",
 "organizations:ListParents",
 "organizations:ListOrganizationalUnitsForParent",
 "organizations:DescribeOrganizationalUnit",
 "organizations:ListAWSServiceAccessForOrganization"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowKMSOperations",
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt",
 "kms:GenerateDataKey"
 ],
 "Resource": "arn:aws:kms:*:*:key/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/SystemsManagerManaged": "true"
 },
 "ArnLike": {
 "kms:EncryptionContext:aws:s3:arn": "arn:aws:s3:::do-not-delete-ssm-diagnosis-*"
 },
 "StringLike": {
 "kms:ViaService": "s3.*.amazonaws.com"
 },
 "Bool": {
 "aws:ViaAWSService": "true"
 }
 }
 },
 {
 "Sid": "AllowReadS3BucketFromOrganization",
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:ListBucket"
 ],
 "Resource": "arn:aws:s3:::do-not-delete-ssm-diagnosis*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceOrgId": "${aws:PrincipalOrgId}"
 }
 }
 },
 {
 "Sid": "AllowReadS3BucketFromSingleAccount",
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:ListBucket"
 ],
 "Resource": "arn:aws:s3:::do-not-delete-ssm-diagnosis*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": [
 "arn:aws:iam::*:role/AWS-SSM-DiagnosisAdminRole*",
 "arn:aws:iam::*:role/AWS-SSM-DiagnosisExecutionRole*",
 "arn:aws:iam::*:role/AWS-SSM-RemediationAdminRole*",
 "arn:aws:iam::*:role/AWS-SSM-RemediationExecutionRole*"
 ],
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": "ssm.amazonaws.com"
 }
 }
 },
 {
 "Sid": "IamReadOnly",
 "Effect": "Allow",
 "Action": "iam:GetRole",
 "Resource": [
 "arn:aws:iam::*:role/AWS-QuickSetup-*",
 "arn:aws:iam::*:role/service-role/AWS-QuickSetup-*"
 ]
 }
 ]
}`

```

## AWS Systems Manager console operator read-only

policy

You can create an IAM policy like the one shown in the following example, and attach
the policy to your IAM identities. This policy grants read-only access to use Systems Manager.

- `ssm` – Allows principals access to Systems Manager read-only APIs.
- `ssm-quicksetup` – Allows principals to read their Quick Setup
  configurations.
- `cloudformation` – Allows principals to read their Quick Setup
  stacks.
- `iam:GetRole` – Allows principals to get specific role information
  for Quick Setup roles when they are using Systems Manager.
- `ec2:DescribeRegions` – Allows Systems Manager to determine your enabled
  AWS Regions.
- `organizations` – Allows principals to read an organization's
  structure in AWS Organizations when they are onboarding to Systems Manager as an organization.
- `s3` – Allows principals to list and get objects in an Amazon S3 bucket
  that is created during the Systems Manager onboarding process.

**Permissions details**

This policy includes the following permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ssm:Describe*",
 "ssm:Get*",
 "ssm:List*",
 "ssm-quicksetup:List*",
 "ssm-quicksetup:Get*",
 "cloudformation:Describe*",
 "cloudformation:Get*",
 "cloudformation:List*",
 "iam:GetRole",
 "ec2:DescribeRegions",
 "organizations:Describe*",
 "organizations:List*"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowKMSOperations",
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt"
 ],
 "Resource": "arn:aws:kms:*:*:key/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/SystemsManagerManaged": "true"
 },
 "ArnLike": {
 "kms:EncryptionContext:aws:s3:arn": "arn:aws:s3:::do-not-delete-ssm-diagnosis-*"
 },
 "StringLike": {
 "kms:ViaService": "s3.*.amazonaws.com"
 },
 "Bool": {
 "aws:ViaAWSService": "true"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:ListBucket"
 ],
 "Resource": "arn:aws:s3:::do-not-delete-ssm-diagnosis*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceOrgId": "${aws:PrincipalOrgId}"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:ListBucket"
 ],
 "Resource": "arn:aws:s3:::do-not-delete-ssm-diagnosis*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 }
 ]
}`

```
