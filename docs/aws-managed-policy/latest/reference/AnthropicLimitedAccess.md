# AnthropicLimitedAccess

**Description**: Provides limited access to Claude Platform on AWS

`AnthropicLimitedAccess` is an [AWS managed policy](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies").

## Using this policy

You can attach `AnthropicLimitedAccess` to your users, groups, and roles.

## Policy details

- **Type**: AWS managed policy
- **Creation time**: April 01, 2026, 04:57 UTC
- **Edited time:** June 12, 2026, 16:57 UTC
- **ARN**:
  `arn:aws:iam::aws:policy/AnthropicLimitedAccess`

## Policy version

**Policy version:** v6 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a
request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request.

## JSON policy document

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "AnthropicLimitedWorkspace",
      "Effect" : "Allow",
      "Action" : [
        "aws-external-anthropic:Get*",
        "aws-external-anthropic:List*",
        "aws-external-anthropic:ArchiveAgent",
        "aws-external-anthropic:ArchiveEnvironment",
        "aws-external-anthropic:ArchiveMemoryStore",
        "aws-external-anthropic:ArchiveSession",
        "aws-external-anthropic:ArchiveVault",
        "aws-external-anthropic:CancelBatchInference",
        "aws-external-anthropic:CountTokens",
        "aws-external-anthropic:CreateAgent",
        "aws-external-anthropic:CreateBatchInference",
        "aws-external-anthropic:CreateEnvironment",
        "aws-external-anthropic:CreateFile",
        "aws-external-anthropic:CreateInference",
        "aws-external-anthropic:CreateMemoryStore",
        "aws-external-anthropic:CreateSession",
        "aws-external-anthropic:CreateSkill",
        "aws-external-anthropic:CreateUserProfile",
        "aws-external-anthropic:CreateVault",
        "aws-external-anthropic:CreateWebhook",
        "aws-external-anthropic:DeleteBatchInference",
        "aws-external-anthropic:DeleteEnvironment",
        "aws-external-anthropic:DeleteFile",
        "aws-external-anthropic:DeleteMemoryStore",
        "aws-external-anthropic:DeleteSession",
        "aws-external-anthropic:DeleteSkill",
        "aws-external-anthropic:DeleteVault",
        "aws-external-anthropic:DeleteWebhook",
        "aws-external-anthropic:ProcessEnvironmentWork",
        "aws-external-anthropic:RotateWebhookSecret",
        "aws-external-anthropic:UpdateAgent",
        "aws-external-anthropic:UpdateEnvironment",
        "aws-external-anthropic:UpdateMemoryStore",
        "aws-external-anthropic:UpdateSession",
        "aws-external-anthropic:UpdateSkill",
        "aws-external-anthropic:UpdateUserProfile",
        "aws-external-anthropic:UpdateVault",
        "aws-external-anthropic:UpdateWebhook"
      ],
      "Resource" : "arn:aws:aws-external-anthropic:*:*:workspace/*"
    },
    {
      "Sid" : "AnthropicLimitedResourceless",
      "Effect" : "Allow",
      "Action" : [
        "aws-external-anthropic:GetAccountStatus",
        "aws-external-anthropic:CallWithBearerToken"
      ],
      "Resource" : "*"
    },
    {
      "Sid" : "AnthropicLimitedGetToken",
      "Effect" : "Allow",
      "Action" : "sts:GetWebIdentityToken",
      "Resource" : "*",
      "Condition" : {
        "ForAnyValue:StringEquals" : {
          "sts:IdentityTokenAudience" : [
            "https://api.anthropic.com",
            "https://platform.claude.com"
          ]
        },
        "StringEquals" : {
          "aws:CalledViaLast" : "aws-external-anthropic.amazonaws.com"
        }
      }
    },
    {
      "Sid" : "AnthropicLimitedTagToken",
      "Effect" : "Allow",
      "Action" : "sts:TagGetWebIdentityToken",
      "Resource" : "*"
    },
    {
      "Sid" : "AnthropicLimitedConsoleAccess",
      "Effect" : "Allow",
      "Action" : "aws-external-anthropic:AssumeConsole",
      "Resource" : "*",
      "Condition" : {
        "StringEquals" : {
          "aws-external-anthropic:Capability" : "developer"
        }
      }
    }
  ]
}
```

## Learn more

- [Create a permission set using AWS managed policies in IAM Identity Center](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md")
- [Adding and removing IAM identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md")
- [Understand versioning for IAM policies](../../../IAM/latest/UserGuide/access_policies_managed-versioning.md "../../../IAM/latest/UserGuide/access_policies_managed-versioning.md")
- [Get started with AWS managed policies and move toward least-privilege permissions](../../../IAM/latest/UserGuide/best-practices.md#bp-use-aws-defined-policies "../../../IAM/latest/UserGuide/best-practices.md#bp-use-aws-defined-policies")
