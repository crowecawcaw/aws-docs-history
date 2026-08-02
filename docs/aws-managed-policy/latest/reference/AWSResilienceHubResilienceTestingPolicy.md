# AWSResilienceHubResilienceTestingPolicy

**Description**: Policy for AWS Resilience Hub service role which allows access to AWS Fault Injection Service in order to start resilience testing.

`AWSResilienceHubResilienceTestingPolicy` is an [AWS managed policy](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies").

## Using this policy

You can attach `AWSResilienceHubResilienceTestingPolicy` to your users, groups, and roles.

## Policy details

- **Type**: AWS managed policy
- **Creation time**: July 31, 2026, 22:27 UTC
- **Edited time:** July 31, 2026, 22:27 UTC
- **ARN**:
  `arn:aws:iam::aws:policy/AWSResilienceHubResilienceTestingPolicy`

## Policy version

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a
request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request.

## JSON policy document

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "AWSResilienceHubFISActionStatement",
      "Effect" : "Allow",
      "Action" : "fis:CreateExperimentTemplate",
      "Resource" : "arn:aws:fis:*:*:action/*"
    },
    {
      "Sid" : "AWSResilienceHubFISCreateExperimentTemplateStatement",
      "Effect" : "Allow",
      "Action" : "fis:CreateExperimentTemplate",
      "Resource" : "arn:aws:fis:*:*:experiment-template/*",
      "Condition" : {
        "StringEquals" : {
          "aws:RequestTag/managedBy" : "resiliencehub"
        }
      }
    },
    {
      "Sid" : "AWSResilienceHubFISStartExperimentFromTemplateStatement",
      "Effect" : "Allow",
      "Action" : "fis:StartExperiment",
      "Resource" : "arn:aws:fis:*:*:experiment-template/*",
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceTag/managedBy" : "resiliencehub"
        }
      }
    },
    {
      "Sid" : "AWSResilienceHubFISStartExperimentStatement",
      "Effect" : "Allow",
      "Action" : "fis:StartExperiment",
      "Resource" : "arn:aws:fis:*:*:experiment/*",
      "Condition" : {
        "StringEquals" : {
          "aws:RequestTag/managedBy" : "resiliencehub"
        }
      }
    },
    {
      "Sid" : "AWSResilienceHubFISExperimentStatement",
      "Effect" : "Allow",
      "Action" : [
        "fis:GetExperiment",
        "fis:StopExperiment",
        "fis:ListExperimentResolvedTargets"
      ],
      "Resource" : "arn:aws:fis:*:*:experiment/*",
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceTag/managedBy" : "resiliencehub"
        }
      }
    },
    {
      "Sid" : "AWSResilienceHubFISExperimentTemplateStatement",
      "Effect" : "Allow",
      "Action" : [
        "fis:CreateTargetAccountConfiguration",
        "fis:DeleteExperimentTemplate"
      ],
      "Resource" : "arn:aws:fis:*:*:experiment-template/*",
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceTag/managedBy" : "resiliencehub"
        }
      }
    },
    {
      "Sid" : "AWSResilienceHubFISPassRoleStatement",
      "Effect" : "Allow",
      "Action" : "iam:PassRole",
      "Resource" : "arn:aws:iam::*:role/*",
      "Condition" : {
        "StringEquals" : {
          "iam:PassedToService" : "fis.amazonaws.com"
        }
      }
    },
    {
      "Sid" : "AWSResilienceHubFISTagResourceStatement",
      "Effect" : "Allow",
      "Action" : "fis:TagResource",
      "Resource" : [
        "arn:aws:fis:*:*:experiment-template/*",
        "arn:aws:fis:*:*:experiment/*"
      ],
      "Condition" : {
        "StringEquals" : {
          "aws:RequestTag/managedBy" : "resiliencehub"
        }
      }
    },
    {
      "Sid" : "AWSResilienceHubRegionSwitchStatement",
      "Effect" : "Allow",
      "Action" : [
        "arc-region-switch:ListPlanExecutions",
        "arc-region-switch:GetPlanExecution"
      ],
      "Resource" : "arn:aws:arc-region-switch::*:plan/*:*"
    },
    {
      "Sid" : "AWSResilienceHubFISCreateSLRStatement",
      "Effect" : "Allow",
      "Action" : "iam:CreateServiceLinkedRole",
      "Resource" : "arn:aws:iam::*:role/*",
      "Condition" : {
        "StringEquals" : {
          "iam:AWSServiceName" : "fis.amazonaws.com"
        }
      }
    },
    {
      "Sid" : "AWSResilienceHubCloudWatchAlarmStatement",
      "Effect" : "Allow",
      "Action" : "cloudwatch:DescribeAlarmHistory",
      "Resource" : "*"
    }
  ]
}
```

## Learn more

- [Create a permission set using AWS managed policies in IAM Identity Center](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md")
- [Adding and removing IAM identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md")
- [Understand versioning for IAM policies](../../../IAM/latest/UserGuide/access_policies_managed-versioning.md "../../../IAM/latest/UserGuide/access_policies_managed-versioning.md")
- [Get started with AWS managed policies and move toward least-privilege permissions](../../../IAM/latest/UserGuide/best-practices.md#bp-use-aws-defined-policies "../../../IAM/latest/UserGuide/best-practices.md#bp-use-aws-defined-policies")
