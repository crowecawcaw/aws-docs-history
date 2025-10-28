# Permissions required to create connector and Athena catalog

To invoke Athena `CreateDataCatalog` you must create a role that has the
following permissions:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ECR",
 "Effect": "Allow",
 "Action": [
 "ecr:BatchGetImage",
 "ecr:GetDownloadUrlForLayer"
 ],
 "Resource": "arn:aws:ecr:*:*:repository/*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "glue:TagResource",
 "glue:GetConnection",
 "glue:CreateConnection",
 "glue:DeleteConnection",
 "glue:UpdateConnection",
 "serverlessrepo:CreateCloudFormationTemplate",
 "serverlessrepo:GetCloudFormationTemplate",
 "cloudformation:CreateStack",
 "cloudformation:DeleteStack",
 "cloudformation:DescribeStacks",
 "cloudformation:CreateChangeSet",
 "cloudformation:DescribeAccountLimits",
 "cloudformation:CreateStackSet",
 "cloudformation:ValidateTemplate",
 "cloudformation:CreateUploadBucket",
 "cloudformation:DescribeStackDriftDetectionStatus",
 "cloudformation:ListExports",
 "cloudformation:ListStacks",
 "cloudformation:EstimateTemplateCost",
 "cloudformation:ListImports",
 "lambda:InvokeFunction",
 "lambda:GetFunction",
 "lambda:DeleteFunction",
 "lambda:CreateFunction",
 "lambda:TagResource",
 "lambda:ListFunctions",
 "lambda:GetAccountSettings",
 "lambda:ListEventSourceMappings",
 "lambda:ListVersionsByFunction",
 "lambda:GetFunctionConfiguration",
 "lambda:PutFunctionConcurrency",
 "lambda:UpdateFunctionConfiguration",
 "lambda:UpdateFunctionCode",
 "lambda:DeleteFunctionConcurrency",
 "lambda:RemovePermission",
 "lambda:AddPermission",
 "lambda:ListTags",
 "lambda:GetAlias",
 "lambda:GetPolicy",
 "lambda:ListAliases",
 "ec2:DescribeSecurityGroups",
 "ec2:DescribeSubnets",
 "ec2:DescribeVpcs",
 "secretsmanager:ListSecrets",
 "glue:GetCatalogs"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:AttachRolePolicy",
 "iam:DetachRolePolicy",
 "iam:DeleteRolePolicy",
 "iam:PutRolePolicy",
 "iam:GetRolePolicy",
 "iam:CreateRole",
 "iam:TagRole",
 "iam:DeleteRole",
 "iam:GetRole",
 "iam:PassRole",
 "iam:ListRoles",
 "iam:ListAttachedRolePolicies",
 "iam:ListRolePolicies",
 "iam:GetPolicy",
 "iam:UpdateRole"
 ],
 "Resource": [
 "arn:aws:iam::*:role/`RoleName`",
 "arn:aws:iam::`111122223333`:policy/*"
 ]
 }
 ]
 }`

```
