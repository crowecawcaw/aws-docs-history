# OpenSearch Agent Skills

Developers today can go from idea to working prototype in minutes using agentic IDEs
like Kiro, Claude Code, and Cursor. But whether you're experimenting with a new
idea, building a proof of concept, or running production systems, the experience quickly
becomes more complex. Search results don't behave as expected, latency spikes
require digging through logs, and deploying to AWS introduces configuration decisions
that require deep expertise. Translating high-level intent into query DSLs, index
configurations, and multi-step workflows still takes significant time – even with
an AI agent at your side.

[OpenSearch Agent Skills](https://github.com/opensearch-project/opensearch-agent-skills "https://github.com/opensearch-project/opensearch-agent-skills") addresses this by providing a repository of
skills that bring OpenSearch intelligence directly into your agent. Each
skill encapsulates domain knowledge, best practices, and multi-step execution logic for
a specific workflow – so your agent not only gets results, but understands how
they were achieved. Skills work with any coding agent that supports the [Agent Skills standard](https://agentskills.io/specification "https://agentskills.io/specification"), including
Kiro, Claude Code, and Cursor.

## What you can do with Agent Skills

### Build a local search application

The `opensearch-launchpad` skill brings an intent-driven
experience to building and iterating on search applications. It translates
natural language requirements or sample data into a fully configured
OpenSearch index – with optimized mappings, ingest pipelines, and ML
model integrations for keyword, semantic, and hybrid search – and
produces a working search experience ready to test and iterate on.

Example prompt:

```
Build a semantic search application for product documentation
```

The agent configures the index mappings, sets up an embedding model and
ingest pipeline, and returns a working search API and UI – walking you
through each decision along the way.

### Investigate incidents with log analytics

The `log-analytics` skill brings agentic intelligence to
observability workflows. Instead of manually crafting Piped Processing Language
(PPL) queries or piecing together log data across services, you express your
intent and the skill handles the complexity – from error pattern
detection to anomaly analysis to root cause correlation.

Example prompt:

```
Investigate why my service is returning 500s and correlate with recent traces
```

The agent runs PPL queries to surface error patterns and log volume
anomalies, then correlates log errors to specific trace IDs for faster root
cause analysis – without requiring you to master PPL syntax or manually
navigate trace data.

### Investigate distributed traces

The `trace-analytics` skill investigates distributed traces
directly within OpenSearch. It identifies slow spans, error spans, and
service dependencies, and correlates logs and traces using trace IDs to surface
root causes across the full observability stack.

Example prompt:

```
Which service is causing the p99 latency regression in the checkout flow?
```

The agent builds a service map, identifies the slow spans, and pinpoints the
bottleneck – without requiring you to manually navigate trace data across
services.

### Deploy OpenSearch to AWS

The `aws-setup` skill walks your agent through provisioning an
OpenSearch Service domain or OpenSearch Serverless collection, configuring access and encryption policies,
and connecting your application – with separate guides for managed
domains and serverless collections.

Example prompt:

```
Set up an OpenSearch Serverless collection for my search application
```

The agent handles provisioning, policy configuration, and validation,
guiding you through each step.

## Available skills

Skills are organized by category. You can install the complete collection or
individual skills:

| Category      | Skill                  | What it does                                                                                                                                                                                                |
| ------------- | ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Search        | `opensearch-launchpad` | Scaffolds a search application from scratch. Covers BM25 lexical<br>search, semantic search, hybrid search, and agentic search. Includes<br>model selection guides, evaluation strategies, and sample data. |
| Observability | `log-analytics`        | Queries and analyzes logs using Piped Processing Language (PPL).<br>Helps the agent detect error patterns, surface anomalies, and<br>correlate events across indexes.                                       |
| Observability | `trace-analytics`      | Investigates distributed traces. Identifies slow spans, builds<br>service maps, and traces AI agent tool invocations through your<br>system.                                                                |
| Cloud         | `aws-setup`            | Deploys OpenSearch to AWS. Includes dedicated guides for<br>Amazon OpenSearch Service domains and OpenSearch Serverless collections, covering provisioning,<br>access policies, and network configuration.  |

The project is under active development. For the latest skill list and contribution
guidance, see the [opensearch-agent-skills](https://github.com/opensearch-project/opensearch-agent-skills "https://github.com/opensearch-project/opensearch-agent-skills") repository.

## Prerequisites

Prerequisites vary by skill. To use the full collection you need:

- A coding agent that supports Agent Skills (Claude Code, Cursor, or
  Kiro).
- [Node.js](https://nodejs.org/ "https://nodejs.org/") with `npx`
  on your `PATH`, to run the `skills` installer.
- [`uv`](https://docs.astral.sh/uv/getting-started/installation/ "https://docs.astral.sh/uv/getting-started/installation/") and Python 3.11 or later. Skills use
  `uv` to run scripts in isolated environments.
- [Docker](https://docs.docker.com/get-docker/ "https://docs.docker.com/get-docker/") installed
  and running, if you plan to use skills that spin up a local cluster (such
  as `opensearch-launchpad`).
- AWS credentials configured with appropriate permissions if you plan to
  use the `aws-setup` skill. For guidance on required permissions,
  see [Identity-based policies](ac.md#ac-types-identity "ac.md#ac-types-identity").

## Install and use skills

Skills install through the [`skills`](https://agentskills.io "https://agentskills.io") CLI, which you invoke with `npx`. The
installer detects your agent and places skill files in the correct location.

To install the entire collection:

```
npx skills add opensearch-project/opensearch-agent-skills
```

To install a single skill, use the `@skill-name` suffix. The
`--full-depth` flag includes all reference material the agent may need
for follow-up questions:

```
npx skills add opensearch-project/opensearch-agent-skills@opensearch-launchpad --full-depth
npx skills add opensearch-project/opensearch-agent-skills@log-analytics --full-depth
npx skills add opensearch-project/opensearch-agent-skills@trace-analytics --full-depth
npx skills add opensearch-project/opensearch-agent-skills@aws-setup --full-depth
```

Common install options:

**`-a `agent-name``**

Install to a specific agent, for example
`-a claude-code`.

**`-g`**

Install globally so the skill is available across all projects on
your machine.

**`--all`**

Install to every agent the CLI detects on your machine.

After installation, restart your agent so it picks up the new skill files. Then
try a prompt such as _"I want to build a hybrid search app with
OpenSearch."_ The agent reads the skill instructions and runs
the required scripts directly.

The `aws-setup` skill includes dedicated guides for both OpenSearch Service product
families. For Amazon OpenSearch Service managed domains, the skill walks through creating a domain,
configuring access policies, and connecting your application (see [Introduction](what-is.md "what-is.md")). For OpenSearch Serverless, it covers creating a collection, configuring
data access and encryption policies, and ingesting data (see [Amazon OpenSearch Serverless](serverless.md "serverless.md")). For interactive queries against a running cluster,
pair the skills with the [OpenSearch MCP server](opensearch-mcp-server.md "opensearch-mcp-server.md").

## Security considerations

When you install and run a skill, your agent executes the scripts and commands it
describes. Treat skills as you would any third-party developer tool:

- Review the skill's `SKILL.md` file in the [source repository](https://github.com/opensearch-project/opensearch-agent-skills "https://github.com/opensearch-project/opensearch-agent-skills") before installing.
- Run skills in a development or sandbox environment before pointing them
  at production resources.
- Use least-privilege IAM credentials when running the
  `aws-setup` skill, scoped to the AWS account and AWS Region
  where you intend to deploy.
- Review any AWS resources the skill creates before committing to
  long-lived infrastructure. Skills may provision domains, collections, IAM
  roles, and networking resources on your behalf.

## Additional resources

- [opensearch-agent-skills](https://github.com/opensearch-project/opensearch-agent-skills "https://github.com/opensearch-project/opensearch-agent-skills") on GitHub – Source, issues, and
  the developer guide for authoring new skills.
- [Agent Skills
  specification](https://agentskills.io/specification "https://agentskills.io/specification") – The open standard that skills
  implement.
- [OpenSearch MCP server](opensearch-mcp-server.md "opensearch-mcp-server.md") – The companion MCP server
  for interactive queries against a running cluster.
