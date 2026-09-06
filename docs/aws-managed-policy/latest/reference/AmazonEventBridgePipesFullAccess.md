

# AmazonEventBridgePipesFullAccess
<a name="AmazonEventBridgePipesFullAccess"></a>

**Description**: Provides full access to Amazon EventBridge Pipes.

`AmazonEventBridgePipesFullAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonEventBridgePipesFullAccess-how-to-use"></a>

You can attach `AmazonEventBridgePipesFullAccess` to your users, groups, and roles.

## Policy details
<a name="AmazonEventBridgePipesFullAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: December 01, 2022, 17:03 UTC 
+ **Edited time:** December 01, 2022, 17:03 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AmazonEventBridgePipesFullAccess`

## Policy version
<a name="AmazonEventBridgePipesFullAccess-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonEventBridgePipesFullAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "EventBridgePipesActions",
      "Effect" : "Allow",
      "Action" : "pipes:*",
      "Resource" : "*"
    },
    {
      "Sid" : "IAMPassRoleAccessForPipes",
      "Effect" : "Allow",
      "Action" : "iam:PassRole",
      "Resource" : "arn:aws:iam::*:role/*",
      "Condition" : {
        "StringLike" : {
          "iam:PassedToService" : "pipes.amazonaws.com"
        }
      }
    }
  ]
}
```

## Learn more
<a name="AmazonEventBridgePipesFullAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)