

# AWS managed policies for SageMaker AI jobs
<a name="security-iam-awsmanpol-jobs"></a>

This AWS managed policy grants permissions needed for SageMaker AI job execution roles to access data in Amazon S3, invoke agents through Amazon API Gateway AgentCore, track experiments with MLflow, publish model packages, write logs to CloudWatch, invoke Lambda functions, and manage Amazon VPC network interfaces.

**Topics**
+ [AWS managed policy: AmazonSageMakerJobFullAccess](#security-iam-awsmanpol-AmazonSageMakerJobFullAccess)
+ [Amazon SageMaker AI updates to SageMaker AI jobs managed policies](#security-iam-awsmanpol-jobs-updates)

## AWS managed policy: AmazonSageMakerJobFullAccess
<a name="security-iam-awsmanpol-AmazonSageMakerJobFullAccess"></a>

This policy provides permissions for SageMaker AI job execution roles to access the resources needed to run training, processing, and transform jobs. You can attach this policy to IAM roles that you use as SageMaker AI job execution roles.

**Permissions details**

This policy includes the following permissions.
+ `s3` – Allows SageMaker AI jobs to read input data from, write output data to, and list the contents of Amazon S3 buckets. Restricted to resources in the same account.
+ `kms` – Allows SageMaker AI jobs to decrypt and generate data keys for server-side encryption of Amazon S3 objects using customer-managed AWS KMS keys. The `Decrypt` and `GenerateDataKey` actions are restricted through `kms:ViaService` to Amazon S3 only. `DescribeKey` is allowed without the `kms:ViaService` restriction. Restricted to resources in the same account.
+ `sagemaker` (Hub) – Allows describing hub content such as pre-built models and algorithms. Restricted to resources in the same account.
+ `sagemaker` (Model Packages) – Allows creating, accessing, and describing model packages and model package groups for model registry workflows. Restricted to resources in the same account.
+ `sagemaker` and `sagemaker-mlflow` – Allows jobs to use MLflow for experiment tracking, including creating experiments and runs, logging metrics, retrieving results, and managing traces. Restricted to resources in the same account.
+ `bedrock-agentcore` – Allows jobs to invoke AI agents through Amazon API Gateway AgentCore runtimes, stop runtime sessions, and get runtime details. Restricted to resources in the same account.
+ `ec2` – Allows managing Amazon VPC network interfaces for jobs running in Amazon VPC mode, including creating, deleting, and describing network interfaces and related Amazon VPC resources. The `ec2:CreateTags` action is restricted to the `CreateNetworkInterface` action. Restricted to resources in the same account.
+ `logs` – Allows creating log groups, log streams, and writing log events to Amazon CloudWatch Logs. Restricted to log groups with the `/aws/sagemaker/*` prefix. Restricted to resources in the same account.
+ `lambda` – Allows invoking Lambda functions in the same account.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "S3Permissions",
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:PutObject",
                "s3:ListBucket"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "s3:ResourceAccount": "${aws:PrincipalAccount}"
                }
            }
        },
        {
            "Sid": "KMSPermissions",
            "Effect": "Allow",
            "Action": [
                "kms:Decrypt",
                "kms:GenerateDataKey"
            ],
            "Resource": "arn:aws:kms:*:*:key/*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
                },
                "StringLike": {
                    "kms:ViaService": "s3.*.amazonaws.com"
                }
            }
        },
        {
            "Sid": "KMSDescribeKey",
            "Effect": "Allow",
            "Action": "kms:DescribeKey",
            "Resource": "arn:aws:kms:*:*:key/*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
                }
            }
        },
        {
            "Sid": "SageMakerHubPermissions",
            "Effect": "Allow",
            "Action": [
                "sagemaker:DescribeHubContent"
            ],
            "Resource": [
                "arn:aws:sagemaker:*:*:hub/*",
                "arn:aws:sagemaker:*:*:hub-content/*"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
                }
            }
        },
        {
            "Sid": "SageMakerModelPackagePermissions",
            "Effect": "Allow",
            "Action": [
                "sagemaker:AccessModelPackage",
                "sagemaker:CreateModelPackage",
                "sagemaker:DescribeModelPackage",
                "sagemaker:DescribeModelPackageGroup"
            ],
            "Resource": [
                "arn:aws:sagemaker:*:*:model-package/*",
                "arn:aws:sagemaker:*:*:model-package-group/*"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
                }
            }
        },
        {
            "Sid": "MLflowPermissions",
            "Effect": "Allow",
            "Action": [
                "sagemaker:DescribeMlflowApp",
                "sagemaker:CallMlflowAppApi",
                "sagemaker-mlflow:CreateExperiment",
                "sagemaker-mlflow:CreateRun",
                "sagemaker-mlflow:UpdateRun",
                "sagemaker-mlflow:LogBatch",
                "sagemaker-mlflow:GetExperimentByName",
                "sagemaker-mlflow:GetMetricHistory",
                "sagemaker-mlflow:GetRun",
                "sagemaker-mlflow:StartTrace",
                "sagemaker-mlflow:EndTrace",
                "sagemaker-mlflow:SearchTraces",
                "sagemaker-mlflow:ListArtifacts"
            ],
            "Resource": [
                "arn:aws:sagemaker:*:*:mlflow-app/*"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
                }
            }
        },
        {
            "Sid": "BedrockAgentCorePermissions",
            "Effect": "Allow",
            "Action": [
                "bedrock-agentcore:InvokeAgentRuntime",
                "bedrock-agentcore:StopRuntimeSession",
                "bedrock-agentcore:GetAgentRuntime"
            ],
            "Resource": "arn:aws:bedrock-agentcore:*:*:runtime/*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
                }
            }
        },
        {
            "Sid": "EC2NetworkPermissions",
            "Effect": "Allow",
            "Action": [
                "ec2:CreateNetworkInterface",
                "ec2:CreateNetworkInterfacePermission",
                "ec2:DescribeNetworkInterfaces",
                "ec2:DescribeVpcs",
                "ec2:DescribeSubnets",
                "ec2:DescribeSecurityGroups",
                "ec2:DescribeDhcpOptions"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
                }
            }
        },
        {
            "Sid": "EC2NetworkInterfaceTagPermissions",
            "Effect": "Allow",
            "Action": [
                "ec2:CreateTags"
            ],
            "Resource": "arn:aws:ec2:*:*:network-interface/*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "${aws:PrincipalAccount}",
                    "ec2:CreateAction": "CreateNetworkInterface"
                }
            }
        },
        {
            "Sid": "EC2NetworkInterfaceDeletePermissions",
            "Effect": "Allow",
            "Action": [
                "ec2:DeleteNetworkInterface",
                "ec2:DeleteNetworkInterfacePermission"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
                }
            }
        },
        {
            "Sid": "CloudWatchLogsPermissions",
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents",
                "logs:DescribeLogStreams"
            ],
            "Resource": "arn:aws:logs:*:*:log-group:/aws/sagemaker/*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
                }
            }
        },
        {
            "Sid": "LambdaPermissions",
            "Effect": "Allow",
            "Action": [
                "lambda:InvokeFunction"
            ],
            "Resource": "arn:aws:lambda:*:*:function:*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
                }
            }
        }
    ]
}
```

For more information, see [AmazonSageMakerJobFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonSageMakerJobFullAccess.html) in the AWS Managed Policy Reference Guide.

## Amazon SageMaker AI updates to SageMaker AI jobs managed policies
<a name="security-iam-awsmanpol-jobs-updates"></a>

View details about updates to AWS managed policies for SageMaker AI jobs since this service began tracking these changes.


| Policy | Version | Change | Date | 
| --- | --- | --- | --- | 
| [AmazonSageMakerJobFullAccess](#security-iam-awsmanpol-AmazonSageMakerJobFullAccess) – New policy | 1 | Initial policy | June 4, 2026 | 