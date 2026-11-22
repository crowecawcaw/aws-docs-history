

AWS FinOps Agent is in preview release and is subject to change.

# AWS managed policies for AWS FinOps Agent

AWS managed policies are standalone identity-based policies that AWS creates and maintains. AWS FinOps Agent uses the following managed policies for the roles it assumes. If you configure roles manually, see the [IAM setup guide](setting-up.md).

**Topics**
+ [AWS managed policy: FinOpsAgentAgentPolicy](#security-iam-awsmanpol-FinOpsAgentAgentPolicy)
+ [AWS managed policy: FinOpsAgentOperatorPolicy](#security-iam-awsmanpol-FinOpsAgentOperatorPolicy)
+ [AWS managed policy: AWSFinOpsAgentServiceRolePolicy](#security-iam-awsmanpol-AWSFinOpsAgentServiceRolePolicy)
+ [AWS FinOps Agent updates to AWS managed policies](#security-iam-awsmanpol-updates)

## AWS managed policy: FinOpsAgentAgentPolicy
<a name="security-iam-awsmanpol-FinOpsAgentAgentPolicy"></a>

Attach `FinOpsAgentAgentPolicy` to the agent role for an account-scoped agent. AWS FinOps Agent assumes this role to read the cost, billing, optimization, and resource data that agent workflows use.

Because this policy includes every action in [`AWSFinOpsAgentServiceRolePolicy`](#security-iam-awsmanpol-AWSFinOpsAgentServiceRolePolicy), account-scoped agents can read the same data as organization-wide agents.

The policy includes permissions to do the following:
+ Read cost, usage, and billing information. This includes invoices, credits, billing views, budgets, purchase orders, Free Tier usage, cost categories, data exports, and AWS Billing Conductor billing groups. The agent uses this information to answer cost questions and explain cost changes.
+ Read prices and AWS Pricing Calculator workload estimates, and start commitment purchase analyses and Savings Plans recommendation generation. The agent uses these to estimate costs and savings.
+ Read optimization recommendations and settings from AWS Cost Optimization Hub, AWS Compute Optimizer, and Cost Optimization Automation, and read Savings Plans and reservation details. The agent uses these to find savings opportunities.
+ Read the configuration of resources that affect cost, such as compute, container, database, storage, machine learning, and Amazon WorkSpaces resources. Find resources with AWS Resource Explorer and tags. The policy allows reading Amazon S3 bucket settings only in the role's own account.
+ Read Amazon CloudWatch metrics and log group settings, and run CloudWatch Logs Insights queries. Read AWS CloudTrail trail settings and events, and AWS Health events. The agent uses these to relate usage and events to cost.
+ Read your account and organization structure, so the agent can attribute costs to accounts and organizational units.
+ List datasets in Data Hub, a feature of AWS Billing and Cost Management, and run read-only queries on them. The agent uses these queries to answer questions that need line-item cost and usage data.
+ Manage the Amazon EventBridge rules that AWS FinOps Agent owns in the role's own account for the workflows that you configure. You can't use this policy to manage other EventBridge rules.

For instructions on setting up the agent role, see [Agent permissions policy](setting-up.md#setting-up-agent-policy). Organization-wide agents use the service-linked role described in [Setting up organization-wide access and a delegated administrator](setting-up-organization-access.md).

For more information about the current policy document, see [FinOpsAgentAgentPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/FinOpsAgentAgentPolicy.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: FinOpsAgentOperatorPolicy
<a name="security-iam-awsmanpol-FinOpsAgentOperatorPolicy"></a>

Attach `FinOpsAgentOperatorPolicy` to the operator role. AWS FinOps Agent assumes this role to perform web application operations, including conversations, tasks, automations, context files, and reports.

For instructions on setting up the operator role, see [Operator permissions policy](setting-up.md#setting-up-operator-policy).

For more information about the current policy document, see [FinOpsAgentOperatorPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/FinOpsAgentOperatorPolicy.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: AWSFinOpsAgentServiceRolePolicy
<a name="security-iam-awsmanpol-AWSFinOpsAgentServiceRolePolicy"></a>

You can't attach `AWSFinOpsAgentServiceRolePolicy` to your IAM entities. This policy is attached to the `AWSServiceRoleForFinOpsAgent` service-linked role. The role allows AWS FinOps Agent to read cost, billing, optimization, and infrastructure data across the accounts in your organization. AWS FinOps Agent can also use it to query Data Hub datasets and to manage the Amazon EventBridge rules that it creates for automations. For the permissions and how the role is used, see [Using service-linked roles for AWS FinOps Agent](using-service-linked-roles.md).

For more information about the current policy document, see [AWSFinOpsAgentServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSFinOpsAgentServiceRolePolicy.html) in the *AWS Managed Policy Reference*.

## AWS FinOps Agent updates to AWS managed policies
<a name="security-iam-awsmanpol-updates"></a>

View details about updates to AWS managed policies for AWS FinOps Agent since this service began tracking these changes. For automatic alerts about changes to this page, subscribe to the RSS feed on the AWS FinOps Agent [Document history](doc-history.md) page.


| Change | Description | Date | 
| --- | --- | --- | 
| [Service-linked role policy](#security-iam-awsmanpol-AWSFinOpsAgentServiceRolePolicy) – Update to an existing policy | AWS FinOps Agent added permissions to list Data Hub datasets, read their schemas, and run, monitor, cancel, and retrieve results from read-only queries. Organization-wide agents use these permissions to answer cost questions from Data Hub datasets.<br />AWS FinOps Agent also tightened the AWS Organizations `ListDelegatedAdministrators` action so the policy allows it only when a request specifies `finops-agent.amazonaws.com`. | November 19, 2026 | 
| [FinOpsAgentAgentPolicy](#security-iam-awsmanpol-FinOpsAgentAgentPolicy) – Update to an existing policy | AWS FinOps Agent added permissions so that account-scoped agents can read the same data as organization-wide agents. The new permissions cover billing, invoice, purchase order, Free Tier, and credit program details; budget action details and history; and cost category and data export settings. They also cover organization structure, log group settings, and the configuration of compute, database, storage, machine learning, and Amazon WorkSpaces resources. Other new permissions allow searching for resources with AWS Resource Explorer and tags, and reading Amazon S3 bucket settings in the role's own account only. AWS FinOps Agent also added permissions to list Data Hub datasets and run read-only queries on them.<br />The added AWS Organizations `ListDelegatedAdministrators` permission applies only when a request specifies `finops-agent.amazonaws.com`. | November 19, 2026 | 
| [Service-linked role policy](#security-iam-awsmanpol-AWSFinOpsAgentServiceRolePolicy) – New policy | AWS FinOps Agent added a new AWS managed policy for the `AWSServiceRoleForFinOpsAgent` service-linked role. The policy allows AWS FinOps Agent to read cost, billing, optimization, and infrastructure data across the accounts in your organization. It also allows AWS FinOps Agent to manage the Amazon EventBridge rules that it creates for automations. | October 20, 2026 | 
| [FinOpsAgentAgentPolicy](#security-iam-awsmanpol-FinOpsAgentAgentPolicy) – Update to an existing policy | AWS FinOps Agent added permissions to read AWS Cost Optimization Hub preferences and enrollment status, billing view segments, and Amazon RDS major engine versions. | October 2, 2026 | 
| [FinOpsAgentAgentPolicy](#security-iam-awsmanpol-FinOpsAgentAgentPolicy) – Update to an existing policy | AWS FinOps Agent added permissions to read billing preferences and AWS Cost Optimization Hub efficiency metrics. | September 24, 2026 | 
| [FinOpsAgentAgentPolicy](#security-iam-awsmanpol-FinOpsAgentAgentPolicy) – Update to an existing policy | AWS FinOps Agent added permissions to read Enterprise Support charges, budget actions, and Savings Plans details. It also added permissions to start and read commitment purchase analyses and Savings Plans purchase recommendation generation. | September 1, 2026 | 
| [FinOpsAgentAgentPolicy](#security-iam-awsmanpol-FinOpsAgentAgentPolicy) – Update to an existing policy | AWS FinOps Agent added permissions to read Cost Optimization Automation rules and events, billing views and credits, and AWS Health events. It also added permissions to read AWS Billing Conductor billing groups and pricing, and invoice profiles, units, summaries, and procurement portal preferences. | August 19, 2026 | 
| AWS FinOps Agent started tracking changes | AWS FinOps Agent started tracking changes for its AWS managed policies. | June 9, 2026 | 