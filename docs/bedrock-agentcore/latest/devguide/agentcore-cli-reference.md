

# AgentCore CLI reference
<a name="agentcore-cli-reference"></a>

This reference documents the public Amazon Bedrock AgentCore CLI releases.

**Topics**
+ [Project Lifecycle](#cli-project-lifecycle)
+ [Invocation & Runtime](#cli-invocation)
+ [Resource Management](#cli-resources)
+ [Evaluation & Datasets](#cli-evaluation)
+ [Optimization & Config Bundles](#cli-optimization)
+ [Operations & Settings](#cli-operations)

## Project Lifecycle
<a name="cli-project-lifecycle"></a>

 *Auto-generated from `@aws/agentcore` v0.28.1 — do not edit by hand.* 

### agentcore create
<a name="_agentcore_create"></a>

```
agentcore create [options]
```

Create a new AgentCore project

 **Parameters** 

 `--name <name>` *(optional)*   
Resource name [non-interactive]

 `--project-name <name>` *(optional)*   
Project name (start with letter, alphanumeric only, max 23 chars) [non-interactive]

 `--no-agent` *(optional)*   
Skip agent creation [non-interactive]

 `--defaults` *(optional)*   
Create a harness project with default settings (this is the default) [non-interactive]

 `--build <type>` *(optional)*   
Build type: CodeZip or Container (default: CodeZip) [non-interactive]

 `--language <language>` *(optional)*   
Target language: Python or TypeScript (default: Python) [non-interactive]

 `--framework <framework>` *(optional)*   
Agent framework (Strands, LangChain\_LangGraph, GoogleADK, OpenAIAgents, VercelAI) [non-interactive]

 `--model-provider <provider>` *(optional)*   
Model provider (Bedrock, Anthropic, OpenAI, Gemini) [non-interactive]

 `--api-key <key>` *(optional)*   
API key for non-Bedrock providers [non-interactive]

 `--memory <option>` *(optional)*   
Memory option (none, shortTerm, longAndShortTerm) [non-interactive]

 `--protocol <protocol>` *(optional)*   
Protocol: HTTP, MCP, A2A, AGUI (default: HTTP) [non-interactive]

 `--type <type>` *(optional)*   
Agent type: create or import (default: create) [non-interactive]

 `--agent-id <id>` *(optional)*   
Bedrock Agent ID (required for --type import) [non-interactive]

 `--agent-alias-id <id>` *(optional)*   
Bedrock Agent Alias ID (required for --type import) [non-interactive]

 `--region <region>` *(optional)*   
The AWS Region for Bedrock Agent (required for --type import) [non-interactive]

 `--network-mode <mode>` *(optional)*   
Network mode (PUBLIC, VPC) [non-interactive]

 `--subnets <ids>` *(optional)*   
Comma-separated subnet IDs (required for VPC mode) [non-interactive]

 `--security-groups <ids>` *(optional)*   
Comma-separated security group IDs (required for VPC mode) [non-interactive]

 `--vpc-id <id>` *(optional)*   
VPC ID (required for Container builds with VPC mode) [non-interactive]

 `--idle-timeout <seconds>` *(optional)*   
Idle session timeout in seconds (60-28800) [non-interactive]

 `--max-lifetime <seconds>` *(optional)*   
Max instance lifetime in seconds (60-28800) [non-interactive]

 `--session-storage-mount-path <path>` *(optional)*   
Absolute mount path for session filesystem storage under /mnt (for example, /mnt/data) [non-interactive]

 `--efs-access-point-arn <arn>` *(optional)*   
EFS access point ARN (repeatable, paired with --efs-mount-path) [non-interactive] (default: [])

 `--efs-mount-path <path>` *(optional)*   
EFS mount path (for example, /mnt/tools, paired with --efs-access-point-arn) [non-interactive] (default: [])

 `--s3-access-point-arn <arn>` *(optional)*   
S3 Files access point ARN (repeatable, paired with --s3-mount-path) [non-interactive] (default: [])

 `--s3-mount-path <path>` *(optional)*   
S3 Files mount path (for example, /mnt/datasets, paired with --s3-access-point-arn) [non-interactive] (default: [])

 `--with-config-bundle` *(optional)*   
Create a config bundle wired into the agent template [non-interactive]

 `--output-dir <dir>` *(optional)*   
Output directory (default: current directory) [non-interactive]

 `--skip-git` *(optional)*   
Skip git repository initialization [non-interactive]

 `--skip-python-setup` *(optional)*   
Skip Python virtual environment setup [non-interactive]

 `--skip-install` *(optional)*   
Skip all dependency installation (npm install, uv sync) [non-interactive]

 `--dry-run` *(optional)*   
Preview what would be created without making changes [non-interactive]

 `--json` *(optional)*   
Output as JSON [non-interactive]

 `--model-id <id>` *(optional)*   
Model ID for harness [non-interactive]

 `--api-key-arn <arn>` *(optional)*   
API key ARN for non-Bedrock harness providers [non-interactive]

 `--api-base <url>` *(optional)*   
Base URL for the harness model provider API endpoint (lite\_llm) [non-interactive]

 `--additional-params <json>` *(optional)*   
Provider-specific harness params as a JSON object (lite\_llm) [non-interactive]

 `--no-harness-memory` *(optional)*   
Disable memory for the harness (this is the default) [non-interactive]

 `--max-iterations <n>` *(optional)*   
Max agent loop iterations (harness) [non-interactive]

 `--max-tokens <n>` *(optional)*   
Max tokens per iteration (harness) [non-interactive]

 `--timeout <seconds>` *(optional)*   
Max execution duration in seconds (harness) [non-interactive]

 `--truncation-strategy <strategy>` *(optional)*   
Truncation strategy: sliding\_window or summarization (harness) [non-interactive]

 `--container <uri-or-path>` *(optional)*   
Container image URI or Dockerfile path (harness) [non-interactive]

### agentcore deploy
<a name="_agentcore_deploy"></a>

```
agentcore deploy|dp [options]
```

Deploy project infrastructure to AWS via CDK.

 **Parameters** 

 `--target <target>` *(optional)*   
Deployment target name (default: "default") [non-interactive]

 `-y, --yes` *(optional)*   
Auto-confirm prompts, read credentials from env [non-interactive]

 `-v, --verbose` *(optional)*   
Show resource-level deployment events [non-interactive]

 `--json` *(optional)*   
Output as JSON [non-interactive]

 `--dry-run` *(optional)*   
Preview deployment without deploying [non-interactive]

 `--diff` *(optional)*   
Show CDK diff without deploying [non-interactive]

### agentcore dev
<a name="_agentcore_dev"></a>

```
agentcore dev|d [options] [prompt]
```

Launch local dev server, or invoke an agent locally.

 **Parameters** 

 `prompt`   
Send a prompt to a running dev server [non-interactive]

 `-p, --port <port>` *(optional)*   
Port for development server. Used as-is when set explicitly; the default is offset by the runtime index in multi-runtime projects. (default: "8080")

 `-r, --runtime <name>` *(optional)*   
Runtime to run or invoke (required if multiple runtimes)

 `-s, --stream` *(optional)*   
Stream response when invoking [non-interactive]

 `-l, --logs` *(optional)*   
Run dev server with logs to stdout [non-interactive]

 `--exec` *(optional)*   
Execute a shell command in the running dev container (Container agents only) [non-interactive]

 `--tool <name>` *(optional)*   
MCP tool name (used with "call-tool" prompt) [non-interactive]

 `--input <json>` *(optional)*   
MCP tool arguments as JSON (used with --tool) [non-interactive]

 `--skip-deploy` *(optional)*   
Skip automatic resource deployment before starting dev server

 `-H, --header <header>` *(optional)*   
Custom header to forward to the agent (format: "Name: Value", repeatable) [non-interactive] (default: [])

 `-b, --no-browser` *(optional)*   
Use terminal TUI instead of web-based chat UI

 `--no-traces` *(optional)*   
Disable local OTEL trace collection

### agentcore package
<a name="_agentcore_package"></a>

```
agentcore package|pkg [options]
```

Package agent artifacts without deploying.

 **Parameters** 

 `-d, --directory <path>` *(optional)*   
Project directory containing agentcore config

 `-r, --runtime <name>` *(optional)*   
Package only the specified runtime

### agentcore export
<a name="_agentcore_export"></a>

```
agentcore export [options] [command]
```

Export a harness to a Strands runtime agent.

### agentcore update
<a name="_agentcore_update"></a>

```
agentcore update [options] [command]
```

Check for and install CLI updates

 **Parameters** 

 `-c, --check` *(optional)*   
Check for updates without installing

### agentcore validate
<a name="_agentcore_validate"></a>

```
agentcore validate [options]
```

Validate agentcore/ config files.

 **Parameters** 

 `-d, --directory <path>` *(optional)*   
Project directory containing agentcore config

 `--json` *(optional)*   
Output as JSON [non-interactive]

## Invocation & Runtime
<a name="cli-invocation"></a>

 *Auto-generated from `@aws/agentcore` v0.28.1 — do not edit by hand.* 

### agentcore invoke
<a name="_agentcore_invoke"></a>

```
agentcore invoke|i [options] [prompt]
```

Invoke a deployed agent endpoint.

 **Parameters** 

 `prompt`   
Prompt to send to the agent. Also accepts piped stdin when no prompt is provided and stdin is not a TTY [non-interactive]

 `--prompt <text>` *(optional)*   
Prompt to send to the agent [non-interactive]

 `--prompt-file <path>` *(optional)*   
Read the prompt from a file (for long or structured payloads that exceed shell arg limits) [non-interactive]

 `--runtime <name>` *(optional)*   
Select specific runtime [non-interactive]

 `--gateway <name>` *(optional)*   
Invoke through a gateway [non-interactive]

 `--gateway-target-name <name>` *(optional)*   
HTTP runtime target on the gateway [non-interactive]

 `--target <name>` *(optional)*   
Select deployment target [non-interactive]

 `--session-id <id>` *(optional)*   
Use specific session ID for conversation continuity

 `--user-id <id>` *(optional)*   
User ID for runtime invocation (default: "default-user")

 `--api-base <url>` *(optional)*   
The LiteLLM API base URL override for harness invocations. Available only with `lite_llm` in non-interactive mode.

 `--additional-params <json>` *(optional)*   
The additional LiteLLM parameters, as a JSON object, for harness invocations. Available only with `lite_llm` in non-interactive mode.

 `--payment-user-id <id>` *(optional)*   
End-user/wallet-owner identity (defaults to --user-id)

 `--payment-instrument-id <id>` *(optional)*   
Payment instrument (wallet) ID

 `--payment-session-id <id>` *(optional)*   
Payment session ID for budget tracking

 `--auto-session` *(optional)*   
Auto-create/reuse a payment session for testing

 `--json` *(optional)*   
Output as JSON

 `--stream` *(optional)*   
Stream response in real-time

 `--tool <name>` *(optional)*   
MCP tool name (use with "call-tool" prompt)

 `--input <json>` *(optional)*   
MCP tool arguments as JSON (use with --tool)

 `--exec` *(optional)*   
Execute a shell command in the runtime container

 `--timeout <seconds>` *(optional)*   
Timeout in seconds for --exec commands

 `-H, --header <header>` *(optional)*   
Custom header "Name: Value" (repeatable)

 `--bearer-token <token>` *(optional)*   
Bearer token for CUSTOM\_JWT auth (bypasses SigV4)

 `--harness <name>` *(optional)*   
Select specific harness to invoke

 `--harness-arn <arn>` *(optional)*   
Invoke a harness by ARN (no project required)

 `--region <region>` *(optional)*   
The AWS Region (required with --harness-arn)

 `--verbose` *(optional)*   
Print verbose streaming JSON events

 `--model-id <id>` *(optional)*   
Override model

 `--model-provider <provider>` *(optional)*   
The model provider. Valid values: `bedrock`, `open_ai`, or `gemini`.

 `--api-key-arn <arn>` *(optional)*   
API key ARN for open\_ai/gemini

 `--tools <tools>` *(optional)*   
Override tools (comma-separated)

 `--allowed-tools <tools>` *(optional)*   
Override allowed tools (comma-separated)

 `--skills <paths>` *(optional)*   
Skills (comma-separated paths)

 `--system-prompt <text>` *(optional)*   
Override system prompt

 `--actor-id <id>` *(optional)*   
Override memory actor ID

 `--max-iterations <n>` *(optional)*   
Override max iterations

 `--max-tokens <n>` *(optional)*   
Override max tokens

 `--harness-timeout <seconds>` *(optional)*   
Override timeout seconds

### agentcore exec
<a name="_agentcore_exec"></a>

```
agentcore exec [options] [command...]
```

Open an interactive shell or run a one-shot command in a deployed agent container.

 **Parameters** 

 `command`   
Command to execute (one-shot mode, non-interactive)

 `--it` *(optional)*   
Open an interactive PTY shell session

 `--runtime <name|arn>` *(optional)*   
Target agent name or runtime ARN (skips agent picker)

 `--harness <name|arn>` *(optional)*   
Target harness name or harness ARN (skips agent picker)

 `--session-id <id>` *(optional)*   
Pin to a specific runtime session / VM

 `--shell-id <id>` *(optional)*   
Reconnect to an existing shell

 `--region <region>` *(optional)*   
The AWS Region

 `--bearer-token <token>` *(optional)*   
Bearer token for CUSTOM\_JWT authentication (skips SigV4)

 `--target <name>` *(optional)*   
Deployment target name (from agentcore.json)

 `--timeout <seconds>` *(optional)*   
Timeout in seconds for one-shot commands

 `--json` *(optional)*   
Output result as JSON (one-shot mode only, incompatible with --it)

### agentcore run
<a name="_agentcore_run"></a>

```
agentcore run [options] [command]
```

Run evaluations, batch evaluations, or optimization recommendations.

### agentcore logs
<a name="_agentcore_logs"></a>

```
agentcore logs|l [options] [command]
```

Stream or search agent runtime logs.

 **Parameters** 

 `--runtime <name>` *(optional)*   
Select specific runtime

 `--since <time>` *(optional)*   
Start time — defaults to 1h ago in search mode (for example, "1h", "30m", "2d", ISO 8601)

 `--until <time>` *(optional)*   
End time — defaults to now in search mode (for example, "now", ISO 8601)

 `--level <level>` *(optional)*   
Filter by log level (error, warn, info, debug)

 `-n, --limit <count>` *(optional)*   
Maximum number of log lines to return

 `--query <text>` *(optional)*   
Server-side text filter

 `--json` *(optional)*   
Output as JSON Lines

### agentcore traces
<a name="_agentcore_traces"></a>

```
agentcore traces|t [options] [command]
```

View and download agent traces.

### agentcore status
<a name="_agentcore_status"></a>

```
agentcore status|s [options]
```

Show deployed resource details and status.

 **Parameters** 

 `--runtime-id <id>` *(optional)*   
Look up a specific runtime by ID

 `--target <name>` *(optional)*   
Select deployment target

 `--type <type>` *(optional)*   
Filter by resource type (agent, runtime-endpoint, memory, credential, gateway, evaluator, online-eval, payment, policy-engine, policy, config-bundle, dataset, knowledge-base, harness)

 `--state <state>` *(optional)*   
Filter by deployment state (deployed, local-only, pending-removal)

 `--runtime <name>` *(optional)*   
Filter to a specific runtime

 `--name <name>` *(optional)*   
Show details for a single resource by name (knowledge-base)

 `--json` *(optional)*   
Output as JSON

### agentcore fetch
<a name="_agentcore_fetch"></a>

```
agentcore fetch [options] [command]
```

Fetch access info for deployed resources.

### agentcore view
<a name="_agentcore_view"></a>

```
agentcore view [options] [command]
```

View job history and details

## Resource Management
<a name="cli-resources"></a>

 *Auto-generated from `@aws/agentcore` v0.28.1 — do not edit by hand.* 

### agentcore add
<a name="_agentcore_add"></a>

```
agentcore add [options] [command] [subcommand]
```

Add resources to project config.

### agentcore remove
<a name="_agentcore_remove"></a>

```
agentcore remove [options] [command] [subcommand]
```

Remove resources from project config.

### agentcore import
<a name="_agentcore_import"></a>

```
agentcore import [options] [command]
```

Import a runtime, memory, or starter toolkit into this project.

 **Parameters** 

 `--source <path>` *(optional)*   
Path to the .bedrock\_agentcore.yaml configuration file

 `--target <target>` *(optional)*   
Deployment target name (only needed if project has multiple targets)

 `-y, --yes` *(optional)*   
Auto-confirm prompts

## Evaluation & Datasets
<a name="cli-evaluation"></a>

 *Auto-generated from `@aws/agentcore` v0.28.1 — do not edit by hand.* 

### agentcore evals
<a name="_agentcore_evals"></a>

```
agentcore evals [options] [command]
```

View saved eval and batch eval results from past runs.

### agentcore batch-evaluations
<a name="_agentcore_batch_evaluations"></a>

```
agentcore batch-evaluations [options] [command] <id>
```

View batch evaluation jobs and their results.

 **Parameters** 

 `id`   
Batch evaluation job ID to view

 `--json` *(optional)*   
Output as JSON

### agentcore dataset
<a name="_agentcore_dataset"></a>

```
agentcore dataset [options] [command]
```

Manage dataset content and versions

## Optimization & Config Bundles
<a name="cli-optimization"></a>

 *Auto-generated from `@aws/agentcore` v0.28.1 — do not edit by hand.* 

### agentcore config-bundle
<a name="_agentcore_config_bundle"></a>

```
agentcore config-bundle|cb [options] [command]
```

Manage configuration bundles (use bundle name from agentcore.json, not the ID)

### agentcore promote
<a name="_agentcore_promote"></a>

```
agentcore promote [options] [command]
```

Promote resources

### agentcore archive
<a name="_agentcore_archive"></a>

```
agentcore archive [options] [command]
```

Archive (delete) a batch evaluation or recommendation on the service and clear local history.

## Operations & Settings
<a name="cli-operations"></a>

 *Auto-generated from `@aws/agentcore` v0.28.1 — do not edit by hand.* 

### agentcore pause
<a name="_agentcore_pause"></a>

```
agentcore pause [options] [command]
```

Pause a deployed resource (online eval config, A/B test).

### agentcore resume
<a name="_agentcore_resume"></a>

```
agentcore resume [options] [command]
```

Resume a paused resource (online eval config, A/B test).

### agentcore stop
<a name="_agentcore_stop"></a>

```
agentcore stop [options] [command]
```

Stop a running batch evaluation or A/B test.

### agentcore config
<a name="_agentcore_config"></a>

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
<a name="_agentcore_telemetry"></a>

```
agentcore telemetry [options] [command]
```

Manage anonymous usage analytics preferences.

### agentcore feedback
<a name="_agentcore_feedback"></a>

```
agentcore feedback [options] [message]
```

Send feedback about the AgentCore CLI to the team.

 **Parameters** 

 `message`   
Feedback message [non-interactive]

 `--screenshot <path>` *(optional)*   
Path to a PNG or JPG screenshot (max 100MB) [non-interactive]

 `--json` *(optional)*   
Output result as JSON [non-interactive]