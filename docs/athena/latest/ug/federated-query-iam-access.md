# Allow access to Athena Federated Query: Example policies

The permission policy examples in this topic demonstrate required allowed actions and the
resources for which they are allowed. Examine these policies carefully and modify them
according to your requirements before attaching them to IAM identities.

For information about attaching policies to IAM identities, see [Adding and removing
IAM identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md") in the [IAM User Guide](../../../IAM/latest/UserGuide.md "../../../IAM/latest/UserGuide.md").

- [Example policy to allow an IAM principal to run and return results using Athena Federated Query](#fed-using-iam "#fed-using-iam")
- [Example Policy to Allow an IAM Principal to Create a Data Source Connector](#fed-creating-iam "#fed-creating-iam")

###### Example – Allow an IAM principal to run and return results using Athena Federated Query

The following identity-based permissions policy allows actions that a user or other
IAM principal requires to use Athena Federated Query. Principals who are allowed to perform these
actions are able to run queries that specify Athena catalogs associated with a federated
data source.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Athena",
 "Effect": "Allow",
 "Action": [
 "athena:GetDataCatalog",
 "athena:GetQueryExecution",
 "athena:GetQueryResults",
 "athena:GetWorkGroup",
 "athena:StartQueryExecution",
 "athena:StopQueryExecution"
 ],
 "Resource": [
 "arn:aws:athena:*:`111122223333`:workgroup/`WorkgroupName`",
 "arn:aws:athena:`us-east-1`:`111122223333`:datacatalog/`DataCatalogName`"
 ]
 },
 {
 "Sid": "ListAthenaWorkGroups",
 "Effect": "Allow",
 "Action": "athena:ListWorkGroups",
 "Resource": "*"
 },
 {
 "Sid": "Lambda",
 "Effect": "Allow",
 "Action": "lambda:InvokeFunction",
 "Resource": [
 "arn:aws:lambda:*:`111122223333`:function:`OneAthenaLambdaFunction`",
 "arn:aws:lambda:*:`111122223333`:function:`AnotherAthenaLambdaFunction`"
 ]
 },
 {
 "Sid": "S3",
 "Effect": "Allow",
 "Action": [
 "s3:AbortMultipartUpload",
 "s3:GetBucketLocation",
 "s3:GetObject",
 "s3:ListBucket",
 "s3:ListMultipartUploadParts",
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::`MyLambdaSpillBucket`",
 "arn:aws:s3:::`MyLambdaSpillBucket`/*",
 "arn:aws:s3:::`MyQueryResultsBucket`",
 "arn:aws:s3:::`MyQueryResultsBucket`/*"
 ]
 }
 ]
}`

```

| Explanation of permissions                                                                                                                                                               | Allowed actions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Explanation |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| `<br>"athena:GetQueryExecution",<br>"athena:GetQueryResults",<br>"athena:GetWorkGroup",<br>"athena:StartQueryExecution",<br>"athena:StopQueryExecution"<br>`                             | Athena permissions that are required to run federated<br>queries.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `<br>"athena:GetDataCatalog",<br>"athena:GetQueryExecution,"<br>"athena:GetQueryResults",<br>"athena:GetWorkGroup",<br>"athena:StartQueryExecution",<br>"athena:StopQueryExecution"<br>` | Athena permissions that are required to run federated view queries.<br>The `GetDataCatalog` action is required for views.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `<br>"lambda:InvokeFunction"<br>`                                                                                                                                                        | Allows queries to invoke the AWS Lambda functions for the AWS Lambda<br>functions specified in the `Resource` block. For example,<br>`arn:aws:lambda:*:`MyAWSAcctId`:function:`MyAthenaLambdaFunction``,<br>where `MyAthenaLambdaFunction` specifies the<br>name of a Lambda function to be invoked. As shown in the example,<br>multiple functions can be specified.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `<br>"s3:AbortMultipartUpload",<br>"s3:GetBucketLocation",<br>"s3:GetObject",<br>"s3:ListBucket",<br>"s3:ListMultipartUploadParts",<br>"s3:PutObject"<br>`                               | The `s3:ListBucket` and<br>`s3:GetBucketLocation` permissions are required to<br>access the query output bucket for IAM principals that run<br>`StartQueryExecution`.<br>`s3:PutObject`,<br>`s3:ListMultipartUploadParts`, and<br>`s3:AbortMultipartUpload` allow writing query results<br>to all sub-folders of the query results bucket as specified by the<br>`arn:aws:s3:::`MyQueryResultsBucket`/*`<br>resource identifier, where<br>`MyQueryResultsBucket` is the Athena<br>query results bucket. For more information, see [Work with query results and recent queries](querying.md "querying.md").<br>`s3:GetObject` allows reading of query results and<br>query history for the resource specified as<br>`arn:aws:s3:::`MyQueryResultsBucket``,<br>where `MyQueryResultsBucket` is the Athena<br>query results bucket.<br>`s3:GetObject` also allows reading from the resource<br>specified as<br>`"arn:aws:s3:::`MyLambdaSpillBucket`/`MyLambdaSpillPrefix`\*"`,<br>where `MyLambdaSpillPrefix` is specified in<br>the configuration of the Lambda function or functions being<br>invoked. |

###### Example – Allow an IAM principal to create a data source connector

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "lambda:CreateFunction",
                "lambda:ListVersionsByFunction",
                "iam:CreateRole",
                "lambda:GetFunctionConfiguration",
                "iam:AttachRolePolicy",
                "iam:PutRolePolicy",
                "lambda:PutFunctionConcurrency",
                "iam:PassRole",
                "iam:DetachRolePolicy",
                "lambda:ListTags",
                "iam:ListAttachedRolePolicies",
                "iam:DeleteRolePolicy",
                "lambda:DeleteFunction",
                "lambda:GetAlias",
                "iam:ListRolePolicies",
                "iam:GetRole",
                "iam:GetPolicy",
                "lambda:InvokeFunction",
                "lambda:GetFunction",
                "lambda:ListAliases",
                "lambda:UpdateFunctionConfiguration",
                "iam:DeleteRole",
                "lambda:UpdateFunctionCode",
                "s3:GetObject",
                "lambda:AddPermission",
                "iam:UpdateRole",
                "lambda:DeleteFunctionConcurrency",
                "lambda:RemovePermission",
                "iam:GetRolePolicy",
                "lambda:GetPolicy"
            ],
            "Resource": [
                "arn:aws:lambda:*:`111122223333`:function:`MyAthenaLambdaFunctionsPrefix`*",
                "arn:aws:s3:::awsserverlessrepo-changesets-`1iiv3xa62ln3m`/*",
                "arn:aws:iam::*:role/`RoleName`",
                "arn:aws:iam::`111122223333`:policy/*"
            ]
        },
        {
            "Sid": "VisualEditor1",
            "Effect": "Allow",
            "Action": [
                "cloudformation:CreateUploadBucket",
                "cloudformation:DescribeStackDriftDetectionStatus",
                "cloudformation:ListExports",
                "cloudformation:ListStacks",
                "cloudformation:ListImports",
                "lambda:ListFunctions",
                "iam:ListRoles",
                "lambda:GetAccountSettings",
                "ec2:DescribeSecurityGroups",
                "cloudformation:EstimateTemplateCost",
                "ec2:DescribeVpcs",
                "lambda:ListEventSourceMappings",
                "cloudformation:DescribeAccountLimits",
                "ec2:DescribeSubnets",
                "cloudformation:CreateStackSet",
                "cloudformation:ValidateTemplate"
            ],
            "Resource": "*"
        },
        {
            "Sid": "VisualEditor2",
            "Effect": "Allow",
            "Action": "cloudformation:*",
            "Resource": [
                "arn:aws:cloudformation:*:`111122223333`:stack/aws-serverless-repository-`MyCFStackPrefix`*/*",
                "arn:aws:cloudformation:*:`111122223333`:stack/serverlessrepo-`MyCFStackPrefix`*/*",
                "arn:aws:cloudformation:*:*:transform/Serverless-*",
                "arn:aws:cloudformation:*:`111122223333`:stackset/aws-serverless-repository-`MyCFStackPrefix`*:*",
                "arn:aws:cloudformation:*:`111122223333`:stackset/serverlessrepo-`MyCFStackPrefix`*:*"
            ]
        },
        {
            "Sid": "VisualEditor3",
            "Effect": "Allow",
            "Action": "serverlessrepo:*",
            "Resource": "arn:aws:serverlessrepo:*:*:applications/*"
        },
        {
            "Sid": "ECR",
            "Effect": "Allow",
            "Action": [
                "ecr:BatchGetImage",
                "ecr:GetDownloadUrlForLayer"
            ],
            "Resource": "arn:aws:ecr:*:*:repository/*"
        }
    ]
}

```

| Explanation of permissions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Allowed actions                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Explanation |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| `<br>"lambda:CreateFunction",<br>"lambda:ListVersionsByFunction",<br>"lambda:GetFunctionConfiguration",<br>"lambda:PutFunctionConcurrency",<br>"lambda:ListTags",<br>"lambda:DeleteFunction",<br>"lambda:GetAlias",<br>"lambda:InvokeFunction",<br>"lambda:GetFunction",<br>"lambda:ListAliases",<br>"lambda:UpdateFunctionConfiguration",<br>"lambda:UpdateFunctionCode",<br>"lambda:AddPermission",<br>"lambda:DeleteFunctionConcurrency",<br>"lambda:RemovePermission",<br>"lambda:GetPolicy"<br>"lambda:GetAccountSettings",<br>"lambda:ListFunctions",<br>"lambda:ListEventSourceMappings",<br>` | Allow the creation and management of Lambda functions listed as<br>resources. In the example, a name prefix is used in the resource<br>identifier<br>`arn:aws:lambda:*:`MyAWSAcctId`:function:`MyAthenaLambdaFunctionsPrefix`*`,<br>where<br>`MyAthenaLambdaFunctionsPrefix`<br>is a shared prefix used in the name of a group of Lambda functions so<br>that they don't need to be specified individually as resources. You<br>can specify one or more Lambda function resources. |
| `<br>"s3:GetObject"<br>`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Allows reading of a bucket that AWS Serverless Application Repository requires as specified by the<br>resource identifier<br>`arn:aws:s3:::awsserverlessrepo-changesets-`1iiv3xa62ln3m`/*`.<br>This bucket may be specific to your account.                                                                                                                                                                                                                                        |
| `<br>"cloudformation:*"<br>`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Allows the creation and management of AWS CloudFormation stacks specified by<br>the resource<br>`MyCFStackPrefix`. These<br>stacks and stacksets are how AWS Serverless Application Repository deploys connectors and<br>UDFs.                                                                                                                                                                                                                                                     |
| `<br>"serverlessrepo:*"<br>`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Allows searching, viewing, publishing, and updating applications in<br>the AWS Serverless Application Repository, specified by the resource identifier<br>`arn:aws:serverlessrepo:*:*:applications/*`.                                                                                                                                                                                                                                                                             |
| `<br>"ecr:BatchGetImage",<br>"ecr:GetDownloadUrlForLayer"<br>`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Allows the created Lambda function to access the federation<br>connector ECR image.                                                                                                                                                                                                                                                                                                                                                                                                |
