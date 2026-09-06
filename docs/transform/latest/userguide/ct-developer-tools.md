

# Developer tools
<a name="ct-developer-tools"></a>

You can access continuous modernization from agentic IDEs using the AWS Transform Power and agent plugin. The agent orchestrates setup, onboarding, and ongoing use of continuous modernization through conversational interaction.
+ **Kiro IDE** — Install the [AWS Transform Kiro Power](https://kiro.dev/launch/powers/aws-transform). Open Kiro Chat and ask the agent to help with continuous modernization workflows.
+ **Claude Code, Codex, Cursor** — Install the [awslabs/agent-plugins](https://github.com/awslabs/agent-plugins) (`plugins/aws-transform` directory). The agent plugin provides the same capabilities as the Kiro Power.

## Agent skills
<a name="ct-agent-skills"></a>

The Kiro Power and agent plugin include skills that orchestrate continuous modernization workflows through conversational interaction:


| Skill | Description | 
| --- | --- | 
| Guide | Interactive onboarding that walks you through the full workflow step by step | 
| Source | Add, list, and remove source connections | 
| Discovery | Scan sources to discover repositories | 
| Analysis | Run and manage analyses across all types | 
| Findings | Query, filter, and manage analysis findings | 
| Remediation | Create and manage remediations to fix findings | 
| EC2 Execution | Provision and manage an Amazon EC2 instance for remote analysis | 
| Batch Execution | Submit analysis jobs to AWS Batch with Fargate | 
| Schedule | Set up recurring analysis on a cron schedule using Amazon EventBridge Scheduler | 
| Reporting | Generate self-contained HTML reports with charts showing findings, severity distribution, and remediation progress | 

## CLI reference
<a name="ct-cli-reference"></a>

The following table summarizes all `atx ct` subcommands.


| Subcommand | Description | 
| --- | --- | 
| atx ct status | View system status including sources, repositories, analyses, findings, and remediations | 
| atx ct source add | Add a source (GitHub, GitLab, Bitbucket, or local) | 
| atx ct source list | List configured sources | 
| atx ct source get | Show details for a single source | 
| atx ct source update | Update the token for an existing source | 
| atx ct source remove | Remove a source | 
| atx ct discovery scan | Discover repositories from a source | 
| atx ct discovery status | Check discovery scan status | 
| atx ct repository list | List repositories with optional filters | 
| atx ct repository get | Get a single repository | 
| atx ct repository update | Update repository labels | 
| atx ct repository delete | Delete a repository | 
| atx ct analysis run | Run an analysis on repositories | 
| atx ct analysis get | Get analysis details | 
| atx ct analysis list | List analyses with optional status and type filters | 
| atx ct analysis cancel | Cancel a running analysis | 
| atx ct analysis delete | Delete an analysis | 
| atx ct findings list | List findings with filters for repo, source, severity, type, status, and analysis | 
| atx ct findings count | Count findings aggregated by severity, repo, or analysis type | 
| atx ct findings get | Get a single finding | 
| atx ct findings update | Update finding status (open or dismissed) | 
| atx ct findings batch-update | Batch update multiple findings | 
| atx ct findings delete | Delete a dismissed or obsolete finding | 
| atx ct remediation create | Create a remediation from findings or a transformation definition | 
| atx ct remediation list | List all remediations | 
| atx ct remediation status | Check remediation status and view PR/MR links | 
| atx ct remediation retry | Retry a failed remediation | 
| atx ct remediation cancel | Cancel a running remediation | 
| atx ct remediation delete | Delete a remediation | 
| atx ct remote provision | Deploy remote execution infrastructure (Amazon EC2 or Batch AWS CloudFormation stack) | 
| atx ct remote analysis | Run analysis remotely on Amazon EC2 or Batch | 
| atx ct remote remediation | Run remediation remotely on Amazon EC2 or Batch | 
| atx ct remote status | Show status of a remote submission | 
| atx ct remote detect | Check whether remote infrastructure is deployed | 
| atx ct remote update | Update remote execution infrastructure to the latest template | 
| atx ct remote credentials | Manage source tokens in Secrets Manager for remote execution | 
| atx ct remote cancel | Cancel a running remote run | 
| atx ct remote teardown | Destroy remote execution infrastructure | 
| atx ct remote network | Discover or create VPC, subnets, and security groups for remote provisioning | 
| atx ct schedule create | Create a recurring analysis schedule (Amazon EventBridge Scheduler) | 
| atx ct schedule list | List schedules | 
| atx ct schedule get | Show a single schedule | 
| atx ct schedule enable | Enable a schedule | 
| atx ct schedule disable | Disable a schedule | 
| atx ct schedule delete | Delete a schedule | 
| atx ct schedule teardown | Delete the scheduler role and schedule group | 
| atx ct setup security-agent | Provision or manage security agent infrastructure | 
| atx ct mcp | Start the MCP server exposing continuous modernization tools | 
| atx ct schema | Print a machine-readable JSON manifest of the full atx ct command surface — every command, option, and argument — so agents and automation can discover the CLI without parsing help text | 