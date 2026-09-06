

AWS FinOps Agent is in preview release and is subject to change.

# Surfacing cost optimization recommendations
<a name="optimization-recommendations"></a>

Ask the agent to retrieve, filter, and present cost-saving opportunities from AWS Cost Optimization Hub and AWS Compute Optimizer. Each recommendation includes the affected resource, current and recommended configuration, estimated monthly savings, implementation effort, and implementation guidance.

The agent retrieves recommendations from two complementary sources. **AWS Cost Optimization Hub** aggregates optimization opportunities across your account and groups them by action type (rightsizing, idle resource deletion, Savings Plans, Reserved Instances, architecture migration). **AWS Compute Optimizer** provides resource-level recommendations for EC2, Auto Scaling groups, EBS, Lambda, RDS, and ECS, including utilization metrics and per-resource savings.

The agent presents several categories of opportunities:
+ **Rightsizing.** Resources overprovisioned relative to actual usage, with current configuration, recommended smaller configuration, and supporting utilization data.
+ **Idle resources.** Unused resources that can be stopped or deleted, including unattached EBS volumes, idle EC2 instances, and unused DynamoDB tables and global secondary indexes.
+ **Savings Plans and Reserved Instances.** Opportunities to reduce costs by committing to consistent usage, with current coverage and estimated savings from additional commitments.
+ **Architecture migration.** Opportunities to move to more cost-effective platforms, such as migrating EC2 instances to Graviton processors or converting GP2 EBS volumes to GP3.

You can filter recommendations by account, Region, service, action type, effort level, or minimum savings threshold. By default, the agent orders recommendations by estimated monthly savings, highest first. You can use context files to define rules such as ignoring rightsizing in production accounts, discarding recommendations below a savings threshold, or grouping by engineering team.

From the agent, you can summarize selected recommendations into a Jira ticket. The engineering team picks up the work in Jira. Each ticket includes the recommendation summary, estimated savings, affected resources, effort level, and implementation guidance. For recurring optimization reviews, create a scheduled automation that reviews new recommendations on a cadence you set and summarizes them into Jira tickets. For details on scheduled automations, see [Task management](task-management.md).

Sample prompts:
+ “Show me all optimization opportunities sorted by savings.”
+ “Narrow it to low-effort ones saving over $500 per month.”
+ “What are our top quick-win optimization opportunities?”
+ “What instance type should I downsize i-abc123 to?”
+ “Estimate my annual savings if I implement all recommendations.”
+ “Every Monday, review new optimization opportunities and create Jira tickets in {{<jira-space-key>}}.”