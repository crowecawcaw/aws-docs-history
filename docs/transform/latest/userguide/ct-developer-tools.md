# Developer tools

You can access continuous modernization from agentic IDEs using the AWS Transform Power and agent
plugin. The agent orchestrates setup, onboarding, and ongoing use of continuous modernization
through conversational interaction.

- **Kiro IDE** — Install the
  [AWS Transform Kiro Power](https://kiro.dev/launch/powers/aws-transform "https://kiro.dev/launch/powers/aws-transform").
  Open Kiro Chat and ask the agent to help with continuous modernization
  workflows.
- **Claude Code, Codex, Cursor** — Install the
  [awslabs/agent-plugins](https://github.com/awslabs/agent-plugins "https://github.com/awslabs/agent-plugins")
  (`plugins/aws-transform` directory). The agent plugin provides the same
  capabilities as the Kiro Power.

## Agent skills

The Kiro Power and agent plugin include skills that orchestrate continuous modernization
workflows through conversational interaction:

| Skill           | Description                                                                                                           |
| --------------- | --------------------------------------------------------------------------------------------------------------------- |
| Guide           | Interactive onboarding that walks you through the full workflow step by step                                          |
| Source          | Add, list, and remove source connections                                                                              |
| Discovery       | Scan sources to discover repositories                                                                                 |
| Analysis        | Run and manage analyses across all types                                                                              |
| Findings        | Query, filter, and manage analysis findings                                                                           |
| Remediation     | Create and manage remediations to fix findings                                                                        |
| EC2 Execution   | Provision and manage an Amazon EC2 instance for remote analysis                                                       |
| Batch Execution | Submit analysis jobs to AWS Batch with Fargate                                                                        |
| Schedule        | Set up recurring analysis on a cron schedule using Amazon EventBridge<br>Scheduler                                    |
| Reporting       | Generate self-contained HTML reports with charts showing findings, severity<br>distribution, and remediation progress |

## CLI reference

The following table summarizes all `atx ct` subcommands.

| Subcommand                     | Description                                                                                                                                                                                       |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `atx ct server`                | Start the continuous modernization server                                                                                                                                                         |
| `atx ct status`                | View system status including sources, repositories, analyses, findings, and<br>remediations                                                                                                       |
| `atx ct source add`            | Add a source (GitHub, GitLab, Bitbucket, or local)                                                                                                                                                |
| `atx ct source list`           | List configured sources                                                                                                                                                                           |
| `atx ct source remove`         | Remove a source                                                                                                                                                                                   |
| `atx ct discovery scan`        | Discover repositories from a source                                                                                                                                                               |
| `atx ct discovery status`      | Check discovery scan status                                                                                                                                                                       |
| `atx ct repository list`       | List repositories with optional filters                                                                                                                                                           |
| `atx ct repository get`        | Get a single repository                                                                                                                                                                           |
| `atx ct repository update`     | Update repository labels                                                                                                                                                                          |
| `atx ct repository delete`     | Delete a repository                                                                                                                                                                               |
| `atx ct analysis run`          | Run an analysis on repositories                                                                                                                                                                   |
| `atx ct analysis get`          | Get analysis details                                                                                                                                                                              |
| `atx ct analysis list`         | List analyses with optional status and type filters                                                                                                                                               |
| `atx ct analysis cancel`       | Cancel a running analysis                                                                                                                                                                         |
| `atx ct analysis delete`       | Delete an analysis                                                                                                                                                                                |
| `atx ct findings list`         | List findings with filters for repo, source, severity, type, status, and<br>analysis                                                                                                              |
| `atx ct findings get`          | Get a single finding                                                                                                                                                                              |
| `atx ct findings update`       | Update finding status (open or dismissed)                                                                                                                                                         |
| `atx ct findings batch-update` | Batch update multiple findings                                                                                                                                                                    |
| `atx ct findings delete`       | Delete a dismissed or obsolete finding                                                                                                                                                            |
| `atx ct remediation create`    | Create a remediation from findings or a transformation definition                                                                                                                                 |
| `atx ct remediation list`      | List all remediations                                                                                                                                                                             |
| `atx ct remediation status`    | Check remediation status and view PR/MR links                                                                                                                                                     |
| `atx ct remediation retry`     | Retry a failed remediation                                                                                                                                                                        |
| `atx ct remediation delete`    | Delete a remediation                                                                                                                                                                              |
| `atx ct setup security-agent`  | Provision or manage security agent infrastructure                                                                                                                                                 |
| `atx ct schema`                | Print a machine-readable JSON manifest of the full `atx ct` command<br>surface — every command, option, and argument — so agents and automation can discover<br>the CLI without parsing help text |
