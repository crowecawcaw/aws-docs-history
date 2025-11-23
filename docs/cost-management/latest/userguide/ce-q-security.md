# Security for cost management capabilities in Amazon Q

Developer

The following provides an overview of permissions and data protection for the cost
management capabilities in Amazon Q Developer.

## Permissions overview

To use the cost management capabilities in Amazon Q Developer, you need three sets of Identity and Access Management (IAM) permissions:

1. **Amazon Q permissions**: Permissions to chat with Amazon Q in the console (such as `q:StartConversation` and q:SendMessage)
2. **Service permissions**: Permissions to access the underlying Billing and Cost Management services that provide cost data
3. **PassRequest permission**: The `q:PassRequest` permission that allows Amazon Q to call AWS APIs on your behalf

The quickest way for an administrator to grant users access to Amazon Q Developer is to use the `AmazonQFullAccess` managed policy.

## Permissions for cost management capabilities

The following IAM policy statement grants users access to all cost management capabilities in Amazon Q Developer:

```
{
    "Version": "2012-10-17",
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

You can scope down this policy to grant access to only specific cost management capabilities. For example, if you don't want users to access resource-level cost data, you can remove the `ce:GetCostAndUsageWithResources` action, or add an explicit deny statement.

## q:PassRequest permission

`q:PassRequest` is an Amazon Q Developer permission that allows Amazon Q Developer to call AWS APIs on your behalf. When you add the `q:PassRequest` permission to an IAM identity, Amazon Q Developer gains permission to call any API that the IAM identity has permission to call. For example, if an IAM role has the `ce:GetCostAndUsage` permission and the `q:PassRequest` permission, Amazon Q Developer can call the GetCostAndUsage API when a user assuming that IAM role asks Amazon Q Developer to retrieve cost and usage data from Cost Explorer.

You can also allow IAM principals to access Cost Explorer and to use Amazon Q Developer, but restrict them from using the cost analysis or cost optimization capabilities in Amazon Q Developer, by using the `aws:CalledVia` [global condition key](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-calledvia "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-calledvia"). The following IAM policy provides an example of using this condition key:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
           "Sid": "AllowQDeveloperAccess",
            "Effect": "Allow",
            "Action": [
                "q:StartConversation",
                "q:SendMessage",
                "q:GetConversation",
                "q:ListConversations",
                "q:PassRequest"
            ],
            "Resource": "*"
        },
        {
            "Sid": "AllowCostExplorerAccess",
            "Effect": "Allow",
            "Action": [
                "ce:*"
            ],
            "Resource": "*"
       },
        {
           "Sid": "DenyCostExplorerAccessViaAmazonQ",
            "Effect": "Deny",
            "Action": [
                "ce:*"
            ],
            "Resource": "*",
            "Condition": {
                "ForAnyValue:StringEquals": {
                    "aws:CalledVia": [
                        "q.amazonaws.com"
                    ]
                }
            }
        }
    ]
}
```

## Multi-account access

For users of AWS Organizations, management account administrators can restrict member account users' access to Cost Explorer and Cost Optimization Hub data (including access to discounts, credits, and refunds) using the Cost Management preferences in the AWS Billing and Cost Management console. These preferences apply to Amazon Q Developer in the same way that they apply to the management console, SDK, and CLI. Amazon Q Developer respects the existing preferences of customers.

## Cross-region calls

Data from the Cost Optimization Hub and Cost Explorer services is hosted in the US East (N. Virginia) Region. Data from AWS Compute Optimizer is hosted in the AWS Region where the underlying resources, such as EC2 instances, are located. Data served from the AWS Price List APIs is hosted in us-east-1, eu-central-1, and ap-south-1 (note that AWS Price List APIs do not serve any customer-specific data). Cost management requests in Amazon Q Developer may require cross-region calls. For more information, see [Cross-region processing in Amazon Q Developer](../../../amazonq/latest/qdeveloper-ug/cross-region-processing.md "../../../amazonq/latest/qdeveloper-ug/cross-region-processing.md") in the _Amazon Q Developer User Guide_.

## Data protection

We may use certain content from Amazon Q Developer Free Tier for service improvement. Amazon Q Developer may use this content, for example, to provide better responses to common questions, fix Amazon Q Developer operational issues, for debugging, or for model training. Content that AWS may use for service improvement includes, for example, your questions to Amazon Q Developer and the responses and code that Amazon Q Developer generates. We do not use content from Amazon Q Developer Pro or Amazon Q Business for service improvement.

The way you opt out of Amazon Q Developer Free Tier using content for service improvement depends on the environment where you use Amazon Q. For the AWS Management Console, AWS Console Mobile Application, AWS websites, and AWS Chatbot, configure an AI services opt-out policy in AWS Organizations. For more information, see [AI services opt-out policies](../../../organizations/latest/userguide/orgs_manage_policies_ai-opt-out.md "../../../organizations/latest/userguide/orgs_manage_policies_ai-opt-out.md") in the _AWS Organizations User Guide_.
