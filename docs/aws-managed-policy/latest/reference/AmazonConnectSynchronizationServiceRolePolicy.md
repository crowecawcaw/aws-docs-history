

# AmazonConnectSynchronizationServiceRolePolicy
<a name="AmazonConnectSynchronizationServiceRolePolicy"></a>

**Description**: Allows Amazon Connect to synchronize AWS resources across regions on your behalf.

`AmazonConnectSynchronizationServiceRolePolicy` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonConnectSynchronizationServiceRolePolicy-how-to-use"></a>

This policy is attached to a service-linked role that allows the service to perform actions on your behalf. You cannot attach this policy to your users, groups, or roles.

## Policy details
<a name="AmazonConnectSynchronizationServiceRolePolicy-details"></a>
+ **Type**: Service-linked role policy 
+ **Creation time**: October 27, 2023, 22:38 UTC 
+ **Edited time:** November 06, 2026, 19:27 UTC
+ **ARN**: `arn:aws:iam::aws:policy/aws-service-role/AmazonConnectSynchronizationServiceRolePolicy`

## Policy version
<a name="AmazonConnectSynchronizationServiceRolePolicy-version"></a>

**Policy version:** v8 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonConnectSynchronizationServiceRolePolicy-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "AllowConnectActions",
      "Effect" : "Allow",
      "Action" : [
        "connect:Create*",
        "connect:BatchCreate*",
        "connect:Update*",
        "connect:BatchUpdate*",
        "connect:Delete*",
        "connect:BatchDelete*",
        "connect:Describe*",
        "connect:BatchDescribe*",
        "connect:List*",
        "connect:Search*",
        "connect:Associate*",
        "connect:Disassociate*",
        "connect:Get*",
        "connect:BatchGet*",
        "connect:Import*",
        "connect:TagResource",
        "connect:UntagResource"
      ],
      "Resource" : "*"
    },
    {
      "Sid" : "DisallowedConnectActions",
      "Effect" : "Deny",
      "Action" : [
        "connect:Start*",
        "connect:Stop*",
        "connect:Resume*",
        "connect:Suspend*",
        "connect:*Contact",
        "connect:SearchContacts",
        "connect:*ContactAttributes*",
        "connect:*RealtimeContact*",
        "connect:*AnalyticsData*",
        "connect:*MetricData*",
        "connect:*UserData*",
        "connect:*ContactEvaluation",
        "connect:GetAttachedFile",
        "connect:BatchGetAttachedFileMetadata",
        "connect:DeleteAttachedFile",
        "connect:CompleteAttachedFileUpload",
        "connect:CreateAttachedFile",
        "connect:UpdateContactSchedule",
        "connect:UpdateContactRoutingData",
        "connect:ListContactReferences",
        "connect:CreateParticipant",
        "connect:CreatePersistentContactAssociation",
        "connect:CreateInstance",
        "connect:DeleteInstance",
        "connect:ListInstances",
        "connect:ReplicateInstance",
        "connect:GetFederationToken",
        "connect:ClaimPhoneNumber",
        "connect:ImportPhoneNumber",
        "connect:ReleasePhoneNumber",
        "connect:SearchAvailablePhoneNumbers",
        "connect:CreateTrafficDistributionGroup",
        "connect:DeleteTrafficDistributionGroup",
        "connect:GetTrafficDistribution",
        "connect:UpdateTrafficDistribution"
      ],
      "Resource" : "*"
    },
    {
      "Sid" : "AllowPutMetricsForConnectNamespace",
      "Effect" : "Allow",
      "Action" : "cloudwatch:PutMetricData",
      "Resource" : "*",
      "Condition" : {
        "StringEquals" : {
          "cloudwatch:namespace" : "AWS/Connect"
        }
      }
    },
    {
      "Sid" : "AllowAppIntegrationsListApplications",
      "Effect" : "Allow",
      "Action" : [
        "app-integrations:ListApplicationAssociations",
        "app-integrations:ListApplications"
      ],
      "Resource" : "*"
    },
    {
      "Sid" : "AllowAppIntegrationsScopedToApplications",
      "Effect" : "Allow",
      "Action" : [
        "app-integrations:CreateApplication",
        "app-integrations:CreateApplicationAssociation",
        "app-integrations:GetApplication",
        "app-integrations:UpdateApplication",
        "app-integrations:DeleteApplication",
        "app-integrations:ListTagsForResource",
        "app-integrations:TagResource",
        "app-integrations:UntagResource"
      ],
      "Resource" : "arn:aws:app-integrations:*:*:application/*",
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid" : "AllowAppIntegrationsScopedToApplicationAssociations",
      "Effect" : "Allow",
      "Action" : [
        "app-integrations:DeleteApplicationAssociation",
        "app-integrations:ListTagsForResource",
        "app-integrations:TagResource",
        "app-integrations:UntagResource"
      ],
      "Resource" : "arn:aws:app-integrations:*:*:application-association/*",
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid" : "AllowWisdomActions",
      "Effect" : "Allow",
      "Action" : [
        "wisdom:CreateAssistant",
        "wisdom:DeleteAssistant",
        "wisdom:GetAssistant",
        "wisdom:ListAssistants",
        "wisdom:UpdateAssistantAIAgent",
        "wisdom:RemoveAssistantAIAgent",
        "wisdom:CreateAssistantAssociation",
        "wisdom:DeleteAssistantAssociation",
        "wisdom:GetAssistantAssociation",
        "wisdom:ListAssistantAssociations",
        "wisdom:CreateAIAgent",
        "wisdom:CreateAIAgentVersion",
        "wisdom:DeleteAIAgent",
        "wisdom:DeleteAIAgentVersion",
        "wisdom:GetAIAgent",
        "wisdom:ListAIAgents",
        "wisdom:ListAIAgentVersions",
        "wisdom:UpdateAIAgent",
        "wisdom:CreateAIPrompt",
        "wisdom:CreateAIPromptVersion",
        "wisdom:DeleteAIPrompt",
        "wisdom:DeleteAIPromptVersion",
        "wisdom:GetAIPrompt",
        "wisdom:ListAIPrompts",
        "wisdom:ListAIPromptVersions",
        "wisdom:UpdateAIPrompt",
        "wisdom:CreateAIGuardrail",
        "wisdom:CreateAIGuardrailVersion",
        "wisdom:DeleteAIGuardrail",
        "wisdom:DeleteAIGuardrailVersion",
        "wisdom:GetAIGuardrail",
        "wisdom:ListAIGuardrails",
        "wisdom:ListAIGuardrailVersions",
        "wisdom:UpdateAIGuardrail",
        "wisdom:CreateKnowledgeBase",
        "wisdom:DeleteKnowledgeBase",
        "wisdom:GetKnowledgeBase",
        "wisdom:ListKnowledgeBases",
        "wisdom:UpdateKnowledgeBaseTemplateUri",
        "wisdom:RemoveKnowledgeBaseTemplateUri",
        "wisdom:CreateContent",
        "wisdom:StartContentUpload",
        "wisdom:DeleteContent",
        "wisdom:GetContent",
        "wisdom:GetContentSummary",
        "wisdom:ListContents",
        "wisdom:UpdateContent",
        "wisdom:CreateContentAssociation",
        "wisdom:DeleteContentAssociation",
        "wisdom:GetContentAssociation",
        "wisdom:ListContentAssociations",
        "wisdom:CreateQuickResponse",
        "wisdom:DeleteQuickResponse",
        "wisdom:GetQuickResponse",
        "wisdom:ListQuickResponses",
        "wisdom:UpdateQuickResponse",
        "wisdom:ListTagsForResource",
        "wisdom:TagResource",
        "wisdom:UntagResource",
        "wisdom:ListModels"
      ],
      "Resource" : "*",
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid" : "AllowKmsKeyValidationForQinConnectReplicaResources",
      "Effect" : "Allow",
      "Action" : "kms:DescribeKey",
      "Resource" : "arn:aws:kms:*:*:key/*",
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        },
        "StringLike" : {
          "kms:ViaService" : [
            "wisdom.*.amazonaws.com"
          ]
        }
      }
    },
    {
      "Sid" : "AllowKmsGrantCreationForQinConnectReplicaAssistant",
      "Effect" : "Allow",
      "Action" : "kms:CreateGrant",
      "Resource" : "arn:aws:kms:*:*:key/*",
      "Condition" : {
        "Bool" : {
          "kms:GrantIsForAWSResource" : "true"
        },
        "ForAllValues:StringEquals" : {
          "kms:EncryptionContextKeys" : [
            "aws:wisdom:assistant:arn"
          ],
          "kms:GrantOperations" : [
            "DescribeKey",
            "Decrypt",
            "GenerateDataKey",
            "CreateGrant"
          ]
        },
        "Null" : {
          "kms:EncryptionContextKeys" : "false",
          "kms:GrantOperations" : "false"
        },
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}",
          "kms:GrantConstraintType" : "EncryptionContextSubset"
        },
        "StringLike" : {
          "kms:EncryptionContext:aws:wisdom:assistant:arn" : "arn:aws:wisdom:*:${aws:PrincipalAccount}:assistant/*",
          "kms:ViaService" : "wisdom.*.amazonaws.com"
        }
      }
    },
    {
      "Sid" : "AllowKmsGrantCreationForQinConnectReplicaKnowledgeBase",
      "Effect" : "Allow",
      "Action" : "kms:CreateGrant",
      "Resource" : "arn:aws:kms:*:*:key/*",
      "Condition" : {
        "Bool" : {
          "kms:GrantIsForAWSResource" : "true"
        },
        "ForAllValues:StringEquals" : {
          "kms:EncryptionContextKeys" : [
            "aws:wisdom:knowledgeBase:arn"
          ],
          "kms:GrantOperations" : [
            "DescribeKey",
            "Decrypt",
            "GenerateDataKey",
            "CreateGrant"
          ]
        },
        "Null" : {
          "kms:EncryptionContextKeys" : "false",
          "kms:GrantOperations" : "false"
        },
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}",
          "kms:GrantConstraintType" : "EncryptionContextSubset"
        },
        "StringLike" : {
          "kms:EncryptionContext:aws:wisdom:knowledgeBase:arn" : "arn:aws:wisdom:*:${aws:PrincipalAccount}:knowledge-base/*",
          "kms:ViaService" : "wisdom.*.amazonaws.com"
        }
      }
    },
    {
      "Sid" : "AllowKmsCryptoForQinConnectReplicaAssistant",
      "Effect" : "Allow",
      "Action" : [
        "kms:Decrypt",
        "kms:GenerateDataKey",
        "kms:GenerateDataKeyWithoutPlaintext"
      ],
      "Resource" : "arn:aws:kms:*:*:key/*",
      "Condition" : {
        "ForAllValues:StringEquals" : {
          "kms:EncryptionContextKeys" : [
            "aws:wisdom:assistant:arn"
          ]
        },
        "Null" : {
          "kms:EncryptionContextKeys" : "false"
        },
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        },
        "StringLike" : {
          "kms:EncryptionContext:aws:wisdom:assistant:arn" : "arn:aws:wisdom:*:${aws:PrincipalAccount}:assistant/*",
          "kms:ViaService" : "wisdom.*.amazonaws.com"
        }
      }
    },
    {
      "Sid" : "AllowKmsCryptoForQinConnectReplicaKnowledgeBase",
      "Effect" : "Allow",
      "Action" : [
        "kms:Decrypt",
        "kms:GenerateDataKey",
        "kms:GenerateDataKeyWithoutPlaintext"
      ],
      "Resource" : "arn:aws:kms:*:*:key/*",
      "Condition" : {
        "ForAllValues:StringEquals" : {
          "kms:EncryptionContextKeys" : [
            "aws:wisdom:knowledgeBase:arn"
          ]
        },
        "Null" : {
          "kms:EncryptionContextKeys" : "false"
        },
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        },
        "StringLike" : {
          "kms:EncryptionContext:aws:wisdom:knowledgeBase:arn" : "arn:aws:wisdom:*:${aws:PrincipalAccount}:knowledge-base/*",
          "kms:ViaService" : "wisdom.*.amazonaws.com"
        }
      }
    },
    {
      "Sid" : "AllowKmsGrantCreationForQinConnectInstanceAssociationAssistant",
      "Effect" : "Allow",
      "Action" : "kms:CreateGrant",
      "Resource" : "arn:aws:kms:*:*:key/*",
      "Condition" : {
        "Bool" : {
          "kms:GrantIsForAWSResource" : "true"
        },
        "ForAllValues:StringEquals" : {
          "kms:EncryptionContextKeys" : [
            "aws:wisdom:assistant:arn"
          ],
          "kms:GrantOperations" : [
            "DescribeKey",
            "Decrypt",
            "GenerateDataKey",
            "GenerateDataKeyPair"
          ]
        },
        "Null" : {
          "kms:EncryptionContextKeys" : "false",
          "kms:GrantOperations" : "false"
        },
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}",
          "kms:GrantConstraintType" : "EncryptionContextEquals"
        },
        "StringLike" : {
          "kms:EncryptionContext:aws:wisdom:assistant:arn" : "arn:aws:wisdom:*:${aws:PrincipalAccount}:assistant/*",
          "kms:ViaService" : "connect.*.amazonaws.com"
        }
      }
    },
    {
      "Sid" : "AllowKmsGrantCreationForQinConnectInstanceAssociationKnowledgeBase",
      "Effect" : "Allow",
      "Action" : "kms:CreateGrant",
      "Resource" : "arn:aws:kms:*:*:key/*",
      "Condition" : {
        "Bool" : {
          "kms:GrantIsForAWSResource" : "true"
        },
        "ForAllValues:StringEquals" : {
          "kms:EncryptionContextKeys" : [
            "aws:wisdom:knowledgeBase:arn"
          ],
          "kms:GrantOperations" : [
            "DescribeKey",
            "Decrypt",
            "GenerateDataKey",
            "GenerateDataKeyPair"
          ]
        },
        "Null" : {
          "kms:EncryptionContextKeys" : "false",
          "kms:GrantOperations" : "false"
        },
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}",
          "kms:GrantConstraintType" : "EncryptionContextEquals"
        },
        "StringLike" : {
          "kms:EncryptionContext:aws:wisdom:knowledgeBase:arn" : "arn:aws:wisdom:*:${aws:PrincipalAccount}:knowledge-base/*",
          "kms:ViaService" : "connect.*.amazonaws.com"
        }
      }
    }
  ]
}
```

## Learn more
<a name="AmazonConnectSynchronizationServiceRolePolicy-learn-more"></a>
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)