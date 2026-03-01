# Allow access to Athena UDFs: Example policies

The permission policy examples in this topic demonstrate required allowed actions and the
resources for which they are allowed. Examine these policies carefully and modify them
according to your requirements before you attach similar permissions policies to IAM
identities.

- [Example Policy to Allow an IAM Principal to Run and Return Queries that Contain an Athena UDF Statement](#udf-using-iam "#udf-using-iam")
- [Example Policy to Allow an IAM Principal to Create an Athena UDF](#udf-creating-iam "#udf-creating-iam")

###### Example – Allow an IAM principal to run and return queries that contain an Athena UDF statement

The following identity-based permissions policy allows actions that a user or other
IAM principal requires to run queries that use Athena UDF statements.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "athena:StartQueryExecution",
                "lambda:InvokeFunction",
                "athena:GetQueryResults",
                "s3:ListMultipartUploadParts",
                "athena:GetWorkGroup",
                "s3:PutObject",
                "s3:GetObject",
                "s3:AbortMultipartUpload",
                "athena:StopQueryExecution",
                "athena:GetQueryExecution",
                "s3:GetBucketLocation"
            ],
            "Resource": [
                "arn:aws:athena:*:`MyAWSAcctId`:workgroup/`MyAthenaWorkGroup`",
                "arn:aws:s3:::`MyQueryResultsBucket`/*",
                "arn:aws:lambda:*:`MyAWSAcctId`:function:`OneAthenaLambdaFunction`",
                "arn:aws:lambda:*:`MyAWSAcctId`:function:`AnotherAthenaLambdaFunction`"
            ]
        },
        {
            "Sid": "VisualEditor1",
            "Effect": "Allow",
            "Action": "athena:ListWorkGroups",
            "Resource": "*"
        }
    ]
}
```

| Explanation of permissions                                                                                                                                    | Allowed actions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Explanation |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| `<br>"athena:StartQueryExecution",<br>"athena:GetQueryResults",<br>"athena:GetWorkGroup",<br>"athena:StopQueryExecution",<br>"athena:GetQueryExecution",<br>` | Athena permissions that are required to run queries in the<br>`MyAthenaWorkGroup` work group.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `<br>"s3:PutObject",<br>"s3:GetObject",<br>"s3:AbortMultipartUpload"<br>`                                                                                     | `s3:PutObject` and `s3:AbortMultipartUpload`<br>allow writing query results to all sub-folders of the query results<br>bucket as specified by the<br>`arn:aws:s3:::`MyQueryResultsBucket`/*`<br>resource identifier, where<br>`MyQueryResultsBucket` is the Athena<br>query results bucket. For more information, see [Work with query results and recent queries](querying.md "querying.md").<br>`s3:GetObject` allows reading of query results and<br>query history for the resource specified as<br>`arn:aws:s3:::`MyQueryResultsBucket``,<br>where `MyQueryResultsBucket` is the Athena<br>query results bucket. For more information, see [Work with query results and recent queries](querying.md "querying.md").<br>`s3:GetObject` also allows reading from the resource<br>specified as<br>`"arn:aws:s3:::`MyLambdaSpillBucket`/`MyLambdaSpillPrefix`\*"`,<br>where `MyLambdaSpillPrefix` is specified in<br>the configuration of the Lambda function or functions being<br>invoked. |
| `<br>"lambda:InvokeFunction"<br>`                                                                                                                             | Allows queries to invoke the AWS Lambda functions specified in the<br>`Resource` block. For example,<br>`arn:aws:lambda:*:`MyAWSAcctId`:function:`MyAthenaLambdaFunction``,<br>where `MyAthenaLambdaFunction` specifies the<br>name of a Lambda function to be invoked. Multiple functions can be<br>specified as shown in the example.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

###### Example – Allow an IAM principal to create an Athena UDF

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

| Explanation of permissions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Allowed actions                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Explanation |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| `<br>"lambda:CreateFunction",<br>"lambda:ListVersionsByFunction",<br>"lambda:GetFunctionConfiguration",<br>"lambda:PutFunctionConcurrency",<br>"lambda:ListTags",<br>"lambda:DeleteFunction",<br>"lambda:GetAlias",<br>"lambda:InvokeFunction",<br>"lambda:GetFunction",<br>"lambda:ListAliases",<br>"lambda:UpdateFunctionConfiguration",<br>"lambda:UpdateFunctionCode",<br>"lambda:AddPermission",<br>"lambda:DeleteFunctionConcurrency",<br>"lambda:RemovePermission",<br>"lambda:GetPolicy"<br>"lambda:GetAccountSettings",<br>"lambda:ListFunctions",<br>"lambda:ListEventSourceMappings",<br>` | Allow the creation and management of Lambda functions listed as<br>resources. In the example, a name prefix is used in the resource<br>identifier<br>`arn:aws:lambda:*:`MyAWSAcctId`:function:`MyAthenaLambdaFunctionsPrefix`*`,<br>where `MyAthenaLambdaFunctionsPrefix` is a<br>shared prefix used in the name of a group of Lambda functions so that<br>they don't need to be specified individually as resources. You can<br>specify one or more Lambda function resources. |
| `<br>"s3:GetObject"<br>`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Allows reading of a bucket that AWS Serverless Application Repository requires as specified by the<br>resource identifier<br>`arn:aws:s3:::awsserverlessrepo-changesets-`1iiv3xa62ln3m`/*`.                                                                                                                                                                                                                                                                                     |
| `<br>"cloudformation:*"<br>`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Allows the creation and management of CloudFormation stacks specified by<br>the resource `MyCFStackPrefix`. These<br>stacks and stacksets are how AWS Serverless Application Repository deploys connectors and<br>UDFs.                                                                                                                                                                                                                                                         |
| `<br>"serverlessrepo:*"<br>`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Allows searching, viewing, publishing, and updating applications in<br>the AWS Serverless Application Repository, specified by the resource identifier<br>`arn:aws:serverlessrepo:*:*:applications/*`.                                                                                                                                                                                                                                                                          |
