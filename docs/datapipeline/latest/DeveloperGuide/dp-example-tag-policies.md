AWS Data Pipeline is no longer available to new customers. Existing customers of AWS Data Pipeline can continue to use the service as normal. [Learn more](https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/ "https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/")

# Example Policies for AWS Data Pipeline

The following examples demonstrate how to grant users full or restricted access to
pipelines.

###### Contents

- [Example 1: Grant users read-only access based on a tag](#ex1 "#ex1")
- [Example 2: Grant users full access based on a tag](#ex2 "#ex2")
- [Example 3: Grant the pipeline owner full access](#ex3 "#ex3")
- [Example 4: Grant users access to the AWS Data Pipeline console](#example4-grant-users-access-to-console "#example4-grant-users-access-to-console")

## Example 1: Grant users read-only access based on a tag

The following policy allows users to use the read-only AWS Data Pipeline API actions, but
only with pipelines that have the tag "environment=production".

The ListPipelines API action does not support tag-based authorization.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "datapipeline:Describe*",
 "datapipeline:GetPipelineDefinition",
 "datapipeline:ValidatePipelineDefinition",
 "datapipeline:QueryObjects"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringEquals": {
 "datapipeline:Tag/environment": "production"
 }
 }
 }
 ]
}`

```

## Example 2: Grant users full access based on a tag

The following policy allows users to use all AWS Data Pipeline API actions, with the exception of ListPipelines,
but only with pipelines that have the tag "environment=test".

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "datapipeline:*"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringEquals": {
 "datapipeline:Tag/environment": "test"
 }
 }
 }
 ]
}`

```

## Example 3: Grant the pipeline owner full access

The following policy allows users to use all the AWS Data Pipeline API actions,
but only with their own pipelines.

## Example 4: Grant users access to the AWS Data Pipeline console

The following policy allows users to create and manage a pipeline using the AWS Data Pipeline
console.

This policy includes the action for `PassRole` permissions for specific
resources tied to the `roleARN` that AWS Data Pipeline needs. For more information
about the identity-based (IAM) `PassRole` permission, see the blog post
[Granting Permission to Launch EC2 Instances with IAM Roles (PassRole
Permission)](https://aws.amazon.com/blogs/security/granting-permission-to-launch-ec2-instances-with-iam-roles-passrole-permission/ "https://aws.amazon.com/blogs/security/granting-permission-to-launch-ec2-instances-with-iam-roles-passrole-permission/").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Action": [
 "cloudwatch:*",
 "datapipeline:*",
 "dynamodb:DescribeTable",
 "elasticmapreduce:AddJobFlowSteps",
 "elasticmapreduce:ListInstance*",
 "iam:AddRoleToInstanceProfile",
 "iam:CreateInstanceProfile",
 "iam:GetInstanceProfile",
 "iam:GetRole",
 "iam:GetRolePolicy",
 "iam:ListInstanceProfiles",
 "iam:ListInstanceProfilesForRole",
 "iam:ListRoles",
 "rds:DescribeDBInstances",
 "rds:DescribeDBSecurityGroups",
 "redshift:DescribeClusters",
 "redshift:DescribeClusterSecurityGroups",
 "s3:List*",
 "sns:ListTopics"
 ],
 "Effect": "Allow",
 "Resource": [
 "*"
 ]
 },
 {
 "Action": "iam:PassRole",
 "Effect": "Allow",
 "Resource": [
 "arn:aws:iam::*:role/DataPipelineDefaultResourceRole",
 "arn:aws:iam::*:role/DataPipelineDefaultRole"
 ]
 }
 ]
}`

```
