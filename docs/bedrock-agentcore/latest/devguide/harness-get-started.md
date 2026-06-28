# Get started

You can use the harness through the [AgentCore CLI](https://github.com/aws/agentcore-cli "https://github.com/aws/agentcore-cli") or directly with AWS SDKs such as `boto3`. The CLI is the fastest path for most developers; SDKs are for programmatic use from your own application.

## Prerequisites

- AWS credentials configured in one of the [supported regions](agentcore-regions.md "agentcore-regions.md").
- For the CLI: Node.js 20+
- For the SDK/boto3: Python 3.10+, [`boto3` installed](../../../boto3/latest/guide/quickstart.md "../../../boto3/latest/guide/quickstart.md"), and an IAM execution role the harness can assume. See the [execution role policy](harness-security.md#harness-execution-role-policy "harness-security.md#harness-execution-role-policy") for minimum permissions.

## Get started

###### Example

AWS CLI/boto3
Create the harness with a name and execution role:

```
aws bedrock-agentcore-control create-harness \
  --harness-name "MyHarness" \
  --execution-role-arn "arn:aws:iam::123456789012:role/MyHarnessRole"
```

Poll `get-harness` until `"status": "READY"`. Note the `arn` in the response.

```
aws bedrock-agentcore-control get-harness \
  --harness-id "MyHarness-XyZ123"
```

Invoke from Python. If you don’t specify a model, the harness defaults to Anthropic Claude Sonnet 4.6 on Amazon Bedrock:

```
import boto3

client = boto3.client("bedrock-agentcore", region_name="us-west-2")

response = client.invoke_harness(
    harnessArn="arn:aws:bedrock-agentcore:us-west-2:123456789012:harness/MyHarness-XyZ123",  # Replace with your harness ARN
    runtimeSessionId="1234abcd-12ab-34cd-56ef-1234567890ab",
    messages=[{
        "role": "user",
        "content": [{"text": "Research three tropical vacation options under $3k."}]
    }],
)

for event in response["stream"]:
    if "contentBlockDelta" in event:
        delta = event["contentBlockDelta"].get("delta", {})
        if "text" in delta:
            print(delta["text"], end="", flush=True)
    elif "runtimeClientError" in event:
        print(f"\nError: {event['runtimeClientError']['message']}")
```

AgentCore CLI
Install the AgentCore CLI:

```
npm install -g @aws/agentcore
```

Create a harness project non-interactively with flags:

```
agentcore create --name myresearchagent --model-provider bedrock
```

Deploy and invoke:

```
agentcore deploy
agentcore invoke --harness myresearchagent \
  --session-id "$(uuidgen)" \
  "Research three tropical vacation options under $3k, within five hours of NYC."
```

The response streams to your terminal. Reuse the same `--session-id` across invocations to continue the conversation in the same environment.

To add more harnesses to an existing project, use `agentcore add harness`. To generate a standalone Python invoke script, add `--with-invoke-script`.

Useful flags:

- `--no-browser` (`-b`) - use the terminal TUI instead of the browser inspector
- `--logs` (`-l`) - run in non-interactive mode with logs to stdout
- `--port <port>` (`-p`) - set the dev server port (default 8080)
- `--no-traces` - disable local OTEL trace collection

Interactive
Install the AgentCore CLI:

```
npm install -g @aws/agentcore
```

Run `agentcore create` without flags to launch the interactive wizard:

```
agentcore create
```

1. Enter your project name:

![Create wizard: enter project name](images/tui/harness-01-create-project-name.png) 2. Select **Harness** as the project type:

![Create wizard: select project type](images/tui/harness-02-create-project-type.png) 3. Choose your model provider:

![Create wizard: select model provider](images/tui/harness-04-model-provider.png) 4. Choose your environment (default, container URI, or Dockerfile):

![Create wizard: select environment](images/tui/harness-05-custom-environment.png) 5. Configure memory:

![Create wizard: configure memory](images/tui/harness-06-memory.png) 6. Optionally configure advanced settings (tools, auth, network, lifecycle, limits, truncation, session storage):

![Create wizard: advanced settings](images/tui/harness-07-advanced-settings.png) 7. Review your configuration and confirm:

![Create wizard: review and confirm](images/tui/harness-08-confirm.png)

After confirmation, the wizard scaffolds your project. Deploy with `agentcore deploy`, then invoke with `agentcore invoke`.

Check project status at any time with `agentcore status`:

![AgentCore status dashboard](images/tui/harness-13-status.png)

1. Local development

If you want to test the harness in your local environment, you can run the dev server:

```
agentcore dev
```

When you run `agentcore dev`, the CLI first deploys your harness resources to AWS, creating the IAM role, harness, and any memory or credentials configured in your project:

![Deploy progress: CloudFormation resource creation](images/tui/common-deploy-progress.png)

Once deployment completes, it starts a local server and opens the agent inspector in your browser where you can chat with the harness, inspect traces, and browse project resources:

![Agent inspector: chat with your harness](images/tui/harness-agent-inspector.png)

Expand **Harness Settings** to view and override the harness configuration for the current session:

![Agent inspector: harness settings and configuration](images/tui/harness-agent-inspector-settings.png)

That’s all you need to get a harness running. The following sections cover everything you can configure.

###### Note

The `runtimeSessionId` must be at least 33 characters. Use a UUID or similar identifier. Reuse the same session ID across invocations to continue a conversation in the same environment.

## API Documentation

For additional details, see the API Reference:

- [CreateHarness API](../../../bedrock-agentcore-control/latest/APIReference/API_CreateHarness.md "../../../bedrock-agentcore-control/latest/APIReference/API_CreateHarness.md")
- [GetHarness API](../../../bedrock-agentcore-control/latest/APIReference/API_GetHarness.md "../../../bedrock-agentcore-control/latest/APIReference/API_GetHarness.md")
- [UpdateHarness API](../../../bedrock-agentcore-control/latest/APIReference/API_UpdateHarness.md "../../../bedrock-agentcore-control/latest/APIReference/API_UpdateHarness.md")
- [DeleteHarness API](../../../bedrock-agentcore-control/latest/APIReference/API_DeleteHarness.md "../../../bedrock-agentcore-control/latest/APIReference/API_DeleteHarness.md")
- [ListHarnesses API](../../../bedrock-agentcore-control/latest/APIReference/API_ListHarnesses.md "../../../bedrock-agentcore-control/latest/APIReference/API_ListHarnesses.md")
- [ListHarnessVersions API](../../../bedrock-agentcore-control/latest/APIReference/API_ListHarnessVersions.md "../../../bedrock-agentcore-control/latest/APIReference/API_ListHarnessVersions.md")
- [InvokeHarness API](../APIReference/API_InvokeHarness.md "../APIReference/API_InvokeHarness.md")
- [InvokeAgentRuntimeCommand API](../APIReference/API_InvokeAgentRuntimeCommand.md "../APIReference/API_InvokeAgentRuntimeCommand.md")
- [CreateHarnessEndpoint API](../../../bedrock-agentcore-control/latest/APIReference/API_CreateHarnessEndpoint.md "../../../bedrock-agentcore-control/latest/APIReference/API_CreateHarnessEndpoint.md")
- [GetHarnessEndpoint API](../../../bedrock-agentcore-control/latest/APIReference/API_GetHarnessEndpoint.md "../../../bedrock-agentcore-control/latest/APIReference/API_GetHarnessEndpoint.md")
- [UpdateHarnessEndpoint API](../../../bedrock-agentcore-control/latest/APIReference/API_UpdateHarnessEndpoint.md "../../../bedrock-agentcore-control/latest/APIReference/API_UpdateHarnessEndpoint.md")
- [DeleteHarnessEndpoint API](../../../bedrock-agentcore-control/latest/APIReference/API_DeleteHarnessEndpoint.md "../../../bedrock-agentcore-control/latest/APIReference/API_DeleteHarnessEndpoint.md")
- [ListHarnessesEndpoints API](../../../bedrock-agentcore-control/latest/APIReference/API_ListHarnessesEndpoint.md "../../../bedrock-agentcore-control/latest/APIReference/API_ListHarnessesEndpoint.md")

## Streaming response format

`InvokeHarness` returns a stream of events. The key event types are:

- `messageStart` - beginning of a new message (includes `role`)
- `contentBlockStart` - beginning of a content block (text, `toolUse`, or `toolResult`)
- `contentBlockDelta` - incremental content (`text`, `toolUse` input, `reasoningContent`)
- `contentBlockStop` - end of a content block
- `messageStop` - end of the message (includes `stopReason`)
- `metadata` - token usage and latency metrics
- `runtimeClientError` - error during execution

The `stopReason` in `messageStop` indicates why the agent stopped:

- `end_turn` - the agent finished normally
- `tool_use` - the agent is calling an inline function and waiting for a client-side result
- `max_tokens` - the model’s per-turn token limit was reached
- `max_iterations_exceeded` - the `maxIterations` limit was hit
- `timeout_exceeded` - the `timeoutSeconds` limit was hit
- `max_output_tokens_exceeded` - the `maxTokens` budget was exhausted
