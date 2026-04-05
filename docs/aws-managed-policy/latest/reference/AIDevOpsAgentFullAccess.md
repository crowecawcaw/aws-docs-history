# AIDevOpsAgentFullAccess

**Description**: Provides full access to Amazon DevOps Agent via the AWS Management Console

`AIDevOpsAgentFullAccess` is an [AWS managed policy](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies").

## Using this policy

You can attach `AIDevOpsAgentFullAccess` to your users, groups, and roles.

## Policy details

- **Type**: AWS managed policy
- **Creation time**: March 26, 2026, 03:42 UTC
- **Edited time:** March 26, 2026, 03:42 UTC
- **ARN**:
  `arn:aws:iam::aws:policy/AIDevOpsAgentFullAccess`

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
      "Sid" : "AIDevOpsAgentSpaceAccess",
      "Effect" : "Allow",
      "Action" : [
        "aidevops:CreateAgentSpace",
        "aidevops:DeleteAgentSpace",
        "aidevops:GetAgentSpace",
        "aidevops:ListAgentSpaces",
        "aidevops:UpdateAgentSpace"
      ],
      "Resource" : "*"
    },
    {
      "Sid" : "AIDevOpsServiceAccess",
      "Effect" : "Allow",
      "Action" : [
        "aidevops:DeregisterService",
        "aidevops:GetService",
        "aidevops:ListServices",
        "aidevops:RegisterService",
        "aidevops:SearchServiceAccessibleResource"
      ],
      "Resource" : "*"
    },
    {
      "Sid" : "AIDevOpsAssociationAccess",
      "Effect" : "Allow",
      "Action" : [
        "aidevops:AssociateService",
        "aidevops:DisassociateService",
        "aidevops:GetAssociation",
        "aidevops:ListAssociations",
        "aidevops:UpdateAssociation",
        "aidevops:ValidateAwsAssociations"
      ],
      "Resource" : "*"
    },
    {
      "Sid" : "AIDevOpsWebhookAccess",
      "Effect" : "Allow",
      "Action" : [
        "aidevops:ListWebhooks"
      ],
      "Resource" : "*"
    },
    {
      "Sid" : "AIDevOpsOperatorAppAccess",
      "Effect" : "Allow",
      "Action" : [
        "aidevops:DisableOperatorApp",
        "aidevops:EnableOperatorApp",
        "aidevops:GetOperatorApp",
        "aidevops:UpdateOperatorAppIdpConfig"
      ],
      "Resource" : "*"
    },
    {
      "Sid" : "AIDevOpsKnowledgeAccess",
      "Effect" : "Allow",
      "Action" : [
        "aidevops:CreateKnowledgeItem",
        "aidevops:DeleteKnowledgeItem",
        "aidevops:GetKnowledgeItem",
        "aidevops:ListKnowledgeItems",
        "aidevops:ListKnowledgeItemVersions",
        "aidevops:UpdateKnowledgeItem"
      ],
      "Resource" : "*"
    },
    {
      "Sid" : "AIDevOpsBacklogAccess",
      "Effect" : "Allow",
      "Action" : [
        "aidevops:CreateBacklogTask",
        "aidevops:GetBacklogTask",
        "aidevops:ListBacklogTasks",
        "aidevops:ListGoals",
        "aidevops:UpdateBacklogTask",
        "aidevops:UpdateGoal"
      ],
      "Resource" : "*"
    },
    {
      "Sid" : "AIDevOpsRecommendationAccess",
      "Effect" : "Allow",
      "Action" : [
        "aidevops:GetRecommendation",
        "aidevops:ListRecommendations",
        "aidevops:UpdateRecommendation"
      ],
      "Resource" : "*"
    },
    {
      "Sid" : "AIDevOpsAgentChatAccess",
      "Effect" : "Allow",
      "Action" : [
        "aidevops:CreateChat",
        "aidevops:ListChats",
        "aidevops:ListPendingMessages",
        "aidevops:SendMessage"
      ],
      "Resource" : "*"
    },
    {
      "Sid" : "AIDevOpsJournalAccess",
      "Effect" : "Allow",
      "Action" : [
        "aidevops:ListExecutions",
        "aidevops:ListJournalRecords"
      ],
      "Resource" : "*"
    },
    {
      "Sid" : "AIDevOpsTopologyAccess",
      "Effect" : "Allow",
      "Action" : [
        "aidevops:DiscoverTopology"
      ],
      "Resource" : "*"
    },
    {
      "Sid" : "AIDevOpsSupportAccess",
      "Effect" : "Allow",
      "Action" : [
        "aidevops:DescribeSupportLevel",
        "aidevops:EndChatForCase",
        "aidevops:InitiateChatForCase"
      ],
      "Resource" : "*"
    },
    {
      "Sid" : "AIDevOpsUsageAccess",
      "Effect" : "Allow",
      "Action" : [
        "aidevops:GetAccountUsage"
      ],
      "Resource" : "*"
    },
    {
      "Sid" : "AIDevOpsTaggingAccess",
      "Effect" : "Allow",
      "Action" : [
        "aidevops:ListTagsForResource",
        "aidevops:TagResource",
        "aidevops:UntagResource"
      ],
      "Resource" : "*"
    },
    {
      "Sid" : "AIDevOpsVendedLogs",
      "Effect" : "Allow",
      "Action" : [
        "aidevops:AllowVendedLogDeliveryForResource"
      ],
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
