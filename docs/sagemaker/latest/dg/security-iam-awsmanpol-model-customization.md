# AWS managed policies for Amazon SageMaker AI model customization

These AWS managed policies add permissions required to use Amazon SageMaker AI model
customization. The policies are available in your AWS account and are used by execution
roles created from the SageMaker AI console.

###### Topics

- [AWS managed policy: AmazonSageMakerModelCustomizationCoreAccess](#security-iam-awsmanpol-AmazonSageMakerModelCustomizationCoreAccess "#security-iam-awsmanpol-AmazonSageMakerModelCustomizationCoreAccess")
- [Amazon SageMaker AI updates to model customization managed policies](#security-iam-awsmanpol-model-customization-updates "#security-iam-awsmanpol-model-customization-updates")

## AWS managed policy: AmazonSageMakerModelCustomizationCoreAccess

This policy grants permissions required for model customization workflows in Amazon SageMaker AI,
including serverless training, custom reward function reinforcement learning, model
evaluation, and deployment to SageMaker or Bedrock endpoints.

**Permissions details**

This AWS managed policy includes the following permissions.

- `sagemaker` – Allows principals to manage SageMaker Hub
  content, create and manage training jobs, pipelines, endpoints with inference
  components, model packages, lineage tracking, MLflow experiment tracking, and
  perform search and tagging operations across model customization resources.
- `sagemaker-mlflow` – Allows principals to access the MLflow
  tracking UI, create experiments and runs, and log metrics, parameters, and
  models.
- `s3` – Allows principals to read objects from JumpStart
  buckets and read/write objects in S3 buckets with names containing "sagemaker"
  (case-insensitive), restricted to the principal's own account.
- `lambda` – Allows principals to list, create, delete,
  invoke, and get Lambda functions with names containing "SageMaker"
  (case-insensitive) for custom reward functions. Also allows read access to the
  AWS SDK Lambda layer.
- `bedrock` – Allows principals to create custom models and
  evaluation jobs, import models, invoke models (including streaming), and list
  foundation models and provisioned throughputs.
- `ecr` – Allows principals to pull container images and get
  authorization tokens for inference. Uses `Resource: *` to support
  cross-account pulls from AWS Deep Learning Container accounts.
- `application-autoscaling` – Allows principals to describe
  scalable targets for inference endpoint autoscaling.
- `logs` – Allows principals to read and write CloudWatch Logs
  for SageMaker log groups (`/aws/sagemaker/*`).
- `iam` – Allows principals to pass roles to SageMaker,
  Lambda, and Bedrock services. PassRole is scoped by role naming conventions
  (`*SageMaker*` for SageMaker, `SageMakerForLambda*` for
  Lambda, `SageMakerForBedrock*` for Bedrock) and
  `iam:PassedToService` conditions. Also allows
  `ListRoles` for UI dropdowns.
- `kms` – Allows principals to describe keys and list aliases
  for job configuration. Read-only.
- `ec2` – Allows principals to describe VPCs for job
  configuration. Read-only.
- `servicequotas` – Allows principals to list service quotas
  for Amazon SageMaker AI. This enables the Studio UI to look up instance-type-specific quota
  codes and provide direct links to the Service Quotas console when a quota limit
  is reached. Read-only.

###### Example Permissions policy

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "SageMakerPublicHubPermissions",
            "Effect": "Allow",
            "Action": [
                "sagemaker:ListHubContents"
            ],
            "Resource": [
                "arn:aws:sagemaker:*:aws:hub/SageMakerPublicHub"
            ]
        },
        {
            "Sid": "SageMakerHubPermissions",
            "Effect": "Allow",
            "Action": [
                "sagemaker:ImportHubContent",
                "sagemaker:ListHubs",
                "sagemaker:ListHubContents",
                "sagemaker:ListHubContentVersions",
                "sagemaker:DescribeHubContent",
                "sagemaker:DeleteHubContent"
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
            "Sid": "JumpStartS3Access",
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::jumpstart*"
            ]
        },
        {
            "Sid": "SageMakerTrainingJob",
            "Effect": "Allow",
            "Action": [
                "sagemaker:CreateTrainingJob",
                "sagemaker:DescribeTrainingJob",
                "sagemaker:ListTrainingJobs",
                "sagemaker:StopTrainingJob"
            ],
            "Resource": [
                "arn:aws:sagemaker:*:*:training-job/*"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
                }
            }
        },
        {
            "Sid": "SageMakerMLFlow",
            "Effect": "Allow",
            "Action": [
                "sagemaker:UpdateMlflowApp",
                "sagemaker:DescribeMlflowApp",
                "sagemaker:CreatePresignedMlflowAppUrl",
                "sagemaker:CallMlflowAppApi",
                "sagemaker-mlflow:AccessUI",
                "sagemaker-mlflow:GetExperiment",
                "sagemaker-mlflow:GetExperimentByName",
                "sagemaker-mlflow:GetRun",
                "sagemaker-mlflow:GetMetricHistory",
                "sagemaker-mlflow:GetLoggedModel",
                "sagemaker-mlflow:SearchExperiments",
                "sagemaker-mlflow:SearchRuns",
                "sagemaker-mlflow:ListArtifacts",
                "sagemaker-mlflow:CreateExperiment",
                "sagemaker-mlflow:CreateRun",
                "sagemaker-mlflow:LogBatch",
                "sagemaker-mlflow:LogMetric",
                "sagemaker-mlflow:LogParam",
                "sagemaker-mlflow:LogModel",
                "sagemaker-mlflow:LogInputs",
                "sagemaker-mlflow:SetTag",
                "sagemaker-mlflow:UpdateRun"
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
            "Sid": "BYODataSetS3Access",
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket",
                "s3:GetObject",
                "s3:PutObject"
            ],
            "Resource": [
                "arn:aws:s3:::*SageMaker*",
                "arn:aws:s3:::*Sagemaker*",
                "arn:aws:s3:::*sagemaker*"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
                }
            }
        },
        {
            "Sid": "SageMakerModelPackage",
            "Effect": "Allow",
            "Action": [
                "sagemaker:CreateModel",
                "sagemaker:CreateModelPackage",
                "sagemaker:CreateModelPackageGroup",
                "sagemaker:UpdateModelPackage",
                "sagemaker:DescribeModelPackage",
                "sagemaker:DescribeModelPackageGroup",
                "sagemaker:ListModelPackages",
                "sagemaker:ListModelPackageGroups",
                "sagemaker:DescribeModel",
                "sagemaker:DeleteModelPackage",
                "sagemaker:DeleteModelPackageGroup"
            ],
            "Resource": [
                "arn:aws:sagemaker:*:*:model-package-group/*",
                "arn:aws:sagemaker:*:*:model-package/*",
                "arn:aws:sagemaker:*:*:model/*"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
                }
            }
        },
        {
            "Sid": "SageMakerLineage",
            "Effect": "Allow",
            "Action": [
                "sagemaker:CreateAction",
                "sagemaker:CreateArtifact",
                "sagemaker:CreateContext",
                "sagemaker:DescribeAction",
                "sagemaker:DescribeArtifact",
                "sagemaker:DescribeTrialComponent",
                "sagemaker:QueryLineage",
                "sagemaker:AddAssociation",
                "sagemaker:UpdateArtifact"
            ],
            "Resource": [
                "arn:aws:sagemaker:*:*:action/*",
                "arn:aws:sagemaker:*:*:artifact/*",
                "arn:aws:sagemaker:*:*:context/*",
                "arn:aws:sagemaker:*:*:endpoint/*",
                "arn:aws:sagemaker:*:*:experiment-trial-component/*",
                "arn:aws:sagemaker:*:*:model-package/*",
                "arn:aws:sagemaker:*:*:pipeline/*"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
                }
            }
        },
        {
            "Sid": "SageMakerPipelines",
            "Effect": "Allow",
            "Action": [
                "sagemaker:CreatePipeline",
                "sagemaker:DescribePipeline",
                "sagemaker:DescribePipelineDefinitionForExecution",
                "sagemaker:DescribePipelineExecution",
                "sagemaker:UpdatePipeline",
                "sagemaker:StartPipelineExecution"
            ],
            "Resource": [
                "arn:aws:sagemaker:*:*:pipeline/*"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
                }
            }
        },
        {
            "Sid": "SageMakerInference",
            "Effect": "Allow",
            "Action": [
                "sagemaker:CreateEndpoint",
                "sagemaker:CreateEndpointConfig",
                "sagemaker:CreateInferenceComponent",
                "sagemaker:DescribeInferenceComponent",
                "sagemaker:DescribeEndpoint",
                "sagemaker:DescribeEndpointConfig",
                "sagemaker:DeleteInferenceComponent",
                "sagemaker:DeleteEndpoint",
                "sagemaker:InvokeEndpoint"
            ],
            "Resource": [
                "arn:aws:sagemaker:*:*:inference-component/*",
                "arn:aws:sagemaker:*:*:endpoint/*",
                "arn:aws:sagemaker:*:*:endpoint-config/*"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
                }
            }
        },
        {
            "Sid": "SageMakerInferenceAutoscaling",
            "Effect": "Allow",
            "Action": [
                "application-autoscaling:DescribeScalableTargets"
            ],
            "Resource": [
                "arn:aws:application-autoscaling:*:*:scalable-target/*"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
                }
            }
        },
        {
            "Sid": "SageMakerInferenceEcrReadAccess",
            "Effect": "Allow",
            "Action": [
                "ecr:BatchGetImage",
                "ecr:BatchCheckLayerAvailability",
                "ecr:GetDownloadUrlForLayer",
                "ecr:GetAuthorizationToken"
            ],
            "Resource": "*"
        },
        {
            "Sid": "SageMakerListPermissions",
            "Effect": "Allow",
            "Action": [
                "sagemaker:ListActions",
                "sagemaker:ListArtifacts",
                "sagemaker:ListAssociations",
                "sagemaker:ListEndpoints",
                "sagemaker:ListInferenceComponents",
                "sagemaker:ListMlflowApps",
                "sagemaker:ListMlflowTrackingServers",
                "sagemaker:ListPipelineExecutions",
                "sagemaker:ListPipelineExecutionSteps",
                "sagemaker:ListWorkforces",
                "sagemaker:Search"
            ],
            "Resource": [
                "*"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
                }
            }
        },
        {
            "Sid": "SageMakerTagsPermission",
            "Effect": "Allow",
            "Action": [
                "sagemaker:AddTags",
                "sagemaker:ListTags"
            ],
            "Resource": [
                "arn:aws:sagemaker:*:*:model-package-group/*",
                "arn:aws:sagemaker:*:*:model-package/*",
                "arn:aws:sagemaker:*:*:hub/*",
                "arn:aws:sagemaker:*:*:hub-content/*",
                "arn:aws:sagemaker:*:*:training-job/*",
                "arn:aws:sagemaker:*:*:model/*",
                "arn:aws:sagemaker:*:*:endpoint/*",
                "arn:aws:sagemaker:*:*:endpoint-config/*",
                "arn:aws:sagemaker:*:*:pipeline/*",
                "arn:aws:sagemaker:*:*:inference-component/*",
                "arn:aws:sagemaker:*:*:action/*"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
                }
            }
        },
        {
            "Sid": "SageMakerJobAdvancedSettings",
            "Effect": "Allow",
            "Action": [
                "kms:DescribeKey",
                "kms:ListAliases",
                "iam:ListRoles",
                "ec2:DescribeVpcs",
                "servicequotas:ListServiceQuotas"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
                }
            }
        },
        {
            "Sid": "CloudWatchLogReadAccess",
            "Effect": "Allow",
            "Action": [
                "logs:DescribeLogGroups",
                "logs:DescribeLogStreams",
                "logs:GetLogEvents"
            ],
            "Resource": [
                "arn:aws:logs:*:*:log-group:/aws/sagemaker/*",
                "arn:aws:logs:*:*:log-group::log-stream:"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
                }
            }
        },
        {
            "Sid": "CloudWatchLogWriteAccess",
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": [
                "arn:aws:logs:*:*:log-group:/aws/sagemaker/*"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
                }
            }
        },
        {
            "Sid": "LambdaListFunctions",
            "Effect": "Allow",
            "Action": [
                "lambda:ListFunctions"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
                }
            }
        },
        {
            "Sid": "LambdaPermissionsForRewardFunction",
            "Effect": "Allow",
            "Action": [
                "lambda:CreateFunction",
                "lambda:DeleteFunction",
                "lambda:InvokeFunction",
                "lambda:GetFunction"
            ],
            "Resource": [
                "arn:aws:lambda:*:*:function:*SageMaker*",
                "arn:aws:lambda:*:*:function:*sagemaker*",
                "arn:aws:lambda:*:*:function:*Sagemaker*"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
                }
            }
        },
        {
            "Sid": "LambdaLayerForAWSSDK",
            "Effect": "Allow",
            "Action": [
                "lambda:GetLayerVersion"
            ],
            "Resource": [
                "arn:aws:lambda:*:336392948345:layer:AWSSDK*"
            ]
        },
        {
            "Sid": "BedrockCustomModelAndEvaluation",
            "Effect": "Allow",
            "Action": [
                "bedrock:CreateCustomModel",
                "bedrock:CreateEvaluationJob",
                "bedrock:GetCustomModel",
                "bedrock:GetModelImportJob",
                "bedrock:GetImportedModel",
                "bedrock:GetEvaluationJob",
                "bedrock:InvokeModel",
                "bedrock:InvokeModelWithResponseStream"
            ],
            "Resource": [
                "arn:aws:bedrock:*:*:evaluation-job/*",
                "arn:aws:bedrock:*:*:imported-model/*",
                "arn:aws:bedrock:*:*:custom-model/*",
                "arn:aws:bedrock:*:*:model-import-job/*",
                "arn:aws:bedrock:*:*:foundation-model/*"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
                }
            }
        },
        {
            "Sid": "BedrockModelImportAndList",
            "Effect": "Allow",
            "Action": [
                "bedrock:CreateModelImportJob",
                "bedrock:ListProvisionedModelThroughputs",
                "bedrock:ListCustomModelDeployments",
                "bedrock:ListCustomModels",
                "bedrock:ListModelImportJobs"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
                }
            }
        },
        {
            "Sid": "BedrockFoundationModelOperations",
            "Effect": "Allow",
            "Action": [
                "bedrock:GetFoundationModelAvailability",
                "bedrock:ListFoundationModels"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Sid": "PassRoleForSageMaker",
            "Effect": "Allow",
            "Action": [
                "iam:PassRole"
            ],
            "Resource": [
                "arn:aws:iam::*:role/service-role/*SageMaker*",
                "arn:aws:iam::*:role/service-role/*Sagemaker*",
                "arn:aws:iam::*:role/service-role/*sagemaker*"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "${aws:PrincipalAccount}",
                    "iam:PassedToService": [
                        "sagemaker.amazonaws.com",
                        "job.sagemaker.amazonaws.com"
                    ]
                },
                "ArnLike": {
                    "iam:AssociatedResourceArn": "arn:aws:sagemaker:*:*:*"
                }
            }
        },
        {
            "Sid": "PassRoleForAWSLambda",
            "Effect": "Allow",
            "Action": [
                "iam:PassRole"
            ],
            "Resource": "arn:aws:iam::*:role/SageMakerForLambda*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "${aws:PrincipalAccount}",
                    "iam:PassedToService": "lambda.amazonaws.com"
                },
                "ArnLike": {
                    "iam:AssociatedResourceArn": "arn:aws:lambda:*:*:function:*"
                }
            }
        },
        {
            "Sid": "PassRoleForBedrock",
            "Effect": "Allow",
            "Action": [
                "iam:PassRole"
            ],
            "Resource": "arn:aws:iam::*:role/SageMakerForBedrock*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "${aws:PrincipalAccount}",
                    "iam:PassedToService": "bedrock.amazonaws.com"
                }
            }
        }
    ]
}
```

## Amazon SageMaker AI updates to model customization managed policies

View details about updates to AWS managed policies for Amazon SageMaker AI model customization
since this service began tracking these changes. For automatic alerts about changes to
this page, subscribe to the RSS feed on the SageMaker AI [Document
history page.](doc-history.md "doc-history.md")

| Policy                                                                                                                                                                                                                        | Version | Change                                                                                                                                                                                                                                                                                                                                 | Date          |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| [AWS managed policy: AmazonSageMakerModelCustomizationCoreAccess](#security-iam-awsmanpol-AmazonSageMakerModelCustomizationCoreAccess "#security-iam-awsmanpol-AmazonSageMakerModelCustomizationCoreAccess") – Updated policy | 2       | Added `servicequotas:ListServiceQuotas` to the<br>`SageMakerJobAdvancedSettings` statement. This allows<br>the Amazon SageMaker AI Studio UI to look up instance-type-specific service<br>quota codes and provide direct links to the Service Quotas console<br>when a quota limit is reached during model customization<br>workflows. | June 30, 2026 |
| AmazonSageMakerModelCustomizationCoreAccess<br>• New policy                                                                                                                                                                   | 1       | Initial policy                                                                                                                                                                                                                                                                                                                         | May 26, 2026  |
