

# AWSBudgetsActionExecutionPolicy

**Description**: Grants permissions to AWS Budgets so it can execute Budgets Actions to limit spend on your behalf using service APIs and policy restrictions.

`AWSBudgetsActionExecutionPolicy` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSBudgetsActionExecutionPolicy-how-to-use"></a>

This policy is attached to a service-linked role that allows the service to perform actions on your behalf. You cannot attach this policy to your users, groups, or roles.

## Policy details
<a name="AWSBudgetsActionExecutionPolicy-details"></a>
+ **Type**: Service-linked role policy 
+ **Creation time**: November 20, 2026, 21:37 UTC 
+ **Edited time:** November 20, 2026, 21:37 UTC
+ **ARN**: `arn:aws:iam::aws:policy/aws-service-role/AWSBudgetsActionExecutionPolicy`

## Policy version
<a name="AWSBudgetsActionExecutionPolicy-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSBudgetsActionExecutionPolicy-json"></a>

```json
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "CreateTaggedScp",
      "Effect" : "Allow",
      "Action" : "organizations:CreatePolicy",
      "Resource" : "arn:aws:organizations::*:policy/*/service_control_policy/*",
      "Condition" : {
        "StringEquals" : {
          "aws:RequestTag/budgets:managed" : "true",
          "organizations:PolicyType" : "SERVICE_CONTROL_POLICY"
        },
        "ForAllValues:StringEquals" : {
          "aws:TagKeys" : [
            "budgets:managed"
          ]
        }
      }
    },
    {
      "Sid" : "TagOnlyOwnScps",
      "Effect" : "Allow",
      "Action" : "organizations:TagResource",
      "Resource" : "arn:aws:organizations::*:policy/*/service_control_policy/*",
      "Condition" : {
        "StringEquals" : {
          "aws:RequestTag/budgets:managed" : "true",
          "aws:ResourceTag/budgets:managed" : "true"
        },
        "ForAllValues:StringEquals" : {
          "aws:TagKeys" : [
            "budgets:managed"
          ]
        }
      }
    },
    {
      "Sid" : "ManageOwnScps",
      "Effect" : "Allow",
      "Action" : [
        "organizations:DescribePolicy",
        "organizations:UpdatePolicy",
        "organizations:DeletePolicy",
        "organizations:AttachPolicy",
        "organizations:DetachPolicy",
        "organizations:ListTargetsForPolicy"
      ],
      "Resource" : "arn:aws:organizations::*:policy/*/service_control_policy/*",
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceTag/budgets:managed" : "true"
        }
      }
    },
    {
      "Sid" : "AttachTargets",
      "Effect" : "Allow",
      "Action" : [
        "organizations:AttachPolicy",
        "organizations:DetachPolicy"
      ],
      "Resource" : [
        "arn:aws:organizations::*:account/*",
        "arn:aws:organizations::*:ou/*",
        "arn:aws:organizations::*:root/*"
      ]
    },
    {
      "Sid" : "Read",
      "Effect" : "Allow",
      "Action" : [
        "organizations:ListRoots",
        "organizations:ListAccounts",
        "organizations:ListPolicies",
        "organizations:ListPoliciesForTarget"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AWSBudgetsActionExecutionPolicy-learn-more"></a>
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)