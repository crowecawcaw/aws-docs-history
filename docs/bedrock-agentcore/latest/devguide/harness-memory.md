# Persist memory and filesystem

The harness persists state at two layers: conversation state in [AgentCore Memory](memory.md "memory.md"), and file state on the agent’s filesystem.

**Memory.** Attach an [AgentCore Memory](memory.md "memory.md") instance to the harness and every invocation saves the conversation automatically, scoped by session ID (and additionally by actor ID, if provided). On subsequent invocations with the same session ID, the agent’s history is loaded from Memory before it reasons, so it remembers what happened in previous turns, even after the underlying microVM session has expired. You do not need to pass previous messages yourself; just send the new message.

- **Short-term memory** captures raw events (messages, tool calls) within a session.
- **Long-term memory** extracts durable knowledge via configurable strategies ([semantic](semantic-memory-strategy.md "semantic-memory-strategy.md"), [summarization](summary-strategy.md "summary-strategy.md"), [user preference](user-preference-memory-strategy.md "user-preference-memory-strategy.md"), [episodic](episodic-memory-strategy.md "episodic-memory-strategy.md"), or [custom](memory-custom-strategy.md "memory-custom-strategy.md")) and makes them retrievable via semantic search in later sessions.
- **Actor ID** - identifies the entity interacting with the agent (a user, another agent, or a system). Memory events are scoped by actorId + sessionId, so each actor has isolated memory. Long-term retrieval uses actorId as a template variable in
  namespace paths (e.g. /summary/{actorId}/{sessionId}/), mapping to the configured memory strategies.

**Filesystem.** If enabled, each session runs in a Firecracker microVM with a working filesystem. Files written during a session persist through the session’s lifetime. For state that needs to outlast a single session, mount S3-backed storage through [AgentCore Runtime file system configurations](runtime-filesystem-configurations.md "runtime-filesystem-configurations.md").

## Add memory

###### Example

AgentCore CLI
When you create a harness with `agentcore create`, long-term memory is enabled by default - the CLI creates a memory resource and wires it to the harness automatically. To skip it, pass `--no-harness-memory`:

```
# Create with memory (default)
agentcore create --name myagent

# Create without memory
agentcore create --name myagent --no-harness-memory
```

After creation, deploy to provision the memory resource:

```
agentcore deploy
```

To scope memory to a specific user, pass `--actor-id` at invoke time. Each actor gets isolated memory - the agent remembers that user’s context even across different sessions:

```
# Session 1: user Alice asks a question
agentcore invoke --harness research-agent \
  --session-id "$(uuidgen)" \
  --actor-id alice \
  "Research tropical vacations under $3k"

# Session 2 (new session): Alice's memory carries over
agentcore invoke --harness research-agent \
  --session-id "$(uuidgen)" \
  --actor-id alice \
  "What did we decide about the Portugal option?"
```

Continue a conversation within the same session by reusing the same session ID:

```
SESSION_ID="$(uuidgen)"
agentcore invoke --harness research-agent \
  --session-id "$SESSION_ID" \
  "Research tropical vacations under $3k"
agentcore invoke --harness research-agent \
  --session-id "$SESSION_ID" \
  "What did we decide about the Portugal option?"
```

AWS CLI/boto3
Create a memory instance:

```
aws bedrock-agentcore-control create-memory \
  --name "MyMemory" \
  --event-expiry-duration 30 \
  --description "Memory for my harness"
```

Attach it to the harness:

```
aws bedrock-agentcore-control update-harness \
  --harness-id "MyHarness-UuFdkQoXSL" \
  --memory '{"optionalValue": {"agentCoreMemoryConfiguration": {"arn": "arn:aws:bedrock-agentcore:us-west-2:123456789012:memory/MyMemory-abc123"}}}'
```

Reuse the same `runtimeSessionId` across invocations and the agent recalls prior turns from Memory, even after the microVM session expires.

To scope memory to a specific user, pass `actorId` at invoke time:

```
response = client.invoke_harness(
    harnessArn=HARNESS_ARN,
    runtimeSessionId=SESSION_ID,
    actorId="user-123",
    messages=[{"role": "user", "content": [{"text": "What do you remember about my preferences?"}]}],
)
```

The `actorId` determines whose memory is loaded. Long-term memory strategies (semantic, summarization, etc.) use the actorId to scope extracted knowledge - each actor gets their own isolated memory namespace. For more details on configuring long-term memory, see [configuring long-term memory strategies](long-term-configuring-built-in-strategies.md "long-term-configuring-built-in-strategies.md").

## Long-term memory retrieval

When you attach a Memory instance that has active strategies (semantic, user preference, episodic, etc.), the harness automatically derives a retrieval configuration from those strategies. This means long-term memory retrieval works out of the box - you don’t need to manually specify a `retrievalConfig`.

**How it works:**

- When you create or update a harness with a Memory ARN, the service reads the Memory instance’s active strategies and automatically configures retrieval for each strategy’s namespaces with default parameters (`topK=10`, `relevanceScore=0.2`).
- On each invocation, the agent queries these namespaces for relevant long-term memories and injects them into the conversation context before reasoning.

**Override the defaults:** If you explicitly provide a `retrievalConfig` in the memory configuration, your values take priority and no automatic derivation occurs. This lets you customize which namespaces are queried, adjust `topK` or `relevanceScore`, or disable retrieval for specific strategies.

```
aws bedrock-agentcore-control update-harness \
  --harness-id "MyHarness-UuFdkQoXSL" \
  --memory '{"optionalValue": {"agentCoreMemoryConfiguration": {"arn": "arn:aws:bedrock-agentcore:us-west-2:123456789012:memory/MyMemory-abc123", "retrievalConfig": {"/facts/{actorId}/": {"topK": 5, "relevanceScore": 0.5, "strategyId": "FactExtractor-abc123"}}}}}'
```

###### Important

If you update your Memory instance’s strategies (add or remove) after creating the harness, call `UpdateHarness` to refresh the retrieval configuration. Invocations will continue to work with the previous configuration until updated.

## Filesystem

Mount S3-backed persistent storage that survives session termination. Files written to the mount path persist across session restarts when using the same `runtimeSessionId`.

###### Example

AgentCore CLI
Configure at create time or add to an existing harness:

```
# At create time
agentcore create --name myagent --session-storage /mnt/data/

# Or add to an existing harness
agentcore add harness --name my-agent --session-storage /mnt/data/
agentcore deploy
```

AWS CLI/boto3

```
aws bedrock-agentcore-control update-harness \
  --harness-id "MyHarness-UuFdkQoXSL" \
  --environment '{"agentCoreRuntimeEnvironment": {"filesystemConfigurations": [{"sessionStorage": {"mountPath": "/mnt/data/"}}]}}'
```

Learn more: [AgentCore Memory](memory.md "memory.md"), [create a memory store](memory-create-a-memory-store.md "memory-create-a-memory-store.md"), [long-term memory strategies](long-term-configuring-built-in-strategies.md "long-term-configuring-built-in-strategies.md"), [file system configurations on Runtime](runtime-filesystem-configurations.md "runtime-filesystem-configurations.md").

### Related topics

- [Configure agents and models](harness-config-and-models.md "harness-config-and-models.md") - configure models and system prompts
- [Environment and Skills](harness-environment.md "harness-environment.md") - bring your own container with persistent storage mounts
- [Control cost with limits](harness-operations.md#harness-limits "harness-operations.md#harness-limits") - execution limits
- [API Documentation](harness-get-started.md#api-documentation "harness-get-started.md#api-documentation")
