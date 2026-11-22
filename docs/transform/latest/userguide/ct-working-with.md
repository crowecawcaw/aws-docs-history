

# Working with continuous modernization

## Source management
<a name="ct-source-management"></a>

Use `atx ct source` commands to connect repositories. Supported providers: GitHub, GitLab, Bitbucket, local.

GitHub and GitLab sources authenticate either with a personal access token, described per provider below, or with OAuth. See [Connecting with OAuth](#ct-source-oauth).

### GitHub organizations
<a name="ct-source-github"></a>

Token: personal access token (classic) with `repo` scope. Read-only for analysis, full repo for remediation.

```bash
atx ct source add --name {{name}} --provider github --org {{org}} --token {{pat}}
```

**Note**  
The `--url` flag is supported for self-hosted GitLab or Bitbucket only.

### GitLab groups and users
<a name="ct-source-gitlab"></a>

Token: personal access token with `api` scope.

```bash
atx ct source add --name {{name}} --provider gitlab --org {{group-or-user}} --token {{pat}}
# Self-hosted:
atx ct source add --name {{name}} --provider gitlab --org {{group-or-user}} --token {{pat}} --url https://{{gitlab.example.com}}
```

### Bitbucket workspaces and projects
<a name="ct-source-bitbucket"></a>

Bitbucket Cloud — scopes: `read:repository:bitbucket`, `write:repository:bitbucket`, `read:pullrequest:bitbucket`, `write:pullrequest:bitbucket`. Also needs `--email` and `--username`.

```bash
atx ct source add --name {{name}} --provider bitbucket --org {{workspace}} --token {{api-token}} --email {{email}} --username {{username}}
```

Bitbucket Data Center:

```bash
atx ct source add --name {{name}} --provider bitbucket --org {{project-key}} --token {{http-access-token}} --url https://{{bitbucket.example.com}}
```

### Local repositories
<a name="ct-source-local"></a>

```bash
atx ct source add --name {{name}} --provider local --path {{parent-directory}}
```

**Important**  
`--path` must point to a parent directory containing git repos as subdirectories, not to a single repo.

### Connecting with OAuth
<a name="ct-source-oauth"></a>

Instead of a personal access token, connect a GitHub or GitLab source with OAuth. You sign in through your browser with the AWS Transform app, and no token is requested or stored. AWS Transform clones and pushes through its own git endpoint, using a short-lived credential that AWS Transform mints for each request.

Connect an OAuth source with the CLI, or from the AWS Transform web application. For the web application steps, see [Connecting with OAuth in the web application](#ct-web-application-oauth). Connecting an OAuth source from the CLI requires AWS Transform CLI version 3.25.0 or later.

Your own permissions to add and connect a source are the ones described in [Setting up AWS Transform](https://docs.aws.amazon.com/transform/latest/userguide/transform-setup.html). Scheduled and remote analyses run under an execution role instead of your own identity, and that role needs permission to read a repository's content through the source, and to write it when a remediation opens a pull request. A role that predates OAuth support has neither, so a scheduled or remote run on an OAuth source fails to clone until the role's permissions are updated. For how to grant them, see [Setting up AWS Transform](https://docs.aws.amazon.com/transform/latest/userguide/transform-setup.html).

The following AWS Transform CLI commands connect a source with OAuth in each of the supported cases. Replace {{name}}, {{org}}, and {{login}} with your own values:

```bash
# GitHub organization that already has the AWS Transform app installed
atx ct source add --name {{name}} --provider github --auth oauth --org {{org}}

# GitHub personal account that already has the app installed
atx ct source add --name {{name}} --provider github --auth oauth --user {{login}}

# GitHub, naming neither: opens the app's install page
atx ct source add --name {{name}} --provider github --auth oauth

# GitLab (gitlab.com only, and no organization or user to name)
atx ct source add --name {{name}} --provider gitlab --auth oauth

# Finish, or repeat, the connection for a source that already exists
atx ct source connect --name {{name}}
```

`atx ct source add --auth oauth` creates the source and connects it in one step. If the connection doesn't finish, AWS Transform still creates the source, with a disconnected status, and `atx ct source connect --name {{name}}` completes it. Use the same command to reconnect a source at any time.

**Important**  
The browser must run on the same machine as the CLI. The command opens the provider's sign-in page and receives the result on a one-time listener on `127.0.0.1`, so it doesn't work over a terminal-only session unless you forward that port.

When you name neither `--org` nor `--user`, the command opens the app's install page. The page always lists your personal account and every organization you have access to. Each entry shows **Configure** when that account or organization already has the app, and is empty when it doesn't.

If you don't complete a new installation, the connection has nothing to return, and AWS Transform creates the source with a disconnected status. Connect it by naming the organization or account: `atx ct source connect --name {{name}} --org {{org}}`.

When a connection from the CLI succeeds, the browser confirms that you can close the tab and return to the terminal, and the CLI prints the connected account and the source's status.

A source belongs to one AWS account and one AWS Region. Connect the source in each AWS Region where you run continuous modernization.

**Note**  
If the AWS Transform app is uninstalled and installed again on the provider, run `atx ct source connect` for each source that uses it. Installing the app again replaces the installation the source recorded, and requests for that source fail until you reconnect.

To stop AWS Transform reaching your repositories, remove the access at the provider as well as removing the source. On GitHub, uninstall the AWS Transform app from the organization or account. On GitLab, revoke the aws-transform-custom authorization in your account settings. Then remove the source with `atx ct source remove --name {{name}}`; see [Managing sources](#ct-managing-sources). Revoking access without removing the source leaves the source in place and its requests failing, in the same way the note above describes.

Use OAuth with gitlab.com, where it covers the projects your GitLab account is a member of. For a self-managed GitLab host, use a personal access token with `--url` instead.

### Repository conventions
<a name="ct-source-conventions"></a>

Repositories can enforce rules that reject a push at the end of a remediation — a required commit message format (GitLab push rules, Bitbucket commit hooks, GitHub rulesets), a restricted branch namespace, or a known commit author. Record those conventions on the source so remediation commits and result branches are written in the shape the repositories require. Each option is available on both `atx ct source add` and `atx ct source update`.

```bash
# Commit message format ({PLACEHOLDER} is replaced with a description of each change)
atx ct source update --name {{name}} --commit-message-template "fix: {PLACEHOLDER}"

# Branch namespace ({PLACEHOLDER} is replaced with the branch name AWS Transform generates)
atx ct source update --name {{name}} --branch-name-template "customized/{PLACEHOLDER}"

# Git committer identity (both options are required together)
atx ct source update --name {{name}} --git-committer-name "{{ATX Automation}}" --git-committer-email {{atx-automation@example.com}}
```

Pass an empty string to remove a template or to clear the committer pair. The options apply to security and transformation remediations, and to local sources whose repositories you push by hand.

### Managing sources
<a name="ct-managing-sources"></a>

```bash
atx ct source list
atx ct source update --name {{name}} --token {{new-token}}
atx ct source remove --name {{name}}
```

`atx ct source update` accepts any combination of `--token` and the repository convention options above; passing no options is an error. You can update a source from any machine, not just the host that ran `atx ct source add`.

## Repository discovery and management
<a name="ct-repository-discovery"></a>

```bash
atx ct discovery scan --source {{name}}
atx ct discovery status --source {{name}}
atx ct discovery scan --source {{name}} --path {{new-directory}}
```

After discovery:

```bash
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
+ `security` – Static application security testing (SAST) for insecure coding patterns in source code.
+ `agentic-readiness` – Readiness of your repositories for AI agents (frameworks, APIs, documentation).
+ `modernization-readiness` – Modernization opportunities across your infrastructure, application, data, security, and operations dimensions.
+ `graviton-readiness` – AWS Graviton (Arm64) compatibility of your Java applications (native libraries, dependencies, architecture-specific code, Dockerfiles, build configuration, and JVM flags).
+ `aws-health-readiness` – Lambda runtimes, Amazon EKS Kubernetes versions, and Elastic Beanstalk PHP platforms in your infrastructure code that are deprecated or reach a lifecycle date within 180 days. See [Upgrading resources in AWS Health planned lifecycle events](ct-aws-health.md).
+ `custom` – Issues described by one of your own transformation definitions. Requires `--transformation-name`.

```bash
atx ct analysis run --type {{type}} --source {{name}} [--repo {{source}}::{{repo}}] [--wait]
atx ct analysis get --id {{id}} --json
atx ct analysis list --json
atx ct analysis list --status {{pending|running|complete|cancelled|failed}} --json
atx ct analysis list --type {{type}} --json
atx ct analysis cancel --id {{id}}
atx ct analysis delete --id {{id}} [--cascade-findings]
```

If you omit `--repo`, the command analyzes every repository under `--source`. To scope the run to specific repositories, pass `--repo` (comma-separated) — each a fully-qualified {{source}}::{{repo}}, or a bare name used with `--source`.

To label a run so it's easy to find later, pass `--display-name "{{name}}"` on `atx ct analysis run` or `atx ct remote analysis`. The name is shown in `atx ct analysis list` and `atx ct analysis get`.

### Custom analysis
<a name="ct-custom-analysis"></a>

A **custom analysis** runs one of your own transformation definitions against your repositories to look for the issues you care about. To run one:

1. Write a transformation definition that describes what to look for and how to report it. See [Write a transformation definition for analysis](custom.md#custom-analysis-definitions).

1. Publish it with the `analysis` category. See [Transformation definition categories](custom.md#custom-transformation-categories).

1. Run it with `--type custom` and `--transformation-name`, locally, remotely (including on AWS Transform-managed infrastructure), or on a schedule.

```bash
atx ct analysis run --type custom --transformation-name {{name}} --source {{source}} --repo {{source}}::{{repo}} --wait
```

Configuration with `-g` flag: key-value, JSON, or file path.

If the command fails because the transformation definition was not found, check the name with `atx custom def list`. Transformation definitions are specific to an AWS account and Region. If it fails because of the transformation definition's category, publish it again with `--category analysis`.

## Managing findings
<a name="ct-managing-findings"></a>

```bash
atx ct findings list --json
atx ct findings list --repo {{source}}::{{repo}} --source {{name}} --severity {{high|medium|low}} --type {{analysis-type}} --status {{open|dismissed|obsolete|change_ready}} --analysis-id {{id}} --fix-transform {{transform-name}} --json
```

### Matching findings to transformations
<a name="ct-finding-transformations"></a>

An analysis generates findings, and each finding can be matched to a transformation that remediates it. A remediation then runs the matched transformation on the finding's repository.

Findings from tech-debt analyses (`rapid-techdebt-analysis` and `tech-debt-comprehensive`) and from custom analyses can be matched to an AWS managed transformation or to one of your own transformation definitions with the `remediation` category. Findings from other analysis types are matched to AWS managed transformations only.

A finding is matched to a transformation only when that transformation performs the change needed to remediate it. Your own transformation definitions are judged by what their content says they change. Their names and descriptions don't need to describe the change. Neither kind of transformation is preferred: when more than one fits, the finding is matched to the one that most exactly performs the change. When no transformation fits, the finding isn't matched to one. The finding still describes the change to make (in its `recommendation` field), so you can make the change yourself.

In `atx ct findings get` and `atx ct findings list --json`, the matched transformation is the `fix.transform_name` field.

To list the findings matched to one of your transformation definitions:

```bash
atx ct findings list --fix-transform {{my-transformation-name}} --json
```
+ `{{my-transformation-name}}` – The name of your transformation definition.

A findings-based remediation (`atx ct remediation create --ids`) runs each finding's matched transformation. To make one of your transformation definitions eligible to be matched, see [Transformation definition categories](custom.md#custom-transformation-categories).

### Finding statuses
<a name="ct-finding-statuses"></a>
+ `open` — Active
+ `dismissed` — Manually dismissed (requires reason)
+ `obsolete` — System-set when re-analysis no longer produces the finding
+ `change_ready` — System-set when a remediation succeeds for the finding's repository: a code change is ready to review or was already applied. You can't set this status by hand, but you can still dismiss a `change_ready` finding if you decide not to take the change.

```bash
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

Three modes: findings-based, TD override, direct TD. With `--transformation-name`, use one of your own transformation definitions with the `remediation` category, or an AWS managed transformation (see [Transformation definition categories](custom.md#custom-transformation-categories)).

```bash
atx ct remediation create --ids {{id1}},{{id2}} --name "{{name}}"
atx ct remediation create --ids {{id1}},{{id2}} --transformation-name {{TD}}
atx ct remediation create --transformation-name {{TD}} --repo {{source}}::{{repo}}
```

Output by provider: GitHub PR, GitLab MR, Bitbucket PR, Local branch.

**Note**  
Token must have write access for PR/MR creation.

**Important**  
Remote remediations for `graviton-readiness` findings run on x86 infrastructure (Amazon EC2 or AWS Batch). The remediation makes the code changes needed for Arm64, but it can't build or test them on Arm64. Build and test the changes in your Arm64 pipeline before you merge them.

Local execution with `--local` flag.

```bash
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

```bash
# Run an analysis on AWS Transform-managed infrastructure
atx ct remote analysis --type {{type}} --mode aws-managed --sources {{name}} [--repos {{repo1,repo2}}] [--region {{region}}]

# Poll the submission (there is no remote status command in this mode)
atx ct analysis get --id {{id}} --json
```

This mode runs analyses only. In this mode, you can't run remediations or use local sources. Because there is no stack, the `--stack-name`, `--tags`, `--existing-instance`, and `--batch-name` options don't apply. You can include up to 5,000 repositories in a single analysis submission. To cover larger scopes, split them across multiple submissions with `--repos`. Unlike Amazon EC2 and Batch runs, you monitor progress with `atx ct analysis get` rather than `atx ct remote status`.

To run a custom analysis on AWS Transform-managed infrastructure, add `--type custom` and the name of a transformation definition that you published with the `analysis` category in the same AWS account and Region. For more information about custom analyses, see [Custom analysis](#ct-custom-analysis). In the following command, replace {{transformation-name}} and {{source-name}} with your own values:

```bash
atx ct remote analysis --type custom --transformation-name {{transformation-name}} --mode aws-managed --sources {{source-name}}
```

### Networking
<a name="ct-remote-network"></a>

Remote compute must run in private subnets. Discover existing networking or create a new VPC before you provision:

```bash
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

```bash
atx ct remote network discover --vpc {{vpc-id}} --json
```

#### Concurrency limits for each analysis type
<a name="ct-remote-sizing-limits"></a>

AWS Transform limits how many remote jobs run at the same time in an AWS account and Region. The limit depends on the analysis type. These limits are shared across all users in the account and across both compute modes, and they cap the number of addresses a run can consume. To request a change, contact AWS Support.


| Analysis type | Concurrent jobs | 
| --- | --- | 
| `security` | 5 | 
| `tech-debt-quick`, `tech-debt-comprehensive`, `agentic-readiness`, `modernization-readiness`, `graviton-readiness`, `aws-health-readiness`, and `custom` analysis, and remediation other than security remediation | 50, shared across all of these | 
| Security remediation | 128 | 

**Note**  
The types in the second row share a single pool of 50 jobs. Running a comprehensive tech-debt analysis and a custom remediation at the same time gives you 50 jobs in total, not 100.

#### Minimum subnet size
<a name="ct-remote-sizing-table"></a>

Amazon VPC reserves five addresses in every subnet, so the usable count is five fewer than the subnet size — a `/28` has 11 usable addresses and a `/24` has 251. For details, see [Subnet CIDR blocks](https://docs.aws.amazon.com/vpc/latest/userguide/subnet-sizing.html) in the *Amazon VPC User Guide*.

The addresses each subnet needs are the peak concurrent jobs, plus one or more for each interface endpoint in that subnet, plus any other network interfaces that share the subnet. Peak concurrent jobs is the smaller of the number of repositories in the submission and the concurrency limit for the analysis type. Because the limit caps the total, a 5,000-repository fleet needs no more addresses than a 128-repository one.


| Analysis type | Peak concurrent jobs | Minimum subnet size | 
| --- | --- | --- | 
| `security` | 5 | `/27` | 
| `tech-debt-quick`, `tech-debt-comprehensive`, `agentic-readiness`, `modernization-readiness`, `graviton-readiness`, `aws-health-readiness`, `custom` | 50 | `/25` | 
| Every type running at its limit at once | 183 | `/24` | 

The minimums above include headroom for interface endpoints and for the addresses AWS reserves. Size up if other workloads share the subnet. A `/25` is not enough for 128 concurrent jobs: it provides 128 addresses but only 123 usable ones.

We recommend dedicating subnets to remote execution. AWS Transform admits jobs down to the last free address and cannot account for other workloads that claim addresses in the same subnet.

#### Running large fleets
<a name="ct-remote-sizing-large-fleets"></a>

You can include up to 5,000 repositories in a single analysis submission. AWS Transform rejects submissions that exceed the limit before starting any job. To cover larger fleets, split them with `--repos`, and list the repositories in a source with `atx ct repository list --source {{name}} --json`.

Splitting a fleet does not reduce the addresses you need. Submissions that run at the same time draw from the same subnets, up to the concurrency limit for the analysis type.

There is no option that limits how many repositories are scanned at once. The CLI submits every job in a submission, and AWS Transform releases jobs up to the concurrency limit for the analysis type and holds the rest. To pace a large fleet, size the subnets for that limit or submit in smaller groups.

The CLI bounds the number of simultaneous connections it opens to the analysis service. On a very wide submission you may see `socket usage at capacity` on stderr — that message is informational, not an error. If your shell's open-file limit is at or below the bound, the CLI warns once at startup; raise the limit (for example `ulimit -n 4096`) or lower the bound with the `ATX_MAX_SOCKETS` environment variable.

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

```bash
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

```bash
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

```bash
atx ct remote credentials --source {{name}} --token {{token}}
atx ct remote credentials --source {{name}} --remove
```

### Running remotely
<a name="ct-remote-run"></a>

Remote analysis runs one container for each repository; remote remediation runs one container for each finding. Use `--sources`, `--repos`, and `--labels` to control fan-out, and `--stack-name` or `--tags` to select which provisioned stack to use.

```bash
# Run analysis across a source on Batch
atx ct remote analysis --type {{type}} --mode batch --sources {{name}} [--repos {{repo1,repo2}}] [--labels "{{team:frontend}}"]

# Run remediation for specific findings on EC2
atx ct remote remediation --mode ec2 --ids {{id1,id2}}
atx ct remote remediation --mode ec2 --sources {{name}} --min-severity high
```

### Monitoring and managing runs
<a name="ct-remote-monitor"></a>

```bash
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

```bash
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

To schedule a custom analysis on AWS Transform-managed infrastructure, add `--type custom` and `--transformation-name`. Every run of the schedule uses that transformation definition. In the following command, replace {{schedule-name}}, {{role-arn}}, {{transformation-name}}, and {{source-name}} with your own values:

```bash
atx ct schedule create --name {{schedule-name}} --mode aws-managed --execution-role {{role-arn}} --recurrence daily --type custom --transformation-name {{transformation-name}} --sources {{source-name}}
```

To view the analyses a schedule has run, use `atx ct analysis list --schedule-id {{schedule-id}}`, which returns the schedule's fired runs, newest first.

To remove the scheduler role and schedule group used by customer-managed schedules, run `atx ct schedule teardown --execute`.

### Execution role for AWS Transform-managed schedules
<a name="ct-schedule-execution-role"></a>

A schedule created with `--mode aws-managed` requires an `--execution-role` ARN that AWS Transform assumes each time the schedule runs. Configure the role as follows:
+ The identity creating the schedule must have `iam:PassRole` permission on the execution role.
+ The role's trust policy must allow the `transform-custom.amazonaws.com` service principal to assume it.
+ At a minimum, the role must have the AWS managed policy [`AWSTransformCustomFullAccess`](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSTransformCustomFullAccess) attached, plus `secretsmanager:GetSecretValue` and `secretsmanager:DescribeSecret` permissions on secrets under the `atx/*` prefix so that scheduled runs can retrieve the source clone credentials.
+ For an `aws-health-readiness` schedule, the role also needs the AWS Health read permissions in [Permissions and AWS Support plan](ct-aws-health.md#ct-aws-health-permissions). Without them, the findings don't name your affected resources.

The following inline policy grants the AWS Secrets Manager access that scheduled runs need to retrieve source clone credentials. Attach it to the execution role alongside the [`AWSTransformCustomFullAccess`](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSTransformCustomFullAccess) managed policy, replacing {{region}} and {{account-id}} with the AWS Region and account the schedule runs in.

```json
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

```bash
atx ct source add --name {{name}} --provider github --org {{org}} --token {{pat}} --tags {{team=platform,env=prod}}
atx ct analysis run --type {{type}} --source {{name}} --tags {{team=platform}}
atx ct remediation create --ids {{id1,id2}} --tags {{team=platform}}
```

By default, resources are tagged with the tags you define in `~/.aws/atx/settings.json`. Add the tags you want applied to every resource under `applyTags`, and they become your default tags.

```json
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

1. Sign in with the IAM credentials of the AWS account where AWS Transform is enabled. Continuous modernization doesn't appear when you sign in with AWS IAM Identity Center credentials. To sign in with IAM credentials:

   1. In the AWS Management Console, open AWS Transform and choose **Settings**.

   1. Turn on **Access AWS Transform with IAM credentials**.

   1. Copy the **Web application URL (with IAM)** and paste it into the same browser window where the console is open.

1. Open the left navigation menu and choose **Continuous modernization**.

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

1. **Connect sources** – Open the **Sources** tab and add repositories from GitHub, GitLab, or Bitbucket. **GitHub (OAuth)** and **GitLab (OAuth)** are separate entries in the provider list that connect without an access token. For more information, see [Connecting with OAuth in the web application](#ct-web-application-oauth).

1. **Run or schedule an analysis** – Open the **Analyses** tab, select repositories, choose an analysis type, select an infrastructure mode, and choose **Run**. To run on a recurring cadence (daily, weekly, or monthly), choose **Schedule** instead.

1. **Review findings** – Open the **Findings** tab to view results by severity, or grouped by the problem they share.

1. **Create a remediation** – Select findings and choose **Create remediation**. To remediate groups of findings together, create a remediation plan instead. For more information, see [Remediating grouped findings with remediation plans](ct-remediation-plans.md).

1. **Review pull requests** – Open the **Remediations** tab to view generated PR links per repository.

### Chat about continuous modernization
<a name="ct-web-application-chat"></a>

Use the chat pane on the right side of the continuous modernization page to ask about your sources, repositories, analyses, findings, and remediations. In a narrow browser window, choose **Open chat** to show the chat pane. Chat is available only when you sign in with IAM credentials. For more information about signing in, see [Sign in](#ct-web-application-sign-in).

To make a change, ask chat. Chat replies with a description of one action and a button for it, such as **Run analysis** or **Start remediation**. Chat can propose the following actions:
+ Run an analysis.
+ Start a remediation.
+ Dismiss findings.
+ Reopen findings.
+ Set notes on findings.
+ Clear notes on findings.
+ Cancel an analysis.
+ Cancel a remediation.
+ Create a schedule that runs on customer-owned infrastructure.

For an action that runs on customer-owned infrastructure, chat first uses your own permissions to check which of your continuous modernization stacks are deployed. If chat finds no deployed stack, or finds several and you didn't name one, it tells you what to do instead of proposing the action. If chat can't read your stacks, it still proposes the action, and AWS Transform checks the stack when you choose the button.

Nothing changes until you choose the button. AWS Transform then makes the change with your own IAM credentials.

After you choose the button, AWS Transform tells you if you don't have permission for the action. If the items that the action applies to changed after chat proposed it, AWS Transform makes no change, and you can ask chat for an up-to-date proposal.

Use the page to connect sources, delete resources, or enable or disable schedules. Chat doesn't do these tasks.

Chat reads your data with your own IAM permissions, so your IAM policies apply. Lists and details in chat show only what you can view on the continuous modernization pages. To read your data, chat needs the following permissions:
+ `transform-custom:ListSources`
+ `transform-custom:GetSource`
+ `transform-custom:ListRepositories`
+ `transform-custom:GetRepository`
+ `transform-custom:ListAnalyses`
+ `transform-custom:GetAnalysis`
+ `transform-custom:ListFindings`
+ `transform-custom:GetFinding`
+ `transform-custom:GetFindingGroups`
+ `transform-custom:ListRemediations`
+ `transform-custom:GetRemediation`

Without these permissions, chat tells you that you don't have permission instead of showing data.

When you choose the button, AWS Transform needs the permissions for that action, in addition to the read permissions:


| Action | Permissions | 
| --- | --- | 
| Run an analysis | `transform-custom:CreateAnalysis` and `transform-custom:GetRepository` on each repository in the analysis. On customer-owned infrastructure, also `transform-custom:UpdateAnalysis`. | 
| Start a remediation | `transform-custom:CreateRemediation`, `transform-custom:UpdateRemediation`, `transform-custom:GetFinding` on each finding, and `transform-custom:GetRepository` on each repository | 
| Dismiss findings, reopen findings, set notes, or clear notes | `transform-custom:BatchUpdateFindings` | 
| Cancel an analysis | `transform-custom:UpdateAnalysis` | 
| Cancel a remediation | `transform-custom:UpdateRemediation` | 
| Create a schedule | `transform-custom:CreateAnalysis`, `transform-custom:GetRepository` on each repository, `scheduler:CreateSchedule`, and `iam:PassRole` on the `AtxSchedulerInvocationRole-{{region}}` role for `scheduler.amazonaws.com` | 

For an analysis or remediation that uses a custom transformation, AWS Transform also needs `transform-custom:ListTransformationPackageMetadata`.

A remediation, a schedule, and an analysis on customer-owned infrastructure run on your continuous modernization stack. For these actions, chat and AWS Transform also need `cloudformation:ListStacks` and `cloudformation:DescribeStacks` to find your stack, and `sqs:SendMessage` to send the job to it. Grant `cloudformation:DescribeStacks` on all stacks, because for a security analysis AWS Transform finds the stack by listing all your stacks.

The AWS managed policy [AWSTransformCustomFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSTransformCustomFullAccess) includes all the `transform-custom` permissions in this section. The AWS managed policies [AWSTransformInfrastructureExecutorAccessBatch](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSTransformInfrastructureExecutorAccessBatch) and [AWSTransformInfrastructureExecutorAccessEC2](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSTransformInfrastructureExecutorAccessEC2) include the other permissions for your compute mode. To grant only what chat uses, create a policy with the permissions for the actions you need.

### Connecting with OAuth in the web application
<a name="ct-web-application-oauth"></a>

In the AWS Transform web application, the OAuth providers are their own entries in the provider list, separate from the personal access token entries. For more information about signing in, see [Sign in](#ct-web-application-sign-in).

1. On the continuous modernization page, open the **Sources** tab and choose **Connect new source**.

1. For **Provider**, choose **GitHub (OAuth)** or **GitLab (OAuth)**. Neither asks for an access token, and AWS Transform stores nothing in AWS Secrets Manager.

1. You must enter a **Source name**.

1. For **Organization / group / workspace**, enter the GitHub organization or the GitLab group or user to discover repositories from. It is optional, and defaults to the source name when you leave it blank.

1. (Optional) Set the branch name, commit message, and git commit author options. You can change these later; see [Repository conventions](#ct-source-conventions).

1. Choose **Connect**.

What happens next depends on the provider, because only GitHub has an app to install.

For **GitHub (OAuth)**, AWS Transform shows an authorization page naming the source and the organization. The page also says whether the app is already installed. Choose **Install on GitHub** to open GitHub, install or authorize the app, and select the organization or account there, the same page the CLI opens.

For **GitLab (OAuth)**, there is no app to install and no organization to select. AWS Transform sends you straight to GitLab.com, which asks you to authorize the aws-transform-custom application for your account and then redirects you back.

When the source connects, a notification confirms it and names the provider, and the source page opens with its repositories listed, ready to select and analyze. Unlike the CLI, the web application shows no confirmation page in the provider's tab.