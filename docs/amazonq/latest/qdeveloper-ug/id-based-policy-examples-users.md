

# User permissions
<a name="id-based-policy-examples-users"></a>

The following policies allow users to access features of Amazon Q Developer on AWS apps and websites, including the AWS Management Console, AWS Console Mobile Application, and AWS Documentation site.

For policies that enable administrative access to Amazon Q Developer, see [Administrator permissions](id-based-policy-examples-admins.md). 

**Note**  
Users accessing [Amazon Q in the IDE](q-in-IDE.md) or [Amazon Q on the command line](command-line.md) don't require IAM permissions. 

## Allow users to access Amazon Q with an Amazon Q Developer Pro subscription
<a name="id-based-policy-examples-allow-subs-access"></a>

The following example policy grants permission to use Amazon Q with an Amazon Q Developer Pro subscription. Without these permissions, users can only access the Free tier of Amazon Q. To chat with Amazon Q or use other Amazon Q features, users need additional permissions, such as those granted by the example policies in this section.

------
#### [ JSON ]

****  

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

------

## Allow Amazon Q access to customer managed keys
<a name="id-based-policy-examples-allow-q-access-encryption"></a>

The following example policy grants users permissions to access features encrypted with a customer managed key by allowing Amazon Q access to the key. This policy is required to use Amazon Q if an administrator has set up a customer managed key for encryption.

------
#### [ JSON ]

****  

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

------

## Allow users to chat with Amazon Q
<a name="id-based-policy-examples-allow-chat"></a>

The following example policy grants permissions to chat with Amazon Q in the console.

------
#### [ JSON ]

****  

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

------

## Allow users to use Amazon Q CLI with AWS CloudShell
<a name="id-based-policy-examples-allow-cli-cloudshell"></a>

The following example policy grants permissions to use Amazon Q CLI with AWS CloudShell.

**Note**  
The `codewhisperer` prefix is a legacy name from a service that merged with Amazon Q Developer. For more information, see [Amazon Q Developer rename - Summary of changes](service-rename.md). 

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "codewhisperer:GenerateRecommendations",
                "codewhisperer:ListCustomizations"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "q:StartConversation",
                "q:SendMessage"
            ],
            "Resource": "*"
        }
    ]
}
```

------

## Allow users to run transformations on the command line
<a name="id-based-policy-examples-allow-cli-transformations"></a>

The following example policy grants permissions to transform code with the [Amazon Q command line tool for transformations](transform-CLI.md). This policy does not affect access to [Amazon Q on the command line](command-line.md).

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
              "qdeveloper:StartAgentSession",
              "qdeveloper:ImportArtifact",
              "qdeveloper:ExportArtifact",
              "qdeveloper:TransformCode"
            ],
            "Resource": "*"
        }
    ]
}
```

------

## Allow users to diagnose console errors with Amazon Q
<a name="id-based-policy-examples-allow-error-diagnosing"></a>

The following example policy grants permissions to diagnose console errors with Amazon Q.

------
#### [ JSON ]

****  

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
        "q:PassRequest",
        "cloudformation:GetResource"
      ],
      "Resource": "*"
    }
  ]
}
```

------

## Allow users to generate code from CLI commands with Amazon Q
<a name="id-based-policy-examples-allow-console-to-code"></a>

The following example policy grants permissions to generate code from recorded CLI commands with Amazon Q, which enables the use of the Console-to-Code feature.

------
#### [ JSON ]

****  

```
{
   "Version":"2012-10-17",		 	 	 
   "Statement": [
       {
         "Sid": "AllowAmazonQConsoleToCode",
         "Effect": "Allow",
         "Action": "q:GenerateCodeFromCommands",
         "Resource": "*"
       }
   ]
}
```

------

## Allow users to chat about resources with Amazon Q
<a name="id-based-policy-examples-allow-resource-chat"></a>

The following example policy grants permission to chat with Amazon Q about resources, and allows Amazon Q to retrieve resource information on your behalf. Amazon Q only has permission to access resources that your IAM identity has permissions for. 

------
#### [ JSON ]

****  

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
    },
    {
      "Sid": "AllowCloudControlReadAccess",
      "Effect": "Allow",
      "Action": [
         "cloudformation:GetResource",
         "cloudformation:ListResources"
      ],
      "Resource": "*"
    }
  ]
}
```

------

## Allow Amazon Q to perform actions on your behalf in chat
<a name="id-based-policy-examples-allow-actions"></a>

The following example policy grants permission to chat with Amazon Q, and allows Amazon Q to perform actions on your behalf. Amazon Q only has permission to perform actions that your IAM identity has permission to perform. 

------
#### [ JSON ]

****  

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

------

## Allow users to use Q artifacts in Amazon Q (preview)
<a name="id-based-policy-examples-allow-artifacts"></a>

The following example policy grants permission to use Amazon Q artifacts, which enables you to complete multi-service jobs in Amazon Q. This policy includes permissions for Amazon Q, IAM, and CloudFormation.

In addition to these permissions, you must have access to the resources you ask about. Amazon Q will never access resources that your IAM identity doesn't have access to.

**Important**  
This example policy includes IAM actions (`iam:CreateRole`, `iam:CreatePolicy`, `iam:AttachRolePolicy`, and `iam:PutRolePolicy`) with unrestricted resources. Some Amazon Q workflows include steps that create or configure IAM roles as part of connecting AWS services (for example, creating a role that grants an EC2 instance access to S3). These permissions are required for those steps to execute successfully. If your identity already has administrator access, these permissions are already granted. For non-administrator identities, only grant this policy to trusted users in your account. If you do not need workflows that create or modify IAM roles, you can remove the IAM actions from this policy — steps that require IAM permissions will display a permissions error.

```
{
    "Version": "2012-10-17", 		 	 	 
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
        },
        {
            "Sid": "AllowQArtifactsAccess",
            "Effect": "Allow",
            "Action": [
                "q:GetArtifact",
                "q:CreateArtifact",
                "q:GetArtifactActionResult",
                "q:PerformArtifactAction",
                "iam:CreateRole",
                "iam:CreatePolicy",
                "iam:AttachRolePolicy",
                "iam:PutRolePolicy",
                "cloudformation:GetResource",
                "cloudformation:ListResources",
                "cloudformation:CancelResourceRequest",
                "cloudformation:CreateResource",
                "cloudformation:GetResourceRequestStatus",
                "cloudformation:ListResourceRequests",
                "cloudformation:UpdateResource"
            ],
            "Resource": "*"
        }
    ]
}
```

## Allow Amazon Q to access cost data and provide cost optimization recommendations
<a name="id-based-policy-examples-allow-cost-chat"></a>

The following example policy grants permission to chat with Amazon Q about your costs and allows Amazon Q to access your cost data and provide cost analysis and optimization recommendations. This policy includes permissions for AWS Cost Explorer, AWS Cost Optimization Hub, AWS Compute Optimizer, AWS Budgets, AWS Free Tier, AWS Pricing, and Savings Plans and reservation recommendations.

------
#### [ JSON ]

****  

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

------

## Deny Amazon Q permission to perform specific actions on your behalf
<a name="id-based-policy-examples-deny-some-actions"></a>

The following example policy grants permission to chat with Amazon Q, and allows Amazon Q to perform any action on your behalf that your IAM identity has permission to perform, except for Amazon EC2 actions. This policy uses the [`aws:CalledVia` global condition key](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-calledvia) to specify that Amazon EC2 actions are only denied when Amazon Q calls them. 

------
#### [ JSON ]

****  

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

------

## Allow Amazon Q permission to perform specific actions on your behalf
<a name="id-based-policy-examples-allow-some-actions"></a>

The following example policy grants permission to chat with Amazon Q, and allows Amazon Q to perform any action on your behalf that your IAM identity has permission to perform, with the exception of Amazon EC2 actions. This policy grants your IAM identity permission to perform any Amazon EC2 action, but only allows Amazon Q to perform the `ec2:describeInstances` action. This policy uses the [`aws:CalledVia` global condition key](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-calledvia) to specify that Amazon Q is only allowed to call `ec2:describeInstances`, and not any other Amazon EC2 actions.

------
#### [ JSON ]

****  

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

------

## Allow Amazon Q permission to perform actions on your behalf in specific regions
<a name="id-based-policy-examples-allow-actions-some-regions"></a>

The following example policy grants permission to chat with Amazon Q, and allows Amazon Q to make calls to only the `us-east-1` and `us-west-2` Regions when performing actions on your behalf. Amazon Q can't make calls to any other Region. For more information on how to specify what Regions you can make calls to, see [aws:RequestedRegion](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requestedregion) in the *AWS Identity and Access Management User Guide*.

------
#### [ JSON ]

****  

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

------

## Deny Amazon Q permission to perform actions on your behalf
<a name="id-based-policy-examples-deny-actions"></a>

The following example policy prevents Amazon Q from performing actions on your behalf.

------
#### [ JSON ]

****  

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

------

## Allow users to chat with plugins from one provider
<a name="id-based-policy-examples-allow-plugin-type"></a>

The following example policy grants permission to chat with any plugin from a given provider that an administrator configures, specified by the plugin ARN with the name of the plugin provider and a wildcard character (`*`). If the plugin is deleted and re-configured, a user with these permissions will retain access to the newly configured plugin. To use this policy, replace the following in the ARN in the `Resource` field: 
+ {{AWS-region}} – The AWS Region where the plugin was created.
+ {{AWS-account-ID}} – The AWS account ID of the account where your plugin is configured.
+ {{plugin-provider}} – The name of the plugin provider that you want to allow access to, like `CloudZero`, `Datadog`, or `Wiz`. The plugin provider field is case sensitive.

------
#### [ JSON ]

****  

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

------

## Allow users to chat with a specific plugin
<a name="id-based-policy-examples-allow-plugin-arn"></a>

The following example policy grants permission to chat with a specific plugin, specified by the plugin ARN. If the plugin is deleted and re-configured, a user will not have access to the new plugin unless the plugin ARN is updated in this policy. To use this policy, replace the following in the ARN in the `Resource` field: 
+ {{AWS-region}} – The AWS Region where the plugin was created.
+ {{AWS-account-ID}} – The AWS account ID of the account where your plugin is configured.
+ {{plugin-provider}} – The name of the plugin provider that you want to allow access to, like `CloudZero`, `Datadog`, or `Wiz`. The plugin provider field is case sensitive.
+ {{plugin-ARN}} – The ARN of the plugin you want to allow access to.

## Deny access to Amazon Q
<a name="id-based-policy-examples-deny"></a>

The following example policy denies all permissions to use Amazon Q.

**Note**  
When you deny access to Amazon Q, the Amazon Q icon and chat panel will still appear in the AWS console, AWS website, AWS documentation pages, or AWS Console Mobile Application.

------
#### [ JSON ]

****  

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

------

## Allow users to view their permissions
<a name="id-based-policy-examples-view-own-permissions"></a>

This example shows how you might create a policy that allows IAM users to view the inline and managed policies that are attached to their user identity. This policy includes permissions to complete this action on the console or programmatically using the AWS CLI or AWS API.

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "ViewOwnUserInfo",
            "Effect": "Allow",
            "Action": [
                "iam:GetUserPolicy",
                "iam:ListGroupsForUser",
                "iam:ListAttachedUserPolicies",
                "iam:ListUserPolicies",
                "iam:GetUser"
            ],
            "Resource": ["arn:aws:iam::*:user/${aws:username}"]
        },
        {
            "Sid": "NavigateInConsole",
            "Effect": "Allow",
            "Action": [
                "iam:GetGroupPolicy",
                "iam:GetPolicyVersion",
                "iam:GetPolicy",
                "iam:ListAttachedGroupPolicies",
                "iam:ListGroupPolicies",
                "iam:ListPolicyVersions",
                "iam:ListPolicies",
                "iam:ListUsers"
            ],
            "Resource": "*"
        }
    ]
}
```