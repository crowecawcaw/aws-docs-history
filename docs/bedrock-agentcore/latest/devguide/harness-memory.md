

# Memory
<a name="harness-memory"></a>

When memory is enabled, the harness persists conversation state in [AgentCore Memory](memory.md). On subsequent invocations with the same session ID, the agent loads the stored history before it reasons.

## How memory works
<a name="_how_memory_works"></a>
+  **Short-term memory** captures raw events (messages, tool calls) within a session. This is what gives the agent continuity across turns.
+  **Long-term memory** extracts durable knowledge via configurable strategies ([semantic](semantic-memory-strategy.md), [summarization](summary-strategy.md), [user preference](user-preference-memory-strategy.md), [episodic](episodic-memory-strategy.md), or [custom](memory-custom-strategy.md)) and makes them retrievable via semantic search in later sessions.
+  **Actor ID** identifies the entity interacting with the agent (a user, another agent, or a system). Memory events are scoped by actorId \+ sessionId, so each actor has isolated memory. Long-term retrieval uses actorId as a template variable in namespace paths (e.g. `/summary/{actorId}/{sessionId}/`), mapping to the configured memory strategies.

## Managed memory
<a name="_managed_memory"></a>

When you create a harness directly with the service API and omit the memory configuration, the service provisions managed memory. The AgentCore CLI uses the same default: new CLI harnesses use managed memory unless you pass `--memory` with the `disabled` or `existing` mode.

**Memory charges**  
There is no additional charge for the harness itself. Managed Memory incurs standard AgentCore Memory charges for short-term events, stored long-term memory records, and retrieval requests. To avoid persistent Memory charges, disable Memory when you create the harness. For more information, see [Understand harness costs](harness-operations.md#harness-costs) and [Amazon Bedrock AgentCore pricing](https://aws.amazon.com/bedrock/agentcore/pricing/).

To customize the managed memory at create time:

**Example**  

```
aws bedrock-agentcore-control create-harness \
  --harness-name "MyHarness" \
  --execution-role-arn "arn:aws:iam::123456789012:role/MyHarnessRole" \
  --memory '{"managedMemoryConfiguration": {"strategies": ["SEMANTIC", "SUMMARIZATION", "USER_PREFERENCE"], "eventExpiryDuration": 60}}'
```
To update strategies on an existing harness:  

```
aws bedrock-agentcore-control update-harness \
  --harness-id "MyHarness-UuFdkQoXSL" \
  --memory '{"optionalValue": {"managedMemoryConfiguration": {"strategies": ["SEMANTIC", "SUMMARIZATION", "USER_PREFERENCE", "EPISODIC"]}}}'
```
Create an empty project, then add a harness with managed memory:  

```
agentcore create --name MyHarnessProject --template empty
cd MyHarnessProject
agentcore add harness \
  --name myagent \
  --memory '{"mode":"managed","strategies":["SEMANTIC","SUMMARIZATION"],"eventExpiryDuration":30}'
agentcore deploy
```
To create a harness without memory, run the following command instead of the preceding `agentcore add harness` command:  

```
agentcore add harness \
  --name no_memory \
  --memory '{"mode":"disabled"}'
```

Managed memory is fully managed by the harness:
+ Strategy configuration is controlled through `UpdateHarness`. You can still read/write events and query records directly through the Memory APIs.
+ Managed memory cannot be deleted directly through the Memory APIs. To turn managed memory into a regular AgentCore memory resource, you can disassociate it from the harness in two ways:
  + Use `UpdateHarness` to switch to BYO (`agentCoreMemoryConfiguration`) or disabled.
  + Pass `deleteManagedMemory=false` on deletion to disassociate instead - `DeleteHarness` cascade-deletes the managed memory by default.

Managed memory uses the AgentCore Memory [built-in strategies](built-in-strategies.md) that you select. AgentCore Memory handles extraction and consolidation for these strategies, including the choice of model. You can’t set a model on managed memory, and extraction and consolidation don’t use the harness model. To choose the model for extraction and consolidation, use BYO memory instead. For more information, see [Control which models a harness uses](#harness-memory-fixed-models).

### Available strategies
<a name="_available_strategies"></a>


| Strategy | Description | 
| --- | --- | 
|  `SEMANTIC`  | Extracts factual knowledge from conversations, retrievable via semantic search. | 
|  `SUMMARIZATION`  | Creates running summaries of conversations, scoped by actor and session. | 
|  `USER_PREFERENCE`  | Captures user preferences and settings expressed during conversations. | 
|  `EPISODIC`  | Records significant events and experiences as discrete episodes. | 

## Add existing memory (BYO)
<a name="harness-memory-byo"></a>

For configuration that managed memory doesn’t provide, attach an existing [AgentCore Memory](memory.md) instance instead. For example, you might need custom namespace templates. You might also need one memory shared by multiple harnesses, or a specific model for long-term memory extraction.

To choose the model for extraction and consolidation, configure the memory with a [built-in with overrides strategy](memory-custom-strategy.md) that sets `modelId` on every step that the strategy runs. For the configuration format, see [Configure a custom strategy](long-term-configuring-custom-strategies.md).

Managed memory already accepts `encryptionKeyArn` for a customer managed key in AWS Key Management Service (AWS KMS). You cannot change the key after creation.

**Example**  
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
  --memory '{"optionalValue": {"agentCoreMemoryConfiguration": {"arn": "arn:aws:bedrock-agentcore:us-west-2:123456789012:memory/MyMemory-abc1234567"}}}'
```

```
agentcore create --name MyHarnessProject --template empty
cd MyHarnessProject
agentcore add harness \
  --name myagent \
  --memory '{"mode":"existing","arn":"arn:aws:bedrock-agentcore:us-west-2:123456789012:memory/MyMemory-abc1234567"}'
agentcore deploy
```
To use a memory that the same project declares, reference it by name instead of by ARN:  

```
agentcore add memory --name MyMemory
agentcore add harness \
  --name myagent \
  --memory '{"mode":"existing","name":"MyMemory"}'
agentcore deploy
```
A by-name reference also accepts `retrievalConfig`, and `agentcore export harness` can wire it into the exported agent. A reference by ARN supports neither.

## Disable memory
<a name="harness-memory-disable"></a>

To disable memory entirely:

```
aws bedrock-agentcore-control update-harness \
  --harness-id "MyHarness-UuFdkQoXSL" \
  --memory '{"optionalValue": {"disabled": {}}}'
```

## Per-user memory scoping with actor ID
<a name="_per_user_memory_scoping_with_actor_id"></a>

Pass `actorId` at invoke time to scope memory to a specific user. Each actor gets isolated short-term and long-term memory:

```
response = client.invoke_harness(
    harnessArn=HARNESS_ARN,
    runtimeSessionId=SESSION_ID,
    actorId="user-123",
    messages=[{"role": "user", "content": [{"text": "What do you remember about my preferences?"}]}],
)
```

## Long-term memory retrieval
<a name="_long_term_memory_retrieval"></a>

When a harness has active memory strategies (managed or BYO), retrieval works automatically - the harness derives a retrieval configuration from the Memory instance’s active strategies. On each invocation, the agent queries relevant long-term memories and injects them into the conversation context before reasoning.

 **Default behavior:** 
+ Retrieval is configured automatically with default parameters (`topK=10`, `relevanceScore=0.2`) for each active strategy’s namespace.
+ No manual configuration needed for either managed or BYO memory.

 **Override the defaults:** If you explicitly provide a `retrievalConfig` in the BYO memory configuration, your values take priority and no automatic derivation occurs. This lets you customize which namespaces are queried, adjust `topK` or `relevanceScore`, or disable retrieval for specific strategies.

```
aws bedrock-agentcore-control update-harness \
  --harness-id "MyHarness-UuFdkQoXSL" \
  --memory '{"optionalValue": {"agentCoreMemoryConfiguration": {"arn": "arn:aws:bedrock-agentcore:us-west-2:123456789012:memory/MyMemory-abc1234567", "retrievalConfig": {"/facts/{actorId}/": {"topK": 5, "relevanceScore": 0.5, "strategyId": "FactExtractor-abc123"}}}}}'
```

**Important**  
If you update your BYO Memory instance’s strategies (add or remove) after attaching it to a harness, call `UpdateHarness` to refresh the retrieval configuration. For managed memory, strategy changes through `UpdateHarness` refresh the configuration automatically.

## Context truncation
<a name="harness-context-truncation"></a>

When conversation history grows beyond the model’s context window, the harness applies a truncation strategy. Configure truncation on the harness with `CreateHarness` or `UpdateHarness`.
+ The `sliding_window` strategy keeps the most recent N messages. It is simple and predictable.
+ The `summarization` strategy, the current default, compresses older messages into a summary, so you preserve more context in fewer tokens.
+ The `none` strategy doesn’t truncate the conversation history, so use it only if you manage context size yourself.

The following AWS CLI `update-harness` command sets the `sliding_window` strategy and its settings on the harness. Replace {{MyHarness-UuFdkQoXSL}} with your harness ID.

```
aws bedrock-agentcore-control update-harness \
  --harness-id "MyHarness-UuFdkQoXSL" \
  --truncation '{"strategy": "sliding_window", "config": {"slidingWindow": {"messagesCount": 30}}}'
```

If you don’t configure truncation on the harness, the harness uses the current service default strategy and settings. If you set a strategy without its settings, the harness uses the current default settings for that strategy. These defaults can change.

Currently, the `summarization` truncation strategy generates the summary with the harness model, or with the per-invocation model override if you pass one. This behavior can change. You can’t set a separate model for summarization. The `summarization` truncation strategy is separate from the `SUMMARIZATION` long-term memory strategy.

Learn more: [AgentCore Memory](memory.md), [create a memory store](memory-create-a-memory-store.md), [long-term memory strategies](long-term-configuring-built-in-strategies.md).

## Control which models a harness uses
<a name="harness-memory-fixed-models"></a>

To choose the models that the harness and its long-term memory use, complete the following steps. The `summarization` truncation strategy currently uses the harness model, so these steps also determine the model for summaries.

1. Attach BYO memory in which every strategy is a built-in with overrides strategy that sets `modelId` on every step that the strategy runs. For these strategies, AgentCore Memory uses a memory execution role to call Amazon Bedrock in your AWS account, so the calls count against your Amazon Bedrock quotas and are charged to your account. For more information, see [Amazon Bedrock capacity for built-in with overrides strategies](bedrock-capacity.md).

1. Set `model` on the harness, and don’t pass a per-invocation model override.

1. Set `truncation` on the harness with both the strategy and its settings.

**Note**  
Step 1 requires BYO memory because you can’t set a model on managed memory. To attach BYO memory, see [Add existing memory (BYO)](#harness-memory-byo). Instead of step 1, you can disable memory. For more information, see [Disable memory](#harness-memory-disable).  
If no model is configured, the harness uses the current service default, which can change. Omitting `model` on an update keeps the existing configuration.  
Step 3 decides whether the harness generates summaries at all. Only the `summarization` truncation strategy generates summaries, and it currently uses the harness model from step 2.

The following AWS CLI `update-harness` command completes steps 2 and 3 by setting the harness model and the `summarization` truncation strategy with its settings:

```
aws bedrock-agentcore-control update-harness \
  --harness-id "MyHarness-UuFdkQoXSL" \
  --model '{
    "bedrockModelConfig": {
      "modelId": "global.anthropic.claude-sonnet-4-6"
    }
  }' \
  --truncation '{
    "strategy": "summarization",
    "config": {
      "summarization": {
        "summaryRatio": 0.3,
        "preserveRecentMessages": 10
      }
    }
  }'
```

Replace {{MyHarness-UuFdkQoXSL}} with your harness ID, and replace {{global.anthropic.claude-sonnet-4-6}} with the model ID that you want to use.

For information about how updates affect harness versions and endpoints, see [AgentCore harness versioning and endpoints](harness-versioning.md). `GetHarness` returns effective values, including service defaults, so its response doesn’t show whether a value is one that you set or a service default.

## Related topics
<a name="_related_topics"></a>
+  [Models and instructions](harness-models.md) - configure models and system prompts
+  [Environment and filesystem](harness-environment.md) - environment, filesystem, and custom containers
+  [Skills](harness-skills.md) - attach skills from Git, S3, or AWS Skills
+  [Security and access controls](harness-security.md) - execution role policies for memory access
+  [API Documentation](harness-get-started.md#api-documentation) 