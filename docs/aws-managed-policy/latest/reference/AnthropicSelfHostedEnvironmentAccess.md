

# AnthropicSelfHostedEnvironmentAccess
<a name="AnthropicSelfHostedEnvironmentAccess"></a>

**Description**: Provides access to operate a self-hosted environment runner for Claude Managed Agents

`AnthropicSelfHostedEnvironmentAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AnthropicSelfHostedEnvironmentAccess-how-to-use"></a>

You can attach `AnthropicSelfHostedEnvironmentAccess` to your users, groups, and roles.

## Policy details
<a name="AnthropicSelfHostedEnvironmentAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: June 12, 2026, 17:12 UTC 
+ **Edited time:** June 12, 2026, 17:12 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AnthropicSelfHostedEnvironmentAccess`

## Policy version
<a name="AnthropicSelfHostedEnvironmentAccess-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AnthropicSelfHostedEnvironmentAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "AnthropicSelfHostedEnvironmentWorkspace",
      "Effect" : "Allow",
      "Action" : [
        "aws-external-anthropic:GetEnvironment",
        "aws-external-anthropic:GetSession",
        "aws-external-anthropic:GetSkill",
        "aws-external-anthropic:ProcessEnvironmentWork",
        "aws-external-anthropic:UpdateSession"
      ],
      "Resource" : "arn:aws:aws-external-anthropic:*:*:workspace/*"
    },
    {
      "Sid" : "AnthropicSelfHostedEnvironmentResourceless",
      "Effect" : "Allow",
      "Action" : [
        "aws-external-anthropic:CallWithBearerToken"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AnthropicSelfHostedEnvironmentAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)