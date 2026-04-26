# Configure agents and models

Define a harness once with defaults for model, system prompt, tools, memory, and execution limits. Override any of those on a single invocation when you want to experiment. The harness resource stays unchanged; only that call uses the overrides.

This is the core of the config-based model: **defaults at creation time, overrides at invocation time.** You can test N model/prompt/tool combinations in the time it would take to redeploy once.

###### Example

AgentCore CLI
Set defaults when you create or update the harness:

```
# Create a project if one does not already exist.
agentcore create

# Add a harness to the project
agentcore add harness \
  --name research-agent \
  --model-id us.anthropic.claude-sonnet-4-6-20250514-v1:0 \
  --system-prompt "You are a research assistant." \
  --tools agentcore-browser

agentcore deploy
```

Override on an invocation:

```
# Switch the model for one call
agentcore invoke --harness research-agent \
  --model-id us.anthropic.claude-opus-4-5-20251101-v1:0 \
  "Summarize this research paper"

# Swap tools for one call
agentcore invoke --harness research-agent \
  --tools agentcore-browser,code-interpreter \
  "Plot the citation counts as a bar chart"
```

Overridable at invoke time: `--model-id`, `--tools`, `--system-prompt`, `--max-iterations`, `--max-tokens`, `--harness-timeout`, `--skills`, `--allowed-tools`, `--actor-id`. Add `--verbose` to print raw streaming JSON events for debugging.

To change defaults permanently, edit `app/<name>/harness.json` and run `agentcore deploy`.

AWS CLI/boto3
Defaults on `create-harness`:

```
aws bedrock-agentcore-control create-harness \
  --harness-name "research-agent" \
  --execution-role-arn "arn:aws:iam::123456789012:role/MyHarnessRole" \
  --system-prompt '[{"text": "You are a research assistant."}]' \
  --tools '[{"type": "agentcore_browser", "name": "browser"}]'
```

Overrides per invocation:

```
response = client.invoke_harness(
    harnessArn=HARNESS_ARN,
    runtimeSessionId=SESSION_ID,
    # These apply only to this call; the harness defaults stay intact
    model={"bedrockModelConfig": {"modelId": "us.anthropic.claude-opus-4-5-20251101-v1:0"}},
    systemPrompt=[{"text": "You are a terse research assistant. One paragraph answers only."}],
    tools=[
        {"type": "agentcore_browser", "name": "browser"},
        {"type": "agentcore_code_interpreter", "name": "code_interpreter"},
    ],
    messages=[{"role": "user", "content": [{"text": "Summarize this paper as a bullet list."}]}],
)
```

To change defaults permanently, use `update-harness`.

## Use any model, switch mid-session

Use models from Amazon Bedrock, OpenAI, Google Gemini, or any OpenAI-compatible endpoint (coming soon). Switch providers between turns of the same session and the conversation continues. Context carries over.

If you don’t specify a model, the harness defaults to Anthropic’s Claude Sonnet 4.6 on Amazon Bedrock (`global.anthropic.claude-sonnet-4-6`) so you can get started immediately. You can change the default or override per invocation at any time.

Store third-party API keys in [AgentCore Identity’s](identity.md "identity.md") token vault as an API key credential provider. The harness pulls the key at invocation time. Your agent code never sees raw credentials.

###### Example

AgentCore CLI
Add an API key to [AgentCore Identity](identity.md "identity.md"):

```
agentcore add credential --type api-key --name my-openai-key --api-key $OPENAI_API_KEY
agentcore deploy
```

Invoke with the OpenAI key you just added:

```
agentcore invoke --harness my-agent \
  --model-provider open_ai \
  --model-id gpt-5.4 \
  --api-key-arn arn:aws:bedrock-agentcore:us-west-2:123456789012:token-vault/default/apikeycredentialprovider/my-openai-key \
  --session-id "$(uuidgen)" \
  "Analyze this codebase and identify performance bottlenecks."
```

Switch back to Bedrock on the same session:

```
agentcore invoke --harness my-agent \
  --model-id us.anthropic.claude-sonnet-4-5-20250514-v1:0 \
  --session-id "$(uuidgen)" \
  "Now suggest fixes for the top three issues."
```

AWS CLI/boto3
Register an API key with [AgentCore Identity](identity.md "identity.md"):

```
aws bedrock-agentcore-control create-api-key-credential-provider \
  --name my-openai-key \
  --api-key "$OPENAI_API_KEY"
```

Switch providers across turns of the same session:

```
# Turn 1: Bedrock
response = client.invoke_harness(
    harnessArn=HARNESS_ARN,
    runtimeSessionId=SESSION_ID,
    model={"bedrockModelConfig": {"modelId": "us.anthropic.claude-sonnet-4-5-20250514-v1:0"}},
    messages=[{"role": "user", "content": [{"text": "Analyze this codebase."}]}],
)

# Turn 2: OpenAI on the same session
response = client.invoke_harness(
    harnessArn=HARNESS_ARN,
    runtimeSessionId=SESSION_ID,
    model={
        "openAiModelConfig": {
            "modelId": "gpt-5.4",
            "apiKeyArn": "arn:aws:bedrock-agentcore:us-west-2:123456789012:token-vault/default/apikeycredentialprovider/my-openai-key",
        }
    },
    messages=[{"role": "user", "content": [{"text": "Now suggest fixes for the top three issues."}]}],
)
```

Learn more: [AgentCore Identity](identity.md "identity.md"), [API key credential providers](identity-api-key.md "identity-api-key.md").

For additional information on harness configuration, see the [API Documentation](harness-get-started.md#api-documentation "harness-get-started.md#api-documentation")

### Related topics

- [Connect to tools](harness-tools.md "harness-tools.md") - connect tools to your harness
- [Persist memory and filesystem](harness-memory.md "harness-memory.md") - persist conversations across sessions
- [Control cost with limits](harness-operations.md#harness-limits "harness-operations.md#harness-limits") - set execution limits and truncation strategies
