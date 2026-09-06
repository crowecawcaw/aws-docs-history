# Run migrations with the AWS Transform MCP server

The AWS Transform Model Context Protocol (MCP) server lets you plan and run migrations
from any MCP-compatible client, such as Kiro, Claude Code, Cursor, or Cline, without
leaving your development environment. MCP is a standardized interface that gives the AI
assistant in your client real-time, contextual access to your AWS Transform workspaces and
jobs. With it, you can create workspaces, launch migration jobs, respond to
human-in-the-loop tasks, and download artifacts through natural language.

The MCP server exposes the full migration lifecycle: discovery of your source
environment, migration planning, connecting target AWS accounts, network migration,
landing zone setup, and server rehost. It runs as a local process launched by your MCP
client and communicates with AWS Transform over outbound HTTPS. The MCP client is the
process that runs the server, such as Kiro or Claude Code. The AI assistant is the model
experience in that client that you send prompts to. For a general introduction to
AWS Transform developer tools, including the Kiro Power, agent plugins, and IDE plugin, see
[Developer tools](developer-tools.md "developer-tools.md").

###### Installing the MCP server

The Kiro Power and agent plugins install the MCP server automatically. Install the
MCP server manually only if you want to use it without a Kiro Power or agent
plugin.

## Setting up the AWS Transform MCP server

Before you begin, make sure you have the following:

- Python 3.10 or later.
- An AWS Transform account with tenant access. For information about setting up
  AWS Transform, see [Getting started with AWS Transform](getting-started.md "getting-started.md").
- An MCP-compatible client, such as Kiro, Claude Code, Claude Desktop,
  Cursor, or Cline.

###### Install the MCP server

You can install the AWS Transform MCP server from PyPI as
`awslabs.aws-transform-mcp-server`. The following examples run the server
with `uvx`.

**Claude Code**

```
claude mcp add awslabs.aws-transform-mcp-server -- uvx awslabs.aws-transform-mcp-server@latest
```

**Kiro, Cursor, VS Code, Cline, and Claude Desktop
(macOS/Linux)**

Add the following to your client's MCP configuration file. For Kiro, use
`~/.kiro/settings/mcp.json`.

```
{
  "mcpServers": {
    "awslabs.aws-transform-mcp-server": {
      "command": "uvx",
      "args": ["awslabs.aws-transform-mcp-server@latest"],
      "env": {
        "AWS_REGION": "us-east-1",
        "FASTMCP_LOG_LEVEL": "ERROR"
      }
    }
  }
}
```

**Windows**

```
{
  "mcpServers": {
    "awslabs.aws-transform-mcp-server": {
      "command": "uvx",
      "args": [
        "--from",
        "awslabs.aws-transform-mcp-server@latest",
        "awslabs.aws-transform-mcp-server.exe"
      ],
      "env": {
        "FASTMCP_LOG_LEVEL": "ERROR",
        "AWS_REGION": "us-east-1"
      },
      "disabled": false
    }
  }
}
```

For configuration details for your specific MCP client, see the [aws-transform-mcp-server](https://github.com/awslabs/mcp/tree/main/src/aws-transform-mcp-server "https://github.com/awslabs/mcp/tree/main/src/aws-transform-mcp-server") README on GitHub.

###### Configure environment variables

You can set the following environment variables in the `env` block of
your MCP client configuration.

| Variable                      | Description                                                                                                                                                                                                                                         |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `AWS_REGION`                  | The AWS Region used for control plane API calls. Defaults to the<br>profile Region, and then to US East (N. Virginia).                                                                                                                              |
| `AWS_PROFILE`                 | The credential profile used for control plane tools. Falls back<br>through the standard credential chain if not set.                                                                                                                                |
| `FASTMCP_LOG_LEVEL`           | The log level (`DEBUG`, `INFO`,<br>`WARNING`, or `ERROR`). Defaults to<br>`INFO`.                                                                                                                                                                   |
| `AWS_TRANSFORM_MCP_WRITE_DIR` | The base directory that artifact downloads are confined to. A<br>download path must resolve within this directory. If your client<br>launches the server outside a shell, set this variable so that<br>artifact downloads have a valid destination. |

###### Authenticate

Most MCP tools use web API authentication (browser login). The
`accept_connector` tool also requires AWS credentials, which the server
detects automatically. AWS Transform supports the following authentication
methods.

IAM Identity Center (SSO)

Ask the AI assistant to "Configure AWS Transform with SSO." The assistant
prompts for your IAM Identity Center start URL and opens your browser to
log in. The server then saves your credentials locally and loads them
automatically when you restart it. Re-run this configuration when tools
return authentication errors.

IAM role

Your environment provides AWS credentials automatically. Set
`AWS_PROFILE` in your MCP client configuration to select a
specific profile.

For more information about setting up authentication for AWS Transform, see the
prerequisites earlier in this topic.

###### Verify the connection

After you install and configure the server, restart your MCP client. Then ask the
AI assistant to "Check my AWS Transform connection status." A successful response
confirms that the server is installed, configured, and authenticated.

## Using AWS Transform for migrations via MCP

With the MCP server connected, you drive your migration by talking to the AI
assistant in natural language. The assistant calls AWS Transform MCP tools on your
behalf to manage workspaces, launch migration jobs, respond to human-in-the-loop
tasks, and retrieve artifacts. A typical migration follows these stages.

###### To run a migration through the MCP server

1. **Create or select a workspace.** A workspace
   is a logical container for one or more migration jobs. The workspace
   determines the AWS Region where your jobs, discovery data, and AWS Transform
   recommendations reside. Ask the assistant to create a workspace or list your
   existing workspaces.
2. **Create and start a migration job.** Ask the
   assistant to create a migration job. The assistant discovers the available
   agents and starts the job. For information about the migration job types and
   the steps that each includes, see [Job types](vmware-jobs.md#vmware-job-types "vmware-jobs.md#vmware-job-types").
3. **Run discovery.** Upload your on-premises
   server inventory so AWS Transform can parse, de-duplicate, and validate it. For
   the supported discovery data sources and formats, see [Discover source data](transform-vmware-discover-source-data.md "transform-vmware-discover-source-data.md").
4. **Build the migration plan.** Work with the
   assistant to scope and analyze your inventory, group servers into
   applications, generate move groups, and build migration waves. You can ask
   questions about your environment and iterate on the plan at any time. For
   more information, see [Build migration plan](transform-vmware-review-groupings-and-waves.md "transform-vmware-review-groupings-and-waves.md").
5. **Connect your target account.** Create a
   connector and have an administrator of the target AWS account approve it so
   AWS Transform can deploy infrastructure, migrate networks, and rehost servers.
   For more information, see [Connect target AWS accounts and regions](transform-vmware-connect-target-account.md "transform-vmware-connect-target-account.md").
6. **Migrate the network, build the landing zone, and
   rehost servers.** Ask the assistant to run the remaining
   execution steps in your job plan.
7. **Respond to human-in-the-loop tasks.**
   AWS Transform pauses at review and approval points. The assistant surfaces the
   task and its artifact for you to review. After you decide, the assistant
   submits your response (approve, reject, or send for approval). Always review
   the task details and the agent artifact before you approve.
8. **Track status and download artifacts.** Ask
   the assistant for job status at any time, and have it download artifacts such
   as reports, diagrams, and workspace summaries to your local
   environment.

Because you interact with AWS Transform conversationally, you can move between these
stages iteratively, ask clarifying questions, and refine your plan without switching
tools.

## Best practices

Follow these best practices when you run migrations through the AWS Transform MCP
server.

- **Review before you approve.** Always inspect
  the task details and the agent artifact before you approve a human-in-the-loop
  task. Do not let the assistant auto-submit approvals for migration steps that
  create or modify AWS resources.
- **Use least-privilege credentials.**
  Configure the `AWS_PROFILE` environment variable to point at a
  profile scoped to only the permissions your migration requires. For
  multi-account migrations, prefer a Delegated Administrator account over the
  organization management account. For more information, see [Using a delegated administrator account](transform-vmware-connect-target-account.md#transform-vmware-cta-delegated-admin "transform-vmware-connect-target-account.md#transform-vmware-cta-delegated-admin").
- **Confine artifact downloads.** Set the
  `AWS_TRANSFORM_MCP_WRITE_DIR` environment variable to a dedicated
  directory so that downloaded artifacts land in a known, contained location.
  This is especially important when a desktop or IDE client launches the server
  outside a shell.
- **Keep your session authenticated.** SSO
  tokens expire. Re-run SSO configuration when tools begin returning
  authentication errors, and verify your connection with a status check before
  starting long-running steps.
- **Set the correct Region.** Set
  `AWS_REGION` to the AWS Region where your workspace and
  discovery data reside. If your migration target Region differs from your
  discovery Region, some data is transferred across AWS Regions. For more
  information, see [Supported target regions](transform-vmware-connect-target-account.md#transform-vmware-cta-supported-regions "transform-vmware-connect-target-account.md#transform-vmware-cta-supported-regions").
- **Upload complete, current discovery data.**
  The quality of your migration plan depends on the quality of your inventory.
  Upload the most detailed data available and verify it reflects your current
  environment before you build waves.
- **Consider expert mode for large
  migrations.** When you want to minimize back-and-forth, provide
  your inputs up front and let the agent apply them automatically. For more
  information, see [Use expert mode](transform-app-vmware-expert-mode.md "transform-app-vmware-expert-mode.md").

## Example prompts

Running AWS Transform through the MCP server does more than move the web experience
into your IDE. The AI assistant chains multiple tool calls, reads and writes files
in your local workspace, and applies conditional logic. As a result, you can express
multi-step, iterative, and batch workflows that go beyond a single web-application
interaction. The following examples show sophisticated prompts. Adapt them to your
environment.

###### Verification and monitoring loops

Have the assistant poll a running step, react to what it finds, and pause for you
only when a decision is required. An autonomous loop like this is driven by the
assistant, not the web application.

```
Start network migration for wave 1, then poll the job status every two
minutes until it completes or needs my input. If a human-in-the-loop task
appears, stop polling, summarize the task and its artifact for me, and wait
for my decision before doing anything else.
```

```
Check every active job across all my workspaces. For each one, give me a
one-line status, and flag any job that has been waiting on an approval for
more than 24 hours or has reported an error. Repeat this check every 15
minutes and only message me when something changes.
```

```
Re-run the inventory readiness check after my latest upload. If there are any
data-quality errors, list the affected servers grouped by issue and stop. If
it validates cleanly, proceed to application grouping using the rules in
./planning/grouping-rules.md.
```

###### Reports that combine assessment and planning data

Ask the assistant to cross-reference artifacts from different stages and synthesize
a consolidated report. The assistant can then save it to your local workspace for
review or version control.

```
Pull my migration strategy (7Rs) recommendations and my current wave plan.
Cross-reference them and produce a consolidated readiness report that
highlights every application whose recommended strategy conflicts with the
strategy assigned to its wave. Include the confidence score and reasoning for
each conflict, and save the report to ./reports/readiness.md.
```

```
Build an executive migration report that combines my risk assessment scores,
the 7Rs recommendations, and the wave schedule. Rank waves by combined risk,
call out the top five applications that need attention before cutover, and
export it as both a PDF for stakeholders and a PPTX deck for my review.
```

```
Compare the assessment I ran last month with my current plan. Tell me which
servers were newly discovered, which changed operating system or strategy, and
which moved between waves. Write the diff to ./reports/plan-change-log.md.
```

###### Per-application diagrams and batch generation

Iterate over the applications or waves in your plan and generate an artifact for
each, saving them locally in one pass.

```
For each application in my plan, generate an application dependency diagram
and save it to ./diagrams/APP_NAME.html. When you finish, give me a table of
every application with the number of dependencies found, and list any
applications you could not generate a diagram for and why.
```

```
For each wave, generate a network topology diagram scoped to that wave's
servers plus their cross-wave dependencies, and save each one to
./diagrams/waves/wave-N.html. Highlight any dependency that crosses a wave
boundary, since those need sequencing attention.
```

###### Local-environment integration

Combine AWS Transform with files and tools in your local development environment,
something the web application cannot do.

```
Read the decommissioning list in ./exclusions.csv, remove every matching
server from migration scope, then rebuild my waves and show me what changed in
the plan as a result.
```

```
Read the tagging standard in ./standards/tagging.md and apply it as the
resource tagging configuration for network migration and server rehost. Show
me the resulting tag set and flag any required tag the standard does not
specify a value for.
```

```
Download the workspace summary and the 7Rs report, commit them to the
migration-artifacts git repo in this workspace under ./artifacts/$(date +%F)/,
and write a short changelog entry describing what changed since the last
snapshot.
```

###### Conditional and gated automation

Express approval gates and branching so the assistant advances the migration only
when your conditions are met.

```
Walk my end-to-end job through discovery and planning in expert mode using the
inputs in ./planning/inputs.txt. Pause for my review after wave planning
completes. Do not connect any target account or start execution until I
explicitly approve.
```

```
For wave 1 only, connect the target account, migrate the network, and rehost
the servers. After each step, verify it succeeded before starting the next. If
any step fails or produces a warning, stop immediately, show me the details,
and do not touch waves 2 or 3.
```
