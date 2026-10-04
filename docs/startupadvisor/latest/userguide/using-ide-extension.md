

# Using the AWS Startup Advisor IDE extension
<a name="using-ide-extension"></a>

The AWS Startup Advisor IDE extension (for VS Code, Kiro, and Cursor) has three main capabilities: personalized **alerts** about your AWS account, a **credits and cost widget** for tracking your startup’s AWS credit balance and AWS costs, and a curated library of **prompts** that you can use with your AI coding agent. To use the extension, you sign in to your AWS account (see the Sign in steps in [Getting started](getting-started.md)). When you sign in, you give the extension permission to read your account and generate alerts. You can sign in using one of the following methods: AWS IAM Identity Center (SSO) or an AWS CLI profile. You can switch between multiple profiles or accounts and Regions.

**Topics**
+ [Alerts](#using-ide-extension-alerts)
+ [Credits and cost widget](#using-ide-extension-credits)
+ [Prompts](#using-ide-extension-prompts)

## Alerts
<a name="using-ide-extension-alerts"></a>

The Alerts tab in the AWS Startup Advisor IDE extension surfaces optimization opportunities and recommended actions. AWS Startup Advisor uses your AWS profile permissions to monitor your configured resources. It proactively flags what to fix, so you can act on issues as they arise.

### What the Alerts tab monitors
<a name="alerts-what-monitored"></a>

The AWS Startup Advisor IDE extension surfaces personalized alerts. It generates most alerts locally from read-only AWS API calls against your account, scoped per Region. The alerts fall into three categories:
+  **Security** – For example, root access keys, missing MFA, unused credentials, open security groups, default VPCs, unencrypted RDS, EBS, or ElastiCache resources, CloudTrail gaps, and API Gateway throttling.
+  **Scalability** – For example, missing CloudWatch alarms and throttled Lambda functions.
+  **Cost management** – For example, stopped EC2 instances, orphaned EBS volumes, unattached Elastic IP addresses, orphaned RDS snapshots, idle SageMaker notebooks, Compute Optimizer recommendations, and AWS credits and balances.

**Note**  
The AWS credits and cost information comes from the credits and cost widget, which works differently from the locally computed alerts. For details, see [Credits and cost widget](#using-ide-extension-credits).

### Refresh alerts and switch profiles or Regions
<a name="alerts-refresh-scope"></a>

You can refresh alerts on demand. Alerts are scoped per Region.
+ To refresh alerts, run the ** AWS Startup Advisor: Refresh Alerts** command.
+ To switch your AWS profile or Region, use the avatar menu. Alerts are scoped per Region, so switching the Region changes which alerts appear.

### Configure alert settings
<a name="alerts-settings"></a>

You can configure the following settings for the AWS Startup Advisor extension:
+  `awsStartupAdvisor.alertPollInterval` – How often, in milliseconds, the extension polls for alerts. The default is `15000`.
+  `awsStartupAdvisor.telemetryEnabled` – Whether telemetry is enabled.
+  `awsStartupAdvisor.logLevel` – The log verbosity level.

## Credits and cost widget
<a name="using-ide-extension-credits"></a>

The AWS Startup Advisor IDE extension includes a credits and cost widget that tracks your startup’s AWS credit balance and your AWS costs for your AWS account. To use it, sign in to your AWS account in the extension (see the Sign in steps in [Getting started](getting-started.md)).

Unlike the alerts, which the extension computes locally from read-only AWS API calls, the credits and cost widget calls the AWS Startups service operation `startups:GetSpendSummary` to retrieve your account’s credits and cost data. The AWS Startups service obtains this data from AWS Billing and Cost Management and AWS Cost Explorer on your behalf. Because of this, the credits and cost widget requires AWS billing and cost read permissions. For more information, see [Identity and access management for AWS Startups](security-iam.md).

## Prompts
<a name="using-ide-extension-prompts"></a>

The extension includes a curated library of prompts vetted by AWS Startup Solutions Architects, grouped by category. These prompts are a curated selection drawn from the broader AWS Startups prompt library. They are distinct from the `prompt-library-for-startups` skill, which is the fuller prompt-and-agent library used by coding agents. For more information about that skill, see [Using AWS Startup Advisor skills](using-skills.md).

### Use a prompt
<a name="prompts-how-to-use"></a>

In the extension sidebar, browse prompts by category, open a prompt to review its steps, and then choose **Copy prompt**. Paste it into your AI coding agent (for example, Amazon Q, Kiro Chat, Cursor Chat, GitHub Copilot, or Claude Code) and run it.

### Prompt categories
<a name="prompts-categories"></a>

The prompts are grouped into the following categories. The following lists show representative examples, not every available prompt.
+  **Get started** – For example, set up read-only access for the extension, and set up IAM Identity Center (SSO) access for the extension.
+  **Build** – For example, Day 1 AWS account setup, scaffold your AWS architecture, deploy local code to AWS, and build AI workloads on AWS.
+  **Migrate** – For example, migrate from GCP to AWS, migrate from Heroku to AWS, and migrate AI workloads to AWS.
+  **Cost** – For example, cost and credits, and Compute Optimizer.
+  **Security** – For example, security baseline assessment, and automated GuardDuty and Security Hub deployment.
+  **Scalability** – For example, Well-Architected review, resiliency baseline, and requesting more GPU or Amazon Bedrock quota.

**Note**  
The prompts are starting points that you run in your agent. To have your agent carry out the deeper multi-step workflows (for example, the migrations), install the AWS Startup Advisor skills. You will see a notification when you open the AWS Startup Advisor IDE extension for the first time prompting you to install the AWS Startup Advisor skills. For more information, see [Using AWS Startup Advisor skills](using-skills.md) and, for live data, [Configure live data with MCP servers (optional)](mcp-servers.md). The extension also surfaces a banner that prompts you to install the skills.