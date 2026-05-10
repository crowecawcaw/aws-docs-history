# Environment and Skills

## Run commands on the environment

Not everything needs to go through the agent loop. `InvokeAgentRuntimeCommand` gives you direct shell access to the harness microVM: deterministic command execution with no model reasoning, no token cost, no ambiguity.

Use it to:

- Run deterministic pre-invocation or post-invocation scripts.
- Prepare the environment before an invocation: clone a repo, install dependencies, copy input files.
- Act on what the agent produced: run tests, commit and push, extract build artifacts.
- Inspect the VM during development: `ls`, `cat`, `env`, `python --version` without a round trip through the model.

###### Example

AgentCore CLI

```
# Install dependencies before the agent starts
agentcore invoke --exec --harness my-agent --session-id "$(uuidgen)" \
  "pip install pandas matplotlib"

# After the agent finishes, inspect what it created
agentcore invoke --exec --harness my-agent --session-id "$(uuidgen)" \
  "ls -la /tmp && cat /tmp/results.csv"
```

###### Note

The base environment includes Python and bash. For tools like `git`, `node`, or other runtimes, install them at session start (e.g. `apt-get install -y git`) or use a [custom environment](#harness-custom-container "#harness-custom-container").

In the TUI, press `!` to enter exec mode and run commands inline.

AWS CLI/boto3

```
response = client.invoke_agent_runtime_command(
    agentRuntimeArn=HARNESS_ARN,
    runtimeSessionId=SESSION_ID,
    body={"command": "ls -la /workspace"},
)

for event in response["stream"]:
    chunk = event.get("chunk", {})
    if "contentDelta" in chunk:
        delta = chunk["contentDelta"]
        if "stdout" in delta:
            print(delta["stdout"], end="", flush=True)
        if "stderr" in delta:
            print(delta["stderr"], end="", flush=True)
    elif "contentStop" in chunk:
        print(f"\n[exit code: {chunk['contentStop']['exitCode']}]")
```

See [InvokeAgentRuntimeCommand API](../APIReference/API_InvokeAgentRuntimeCommand.md "../APIReference/API_InvokeAgentRuntimeCommand.md") for details.

## Custom environment (container images)

The base environment includes Python and bash, enough for most tasks. When you need more, package your source code, dependencies, runtimes, and tools into a container image, push it to ECR, and reference it on the harness. Your agent runs in that exact environment. Pair custom images with `InvokeAgentRuntimeCommand` for session-specific setup that varies per invocation.

Container images must be built for the `linux/arm64` platform.

The harness overrides your container’s `ENTRYPOINT` and `CMD` to keep it running as an environment. Your installed software, filesystem, and environment variables are available to the agent; your container’s startup command is not executed. If you need a background process (such as a dev server), start it via `InvokeAgentRuntimeCommand` after the session begins.

###### Example

AgentCore CLI
Scaffold a harness with a Dockerfile:

```
agentcore create --name coding-agent --container ./Dockerfile
agentcore deploy
```

At deploy, the CLI builds the image, pushes to ECR, and attaches it to the harness.

Or reference a pre-built image:

```
agentcore create --name node-agent \
  --container public.ecr.aws/docker/library/node:slim
agentcore deploy
```

AWS CLI/boto3

```
aws bedrock-agentcore-control create-harness \
  --harness-name "CodingAgent" \
  --execution-role-arn "arn:aws:iam::123456789012:role/MyHarnessRole" \
  --environment-artifact '{"optionalValue": {"containerConfiguration": {"containerUri": "123456789012.dkr.ecr.us-west-2.amazonaws.com/my-dev-env:latest"}}}' \
  --system-prompt '[{"text": "You are an expert TypeScript developer."}]'
```

The execution role needs ECR pull permissions. See the [execution role policy](harness-security.md#harness-execution-role-policy "harness-security.md#harness-execution-role-policy") for details.

## Environment variables

Set environment variables that are passed to the runtime container. Environment variables are available to the agent and any custom container running in the session.

###### Example

AgentCore CLI
Set environment variables in `harness.json`:

```
{
  "environmentVariables": {
    "MY_API_URL": "https://api.example.com",
    "LOG_LEVEL": "debug"
  }
}
```

Run `agentcore deploy` to apply.

AWS CLI/boto3

```
aws bedrock-agentcore-control create-harness \
  --harness-name "MyHarness" \
  --execution-role-arn "arn:aws:iam::123456789012:role/MyHarnessRole" \
  --environment-variables '{"MY_API_URL": "https://api.example.com", "LOG_LEVEL": "debug"}'
```

## Agent Skills

[Agent Skills](https://strandsagents.com/docs/user-guide/concepts/plugins/skills/ "https://strandsagents.com/docs/user-guide/concepts/plugins/skills/") are bundles of markdown and scripts that give the agent domain knowledge on demand (e.g. how to work with Excel files, how to use a specific API). Skills must be present in the harness environment (the container filesystem) before they can be used. The `skills` parameter on the harness or at invoke time is a **pointer** to a path inside the environment - it does not upload or install the skill.

### Getting skills into the environment

**Bake into the container image** - include the skill directory in your custom image at a known path (e.g. `.agents/skills/xlsx`). Available to all invocations automatically. This is the recommended approach for production.

**Install at session start** - use `InvokeAgentRuntimeCommand` to install skills after the session begins, before invoking the agent:

```
agentcore invoke --exec --harness my-agent --session-id "$(uuidgen)" \
  "npx @anthropic-ai/agent-skills add xlsx github"
```

### Pointing the harness at installed skills

###### Example

AgentCore CLI
Persist skills on the harness:

```
agentcore add harness --name my-agent \
  --skill-path .agents/skills/xlsx \
  --skill-path .agents/skills/github
agentcore deploy
```

Skills configured this way are stored on the harness and passed to every invocation.

Override skills on a single invocation:

```
agentcore invoke --harness my-agent --skill-path .agents/skills/xlsx \
  "Find errors in the Excel files"
```

AWS CLI/boto3
Pass `skills` in the invoke call to override the harness-configured skills for that call only:

```
response = client.invoke_harness(
    harnessArn=HARNESS_ARN,
    runtimeSessionId=SESSION_ID,
    skills=[{"path": ".agents/skills/xlsx"}],
    messages=[{"role": "user", "content": [{"text": "Find errors in the Excel files"}]}],
)
```

### Related topics

- [Connect to tools](harness-tools.md "harness-tools.md") - connect MCP servers, Gateway, Browser, and Code Interpreter
- [Persist memory and filesystem](harness-memory.md "harness-memory.md") - persist conversations and files across sessions
- [Security and access controls](harness-security.md "harness-security.md") - execution roles and VPC configuration
- [API Documentation](harness-get-started.md#api-documentation "harness-get-started.md#api-documentation")
