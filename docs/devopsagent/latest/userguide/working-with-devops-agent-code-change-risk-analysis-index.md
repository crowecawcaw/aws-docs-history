

# Code Change Risk Analysis

**Preview:** Code Change Risk Analysis is in preview and is subject to change.

Code Change Risk Analysis is an AWS DevOps Agent capability that reviews code changes for production risks before they are deployed. It evaluates each change against your organization's standards, its dependencies across repositories, its access controls, and your production environments. It can also build, run, and test the change in a verification environment that AWS DevOps Agent manages. This capability was previously called release readiness review.

## What Code Change Risk Analysis checks
<a name="what-code-change-risk-analysis-checks"></a>

Code Change Risk Analysis assesses each change through the following checks:
+ **Standards evaluation** – Assesses the change against your organization's standards and best practices, defined as natural-language [skills](about-aws-devops-agent-devops-agent-skills-index.md). Standards can cover security, reliability, performance, and operational best practices without requiring policy-as-code expertise.
+ **Cross-repository dependency analysis** – Maps how your repositories interact and identifies when a change in one repository will break consumers in another, using a knowledge graph built from indexing your connected repositories.
+ **Production intelligence** – Uses what AWS DevOps Agent learns about your production environments to check whether the change will break AWS or third-party observability metrics and alarms, whether IAM or resource policies in your production environments will prevent the change from working as expected, and whether data flows will break in any target production environment.
+ **Automatic verification testing** – Builds, runs, and tests the change in a verification environment. For more information, see [Automatic verification testing](code-change-risk-analysis-reviewing-code-changes.md#automatic-verification-testing).

Each review produces a report with a recommended action (BLOCK, Deploy with Caution, Standard Deployment, Request Permissions, or Insufficient Data), a summary of the changes, specific risk findings with affected code locations, and recommendations. For more information, see [Reviewing code changes](code-change-risk-analysis-reviewing-code-changes.md).

## Review depth
<a name="review-depth"></a>

You choose how deeply Code Change Risk Analysis reviews the changes on each branch of a repository:
+ **Static code analysis** – Reviews the change without building or running it. Static reviews take less time and cost less, but they produce more false positives.
+ **Static code analysis with verification testing** – Also builds, runs, and tests the change in a verification environment. These reviews produce fewer false positives, but they take longer and cost more.

For example, you can run verification testing on pull requests into your `main` branch and static code analysis on all others. For instructions on configuring review depth, see [Configuring review depth](code-change-risk-analysis-reviewing-code-changes.md#configuring-review-depth). For pricing, see [AWS DevOps Agent pricing](https://aws.amazon.com/devops-agent/pricing/).

## Where Code Change Risk Analysis runs
<a name="where-code-change-risk-analysis-runs"></a>

Code Change Risk Analysis integrates into your workflow at multiple points:
+ **During code generation** – In Kiro and Claude Code as code is being written, so that issues are found before code is committed.
+ **In pull requests and merge requests** – Automatically when pull requests or merge requests are opened or updated in GitHub and GitLab. Findings appear as inline comments with recommended fixes.
+ **On demand** – Through AWS DevOps Agent chat, [custom agents](working-with-devops-agent-custom-agents-index.md), and [webhooks](configuring-integrations-and-knowledge-invoking-devops-agent-through-webhook.md). You can request a review of any branch, commit, or repository and ask follow-up questions about findings.

## Getting started with Code Change Risk Analysis
<a name="getting-started-with-code-change-risk-analysis"></a>

To begin using Code Change Risk Analysis:

1. **Connect your repositories** – In your Agent Space, [connect your GitHub or GitLab repositories](configuring-integrations-and-knowledge-connecting-to-cicd-pipelines-index.md). The agent indexes your code to build a knowledge graph of cross-repository dependencies. Initial indexing takes approximately one to two hours.

1. **Choose a review depth (optional)** – Decide which branches run static code analysis only and which also run verification testing. For more information, see [Configuring review depth](code-change-risk-analysis-reviewing-code-changes.md#configuring-review-depth).

1. **Define your standards (optional)** – [Use agent instructions](about-aws-devops-agent-agent-instructions.md) to define the review behaviors and internal standards that every review should include. You can specify what constitutes a blocking change versus a warning.

1. **Request your first review** – In AWS DevOps Agent chat, request a review. For example: "Review branch main on repo my-service for release risks." The agent evaluates the change and returns a report with findings.

## How Code Change Risk Analysis learns
<a name="how-code-change-risk-analysis-learns"></a>

Code Change Risk Analysis improves over time through two mechanisms:

1. **Repository knowledge** – As the agent indexes your repositories, it builds an increasingly complete understanding of cross-repository dependencies, shared resources, API contracts, and infrastructure relationships. This knowledge makes dependency risk analysis more accurate with each review.

1. **Customer-provided skills** – Define custom [skills](about-aws-devops-agent-devops-agent-skills-index.md) that encode your organization's specific approaches to evaluating code, such as how to assess cross-service dependencies, when a feature flag is required, which patterns warrant additional scrutiny, or how to evaluate changes against your internal architectural standards. These skills let you teach the agent your team's policies and practices so that reviews reflect your organization's expectations.