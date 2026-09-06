

# Export harness to code
<a name="harness-export"></a>

Export harness to code takes a managed harness configuration and generates the equivalent agent as editable Python source code using the Strands framework. The generated agent is a normal AgentCore runtime agent: you own the code, can modify it freely, and deploy it like any other agent. The generated agent mirrors the harness’s model, tools, skills, memory, execution limits, and filesystem mounts.

## When to Use Export
<a name="_when_to_use_export"></a>

Use export when you have a working harness and want to:
+  **Customize beyond what the harness config allows** - add custom tool logic, change the agent loop, inject middleware/hooks, or integrate libraries the harness doesn’t expose
+  **Own the code** - move from a declarative config to source code you control, review, and version like the rest of your application.
+  **Graduate a prototype** - start fast with a harness, then export when you’re ready to invest in a hand-maintained agent.

If the harness configuration already does everything you need, you don’t have to export - keep running it as a harness.

## What is supported today
<a name="_what_is_supported_today"></a>
+  **Framework** - Strands, with other frameworks like Claude Agents SDK coming soon
+  **Language** - Python only
+  **Build types** - CodeZip (default) and Container

Harness features carried into the generated agent:
+ Model provider and config (Bedrock, OpenAI, Gemini - including model ID and API key references)
+ Tools - Remote MCP tools, Gateways, inline function tools, AgentCore Browser, AgentCore Code Interpreter, built-in `shell` and `file_operations` tools
+ Memory
+ Execution limits
+ Conversation truncation
+ Skills (Path, S3, Git)
+ Filesystem mounts (session storage, EFS, S3) for VPC harnesses
+ Authorizer configuration

## CLI Usage
<a name="_cli_usage"></a>

### Command Syntax
<a name="_command_syntax"></a>

**Example**  

```
agentcore export harness --arn <arn> [options]
```

### Options
<a name="_options"></a>


| Flag | Description | Default | 
| --- | --- | --- | 
|  `--arn <arn>`  | ARN of the harness to export (use when exporting a harness created outside the current CLI project) |  `arn` or `name` required | 
|  `--name <name>`  | Name of the harness to export (use when exporting a harness created in the same CLI project) |  `arn` or `name` required | 
|  `--target-agent-name <name>`  | Name for the generated runtime agent |  `<harnessName>Agent`  | 
|  `--build <type>`  | Build type: `CodeZip` or `Container`  |  `CodeZip`  | 
|  `--json`  | Output results as JSON | False | 

### Examples
<a name="_examples"></a>

Basic export with defaults:

**Example**  

```
# Export harness with ARN - generates MyHarnessAgent using CodeZip
agentcore export harness --arn arn:aws:bedrock-agentcore:us-east-1:123456789012:harness/MyHarness
# Export harness created within CLI project - generates MyHarnessAgent using CodeZip
agentcore export harness --name MyHarness
# Export with a custom agent name
agentcore export harness --name MyHarness --target-agent-name MyProductionAgent
# Export as a Container build (generates Dockerfile)
agentcore export harness --name MyHarness --build Container
```
Run `agentcore export harness` without `--name` to launch the interactive export wizard.  

1. If the project has more than one harness, select the harness to export. (With a single harness, the wizard skips this step.)  
![Select the harness to export](http://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/images/tui/harness-export-01-select.png)

1. Enter a name for the generated runtime agent, or accept the default `<harness>Agent` .  
![Name the generated runtime agent](http://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/images/tui/harness-export-02-name.png)

1. Choose the build type: **CodeZip** (package Python source as a zip, the default) or **Container** (build a Docker image via ECR and CodeBuild).  
![Select the build type](http://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/images/tui/harness-export-03-build.png)

1. Review the export configuration and confirm.  
![Review and confirm the export](http://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/images/tui/harness-export-04-confirm.png)
After export, review `EXPORT_NOTES.md` , then run `agentcore deploy` to deploy the generated agent.

### After export
<a name="_after_export"></a>

Deploy the generated runtime agent using the AgentCore CLI.

**Example**  

```
agentcore deploy
```

The exported agent is added as a normal runtime, so it deploys alongside the rest of your AgentCore CLI project.

## EXPORT\_NOTES.md
<a name="_export_notes_md"></a>

After every export, `EXPORT_NOTES.md` is written listing items requiring manual follow-up. Export writes notes to EXPORT\_NOTES.md in the agent directory listing each item, why it needs attention, and exactly what to do. Always read EXPORT\_NOTES.md before deploying.

## Deployment Options
<a name="_deployment_options"></a>

After exporting, you can deploy your agent to multiple hosting environments:
+  **AgentCore Runtime (managed)** - Use `agentcore deploy` to host in the AgentCore Runtime, which manages infrastructure, scaling, and credential provisioning automatically.
+  **Self-hosted** - Deploy the generated Python agent anywhere that supports Python 3.12\+:
  +  AWS services: Lambda, ECS/Fargate, EC2
  + Kubernetes clusters
  + On-premise servers
  + Any containerized environment