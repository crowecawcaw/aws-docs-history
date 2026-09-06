

# AWSMcpServiceActionsFullAccess
<a name="AWSMcpServiceActionsFullAccess"></a>

**Description**: Provides full access to all MCP service actions. This policy does not grant access to the actions taken by the MCP, only the MCP actions themselves.

`AWSMcpServiceActionsFullAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSMcpServiceActionsFullAccess-how-to-use"></a>

You can attach `AWSMcpServiceActionsFullAccess` to your users, groups, and roles.

## Policy details
<a name="AWSMcpServiceActionsFullAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: November 21, 2025, 22:49 UTC 
+ **Edited time:** February 12, 2026, 17:57 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AWSMcpServiceActionsFullAccess`

## Policy version
<a name="AWSMcpServiceActionsFullAccess-version"></a>

**Policy version:** v3 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSMcpServiceActionsFullAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "AllowAllMCPServiceActions",
      "Effect" : "Allow",
      "Action" : "*",
      "Resource" : "*",
      "Condition" : {
        "Bool" : {
          "aws:IsMcpServiceAction" : "true"
        }
      }
    }
  ]
}
```

## Learn more
<a name="AWSMcpServiceActionsFullAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)