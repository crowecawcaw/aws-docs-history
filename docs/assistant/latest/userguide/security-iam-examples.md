

# Identity-based policy examples for the AWS assistant
<a name="security-iam-examples"></a>

**The AWS assistant uses the `q` service prefix**  
Technical names didn't change when Amazon Q Developer in the AWS Management Console became the AWS assistant. The following example policies use the `q` service prefix in IAM actions, such as `q:SendMessage`.

The following example policies control access to the AWS assistant in the AWS Management Console and AWS Console Mobile Application.

For the `AmazonQDeveloperAccess` and `AmazonQFullAccess` AWS managed policies, see [AWS managed policies for Amazon Q Developer](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/managed-policy.html) in the *Amazon Q Developer User Guide*.

## User permissions
<a name="iam-examples-users"></a>

Attach one or more of the following policies to the IAM identities that use the AWS assistant.

### Allow users to access the AWS assistant with a Pro subscription
<a name="iam-example-pro"></a>

The following example policy grants permission to use the AWS assistant with a Amazon Q Developer Pro subscription. Without these permissions, you can access only the Free tier. To chat or use other capabilities, you also need permissions such as those in the following example policies.

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Sid": "AllowGetIdentity",
            "Effect": "Allow",
            "Action": [
                "q:GetIdentityMetaData"
            ],
            "Resource": "*"
        },
        {
            "Sid": "AllowSetTrustedIdentity",
            "Effect": "Allow",
            "Action": [
                "sts:SetContext"
            ],
            "Resource": "arn:aws:sts::*:self"
        }
    ]
}
```

### Allow the AWS assistant to access customer managed keys
<a name="iam-example-kms"></a>

The following example policy allows the AWS assistant to use a customer managed key. Users need this policy if an administrator has configured a customer managed key for encryption.

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Sid": "QKMSDecryptGenerateDataKeyPermissions",
            "Effect": "Allow",
            "Action": [
                "kms:Decrypt",
                "kms:GenerateDataKey",
                "kms:GenerateDataKeyWithoutPlaintext",
                "kms:ReEncryptFrom",
                "kms:ReEncryptTo"
            ],
            "Resource": [
            "arn:aws:kms:{{us-east-1}}:{{111122223333}}:key/{{key_id}}"
            ],
            "Condition": {
                "StringLike": {
                    "kms:ViaService": [
                    "q.{{us-east-1}}.amazonaws.com"
                    ]
                }
            }
        }
    ]
}
```

### Allow users to chat with the AWS assistant
<a name="iam-example-chat"></a>

The following example policy grants permission to chat with the AWS assistant in the AWS Management Console.

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Sid": "AllowAmazonQConversationAccess",
      "Effect": "Allow",
      "Action": [
        "q:StartConversation",
        "q:SendMessage",
        "q:GetConversation",
        "q:ListConversations",
        "q:UpdateConversation",
        "q:DeleteConversation"
      ],
      "Resource": "*"
    }
  ]
}
```

### Allow users to diagnose console errors
<a name="iam-example-diagnose"></a>

The following example policy grants permission to diagnose console errors with the AWS assistant.

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Sid": "AllowAmazonQTroubleshooting",
      "Effect": "Allow",
      "Action": [
        "q:StartTroubleshootingAnalysis",
        "q:GetTroubleshootingResults",
        "q:StartTroubleshootingResolutionExplanation",
        "q:UpdateTroubleshootingCommandResult",
        "q:PassRequest"
      ],
      "Resource": "*"
    }
  ]
}
```

### Allow users to chat about resources
<a name="iam-example-resource-chat"></a>

The following example policy grants permission to chat about resources. It also allows the AWS assistant to retrieve resource information on your behalf. The AWS assistant can access only resources that your IAM identity can access.

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Sid": "AllowAmazonQPassRequest",
      "Effect": "Allow",
      "Action": [
        "q:StartConversation",
        "q:SendMessage",
        "q:GetConversation",
        "q:ListConversations",
        "q:UpdateConversation",
        "q:DeleteConversation",
        "q:PassRequest"
      ],
      "Resource": "*"
    }
  ]
}
```

### Allow the AWS assistant to perform actions on your behalf
<a name="iam-example-actions"></a>

The following example policy grants permission to chat with the AWS assistant. It also allows the AWS assistant to perform actions on your behalf. The AWS assistant can perform only actions that your IAM identity has permission to perform.

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Sid": "AllowAmazonQPassRequest",
      "Effect": "Allow",
      "Action": [
        "q:StartConversation",
        "q:SendMessage",
        "q:GetConversation",
        "q:ListConversations",
        "q:UpdateConversation",
        "q:DeleteConversation",
        "q:PassRequest"
      ],
      "Resource": "*"
    }
  ]
}
```

### Allow the AWS assistant to access cost data
<a name="iam-example-cost-chat"></a>

The following example policy grants permission to chat about costs. It also allows the AWS assistant to access cost data and provide cost analysis and optimization recommendations. The policy includes permissions for AWS Cost Explorer, Cost Optimization Hub, AWS Compute Optimizer, AWS Budgets, AWS Free Tier, AWS Pricing, and AWS Savings Plans and reservation recommendations.

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Sid": "AllowAmazonQChatAndPassRequest",
      "Effect": "Allow",
      "Action": [
        "q:StartConversation",
        "q:SendMessage",
        "q:GetConversation",
        "q:ListConversations",
        "q:UpdateConversation",
        "q:DeleteConversation",
        "q:PassRequest"
      ],
      "Resource": "*"
   },
    {
      "Sid": "AllowCostExplorerAccess",
      "Effect": "Allow",
      "Action": [
        "ce:GetCostAndUsage",
        "ce:GetCostAndUsageWithResources",
        "ce:GetCostForecast",
        "ce:GetUsageForecast",
        "ce:GetTags",
        "ce:GetCostCategories",
        "ce:GetDimensionValues",
        "ce:GetSavingsPlansUtilization",
        "ce:GetSavingsPlansCoverage",
        "ce:GetSavingsPlansUtilizationDetails",
        "ce:GetReservationUtilization",
        "ce:GetReservationCoverage",
        "ce:GetSavingsPlansPurchaseRecommendation",
        "ce:GetReservationPurchaseRecommendation",
        "ce:GetRightsizingRecommendation",
        "ce:GetAnomalies",
       "ce:GetCostAndUsageComparisons",
       "ce:GetCostComparisonDrivers"
      ],
      "Resource": "*"
   },
    {
      "Sid": "AllowCostOptimizationHubAccess",
      "Effect": "Allow",
      "Action": [
        "cost-optimization-hub:GetRecommendation",
        "cost-optimization-hub:ListRecommendations",
        "cost-optimization-hub:ListRecommendationSummaries"
      ],
      "Resource": "*"
   },
    {
      "Sid": "AllowComputeOptimizerAccess",
      "Effect": "Allow",
      "Action": [
        "compute-optimizer:GetAutoScalingGroupRecommendations",
        "compute-optimizer:GetEBSVolumeRecommendations",
        "compute-optimizer:GetEC2InstanceRecommendations",
        "compute-optimizer:GetECSServiceRecommendations",
        "compute-optimizer:GetRDSDatabaseRecommendations",
        "compute-optimizer:GetLambdaFunctionRecommendations",
        "compute-optimizer:GetIdleRecommendations",
        "compute-optimizer:GetLicenseRecommendations",
        "compute-optimizer:GetEffectiveRecommendationPreferences"
      ],
      "Resource": "*"
   },
    {
      "Sid": "AllowBudgetsAccess",
      "Effect": "Allow",
      "Action": [
        "budgets:ViewBudget"
      ],
      "Resource": "*"
   },
    {
      "Sid": "AllowFreeTierAccess",
      "Effect": "Allow",
      "Action": [
        "freetier:GetFreeTierUsage",
        "freetier:GetAccountPlanState",
        "freetier:ListAccountActivities",
       "freetier:GetAccountActivity"
      ],
      "Resource": "*"
   },
    {
      "Sid": "AllowPricingAccess",
      "Effect": "Allow",
      "Action": [
        "pricing:GetProducts",
        "pricing:GetAttributeValues",
        "pricing:DescribeServices"
      ],
      "Resource": "*"
   }
  ]
}
```

### Allow administrators to configure plugins
<a name="iam-example-admin-plugins"></a>

The following example policy grants administrators permissions to view and configure third party plugins in the Amazon Q Developer console. For more information about plugins, see [Using plugins with the AWS assistant](plugins.md).

**Note**  
To access the Amazon Q Developer console, administrators also need the permissions in [Allow administrators to use the Amazon Q Developer console](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/id-based-policy-examples-admins.html#q-admin-setup-admin-users) in the *Amazon Q Developer User Guide*.

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "q:CreatePlugin",
        "q:GetPlugin",
        "q:DeletePlugin",
        "q:ListPlugins",
        "q:ListPluginProviders",
        "q:UpdatePlugin",
        "q:CreateAuthGrant",
        "q:CreateOAuthAppConnection",
        "q:SendEvent",
        "q:UpdateAuthGrant",
        "q:UpdateOAuthAppConnection",
        "q:UpdatePlugin",
        "iam:CreateRole",
        "secretsmanager:CreateSecret"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "iam:PassRole"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "iam:PassedToService": [
            "q.amazonaws.com"
          ]
        }
      }
    }
  ]
}
```

### Allow administrators to configure plugins from one provider
<a name="iam-example-admin-plugins-one-provider"></a>

The following example policy grants an administrator permission to configure plugins from one provider, specified by the plugin ARN with the name of the plugin provider and a wildcard character (`*`).

**Note**  
To access the Amazon Q Developer console, administrators also need the permissions in [Allow administrators to use the Amazon Q Developer console](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/id-based-policy-examples-admins.html#q-admin-setup-admin-users) in the *Amazon Q Developer User Guide*.

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Sid": "AllowCreateProviderPlugin",
            "Effect": "Allow",
            "Action": [
                "q:CreatePlugin",
                "q:GetPlugin",
                "q:DeletePlugin"
            ],
            "Resource": "arn:aws:qdeveloper:{{us-east-1}}:{{111122223333}}:plugin/{{plugin-provider}}/*"
        }
    ]
}
```

To use this policy, replace the following in the ARN in the `Resource` field:
+ {{us-east-1}} – The AWS Region where the plugin will be created.
+ {{111122223333}} – The AWS account ID of the account where your plugin is configured.
+ {{plugin-provider}} – The name of the plugin provider that you want to allow configuration for, like `CloudZero`, `Datadog`, or `Wiz`. The plugin provider field is case sensitive.

### Allow users to chat with plugins from one provider
<a name="iam-example-plugin-type"></a>

The following example policy grants permission to chat with any plugin from a given provider that an administrator configures, specified by the plugin ARN with the name of the plugin provider and a wildcard character (`*`). If the plugin is deleted and re-configured, a user with these permissions keeps access to the newly configured plugin.

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Sid": "AllowAmazonQConversationAccess",
            "Effect": "Allow",
            "Action": [
                "q:StartConversation",
                "q:SendMessage",
                "q:GetConversation",
                "q:ListConversations",
                "q:UpdateConversation",
                "q:DeleteConversation"
            ],
            "Resource": "*"
        },
        {
            "Sid": "AllowAmazonQPluginAccess",
            "Effect": "Allow",
            "Action": [
                "q:UsePlugin"
            ],
            "Resource": "arn:aws:qdeveloper:{{us-east-1}}:{{111122223333}}:plugin/{{plugin-provider}}/*"
        }
    ]
}
```

To use this policy, replace the following in the ARN in the `Resource` field:
+ {{us-east-1}} – The AWS Region where the plugin was created.
+ {{111122223333}} – The AWS account ID of the account where your plugin is configured.
+ {{plugin-provider}} – The name of the plugin provider that you want to allow access to, like `CloudZero`, `Datadog`, or `Wiz`. The plugin provider field is case sensitive.

### Deny the AWS assistant permission to perform specific actions
<a name="iam-example-deny-some-actions"></a>

The following example policy grants permission to chat with the AWS assistant. It allows the AWS assistant to perform any action on your behalf that your IAM identity can perform, except Amazon EC2 actions. The policy uses the [`aws:CalledVia` global condition key](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-calledvia) to deny Amazon EC2 actions only when the AWS assistant calls them.

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "q:StartConversation",
        "q:SendMessage",
        "q:GetConversation",
        "q:ListConversations",
        "q:UpdateConversation",
        "q:DeleteConversation",
        "q:PassRequest"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Deny",
      "Action": [
        "ec2:*"
      ],
      "Resource": "*",
      "Condition": {
            "ForAnyValue:StringEquals": {
               "aws:CalledVia": ["q.amazonaws.com"]
            }
       }
    }
  ]
}
```

### Allow the AWS assistant permission to perform specific actions
<a name="iam-example-allow-some-actions"></a>

The following example policy grants your IAM identity permission to perform any Amazon EC2 action. However, the AWS assistant can call only `ec2:describeInstances` on your behalf. The policy uses the [`aws:CalledVia` global condition key](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-calledvia) to apply this restriction.

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "q:StartConversation",
        "q:SendMessage",
        "q:GetConversation",
        "q:ListConversations",
        "q:UpdateConversation",
        "q:DeleteConversation",
        "q:PassRequest"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "ec2:*"
      ],
      "Resource": "*",
      "Condition": {
            "ForAnyValue:StringNotEquals": {
               "aws:CalledVia": ["q.amazonaws.com"]
            }
       }
    },
    {
      "Effect": "Allow",
      "Action": [
        "ec2:describeInstances"
      ],
      "Resource": "*",
       "Condition": {
            "ForAnyValue:StringEquals": {
               "aws:CalledVia": ["q.amazonaws.com"]
            }
       }
    }
  ]
}
```

### Allow the AWS assistant to perform actions in specific Regions
<a name="iam-example-some-regions"></a>

The following example policy grants permission to chat with the AWS assistant. When the AWS assistant performs actions on your behalf, it can call only the `us-east-1` and `us-west-2` Regions. For more information, see [aws:RequestedRegion](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requestedregion) in the *IAM User Guide*.

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "q:StartConversation",
        "q:SendMessage",
        "q:GetConversation",
        "q:ListConversations",
        "q:UpdateConversation",
        "q:DeleteConversation",
        "q:PassRequest"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
            "aws:RequestedRegion": [
                "us-east-1",
                "us-west-2"
            ]
        }
      }
    }
  ]
}
```

### Deny the AWS assistant permission to perform actions on your behalf
<a name="iam-example-deny-actions"></a>

The following example policy prevents the AWS assistant from performing actions on your behalf.

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Sid": "DenyAmazonQPassRequest",
      "Effect": "Deny",
      "Action": [
        "q:PassRequest"
      ],
      "Resource": "*"
    }
  ]
}
```

### Deny access to the AWS assistant
<a name="iam-example-deny"></a>

The following example policy denies all permissions to use the AWS assistant.

**Note**  
When you deny access, the AWS assistant icon and chat panel still appear in the AWS Management Console and AWS Console Mobile Application.

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Sid": "DenyAmazonQFullAccess",
      "Effect": "Deny",
      "Action": [
        "q:*"
      ],
      "Resource": "*"
    }
  ]
}
```

## Service control policies
<a name="iam-examples-scps"></a>

Service control policies (SCPs) are organization policies that manage permissions in your organization. You can use an SCP to control which AWS assistant capabilities are available. For more information, see [Creating, updating, and deleting service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_create.html) in the *AWS Organizations User Guide*.

### Example SCP: Deny access outside the Europe (Frankfurt) Region
<a name="scp-example-deny-outside-eu"></a>

The following SCP denies access to AWS assistant chat and related Amazon Q Developer features outside the Europe (Frankfurt) Region (`eu-central-1`). Use it with an Amazon Q Developer profile in that Region to block features that store content and perform inference in the US.

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Sid": "DenyAmazonQDeveloperOutsideEU",
      "Effect": "Deny",
      "Action": [
         "codewhisperer:GenerateRecommendations",
         "q:SendMessage",
         "q:GenerateCodeFromCommands",
         "sqlworkbench:GetQSqlRecommendations"
         ],
      "Resource": "*",
      "Condition": {
        "StringNotEquals":
        {"aws:RequestedRegion": [ "eu-central-1"] }
      }
    }
  ]
}
```

### Example SCP: Deny access to the AWS assistant
<a name="scp-example-deny"></a>

The following SCP denies access to the AWS assistant.

**Note**  
When you deny access, the AWS assistant icon and chat panel still appear in the AWS Management Console and AWS Console Mobile Application.

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Sid": "DenyAmazonQFullAccess",
      "Effect": "Deny",
      "Action": [
        "q:*"
      ],
      "Resource": "*"
    }
  ]
}
```