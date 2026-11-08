

# Using the AWS Startup Advisor IDE extension
<a name="using-ide-extension"></a>

The AWS Startup Advisor IDE extension (for VS Code, Kiro, and Cursor) brings personalized AWS guidance into your editor. The panel has three tabs: **For you**, **Prompts**, and **Alerts**. It also includes a **Cost & Credits** view for tracking your startup’s AWS spend and promotional credit balance, and an **Exclusive Offers** link to AWS Startups offers.

Before you sign in, you can preview the **Cost & Credits** and **Alerts** views with illustrative sample data, not your own account data. The **Prompts** are available without signing in. To see data for your own account, sign in to the extension (see the Sign in steps in [Getting started](getting-started.md)). When you sign in, you give the extension permission to read your account, so it can generate alerts. You can sign in using one of the following methods: AWS IAM Identity Center (SSO), an AWS CLI profile, or AWS IAM access keys. You can switch between multiple profiles or accounts and Regions.

**Topics**
+ [For you](#using-ide-extension-for-you)
+ [Alerts](#using-ide-extension-alerts)
+ [Cost & Credits](#using-ide-extension-credits)
+ [Exclusive Offers](#using-ide-extension-offers)
+ [Prompts](#using-ide-extension-prompts)
+ [Apply for AWS Activate credits](#using-ide-extension-activate)
+ [Operate with AWS DevOps Agent](#using-ide-extension-operate)

## For you
<a name="using-ide-extension-for-you"></a>

The **For you** tab shows personalized recommendations based on your account’s alerts and spend. For example, when your promotional credits are within about 30 days of running out, the extension recommends that you plan for your credits running out. To see recommendations for your account, sign in to the extension (see the Sign in steps in [Getting started](getting-started.md)).

## Alerts
<a name="using-ide-extension-alerts"></a>

The Alerts tab in the AWS Startup Advisor IDE extension surfaces optimization opportunities and recommended actions. AWS Startup Advisor uses your AWS profile permissions to monitor your configured resources. It proactively flags what to fix, so you can act on issues as they arise.

### What the Alerts tab monitors
<a name="alerts-what-monitored"></a>

The AWS Startup Advisor IDE extension surfaces personalized alerts. It generates most alerts locally from read-only AWS API calls against your account, scoped per Region. The alerts fall into three categories:
+  **Security** – For example, root access keys, IAM users without multi-factor authentication (MFA), missing MFA, unused credentials, open security groups, default Amazon VPCs, VPCs without flow logs, unencrypted Amazon RDS, Amazon EBS, or Amazon ElastiCache resources, AWS Lambda functions with an administrator role, hard-coded Lambda credentials, AWS CloudTrail gaps, CloudTrail log file validation, Amazon Cognito MFA, Amazon Bedrock Guardrails, Amazon Bedrock invocation logging, and Amazon API Gateway throttling.
+  **Scalability** – For example, missing Amazon CloudWatch alarms, throttled Lambda functions, Amazon DynamoDB tables without point-in-time recovery, RDS instances without backups, Amazon EC2 Auto Scaling health checks, and Amazon Route 53 failover.
+  **Cost management** – For example, stopped Amazon EC2 instances, orphaned EBS volumes, unattached Elastic IP addresses, orphaned RDS snapshots, idle Amazon SageMaker notebooks, orphaned SageMaker endpoints, SageMaker training without Spot, idle NAT gateways, idle load balancers, Amazon ECR repositories without lifecycle policies, Amazon S3 incomplete multipart uploads, AWS Compute Optimizer recommendations, and AWS credits and balances.

The Alerts tab also surfaces the following alerts:
+  ** AWS DevOps Agent alerts** – For example, new investigations, recommendations, and included-hours usage (your free trial ending, your usage period ending, and included hours used up and now billing at standard rates). For more information, see [Operate with AWS DevOps Agent](#using-ide-extension-operate).

Two alerts help protect you against LLM-jacking, where attackers use a leaked AWS access key to run Amazon Bedrock models on your bill:
+  **Leaked access key quarantined by AWS ** – When AWS finds one of your access keys posted publicly, for example on GitHub, it attaches a quarantine policy that blocks the riskiest actions, such as running Amazon Bedrock models or launching instances. The key still works for other actions. The alert names the affected users and their access keys, and tells you if you’re signed in to the extension as one of them. It appears first in the Alerts tab. If you dismiss it, it comes back after 24 hours until the quarantine is removed. Keep AWS's quarantine in place until AWS closes your support case.
+  **No billing alerts set up** – The account has no AWS Budgets alert, no Cost Anomaly Detection alert, or neither. Without them, a leaked key can run up charges that you don’t see until your bill arrives. Both services are free and email you when spending looks wrong. If your account is a member of an AWS Organization, the alert notes that your company might have set up spending alerts in its main AWS account.

Each alert’s fix prompt has your coding agent investigate the problem and propose a fix, then wait for your approval before changing anything.

Alerts appear in a set order: the quarantined leaked access key alert first, then AWS DevOps Agent alerts, and then the remaining alerts by priority.

Each alert includes a fix prompt that you can give your coding agent to resolve the issue. You can dismiss alerts that you don’t want to act on. The quarantined leaked access key alert is an exception: if you dismiss it, it comes back after 24 hours.

**Note**  
The AWS credits and cost information comes from the **Cost & Credits** view, which works differently from the locally computed alerts. For details, see [Cost & Credits](#using-ide-extension-credits).

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
+  `awsStartupAdvisor.offersOpenTarget` – Where the **Exclusive Offers** link opens. Use `ideBrowser` (the default) to open the page in the IDE’s built-in browser, or `externalBrowser` to open it in your default browser.

## Cost & Credits
<a name="using-ide-extension-credits"></a>

The **Cost & Credits** view in the AWS Startup Advisor IDE extension tracks your startup’s AWS spend and promotional credit balance for your AWS account. It shows your account spend (month to date and last month), a cost forecast, and your promotional credit balance, including an estimated date that your credits run out. To see data for your account, sign in to the extension (see the Sign in steps in [Getting started](getting-started.md)).

Unlike the alerts, which the extension computes locally from read-only AWS API calls, the **Cost & Credits** view calls the AWS Startups service operation `startups:GetSpendSummary` to retrieve your account’s credits and cost data. The AWS Startups service obtains this data from AWS Billing and Cost Management and AWS Cost Explorer on your behalf. Because of this, the **Cost & Credits** view requires AWS billing and cost read permissions. For more information, see [Identity and access management for AWS Startups](security-iam.md).

**Note**  
Cost data can be delayed.

## Exclusive Offers
<a name="using-ide-extension-offers"></a>

The **Exclusive Offers** link opens the AWS Startups Exclusive Offers page in the IDE’s built-in browser. You can also open the page in your default browser.

You can control where the link opens with the `awsStartupAdvisor.offersOpenTarget` setting:
+  `ideBrowser` – Opens the page in the IDE’s built-in browser. This is the default.
+  `externalBrowser` – Opens the page in your default browser.

## Prompts
<a name="using-ide-extension-prompts"></a>

The extension includes a curated library of prompts vetted by AWS Startup Solutions Architects, grouped by category. These prompts are a curated selection drawn from the broader AWS Startups prompt library. They are distinct from the `prompt-library-for-startups` skill, which is the fuller prompt-and-agent library used by coding agents. For more information about that skill, see [Using AWS Startup Advisor skills](using-skills.md).

### Use a prompt
<a name="prompts-how-to-use"></a>

In the extension sidebar, browse prompts by category, open a prompt to review its steps, and then choose **Copy prompt**. Paste it into your AI coding agent (for example, Amazon Q, Kiro Chat, Cursor Chat, GitHub Copilot, or Claude Code) and run it.

### Prompt categories
<a name="prompts-categories"></a>

The prompts are grouped into the following categories. The following lists show representative examples, not every available prompt.
+  **Get started** – For example, set up read-only access for the extension, set up IAM Identity Center (SSO) access for the extension, and Pre-Fill My AWS Activate Credits Application (see [Apply for AWS Activate credits](#using-ide-extension-activate)).
+  **Build** – For example, Day 1 AWS account setup, scaffold your AWS architecture, deploy local code to AWS, and build AI workloads on AWS.
+  **Migrate** – For example, migrate from GCP to AWS, migrate from Heroku to AWS, and migrate AI workloads to AWS.
+  **Operate** – For example, review a pull request, review what you are about to commit, and investigate a production incident (see [Operate with AWS DevOps Agent](#using-ide-extension-operate)).
+  **Cost** – For example, cost and credits, and Compute Optimizer.
+  **Security** – For example, security baseline assessment, and automated GuardDuty and Security Hub deployment.
+  **Scalability** – For example, Well-Architected review, resiliency baseline, and requesting more GPU or Amazon Bedrock quota.

**Note**  
The prompts are starting points that you run in your agent. To have your agent carry out the deeper multi-step workflows (for example, the migrations), install the AWS Startup Advisor skills. You will see a notification when you open the AWS Startup Advisor IDE extension for the first time prompting you to install the AWS Startup Advisor skills. For more information, see [Using AWS Startup Advisor skills](using-skills.md) and, for live data, [Configure live data with the MCP server (optional)](mcp-servers.md).

## Apply for AWS Activate credits
<a name="using-ide-extension-activate"></a>

The **Pre-Fill My AWS Activate Credits Application** prompt, in the **Get started** category, starts an agent that interviews you, infers what it can from your website, and stages your AWS Activate credits application. Nothing is submitted on your behalf. You review and submit the application yourself.

To pre-fill and submit your AWS Activate credits application:

1. Tell the agent about your startup. Paste your website and a sentence or two describing what you do.

1. Answer the few things the agent can’t work out, such as your email, phone number, and your exact founding and launch dates.

1. Sign in with your AWS Builder ID, using the same email that you gave the agent.

1. Open the presubmission link that the agent gives you.

1. Review the pre-filled application and submit it yourself.

**Note**  
The presubmission link works once, and the staged application expires after 24 hours.

## Operate with AWS DevOps Agent
<a name="using-ide-extension-operate"></a>

The **Operate** prompt category helps you operate a live AWS workload with [AWS DevOps Agent](https://aws.amazon.com/devops-agent/). It has two cards, and both use AWS DevOps Agent:
+  **Catch Breaking Changes Before You Ship** – Runs release-readiness reviews of a pull request, or of the change that you’re about to commit. Release reviews run on GitHub or GitLab repositories connected to the Agent Space. Release-readiness review is in preview, at no charge during the preview, and available only in US East (N. Virginia).
+  **Auto-Investigate Production Incidents** – Runs investigations that find the probable root cause from your logs, metrics, alarms, and recent changes, and then propose a fix for you to approve.

You set up AWS DevOps Agent through your coding agent. Before you enable anything, your coding agent explains what AWS DevOps Agent does, the access it needs, and how billing works. Nothing is enabled or charged until you say yes. Your coding agent then checks your permissions and creates the Agent Space. If setup is interrupted, you can resume it.

Each card shows the Agent Space’s status, its integrations, and its reports on the **Reports** tab. You run investigations and release reviews from ready-made prompts, and you can cancel running tasks. Running tasks incur AWS DevOps Agent charges.

You can pause automatic investigations, reviews, and scheduled evaluations, which keeps your setup. You can also remove AWS DevOps Agent completely by deleting the Agent Space or its role.

When you turn on automated release testing, AWS DevOps Agent copies your code into an AWS managed verification environment to build and test it, instead of running it in your AWS account. The environment runs on dedicated compute, and its network access is limited to trusted sources such as AWS services and package registries. Built-in safeguards block credential exposure and data exfiltration, and prevent changes to your AWS resources. Automated release testing is off by default and requires a separate opt-in. For more information, see [Release readiness code reviews](https://docs.aws.amazon.com/devopsagent/latest/userguide/release-management-release-readiness-code-review.html) in the * AWS DevOps Agent User Guide*. To turn off automated release testing later, ask your coding agent to turn it off, or open your Agent Space in the AWS DevOps Agent console, choose the **Capabilities** tab, edit the GitHub or GitLab connection, and turn off **Automatic verification testing** for the repository. Release reviews keep working without it.

 AWS DevOps Agent recommends fixes. It doesn’t apply them. You review a proposed fix and decide whether your coding agent applies it.

 AWS Startup Advisor is available at no additional charge, but AWS DevOps Agent is a paid AWS service. If you have AWS Activate credits, they can cover your AWS DevOps Agent usage. For pricing information, see [AWS DevOps Agent pricing](https://aws.amazon.com/devops-agent/pricing/). For more information about AWS DevOps Agent, see the [AWS DevOps Agent User Guide](https://docs.aws.amazon.com/devopsagent/latest/userguide/).

For the skill that drives these workflows from your coding agent, see [operate-on-aws](using-skills.md#skill-operate-on-aws). For the permissions that AWS DevOps Agent setup uses, see [Identity and access management for AWS Startups](security-iam.md).