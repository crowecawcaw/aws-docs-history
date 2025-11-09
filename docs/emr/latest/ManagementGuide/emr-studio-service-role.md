# Create an EMR Studio service role

## About the EMR Studio service

role

Each EMR Studio uses an IAM role with permissions that let the Studio
interact with other AWS services. This service role must include permissions that allow
EMR Studio to establish a secure network channel between Workspaces and
clusters, to store notebook files in Amazon S3 Control, and to access the
AWS Secrets Manager while linking a Workspace to a Git
repository.

Use the Studio service role (instead of session policies) to define all
Amazon S3 access permissions for storing notebook files, and to define
AWS Secrets Manager access permissions.

## How to create a service role for

EMR Studio on Amazon EC2 or Amazon EKS

1. Follow the instructions in [Creating a role to
   delegate permissions to an AWS service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") to create the service role with the
   following trust policy.

###### Important

The following trust policy includes the [`aws:SourceArn`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn") and [`aws:SourceAccount`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount") global condition keys to limit the
permissions that you give EMR Studio to particular resources in your account.
Doing so can protect you against [the confused deputy
problem](../../../IAM/latest/UserGuide/confused-deputy.md "../../../IAM/latest/UserGuide/confused-deputy.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "sts:AssumeRole"
 ],
 "Resource": "arn:aws:iam::123456789012:role/EMRStudioServiceRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "123456789012"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:elasticmapreduce:*:123456789012:*"
 }
 },
 "Sid": "AllowSTSAssumerole"
 }
 ]
}`

```

2. Remove the default role permissions. Then, include the permissions from the
   following sample IAM permissions policy. Alternatively, you can create a custom policy
   that uses the [EMR Studio service role
   permissions](#emr-studio-service-role-permissions-table "#emr-studio-service-role-permissions-table").

###### Important

    * For Amazon EC2 tag-based access control with to work with EMR Studio, you
     must set access for the `ModifyNetworkInterfaceAttribute` API as
     shown the following policy.
    * For EMR Studio to work with the service role, you must not change the
     following statements:
     `AllowAddingEMRTagsDuringDefaultSecurityGroupCreation` and
     `AllowAddingTagsDuringEC2ENICreation`.
    * To use the example policy, you must tag the following resources with the key
     `"**for-use-with-amazon-emr-managed-policies**"` and value
     `"**true**"`.




    	+ Your Amazon Virtual Private Cloud (VPC) for EMR Studio.
    	+ Each subnet that you want to use with the Studio.
    	+ Any custom EMR Studio security groups. You must tag any security
    	 groups that you created during the EMR Studio preview period if you want
    	 to continue to use them.
    	+ Secrets maintained in AWS Secrets Manager that Studio
    	 users use to link Git repositories to a Workspace.
    You can apply tags to resources using the **Tags** tab on
     the relevant resource screen in the AWS Management Console.

Where applicable, change the `*` in
`"Resource":"`\*`"` in the following policy to
specify the Amazon Resource Name (ARN) of the resources that the statement covers for
your use case.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowEMRReadOnlyActions",
 "Effect": "Allow",
 "Action": [
 "elasticmapreduce:ListInstances",
 "elasticmapreduce:DescribeCluster",
 "elasticmapreduce:ListSteps"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "AllowEC2ENIActionsWithEMRTags",
 "Effect": "Allow",
 "Action": [
 "ec2:CreateNetworkInterfacePermission",
 "ec2:DeleteNetworkInterface"
 ],
 "Resource": [
 "arn:aws:ec2:*:*:network-interface/*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/for-use-with-amazon-emr-managed-policies": "true"
 }
 }
 },
 {
 "Sid": "AllowEC2ENIAttributeAction",
 "Effect": "Allow",
 "Action": [
 "ec2:ModifyNetworkInterfaceAttribute"
 ],
 "Resource": [
 "arn:aws:ec2:*:*:instance/*",
 "arn:aws:ec2:*:*:network-interface/*",
 "arn:aws:ec2:*:*:security-group/*"
 ]
 },
 {
 "Sid": "AllowEC2SecurityGroupActionsWithEMRTags",
 "Effect": "Allow",
 "Action": [
 "ec2:AuthorizeSecurityGroupEgress",
 "ec2:AuthorizeSecurityGroupIngress",
 "ec2:RevokeSecurityGroupEgress",
 "ec2:RevokeSecurityGroupIngress",
 "ec2:DeleteNetworkInterfacePermission"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/for-use-with-amazon-emr-managed-policies": "true"
 }
 }
 },
 {
 "Sid": "AllowDefaultEC2SecurityGroupsCreationWithEMRTags",
 "Effect": "Allow",
 "Action": [
 "ec2:CreateSecurityGroup"
 ],
 "Resource": [
 "arn:aws:ec2:*:*:security-group/*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/for-use-with-amazon-emr-managed-policies": "true"
 }
 }
 },
 {
 "Sid": "AllowDefaultEC2SecurityGroupsCreationInVPCWithEMRTags",
 "Effect": "Allow",
 "Action": [
 "ec2:CreateSecurityGroup"
 ],
 "Resource": [
 "arn:aws:ec2:*:*:vpc/*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/for-use-with-amazon-emr-managed-policies": "true"
 }
 }
 },
 {
 "Sid": "AllowAddingEMRTagsDuringDefaultSecurityGroupCreation",
 "Effect": "Allow",
 "Action": [
 "ec2:CreateTags"
 ],
 "Resource": [
 "arn:aws:ec2:*:*:security-group/*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/for-use-with-amazon-emr-managed-policies": "true",
 "ec2:CreateAction": "CreateSecurityGroup"
 }
 }
 },
 {
 "Sid": "AllowEC2ENICreationWithEMRTags",
 "Effect": "Allow",
 "Action": [
 "ec2:CreateNetworkInterface"
 ],
 "Resource": [
 "arn:aws:ec2:*:*:network-interface/*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/for-use-with-amazon-emr-managed-policies": "true"
 }
 }
 },
 {
 "Sid": "AllowEC2ENICreationInSubnetAndSecurityGroupWithEMRTags",
 "Effect": "Allow",
 "Action": [
 "ec2:CreateNetworkInterface"
 ],
 "Resource": [
 "arn:aws:ec2:*:*:subnet/*",
 "arn:aws:ec2:*:*:security-group/*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/for-use-with-amazon-emr-managed-policies": "true"
 }
 }
 },
 {
 "Sid": "AllowAddingTagsDuringEC2ENICreation",
 "Effect": "Allow",
 "Action": [
 "ec2:CreateTags"
 ],
 "Resource": [
 "arn:aws:ec2:*:*:network-interface/*"
 ],
 "Condition": {
 "StringEquals": {
 "ec2:CreateAction": "CreateNetworkInterface"
 }
 }
 },
 {
 "Sid": "AllowEC2ReadOnlyActions",
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeSecurityGroups",
 "ec2:DescribeNetworkInterfaces",
 "ec2:DescribeTags",
 "ec2:DescribeInstances",
 "ec2:DescribeSubnets",
 "ec2:DescribeVpcs"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "AllowSecretsManagerReadOnlyActionsWithEMRTags",
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetSecretValue"
 ],
 "Resource": [
 "arn:aws:secretsmanager:*:*:secret:*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/for-use-with-amazon-emr-managed-policies": "true"
 }
 }
 },
 {
 "Sid": "AllowWorkspaceCollaboration",
 "Effect": "Allow",
 "Action": [
 "iam:GetUser",
 "iam:GetRole",
 "iam:ListUsers",
 "iam:ListRoles",
 "sso:GetManagedApplicationInstance",
 "sso-directory:SearchUsers"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

3. Give your service role read and write access to your Amazon S3 location
   for EMR Studio. Use the following minimum set of permissions. For more
   information, see the [Amazon S3: Allows read and write access to objects in an S3 Bucket,
   programmatically and in the console](../../../IAM/latest/UserGuide/reference_policies_examples_s3_rw-bucket-console.md "../../../IAM/latest/UserGuide/reference_policies_examples_s3_rw-bucket-console.md") example.

```
"s3:PutObject",
"s3:GetObject",
"s3:GetEncryptionConfiguration",
"s3:ListBucket",
"s3:DeleteObject"
```

If you encrypt your Amazon S3 bucket, include the following permissions
for AWS Key Management Service.

```
"kms:Decrypt",
"kms:GenerateDataKey",
"kms:ReEncryptFrom",
"kms:ReEncryptTo",
"kms:DescribeKey"
```

[Show moreShow less](# "#") 4. If you want to control access to Git secrets at user level, add tag-based
permissions to `secretsmanager:GetSecretValue` in the EMR Studio
**user role policy**, and remove permissions to
`secretsmanager:GetSecretValue` policy from the EMR Studio **service role policy**. For more information on setting
fine-grained user permissions, see [Create permissions policies for
EMR Studio users](emr-studio-user-permissions.md#emr-studio-permissions-policies "emr-studio-user-permissions.md#emr-studio-permissions-policies").

## Minimum service role for

EMR Serverless

If you want to run interactive workloads with EMR Serverless through EMR Studio
notebooks, use the same trust policy that you use to set up EMR Studio in the previous
section, [How to create a service role for
EMR Studio on Amazon EC2 or Amazon EKS](#emr-studio-service-role-instructions "#emr-studio-service-role-instructions").

For your IAM policy, the minimum viable policy has permissions as follows. Update
`bucket-name` with the name of the bucket that
you plan to use when you configure your EMR Studio and Workspace. EMR Studio uses
the bucket back up the Workspaces and notebook files in your Studio.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ObjectActions",
 "Effect": "Allow",
 "Action": [
 "s3:PutObject",
 "s3:GetObject",
 "s3:DeleteObject"
 ],
 "Resource": [
 "arn:aws:s3:::`bucket-name`/*"
 ]
 },
 {
 "Sid": "BucketActions",
 "Effect": "Allow",
 "Action": [
 "s3:ListBucket",
 "s3:GetEncryptionConfiguration"
 ],
 "Resource": [
 "arn:aws:s3:::`bucket-name`"
 ]
 }
 ]
}`

```

If you plan to use an encrypted Amazon S3 bucket, add the following permissions on your
policy:

```
"kms:Decrypt",
"kms:GenerateDataKey",
"kms:ReEncryptFrom",
"kms:ReEncryptTo",
"kms:DescribeKey"
```

## EMR Studio service role

permissions

The following table lists the operations that EMR Studio performs using the
service role, along with the IAM actions required for each operation.

| Operation                                                                                                                                                                                                                                                                                   | Actions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Establish a secure network channel between a Workspace and an<br>EMR cluster, and perform necessary cleanup actions.                                                                                                                                                                        | `<br>"ec2:CreateNetworkInterface",<br>"ec2:CreateNetworkInterfacePermission",<br>"ec2:DeleteNetworkInterface",<br>"ec2:DeleteNetworkInterfacePermission",<br>"ec2:DescribeNetworkInterfaces",<br>"ec2:ModifyNetworkInterfaceAttribute",<br>"ec2:AuthorizeSecurityGroupEgress",<br>"ec2:AuthorizeSecurityGroupIngress",<br>"ec2:CreateSecurityGroup",<br>"ec2:DescribeSecurityGroups",<br>"ec2:RevokeSecurityGroupEgress",<br>"ec2:DescribeTags",<br>"ec2:DescribeInstances",<br>"ec2:DescribeSubnets",<br>"ec2:DescribeVpcs",<br>"elasticmapreduce:ListInstances",<br>"elasticmapreduce:DescribeCluster",<br>"elasticmapreduce:ListSteps"<br>` |
| Use Git credentials stored in AWS Secrets Manager to link Git<br>repositories to a Workspace.                                                                                                                                                                                               | `<br>"secretsmanager:GetSecretValue"<br>`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Apply AWS tags to the network interface and default security groups that<br>EMR Studio creates while setting up the secure network channel. For more<br>information, see [Tagging AWS<br>resources](../../../general/latest/gr/aws_tagging.md "../../../general/latest/gr/aws_tagging.md"). | `<br>"ec2:CreateTags"<br>`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Access or upload notebook files and metadata to Amazon S3.                                                                                                                                                                                                                                  | `<br>"s3:PutObject",<br>"s3:GetObject",<br>"s3:GetEncryptionConfiguration",<br>"s3:ListBucket",<br>"s3:DeleteObject"<br>`<br>If you use an encrypted Amazon S3 bucket, include the following<br>permissions.<br>`<br>"kms:Decrypt",<br>"kms:GenerateDataKey",<br>"kms:ReEncryptFrom",<br>"kms:ReEncryptTo",<br>"kms:DescribeKey"<br>`                                                                                                                                                                                                                                                                                                          |
| Enable and configure Workspace collaboration.                                                                                                                                                                                                                                               | `<br>"iam:GetUser",<br>"iam:GetRole",<br>"iam:ListUsers",<br>"iam:ListRoles",<br>"sso:GetManagedApplicationInstance",<br>"sso-directory:SearchUsers",<br>"sso:DescribeApplication",<br>"sso:DescribeInstance"<br>`                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [Encrypt EMR Studio workspace notebooks and files using customer managed keys (CMK) with AWS Key Management Service](emr-studio-workspace-storage-encryption.md "emr-studio-workspace-storage-encryption.md")                                                                               | `<br>"kms:Decrypt",<br>"kms:GenerateDataKey",<br>"kms:ReEncryptFrom",<br>"kms:ReEncryptTo",<br>"kms:DescribeKey"<br>`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
