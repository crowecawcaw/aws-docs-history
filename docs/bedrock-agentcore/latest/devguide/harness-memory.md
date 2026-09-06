

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

When you create a harness directly with the service API and omit the memory configuration, the service provisions managed memory. The AgentCore CLI uses a different default: new CLI harnesses have memory disabled unless you select managed memory or an existing memory resource.

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
agentcore create --project-name MyHarnessProject --no-agent
cd MyHarnessProject
agentcore add harness \
  --name myagent \
  --memory-mode managed \
  --memory-strategies SEMANTIC,SUMMARIZATION \
  --memory-event-expiry-days 30
agentcore deploy
```
Memory is disabled by default. To create the harness without memory, run the following command instead of the preceding `agentcore add harness` command:  

```
agentcore add harness --name myagent --no-memory
```
Run `agentcore` in a project directory, select **add** , then choose **Harness** . The wizard includes a memory step.  

1. On the **Memory** step, choose **No persistent memory** or **Enabled** to create persistent memory for the harness.  
![Memory step: No persistent memory or Enabled](http://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/images/tui/harness-memory-01-memory.png)

1. When memory is **Enabled** , an extra **Memory tuning** option appears in **Advanced settings** . Enable it with **Space** and press **Enter** to tune retrieval.  
![Advanced settings: Memory tuning option](http://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/images/tui/harness-memory-02-advanced-memory-tuning.png)

1. Optionally set the messages count, retrieval top K, and relevance score (each can be skipped).  
![Memory tuning: messages count, top K, relevance score](http://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/images/tui/harness-memory-03-messages-count.png)
Confirm the wizard, then run `agentcore deploy` to apply.

Managed memory is fully managed by the harness:
+ Strategy configuration is controlled through `UpdateHarness`. You can still read/write events and query records directly through the Memory APIs.
+ Managed memory cannot be deleted directly through the Memory APIs. To turn managed memory into a regular AgentCore memory resource, you can disassociate it from the harness in two ways:
  + Use `UpdateHarness` to switch to BYO (`agentCoreMemoryConfiguration`) or disabled.
  + Pass `deleteManagedMemory=false` on deletion to disassociate instead - `DeleteHarness` cascade-deletes the managed memory by default.

### Available strategies
<a name="_available_strategies"></a>


| Strategy | Description | 
| --- | --- | 
|  `SEMANTIC`  | Extracts factual knowledge from conversations, retrievable via semantic search. | 
|  `SUMMARIZATION`  | Creates running summaries of conversations, scoped by actor and session. | 
|  `USER_PREFERENCE`  | Captures user preferences and settings expressed during conversations. | 
|  `EPISODIC`  | Records significant events and experiences as discrete episodes. | 

## Add existing memory (BYO)
<a name="_add_existing_memory_byo"></a>

If you need advanced configuration beyond what managed memory provides - custom namespace templates, KMS encryption, or shared memory across multiple harnesses - attach an existing [AgentCore Memory](memory.md) instance instead.

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
  --memory '{"optionalValue": {"agentCoreMemoryConfiguration": {"arn": "arn:aws:bedrock-agentcore:us-west-2:123456789012:memory/MyMemory-abc123"}}}'
```

```
agentcore create --project-name MyHarnessProject --no-agent
cd MyHarnessProject
agentcore add harness --name myagent \
  --memory-arn "arn:aws:bedrock-agentcore:us-west-2:123456789012:memory/MyMemory-abc123"
agentcore deploy
```

## Disable memory
<a name="_disable_memory"></a>

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
  --memory '{"optionalValue": {"agentCoreMemoryConfiguration": {"arn": "arn:aws:bedrock-agentcore:us-west-2:123456789012:memory/MyMemory-abc123", "retrievalConfig": {"/facts/{actorId}/": {"topK": 5, "relevanceScore": 0.5, "strategyId": "FactExtractor-abc123"}}}}}'
```

**Important**  
If you update your BYO Memory instance’s strategies (add or remove) after attaching it to a harness, call `UpdateHarness` to refresh the retrieval configuration. For managed memory, strategy changes through `UpdateHarness` refresh the configuration automatically.

## Context truncation
<a name="_context_truncation"></a>

When conversation history grows beyond the model’s context window, the harness applies a truncation strategy. Configure this on the harness or override per invocation.
+  ** `sliding_window` ** (default) - keeps the most recent N messages. Simple and predictable.
+  ** `summarization` ** - compresses older messages into a summary, preserving more context in fewer tokens.
+  ** `none` ** - no truncation. Use only if you manage context size yourself.

```
aws bedrock-agentcore-control update-harness \
  --harness-id "MyHarness-UuFdkQoXSL" \
  --truncation '{"strategy": "sliding_window", "slidingWindowConfig": {"numMessages": 30}}'
```

Learn more: [AgentCore Memory](memory.md), [create a memory store](memory-create-a-memory-store.md), [long-term memory strategies](long-term-configuring-built-in-strategies.md).

### Related topics
<a name="_related_topics"></a>
+  [Models and instructions](harness-models.md) - configure models and system prompts
+  [Environment and filesystem](harness-environment.md) - environment, filesystem, and custom containers
+  [Skills](harness-skills.md) - attach skills from Git, S3, or AWS Skills
+  [Security and access controls](harness-security.md) - execution role policies for memory access
+  [API Documentation](harness-get-started.md#api-documentation) 