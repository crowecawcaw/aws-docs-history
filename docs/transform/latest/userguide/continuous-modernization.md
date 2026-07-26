# AWS Transform continuous modernization

## What is AWS Transform continuous modernization?

AWS Transform continuous modernization provides analysis and remediation for your
source code repositories. You can connect GitHub organizations, GitLab groups, Bitbucket
workspaces, and local repositories, then run automated analyses to identify technical debt,
security vulnerabilities, modernization opportunities, and agent-readiness across your entire
codebase.

All analysis and remediation run in your AWS account using your credentials. Your source
code stays under your control.

###### Note

We recommend starting with the Kiro Power or agent plugin. The agent skill orchestrates
setup, onboarding, and ongoing use of continuous modernization including infrastructure
provisioning, source configuration, analysis execution, findings triage, and remediation. For
installation instructions, see
[Developer tools](ct-developer-tools.md "ct-developer-tools.md").

## Key capabilities

AWS Transform continuous modernization provides the following capabilities:

- **Tech Debt Analysis** — Scan repositories for outdated
  dependencies, security vulnerabilities, code quality issues, and modernization
  opportunities. Run quick metadata scans across package manifests or comprehensive
  code-level analysis. Define custom analysis criteria using transformation definitions
  tailored to your environment.
- **Autonomous Remediation** — Generate validated pull
  requests at scale. Each finding can be auto-remediated using its associated transformation
  definition. Remediation creates branches and opens PRs/MRs automatically across GitHub,
  GitLab, and Bitbucket.
- **Reporting** — Generate HTML reports showing findings by
  severity, repository, and analysis type. Track remediation progress and finding resolution
  over time.
- **Continuous Monitoring** — Schedule recurring analyses
  using Amazon EventBridge Scheduler. Configure daily, weekly, or custom cron schedules to
  continuously monitor your portfolio for new issues.

## Analysis types

AWS Transform continuous modernization supports the following analysis types to address your
modernization needs.

| Type                      | Description                                                                                                                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `rapid-techdebt-analysis` | Fast metadata-only scan of package manifests (`pom.xml`,<br>`package.json`, `requirements.txt`) to identify stale versions<br>and outdated dependencies. Does not analyze source code.                                                        |
| `tech-debt-comprehensive` | Deep code-level technical debt analysis using the AWS Transform agent. Examines source<br>code to identify debt patterns, code quality issues, architecture concerns, and<br>improvement opportunities.                                       |
| `security`                | Security vulnerability and CVE detection using the AWS Security Agent. Scans<br>source code and dependencies for known vulnerabilities, insecure coding patterns, and<br>exploitable weaknesses. Requires one-time infrastructure setup.      |
| `agentic-readiness`       | AI and agent integration readiness assessment. Scores 56 criteria across five<br>categories: Infrastructure & Platform, Application Architecture, Data Foundations,<br>Identity/Security/Governance, and Operations & Observability.          |
| `modernization-readiness` | Cloud modernization opportunity assessment. Evaluates readiness across<br>infrastructure, application, data, security, and operations dimensions. Identifies<br>candidates for containerization, serverless migration, and platform upgrades. |
| `custom`                  | Run any transformation definition (TD) as an analysis. Use this type to define<br>your own analysis criteria or to run AWS managed transforms not covered by the<br>built-in types.                                                           |

## Understanding key concepts

### Sources

A source tells continuous modernization where your repositories are. Supported source
types:

- **GitHub** — Organizations with personal access
  tokens (classic)
- **GitLab** — Groups or users, including
  self-hosted instances
- **Bitbucket** — Workspaces (Cloud) or projects
  (Data Center)
- **Local** — Parent directories containing git
  repositories

### Repositories

Repositories are discovered by scanning sources. After discovery, you can filter by
source, labels, or other criteria; apply labels for organization (team, priority, migration
wave); and target specific repositories for analysis or remediation.

### Analyses

An analysis is a scan of one or more repositories using a specific analysis type. Each
analysis produces findings that identify issues in your code. You can run analyses on demand
or schedule them to run automatically. Analysis types include rapid-techdebt-analysis,
tech-debt-comprehensive, security, agentic-readiness, modernization-readiness, and custom.
Each analysis tracks its status (pending, running, complete, cancelled, or failed) and the
repositories it scanned.

### Findings

Findings are the results of analysis. Each finding includes severity (high, medium, or
low), status (open, dismissed, or obsolete), and the fix transform that can remediate it (if
auto-fixable). New findings start as open. Users can dismiss findings with a reason.
Re-analysis marks resolved findings as obsolete automatically.

### Remediations

Remediations apply transformation definitions to fix findings. Three modes:
findings-based (each finding uses its own fix transform), TD override (override the
transformation definition for specified findings), and direct TD (run a transformation
against a repository without findings). Output depends on the source provider (GitHub PR,
GitLab MR, Bitbucket PR, or local branch).

### Transformation definitions

A transformation definition contains the instructions and knowledge needed to perform a
specific code transformation. Continuous modernization uses transformation definitions for
custom analysis
(`--type custom --transformation-name `name``) and
 remediation (`--transformation-name `name``). List
available transformation definitions with `atx custom def list`.

## How AWS Transform continuous modernization works

AWS Transform continuous modernization is typically used in large-scale projects where multiple
codebases need continuous analysis and remediation. Teams typically follow this
workflow:

1. **Connect Sources** — Add GitHub organizations, GitLab
   groups, Bitbucket workspaces, or local directories as sources. Provide authentication
   tokens with appropriate scopes.
2. **Discover Repositories** — Run discovery scans to
   enumerate all repositories in your sources. Use labels to organize repositories by team,
   priority, or migration wave.
3. **Run Analysis** — Execute analyses across your portfolio.
   Choose quick scans for fast results or comprehensive analysis for detailed findings.
   Security analysis requires one-time infrastructure setup.
4. **Triage Findings** — Review findings by severity,
   repository, or analysis type. Dismiss false positives with documented reasons. Re-run
   analysis to mark resolved issues as obsolete.
5. **Remediate** — Create remediations to fix findings.
   Continuous modernization automatically creates branches and opens pull/merge requests with
   the fixes. Track remediation status and retry failures.
6. **Set Up Continuous Analysis** — Schedule recurring
   analyses using Amazon EventBridge Scheduler. Configure analysis cadence (daily, weekly,
   or custom cron) to continuously monitor your portfolio for new issues. Combine with
   automated remediation to maintain code health over time.

### Compute options

Continuous modernization supports three compute options for running analyses and
remediation. The agent skills in the Kiro Power and agent plugin help you set up
infrastructure for each option.

###### Note

Regardless of compute option, all analysis and remediation happen in your AWS account
using your credentials. Your source code remains under your control.

#### Local (default)

By default, analyses run on your local machine. This option requires no additional
infrastructure. The server runs locally and executes analyses using local compute resources.
Good for trying out the tool, small repositories, or individual use.

#### Amazon Amazon EC2

Run analyses on a persistent Amazon EC2 instance in your AWS account. This option offloads
compute from your local machine, supports larger analyses, and enables recurring scheduled
analysis. The instance stays running between submissions.

The agent skill provisions a AWS CloudFormation stack that includes:

- An Amazon EC2 instance (Amazon Linux 2023) with Docker and the continuous
  modernization container
- An IAM role with permissions for AWS Transform, Amazon S3, AWS KMS, Secrets Manager,
  and the security agent
- `AmazonSSMManagedInstanceCore` for shell access via SSM (no SSH
  key pair or inbound ports required)
- A security group with no inbound rules

Your IAM user or role needs permissions for Amazon EC2 lifecycle management, AWS CloudFormation stack
operations, IAM role creation, Amazon S3 bucket operations, Secrets Manager secret management,
and SSM commands.

To set up EC2 execution, install the Kiro Power or agent plugin (see
[Developer tools](ct-developer-tools.md "ct-developer-tools.md")), then ask the
agent: _"Set up an EC2 instance for continuous modernization analysis"_.
The agent provisions the infrastructure, verifies the container is healthy, and submits your
analyses via SSM — no SSH required.

#### AWS Batch (Fargate)

Run analyses as isolated jobs on AWS Batch with Fargate for serverless compute. Each
analysis runs in its own container without managing persistent infrastructure. Good for
parallel analysis of multiple sources or analysis types.

This option reuses the AWS Transform CDK infrastructure stack. The agent skill deploys the
required infrastructure including:

- AWS Batch job queue and compute environment
- Job definition with the continuous modernization container
  image
- IAM roles for batch job execution
- A Lambda function for job submission

To set up Batch execution, install the Kiro Power or agent plugin (see
[Developer tools](ct-developer-tools.md "ct-developer-tools.md")), then ask the
agent: _"Run my analysis on Fargate"_ or _"Set up Batch
execution for continuous modernization"_. The agent deploys the CDK stack, stores
your source credentials in Secrets Manager, and submits analysis jobs to AWS Batch.

### Security agent setup

The `security` analysis type uses the AWS Security Agent service for
vulnerability and CVE detection. Unlike other analysis types, it requires one-time
infrastructure setup in your AWS account.

The setup command provisions a AWS CloudFormation stack that includes:

- An Amazon S3 bucket for source code upload
- An IAM role assumed by `securityagent.amazonaws.com`
- A managed policy for the security agent role

Your IAM user or role must have the following additional permissions to run the
setup:

- `cloudformation:CreateStack`, `cloudformation:UpdateStack`,
  `cloudformation:DescribeStacks`
- `iam:CreateRole`, `iam:PutRolePolicy`,
  `iam:AttachRolePolicy`, `iam:CreatePolicy`
- `s3:CreateBucket`, `s3:PutBucketEncryption`,
  `s3:PutBucketPublicAccessBlock`

Use the following commands to manage the security agent infrastructure:

```
# Provision the security agent infrastructure
atx ct setup security-agent

# Check the status
atx ct setup security-agent --status

# Delete the infrastructure
atx ct setup security-agent --delete
```

After setup completes, you can run security analyses the same way as other analysis
types.
