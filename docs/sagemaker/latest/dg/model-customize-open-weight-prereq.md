# Prerequisites

Before you begin, complete the following prerequisites:

- Onboard to a SageMaker AI domain with Studio access. If you don't have permissions to set Studio as the default experience for your domain, contact your administrator. For more information, see [Amazon SageMaker AI domain overview](gs-studio-onboard.md "gs-studio-onboard.md").
- Update the AWS CLI by following the steps in [Installing the current AWS CLI Version](../../../cli/latest/userguide/install-cliv1.md#install-tool-bundled "../../../cli/latest/userguide/install-cliv1.md#install-tool-bundled").
- From your local machine, run `aws configure` and provide your AWS credentials. For information about AWS credentials, see [Understanding and getting your AWS credentials](../../../IAM/latest/UserGuide/security-creds.md "../../../IAM/latest/UserGuide/security-creds.md").

## Required IAM permissions

SageMaker AI model customization requires adding appropriate permissions to your SageMaker AI execution role.

### Setting up permissions through the console

If you create your SageMaker AI domain through the console, permissions for model customization are handled automatically depending on your setup method:

- **Quick setup** — Model customization permissions are included by default. No additional configuration is needed.
- **Custom setup** — Select the **Model customization** ML activity when configuring your execution role. For more information about ML activities and the permissions they grant, see [Configure ML activities for IAM roles](role-manager-ml-activities.md "role-manager-ml-activities.md").

### Setting up permissions manually

If you set up your domain through the AWS CLI, SDK, or CloudFormation, or if you need to add model customization permissions to an existing execution role, use one of the following options.

**Option 1 (Recommended): Attach the AWS managed policy**

Attach the `AmazonSageMakerModelCustomizationCoreAccess` managed policy to your SageMaker AI execution role. This policy covers all permissions needed for basic model customization, including serverless training, custom reward function RL, model evaluation, and deployment to SageMaker AI or Bedrock endpoints. For information about attaching policies, see [Adding and removing IAM identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md") in the _AWS Identity and Access Management User Guide_.

**Option 2: Create an inline policy**

If you prefer to manage permissions manually, create an inline policy with the following JSON and attach it to your execution role:

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
            "Resource": "*",
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
            "Resource": "*"
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
            "Resource": [
                "arn:aws:iam::*:role/SageMakerForLambda*",
                "arn:aws:iam::*:role/service-role/SageMakerForLambda*"
            ],
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
            "Resource": [
                "arn:aws:iam::*:role/SageMakerForBedrock*",
                "arn:aws:iam::*:role/service-role/SageMakerForBedrock*"
            ],
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

## Roles for Lambda and Bedrock

In addition to the permissions on your SageMaker AI execution role, model customization requires roles for two other services:

- **Lambda** — executes custom reward functions during RL-based training
- **Bedrock** — reads model artifacts from S3 when importing a custom model for deployment

### If you previously configured your execution role (legacy approach)

If you previously followed this documentation and updated your SageMaker AI execution role's trust policy to include `lambda.amazonaws.com` and `bedrock.amazonaws.com` as trusted service principals, your existing configuration continues to work. No changes are required.

To use this approach, your execution role's trust policy must include the following service principals:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "sagemaker.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        },
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "lambda.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        },
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "bedrock.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

###### Note

This approach is less secure because Lambda and Bedrock can assume your execution role and inherit all of its permissions — not just the ones each service needs.

### Create separate roles (recommended)

For improved security, create two separate scoped-down IAM roles — one for Lambda and one for Bedrock — rather than adding these service principals to your SageMaker AI execution role. Each role trusts only its respective service and contains only the minimum permissions that service requires.

If you set up your domain through the SageMaker AI console quick setup, these roles are created automatically. If you set up your domain through another method, create them manually using the following steps.

### Lambda role

This role allows Lambda to execute custom reward functions during RL-based model customization.

**Naming convention**: `SageMakerForLambda-{domain-id}`

1. Create an IAM role with the following trust policy. Replace `<ACCOUNT_ID>` with your 12-digit AWS account ID.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "<ACCOUNT_ID>"
        },
        "ArnLike": {
          "aws:SourceArn": "arn:aws:lambda:*:<ACCOUNT_ID>:function:*"
        }
      }
    }
  ]
}
```

2. Attach the `AWSLambdaBasicExecutionRole` AWS managed policy to the role. This grants the permissions needed to write logs to CloudWatch.

###### Note

This role does not require SageMaker AI or Bedrock permissions. The `aws:SourceAccount` and `aws:SourceArn` conditions restrict role assumption to Lambda functions in your account only, protecting against confused deputy attacks.

### Bedrock role

This role allows Bedrock to read model artifacts from your SageMaker AI-managed S3 bucket when importing a custom model.

**Naming convention**: `SageMakerForBedrock-{domain-id}`

1. Create an IAM role with the following trust policy. Replace `<ACCOUNT_ID>` with your 12-digit AWS account ID.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "bedrock.amazonaws.com"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "<ACCOUNT_ID>"
        },
        "ArnLike": {
          "aws:SourceArn": "arn:aws:bedrock:*:<ACCOUNT_ID>:*"
        }
      }
    }
  ]
}
```

2. Attach the following inline policy to the role:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "SageMakerBucketReadAccess",
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::sagemaker-*-${aws:PrincipalAccount}",
                "arn:aws:s3:::sagemaker-*-${aws:PrincipalAccount}/*"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
                }
            }
        },
        {
            "Sid": "AllowSSLRequestsOnly",
            "Action": "s3:*",
            "Effect": "Deny",
            "Resource": [
                "arn:aws:s3:::sagemaker-*-${aws:PrincipalAccount}",
                "arn:aws:s3:::sagemaker-*-${aws:PrincipalAccount}/*"
            ],
            "Condition": {
                "Bool": {
                    "aws:SecureTransport": "false"
                }
            }
        }
    ]
}
```

###### Note

This role does not require SageMaker AI, Lambda, or Bedrock API permissions. It only provides Bedrock with read access to model artifacts in your SageMaker AI-managed S3 bucket.
