# Working with continuous modernization

## Source management

Use `atx ct source` commands to connect repositories. Supported providers:
GitHub, GitLab, Bitbucket, local.

### GitHub organizations

Token: personal access token (classic) with `repo` scope. Read-only for
analysis, full repo for remediation.

```
atx ct source add --name `name` --provider github --org `org` --token `pat`
```

### GitLab groups and users

Token: personal access token with `api` scope.

```
atx ct source add --name `name` --provider gitlab --org `group-or-user` --token `pat`
# Self-hosted:
atx ct source add --name `name` --provider gitlab --org `group-or-user` --token `pat` --url https://`gitlab.example.com`
```

### Bitbucket workspaces and projects

Bitbucket Cloud — scopes: `read:repository:bitbucket`,
`write:repository:bitbucket`, `read:pullrequest:bitbucket`,
`write:pullrequest:bitbucket`. Also needs `--email` and
`--username`.

```
atx ct source add --name `name` --provider bitbucket --org `workspace` --token `api-token` --email `email` --username `username`
```

Bitbucket Data Center:

```
atx ct source add --name `name` --provider bitbucket --org `project-key` --token `http-access-token` --url https://`bitbucket.example.com`
```

### Local repositories

```
atx ct source add --name `name` --provider local --path `parent-directory`
```

###### Important

`--path` must point to a parent directory containing git repos as
subdirectories, not to a single repo.

### Managing sources

```
atx ct source list
atx ct source remove --name `name`
```

## Repository discovery and management

```
atx ct discovery scan --source `name`
atx ct discovery status --source `name`
atx ct discovery scan --source `name` --path `new-directory`
```

After discovery:

```
atx ct repository list
atx ct repository list --source `name`
atx ct repository list --labels "`team:frontend,priority:high`"
atx ct repository update --source `name` --repo "`source`::`repo`" --labels "`team:frontend,priority:high`"
atx ct repository update --source `name` --labels "`migration:wave-1`"
```

## Running analysis

The `--type` flag specifies the kind of analysis to run:

- `rapid-techdebt-analysis` – Outdated dependencies and easy
  wins.
- `tech-debt-comprehensive` – Deeper AI-powered analysis covering
  dependency, security, pattern, performance, maintainability, architecture, code-quality, and
  infrastructure findings.
- `security` – Security vulnerabilities and
  exposures.
- `agentic-readiness` – Readiness of your repositories for AI agents
  (frameworks, APIs, documentation).
- `modernization-readiness` – Modernization opportunities across your
  infrastructure, application, data, security, and operations
  dimensions.

```
atx ct analysis run --type `type` --source `name` [--repo `source`::`repo`] [--wait]
atx ct analysis get --id `id` --json
atx ct analysis list --json
atx ct analysis list --status `pending|running|complete|cancelled|failed` --json
atx ct analysis list --type `type` --json
atx ct analysis cancel --id `id`
atx ct analysis delete --id `id` [--cascade-findings]
```

### Custom analysis

```
atx ct analysis run --type custom --transformation-name `name` --source `source` --repo `source`::`repo` --wait
```

Configuration with `-g` flag: key-value, JSON, or file path.

List TDs: `atx custom def list`

## Managing findings

```
atx ct findings list --json
atx ct findings list --repo `source`::`repo` --source `name` --severity `high|medium|low` --type `analysis-type` --status `open|dismissed|obsolete` --analysis-id `id` --fix-transform `transform-name` --json
```

### Finding statuses

- `open` — Active
- `dismissed` — Manually dismissed (requires reason)
- `obsolete` — System-set when re-analysis no longer produces the
  finding

```
atx ct findings update --id `id` --status dismissed --reason "`reason`"
atx ct findings update --id `id` --status open
atx ct findings batch-update --ids `id1`,`id2` --status dismissed --reason "`reason`"
atx ct findings get --id `id`
atx ct findings delete --id `id`
```

### Finding obsolescence

Re-analysis marks resolved findings as obsolete. Cannot be re-opened. Retained for
audit.

## Creating remediations

Three modes: findings-based, TD override, direct TD.

```
atx ct remediation create --ids `id1`,`id2` --name "`name`"
atx ct remediation create --ids `id1`,`id2` --transformation-name `TD`
atx ct remediation create --transformation-name `TD` --repo `source`::`repo`
```

Output by provider: GitHub PR, GitLab MR, Bitbucket PR, Local branch.

###### Note

Token must have write access for PR/MR creation.

Local execution with `--local` flag.

```
atx ct remediation create --transformation-name `TD` --repo `source`::`repo` -g "`additionalPlanContext=Upgrade to Node.js 22`"
atx ct remediation list
atx ct remediation status --id `id`
atx ct remediation retry --id `id`
atx ct remediation cancel --id `id`
atx ct remediation delete --id `id`
```

## Remote execution

By default, analyses and remediations run on your local machine. For larger portfolios,
you can offload work to remote infrastructure. You can run on AWS Transform-managed infrastructure
with nothing to provision (analyses only), or on infrastructure you provision and manage in
your AWS account—a persistent Amazon EC2 instance or AWS Batch (Fargate) jobs. The
`atx ct remote` commands provision, run, monitor, and tear down customer-managed
infrastructure. Regardless of where execution happens, you create all resources in your
AWS account and your source code stays under your control.

###### Note

Provisioning, updating, and tearing down infrastructure creates and modifies AWS CloudFormation
stacks and IAM roles, and requires administrator permissions. Pass `--ack` to
acknowledge this and skip the interactive prompt. Running analyses and remediations on
already-provisioned infrastructure uses least-privilege executor policies — see
[Tagging and access control](#ct-tagging "#ct-tagging") and the compute options in
[How AWS Transform continuous modernization works](continuous-modernization.md#ct-how-it-works "continuous-modernization.md#ct-how-it-works") for the managed policies
involved.

### Running on AWS Transform-managed infrastructure (no provisioning)

To run an analysis remotely without provisioning anything, use
`--mode aws-managed`. The submission goes to AWS Transform, which runs the analysis on
AWS Transform-managed infrastructure. There is no stack to provision, no networking to configure, and
no credentials to store in AWS Secrets Manager. The submission is the run. Choose the
AWS Region the workload runs in with `--region`.

```
# Run an analysis on AWS Transform-managed infrastructure
atx ct remote analysis --type `type` --mode aws-managed --sources `name` [--repos `repo1,repo2`] [--region `region`]

# Poll the submission (there is no remote status command in this mode)
atx ct analysis get --id `id` --json
```

This mode runs analyses only. It does not support remediation, the `custom`
analysis type, or local sources. Because there is no stack, the `--stack-name`,
`--tags`, `--existing-instance`, and `--batch-name` options
don't apply. A single submission covers up to 100 repositories. To cover larger scopes, split
them across multiple submissions with `--repos`. Unlike Amazon EC2 and Batch runs, you monitor
progress with `atx ct analysis get` rather than
`atx ct remote status`.

### Networking

Remote compute must run in private subnets. Discover existing networking or create a
new VPC before you provision:

```
# List VPCs, private subnets, and security groups in the current account and Region
atx ct remote network discover
atx ct remote network discover --vpc `vpc-id` --json

# Create a new VPC with private subnets, a NAT gateway, and a security group
atx ct remote network create --cidr `10.1.0.0/16` --ack
```

### Provisioning infrastructure

Deploy the Amazon EC2 or Batch stack. Omit `--execute` to preview the template or
changeset; add `--execute` to apply.

Provisioning creates the compute stack for the mode you choose, plus a scheduler
stack:

- **Batch** — an AWS Batch job queue and
  compute environment, a job definition with the continuous modernization container image,
  IAM roles for job execution, and a Lambda function for job submission. Batch requires a
  security group.
- **Amazon EC2** — a persistent Amazon EC2 instance with an
  IAM instance profile and a security group. If you omit `--securityGroup`, the
  stack creates a security group with no inbound rules; access is via SSM.
- **Scheduler** — an `atx-scheduler`
  stack (an Amazon EventBridge Scheduler schedule group and invocation role) used by
  recurring analyses. Pass `--skip-scheduler` to opt out.

```
# Preview, then deploy an EC2 stack
atx ct remote provision --mode ec2 --vpc `vpc-id` --subnets `subnet-a,subnet-b`
atx ct remote provision --mode ec2 --vpc `vpc-id` --subnets `subnet-a,subnet-b` --execute --ack

# Deploy a Batch stack
atx ct remote provision --mode batch --vpc `vpc-id` --subnets `subnet-a,subnet-b` --securityGroup `sg-id` --execute --ack

# Update an existing stack to the latest template, or tear it down
atx ct remote update --mode `ec2|batch` --execute --ack
atx ct remote teardown --mode `ec2|batch` --execute --ack
```

### Storing source credentials

Remote containers clone your repositories using tokens stored in AWS Secrets Manager.
Register a token for each SCM source before running remote analysis or remediation:

```
atx ct remote credentials --source `name` --token `token`
atx ct remote credentials --source `name` --remove
```

### Running remotely

Remote analysis runs one container for each repository; remote remediation runs one
container for each finding. Use `--sources`, `--repos`, and
`--labels` to control fan-out, and `--stack-name` or `--tags`
to select which provisioned stack to use.

```
# Run analysis across a source on Batch
atx ct remote analysis --type `type` --mode batch --sources `name` [--repos `repo1,repo2`] [--labels "`team:frontend`"]

# Run remediation for specific findings on EC2
atx ct remote remediation --mode ec2 --ids `id1,id2`
atx ct remote remediation --mode ec2 --sources `name` --min-severity high
```

### Monitoring and managing runs

```
# Check whether infrastructure is deployed
atx ct remote detect --mode `ec2|batch`

# Track a submission (Batch by batch ID, EC2 by group ID)
atx ct remote status --batch `batch-id` --stack-name `name`
atx ct remote status --group `ec2-group-id` --wait

# Resume a partially-failed Batch run (re-submits only incomplete repos).
# On resume, --batch-name takes the existing batch ID reported by "remote status --batch".
atx ct remote analysis --type `type` --mode batch --sources `name` --resume-incomplete --batch-name `batch-id`

# Cancel a running submission
atx ct remote cancel --mode batch --batch `batch-id` --stack-name `name`
atx ct remote cancel --mode ec2 --group `ec2-group-id`
```

## Scheduling recurring analysis

Use `atx ct schedule` to run analyses automatically on a recurring cadence.
You can schedule analyses but not remediations. Job options mirror
`atx ct remote analysis`. Schedules run remotely, in one of two ways:

- **AWS Transform-managed**
  (`--mode aws-managed`)—a server-side schedule that fires analyses on
  AWS Transform-managed infrastructure. There is no Amazon EventBridge schedule and nothing to
  provision. It requires an execution role (`--execution-role`) that AWS Transform assumes
  at each run (see [Execution role for AWS Transform-managed schedules](#ct-schedule-execution-role "#ct-schedule-execution-role")).
- **Customer-managed**
  (`--mode ec2|batch`)—an Amazon EventBridge Scheduler schedule in your account
  dispatches each run to a persistent Amazon EC2 instance or AWS Batch stack that you provision
  first (see [Remote execution](#ct-remote-execution "#ct-remote-execution")).

The `--recurrence` value accepts `daily`,
`weekly:`DAY`` (for example,
 `weekly:MONDAY`), or `monthly:`N`` where
`N` is a day from 1 to 28. Schedules on AWS Transform-managed infrastructure
run in UTC.

```
# AWS Transform-managed schedule (no infrastructure; requires an execution role)
atx ct schedule create --name `name` --mode aws-managed --execution-role `role-arn` --recurrence `daily` --type `type` --sources `name` [--repos `repo1,repo2`]

# Customer-managed schedule (EventBridge Scheduler dispatching to your EC2 or Batch stack)
atx ct schedule create --name `name` --mode `ec2|batch` --recurrence `weekly:MONDAY` --type `type` --sources `name` [--repos `repo1,repo2`]

# Manage schedules of either type by their schedule ID (from schedule list)
atx ct schedule list
atx ct schedule get `schedule-id`
atx ct schedule disable `schedule-id`
atx ct schedule enable `schedule-id`
atx ct schedule delete `schedule-id`
```

To view the analyses a schedule has run, use
`atx ct analysis list --schedule-id `schedule-id``, which
returns the schedule's fired runs, newest first.

To remove the scheduler role and schedule group used by customer-managed schedules, run
`atx ct schedule teardown --execute`.

### Execution role for AWS Transform-managed schedules

A schedule created with `--mode aws-managed` requires an
`--execution-role` ARN that AWS Transform assumes each time the schedule runs. Configure
the role as follows:

- The identity creating the schedule must have `iam:PassRole`
  permission on the execution role.
- The role's trust policy must allow the
  `transform-custom.amazonaws.com` service principal to assume it.
- At a minimum, the role must have the AWS managed policy
  [AWSTransformCustomFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSTransformCustomFullAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AWSTransformCustomFullAccess")
  attached, plus `secretsmanager:GetSecretValue` and
  `secretsmanager:DescribeSecret` permissions on secrets under the
  `atx/*` prefix so that scheduled runs can retrieve the source clone
  credentials.

The following inline policy grants the AWS Secrets Manager access that scheduled runs
need to retrieve source clone credentials. Attach it to the execution role alongside the
[AWSTransformCustomFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSTransformCustomFullAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AWSTransformCustomFullAccess")
managed policy, replacing `region` and
`account-id` with the AWS Region and account the schedule runs
in.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AtxSourceCredentials",
      "Effect": "Allow",
      "Action": [
        "secretsmanager:GetSecretValue",
        "secretsmanager:DescribeSecret"
      ],
      "Resource": "arn:aws:secretsmanager:`region`:`account-id`:secret:atx/*"
    }
  ]
}
```

## Tagging and access control

You can apply tags (comma-separated `key=value` pairs) to sources, analyses,
and remediations with the `--tags` option. Tags are also supported on remote
infrastructure, stored credentials, and networking resources. With tags, you can organize
resources. Combined with IAM tag conditions, tags implement attribute-based access control
(ABAC) so that teams access only the resources that carry their tags.

```
atx ct source add --name `name` --provider github --org `org` --token `pat` --tags `team=platform,env=prod`
atx ct analysis run --type `type` --source `name` --tags `team=platform`
atx ct remediation create --ids `id1,id2` --tags `team=platform`
```

By default, resources are tagged with the tags you define in
`~/.aws/atx/settings.json`. Add the tags you want applied to every resource under
`applyTags`, and they become your default tags.

```
{
  "applyTags": [
    { "team": "alpha" }
  ]
}
```

###### Note

Tags passed with `--tags` are merged over any configured default tags, and
`--tags` wins for any key set in both places.

## AWS Transform web application

Use the AWS Transform web application to create and run analyses, review findings, create
remediations, and track generated pull requests across your code sources.

Before you use the web application, your organization must enable your user identity to
access AWS Transform. For more information about setting up AWS Transform, see
[Setting up AWS Transform](transform-setup.md "transform-setup.md").

### Sign in

To access the AWS Transform web application, complete the following steps.

1. Open `https://aws.amazon.com/transform/` and sign in with
   AWS IAM Identity Center credentials.
2. If continuous modernization does not appear, sign in with IAM credentials
   instead:

   1. In the AWS Management Console, open AWS Transform and choose
      **Settings**.
   2. Turn on **Access AWS Transform with IAM
      credentials**.
   3. Copy the **Web application URL (with IAM)**
      and paste it into the same browser window where the console is
      open.

3. Open the left navigation menu and choose **continuous
   modernization**.

### Infrastructure modes

When you create an analysis, choose one of the following infrastructure modes:

- **AWS managed** – Run on infrastructure managed by
  AWS Transform. You don't need to provision any infrastructure.
- **Customer owned** – Run on a deployed stack in your own
  AWS account. Use this mode when you need control over compute, networking, or security
  configuration.

###### Note

To run security analysis, use customer-owned infrastructure. Security analysis
runs on the Security Agent deployed in your account.

To use customer-owned infrastructure, open the **Settings** tab.
Use the AWS CloudFormation quick-create links to deploy the following stacks in order:

1. `AtxDispatcherStack` – Message dispatcher (always
   required).
2. Compute stack – `AtxInfrastructureStack` (AWS Batch) or
   `atx-runner` (Amazon EC2).
3. `atx-scheduler` – Required for recurring scheduled
   analyses.
4. `AtxSecurityAgentStack-<region>` – Required only for
   security analysis.

For CLI-based provisioning and networking configuration, see
[Remote execution](#ct-remote-execution "#ct-remote-execution").

### Getting started workflow

1. **Connect sources** – Open the
   **Sources** tab and add repositories from GitHub,
   GitLab, or Bitbucket.
2. **Run or schedule an analysis** – Open the
   **Analyses** tab, select repositories, choose an analysis
   type, select an infrastructure mode, and choose **Run**. To run on a
   recurring cadence (daily, weekly, or monthly), choose **Schedule**
   instead.
3. **Review findings** – Open the
   **Findings** tab to view results by
   severity.
4. **Create a remediation** – Select findings
   and choose **Create remediation**.
5. **Review pull requests** – Open the
   **Remediations** tab to view generated PR links per
   repository.

Chat with AWS Transform directly from the web application to ask questions about your
analyses, findings, or remediations.
