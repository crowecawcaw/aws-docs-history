

AWS FinOps Agent is in preview release and is subject to change.

# AWS FinOps Agent IAM setup guide

When you create an agent, the creation wizard can create the required IAM roles and attach the policies for you. Most customers do not need to configure IAM manually. For the standard flow, see [Creating an agent](creating-an-agent.md).

Use this topic if your IAM administrator manages permissions centrally, or if you want to author the roles and policies yourself. For account-scoped agents, this topic covers 4 IAM policies and 2 IAM roles, the relationships between them, and how to enable the AWS services that the agent depends on. Organization-wide agents use a service-linked role for data access and still need an operator role. For that setup, see [Setting up organization-wide access and a delegated administrator](setting-up-organization-access.md).

## Step 1: Create IAM policies
<a name="setting-up-step-1"></a>

Create the following 4 IAM policies. The policy names shown are samples and can be customized.

### Policy 1: Admin setup policy
<a name="setting-up-administrator-policy"></a>

Sample name: `FinOpsAgentSetupPolicy`

This policy grants the administrator permissions to create and manage AWS FinOps Agent instances, configure third-party integrations, and generate login sessions for web application users. Attach this policy directly to the administrator's IAM user or role.

```json
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "FinOpsAgentAdminSetup",
      "Effect": "Allow",
      "Action": [
        "finops-agent:CreateAgentSpace",
        "finops-agent:GetAgentSpace",
        "finops-agent:ListAgentSpaces",
        "finops-agent:UpdateAgentSpace",
        "finops-agent:DeleteAgentSpace",
        "finops-agent:ListAutomations",
        "finops-agent:ListDocuments",
        "finops-agent:CreateConnection",
        "finops-agent:GetConnection",
        "finops-agent:ListConnections",
        "finops-agent:UpdateConnection",
        "finops-agent:DeleteConnection",
        "finops-agent:CreateIntegration",
        "finops-agent:GetIntegration",
        "finops-agent:ListIntegrations",
        "finops-agent:DeleteIntegration",
        "finops-agent:CreateOneTimeLoginSession"
      ],
      "Resource": "*"
    },
    {
      "Sid": "IamReadForRolePicker",
      "Effect": "Allow",
      "Action": ["iam:GetRole", "iam:ListRoles"],
      "Resource": "*"
    },
    {
      "Sid": "CreateFinOpsServiceRolesOnly",
      "Effect": "Allow",
      "Action": "iam:CreateRole",
      "Resource": "arn:aws:iam::*:role/service-role/*"
    },
    {
      "Sid": "AttachOnlyFinOpsManagedPolicies",
      "Effect": "Allow",
      "Action": "iam:AttachRolePolicy",
      "Resource": "arn:aws:iam::*:role/service-role/*",
      "Condition": {
        "ArnEquals": {
          "iam:PolicyARN": [
            "arn:aws:iam::aws:policy/FinOpsAgentAgentPolicy",
            "arn:aws:iam::aws:policy/FinOpsAgentOperatorPolicy"
          ]
        }
      }
    },
    {
      "Sid": "PassFinOpsRolesToService",
      "Effect": "Allow",
      "Action": "iam:PassRole",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "iam:PassedToService": "finops-agent.amazonaws.com"
        },
        "ArnLike": {
          "iam:AssociatedResourceArn": "arn:aws:finops-agent:*:*:agentspace/*"
        }
      }
    }
  ]
}
```

### Policy 2: Agent permissions policy
<a name="setting-up-agent-policy"></a>

Sample name: `FinOpsAgentAgentPolicy`

This policy defines what AWS services and data an account-scoped agent can read. The agent uses these permissions to query cost and billing data, including credits, budgets, Free Tier usage, invoices, and billing views, retrieve optimization recommendations, look up infrastructure details, and correlate cost changes with operational metrics. Attach this policy to the agent IAM role in [Step 2](#setting-up-step-2).

If you maintain a customer managed policy, include the required permissions for each data source you use and keep the policy up to date. Organization-wide agents use the service-linked role described in [Setting up organization-wide access and a delegated administrator](setting-up-organization-access.md).

You have 2 options for creating this policy:
+ **Option 1: Use the AWS managed policy during agent creation (recommended).** The agent creation wizard creates an agent role and attaches `FinOpsAgentAgentPolicy` automatically. You can skip manual policy creation and let the wizard handle it.
+ **Option 2: Author the policy manually.** Create a customer managed policy with the JSON below if your IAM administrator manages permissions centrally. The example includes permissions for the workflows described in this guide. Attach it to the agent IAM role in [Step 2](#setting-up-step-2). To review the current AWS managed policy document, see [FinOpsAgentAgentPolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-FinOpsAgentAgentPolicy).

```json
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "FinOpsAgentDataAccess",
      "Effect": "Allow",
      "Action": [
        "ce:GetCostAndUsage",
        "ce:GetCostAndUsageWithResources",
        "ce:GetCostForecast",
        "ce:GetUsageForecast",
        "ce:GetDimensionValues",
        "ce:GetTags",
        "ce:GetCostCategories",
        "ce:GetCostAndUsageComparisons",
        "ce:GetCostComparisonDrivers",
        "ce:GetSavingsPlansCoverage",
        "ce:GetSavingsPlansUtilization",
        "ce:GetSavingsPlansUtilizationDetails",
        "ce:GetSavingsPlansPurchaseRecommendation",
        "ce:GetReservationCoverage",
        "ce:GetReservationUtilization",
        "ce:GetReservationPurchaseRecommendation",
        "ce:GetAnomalies",
        "ce:GetAnomalyMonitors",
        "ce:ListCostAllocationTags",
        "ce:ListCostAllocationTagBackfillHistory",
        "ce:DescribeCostCategoryDefinition",
        "ce:ListCostCategoryDefinitions",
        "ce:StartCommitmentPurchaseAnalysis",
        "ce:ListCommitmentPurchaseAnalyses",
        "ce:GetCommitmentPurchaseAnalysis",
        "ce:StartSavingsPlansPurchaseRecommendationGeneration",
        "ce:ListSavingsPlansPurchaseRecommendationGeneration",
        "ce:GetSavingsPlanPurchaseRecommendationDetails",
        "budgets:DescribeBudgetActionsForAccount",
        "budgets:DescribeBudgetActionsForBudget",
        "budgets:ViewBudget",
        "cost-optimization-hub:GetRecommendation",
        "cost-optimization-hub:ListRecommendations",
        "cost-optimization-hub:ListRecommendationSummaries",
        "compute-optimizer:DescribeRecommendationExportJobs",
        "compute-optimizer:GetEnrollmentStatus",
        "compute-optimizer:GetEnrollmentStatusesForOrganization",
        "compute-optimizer:GetRecommendationSummaries",
        "compute-optimizer:GetEC2InstanceRecommendations",
        "compute-optimizer:GetEC2RecommendationProjectedMetrics",
        "compute-optimizer:GetAutoScalingGroupRecommendations",
        "compute-optimizer:GetEBSVolumeRecommendations",
        "compute-optimizer:GetLambdaFunctionRecommendations",
        "compute-optimizer:GetRecommendationPreferences",
        "compute-optimizer:GetEffectiveRecommendationPreferences",
        "compute-optimizer:GetECSServiceRecommendations",
        "compute-optimizer:GetECSServiceRecommendationProjectedMetrics",
        "compute-optimizer:GetLicenseRecommendations",
        "compute-optimizer:GetRDSDatabaseRecommendations",
        "compute-optimizer:GetRDSDatabaseRecommendationProjectedMetrics",
        "compute-optimizer:GetIdleRecommendations",
        "ec2:DescribeInstances",
        "ec2:DescribeVolumes",
        "ecs:ListServices",
        "ecs:ListClusters",
        "autoscaling:DescribeAutoScalingGroups",
        "autoscaling:DescribeAutoScalingInstances",
        "lambda:ListFunctions",
        "lambda:ListProvisionedConcurrencyConfigs",
        "organizations:ListAccounts",
        "organizations:DescribeOrganization",
        "organizations:DescribeAccount",
        "rds:DescribeDBInstances",
        "rds:DescribeDBClusters",
        "rds:DescribeDBMajorEngineVersions",
        "pricing:DescribeServices",
        "pricing:GetAttributeValues",
        "pricing:GetProducts",
        "freetier:GetFreeTierUsage",
        "bcm-pricing-calculator:GetPreferences",
        "bcm-pricing-calculator:GetWorkloadEstimate",
        "bcm-pricing-calculator:ListWorkloadEstimateUsage",
        "bcm-pricing-calculator:ListWorkloadEstimates",
        "cloudtrail:LookupEvents",
        "cloudtrail:DescribeTrails",
        "cloudtrail:GetTrailStatus",
        "cloudtrail:GetEventSelectors",
        "cloudwatch:GetMetricData",
        "cloudwatch:GetMetricStatistics",
        "cloudwatch:ListMetrics",
        "logs:StartQuery",
        "logs:GetQueryResults",
        "billing:GetBillingView",
        "billing:GetEnterpriseSupportChargeSummary",
        "billing:GetEnterpriseSupportContractDetails",
        "billing:ListBillingViews",
        "billing:ListEnterpriseSupportLinkedAccountCharges",
        "billing:ListSourceViewsForBillingView",
        "billing:GetResourcePolicy",
        "billingconductor:ListBillingGroups",
        "billingconductor:ListAccountAssociations",
        "billingconductor:ListBillingGroupCostReports",
        "billingconductor:GetBillingGroupCostReport",
        "billingconductor:ListCustomLineItems",
        "billingconductor:ListCustomLineItemVersions",
        "billingconductor:ListResourcesAssociatedToCustomLineItem",
        "billingconductor:ListPricingRules",
        "billingconductor:ListPricingPlans",
        "billingconductor:ListPricingRulesAssociatedToPricingPlan",
        "billingconductor:ListPricingPlansAssociatedWithPricingRule",
        "invoicing:ListInvoiceSummaries",
        "invoicing:ListInvoiceUnits",
        "invoicing:GetInvoiceUnit",
        "invoicing:BatchGetInvoiceProfile",
        "invoicing:ListProcurementPortalPreferences",
        "invoicing:GetProcurementPortalPreference",
        "aco-automation:GetAutomationEvent",
        "aco-automation:GetAutomationRule",
        "aco-automation:GetEnrollmentConfiguration",
        "aco-automation:ListAccounts",
        "aco-automation:ListAutomationEvents",
        "aco-automation:ListAutomationEventSteps",
        "aco-automation:ListAutomationEventSummaries",
        "aco-automation:ListAutomationRules",
        "aco-automation:ListRecommendedActions",
        "aco-automation:ListRecommendedActionSummaries",
        "aco-automation:ListAutomationRulePreview",
        "aco-automation:ListAutomationRulePreviewSummaries",
        "aco-automation:ListTagsForResource",
        "billing:GetCredits",
        "billing:GetCreditAllocationHistory",
        "health:DescribeEvents",
        "savingsplans:DescribeSavingsPlans",
        "savingsplans:DescribeSavingsPlanRates",
        "savingsplans:DescribeSavingsPlansOfferings",
        "savingsplans:DescribeSavingsPlansOfferingRates",
        "savingsplans:ListTagsForResource",
        "cost-optimization-hub:ListEfficiencyMetrics",
        "cost-optimization-hub:ListEnrollmentStatuses",
        "cost-optimization-hub:GetPreferences",
        "billing:GetBillingPreferences",
        "billing:ListBillingViewSegments",
        "ce:ListCostCategoryResourceAssociations",
        "ce:ListTagsForResource",
        "bcm-data-exports:GetExport",
        "bcm-data-exports:ListExports",
        "cur:DescribeReportDefinitions",
        "billing:GetBillingData",
        "billing:GetBillingDetails",
        "billing:GetBillingNotifications",
        "billing:GetContractInformation",
        "billing:GetIAMAccessPreference",
        "billing:GetSellerOfRecord",
        "billingconductor:ListTagsForResource",
        "budgets:DescribeBudgetAction",
        "budgets:DescribeBudgetActionHistories",
        "budgets:ListTagsForResource",
        "invoicing:GetInvoiceCorrection",
        "invoicing:GetInvoiceEmailDeliveryPreferences",
        "invoicing:GetInvoicePDF",
        "invoicing:ListInvoiceCorrections",
        "invoicing:ListProcurementPortalSuppliers",
        "invoicing:ListProcurementPortals",
        "invoicing:ListTagsForResource",
        "purchase-orders:GetPurchaseOrder",
        "purchase-orders:ListPurchaseOrderInvoices",
        "purchase-orders:ListPurchaseOrders",
        "purchase-orders:ListTagsForResource",
        "purchase-orders:ViewPurchaseOrders",
        "freetier:GetAccountActivity",
        "freetier:GetAccountPlanState",
        "freetier:GetFreeTierAlertPreference",
        "freetier:ListAccountActivities",
        "mapcredits:ListAssociatedPrograms",
        "mapcredits:ListQuarterCredits",
        "mapcredits:ListQuarterSpend",
        "account:GetRegionOptStatus",
        "account:ListRegions",
        "consolidatedbilling:GetAccountBillingRole",
        "consolidatedbilling:ListLinkedAccounts",
        "organizations:DescribeOrganizationalUnit",
        "organizations:ListAWSServiceAccessForOrganization",
        "organizations:ListChildren",
        "organizations:ListOrganizationalUnitsForParent",
        "organizations:ListParents",
        "organizations:ListRoots",
        "application-autoscaling:DescribeScalableTargets",
        "application-autoscaling:DescribeScalingPolicies",
        "ec2:DescribeAddresses",
        "ec2:DescribeInstanceTypes",
        "ec2:DescribeNatGateways",
        "ec2:DescribeReservedInstances",
        "ec2:DescribeSnapshots",
        "ec2:DescribeVpcEndpoints",
        "lambda:GetFunctionConfiguration",
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
        "rds:DescribeDBEngineVersions",
        "rds:DescribeDBSnapshots",
        "rds:DescribeReservedDBInstances",
        "redshift:DescribeClusterSnapshots",
        "redshift:DescribeClusters",
        "redshift:DescribeReservedNodes",
        "sagemaker:DescribeEndpoint",
        "sagemaker:DescribeEndpointConfig",
        "sagemaker:DescribeNotebookInstance",
        "sagemaker:ListApps",
        "sagemaker:ListDomains",
        "sagemaker:ListEndpointConfigs",
        "sagemaker:ListEndpoints",
        "sagemaker:ListNotebookInstances",
        "workspaces:DescribeWorkspaces",
        "workspaces:DescribeWorkspacesConnectionStatus",
        "ram:GetResourceShares",
        "resource-explorer-2:GetIndex",
        "resource-explorer-2:ListIndexes",
        "resource-explorer-2:Search",
        "tag:GetResources",
        "logs:DescribeLogGroups",
        "logs:DescribeSubscriptionFilters"
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
      "Sid": "EventBridgeManagedRuleManagementWritePermissions",
      "Effect": "Allow",
      "Action": [
        "events:PutRule",
        "events:PutTargets",
        "events:DeleteRule",
        "events:RemoveTargets",
        "events:EnableRule",
        "events:DisableRule"
      ],
      "Resource": "arn:aws:events:*:*:rule/*",
      "Condition": {
        "StringEquals": {
          "events:ManagedBy": "finops-agent.amazonaws.com",
          "aws:ResourceAccount": "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid": "EventBridgeManagedRuleManagementReadPermissions",
      "Effect": "Allow",
      "Action": [
        "events:DescribeRule",
        "events:ListTargetsByRule"
      ],
      "Resource": "arn:aws:events:*:*:rule/*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceAccount": "${aws:PrincipalAccount}"
        }
      }
    }
  ]
}
```

AWS FinOps Agent uses Amazon EventBridge actions to manage event-triggered automations for cost anomaly investigation. Without these permissions, the agent cannot create event-triggered automations for cost anomaly investigation. The `events:ManagedBy` condition restricts the EventBridge write actions to rules that the agent created on your behalf, so rules you create directly are not affected. The `aws:ResourceAccount` condition limits these EventBridge permissions to rules in your own account.

The CloudTrail actions support cost anomaly investigation. The agent uses `cloudtrail:LookupEvents` to find the API activity behind a cost change.

You can remove actions you do not need. For example, if you remove `cloudtrail:LookupEvents`, the agent continues to work for cost inquiry, reporting, and recommendations, and it still detects and analyzes cost anomalies, but it can no longer correlate a cost spike with the CloudTrail records that explain what changed.

### Policy 3: Operator permissions policy
<a name="setting-up-operator-policy"></a>

Sample name: `FinOpsAgentOperatorPolicy`

This policy defines what actions the web application can perform with the AWS FinOps Agent service. It covers managing conversations, tasks, automations, context files, and reports. This policy will be attached to the operator IAM role in [Step 2](#setting-up-step-2).

You have 2 options for creating this policy:
+ **Option 1: Auto-create during agent creation (recommended).** The agent creation wizard creates the policy as an AWS managed policy and attaches it to the operator role automatically. You can skip this section and let the wizard handle it.
+ **Option 2: Author the policy manually.** Create the policy with the JSON below if your IAM administrator manages all permissions centrally. You will need to attach this policy to the operator IAM role in [Step 2](#setting-up-step-2) manually.

```json
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "FinOpsAgentOperatorAccess",
      "Effect": "Allow",
      "Action": [
        "finops-agent:CreateConversation",
        "finops-agent:ListConversations",
        "finops-agent:CreateTurn",
        "finops-agent:GetTurn",
        "finops-agent:ListTurns",
        "finops-agent:CancelTurn",
        "finops-agent:AcceptAgentRequest",
        "finops-agent:RejectAgentRequest",
        "finops-agent:GetAgentRequest",
        "finops-agent:CreateTask",
        "finops-agent:GetTask",
        "finops-agent:ListTasks",
        "finops-agent:CancelTask",
        "finops-agent:CreateAutomation",
        "finops-agent:GetAutomation",
        "finops-agent:ListAutomations",
        "finops-agent:UpdateAutomation",
        "finops-agent:DeleteAutomation",
        "finops-agent:CreateDocument",
        "finops-agent:GetDocumentContent",
        "finops-agent:GetDocumentMetadata",
        "finops-agent:ListDocuments",
        "finops-agent:UpdateDocument",
        "finops-agent:DeleteDocument",
        "finops-agent:RestoreDocument",
        "finops-agent:DeleteArtifact",
        "finops-agent:GetArtifactContent",
        "finops-agent:GetArtifactMetadata",
        "finops-agent:ListArtifacts",
        "finops-agent:ListRecords",
        "finops-agent:SendFeedback"
      ],
      "Resource": "*"
    }
  ]
}
```

### Policy 4: Web app user policy
<a name="setting-up-end-user-policy"></a>

Sample name: `FinOpsAgentWebAppPolicy`

This policy grants your team members permissions to find the agent in the AWS console and create a login session for the web application. Attach this policy directly to each team member's IAM user or role.

This policy does not allow users to create or delete agents. To allow a user to create or delete agents, attach [Policy 1 (`FinOpsAgentSetupPolicy`)](#setting-up-administrator-policy) to that user or role.

The Cost Explorer read actions in this policy are optional and not required to access the web application. They enable users to cross-validate the agent's findings by viewing cost data directly in Cost Explorer within the same console session. If your team does not need this, you can remove the `ce:*` actions from the policy.

```json
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "FinOpsAgentUsers",
      "Effect": "Allow",
      "Action": [
        "finops-agent:GetAgentSpace",
        "finops-agent:ListAgentSpaces",
        "finops-agent:ListConnections",
        "finops-agent:GetConnection",
        "finops-agent:ListIntegrations",
        "finops-agent:CreateOneTimeLoginSession",
        "iam:GetRole",
        "ce:GetCostAndUsage",
        "ce:GetCostAndUsageWithResources",
        "ce:GetCostForecast",
        "ce:GetUsageForecast",
        "ce:GetDimensionValues",
        "ce:GetTags",
        "ce:GetCostCategories",
        "ce:GetCostAndUsageComparisons",
        "ce:GetCostComparisonDrivers",
        "ce:GetSavingsPlansCoverage",
        "ce:GetSavingsPlansUtilization",
        "ce:GetSavingsPlansUtilizationDetails",
        "ce:GetSavingsPlansPurchaseRecommendation",
        "ce:GetReservationCoverage",
        "ce:GetReservationUtilization",
        "ce:GetReservationPurchaseRecommendation"
      ],
      "Resource": "*"
    }
  ]
}
```

## Step 2: Create 2 IAM roles
<a name="setting-up-step-2"></a>

AWS FinOps Agent requires 2 IAM roles. Each role serves a different purpose and is assumed by the AWS FinOps Agent service to perform different operations.

The **agent role** (sample name: `FinOpsAgentRole`) is the role the AWS FinOps Agent service assumes to query your AWS billing data, optimization recommendations, and infrastructure metrics. When you ask the agent a question about your costs, the service uses this role to call AWS APIs like AWS Cost Explorer and AWS Compute Optimizer. Attach [Policy 2 (`FinOpsAgentAgentPolicy`)](#setting-up-agent-policy) to this role.

The **operator role** (sample name: `FinOpsAgentOperatorRole`) is the role the AWS FinOps Agent service assumes to perform web application operations. When you send a chat message, create a task, or upload a context file, the service uses this role's credentials to execute those actions. Attach [Policy 3 (`FinOpsAgentOperatorPolicy`)](#setting-up-operator-policy) to this role.

**Note**  
People using an agent act with its operator and agent roles, not their own IAM permissions.

Create 2 IAM roles using the trust policy below, then attach the corresponding permissions policy from [Step 1](#setting-up-step-1).


| IAM role (sample name) | Attach this policy from Step 1 | 
| --- | --- | 
| FinOpsAgentRole | Policy 2 (FinOpsAgentAgentPolicy) | 
| FinOpsAgentOperatorRole | Policy 3 (FinOpsAgentOperatorPolicy) | 

### Trust policy
<a name="setting-up-trust-policy"></a>

Both roles use the same trust policy. This trust policy allows the AWS FinOps Agent service account to assume the role using `sts:AssumeRole` and to stamp the calling user's identity onto the session using `sts:SetSourceIdentity`.

```json
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "finops-agent.amazonaws.com"
      },
      "Action": [
        "sts:AssumeRole",
        "sts:SetSourceIdentity"
      ],
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "{{accountId}}"
        },
        "ArnLike": {
          "aws:SourceArn": "arn:aws:finops-agent:*:{{accountId}}:agentspace/*"
        }
      }
    }
  ]
}
```

Replace `{{accountId}}` with your AWS account ID. The `agentspace/*` wildcard allows any agent in the account to assume the role. To restrict the role to a specific agent, replace the wildcard with the agent ID after you create the agent.

**Why `sts:SetSourceIdentity`?** When AWS FinOps Agent assumes one of these roles on behalf of a web application user, it sets the user's IAM unique identifier as the session's `SourceIdentity`. Every AWS CloudTrail event the agent generates while using these credentials carries that `sourceIdentity` field, so you can attribute agent-driven activity back to the individual user. Without this permission, the role assumption still succeeds, but downstream CloudTrail events do not include the `sourceIdentity` field. For details, see [How caller identity appears in CloudTrail](monitoring-overview.md#cloudtrail-caller-identity).

## Activate dependent AWS services
<a name="setting-up-service-activation"></a>

After you create the IAM policies and roles, activate the underlying AWS services that the agent uses. IAM permissions alone are not enough for the cost optimization and cost anomaly investigation features.

**AWS Compute Optimizer** (for cost optimization recommendations)  
Open the [AWS Compute Optimizer console](https://console.aws.amazon.com/compute-optimizer/) and opt in. Without opt-in, the agent cannot retrieve rightsizing or idle resource recommendations from AWS Compute Optimizer. For details, see [Getting started with AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/getting-started.html).

**AWS Cost Anomaly Detection** (for cost anomaly investigation)  
Open the [AWS Cost Anomaly Detection](https://console.aws.amazon.com/cost-management/home#/anomaly-detection) page in the console and create at least one anomaly monitor. The agent investigates anomalies that AWS Cost Anomaly Detection produces from your monitors. For details, see [Getting started with AWS Cost Anomaly Detection](https://docs.aws.amazon.com/cost-management/latest/userguide/getting-started-ad.html).

**AWS Cost Optimization Hub** (for cost optimization recommendations)  
Open [AWS Cost Optimization Hub](https://console.aws.amazon.com/cost-management/home#/cost-optimization-hub) in the console and enable it. You must opt in before the agent can retrieve AWS Cost Optimization Hub recommendations. For details, see [Getting started with AWS Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html).

**AWS CloudTrail** (for cost anomaly investigation)  
The agent uses CloudTrail Event History (through `LookupEvents`) to identify the change behind a cost spike. CloudTrail Event History is enabled by default in every AWS account at no charge. You do not need to create a trail or configure CloudTrail for the agent to investigate anomalies.