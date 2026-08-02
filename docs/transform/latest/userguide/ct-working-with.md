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
you can offload work to remote infrastructure in your AWS account — a persistent Amazon EC2
instance or AWS Batch (Fargate) jobs. The `atx ct remote` commands provision,
run, monitor, and tear down this infrastructure. Regardless of where execution happens, your
source code stays under your control in your account.

###### Note

Provisioning, updating, and tearing down infrastructure creates and modifies AWS CloudFormation
stacks and IAM roles, and requires administrator permissions. Pass `--ack` to
acknowledge this and skip the interactive prompt. Running analyses and remediations on
already-provisioned infrastructure uses least-privilege executor policies — see
[Tagging and access control](#ct-tagging "#ct-tagging") and the compute options in
[How AWS Transform continuous modernization works](continuous-modernization.md#ct-how-it-works "continuous-modernization.md#ct-how-it-works") for the managed policies
involved.

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
atx ct remote analysis --type `type` --mode batch --sources `name` --resume --batch-name `batch-id`

# Cancel a running submission
atx ct remote cancel --mode batch --batch `batch-id` --stack-name `name`
atx ct remote cancel --mode ec2 --group `ec2-group-id`
```

## Scheduling recurring analysis

Use `atx ct schedule` to run analyses automatically on a recurring cadence
with Amazon EventBridge Scheduler. Only analyses can be scheduled; remediations are not
scheduled. Scheduling runs on remote infrastructure, so provision an Amazon EC2 or Batch stack
first (see [Remote execution](#ct-remote-execution "#ct-remote-execution")). Job
options mirror `atx ct remote analysis`.

The `--recurrence` value accepts `daily`,
`weekly:`DAY`` (for example,
 `weekly:MONDAY`), or `monthly:`N`` where
`N` is a day from 1 to 28.

```
atx ct schedule create --name `name` --mode `ec2|batch` --recurrence `weekly:MONDAY` --type `type` --sources `name` [--repos `repo1,repo2`]
atx ct schedule list
atx ct schedule get `name`
atx ct schedule disable `name`
atx ct schedule enable `name`
atx ct schedule delete `name`
```

To remove the scheduler role and schedule group entirely, run
`atx ct schedule teardown --execute`.

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

## AWS Transform web application (Optional)

The AWS Transform web application is an optional interface for monitoring continuous
modernization analyses, findings, and remediations across your portfolio of code
sources.

Before using the AWS Transform web application, you need to have a user identity enabled to
access AWS Transform in your organization. For information about enabling AWS Transform, see
[Setting up AWS Transform](transform-setup.md "transform-setup.md").

To use the AWS Transform web application:

1. Visit `https://aws.amazon.com/transform/` and sign in using
   AWS IAM Identity Center credentials.
2. If continuous modernization does not appear after you sign in, sign in with
   IAM credentials instead. To enable IAM credentials sign-in:

   1. In the AWS Management Console, open AWS Transform and choose
      **Settings**.
   2. In the **Access AWS Transform with IAM credentials**
      section, enable IAM credentials access.
   3. On the same settings page, copy the sign-in link shown under
      **Web application URL (with IAM)**.
   4. Paste the sign-in URL into the same browser window where the AWS
      Management Console is open. This ensures the web application uses the AWS credentials
      from that account.

3. Open the left navigation menu and choose **continuous
   modernization**. The Dashboard displays summary statistics including sources,
   repositories, total findings by severity, and analysis types.
4. Use the **Analyses**,
   **Findings**, and
   **Remediations** tabs to view detailed
   results.
5. Chat with AWS Transform directly from the web application to ask questions about
   your analyses, findings, or remediations.

The web application is designed for enterprise-scale operations where you need
centralized visibility into continuous modernization analyses and remediations across multiple
codebases.
