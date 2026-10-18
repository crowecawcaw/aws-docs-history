

# AmazonSageMakerTrainingSessionAccess
<a name="AmazonSageMakerTrainingSessionAccess"></a>

**Description**: Provides permissions for a caller identity to create and manage Amazon SageMaker training sessions, run training and sampling operations, use customer managed AWS KMS keys through SageMaker, pass an execution role to SageMaker, publish model packages, access public hub content, and manage SageMaker default Amazon S3 buckets.

`AmazonSageMakerTrainingSessionAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonSageMakerTrainingSessionAccess-how-to-use"></a>

You can attach `AmazonSageMakerTrainingSessionAccess` to your users, groups, and roles.

## Policy details
<a name="AmazonSageMakerTrainingSessionAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: October 13, 2026, 00:37 UTC 
+ **Edited time:** October 13, 2026, 00:37 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AmazonSageMakerTrainingSessionAccess`

## Policy version
<a name="AmazonSageMakerTrainingSessionAccess-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonSageMakerTrainingSessionAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "SageMakerTrainingSessionControlPlanePermissions",
      "Effect" : "Allow",
      "Action" : [
        "sagemaker:CreateTrainingSession",
        "sagemaker:DescribeTrainingSession",
        "sagemaker:StopTrainingSession",
        "sagemaker:DeleteTrainingSession",
        "sagemaker:AddTags"
      ],
      "Resource" : "arn:aws:sagemaker:*:*:training-session/*",
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid" : "SageMakerTrainingSessionRuntimePermissions",
      "Effect" : "Allow",
      "Action" : [
        "sagemaker:ExecuteTrainingOperation",
        "sagemaker:GetTrainingOperationResult",
        "sagemaker:ExecuteSamplingOperation",
        "sagemaker:GetSamplingOperationResult",
        "sagemaker:SampleTrainingSession",
        "sagemaker:SampleTrainingSessionWithResponseStream"
      ],
      "Resource" : "arn:aws:sagemaker:*:*:training-session/*",
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid" : "SageMakerTrainingSessionRuntimeKmsPermissions",
      "Effect" : "Allow",
      "Action" : [
        "kms:Decrypt",
        "kms:GenerateDataKey"
      ],
      "Resource" : "arn:aws:kms:*:*:key/*",
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        },
        "StringLike" : {
          "kms:ViaService" : "sagemaker.*.amazonaws.com"
        }
      }
    },
    {
      "Sid" : "SageMakerTrainingSessionListPermissions",
      "Effect" : "Allow",
      "Action" : [
        "sagemaker:ListTrainingSessions"
      ],
      "Resource" : "*",
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid" : "BearerTokenPermissions",
      "Effect" : "Allow",
      "Action" : [
        "sagemaker:CallWithBearerToken"
      ],
      "Resource" : "*",
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid" : "PassExecutionRolePermissions",
      "Effect" : "Allow",
      "Action" : [
        "iam:PassRole"
      ],
      "Resource" : [
        "arn:aws:iam::*:role/service-role/*SageMaker*",
        "arn:aws:iam::*:role/service-role/*Sagemaker*",
        "arn:aws:iam::*:role/service-role/*sagemaker*"
      ],
      "Condition" : {
        "ArnLike" : {
          "iam:AssociatedResourceArn" : "arn:aws:sagemaker:*:*:*"
        },
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}",
          "iam:PassedToService" : [
            "training-session.sagemaker.amazonaws.com"
          ]
        }
      }
    },
    {
      "Sid" : "SageMakerTrainingSessionModelPackagePermissions",
      "Effect" : "Allow",
      "Action" : [
        "sagemaker:CreateModelPackageGroup",
        "sagemaker:DeleteModelPackage",
        "sagemaker:DescribeModelPackageGroup",
        "sagemaker:DescribeModelPackage",
        "sagemaker:ListModelPackages"
      ],
      "Resource" : [
        "arn:aws:sagemaker:*:*:model-package/*",
        "arn:aws:sagemaker:*:*:model-package-group/*"
      ],
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid" : "SageMakerTrainingSessionPublicHubPermissions",
      "Effect" : "Allow",
      "Action" : [
        "sagemaker:DescribeHubContent",
        "sagemaker:ListHubContents"
      ],
      "Resource" : [
        "arn:aws:sagemaker:*:aws:hub/SageMakerPublicHub",
        "arn:aws:sagemaker:*:aws:hub-content/SageMakerPublicHub/*"
      ]
    },
    {
      "Sid" : "SageMakerTrainingSessionS3Permissions",
      "Effect" : "Allow",
      "Action" : [
        "s3:CreateBucket",
        "s3:DeleteObject",
        "s3:ListBucket"
      ],
      "Resource" : [
        "arn:aws:s3:::sagemaker-*",
        "arn:aws:s3:::sagemaker-*/*"
      ],
      "Condition" : {
        "StringEquals" : {
          "s3:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    }
  ]
}
```

## Learn more
<a name="AmazonSageMakerTrainingSessionAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)