# AWS managed policies for WorkSpaces

Using AWS managed policies makes adding permissions to users, groups, and roles easier
than writing policies yourself. It takes time and expertise to create [IAM
customer managed policies](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") that provide your team with only the permissions they
need. Use AWS managed policies to get started quickly. These policies cover common use
cases and are available in your AWS account. For more information about AWS managed
policies, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the _IAM User Guide_.

AWS services maintain and update AWS managed policies. You can't change the
permissions in AWS managed policies. Services may occasionally add additional permissions
to an AWS managed policy to support new features. This type of update affects all
identities (users, groups, and roles) where the policy is attached. Services are most likely
to update an AWS managed policy when a new feature is launched or when new operations
become available. Services don't remove permissions from an AWS managed policy, so policy
updates won't break your existing permissions.

Additionally, AWS supports managed policies for job functions that span multiple
services. For example, the `ReadOnlyAccess` AWS managed policy provides
read-only access to all AWS services and resources. When a service launches a new feature,
AWS adds read-only permissions for new operations and resources. For a list and
descriptions of job function policies, see [AWS managed policies for
job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md") in the _IAM User Guide_.

## AWS managed policy: AmazonWorkSpacesAdmin

###### Note

Permissions listed are for SDK only and will not work for the Console. Console
requires additional permissions listed in [Amazon WorkSpaces Console operations permissions reference](wsp-console-permissions-ref.md "wsp-console-permissions-ref.md").

This policy provides access to Amazon WorkSpaces administrative actions. It provides the
following permissions:

- `workspaces` - Allows access to perform administrative actions on
  WorkSpaces Personal and WorkSpaces Pools resources.
- `kms` - Allows access to list and describe KMS keys, as well as
  list aliases.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AmazonWorkSpacesAdmin",
 "Effect": "Allow",
 "Action": [
 "kms:DescribeKey",
 "kms:ListAliases",
 "kms:ListKeys",
 "workspaces:CreateTags",
 "workspaces:CreateWorkspaceImage",
 "workspaces:CreateWorkspaces",
 "workspaces:CreateWorkspacesPool",
 "workspaces:CreateStandbyWorkspaces",
 "workspaces:DeleteTags",
 "workspaces:DeregisterWorkspaceDirectory",
 "workspaces:DescribeTags",
 "workspaces:DescribeWorkspaceBundles",
 "workspaces:DescribeWorkspaceDirectories",
 "workspaces:DescribeWorkspaces",
 "workspaces:DescribeWorkspacesPools",
 "workspaces:DescribeWorkspacesPoolSessions",
 "workspaces:DescribeWorkspacesConnectionStatus",
 "workspaces:ModifyCertificateBasedAuthProperties",
 "workspaces:ModifySamlProperties",
 "workspaces:ModifyStreamingProperties",
 "workspaces:ModifyWorkspaceCreationProperties",
 "workspaces:ModifyWorkspaceProperties",
 "workspaces:RebootWorkspaces",
 "workspaces:RebuildWorkspaces",
 "workspaces:RegisterWorkspaceDirectory",
 "workspaces:RestoreWorkspace",
 "workspaces:StartWorkspaces",
 "workspaces:StartWorkspacesPool",
 "workspaces:StopWorkspaces",
 "workspaces:StopWorkspacesPool",
 "workspaces:TerminateWorkspaces",
 "workspaces:TerminateWorkspacesPool",
 "workspaces:TerminateWorkspacesPoolSession",
 "workspaces:UpdateWorkspacesPool"
 ],
 "Resource": "*"
 }
 ]
}`

```

## AWS managed policy:

AmazonWorkspacesPCAAccess

This managed policy provides access to AWS Certificate Manager Private Certificate
Authority (Private CA) resources in your AWS account for certificate-based
authentication. It is included in the AmazonWorkSpacesPCAAccess role, and it provides the
following permissions:

- `acm-pca` - Allows access to AWS Private CA to manage
  certificate-based authentication.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "acm-pca:IssueCertificate",
 "acm-pca:GetCertificate",
 "acm-pca:DescribeCertificateAuthority"
 ],
 "Resource": "arn:*:acm-pca:*:*:*",
 "Condition": {
 "StringLike": {
 "aws:ResourceTag/euc-private-ca": "*"
 }
 }
 }
 ]
}`

```

## AWS managed policy:

AmazonWorkSpacesSelfServiceAccess

This policy provides access to the Amazon WorkSpaces service to perform WorkSpaces self-service
actions initiated by a user. It is included in the `workspaces_DefaultRole`
role, and it provides the following permissions:

- `workspaces` - Allows access to self-service WorkSpaces management
  capabilities for users.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "workspaces:RebootWorkspaces",
 "workspaces:RebuildWorkspaces",
 "workspaces:ModifyWorkspaceProperties"
 ],
 "Effect": "Allow",
 "Resource": "*"
 }
 ]
}`

```

## AWS managed policy:

AmazonWorkSpacesServiceAccess

This policy provides customer account access to the Amazon WorkSpaces service for launching a
WorkSpace. It is included in the `workspaces_DefaultRole` role, and it
provides the following permissions:

- `ec2` - Allows access to manage Amazon EC2 resources associated with a
  WorkSpace, such as network interfaces.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "ec2:CreateNetworkInterface",
 "ec2:DeleteNetworkInterface",
 "ec2:DescribeNetworkInterfaces"
 ],
 "Effect": "Allow",
 "Resource": "*"
 }
 ]
}`

```

## AWS managed policy:

AmazonWorkSpacesPoolServiceAccess

This policy is used in the workspaces_DefaultRole, which WorkSpaces uses to access required
resources in the customer AWS account for WorkSpaces Pools. For more information see [Create the workspaces_DefaultRole Role](workspaces-access-control.md#create-default-role "workspaces-access-control.md#create-default-role"). It provides the
following permissions:

- `ec2` - Allows access to manage Amazon EC2 resources associated with a
  WorkSpaces Pool, such as VPCs, subnets, availability zones, security groups, and route
  tables.
- `s3` - Allows access to perform actions on Amazon S3 buckets required
  for logs, application settings, and the Home Folder feature.

Commercial AWS Regions
The following policy JSON applies to the commercial AWS Regions.

JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ProvisioningWorkSpacesPoolPermissions",
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeVpcs",
 "ec2:DescribeSubnets",
 "ec2:DescribeAvailabilityZones",
 "ec2:DescribeSecurityGroups",
 "ec2:DescribeRouteTables",
 "s3:ListAllMyBuckets"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 },
 {
 "Sid": "WorkSpacesPoolS3Permissions",
 "Effect": "Allow",
 "Action": [
 "s3:CreateBucket",
 "s3:ListBucket",
 "s3:GetObject",
 "s3:PutObject",
 "s3:DeleteObject",
 "s3:GetObjectVersion",
 "s3:DeleteObjectVersion",
 "s3:GetBucketPolicy",
 "s3:PutBucketPolicy",
 "s3:PutEncryptionConfiguration"
 ],
 "Resource": [
 "arn:aws:s3:::wspool-logs-*",
 "arn:aws:s3:::wspool-app-settings-*",
 "arn:aws:s3:::wspool-home-folder-*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 }
 ]
}`

```

AWS GovCloud (US) Regions
The following policy JSON applies to the commercial
AWS GovCloud (US) Regions.

JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ProvisioningWorkSpacesPoolPermissions",
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeVpcs",
 "ec2:DescribeSubnets",
 "ec2:DescribeAvailabilityZones",
 "ec2:DescribeSecurityGroups",
 "ec2:DescribeRouteTables",
 "s3:ListAllMyBuckets"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 },
 {
 "Sid": "WorkSpacesPoolS3Permissions",
 "Effect": "Allow",
 "Action": [
 "s3:CreateBucket",
 "s3:ListBucket",
 "s3:GetObject",
 "s3:PutObject",
 "s3:DeleteObject",
 "s3:GetObjectVersion",
 "s3:DeleteObjectVersion",
 "s3:GetBucketPolicy",
 "s3:PutBucketPolicy",
 "s3:PutEncryptionConfiguration"
 ],
 "Resource": [
 "arn:aws-us-gov:s3:::wspool-logs-*",
 "arn:aws-us-gov:s3:::wspool-app-settings-*",
 "arn:aws-us-gov:s3:::wspool-home-folder-*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 }
 ]
}`

```

## WorkSpaces updates to AWS managed

policies

View details about updates to AWS managed policies for WorkSpaces since this service
began tracking these changes.

| Change                                                                                                                                          | Description                                                                                                                                                             | Date              |
| ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| [AWS managed policy: AmazonWorkSpacesPoolServiceAccess](#workspaces-pools-service-access "#workspaces-pools-service-access") - Added new policy | WorkSpaces added a new managed policy to grant permission to view Amazon EC2 VPCs and related resources, and to view and manage Amazon S3 buckets for WorkSpaces Pools. | June 24, 2024     |
| [AWS managed policy: AmazonWorkSpacesAdmin](#workspaces-admin "#workspaces-admin") - Updated policy                                             | WorkSpaces added several actions for WorkSpaces Pools to the Amazon WorkSpacesAdmin managed policy, granting admins access to manage WorkSpace Pool resources.          | June 24, 2024     |
| [AWS managed policy: AmazonWorkSpacesAdmin](#workspaces-admin "#workspaces-admin") - Updated policy                                             | WorkSpaces added the `workspaces:RestoreWorkspace` action to the Amazon WorkSpacesAdmin managed policy, granting admins access to restore WorkSpaces.                   | June 25, 2023     |
| [AWS managed policy: AmazonWorkspacesPCAAccess](#workspaces-pca-access "#workspaces-pca-access") - Added new policy                             | WorkSpaces added a new managed policy to grant `acm-pca` permission to manage AWS Private CA to manage certificate-based authentication.                                | November 18, 2022 |
| WorkSpaces started tracking changes                                                                                                             | WorkSpaces started tracking changes for its WorkSpaces managed policies.                                                                                                | March 1, 2021     |
