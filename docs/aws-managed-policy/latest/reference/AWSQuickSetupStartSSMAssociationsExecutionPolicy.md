

# AWSQuickSetupStartSSMAssociationsExecutionPolicy
<a name="AWSQuickSetupStartSSMAssociationsExecutionPolicy"></a>

**Description**: This policy grants permissions that allow principals to run the AWSQuickSetupType-StartSSMAssociations Automation runbook, which starts State Manager Associations.

`AWSQuickSetupStartSSMAssociationsExecutionPolicy` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSQuickSetupStartSSMAssociationsExecutionPolicy-how-to-use"></a>

You can attach `AWSQuickSetupStartSSMAssociationsExecutionPolicy` to your users, groups, and roles.

## Policy details
<a name="AWSQuickSetupStartSSMAssociationsExecutionPolicy-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: August 08, 2025, 12:04 UTC 
+ **Edited time:** March 05, 2026, 16:57 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AWSQuickSetupStartSSMAssociationsExecutionPolicy`

## Policy version
<a name="AWSQuickSetupStartSSMAssociationsExecutionPolicy-version"></a>

**Policy version:** v7 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSQuickSetupStartSSMAssociationsExecutionPolicy-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "ssm:StartAutomationExecution"
      ],
      "Resource" : [
        "arn:aws:ssm:*:*:document/AWSQuickSetupType-Scheduler-ChangeCalendarState",
        "arn:aws:ssm:*:*:automation-execution/*",
        "arn:aws:ssm:*:*:automation-definition/AWSQuickSetupType-Scheduler-ChangeCalendarState*"
      ]
    },
    {
      "Effect" : "Allow",
      "Action" : "iam:PassRole",
      "Resource" : [
        "arn:aws:iam::*:role/AWS-QuickSetup*"
      ],
      "Condition" : {
        "StringEquals" : {
          "iam:PassedToService" : [
            "ssm.amazonaws.com"
          ]
        },
        "ArnLike" : {
          "iam:AssociatedResourceARN" : [
            "arn:aws:ssm:*:*:document/AWSQuickSetupType-Scheduler-ChangeCalendarState",
            "arn:aws:ssm:*:*:automation-execution/*",
            "arn:aws:ssm:*:*:automation-definition/AWSQuickSetupType-Scheduler-ChangeCalendarState*"
          ]
        }
      }
    }
  ]
}
```

## Learn more
<a name="AWSQuickSetupStartSSMAssociationsExecutionPolicy-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)