

# AWS managed policies for SageMaker AI training session APIs
<a name="training-sessions-security-iam-awsmanpol"></a>

Use these AWS managed policies to create and interact with Amazon SageMaker AI training session APIs. With `AmazonSageMakerTrainingSessionAccess`, you can manage training sessions and run training and sampling operations. With `AmazonSageMakerTrainingSessionFullAccess`, your training session execution role can access data in Amazon S3, use customer managed AWS Key Management Service (AWS KMS) keys, publish model packages, and manage Amazon VPC network interfaces.

**Topics**
+ [AWS managed policy: AmazonSageMakerTrainingSessionAccess](#training-sessions-awsmanpol-AmazonSageMakerTrainingSessionAccess)
+ [AWS managed policy: AmazonSageMakerTrainingSessionFullAccess](#training-sessions-awsmanpol-AmazonSageMakerTrainingSessionFullAccess)
+ [Amazon SageMaker AI updates to SageMaker AI training sessions managed policies](#training-sessions-awsmanpol-updates)

## AWS managed policy: AmazonSageMakerTrainingSessionAccess
<a name="training-sessions-awsmanpol-AmazonSageMakerTrainingSessionAccess"></a>

With this policy, you can create and manage SageMaker AI training sessions and run training and sampling operations against them. Attach this policy to the IAM users and roles that create and interact with training sessions.

**Permissions details**

This policy includes the following permissions.
+ `sagemaker` – Allows creating, describing, stopping, deleting, and tagging training sessions. Restricted to resources in the same account.
+ `sagemaker` – Allows running training and sampling operations against a training session, retrieving their results, and invoking sample requests. Restricted to resources in the same account.
+ `sagemaker` – Allows listing training sessions. Restricted to resources in the same account.
+ `sagemaker` – Allows calling SageMaker AI training session runtime APIs with a bearer token. Restricted to resources in the same account.
+ `kms` – Allows the caller identity to use customer managed AWS KMS keys with training sessions at runtime. The `Decrypt` and `GenerateDataKey` actions are restricted through `kms:ViaService` to SageMaker AI only. Restricted to resources in the same account.
+ `iam` – Allows passing an execution role to SageMaker AI. The `iam:PassRole` action is restricted to roles under the `service-role` path whose names contain `SageMaker`, is restricted through `iam:PassedToService` to the SageMaker AI training session service only, and applies only when the role is associated with a SageMaker AI resource. Restricted to resources in the same account.
+ `sagemaker` – Allows creating model package groups, deleting model packages, describing model packages and model package groups, and listing model packages, for checkpoint publication workflows. Restricted to resources in the same account.
+ `sagemaker` – Allows describing and listing public hub content, such as pre-built models, in the AWS owned SageMaker AI public hub.
+ `s3` – Allows creating the SageMaker AI default Amazon S3 bucket, listing its contents, and deleting output objects in buckets whose names begin with `sagemaker-`. Restricted to resources in the same account.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "SageMakerTrainingSessionControlPlanePermissions",
            "Effect": "Allow",
            "Action": [
                "sagemaker:CreateTrainingSession",
                "sagemaker:DescribeTrainingSession",
                "sagemaker:StopTrainingSession",
                "sagemaker:DeleteTrainingSession",
                "sagemaker:AddTags"
            ],
            "Resource": "arn:aws:sagemaker:*:*:training-session/*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
                }
            }
        },
        {
            "Sid": "SageMakerTrainingSessionRuntimePermissions",
            "Effect": "Allow",
            "Action": [
                "sagemaker:ExecuteTrainingOperation",
                "sagemaker:GetTrainingOperationResult",
                "sagemaker:ExecuteSamplingOperation",
                "sagemaker:GetSamplingOperationResult",
                "sagemaker:SampleTrainingSession",
                "sagemaker:SampleTrainingSessionWithResponseStream"
            ],
            "Resource": "arn:aws:sagemaker:*:*:training-session/*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
                }
            }
        },
        {
            "Sid": "SageMakerTrainingSessionRuntimeKmsPermissions",
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
        },
        {
            "Sid": "SageMakerTrainingSessionListPermissions",
            "Effect": "Allow",
            "Action": [
                "sagemaker:ListTrainingSessions"
            ],
            "Resource": "*",
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
            "Sid": "PassExecutionRolePermissions",
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
                "ArnLike": {
                    "iam:AssociatedResourceArn": "arn:aws:sagemaker:*:*:*"
                },
                "StringEquals": {
                    "aws:ResourceAccount": "${aws:PrincipalAccount}",
                    "iam:PassedToService": [
                        "training-session.sagemaker.amazonaws.com"
                    ]
                }
            }
        },
        {
            "Sid": "SageMakerTrainingSessionModelPackagePermissions",
            "Effect": "Allow",
            "Action": [
                "sagemaker:CreateModelPackageGroup",
                "sagemaker:DeleteModelPackage",
                "sagemaker:DescribeModelPackageGroup",
                "sagemaker:DescribeModelPackage",
                "sagemaker:ListModelPackages"
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
            "Sid": "SageMakerTrainingSessionPublicHubPermissions",
            "Effect": "Allow",
            "Action": [
                "sagemaker:DescribeHubContent",
                "sagemaker:ListHubContents"
            ],
            "Resource": [
                "arn:aws:sagemaker:*:aws:hub/SageMakerPublicHub",
                "arn:aws:sagemaker:*:aws:hub-content/SageMakerPublicHub/*"
            ]
        },
        {
            "Sid": "SageMakerTrainingSessionS3Permissions",
            "Effect": "Allow",
            "Action": [
                "s3:CreateBucket",
                "s3:DeleteObject",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::sagemaker-*",
                "arn:aws:s3:::sagemaker-*/*"
            ],
            "Condition": {
                "StringEquals": {
                    "s3:ResourceAccount": "${aws:PrincipalAccount}"
                }
            }
        }
    ]
}
```

For more information, see [AmazonSageMakerTrainingSessionAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonSageMakerTrainingSessionAccess.html) in the AWS Managed Policy Reference Guide.

## AWS managed policy: AmazonSageMakerTrainingSessionFullAccess
<a name="training-sessions-awsmanpol-AmazonSageMakerTrainingSessionFullAccess"></a>

With this policy, your SageMaker AI training session execution roles can access the resources needed to run training sessions. Attach this policy to IAM roles that you use as SageMaker AI training session execution roles.

**Permissions details**

This policy includes the following permissions.
+ `s3` – Allows training sessions to read input data from, write output data to, and list the contents of Amazon S3 buckets. Restricted to resources in the same account.
+ `kms` – Allows training sessions to decrypt and generate data keys for server-side encryption of Amazon S3 objects using customer managed AWS KMS keys. The `Decrypt` and `GenerateDataKey` actions are restricted through `kms:ViaService` to Amazon S3 only. `DescribeKey` is allowed without the `kms:ViaService` restriction. Restricted to resources in the same account.
+ `sagemaker` – Allows describing public hub content, such as pre-built models, in the AWS owned SageMaker AI public hub.
+ `sagemaker` – Allows accessing, creating, and describing model packages, and describing model package groups for checkpoint publication workflows. Restricted to resources in the same account.
+ `ec2` – Allows managing Amazon VPC network interfaces for training sessions running in Amazon VPC mode, including creating, deleting, and describing network interfaces and related Amazon VPC resources. The `ec2:CreateTags` action is restricted to the `CreateNetworkInterface` action. Restricted to resources in the same account.

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
            "Sid": "SageMakerPublicHubReadPermissions",
            "Effect": "Allow",
            "Action": [
                "sagemaker:DescribeHubContent"
            ],
            "Resource": [
                "arn:aws:sagemaker:*:aws:hub/SageMakerPublicHub",
                "arn:aws:sagemaker:*:aws:hub-content/SageMakerPublicHub/*"
            ]
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
        }
    ]
}
```

For more information, see [AmazonSageMakerTrainingSessionFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonSageMakerTrainingSessionFullAccess.html) in the AWS Managed Policy Reference Guide.

## Amazon SageMaker AI updates to SageMaker AI training sessions managed policies
<a name="training-sessions-awsmanpol-updates"></a>

View the following table for a history of AWS managed policies for SageMaker AI training sessions, including each policy version and the date it was added.


| Policy | Version | Change | Date | 
| --- | --- | --- | --- | 
| [AmazonSageMakerTrainingSessionAccess](#training-sessions-awsmanpol-AmazonSageMakerTrainingSessionAccess) – New policy | 1 | Initial policy (version 1). | October 13, 2026 | 
| [AmazonSageMakerTrainingSessionFullAccess](#training-sessions-awsmanpol-AmazonSageMakerTrainingSessionFullAccess) – New policy | 1 | Initial policy (version 1). | October 13, 2026 | 