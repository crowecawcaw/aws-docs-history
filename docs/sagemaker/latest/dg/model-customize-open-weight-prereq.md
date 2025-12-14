# Prerequisites

Before you begin, complete the following prerequisites:

- Onboard to a SageMaker AI domain with Studio access. If you don't have
  permissions to set Studio as the default experience for your domain, contact
  your administrator. For more information, see [Amazon SageMaker AI domain overview](gs-studio-onboard.md "gs-studio-onboard.md").
- Update the AWS CLI by following the steps in [Installing the current AWS CLI Version](../../../cli/latest/userguide/install-cliv1.md#install-tool-bundled "../../../cli/latest/userguide/install-cliv1.md#install-tool-bundled").
- From your local machine, run `aws configure` and provide your
  AWS credentials. For information about AWS credentials, see [Understanding and getting your AWS credentials](../../../IAM/latest/UserGuide/security-creds.md "../../../IAM/latest/UserGuide/security-creds.md").

## Required IAM permissions

SageMaker AI model customization requires adding appropriate permissions to your
SageMaker AI domain execution. To do this, you can create an inline IAM
permissions policy and attach it to the IAM role. For information about adding
policies, see [Adding and removing IAM identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md") in the _AWS Identity and Access Management User Guide_.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowNonAdminStudioActions",
            "Effect": "Allow",
            "Action": [
                "sagemaker:CreatePresignedDomainUrl",
                "sagemaker:DescribeDomain",
                "sagemaker:DescribeUserProfile",
                "sagemaker:DescribeSpace",
                "sagemaker:ListSpaces",
                "sagemaker:DescribeApp",
                "sagemaker:ListApps"
            ],
            "Resource": [
                "arn:aws:sagemaker:*:*:domain/*",
                "arn:aws:sagemaker:*:*:user-profile/*",
                "arn:aws:sagemaker:*:*:app/*",
                "arn:aws:sagemaker:*:*:space/*"
             ]
        },
        {
            "Sid": "LambdaListPermissions",
            "Effect": "Allow",
            "Action": [
                "lambda:ListFunctions"
            ],
            "Resource": [
                "*"
            ]
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
                "sagemaker:ListHubs",
                "sagemaker:ListHubContents",
                "sagemaker:DescribeHubContent",
                "sagemaker:DeleteHubContent",
                "sagemaker:ListHubContentVersions",
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
            "Sid": "JumpStartAccess",
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
            "Sid": "ListMLFlowOperations",
            "Effect": "Allow",
            "Action": [
                "sagemaker:ListMlflowApps",
                "sagemaker:ListMlflowTrackingServers"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Sid": "MLFlowAccess",
            "Effect": "Allow",
            "Action": [
                "sagemaker:UpdateMlflowApp",
                "sagemaker:DescribeMlflowApp",
                "sagemaker:CreatePresignedMlflowAppUrl",
                "sagemaker:CallMlflowAppApi",
                "sagemaker-mlflow:*"
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
            ]
        },
        {
            "Sid": "AllowHubPermissions",
            "Effect": "Allow",
            "Action": [
                "sagemaker:ImportHubContent"
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
            "Sid": "PassRoleForSageMaker",
            "Effect": "Allow",
            "Action": [
                "iam:PassRole"
            ],
            "Resource": [
                "arn:aws:iam::*:role/service-role/AmazonSageMaker-ExecutionRole-*"
            ],
            "Condition": {
                "StringEquals": {
                    "iam:PassedToService": "sagemaker.amazonaws.com",
                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
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
                "arn:aws:iam::*:role/service-role/AmazonSageMaker-ExecutionRole-*"
            ],
            "Condition": {
                "StringEquals": {
                    "iam:PassedToService": "lambda.amazonaws.com",
                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
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
                "arn:aws:iam::*:role/service-role/AmazonSageMaker-ExecutionRole-*"
            ],
            "Condition": {
                "StringEquals": {
                    "iam:PassedToService": "bedrock.amazonaws.com",
                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
                }
            }
        },
        {
            "Sid": "TrainingJobRun",
            "Effect": "Allow",
            "Action": [
                "sagemaker:CreateTrainingJob",
                "sagemaker:DescribeTrainingJob",
                "sagemaker:ListTrainingJobs"
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
            "Sid": "ModelPackageAccess",
            "Effect": "Allow",
            "Action": [
                "sagemaker:CreateModelPackage",
                "sagemaker:DescribeModelPackage",
                "sagemaker:ListModelPackages",
                "sagemaker:CreateModelPackageGroup",
                "sagemaker:DescribeModelPackageGroup",
                "sagemaker:ListModelPackageGroups",
                "sagemaker:CreateModel"
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
            "Sid": "TagsPermission",
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
            "Sid": "LogAccess",
            "Effect": "Allow",
            "Action": [
                "logs:DescribeLogGroups",
                "logs:DescribeLogStreams",
                "logs:GetLogEvents"
            ],
            "Resource": [
                "arn:aws:logs:*:*:log-group*",
                "arn:aws:logs:*:*:log-group:/aws/sagemaker/TrainingJobs:log-stream:*"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
                }
            }
        },
        {
            "Sid": "BedrockDeploy",
            "Effect": "Allow",
            "Action": [
                "bedrock:CreateModelImportJob"
            ],
            "Resource": [
                "arn:aws:bedrock:*:*:*"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
                }
            }
        },
        {
            "Sid": "BedrockOperations",
            "Effect": "Allow",
            "Action": [
                "bedrock:GetModelImportJob",
                "bedrock:GetImportedModel",
                "bedrock:ListProvisionedModelThroughputs",
                "bedrock:ListCustomModelDeployments",
                "bedrock:ListCustomModels",
                "bedrock:ListModelImportJobs",
                "bedrock:GetEvaluationJob",
                "bedrock:CreateEvaluationJob",
                "bedrock:InvokeModel"
            ],
            "Resource": [
                "arn:aws:bedrock:*:*:evaluation-job/*",
                "arn:aws:bedrock:*:*:imported-model/*",
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
            "Sid": "SageMakerPipelinesAndLineage",
            "Effect": "Allow",
            "Action": [
                "sagemaker:ListActions",
                "sagemaker:ListArtifacts",
                "sagemaker:QueryLineage",
                "sagemaker:ListAssociations",
                "sagemaker:AddAssociation",
                "sagemaker:DescribeAction",
                "sagemaker:AddAssociation",
                "sagemaker:CreateAction",
                "sagemaker:CreateContext",
                "sagemaker:DescribeTrialComponent"
            ],
            "Resource": [
                "arn:aws:sagemaker:*:*:artifact/*",
                "arn:aws:sagemaker:*:*:action/*",
                "arn:aws:sagemaker:*:*:context/*",
                "arn:aws:sagemaker:*:*:action/*",
                "arn:aws:sagemaker:*:*:model-package/*",
                "arn:aws:sagemaker:*:*:context/*",
                "arn:aws:sagemaker:*:*:pipeline/*",
                "arn:aws:sagemaker:*:*:experiment-trial-component/*"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
                }
            }
        },
        {
            "Sid": "ListOperations",
            "Effect": "Allow",
            "Action": [
                "sagemaker:ListInferenceComponents",
                "sagemaker:ListWorkforces"
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
            "Sid": "SageMakerInference",
            "Effect": "Allow",
            "Action": [
                "sagemaker:DescribeInferenceComponent",
                "sagemaker:CreateEndpoint",
                "sagemaker:CreateEndpointConfig",
                "sagemaker:DescribeEndpoint",
                "sagemaker:DescribeEndpointConfig",
                "sagemaker:ListEndpoints"
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
            "Sid": "SageMakerPipelines",
            "Effect": "Allow",
            "Action": [
                "sagemaker:DescribePipelineExecution",
                "sagemaker:ListPipelineExecutions",
                "sagemaker:ListPipelineExecutionSteps",
                "sagemaker:CreatePipeline",
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
        }
    ]
}
```

If you've attached the [AmazonSageMakerFullAccessPolicy](../../../aws-managed-policy/latest/reference/AmazonSageMakerFullAccess.md "../../../aws-managed-policy/latest/reference/AmazonSageMakerFullAccess.md") to your execution role then you can add
this reduced policy:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "LambdaListPermissions",
            "Effect": "Allow",
            "Action": [
                "lambda:ListFunctions"
            ],
            "Resource": [
                "*"
            ]
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
            "Sid": "S3Access",
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:PutObject"
            ],
            "Resource": [
                "arn:aws:s3:::*SageMaker*",
                "arn:aws:s3:::*Sagemaker*",
                "arn:aws:s3:::*sagemaker*",
                "arn:aws:s3:::jumpstart*"
            ]
        },
        {
            "Sid": "PassRoleForSageMakerAndLambdaAndBedrock",
            "Effect": "Allow",
            "Action": [
                "iam:PassRole"
            ],
            "Resource": [
                "arn:aws:iam::*:role/service-role/AmazonSageMaker-ExecutionRole-*"
            ],
            "Condition": {
                "StringEquals": {
                    "iam:PassedToService": [
                        "lambda.amazonaws.com",
                        "bedrock.amazonaws.com"
                     ],
                     "aws:ResourceAccount": "${aws:PrincipalAccount}"
                 }
            }
        },
        {
            "Sid": "BedrockDeploy",
            "Effect": "Allow",
            "Action": [
                "bedrock:CreateModelImportJob"
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
            "Sid": "BedrockOperations",
            "Effect": "Allow",
            "Action": [
                "bedrock:GetModelImportJob",
                "bedrock:GetImportedModel",
                "bedrock:ListProvisionedModelThroughputs",
                "bedrock:ListCustomModelDeployments",
                "bedrock:ListCustomModels",
                "bedrock:ListModelImportJobs",
                "bedrock:GetEvaluationJob",
                "bedrock:CreateEvaluationJob",
                "bedrock:InvokeModel"
            ],
            "Resource": [
                "arn:aws:bedrock:*:*:evaluation-job/*",
                "arn:aws:bedrock:*:*:imported-model/*",
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
            "Sid": "BedrockFoundationModelOperations",
            "Effect": "Allow",
            "Action": [
                "bedrock:GetFoundationModelAvailability",
                "bedrock:ListFoundationModels"
            ],
            "Resource": [
                "*"
            ]
        }
    ]
}

```

You must then click on **Edit Trust Policy** and replace it with the following
policy, then click on **Update Policy**.

```
{
    "Version": "2012-10-17",
    "Statement": [
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
                   "Service": "sagemaker.amazonaws.com"
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
