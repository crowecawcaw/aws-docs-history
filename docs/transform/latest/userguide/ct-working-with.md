

# Working with continuous modernization
<a name="ct-working-with"></a>

## Source management
<a name="ct-source-management"></a>

Use `atx ct source` commands to connect repositories. Supported providers: GitHub, GitLab, Bitbucket, local.

### GitHub organizations
<a name="ct-source-github"></a>

Token: personal access token (classic) with `repo` scope. Read-only for analysis, full repo for remediation.

```
atx ct source add --name {{name}} --provider github --org {{org}} --token {{pat}}
```

### GitLab groups and users
<a name="ct-source-gitlab"></a>

Token: personal access token with `api` scope.

```
atx ct source add --name {{name}} --provider gitlab --org {{group-or-user}} --token {{pat}}
# Self-hosted:
atx ct source add --name {{name}} --provider gitlab --org {{group-or-user}} --token {{pat}} --url https://{{gitlab.example.com}}
```

### Bitbucket workspaces and projects
<a name="ct-source-bitbucket"></a>

Bitbucket Cloud — scopes: `read:repository:bitbucket`, `write:repository:bitbucket`, `read:pullrequest:bitbucket`, `write:pullrequest:bitbucket`. Also needs `--email` and `--username`.

```
atx ct source add --name {{name}} --provider bitbucket --org {{workspace}} --token {{api-token}} --email {{email}} --username {{username}}
```

Bitbucket Data Center:

```
atx ct source add --name {{name}} --provider bitbucket --org {{project-key}} --token {{http-access-token}} --url https://{{bitbucket.example.com}}
```

### Local repositories
<a name="ct-source-local"></a>

```
atx ct source add --name {{name}} --provider local --path {{parent-directory}}
```

**Important**  
`--path` must point to a parent directory containing git repos as subdirectories, not to a single repo.

### Managing sources
<a name="ct-managing-sources"></a>

```
atx ct source list
atx ct source remove --name {{name}}
```

## Repository discovery and management
<a name="ct-repository-discovery"></a>

```
atx ct discovery scan --source {{name}}
atx ct discovery status --source {{name}}
atx ct discovery scan --source {{name}} --path {{new-directory}}
```

After discovery:

```
atx ct repository list
atx ct repository list --source {{name}}
atx ct repository list --labels "{{team:frontend,priority:high}}"
atx ct repository update --source {{name}} --repo "{{source}}::{{repo}}" --labels "{{team:frontend,priority:high}}"
atx ct repository update --source {{name}} --labels "{{migration:wave-1}}"
```

## Running analysis
<a name="ct-running-analysis"></a>

The `--type` flag specifies the kind of analysis to run:
+ `rapid-techdebt-analysis` – Outdated dependencies and easy wins.
+ `tech-debt-comprehensive` – Deeper AI-powered analysis covering dependency, security, pattern, performance, maintainability, architecture, code-quality, and infrastructure findings.
+ `security` – Security vulnerabilities and exposures.
+ `agentic-readiness` – Readiness of your repositories for AI agents (frameworks, APIs, documentation).
+ `modernization-readiness` – Modernization opportunities across your infrastructure, application, data, security, and operations dimensions.

```
atx ct analysis run --type {{type}} --source {{name}} [--repo {{source}}::{{repo}}] [--wait]
atx ct analysis get --id {{id}} --json
atx ct analysis list --json
atx ct analysis list --status {{pending|running|complete|cancelled|failed}} --json
atx ct analysis list --type {{type}} --json
atx ct analysis cancel --id {{id}}
atx ct analysis delete --id {{id}} [--cascade-findings]
```

If you omit `--repo`, the command analyzes every repository under `--source`. To scope the run to specific repositories, pass `--repo` (comma-separated) — each a fully-qualified {{source}}::{{repo}}, or a bare name used with `--source`.

### Custom analysis
<a name="ct-custom-analysis"></a>

```
atx ct analysis run --type custom --transformation-name {{name}} --source {{source}} --repo {{source}}::{{repo}} --wait
```

Configuration with `-g` flag: key-value, JSON, or file path.

List TDs: `atx custom def list`

## Managing findings
<a name="ct-managing-findings"></a>

```
atx ct findings list --json
atx ct findings list --repo {{source}}::{{repo}} --source {{name}} --severity {{high|medium|low}} --type {{analysis-type}} --status {{open|dismissed|obsolete}} --analysis-id {{id}} --fix-transform {{transform-name}} --json
```

### Finding statuses
<a name="ct-finding-statuses"></a>
+ `open` — Active
+ `dismissed` — Manually dismissed (requires reason)
+ `obsolete` — System-set when re-analysis no longer produces the finding

```
atx ct findings update --id {{id}} --status dismissed --reason "{{reason}}"
atx ct findings update --id {{id}} --status open
atx ct findings batch-update --ids {{id1}},{{id2}} --status dismissed --reason "{{reason}}"
atx ct findings get --id {{id}}
atx ct findings delete --id {{id}}
```

### Finding obsolescence
<a name="ct-finding-obsolescence"></a>

Re-analysis marks resolved findings as obsolete. Cannot be re-opened. Retained for audit.

## Creating remediations
<a name="ct-creating-remediations"></a>

Three modes: findings-based, TD override, direct TD.

```
atx ct remediation create --ids {{id1}},{{id2}} --name "{{name}}"
atx ct remediation create --ids {{id1}},{{id2}} --transformation-name {{TD}}
atx ct remediation create --transformation-name {{TD}} --repo {{source}}::{{repo}}
```

Output by provider: GitHub PR, GitLab MR, Bitbucket PR, Local branch.

**Note**  
Token must have write access for PR/MR creation.

Local execution with `--local` flag.

```
atx ct remediation create --transformation-name {{TD}} --repo {{source}}::{{repo}} -g "{{additionalPlanContext=Upgrade to Node.js 22}}"
atx ct remediation list
atx ct remediation status --id {{id}}
atx ct remediation retry --id {{id}}
atx ct remediation cancel --id {{id}}
atx ct remediation delete --id {{id}}
```

## Remote execution
<a name="ct-remote-execution"></a>

By default, analyses and remediations run on your local machine. For larger portfolios, you can offload work to remote infrastructure. You can run on AWS Transform-managed infrastructure with nothing to provision (analyses only), or on infrastructure you provision and manage in your AWS account—a persistent Amazon EC2 instance or AWS Batch (Fargate) jobs. The `atx ct remote` commands provision, run, monitor, and tear down customer-managed infrastructure. Regardless of where execution happens, you create all resources in your AWS account and your source code stays under your control.

With the `atx ct remote` analysis and remediation commands, you choose which repositories to process using `--sources` and `--repos` (both comma-separated). `--sources` selects every repository in the named sources. `--repos` selects specific repositories, each written as {{source}}::{{repo}}. If you provide both, the command processes the union of the two sets: every repository in the named sources, plus the named repositories. To scope a run to specific repositories, pass only `--repos`.

**Note**  
Provisioning, updating, and tearing down infrastructure creates and modifies AWS CloudFormation stacks and IAM roles, and requires administrator permissions. Pass `--ack` to acknowledge this and skip the interactive prompt. Running analyses and remediations on already-provisioned infrastructure uses least-privilege executor policies — see [Tagging and access control](#ct-tagging) and the compute options in [How AWS Transform continuous modernization works](continuous-modernization.md#ct-how-it-works) for the managed policies involved.

### Running on AWS Transform-managed infrastructure (no provisioning)
<a name="ct-remote-aws-managed"></a>

To run an analysis remotely without provisioning anything, use `--mode aws-managed`. The submission goes to AWS Transform, which runs the analysis on AWS Transform-managed infrastructure. There is no stack to provision, no networking to configure, and no credentials to store in AWS Secrets Manager. The submission is the run. Choose the AWS Region the workload runs in with `--region`.

```
# Run an analysis on AWS Transform-managed infrastructure
atx ct remote analysis --type {{type}} --mode aws-managed --sources {{name}} [--repos {{repo1,repo2}}] [--region {{region}}]

# Poll the submission (there is no remote status command in this mode)
atx ct analysis get --id {{id}} --json
```

This mode runs analyses only. It does not support remediation, the `custom` analysis type, or local sources. Because there is no stack, the `--stack-name`, `--tags`, `--existing-instance`, and `--batch-name` options don't apply. A single submission covers up to 100 repositories. To cover larger scopes, split them across multiple submissions with `--repos`. Unlike Amazon EC2 and Batch runs, you monitor progress with `atx ct analysis get` rather than `atx ct remote status`.

### Networking
<a name="ct-remote-network"></a>

Remote compute must run in private subnets. Discover existing networking or create a new VPC before you provision:

```
# List VPCs, private subnets, and security groups in the current account and Region
atx ct remote network discover
atx ct remote network discover --vpc {{vpc-id}} --json

# Create a new VPC with private subnets, a NAT gateway, and a security group
atx ct remote network create --cidr {{10.1.0.0/16}} --ack
```

`--cidr` is optional and defaults to `10.1.0.0/16`.

Whether you bring your own network or use `network create`, it must meet these requirements:
+ **Private subnets in two Availability Zones** — provisioning rejects public subnets (a subnet whose route table has a default route to an internet gateway). Provide at least two private subnets in different Availability Zones. AWS Batch spreads jobs across all of them. Amazon EC2 uses the first subnet.
+ **Outbound internet through a NAT gateway** — jobs run in private subnets. They need outbound access to pull the container image from public Amazon ECR and to reach AWS Transform and other AWS APIs. Each private subnet's route table must send `0.0.0.0/0` to a NAT gateway in a public subnet. You can instead reach AWS APIs over interface endpoints — see [AWS Transform custom and interface endpoints (AWS PrivateLink)](vpc-interface-endpoints-transform-custom.md).
+ **Security group with outbound access** — the security group needs only outbound (egress) rules. No inbound rules are required. AWS Batch requires you to pass `--securityGroup` at provision time. For Amazon EC2, if you omit `--securityGroup` the stack creates an egress-only security group with no inbound rules, and you reach the instance through SSM. A group that allows all outbound traffic (the default for a new security group) is sufficient.
+ **Enough free IP addresses** — each running AWS Batch (Fargate) job uses one private IP address from a subnet. An Amazon EC2 instance uses one private IP address in total, no matter how many workers it runs. Size the subnets for the number of jobs you run in parallel. If a subnet runs low on addresses, jobs can fail with `InsufficientFreeAddressesInSubnet`. If you use `network create`, subnet size scales with the VPC CIDR. The VPC must be `/26` or larger. The default `10.1.0.0/16` produces `/24` subnets. For the arithmetic, the concurrency limit for each analysis type, and minimum subnet sizes, see [Sizing subnets and concurrency](#ct-remote-sizing).

### Sizing subnets and concurrency
<a name="ct-remote-sizing"></a>

Before you provision AWS Batch infrastructure for a large repository fleet, size your private subnets for the number of jobs that run in parallel. A subnet that is too small is the most common cause of failed jobs in a large run.

Each AWS Batch job runs as one Fargate task, which needs one elastic network interface and therefore **one private IPv4 address**. Public IP address assignment is disabled, so a private address is required — a job cannot start without one. AWS Batch does not queue a job it cannot place; it fails the job.

**Important**  
Free addresses do not add up across subnets. AWS Transform treats your available capacity as the **smallest** number of free addresses in any one of the subnets you pass to `--subnets`, not the total across them. Two `/28` subnets give you 11 concurrent jobs, not 22. Adding a subnet never raises capacity, and adding a small subnet lowers it. Give every subnet in the stack enough free addresses on its own.

#### Checking free addresses before you provision
<a name="ct-remote-sizing-check"></a>

Provisioning does not check subnet capacity for you. Check it yourself with `--json`, which reports `availableIpCount` for each subnet. The default table output does not include this value. Compare the **smallest** count against the concurrency limit for the analysis type you plan to run.

```
atx ct remote network discover --vpc {{vpc-id}} --json
```

#### Concurrency limits for each analysis type
<a name="ct-remote-sizing-limits"></a>

AWS Transform limits how many remote jobs run at the same time in an AWS account and Region. The limit depends on the analysis type. These limits are shared across all users in the account and across both compute modes, and they cap the number of addresses a run can consume. To request a change, contact AWS Support.


| Analysis type | Concurrent jobs | 
| --- | --- | 
| `security` | 5 | 
| `tech-debt-quick` | 128 | 
| `tech-debt-comprehensive`, `agentic-readiness`, `modernization-readiness`, and `custom` analysis, and remediation other than security remediation | 30, shared across all of these | 
| Security remediation | 128 | 

**Note**  
The types in the third row share a single pool of 30 jobs. Running a comprehensive tech-debt analysis and a custom remediation at the same time gives you 30 jobs in total, not 60.

#### Minimum subnet size
<a name="ct-remote-sizing-table"></a>

Amazon VPC reserves five addresses in every subnet, so the usable count is five fewer than the subnet size — a `/28` has 11 usable addresses and a `/24` has 251. For details, see [Subnet CIDR blocks](https://docs.aws.amazon.com/vpc/latest/userguide/subnet-sizing.html) in the *Amazon VPC User Guide*.

The addresses each subnet needs are the peak concurrent jobs, plus one or more for each interface endpoint in that subnet, plus any other network interfaces that share the subnet. Peak concurrent jobs is the smaller of the number of repositories in the submission and the concurrency limit for the analysis type. Because the limit caps the total, a 1,000-repository fleet needs no more addresses than a 128-repository one.


| Analysis type | Peak concurrent jobs | Minimum subnet size | 
| --- | --- | --- | 
| `security` | 5 | `/27` | 
| `tech-debt-comprehensive`, `agentic-readiness`, `modernization-readiness`, `custom` | 30 | `/26` | 
| `tech-debt-quick` | Up to 128 | `/24` | 
| Every type running at its limit at once | 291 | `/23` | 

The minimums above include headroom for interface endpoints and for the addresses AWS reserves. Size up if other workloads share the subnet. A `/25` is not enough for 128 concurrent jobs: it provides 128 addresses but only 123 usable ones.

We recommend dedicating subnets to remote execution. AWS Transform admits jobs down to the last free address and cannot account for other workloads that claim addresses in the same subnet.

#### Running large fleets
<a name="ct-remote-sizing-large-fleets"></a>

A single submission covers up to 100 repositories. Submissions above that limit are rejected before any job starts, so a 1,000-repository fleet needs at least 10 submissions. Split them with `--repos`, and list the repositories in a source with `atx ct repository list --source {{name}} --json`.

Splitting a fleet does not reduce the addresses you need. Submissions that run at the same time draw from the same subnets, up to the concurrency limit for the analysis type.

There is no option that limits how many repositories are scanned at once. The CLI submits every job in a submission, and AWS Transform releases jobs up to the concurrency limit for the analysis type and holds the rest. To pace a large fleet, size the subnets for that limit and submit in groups of 100 repositories or fewer.

#### Choosing Amazon EC2 for constrained networks
<a name="ct-remote-sizing-ec2"></a>

Amazon EC2 uses one private IP address in total, in the first subnet you pass, no matter how many workers the instance runs. If free addresses are scarce, Amazon EC2 avoids the problem entirely.

The tradeoff is concurrency: `--workers` accepts 1–5, so an Amazon EC2 instance runs at most 5 repositories in parallel. For fleets that need more, use AWS Batch. For `security` analysis the account limit is also 5, so AWS Batch offers no additional concurrency for that type.

Size `--workers`, `--instance-type`, and `--volume-size` when you provision. Instance memory must be at least 2 GB for each worker plus 4 GB for the operating system. `atx ct remote update` keeps these values; changing them requires tearing down and provisioning again, which replaces the instance and deletes its volume.

### Provisioning infrastructure
<a name="ct-remote-provision"></a>

Deploy the Amazon EC2 or AWS Batch stack. Omit `--execute` to preview the template or changeset; add `--execute` to apply.

Provisioning creates the compute stack for the mode you choose, plus dispatcher and scheduler stacks:
+ **AWS Batch** — a job queue and compute environment, a job definition with the continuous modernization container image, IAM roles for job execution, and a Lambda function for job submission. AWS Batch requires a security group.
+ **Amazon EC2** — a persistent Amazon EC2 instance with an IAM instance profile and a security group. If you omit `--securityGroup`, the stack creates a security group with no inbound rules; access is via SSM.
+ **Dispatcher** — an `AtxDispatcherStack` stack that queues jobs and dispatches them to your compute stack. It is always required. Provisioning creates it, and `update` reconciles it to the latest template. Pass `--skip-dispatcher` on `update` to skip that reconcile. The dispatcher is not removed. For information about how `update` affects a custom image, see [Container image](#ct-remote-image).
+ **Scheduler** — an `atx-scheduler` stack (an Amazon EventBridge Scheduler schedule group and invocation role) used by recurring analyses. Pass `--skip-scheduler` to opt out.

By default, Amazon EC2 stacks are named `atx-runner` and AWS Batch stacks are named `AtxInfrastructureStack`. To run more than one stack of the same mode, give each a distinct name when you provision: use `--stack-name` (Amazon EC2 only; the name must start with `atx-runner`) or `--suffix` to append a suffix to all resource names. For `update`, `detect`, and remote analyses or remediations, pass `--stack-name` to target a custom-named stack. If you omit it, they use the default name (`atx-runner` for Amazon EC2, `AtxInfrastructureStack` for AWS Batch). `teardown` always requires `--stack-name`. On Amazon EC2, `--workers` sets the number of parallel worker containers (1-5, default 5) and sizes the instance.

```
# Preview, then deploy an EC2 stack
atx ct remote provision --mode ec2 --vpc {{vpc-id}} --subnets {{subnet-a,subnet-b}}
atx ct remote provision --mode ec2 --vpc {{vpc-id}} --subnets {{subnet-a,subnet-b}} --execute --ack

# Deploy a Batch stack
atx ct remote provision --mode batch --vpc {{vpc-id}} --subnets {{subnet-a,subnet-b}} --securityGroup {{sg-id}} --execute --ack

# Update to the latest template (--stack-name optional; defaults to the standard stack name)
atx ct remote update --mode {{ec2|batch}} [--stack-name {{stack-name}}] --execute --ack

# Tear down (--stack-name required)
atx ct remote teardown --mode {{ec2|batch}} --stack-name {{stack-name}} --execute --ack
```

### Container image
<a name="ct-remote-image"></a>

When you run remote analyses and remediations, they execute inside a container image. By default, when you provision a remote environment, it uses the public AWS Transform image, `public.ecr.aws/d9h8z6l7/aws-transform:latest`. AWS Batch sets it as the job definition image. Amazon EC2 uses it as the runner image.

To run a different image—for example, a private Amazon ECR image that bundles additional languages or tools—pass `--image-uri` when you provision:

```
# Batch: provision with a custom image
atx ct remote provision --mode batch --vpc {{vpc-id}} --subnets {{subnet-a,subnet-b}} --securityGroup {{sg-id}} --image-uri {{account-id}}.dkr.ecr.{{region}}.amazonaws.com/{{repo}}:{{tag}} --execute --ack

# EC2: provision with a custom image
atx ct remote provision --mode ec2 --vpc {{vpc-id}} --subnets {{subnet-a,subnet-b}} --image-uri {{account-id}}.dkr.ecr.{{region}}.amazonaws.com/{{repo}}:{{tag}} --execute --ack
```

**Note**  
A later `atx ct remote update` (see [Provisioning infrastructure](#ct-remote-provision)) resets the image to the template default. To keep a custom image, re-run `provision` with `--image-uri` after you update.

### Storing source credentials
<a name="ct-remote-credentials"></a>

Remote containers clone your repositories using tokens stored in AWS Secrets Manager. Register a token for each SCM source before running remote analysis or remediation:

```
atx ct remote credentials --source {{name}} --token {{token}}
atx ct remote credentials --source {{name}} --remove
```

### Running remotely
<a name="ct-remote-run"></a>

Remote analysis runs one container for each repository; remote remediation runs one container for each finding. Use `--sources`, `--repos`, and `--labels` to control fan-out, and `--stack-name` or `--tags` to select which provisioned stack to use.

```
# Run analysis across a source on Batch
atx ct remote analysis --type {{type}} --mode batch --sources {{name}} [--repos {{repo1,repo2}}] [--labels "{{team:frontend}}"]

# Run remediation for specific findings on EC2
atx ct remote remediation --mode ec2 --ids {{id1,id2}}
atx ct remote remediation --mode ec2 --sources {{name}} --min-severity high
```

### Monitoring and managing runs
<a name="ct-remote-monitor"></a>

```
# Check whether infrastructure is deployed
atx ct remote detect --mode {{ec2|batch}}

# Track a submission (Batch by batch ID, EC2 by group ID)
atx ct remote status --batch {{batch-id}} --stack-name {{name}}
atx ct remote status --group {{ec2-group-id}} --wait

# Resume a partially-failed Batch run (re-submits only incomplete repos).
# On resume, --batch-name takes the existing batch ID reported by "remote status --batch".
atx ct remote analysis --type {{type}} --mode batch --sources {{name}} --resume-incomplete --batch-name {{batch-id}}

# Cancel a running submission
atx ct remote cancel --mode batch --batch {{batch-id}} --stack-name {{name}}
atx ct remote cancel --mode ec2 --group {{ec2-group-id}}
```

## Scheduling recurring analysis
<a name="ct-scheduling"></a>

Use `atx ct schedule` to run analyses automatically on a recurring cadence. You can schedule analyses but not remediations. Job options mirror `atx ct remote analysis`. Schedules run remotely, in one of two ways:
+ **AWS Transform-managed** (`--mode aws-managed`)—a server-side schedule that fires analyses on AWS Transform-managed infrastructure. There is no Amazon EventBridge schedule and nothing to provision. It requires an execution role (`--execution-role`) that AWS Transform assumes at each run (see [Execution role for AWS Transform-managed schedules](#ct-schedule-execution-role)).
+ **Customer-managed** (`--mode ec2|batch`)—an Amazon EventBridge Scheduler schedule in your account dispatches each run to a persistent Amazon EC2 instance or AWS Batch stack that you provision first (see [Remote execution](#ct-remote-execution)).

The `--recurrence` value accepts `daily`, `weekly:{{DAY}}` (for example, `weekly:MONDAY`), or `monthly:{{N}}` where {{N}} is a day from 1 to 28. Schedules on AWS Transform-managed infrastructure run in UTC.

```
# AWS Transform-managed schedule (no infrastructure; requires an execution role)
atx ct schedule create --name {{name}} --mode aws-managed --execution-role {{role-arn}} --recurrence {{daily}} --type {{type}} --sources {{name}} [--repos {{repo1,repo2}}]

# Customer-managed schedule (EventBridge Scheduler dispatching to your EC2 or Batch stack)
atx ct schedule create --name {{name}} --mode {{ec2|batch}} --recurrence {{weekly:MONDAY}} --type {{type}} --sources {{name}} [--repos {{repo1,repo2}}]

# Manage schedules of either type by their schedule ID (from schedule list)
atx ct schedule list
atx ct schedule get {{schedule-id}}
atx ct schedule disable {{schedule-id}}
atx ct schedule enable {{schedule-id}}
atx ct schedule delete {{schedule-id}}
```

To view the analyses a schedule has run, use `atx ct analysis list --schedule-id {{schedule-id}}`, which returns the schedule's fired runs, newest first.

To remove the scheduler role and schedule group used by customer-managed schedules, run `atx ct schedule teardown --execute`.

### Execution role for AWS Transform-managed schedules
<a name="ct-schedule-execution-role"></a>

A schedule created with `--mode aws-managed` requires an `--execution-role` ARN that AWS Transform assumes each time the schedule runs. Configure the role as follows:
+ The identity creating the schedule must have `iam:PassRole` permission on the execution role.
+ The role's trust policy must allow the `transform-custom.amazonaws.com` service principal to assume it.
+ At a minimum, the role must have the AWS managed policy [`AWSTransformCustomFullAccess`](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSTransformCustomFullAccess) attached, plus `secretsmanager:GetSecretValue` and `secretsmanager:DescribeSecret` permissions on secrets under the `atx/*` prefix so that scheduled runs can retrieve the source clone credentials.

The following inline policy grants the AWS Secrets Manager access that scheduled runs need to retrieve source clone credentials. Attach it to the execution role alongside the [`AWSTransformCustomFullAccess`](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSTransformCustomFullAccess) managed policy, replacing {{region}} and {{account-id}} with the AWS Region and account the schedule runs in.

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
      "Resource": "arn:aws:secretsmanager:{{region}}:{{account-id}}:secret:atx/*"
    }
  ]
}
```

## Tagging and access control
<a name="ct-tagging"></a>

You can apply tags (comma-separated `key=value` pairs) to sources, analyses, and remediations with the `--tags` option. Tags are also supported on remote infrastructure, stored credentials, and networking resources. With tags, you can organize resources. Combined with IAM tag conditions, tags implement attribute-based access control (ABAC) so that teams access only the resources that carry their tags.

```
atx ct source add --name {{name}} --provider github --org {{org}} --token {{pat}} --tags {{team=platform,env=prod}}
atx ct analysis run --type {{type}} --source {{name}} --tags {{team=platform}}
atx ct remediation create --ids {{id1,id2}} --tags {{team=platform}}
```

By default, resources are tagged with the tags you define in `~/.aws/atx/settings.json`. Add the tags you want applied to every resource under `applyTags`, and they become your default tags.

```
{
  "applyTags": [
    { "team": "alpha" }
  ]
}
```

**Note**  
Tags passed with `--tags` are merged over any configured default tags, and `--tags` wins for any key set in both places.

## AWS Transform web application
<a name="ct-web-application"></a>

Use the AWS Transform web application to create and run analyses, review findings, create remediations, and track generated pull requests across your code sources.

Before you use the web application, your organization must enable your user identity to access AWS Transform. For more information about setting up AWS Transform, see [Setting up AWS Transform](https://docs.aws.amazon.com/transform/latest/userguide/transform-setup.html).

### Sign in
<a name="ct-web-application-sign-in"></a>

To access the AWS Transform web application, complete the following steps.

1. Open `https://aws.amazon.com/transform/` and sign in with AWS IAM Identity Center credentials.

1. If continuous modernization does not appear, sign in with IAM credentials instead:

   1. In the AWS Management Console, open AWS Transform and choose **Settings**.

   1. Turn on **Access AWS Transform with IAM credentials**.

   1. Copy the **Web application URL (with IAM)** and paste it into the same browser window where the console is open.

1. Open the left navigation menu and choose **continuous modernization**.

### Infrastructure modes
<a name="ct-web-application-prerequisites"></a>

When you create an analysis, choose one of the following infrastructure modes:
+ **AWS managed** – Run on infrastructure managed by AWS Transform. You don't need to provision any infrastructure.
+ **Customer owned** – Run on a deployed stack in your own AWS account. Use this mode when you need control over compute, networking, or security configuration.

**Note**  
To run security analysis, use customer-owned infrastructure. Security analysis runs on the Security Agent deployed in your account.

To use customer-owned infrastructure, open the **Settings** tab. Use the AWS CloudFormation quick-create links to deploy the following stacks in order:

1. `AtxDispatcherStack` – Message dispatcher (always required).

1. Compute stack – `AtxInfrastructureStack` (AWS Batch) or `atx-runner` (Amazon EC2).

1. `atx-scheduler` – Required for recurring scheduled analyses.

1. `AtxSecurityAgentStack-<region>` – Required only for security analysis.

For CLI-based provisioning and networking configuration, see [Remote execution](#ct-remote-execution).

### Getting started workflow
<a name="ct-web-application-workflow"></a>

1. **Connect sources** – Open the **Sources** tab and add repositories from GitHub, GitLab, or Bitbucket.

1. **Run or schedule an analysis** – Open the **Analyses** tab, select repositories, choose an analysis type, select an infrastructure mode, and choose **Run**. To run on a recurring cadence (daily, weekly, or monthly), choose **Schedule** instead.

1. **Review findings** – Open the **Findings** tab to view results by severity.

1. **Create a remediation** – Select findings and choose **Create remediation**.

1. **Review pull requests** – Open the **Remediations** tab to view generated PR links per repository.

Chat with AWS Transform directly from the web application to ask questions about your analyses, findings, or remediations.