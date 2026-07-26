# Using AI agents with DMS Schema Conversion

You can use AI agents to drive DMS Schema Conversion workflows through the AWS API. An AI
agent is a software tool that uses large language models to understand natural
language instructions and automate tasks. When connected to the
[AWS MCP server](../../../agent-toolkit/latest/userguide/mcp-server.md "../../../agent-toolkit/latest/userguide/mcp-server.md"), an AI agent can create
migration projects, browse your source database metadata tree, convert schemas,
generate assessment reports, export results, and explain various aspects of the
service. You control these operations through natural language prompts.

To improve the agent's accuracy and efficiency with DMS Schema Conversion, you can install
the AWS DMS Schema Conversion skill. The skill provides DMS Schema Conversion-specific context including API
patterns, system schema exclusions, operation sequencing, and service best
practices.

###### Important

The skill contains instructions that **prevent common
errors that AI agents make when using DMS Schema Conversion** and **reduce trial-and-error loops, which helps decrease token usage and increase the speed of achieving the desired goal**. We strongly recommend installing it before you
start.

This topic shows how to install the skill, and provides examples of common
DMS Schema Conversion workflows that you can run through an AI agent.

## Prerequisites

Before you begin, make sure you have the following prerequisites. This guide assumes
familiarity with AWS DMS and command-line interfaces.

- **An AI agent** — An AI coding agent
  that supports the Model Context Protocol (MCP), such as
  [Kiro CLI](https://kiro.dev/cli/ "https://kiro.dev/cli/"),
  [Claude Code](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview "https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview"),
  or [Cursor](https://www.cursor.com/ "https://www.cursor.com/").
- **AWS MCP server** — Configure the
  [AWS MCP server](../../../agent-toolkit/latest/userguide/mcp-server.md "../../../agent-toolkit/latest/userguide/mcp-server.md")
  in your agent so it can make AWS API calls. For more information, see
  [Setting up the AWS MCP Server](../../../agent-toolkit/latest/userguide/getting-started-aws-mcp-server.md "../../../agent-toolkit/latest/userguide/getting-started-aws-mcp-server.md") in the AWS Agent Toolkit User Guide.
- **AWS credentials** — The agent needs
  AWS credentials with permissions to call AWS DMS APIs. Configure
  credentials using the
  [AWS CLI](../../../cli/latest/userguide/cli-chap-authentication.md "../../../cli/latest/userguide/cli-chap-authentication.md"). For more information about required permissions, see
  [IAM permissions needed to use AWS DMS](security-iam.md#CHAP_Security.IAMPermissions "security-iam.md#CHAP_Security.IAMPermissions").

###### Note

If you already have a migration project configured in DMS Schema Conversion, the
agent can work with it immediately. Otherwise, the agent can create one
for you. For more information, see
[Working with data providers, instance profiles, and migration projects in AWS DMS](migration-projects.md "migration-projects.md").

## Installing the AWS DMS Schema Conversion skill

A skill is a curated package of instructions and reference materials that
helps your AI agent complete DMS Schema Conversion tasks effectively. The AWS DMS Schema
Conversion skill contains API patterns, system schema exclusions, operation
sequencing rules, and service best practices. With this skill, the agent
makes fewer errors and requires less back-and-forth to complete DMS Schema Conversion
operations.

Choose one of the following methods to install the skill.

AWS MCP server
If your agent is connected to the AWS MCP Server, the agent
can find and load the skill automatically through the MCP server.
Before proceeding, verify that your MCP servers are loaded and
connected. In most AI agents, you can check MCP server status by
entering `/mcp`. Then ask your agent:

```
Load "dms-schema-conversion" skill using the `retrieve_skill` tool.
```

The agent retrieves the skill from the AWS MCP server and
applies it to the current session.

npx skills CLI
If your agent doesn't use the AWS MCP server, you can install
the skill locally from the
[AWS
Agent Toolkit for AWS](https://github.com/aws/agent-toolkit-for-aws "https://github.com/aws/agent-toolkit-for-aws") repository on GitHub. Run the
following command from your project directory:

```
npx skills add aws/agent-toolkit-for-aws/skills/specialized-skills/migration-and-modernization-skills/dms-schema-conversion
```

###### Note

If you use a custom agent definition within your AI coding tool, make sure
that the agent configuration includes a skills directory. Otherwise, the
agent cannot discover and load the skill.

Manual installation
Clone the
[AWS
Agent Toolkit for AWS](https://github.com/aws/agent-toolkit-for-aws "https://github.com/aws/agent-toolkit-for-aws") repository and copy the skill
directory to your agent's skills location. The following table
shows the skills path for supported agents.

| Agent       | Project skills path | Global skills path  |
| ----------- | ------------------- | ------------------- |
| Kiro CLI    | `.kiro/skills/`     | `~/.kiro/skills/`   |
| Claude Code | `.claude/skills/`   | `~/.claude/skills/` |
| Cursor      | `.cursor/skills/`   | `~/.cursor/skills/` |
| Codex       | `.agents/skills/`   | `~/.codex/skills/`  |

###### Note

If you use a custom agent definition within your AI coding tool, make sure
that the agent configuration includes a skills directory. Otherwise, the
agent cannot discover and load the skill.

Direct URL
You can load the skill directly from the GitHub URL without
installing anything locally. Ask your agent:

```
Load skill from https://github.com/aws/agent-toolkit-for-aws/blob/main/skills/specialized-skills/migration-and-modernization-skills/dms-schema-conversion/SKILL.md
```

The agent fetches the skill content from GitHub and applies it
to the current session.

After the skill loads successfully, you see an action menu with available
schema conversion actions.

## Best practices

Follow these recommendations to get the best results when using AI agents
with DMS Schema Conversion.

- **Browse before converting** — Use the
  agent to explore the metadata tree before you start converting schemas.
  This helps you understand the scope of the migration and identify which
  schemas to convert.
- **Convert one schema at a time** — For
  large databases, convert schemas individually rather than all at once.
  This makes it easier to review the converted code and address action
  items incrementally.
- **Skip system schemas** — Do not convert
  system databases or system schemas. They contain engine-internal objects
  that produce large numbers of unconvertible action items.
- **Review converted SQL before applying**
  — Export the converted code as SQL scripts and review it before applying
  to your target database, especially for code objects.
- **Enable generative AI-assisted conversion** —
  Enable generative AI-assisted conversion to improve the conversion rate for
  code objects. Generative AI-assisted conversion uses machine learning to convert
  objects that the rule-based converter cannot handle automatically. For
  more information, see
  [Converting database objects with generative AI](schema-conversion-convert.databaseobjects.md "schema-conversion-convert.databaseobjects.md").
- **Use the assessment report** — After
  conversion or assessment, generate an assessment report to get a summary
  of conversion results and remaining manual work. For more information,
  see [Conversion assessment reports with DMS Schema Conversion](assessment-reports.md "assessment-reports.md").

## Examples

The following examples show common DMS Schema Conversion workflows that you can run
through an AI agent after loading the skill.

In this example, you use an AI agent to create a migration project for
converting a Microsoft SQL Server database to Amazon Aurora PostgreSQL. The
agent creates the required AWS DMS resources and links them together.

The following prompt instructs the agent to create a migration project:

```
I want to migrate my SQL Server database to Aurora PostgreSQL using DMS Schema Conversion. The source database is on an EC2 instance at 10.0.1.50, port 1433, database name "AdventureWorks". The credentials are stored in Secrets Manager under "mydb-source-credentials". Create a migration project for me.
```

The agent creates a source data provider, a target data provider, an instance profile, and the
migration project that links them together. If you don't have a target database yet, the agent
creates a virtual target data provider so you can convert and export schemas as SQL
scripts. The agent also creates required IAM
roles and S3 buckets, and checks network configuration.

After the agent creates the migration project, you can browse the source
database metadata, assess or convert schemas, and export results.

You can use the agent to explore your source database structure. The agent
navigates the metadata tree hierarchically, listing databases, schemas, tables,
stored procedures, and other objects.

```
Show me the databases and schemas in my source database.
```

The agent imports the source metadata if it has not been imported yet, then
navigates the metadata tree using the AWS DMS API. You can drill deeper into
specific schemas:

```
Show me the stored procedures in the AdventureWorks.dbo schema.
```

After you browse the metadata tree, you can use the agent to assess or convert
schemas and export the results.

```
Convert the AdventureWorks.dbo schema to Aurora PostgreSQL and export the converted SQL scripts.
```

The agent converts the schema objects and exports the converted SQL scripts to
the S3 bucket. Each conversion and export operation runs asynchronously, and the
agent polls for completion before starting the next operation. After conversion,
the agent generates an assessment report.

The assessment report includes a summary of converted objects, action items
for objects that require manual changes, and effort estimates. You can also ask
the agent to explain the meaning of specific action items and provide guidance
on how to resolve them.

Some DMS Schema Conversion operations, such as schema conversion, metadata import,
and assessment, run asynchronously and can take time. While the agent polls
for completion, you might want to ask questions, get clarifications, or give
additional instructions without interrupting the workflow.

The following approaches let you interact with the agent during a
long-running operation. Choose a method based on your agent's
capabilities.

Ctrl+C
This approach works in most AI agents, including Kiro CLI,
Claude Code, and Cursor.

Press Ctrl+C to interrupt the agent
while it polls for progress. You can then ask your
question or give a new instruction. The agent pauses the
current operation but doesn't cancel the operation on the
server side — it continues running in AWS DMS.

After the agent answers your question, you can ask it to
resume checking on the operation status.

```
Check if the conversion is done now.
```

Separate session
This approach works with any AI agent.

Open a new terminal tab and start a separate agent session.
Use one session to run the operation and poll for completion,
and the other session to ask questions or do other work. Both
sessions can access the same MCP servers and AWS
resources.

Instructing the agent not to poll
This approach works with any AI agent.

Instead of waiting for an operation to complete, instruct the
agent to start the operation and return immediately. You can
then ask questions, do other work, and check on the status
when ready.

Example prompt:

```
Start converting the AdventureWorks.dbo schema but don't wait for it to finish. I'll ask you to check the status later.
```

Then later:

```
Check if the dbo schema conversion is complete.
```

/btw command
This approach is available in Claude Code and other agents
that support background messages.

Enter `/btw` followed by your question to send a
side message without interrupting the agent's current task. The
agent processes your question in the background while continuing
to poll for completion.

Example:

```
/btw What action items typically appear for stored procedures?
```

Subagents
This approach is available in agents that support background
subagents, such as Claude Code.

Instruct the agent to run the operation in a background
subagent. The subagent polls for completion while your main
session remains free for questions and other work.

Example prompt:

```
Run the AdventureWorks.dbo schema conversion in a background subagent and let me know when it's done.
```
