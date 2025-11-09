# AWS Managed Policies for SageMaker Notebooks

These AWS managed policies add permissions required to use SageMaker Notebooks. The policies
are available in your AWS account and are used by execution roles created from the SageMaker AI console.

###### Topics

- [AWS
  managed policy: AmazonSageMakerNotebooksServiceRolePolicy](#security-iam-awsmanpol-AmazonSageMakerNotebooksServiceRolePolicy "#security-iam-awsmanpol-AmazonSageMakerNotebooksServiceRolePolicy")
- [Amazon SageMaker AI updates to SageMaker AI
  Notebooks managed policies](#security-iam-awsmanpol-notebooks-updates "#security-iam-awsmanpol-notebooks-updates")

## AWS

managed policy: AmazonSageMakerNotebooksServiceRolePolicy

This AWS managed policy grants permissions commonly needed to use Amazon SageMaker Notebooks.
The policy is added to the `AWSServiceRoleForAmazonSageMakerNotebooks` that is created when
you onboard to Amazon SageMaker Studio Classic. For more information on service-linked roles, see
[Service-linked roles](security_iam_service-with-iam.md#security_iam_service-with-iam-roles-service-linked "security_iam_service-with-iam.md#security_iam_service-with-iam-roles-service-linked"). For more information,
see [AmazonSageMakerNotebooksServiceRolePolicy](../../../aws-managed-policy/latest/reference/AmazonSageMakerNotebooksServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AmazonSageMakerNotebooksServiceRolePolicy.md")

**Permissions details**

This policy includes the following permissions.

- `elasticfilesystem` – Allows principals to create and delete
  Amazon Elastic File System (EFS) file systems, access points, and mount targets. These are limited to those
  tagged with the key _ManagedByAmazonSageMakerResource_. Allows
  principals to describe all EFS file systems, access points, and mount targets. Allows
  principals to create or overwrite tags for EFS access points and mount targets.
- `ec2` – Allows principals to create network interfaces and
  security groups for Amazon Elastic Compute Cloud (EC2) instances. Also allows principals to create and
  overwrite tags for these resources.
- `sso` – Allows principals to add and delete managed application
  instances to AWS IAM Identity Center.
- `sagemaker` – Allows principals to create and read SageMaker AI
  user profiles and SageMaker AI spaces; delete SageMaker AI spaces and SageMaker AI apps; and add and list tags.
- `fsx` – Allows principals to describe Amazon FSx for Lustre file system,
  and use the metadata to mount it on notebook.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowFSxDescribe",
 "Effect": "Allow",
 "Action": [
 "fsx:DescribeFileSystems"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 },
 {
 "Sid": "AllowSageMakerDeleteApp",
 "Effect": "Allow",
 "Action": [
 "sagemaker:DeleteApp"
 ],
 "Resource": "arn:aws:sagemaker:*:*:app/*"
 },
 {
 "Sid": "AllowEFSAccessPointCreation",
 "Effect": "Allow",
 "Action": "elasticfilesystem:CreateAccessPoint",
 "Resource": "arn:aws:elasticfilesystem:*:*:file-system/*",
 "Condition": {
 "StringLike": {
 "aws:ResourceTag/ManagedByAmazonSageMakerResource": "*",
 "aws:RequestTag/ManagedByAmazonSageMakerResource": "*"
 }
 }
 },
 {
 "Sid": "AllowEFSAccessPointDeletion",
 "Effect": "Allow",
 "Action": [
 "elasticfilesystem:DeleteAccessPoint"
 ],
 "Resource": "arn:aws:elasticfilesystem:*:*:access-point/*",
 "Condition": {
 "StringLike": {
 "aws:ResourceTag/ManagedByAmazonSageMakerResource": "*"
 }
 }
 },
 {
 "Sid": "AllowEFSCreation",
 "Effect": "Allow",
 "Action": "elasticfilesystem:CreateFileSystem",
 "Resource": "*",
 "Condition": {
 "StringLike": {
 "aws:RequestTag/ManagedByAmazonSageMakerResource": "*"
 }
 }
 },
 {
 "Sid": "AllowEFSMountWithDeletion",
 "Effect": "Allow",
 "Action": [
 "elasticfilesystem:CreateMountTarget",
 "elasticfilesystem:DeleteFileSystem",
 "elasticfilesystem:DeleteMountTarget"
 ],
 "Resource": "*",
 "Condition": {
 "StringLike": {
 "aws:ResourceTag/ManagedByAmazonSageMakerResource": "*"
 }
 }
 },
 {
 "Sid": "AllowEFSDescribe",
 "Effect": "Allow",
 "Action": [
 "elasticfilesystem:DescribeAccessPoints",
 "elasticfilesystem:DescribeFileSystems",
 "elasticfilesystem:DescribeMountTargets"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowEFSTagging",
 "Effect": "Allow",
 "Action": "elasticfilesystem:TagResource",
 "Resource": [
 "arn:aws:elasticfilesystem:*:*:access-point/*",
 "arn:aws:elasticfilesystem:*:*:file-system/*"
 ],
 "Condition": {
 "StringLike": {
 "aws:ResourceTag/ManagedByAmazonSageMakerResource": "*"
 }
 }
 },
 {
 "Sid": "AllowEC2Tagging",
 "Effect": "Allow",
 "Action": "ec2:CreateTags",
 "Resource": [
 "arn:aws:ec2:*:*:network-interface/*",
 "arn:aws:ec2:*:*:security-group/*"
 ]
 },
 {
 "Sid": "AllowEC2Operations",
 "Effect": "Allow",
 "Action": [
 "ec2:CreateNetworkInterface",
 "ec2:CreateSecurityGroup",
 "ec2:DeleteNetworkInterface",
 "ec2:DescribeDhcpOptions",
 "ec2:DescribeNetworkInterfaces",
 "ec2:DescribeSecurityGroups",
 "ec2:DescribeSubnets",
 "ec2:DescribeVpcs",
 "ec2:ModifyNetworkInterfaceAttribute"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowEC2AuthZ",
 "Effect": "Allow",
 "Action": [
 "ec2:AuthorizeSecurityGroupEgress",
 "ec2:AuthorizeSecurityGroupIngress",
 "ec2:CreateNetworkInterfacePermission",
 "ec2:DeleteNetworkInterfacePermission",
 "ec2:DeleteSecurityGroup",
 "ec2:RevokeSecurityGroupEgress",
 "ec2:RevokeSecurityGroupIngress"
 ],
 "Resource": "*",
 "Condition": {
 "StringLike": {
 "ec2:ResourceTag/ManagedByAmazonSageMakerResource": "*"
 }
 }
 },
 {
 "Sid": "AllowIdcOperations",
 "Effect": "Allow",
 "Action": [
 "sso:CreateManagedApplicationInstance",
 "sso:DeleteManagedApplicationInstance",
 "sso:GetManagedApplicationInstance"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowSagemakerProfileCreation",
 "Effect": "Allow",
 "Action": [
 "sagemaker:CreateUserProfile",
 "sagemaker:DescribeUserProfile"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowSagemakerSpaceOperationsForCanvasManagedSpaces",
 "Effect": "Allow",
 "Action": [
 "sagemaker:CreateSpace",
 "sagemaker:DescribeSpace",
 "sagemaker:DeleteSpace",
 "sagemaker:ListTags"
 ],
 "Resource": "arn:aws:sagemaker:*:*:space/*/CanvasManagedSpace-*"
 },
 {
 "Sid": "AllowSagemakerAddTagsForAppManagedSpaces",
 "Effect": "Allow",
 "Action": [
 "sagemaker:AddTags"
 ],
 "Resource": "arn:aws:sagemaker:*:*:space/*/CanvasManagedSpace-*",
 "Condition": {
 "StringEquals": {
 "sagemaker:TaggingAction": "CreateSpace"
 }
 }
 }
 ]
}`

```

## Amazon SageMaker AI updates to SageMaker AI

Notebooks managed policies

View details about updates to AWS managed policies for Amazon SageMaker AI since this service
began tracking these changes.

| Policy                                                                                                                                                                                                               | Version | Change                                                                                                                                            | Date              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| [AmazonSageMakerNotebooksServiceRolePolicy](#security-iam-awsmanpol-AmazonSageMakerNotebooksServiceRolePolicy "#security-iam-awsmanpol-AmazonSageMakerNotebooksServiceRolePolicy")<br>• Update to an existing policy | 10      | Add `fsx:DescribeFileSystems` permission.                                                                                                         | November 14, 2024 |
| [AmazonSageMakerNotebooksServiceRolePolicy](#security-iam-awsmanpol-AmazonSageMakerNotebooksServiceRolePolicy "#security-iam-awsmanpol-AmazonSageMakerNotebooksServiceRolePolicy")<br>• Update to an existing policy | 9       | Add `sagemaker:DeleteApp` permission.                                                                                                             | July 24, 2024     |
| AmazonSageMakerNotebooksServiceRolePolicy<br>• Update to an existing policy                                                                                                                                          | 8       | Add `sagemaker:CreateSpace`,<br>`sagemaker:DescribeSpace`, `sagemaker:DeleteSpace`,<br>`sagemaker:ListTags`, and `sagemaker:AddTags` permissions. | May 22, 2024      |
| AmazonSageMakerNotebooksServiceRolePolicy<br>• Update to an existing policy                                                                                                                                          | 7       | Add `elasticfilesystem:TagResource` permission.                                                                                                   | March 9, 2023     |
| AmazonSageMakerNotebooksServiceRolePolicy<br>• Update to an existing policy                                                                                                                                          | 6       | Add `elasticfilesystem:CreateAccessPoint`,<br>`elasticfilesystem:DeleteAccessPoint`, and<br>`elasticfilesystem:DescribeAccessPoints` permissions. | January 12, 2023  |
|                                                                                                                                                                                                                      |         | SageMaker AI started tracking changes for its AWS managed policies.                                                                               | June 1, 2021      |
