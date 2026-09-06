

# AIDevOpsAgentFullAccess
<a name="AIDevOpsAgentFullAccess"></a>

**Description**: Provides full access to Amazon DevOps Agent via the AWS Management Console

`AIDevOpsAgentFullAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AIDevOpsAgentFullAccess-how-to-use"></a>

You can attach `AIDevOpsAgentFullAccess` to your users, groups, and roles.

## Policy details
<a name="AIDevOpsAgentFullAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: March 26, 2026, 03:42 UTC 
+ **Edited time:** June 26, 2026, 23:57 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AIDevOpsAgentFullAccess`

## Policy version
<a name="AIDevOpsAgentFullAccess-version"></a>

**Policy version:** v6 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AIDevOpsAgentFullAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "AIDevOpsAgentAccess",
      "Effect" : "Allow",
      "Action" : [
        "aidevops:AllowVendedLogDeliveryForResource",
        "aidevops:AssociateService",
        "aidevops:CreateAccessToken",
        "aidevops:CreateAgentSpace",
        "aidevops:CreateAsset",
        "aidevops:CreateAssetFile",
        "aidevops:CreateBacklogTask",
        "aidevops:CreateChat",
        "aidevops:CreateKnowledgeItem",
        "aidevops:CreateOneTimeLoginSession",
        "aidevops:CreatePrivateConnection",
        "aidevops:CreateTrigger",
        "aidevops:DeleteAgentSpace",
        "aidevops:DeleteAsset",
        "aidevops:DeleteAssetFile",
        "aidevops:DeleteKnowledgeItem",
        "aidevops:DeletePrivateConnection",
        "aidevops:DeleteTrigger",
        "aidevops:DeregisterService",
        "aidevops:DescribePrivateConnection",
        "aidevops:DescribeServices",
        "aidevops:DescribeSupportLevel",
        "aidevops:DisableOperatorApp",
        "aidevops:DisassociateService",
        "aidevops:DiscoverTopology",
        "aidevops:EnableOperatorApp",
        "aidevops:EndChatForCase",
        "aidevops:GetAccessToken",
        "aidevops:GetAccountUsage",
        "aidevops:GetAgentSpace",
        "aidevops:GetAsset",
        "aidevops:GetAssetContent",
        "aidevops:GetAssetFile",
        "aidevops:GetAssociation",
        "aidevops:GetBacklogTask",
        "aidevops:GetKnowledgeItem",
        "aidevops:GetOperatorApp",
        "aidevops:GetRecommendation",
        "aidevops:GetService",
        "aidevops:GetTrigger",
        "aidevops:InitiateChatForCase",
        "aidevops:ListAccessTokens",
        "aidevops:ListAgentSpaces",
        "aidevops:ListAssetFiles",
        "aidevops:ListAssets",
        "aidevops:ListAssetTypes",
        "aidevops:ListAssetVersions",
        "aidevops:ListAssociations",
        "aidevops:ListBacklogTasks",
        "aidevops:ListChats",
        "aidevops:ListExecutions",
        "aidevops:ListGoals",
        "aidevops:ListJournalRecords",
        "aidevops:ListKnowledgeItems",
        "aidevops:ListKnowledgeItemVersions",
        "aidevops:ListPendingMessages",
        "aidevops:ListPrivateConnections",
        "aidevops:ListRecommendations",
        "aidevops:ListServices",
        "aidevops:ListTagsForResource",
        "aidevops:ListTriggers",
        "aidevops:ListWebhooks",
        "aidevops:RegisterService",
        "aidevops:RevokeAccessToken",
        "aidevops:RotateAccessToken",
        "aidevops:SearchServiceAccessibleResource",
        "aidevops:SendMessage",
        "aidevops:TagResource",
        "aidevops:UntagResource",
        "aidevops:UpdateAgentSpace",
        "aidevops:UpdateApprovalAction",
        "aidevops:UpdateAsset",
        "aidevops:UpdateAssetFile",
        "aidevops:UpdateAssociation",
        "aidevops:UpdateBacklogTask",
        "aidevops:UpdateGoal",
        "aidevops:UpdateKnowledgeItem",
        "aidevops:UpdateOperatorAppIdpConfig",
        "aidevops:UpdatePrivateConnectionCertificate",
        "aidevops:UpdateRecommendation",
        "aidevops:UpdateTrigger",
        "aidevops:ValidateAwsAssociations"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AIDevOpsAgentFullAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)