# AgentCore CLI reference

This reference documents the public Amazon Bedrock AgentCore CLI releases.

###### Topics

- [Project Lifecycle](#cli-project-lifecycle "#cli-project-lifecycle")
- [Invocation & Runtime](#cli-invocation "#cli-invocation")
- [Resource Management](#cli-resources "#cli-resources")
- [Evaluation & Datasets](#cli-evaluation "#cli-evaluation")
- [Optimization & Config Bundles](#cli-optimization "#cli-optimization")
- [Operations & Settings](#cli-operations "#cli-operations")

## Project Lifecycle

_Auto-generated from `@aws/agentcore` v0.28.1 — do not edit by hand._

### agentcore create

```
agentcore create [options]
```

Create a new AgentCore project

**Parameters**

`--name <name>`
_(optional)_

Resource name [non-interactive]

`--project-name <name>`
_(optional)_

Project name (start with letter, alphanumeric only, max 23 chars) [non-interactive]

`--no-agent`
_(optional)_

Skip agent creation [non-interactive]

`--defaults`
_(optional)_

Create a harness project with default settings (this is the default) [non-interactive]

`--build <type>`
_(optional)_

Build type: CodeZip or Container (default: CodeZip) [non-interactive]

`--language <language>`
_(optional)_

Target language: Python or TypeScript (default: Python) [non-interactive]

`--framework <framework>`
_(optional)_

Agent framework (Strands, LangChain\_LangGraph, GoogleADK, OpenAIAgents, VercelAI) [non-interactive]

`--model-provider <provider>`
_(optional)_

Model provider (Bedrock, Anthropic, OpenAI, Gemini) [non-interactive]

`--api-key <key>`
_(optional)_

API key for non-Bedrock providers [non-interactive]

`--memory <option>`
_(optional)_

Memory option (none, shortTerm, longAndShortTerm) [non-interactive]

`--protocol <protocol>`
_(optional)_

Protocol: HTTP, MCP, A2A, AGUI (default: HTTP) [non-interactive]

`--type <type>`
_(optional)_

Agent type: create or import (default: create) [non-interactive]

`--agent-id <id>`
_(optional)_

Bedrock Agent ID (required for --type import) [non-interactive]

`--agent-alias-id <id>`
_(optional)_

Bedrock Agent Alias ID (required for --type import) [non-interactive]

`--region <region>`
_(optional)_

The AWS Region for Bedrock Agent (required for --type import) [non-interactive]

`--network-mode <mode>`
_(optional)_

Network mode (PUBLIC, VPC) [non-interactive]

`--subnets <ids>`
_(optional)_

Comma-separated subnet IDs (required for VPC mode) [non-interactive]

`--security-groups <ids>`
_(optional)_

Comma-separated security group IDs (required for VPC mode) [non-interactive]

`--vpc-id <id>`
_(optional)_

VPC ID (required for Container builds with VPC mode) [non-interactive]

`--idle-timeout <seconds>`
_(optional)_

Idle session timeout in seconds (60-28800) [non-interactive]

`--max-lifetime <seconds>`
_(optional)_

Max instance lifetime in seconds (60-28800) [non-interactive]

`--session-storage-mount-path <path>`
_(optional)_

Absolute mount path for session filesystem storage under /mnt (for example, /mnt/data) [non-interactive]

`--efs-access-point-arn <arn>`
_(optional)_

EFS access point ARN (repeatable, paired with --efs-mount-path) [non-interactive] (default: [])

`--efs-mount-path <path>`
_(optional)_

EFS mount path (for example, /mnt/tools, paired with --efs-access-point-arn) [non-interactive] (default: [])

`--s3-access-point-arn <arn>`
_(optional)_

S3 Files access point ARN (repeatable, paired with --s3-mount-path) [non-interactive] (default: [])

`--s3-mount-path <path>`
_(optional)_

S3 Files mount path (for example, /mnt/datasets, paired with --s3-access-point-arn) [non-interactive] (default: [])

`--with-config-bundle`
_(optional)_

Create a config bundle wired into the agent template [non-interactive]

`--output-dir <dir>`
_(optional)_

Output directory (default: current directory) [non-interactive]

`--skip-git`
_(optional)_

Skip git repository initialization [non-interactive]

`--skip-python-setup`
_(optional)_

Skip Python virtual environment setup [non-interactive]

`--skip-install`
_(optional)_

Skip all dependency installation (npm install, uv sync) [non-interactive]

`--dry-run`
_(optional)_

Preview what would be created without making changes [non-interactive]

`--json`
_(optional)_

Output as JSON [non-interactive]

`--model-id <id>`
_(optional)_

Model ID for harness [non-interactive]

`--api-key-arn <arn>`
_(optional)_

API key ARN for non-Bedrock harness providers [non-interactive]

`--api-base <url>`
_(optional)_

Base URL for the harness model provider API endpoint (lite\_llm) [non-interactive]

`--additional-params <json>`
_(optional)_

Provider-specific harness params as a JSON object (lite\_llm) [non-interactive]

`--no-harness-memory`
_(optional)_

Disable memory for the harness (this is the default) [non-interactive]

`--max-iterations <n>`
_(optional)_

Max agent loop iterations (harness) [non-interactive]

`--max-tokens <n>`
_(optional)_

Max tokens per iteration (harness) [non-interactive]

`--timeout <seconds>`
_(optional)_

Max execution duration in seconds (harness) [non-interactive]

`--truncation-strategy <strategy>`
_(optional)_

Truncation strategy: sliding\_window or summarization (harness) [non-interactive]

`--container <uri-or-path>`
_(optional)_

Container image URI or Dockerfile path (harness) [non-interactive]

### agentcore deploy

```
agentcore deploy|dp [options]
```

Deploy project infrastructure to AWS via CDK.

**Parameters**

`--target <target>`
_(optional)_

Deployment target name (default: "default") [non-interactive]

`-y, --yes`
_(optional)_

Auto-confirm prompts, read credentials from env [non-interactive]

`-v, --verbose`
_(optional)_

Show resource-level deployment events [non-interactive]

`--json`
_(optional)_

Output as JSON [non-interactive]

`--dry-run`
_(optional)_

Preview deployment without deploying [non-interactive]

`--diff`
_(optional)_

Show CDK diff without deploying [non-interactive]

### agentcore dev

```
agentcore dev|d [options] [prompt]
```

Launch local dev server, or invoke an agent locally.

**Parameters**

`prompt`

Send a prompt to a running dev server [non-interactive]

`-p, --port <port>`
_(optional)_

Port for development server. Used as-is when set explicitly; the default is offset by the runtime index in multi-runtime projects. (default: "8080")

`-r, --runtime <name>`
_(optional)_

Runtime to run or invoke (required if multiple runtimes)

`-s, --stream`
_(optional)_

Stream response when invoking [non-interactive]

`-l, --logs`
_(optional)_

Run dev server with logs to stdout [non-interactive]

`--exec`
_(optional)_

Execute a shell command in the running dev container (Container agents only) [non-interactive]

`--tool <name>`
_(optional)_

MCP tool name (used with "call-tool" prompt) [non-interactive]

`--input <json>`
_(optional)_

MCP tool arguments as JSON (used with --tool) [non-interactive]

`--skip-deploy`
_(optional)_

Skip automatic resource deployment before starting dev server

`-H, --header <header>`
_(optional)_

Custom header to forward to the agent (format: "Name: Value", repeatable) [non-interactive] (default: [])

`-b, --no-browser`
_(optional)_

Use terminal TUI instead of web-based chat UI

`--no-traces`
_(optional)_

Disable local OTEL trace collection

### agentcore package

```
agentcore package|pkg [options]
```

Package agent artifacts without deploying.

**Parameters**

`-d, --directory <path>`
_(optional)_

Project directory containing agentcore config

`-r, --runtime <name>`
_(optional)_

Package only the specified runtime

### agentcore export

```
agentcore export [options] [command]
```

Export a harness to a Strands runtime agent.

### agentcore update

```
agentcore update [options] [command]
```

Check for and install CLI updates

**Parameters**

`-c, --check`
_(optional)_

Check for updates without installing

### agentcore validate

```
agentcore validate [options]
```

Validate agentcore/ config files.

**Parameters**

`-d, --directory <path>`
_(optional)_

Project directory containing agentcore config

`--json`
_(optional)_

Output as JSON [non-interactive]

## Invocation & Runtime

_Auto-generated from `@aws/agentcore` v0.28.1 — do not edit by hand._

### agentcore invoke

```
agentcore invoke|i [options] [prompt]
```

Invoke a deployed agent endpoint.

**Parameters**

`prompt`

Prompt to send to the agent. Also accepts piped stdin when no prompt is provided and stdin is not a TTY [non-interactive]

`--prompt <text>`
_(optional)_

Prompt to send to the agent [non-interactive]

`--prompt-file <path>`
_(optional)_

Read the prompt from a file (for long or structured payloads that exceed shell arg limits) [non-interactive]

`--runtime <name>`
_(optional)_

Select specific runtime [non-interactive]

`--gateway <name>`
_(optional)_

Invoke through a gateway [non-interactive]

`--gateway-target-name <name>`
_(optional)_

HTTP runtime target on the gateway [non-interactive]

`--target <name>`
_(optional)_

Select deployment target [non-interactive]

`--session-id <id>`
_(optional)_

Use specific session ID for conversation continuity

`--user-id <id>`
_(optional)_

User ID for runtime invocation (default: "default-user")

`--api-base <url>`
_(optional)_

The LiteLLM API base URL override for harness invocations. Available only with `lite_llm` in non-interactive mode.

`--additional-params <json>`
_(optional)_

The additional LiteLLM parameters, as a JSON object, for harness invocations. Available only with `lite_llm` in non-interactive mode.

`--payment-user-id <id>`
_(optional)_

End-user/wallet-owner identity (defaults to --user-id)

`--payment-instrument-id <id>`
_(optional)_

Payment instrument (wallet) ID

`--payment-session-id <id>`
_(optional)_

Payment session ID for budget tracking

`--auto-session`
_(optional)_

Auto-create/reuse a payment session for testing

`--json`
_(optional)_

Output as JSON

`--stream`
_(optional)_

Stream response in real-time

`--tool <name>`
_(optional)_

MCP tool name (use with "call-tool" prompt)

`--input <json>`
_(optional)_

MCP tool arguments as JSON (use with --tool)

`--exec`
_(optional)_

Execute a shell command in the runtime container

`--timeout <seconds>`
_(optional)_

Timeout in seconds for --exec commands

`-H, --header <header>`
_(optional)_

Custom header "Name: Value" (repeatable)

`--bearer-token <token>`
_(optional)_

Bearer token for CUSTOM\_JWT auth (bypasses SigV4)

`--harness <name>`
_(optional)_

Select specific harness to invoke

`--harness-arn <arn>`
_(optional)_

Invoke a harness by ARN (no project required)

`--region <region>`
_(optional)_

The AWS Region (required with --harness-arn)

`--verbose`
_(optional)_

Print verbose streaming JSON events

`--model-id <id>`
_(optional)_

Override model

`--model-provider <provider>`
_(optional)_

The model provider. Valid values: `bedrock`, `open_ai`, or `gemini`.

`--api-key-arn <arn>`
_(optional)_

API key ARN for open\_ai/gemini

`--tools <tools>`
_(optional)_

Override tools (comma-separated)

`--allowed-tools <tools>`
_(optional)_

Override allowed tools (comma-separated)

`--skills <paths>`
_(optional)_

Skills (comma-separated paths)

`--system-prompt <text>`
_(optional)_

Override system prompt

`--actor-id <id>`
_(optional)_

Override memory actor ID

`--max-iterations <n>`
_(optional)_

Override max iterations

`--max-tokens <n>`
_(optional)_

Override max tokens

`--harness-timeout <seconds>`
_(optional)_

Override timeout seconds

### agentcore exec

```
agentcore exec [options] [command...]
```

Open an interactive shell or run a one-shot command in a deployed agent container.

**Parameters**

`command`

Command to execute (one-shot mode, non-interactive)

`--it`
_(optional)_

Open an interactive PTY shell session

`--runtime <name|arn>`
_(optional)_

Target agent name or runtime ARN (skips agent picker)

`--harness <name|arn>`
_(optional)_

Target harness name or harness ARN (skips agent picker)

`--session-id <id>`
_(optional)_

Pin to a specific runtime session / VM

`--shell-id <id>`
_(optional)_

Reconnect to an existing shell

`--region <region>`
_(optional)_

The AWS Region

`--bearer-token <token>`
_(optional)_

Bearer token for CUSTOM\_JWT authentication (skips SigV4)

`--target <name>`
_(optional)_

Deployment target name (from agentcore.json)

`--timeout <seconds>`
_(optional)_

Timeout in seconds for one-shot commands

`--json`
_(optional)_

Output result as JSON (one-shot mode only, incompatible with --it)

### agentcore run

```
agentcore run [options] [command]
```

Run evaluations, batch evaluations, or optimization recommendations.

### agentcore logs

```
agentcore logs|l [options] [command]
```

Stream or search agent runtime logs.

**Parameters**

`--runtime <name>`
_(optional)_

Select specific runtime

`--since <time>`
_(optional)_

Start time — defaults to 1h ago in search mode (for example, "1h", "30m", "2d", ISO 8601)

`--until <time>`
_(optional)_

End time — defaults to now in search mode (for example, "now", ISO 8601)

`--level <level>`
_(optional)_

Filter by log level (error, warn, info, debug)

`-n, --limit <count>`
_(optional)_

Maximum number of log lines to return

`--query <text>`
_(optional)_

Server-side text filter

`--json`
_(optional)_

Output as JSON Lines

### agentcore traces

```
agentcore traces|t [options] [command]
```

View and download agent traces.

### agentcore status

```
agentcore status|s [options]
```

Show deployed resource details and status.

**Parameters**

`--runtime-id <id>`
_(optional)_

Look up a specific runtime by ID

`--target <name>`
_(optional)_

Select deployment target

`--type <type>`
_(optional)_

Filter by resource type (agent, runtime-endpoint, memory, credential, gateway, evaluator, online-eval, payment, policy-engine, policy, config-bundle, dataset, knowledge-base, harness)

`--state <state>`
_(optional)_

Filter by deployment state (deployed, local-only, pending-removal)

`--runtime <name>`
_(optional)_

Filter to a specific runtime

`--name <name>`
_(optional)_

Show details for a single resource by name (knowledge-base)

`--json`
_(optional)_

Output as JSON

### agentcore fetch

```
agentcore fetch [options] [command]
```

Fetch access info for deployed resources.

### agentcore view

```
agentcore view [options] [command]
```

View job history and details

## Resource Management

_Auto-generated from `@aws/agentcore` v0.28.1 — do not edit by hand._

### agentcore add

```
agentcore add [options] [command] [subcommand]
```

Add resources to project config.

### agentcore remove

```
agentcore remove [options] [command] [subcommand]
```

Remove resources from project config.

### agentcore import

```
agentcore import [options] [command]
```

Import a runtime, memory, or starter toolkit into this project.

**Parameters**

`--source <path>`
_(optional)_

Path to the .bedrock\_agentcore.yaml configuration file

`--target <target>`
_(optional)_

Deployment target name (only needed if project has multiple targets)

`-y, --yes`
_(optional)_

Auto-confirm prompts

## Evaluation & Datasets

_Auto-generated from `@aws/agentcore` v0.28.1 — do not edit by hand._

### agentcore evals

```
agentcore evals [options] [command]
```

View saved eval and batch eval results from past runs.

### agentcore batch-evaluations

```
agentcore batch-evaluations [options] [command] <id>
```

View batch evaluation jobs and their results.

**Parameters**

`id`

Batch evaluation job ID to view

`--json`
_(optional)_

Output as JSON

### agentcore dataset

```
agentcore dataset [options] [command]
```

Manage dataset content and versions

## Optimization & Config Bundles

_Auto-generated from `@aws/agentcore` v0.28.1 — do not edit by hand._

### agentcore config-bundle

```
agentcore config-bundle|cb [options] [command]
```

Manage configuration bundles (use bundle name from agentcore.json, not the ID)

### agentcore promote

```
agentcore promote [options] [command]
```

Promote resources

### agentcore archive

```
agentcore archive [options] [command]
```

Archive (delete) a batch evaluation or recommendation on the service and clear local history.

## Operations & Settings

_Auto-generated from `@aws/agentcore` v0.28.1 — do not edit by hand._

### agentcore pause

```
agentcore pause [options] [command]
```

Pause a deployed resource (online eval config, A/B test).

### agentcore resume

```
agentcore resume [options] [command]
```

Resume a paused resource (online eval config, A/B test).

### agentcore stop

```
agentcore stop [options] [command]
```

Stop a running batch evaluation or A/B test.

### agentcore config

```
agentcore config [options] [key] [value]
```

Adjust global configuration settings such as telemetry opt-out status

**Parameters**

`key`

Config key in dot notation (for example, telemetry.enabled)

`value`

Value to set

### agentcore telemetry

```
agentcore telemetry [options] [command]
```

Manage anonymous usage analytics preferences.

### agentcore feedback

```
agentcore feedback [options] [message]
```

Send feedback about the AgentCore CLI to the team.

**Parameters**

`message`

Feedback message [non-interactive]

`--screenshot <path>`
_(optional)_

Path to a PNG or JPG screenshot (max 100MB) [non-interactive]

`--json`
_(optional)_

Output result as JSON [non-interactive]
