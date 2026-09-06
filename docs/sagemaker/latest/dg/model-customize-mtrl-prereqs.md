

# Prerequisites
<a name="model-customize-mtrl-prereqs"></a>

Multi-turn RL uses the SageMaker AI `CreateJob` API, which requires additional permissions on top of the existing model customization prerequisites. The table below summarizes what's new versus already covered.


| What | Status | Notes | 
| --- | --- | --- | 
| Trust policy: job.sagemaker.amazonaws.com | New | Required for CreateJob API | 
| Trust policy: bedrock-agentcore.amazonaws.com | New | Required on agent runtime role (AgentCore path only) | 
| PassRole: job.sagemaker.amazonaws.com | New | Existing prereqs only cover sagemaker.amazonaws.com | 
| Job actions (CreateJob, DescribeJob, etc.) | New | Not in AmazonSageMakerFullAccess | 
| bedrock-agentcore:ListAgentRuntimes | New | Required for Studio runtime picker | 
| bedrock-agentcore:ListAgentRuntimeVersions | New | Required for Studio version selector | 
| AmazonSageMakerJobFullAccess managed policy | New | Attach to job execution role | 
| AmazonSageMakerJobRuntimeAccess managed policy | New | Attach to agent runtime role | 
| Lambda, Bedrock deployment, S3, KMS, MLflow, CloudWatch | Already covered | Via existing prereqs or managed policies | 

## Caller role
<a name="model-customize-mtrl-prereqs-caller-role"></a>

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PassRoleForCreateJob",
      "Effect": "Allow",
      "Action": "iam:PassRole",
      "Resource": "arn:aws:iam::<account-id>:role/<ExecutionRoleName>",
      "Condition": {
        "StringEquals": {
          "iam:PassedToService": "job.sagemaker.amazonaws.com"
        }
      }
    },
    {
      "Sid": "MTRLJobActions",
      "Effect": "Allow",
      "Action": [
        "sagemaker:CreateJob",
        "sagemaker:DescribeJob",
        "sagemaker:StopJob",
        "sagemaker:DeleteJob"
      ],
      "Resource": "arn:aws:sagemaker:*:*:job/*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceAccount": "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid": "MTRLListJobsPermission",
      "Effect": "Allow",
      "Action": [
        "sagemaker:ListJobs",
        "sagemaker:ListJobSchemaVersions",
        "sagemaker:DescribeJobSchemaVersion"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceAccount": "${aws:PrincipalAccount}"
        }
      }
    }
  ]
}
```

PassRole — lets the caller delegate the execution role to `job.sagemaker.amazonaws.com`.

## Managed policies
<a name="model-customize-mtrl-prereqs-managed-policies"></a>

Multi-turn RL uses two AWS managed policies. Attach each to the appropriate role before creating a job.

**AmazonSageMakerJobFullAccess** – attach to the SageMaker AI job execution role (the `RoleArn` you pass to `CreateJob`).

This policy grants the job the permissions it needs while running: read/write access to training data and checkpoints in S3, KMS permissions for S3-side encryption, access to SageMaker AI hub content and model packages, MLflow experiment tracing, agent invocation via Bedrock AgentCore or Lambda, VPC network interface management, and CloudWatch Logs writes. Reference: [AmazonSageMakerJobFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonSageMakerJobFullAccess.html).

**AmazonSageMakerJobRuntimeAccess** – attach to the agent runtime role (the role your agent runs under, whether on Bedrock AgentCore or behind a Lambda forwarder). This policy grants the runtime APIs your agent calls during a rollout: `sagemaker:Sample`, `sagemaker:SampleWithResponseStream`, `sagemaker:CompleteRollout`, `sagemaker:UpdateReward`, and `sagemaker:CallWithBearerToken`. Reference: [AmazonSageMakerJobRuntimeAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonSageMakerJobRuntimeAccess.html).

## Trust policy updates
<a name="model-customize-mtrl-prereqs-trust-policy"></a>

Add `job.sagemaker.amazonaws.com` to your execution role's trust policy:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "job.sagemaker.amazonaws.com"
      },
      "Action": ["sts:AssumeRole", "sts:TagSession"]
    }
  ]
}
```

If using Bedrock AgentCore, your agent runtime role also needs its own trust policy:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "bedrock-agentcore.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

## Additional inline policy for Studio UI
<a name="model-customize-mtrl-prereqs-studio-policy"></a>

If you are submitting jobs through SageMaker AI Studio, add the following inline policy to your SageMaker AI domain execution role:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "MTRLJobActions",
      "Effect": "Allow",
      "Action": [
        "sagemaker:CreateJob",
        "sagemaker:DescribeJob",
        "sagemaker:StopJob",
        "sagemaker:DeleteJob",
        "sagemaker:ListJobs",
        "sagemaker:ListJobSchemaVersions",
        "sagemaker:DescribeJobSchemaVersion"
      ],
      "Resource": "arn:aws:sagemaker:*:*:job/*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceAccount": "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid": "BedrockAgentCoreListPermissions",
      "Effect": "Allow",
      "Action": [
        "bedrock-agentcore:ListAgentRuntimes",
        "bedrock-agentcore:ListAgentRuntimeVersions"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceAccount": "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid": "PassRoleForCreateJob",
      "Effect": "Allow",
      "Action": "iam:PassRole",
      "Resource": "arn:aws:iam::*:role/*",
      "Condition": {
        "StringEquals": {
          "iam:PassedToService": "job.sagemaker.amazonaws.com",
          "aws:ResourceAccount": "${aws:PrincipalAccount}"
        }
      }
    }
  ]
}
```

## Custom policy option
<a name="model-customize-mtrl-prereqs-custom-policy"></a>

If you prefer to define your own policies instead of using the AWS managed ones, use the following as a starting point.

**SageMaker AI job execution role policy** (equivalent to `AmazonSageMakerJobFullAccess`):

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

**Trust relationship for the execution role:**

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "job.sagemaker.amazonaws.com"
      },
      "Action": ["sts:AssumeRole", "sts:TagSession"]
    }
  ]
}
```

**AmazonSageMakerJobRuntimeAccess equivalent \+ BedrockAgentCoreFullAccess**

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "SageMakerJobRuntimePermissions",
      "Effect": "Allow",
      "Action": [
        "sagemaker:Sample",
        "sagemaker:SampleWithResponseStream",
        "sagemaker:CompleteRollout",
        "sagemaker:UpdateReward"
      ],
      "Resource": "arn:aws:sagemaker:*:*:job/*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceAccount": "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid": "BearerTokenPermissions",
      "Effect": "Allow",
      "Action": [
        "sagemaker:CallWithBearerToken"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceAccount": "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid": "KMSPermissionsForMTRLRuntime",
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
          "kms:ViaService": "sagemaker.*.amazonaws.com"
        }
      }
    }
  ]
}
```

**Trust relationship for the agent runtime role:**

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "bedrock-agentcore.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

## Lambda forwarder note
<a name="model-customize-mtrl-prereqs-lambda-forwarder"></a>

The existing model customization Lambda permissions cover functions with *SageMaker* or *sagemaker* in the name. If your Lambda forwarder uses a different naming convention, add its ARN explicitly:

```
{
  "Sid": "CustomAgentLambdaPermission",
  "Effect": "Allow",
  "Action": ["lambda:InvokeFunction"],
  "Resource": "arn:aws:lambda:*:*:function:your-agent-forwarder-function-name",
  "Condition": {
    "StringEquals": {"aws:ResourceAccount": "${aws:PrincipalAccount}"}
  }
}
```

## Other Setup
<a name="model-customize-mtrl-prereqs-other-setup"></a>
+ If you use a customer-managed VPC, see [Configure a VPC for multi-turn RL jobs](model-customize-mtrl-vpc.md).
+ If you use a customer-managed KMS key to encrypt job input and output, the execution role, caller role, and agent runtime role must have additional permissions. See [Encryption at rest for multi-turn reinforcement learning](model-customize-mtrl-encryption-at-rest.md).