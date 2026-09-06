

# AWSBudgetsReadOnlyAccess
<a name="AWSBudgetsReadOnlyAccess"></a>

**Description**: Provides read only access to AWS Budgets Console via the AWS Management Console.

`AWSBudgetsReadOnlyAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSBudgetsReadOnlyAccess-how-to-use"></a>

You can attach `AWSBudgetsReadOnlyAccess` to your users, groups, and roles.

## Policy details
<a name="AWSBudgetsReadOnlyAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: October 15, 2020, 17:18 UTC 
+ **Edited time:** June 17, 2024, 17:41 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AWSBudgetsReadOnlyAccess`

## Policy version
<a name="AWSBudgetsReadOnlyAccess-version"></a>

**Policy version:** v2 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSBudgetsReadOnlyAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "AWSBudgetsReadOnlyAccess",
      "Effect" : "Allow",
      "Action" : [
        "aws-portal:ViewBilling",
        "budgets:ViewBudget",
        "budgets:Describe*",
        "budgets:ListTagsForResource"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AWSBudgetsReadOnlyAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)