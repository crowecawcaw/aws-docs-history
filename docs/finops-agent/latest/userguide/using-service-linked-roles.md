

AWS FinOps Agent is in preview release and is subject to change.

# Using service-linked roles for AWS FinOps Agent

AWS FinOps Agent uses an IAM [service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role). A service-linked role is a unique type of IAM role that is linked directly to AWS FinOps Agent. Service-linked roles are predefined by AWS FinOps Agent and include all the permissions that the service requires to call other AWS services on your behalf.

A service-linked role makes setting up AWS FinOps Agent for organization-wide access easier because you don't have to manually add the necessary permissions. AWS FinOps Agent defines the permissions of its service-linked role, and unless defined otherwise, only AWS FinOps Agent can assume the role. The defined permissions include the trust policy and the permissions policy, and that permissions policy cannot be attached to any other IAM entity.

For information about other services that support service-linked roles, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) and look for the services that have **Yes** in the **Service-linked role** column. Choose a **Yes** with a link to view the service-linked role documentation for that service.

## Service-linked role permissions for AWS FinOps Agent
<a name="service-linked-role-permissions"></a>

AWS FinOps Agent uses the service-linked role named `AWSServiceRoleForFinOpsAgent`. AWS FinOps Agent assumes this role in the management account and member accounts to read the cost, billing, optimization, and infrastructure data that supports organization-wide agent workflows.

The `AWSServiceRoleForFinOpsAgent` service-linked role trusts the following service to assume the role:
+ `finops-agent.amazonaws.com`

The role permissions policy named `AWSFinOpsAgentServiceRolePolicy` allows AWS FinOps Agent to complete the following actions on the specified resources. The permissions are primarily read-only and scoped to cost and infrastructure data. Additional actions let AWS FinOps Agent start cost analyses, run or cancel read-only queries in Data Hub, and manage Amazon EventBridge rules. The `events:ManagedBy` condition restricts the EventBridge write actions to rules that AWS FinOps Agent created on your behalf.

```json
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "CostExplorerReadAndAnalyzeAccess",
      "Effect": "Allow",
      "Action": [
        "ce:DescribeCostCategoryDefinition",
        "ce:GetAnomalies",
        "ce:GetAnomalyMonitors",
        "ce:GetCommitmentPurchaseAnalysis",
        "ce:GetCostAndUsage",
        "ce:GetCostAndUsageComparisons",
        "ce:GetCostAndUsageWithResources",
        "ce:GetCostCategories",
        "ce:GetCostComparisonDrivers",
        "ce:GetCostForecast",
        "ce:GetDimensionValues",
        "ce:GetReservationCoverage",
        "ce:GetReservationPurchaseRecommendation",
        "ce:GetReservationUtilization",
        "ce:GetSavingsPlanPurchaseRecommendationDetails",
        "ce:GetSavingsPlansCoverage",
        "ce:GetSavingsPlansPurchaseRecommendation",
        "ce:GetSavingsPlansUtilization",
        "ce:GetSavingsPlansUtilizationDetails",
        "ce:GetTags",
        "ce:GetUsageForecast",
        "ce:ListCommitmentPurchaseAnalyses",
        "ce:ListCostAllocationTagBackfillHistory",
        "ce:ListCostAllocationTags",
        "ce:ListCostCategoryDefinitions",
        "ce:ListCostCategoryResourceAssociations",
        "ce:ListSavingsPlansPurchaseRecommendationGeneration",
        "ce:ListTagsForResource",
        "ce:StartCommitmentPurchaseAnalysis",
        "ce:StartSavingsPlansPurchaseRecommendationGeneration"
      ],
      "Resource": "*"
    },
    {
      "Sid": "CostAndUsageReportReadAccess",
      "Effect": "Allow",
      "Action": [
        "bcm-data-exports:GetExport",
        "bcm-data-exports:ListExports",
        "cur:DescribeReportDefinitions"
      ],
      "Resource": "*"
    },
    {
      "Sid": "BillingReadAccess",
      "Effect": "Allow",
      "Action": [
        "billing:GetBillingData",
        "billing:GetBillingDetails",
        "billing:GetBillingNotifications",
        "billing:GetBillingPreferences",
        "billing:GetBillingView",
        "billing:GetContractInformation",
        "billing:GetCreditAllocationHistory",
        "billing:GetCredits",
        "billing:GetEnterpriseSupportChargeSummary",
        "billing:GetEnterpriseSupportContractDetails",
        "billing:GetIAMAccessPreference",
        "billing:GetResourcePolicy",
        "billing:GetSellerOfRecord",
        "billing:ListBillingViews",
        "billing:ListEnterpriseSupportLinkedAccountCharges",
        "billing:ListSourceViewsForBillingView"
      ],
      "Resource": "*"
    },
    {
      "Sid": "BillingConductorReadAccess",
      "Effect": "Allow",
      "Action": [
        "billingconductor:GetBillingGroupCostReport",
        "billingconductor:ListAccountAssociations",
        "billingconductor:ListBillingGroupCostReports",
        "billingconductor:ListBillingGroups",
        "billingconductor:ListCustomLineItemVersions",
        "billingconductor:ListCustomLineItems",
        "billingconductor:ListPricingPlans",
        "billingconductor:ListPricingPlansAssociatedWithPricingRule",
        "billingconductor:ListPricingRules",
        "billingconductor:ListPricingRulesAssociatedToPricingPlan",
        "billingconductor:ListResourcesAssociatedToCustomLineItem",
        "billingconductor:ListTagsForResource"
      ],
      "Resource": "*"
    },
    {
      "Sid": "BudgetsReadAccess",
      "Effect": "Allow",
      "Action": [
        "budgets:DescribeBudgetAction",
        "budgets:DescribeBudgetActionHistories",
        "budgets:DescribeBudgetActionsForAccount",
        "budgets:DescribeBudgetActionsForBudget",
        "budgets:ListTagsForResource",
        "budgets:ViewBudget"
      ],
      "Resource": "*"
    },
    {
      "Sid": "InvoicingReadAccess",
      "Effect": "Allow",
      "Action": [
        "invoicing:BatchGetInvoiceProfile",
        "invoicing:GetInvoiceCorrection",
        "invoicing:GetInvoiceEmailDeliveryPreferences",
        "invoicing:GetInvoicePDF",
        "invoicing:GetInvoiceUnit",
        "invoicing:GetProcurementPortalPreference",
        "invoicing:ListInvoiceCorrections",
        "invoicing:ListInvoiceSummaries",
        "invoicing:ListInvoiceUnits",
        "invoicing:ListProcurementPortalPreferences",
        "invoicing:ListProcurementPortalSuppliers",
        "invoicing:ListProcurementPortals",
        "invoicing:ListTagsForResource"
      ],
      "Resource": "*"
    },
    {
      "Sid": "PurchaseOrderReadAccess",
      "Effect": "Allow",
      "Action": [
        "purchase-orders:GetPurchaseOrder",
        "purchase-orders:ListPurchaseOrderInvoices",
        "purchase-orders:ListPurchaseOrders",
        "purchase-orders:ListTagsForResource",
        "purchase-orders:ViewPurchaseOrders"
      ],
      "Resource": "*"
    },
    {
      "Sid": "FreeTierReadAccess",
      "Effect": "Allow",
      "Action": [
        "freetier:GetAccountActivity",
        "freetier:GetAccountPlanState",
        "freetier:GetFreeTierAlertPreference",
        "freetier:GetFreeTierUsage",
        "freetier:ListAccountActivities"
      ],
      "Resource": "*"
    },
    {
      "Sid": "CreditProgramReadAccess",
      "Effect": "Allow",
      "Action": [
        "mapcredits:ListAssociatedPrograms",
        "mapcredits:ListQuarterCredits",
        "mapcredits:ListQuarterSpend"
      ],
      "Resource": "*"
    },
    {
      "Sid": "PricingReadAccess",
      "Effect": "Allow",
      "Action": [
        "pricing:DescribeServices",
        "pricing:GetAttributeValues",
        "pricing:GetProducts"
      ],
      "Resource": "*"
    },
    {
      "Sid": "PricingCalculatorReadAccess",
      "Effect": "Allow",
      "Action": [
        "bcm-pricing-calculator:GetPreferences",
        "bcm-pricing-calculator:GetWorkloadEstimate",
        "bcm-pricing-calculator:ListWorkloadEstimateUsage",
        "bcm-pricing-calculator:ListWorkloadEstimates"
      ],
      "Resource": "*"
    },
    {
      "Sid": "OrganizationStructureReadAccess",
      "Effect": "Allow",
      "Action": [
        "account:GetRegionOptStatus",
        "account:ListRegions",
        "consolidatedbilling:GetAccountBillingRole",
        "consolidatedbilling:ListLinkedAccounts",
        "organizations:DescribeAccount",
        "organizations:DescribeOrganization",
        "organizations:DescribeOrganizationalUnit",
        "organizations:ListAWSServiceAccessForOrganization",
        "organizations:ListAccounts",
        "organizations:ListChildren",
        "organizations:ListOrganizationalUnitsForParent",
        "organizations:ListParents",
        "organizations:ListRoots"
      ],
      "Resource": "*"
    },
    {
      "Sid": "AwsOrgsScopedAccess",
      "Effect": "Allow",
      "Action": [
        "organizations:ListDelegatedAdministrators"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "organizations:ServicePrincipal": [
            "finops-agent.amazonaws.com"
          ]
        }
      }
    },
    {
      "Sid": "CostOptimizationHubReadAccess",
      "Effect": "Allow",
      "Action": [
        "cost-optimization-hub:GetPreferences",
        "cost-optimization-hub:GetRecommendation",
        "cost-optimization-hub:ListEfficiencyMetrics",
        "cost-optimization-hub:ListEnrollmentStatuses",
        "cost-optimization-hub:ListRecommendationSummaries",
        "cost-optimization-hub:ListRecommendations"
      ],
      "Resource": "*"
    },
    {
      "Sid": "ComputeOptimizerReadAccess",
      "Effect": "Allow",
      "Action": [
        "compute-optimizer:DescribeRecommendationExportJobs",
        "compute-optimizer:GetAutoScalingGroupRecommendations",
        "compute-optimizer:GetEBSVolumeRecommendations",
        "compute-optimizer:GetEC2InstanceRecommendations",
        "compute-optimizer:GetEC2RecommendationProjectedMetrics",
        "compute-optimizer:GetECSServiceRecommendationProjectedMetrics",
        "compute-optimizer:GetECSServiceRecommendations",
        "compute-optimizer:GetEffectiveRecommendationPreferences",
        "compute-optimizer:GetEnrollmentStatus",
        "compute-optimizer:GetEnrollmentStatusesForOrganization",
        "compute-optimizer:GetIdleRecommendations",
        "compute-optimizer:GetLambdaFunctionRecommendations",
        "compute-optimizer:GetLicenseRecommendations",
        "compute-optimizer:GetRDSDatabaseRecommendationProjectedMetrics",
        "compute-optimizer:GetRDSDatabaseRecommendations",
        "compute-optimizer:GetRecommendationPreferences",
        "compute-optimizer:GetRecommendationSummaries"
      ],
      "Resource": "*"
    },
    {
      "Sid": "CostOptimizationAutomationReadAccess",
      "Effect": "Allow",
      "Action": [
        "aco-automation:GetAutomationEvent",
        "aco-automation:GetAutomationRule",
        "aco-automation:GetEnrollmentConfiguration",
        "aco-automation:ListAccounts",
        "aco-automation:ListAutomationEventSteps",
        "aco-automation:ListAutomationEventSummaries",
        "aco-automation:ListAutomationEvents",
        "aco-automation:ListAutomationRulePreview",
        "aco-automation:ListAutomationRulePreviewSummaries",
        "aco-automation:ListAutomationRules",
        "aco-automation:ListRecommendedActionSummaries",
        "aco-automation:ListRecommendedActions",
        "aco-automation:ListTagsForResource"
      ],
      "Resource": "*"
    },
    {
      "Sid": "SavingsPlansReadAccess",
      "Effect": "Allow",
      "Action": [
        "savingsplans:DescribeSavingsPlanRates",
        "savingsplans:DescribeSavingsPlans",
        "savingsplans:DescribeSavingsPlansOfferingRates",
        "savingsplans:DescribeSavingsPlansOfferings",
        "savingsplans:ListTagsForResource"
      ],
      "Resource": "*"
    },
    {
      "Sid": "ComputeResourceReadAccess",
      "Effect": "Allow",
      "Action": [
        "application-autoscaling:DescribeScalableTargets",
        "application-autoscaling:DescribeScalingPolicies",
        "autoscaling:DescribeAutoScalingGroups",
        "autoscaling:DescribeAutoScalingInstances",
        "ec2:DescribeAddresses",
        "ec2:DescribeInstanceTypes",
        "ec2:DescribeInstances",
        "ec2:DescribeNatGateways",
        "ec2:DescribeReservedInstances",
        "ec2:DescribeSnapshots",
        "ec2:DescribeVolumes",
        "ec2:DescribeVpcEndpoints"
      ],
      "Resource": "*"
    },
    {
      "Sid": "LambdaResourceReadAccess",
      "Effect": "Allow",
      "Action": [
        "lambda:GetFunctionConfiguration",
        "lambda:ListFunctions",
        "lambda:ListProvisionedConcurrencyConfigs"
      ],
      "Resource": "*"
    },
    {
      "Sid": "ContainerResourceReadAccess",
      "Effect": "Allow",
      "Action": [
        "ecs:ListClusters",
        "ecs:ListServices"
      ],
      "Resource": "*"
    },
    {
      "Sid": "DatabaseResourceReadAccess",
      "Effect": "Allow",
      "Action": [
        "dynamodb:DescribeContinuousBackups",
        "dynamodb:DescribeTable",
        "dynamodb:ListTables",
        "elasticache:DescribeCacheClusters",
        "elasticache:DescribeReplicationGroups",
        "elasticache:DescribeReservedCacheNodes",
        "elasticache:DescribeSnapshots",
        "memorydb:DescribeClusters",
        "memorydb:DescribeSnapshots",
        "rds:DescribeDBClusterSnapshots",
        "rds:DescribeDBClusters",
        "rds:DescribeDBEngineVersions",
        "rds:DescribeDBInstances",
        "rds:DescribeDBSnapshots",
        "rds:DescribeReservedDBInstances",
        "redshift:DescribeClusterSnapshots",
        "redshift:DescribeClusters",
        "redshift:DescribeReservedNodes"
      ],
      "Resource": "*"
    },
    {
      "Sid": "StorageResourceReadAccess",
      "Effect": "Allow",
      "Action": [
        "s3:GetBucketLocation",
        "s3:GetBucketVersioning",
        "s3:GetIntelligentTieringConfiguration",
        "s3:GetInventoryConfiguration",
        "s3:GetLifecycleConfiguration",
        "s3:GetReplicationConfiguration",
        "s3:GetStorageLensConfiguration",
        "s3:ListAllMyBuckets"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceAccount": "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid": "MachineLearningResourceReadAccess",
      "Effect": "Allow",
      "Action": [
        "sagemaker:DescribeEndpoint",
        "sagemaker:DescribeEndpointConfig",
        "sagemaker:DescribeNotebookInstance",
        "sagemaker:ListApps",
        "sagemaker:ListDomains",
        "sagemaker:ListEndpointConfigs",
        "sagemaker:ListEndpoints",
        "sagemaker:ListNotebookInstances"
      ],
      "Resource": "*"
    },
    {
      "Sid": "WorkspacesReadAccess",
      "Effect": "Allow",
      "Action": [
        "workspaces:DescribeWorkspaces",
        "workspaces:DescribeWorkspacesConnectionStatus"
      ],
      "Resource": "*"
    },
    {
      "Sid": "ResourceDiscoveryReadAccess",
      "Effect": "Allow",
      "Action": [
        "ram:GetResourceShares",
        "resource-explorer-2:GetIndex",
        "resource-explorer-2:ListIndexes",
        "resource-explorer-2:Search",
        "tag:GetResources"
      ],
      "Resource": "*"
    },
    {
      "Sid": "UtilizationMetricsReadAccess",
      "Effect": "Allow",
      "Action": [
        "cloudwatch:GetMetricData",
        "cloudwatch:GetMetricStatistics",
        "cloudwatch:ListMetrics"
      ],
      "Resource": "*"
    },
    {
      "Sid": "LogConfigurationReadAccess",
      "Effect": "Allow",
      "Action": [
        "logs:DescribeLogGroups",
        "logs:DescribeSubscriptionFilters"
      ],
      "Resource": "*"
    },
    {
      "Sid": "CloudTrailConfigurationReadAccess",
      "Effect": "Allow",
      "Action": [
        "cloudtrail:DescribeTrails",
        "cloudtrail:GetEventSelectors",
        "cloudtrail:GetTrailStatus",
        "cloudtrail:LookupEvents"
      ],
      "Resource": "*"
    },
    {
      "Sid": "HealthEventReadAccess",
      "Effect": "Allow",
      "Action": [
        "health:DescribeEvents"
      ],
      "Resource": "*"
    },
    {
      "Sid": "EventBridgeManagedRuleManagementWritePermissions",
      "Effect": "Allow",
      "Action": [
        "events:DeleteRule",
        "events:DisableRule",
        "events:EnableRule",
        "events:PutRule",
        "events:PutTargets",
        "events:RemoveTargets"
      ],
      "Resource": "arn:aws:events:*:*:rule/*",
      "Condition": {
        "StringEquals": {
          "events:ManagedBy": "finops-agent.amazonaws.com"
        }
      }
    },
    {
      "Sid": "BCMDataHubQueryAccess",
      "Effect": "Allow",
      "Action": [
        "bcm-data-hub:ListDatasets",
        "bcm-data-hub:GetDataset",
        "bcm-data-hub:GetDatasetSchema",
        "bcm-data-hub:StartQueryExecution",
        "bcm-data-hub:GetQueryExecution",
        "bcm-data-hub:GetQueryExecutionResults",
        "bcm-data-hub:CancelQueryExecution",
        "bcm-data-hub:ListQueryExecutions"
      ],
      "Resource": "*"
    },
    {
      "Sid": "EventBridgeManagedRuleManagementReadPermissions",
      "Effect": "Allow",
      "Action": [
        "events:DescribeRule",
        "events:ListTargetsByRule"
      ],
      "Resource": "arn:aws:events:*:*:rule/*"
    }
  ]
}
```

For changes to this policy, see [AWS FinOps Agent updates to AWS managed policies](security-iam-awsmanpol.md#security-iam-awsmanpol-updates).

You must configure permissions to allow your users, groups, or roles to create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#service-linked-role-permissions) in the *IAM User Guide*.

## Creating a service-linked role for AWS FinOps Agent
<a name="creating-a-service-linked-role"></a>

You don't need to manually create the `AWSServiceRoleForFinOpsAgent` role. AWS FinOps Agent creates the service-linked role in the management account and in your member accounts when you enable organization-wide access from the management account. Enabling organization-wide access turns on trusted access for AWS FinOps Agent and provisions the role so the agent can read data across the accounts in your organization.

If you delete this service-linked role and then need to create it again, you can use the same process to recreate the role in your account. When you enable organization-wide access again, AWS FinOps Agent creates the service-linked role for you again.

## Editing a service-linked role for AWS FinOps Agent
<a name="editing-a-service-linked-role"></a>

AWS FinOps Agent does not allow you to edit the `AWSServiceRoleForFinOpsAgent` service-linked role. After you create a service-linked role, you cannot change the name of the role because various entities might reference the role. However, you can edit the description of the role using IAM. For more information, see [Editing a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#edit-service-linked-role) in the *IAM User Guide*.

## Deleting a service-linked role for AWS FinOps Agent
<a name="deleting-a-service-linked-role"></a>

If you no longer need to use AWS FinOps Agent for organization-wide access, we recommend that you delete the `AWSServiceRoleForFinOpsAgent` role. That way you don't have an unused entity that is not actively monitored or maintained. Before you can delete the role, you must disable organization-wide access for AWS FinOps Agent so that the role is no longer in use in your member accounts.

You can use the IAM console, the IAM CLI, or the IAM API to delete the service-linked role. For more information, see [Deleting a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#delete-service-linked-role) in the *IAM User Guide*.

## Supported Regions for AWS FinOps Agent service-linked roles
<a name="service-linked-role-supported-regions"></a>

AWS FinOps Agent supports using service-linked roles in the AWS Regions where the service is available. AWS FinOps Agent organization-wide access is available in the US East (N. Virginia) (`us-east-1`) Region.