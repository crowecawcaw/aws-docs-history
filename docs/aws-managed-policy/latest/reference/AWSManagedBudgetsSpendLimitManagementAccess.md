

# AWSManagedBudgetsSpendLimitManagementAccess
<a name="AWSManagedBudgetsSpendLimitManagementAccess"></a>

**Description**: Grants the AWS Budgets service permissions to attach and detach Service Control Policies and manage accounts in an AWS Organization to enforce spend limit guardrails on member accounts.

`AWSManagedBudgetsSpendLimitManagementAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSManagedBudgetsSpendLimitManagementAccess-how-to-use"></a>

You can attach `AWSManagedBudgetsSpendLimitManagementAccess` to your users, groups, and roles.

## Policy details
<a name="AWSManagedBudgetsSpendLimitManagementAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: July 17, 2026, 21:12 UTC 
+ **Edited time:** August 07, 2026, 21:07 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AWSManagedBudgetsSpendLimitManagementAccess`

## Policy version
<a name="AWSManagedBudgetsSpendLimitManagementAccess-version"></a>

**Policy version:** v2 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSManagedBudgetsSpendLimitManagementAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "SCPActions",
      "Effect" : "Allow",
      "Action" : [
        "organizations:AttachPolicy",
        "organizations:DescribePolicy",
        "organizations:DetachPolicy"
      ],
      "Resource" : "arn:aws:organizations::*:policy/*/service_control_policy/*",
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceTag/ManagedBy" : "SpendLimit"
        }
      }
    },
    {
      "Sid" : "SCPListPolicyAction",
      "Effect" : "Allow",
      "Action" : "organizations:ListPolicies",
      "Resource" : "*"
    },
    {
      "Sid" : "SCPTargetActions",
      "Effect" : "Allow",
      "Action" : [
        "organizations:AttachPolicy",
        "organizations:DetachPolicy"
      ],
      "Resource" : "arn:aws:organizations::*:account/*"
    },
    {
      "Sid" : "AccountActions",
      "Effect" : "Allow",
      "Action" : "organizations:CloseAccount",
      "Resource" : "arn:aws:organizations::*:account/*"
    }
  ]
}
```

## Learn more
<a name="AWSManagedBudgetsSpendLimitManagementAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)