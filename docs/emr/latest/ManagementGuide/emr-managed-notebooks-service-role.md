# Service role for

EMR Notebooks

Each EMR notebook needs permissions to access other AWS resources and
perform actions. The IAM policies attached to this service role provide
permissions for the notebook to interoperate with other AWS services. When you
create a notebook using the AWS Management Console, you specify an _AWS service
role_. You can use the default role,
`EMR_Notebooks_DefaultRole`, or specify a role that you create. If a
notebook has not been created before, you can choose to create the default
role.

- The default role name is `EMR_Notebooks_DefaultRole`.
- The default managed policies attached to
  `EMR_Notebooks_DefaultRole` are
  `AmazonElasticMapReduceEditorsRole` and
  `S3FullAccessPolicy`.
  Your service role should use the following trust policy.

###### Important

The following trust policy includes the [`aws:SourceArn`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn") and [`aws:SourceAccount`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount") global condition keys, which
limit the permissions that you give Amazon EMR to particular resources in your
account. Using them can protect you against [the confused deputy
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
 "Resource": "arn:aws:iam::123456789012:role/EMRServiceRole",
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

The contents of version 1 of `AmazonElasticMapReduceEditorsRole` are as
follows.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ec2:AuthorizeSecurityGroupEgress",
 "ec2:AuthorizeSecurityGroupIngress",
 "ec2:CreateSecurityGroup",
 "ec2:DescribeSecurityGroups",
 "ec2:RevokeSecurityGroupEgress",
 "ec2:CreateNetworkInterface",
 "ec2:CreateNetworkInterfacePermission",
 "ec2:DeleteNetworkInterface",
 "ec2:DeleteNetworkInterfacePermission",
 "ec2:DescribeNetworkInterfaces",
 "ec2:ModifyNetworkInterfaceAttribute",
 "ec2:DescribeTags",
 "ec2:DescribeInstances",
 "ec2:DescribeSubnets",
 "ec2:DescribeVpcs",
 "elasticmapreduce:ListInstances",
 "elasticmapreduce:DescribeCluster",
 "elasticmapreduce:ListSteps"
 ],
 "Resource": [
 "*"
 ],
 "Sid": "AllowEC2Authorizesecuritygroupegress"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:CreateTags"
 ],
 "Resource": [
 "arn:aws:ec2:*:*:network-interface/*"
 ],
 "Condition": {
 "ForAllValues:StringEquals": {
 "aws:TagKeys": [
 "aws:elasticmapreduce:editor-id",
 "aws:elasticmapreduce:job-flow-id"
 ]
 }
 },
 "Sid": "AllowEC2Createtags"
 }
 ]
}`

```

Following is the contents of the `S3FullAccessPolicy`. The
`S3FullAccessPolicy` allows your service role for EMR Notebooks to
perform all Amazon S3 actions on objects in your AWS account. When you
create a custom service role for EMR Notebooks, you must give your service role
Amazon S3 permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:*"
 ],
 "Resource": [
 "*"
 ],
 "Sid": "AllowS3"
 }
 ]
}`

```

You can scope down read and write access for your service role to the
Amazon S3 location where you want to save your notebook files. Use the
following minimum set of Amazon S3 permissions.

```
"s3:PutObject",
"s3:GetObject",
"s3:GetEncryptionConfiguration",
"s3:ListBucket",
"s3:DeleteObject"
```

If your Amazon S3 bucket is encrypted, you must include the following
permissions for AWS Key Management Service.

```
"kms:Decrypt",
"kms:GenerateDataKey",
"kms:ReEncryptFrom",
"kms:ReEncryptTo",
"kms:DescribeKey"
```

When you link Git repositories to your notebook and need to create a secret for
the repository, you must add the `secretsmanager:GetSecretValue`
permission in the IAM policy attached to the service role for Amazon EMR notebooks. An
example policy is demonstrated below:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetSecretValue"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

## EMR Notebooks

service role permissions

This table lists the actions that EMR Notebooks takes using the service role,
along with the permissions that are needed for each action.

| Action                                                                                                                                                                                                                                                                                | Permissions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Establish a secure network channel between a notebook and an Amazon EMR cluster, and perform necessary cleanup actions.                                                                                                                                                               | `"ec2:CreateNetworkInterface", "ec2:CreateNetworkInterfacePermission", "ec2:DeleteNetworkInterface", "ec2:DeleteNetworkInterfacePermission", "ec2:DescribeNetworkInterfaces", "ec2:ModifyNetworkInterfaceAttribute", "ec2:AuthorizeSecurityGroupEgress", "ec2:AuthorizeSecurityGroupIngress", "ec2:CreateSecurityGroup", "ec2:DescribeSecurityGroups", "ec2:RevokeSecurityGroupEgress", "ec2:DescribeTags", "ec2:DescribeInstances", "ec2:DescribeSubnets", "ec2:DescribeVpcs", "elasticmapreduce:ListInstances", "elasticmapreduce:DescribeCluster", "elasticmapreduce:ListSteps"` |
| Use Git credentials stored in AWS Secrets Manager to link Git repositories to a notebook.                                                                                                                                                                                             | `"secretsmanager:GetSecretValue"`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Apply AWS tags to the network interface and default security groups that EMR Notebooks creates while setting up the secure network channel. For more information, see [Tagging AWS resources](../../../general/latest/gr/aws_tagging.md "../../../general/latest/gr/aws_tagging.md"). | `"ec2:CreateTags"`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Access or upload notebook files and metadata to Amazon S3.                                                                                                                                                                                                                            | `"s3:PutObject", "s3:GetObject", "s3:GetEncryptionConfiguration", "s3:ListBucket", "s3:DeleteObject"` The following permissions are only required if you use an encrypted Amazon S3 bucket. `"kms:Decrypt", "kms:GenerateDataKey", "kms:ReEncryptFrom", "kms:ReEncryptTo", "kms:DescribeKey"`                                                                                                                                                                                                                                                                                       | ## EMR Notebooks updates to AWS managed policies View details about updates to AWS managed policies for EMR Notebooks since March 1, 2021. |
| Change                                                                                                                                                                                                                                                                                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Date                                                                                                                                       |
| ---                                                                                                                                                                                                                                                                                   | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | ---                                                                                                                                        |
| `AmazonElasticMapReduceEditorsRole - Added permissions`                                                                                                                                                                                                                               | EMR Notebooks added `ec2:describeVPCs` and `elastmicmapreduce:ListSteps` permissions to `AmazonElasticMapReduceEditorsRole`.                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Feb 8, 2023                                                                                                                                |
| EMR Notebooks started tracking changes                                                                                                                                                                                                                                                | EMR Notebooks started tracking changes for its AWS managed policies.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Feb 8, 2023                                                                                                                                |
