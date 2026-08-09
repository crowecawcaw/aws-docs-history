AWS FinOps Agent is in preview release and is subject to change.

# AWS FinOps Agent IAM setup guide

When you create an agent, the creation wizard can create the required IAM roles and attach the policies for you. Most customers do not need to configure IAM manually. For the standard flow, see [Creating an agent](creating-an-agent.md "creating-an-agent.md").

Use this topic if your IAM administrator manages permissions centrally, or if you want to author the roles and policies yourself. AWS FinOps Agent uses 4 IAM policies and 2 IAM roles. This topic walks through each policy, the roles that the policies attach to, and how to enable the AWS services that the agent depends on.

## Step 1: Create IAM policies

Create the following 4 IAM policies. The policy names shown are samples and can be customized.

### Policy 1: Admin setup policy

Sample name: `FinOpsAgentSetupPolicy`

This policy grants the administrator permissions to create and manage AWS FinOps Agent instances, configure third-party integrations, and generate login sessions for web application users. Attach this policy directly to the administrator's IAM user or role.

```
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

Sample name: `FinOpsAgentAgentPolicy`

This policy defines what AWS services and data the AWS FinOps Agent can read in your account. The agent uses these permissions to query billing and cost data, retrieve optimization recommendations, look up infrastructure details, and correlate cost changes with operational metrics. This policy will be attached to the agent IAM role in [Step 2](#setting-up-step-2 "#setting-up-step-2").

You have 2 options for creating this policy:

- **Option 1: Auto-create during agent creation (recommended).** The agent creation wizard creates the policy as an AWS managed policy and attaches it to the agent role automatically. You can skip this section and let the wizard handle it.
- **Option 2: Author the policy manually.** Create the policy with the JSON below if your IAM administrator manages all permissions centrally. You will need to attach this policy to the agent IAM role in [Step 2](#setting-up-step-2 "#setting-up-step-2") manually.

```
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
        "logs:GetQueryResults"
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

AWS FinOps Agent uses AWS EventBridge actions to manage event-triggered automations for cost anomaly investigation. Without these permissions, the agent cannot create event-triggered automations for cost anomaly investigation. The `events:ManagedBy` condition restricts the agent to managing only the EventBridge rules it created on your behalf, so rules you create directly are not affected. The `aws:ResourceAccount` condition limits the agent to managing rules in your own account.

The CloudTrail actions support cost anomaly investigation. The agent uses `cloudtrail:LookupEvents` to find the API activity behind a cost change.

You can remove actions you do not need. For example, if you remove `cloudtrail:LookupEvents`, the agent continues to work for cost inquiry, reporting, and recommendations, and it still detects and analyzes cost anomalies, but it can no longer correlate a cost spike with the CloudTrail records that explain what changed.

### Policy 3: Operator permissions policy

Sample name: `FinOpsAgentOperatorPolicy`

This policy defines what actions the web application can perform with the AWS FinOps Agent service. It covers managing conversations, tasks, automations, context files, and reports. This policy will be attached to the operator IAM role in [Step 2](#setting-up-step-2 "#setting-up-step-2").

You have 2 options for creating this policy:

- **Option 1: Auto-create during agent creation (recommended).** The agent creation wizard creates the policy as an AWS managed policy and attaches it to the operator role automatically. You can skip this section and let the wizard handle it.
- **Option 2: Author the policy manually.** Create the policy with the JSON below if your IAM administrator manages all permissions centrally. You will need to attach this policy to the operator IAM role in [Step 2](#setting-up-step-2 "#setting-up-step-2") manually.

```
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

Sample name: `FinOpsAgentWebAppPolicy`

This policy grants your team members permissions to find the agent in the AWS console and create a login session for the web application. Attach this policy directly to each team member's IAM user or role.

This policy does not allow users to create or delete agents. To allow a user to create or delete agents, attach [Policy 1 (FinOpsAgentSetupPolicy)](#setting-up-administrator-policy "#setting-up-administrator-policy") to that user or role.

The Cost Explorer read actions in this policy are optional and not required to access the web application. They enable users to cross-validate the agent's findings by viewing cost data directly in Cost Explorer within the same console session. If your team does not need this, you can remove the `ce:*` actions from the policy.

```
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

AWS FinOps Agent requires 2 IAM roles. Each role serves a different purpose and is assumed by the AWS FinOps Agent service to perform different operations.

The **agent role** (sample name: `FinOpsAgentRole`) is the role the AWS FinOps Agent service assumes to query your AWS billing data, optimization recommendations, and infrastructure metrics. When you ask the agent a question about your costs, the service uses this role to call AWS APIs like AWS Cost Explorer and AWS Compute Optimizer. Attach [Policy 2 (FinOpsAgentAgentPolicy)](#setting-up-agent-policy "#setting-up-agent-policy") to this role.

The **operator role** (sample name: `FinOpsAgentOperatorRole`) is the role the AWS FinOps Agent service assumes to perform web application operations. When you send a chat message, create a task, or upload a context file, the service uses this role's credentials to execute those actions. Attach [Policy 3 (FinOpsAgentOperatorPolicy)](#setting-up-operator-policy "#setting-up-operator-policy") to this role.

Create 2 IAM roles using the trust policy below, then attach the corresponding permissions policy from [Step 1](#setting-up-step-1 "#setting-up-step-1").

| IAM role (sample name)    | Attach this policy from Step 1         |
| ------------------------- | -------------------------------------- |
| `FinOpsAgentRole`         | Policy 2 (`FinOpsAgentAgentPolicy`)    |
| `FinOpsAgentOperatorRole` | Policy 3 (`FinOpsAgentOperatorPolicy`) |

### Trust policy

Both roles use the same trust policy. This trust policy allows the AWS FinOps Agent service account to assume the role using `sts:AssumeRole` and to stamp the calling user's identity onto the session using `sts:SetSourceIdentity`.

```
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

**Why `sts:SetSourceIdentity`?** When AWS FinOps Agent assumes one of these roles on behalf of a web application user, it sets the user's IAM unique identifier as the session's `SourceIdentity`. Every AWS CloudTrail event the agent generates while using these credentials carries that `sourceIdentity` field, so you can attribute agent-driven activity back to the individual user. Without this permission, the role assumption still succeeds, but downstream CloudTrail events do not include the `sourceIdentity` field. For details, see [How caller identity appears in CloudTrail](monitoring-overview.md#cloudtrail-caller-identity "monitoring-overview.md#cloudtrail-caller-identity").

## Activate dependent AWS services

After you create the IAM policies and roles, activate the underlying AWS services that the agent uses. IAM permissions alone are not enough for the cost optimization and cost anomaly investigation features.

**AWS Compute Optimizer** (for cost optimization recommendations)

Open the [AWS Compute Optimizer console](https://console.aws.amazon.com/compute-optimizer/ "https://console.aws.amazon.com/compute-optimizer/") and opt in. Without opt-in, the agent cannot retrieve rightsizing or idle resource recommendations from AWS Compute Optimizer. For details, see [Getting started with AWS Compute Optimizer](../../../compute-optimizer/latest/ug/getting-started.md "../../../compute-optimizer/latest/ug/getting-started.md").

**AWS Cost Anomaly Detection** (for cost anomaly investigation)

Open the [AWS Cost Anomaly Detection](https://console.aws.amazon.com/cost-management/home#/anomaly-detection "https://console.aws.amazon.com/cost-management/home#/anomaly-detection") page in the console and create at least one anomaly monitor. The agent investigates anomalies that AWS Cost Anomaly Detection produces from your monitors. For details, see [Getting started with AWS Cost Anomaly Detection](../../../cost-management/latest/userguide/getting-started-ad.md "../../../cost-management/latest/userguide/getting-started-ad.md").

**AWS Cost Optimization Hub** (for cost optimization recommendations)

AWS Cost Optimization Hub is enabled by default in every AWS account. No additional setup is required.

**AWS CloudTrail** (for cost anomaly investigation)

The agent uses CloudTrail Event History (through `LookupEvents`) to identify the change behind a cost spike. CloudTrail Event History is enabled by default in every AWS account at no charge. You do not need to create a trail or configure CloudTrail for the agent to investigate anomalies.
