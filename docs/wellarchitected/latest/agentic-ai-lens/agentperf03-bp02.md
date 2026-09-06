

# AGENTPERF03-BP02 Optimize context window utilization and prompt management
<a name="agentperf03-bp02"></a>

 Every token sent to an LLM competes for the model's attention, consumes input-token cost, and adds inference latency, which makes prompt content a first-order performance lever. Effective context window management budgets tokens across prompt components, assembles only what the current task needs, and compresses or summarizes the rest. Without this discipline, conversation history and tool schemas crowd out reasoning capacity and inflate latency on every iteration. 

 **Desired outcome:** 
+  You have an explicit token budget allocated across prompt components, system instructions, conversation history, retrieved knowledge, and tool schemas, with per-component token usage measured on every request. 
+  You have context assembled dynamically per request, including only the tool definitions, retrieved passages, and conversation context relevant to the current task rather than a fixed maximal payload. 
+  You have conversation history bounded by summarization, sliding windows, or semantic compression so prompt size doesn't grow linearly with session length. 
+  You have prompt templates versioned and evaluated so changes to wording, ordering, or component composition are measured against quality and token-cost baselines before rollout. 

 **Common anti-patterns:** 
+  Including the full conversation history in every prompt without summarization or truncation, causing prompt size and inference latency to grow linearly with session length. 
+  Injecting the full tool catalog in every prompt regardless of task relevance, spending context budget on schemas the agent will not invoke for the current request. 
+  Passing RAG retrievals straight into the prompt without per-passage filtering or truncation, so low-relevance chunks displace more useful context. 
+  Treating the prompt as a single opaque string rather than a composition of components, making it impossible to attribute token consumption to system instructions, history, retrievals, or tool schemas. 
+  Shipping prompt changes without versioning or side-by-side evaluation, so quality or token-cost regressions are detected only after rollout. 

 **Benefits of establishing this best practice:** 
+  Removing tokens from the prompt can reduce request cost and shorten time-to-first-token on each iteration. 
+  Pruned, high-density context leaves more of the model's effective attention on the current task instead of parsing stale history or unused tool schemas. 
+  Summarization and sliding-window strategies decouple prompt size from conversation length, keeping per-turn latency and cost stable. 
+  Stable, component-structured prompts with invariant prefixes compose with prompt caching, turning a large portion of input tokens into cached reads at a fraction of standard input cost. 
+  Versioned templates with evaluation gates let prompt changes ship with quality and cost evidence rather than by guess. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Prompts behave as compositions of discrete components, system instructions, tool schemas, retrieved knowledge, conversation history, and the current user turn. Treating them as a single opaque string makes runaway growth impossible to attribute. Per-component token attribution on every request demystifies issues, such as a tool catalog that doubled when a new tool was registered. Component-level budgets that sum to the workload's input-length target make the trade-offs explicit: more budget for retrievals means less for history, and every reallocation becomes a deliberate decision. 

 The [Amazon Bedrock prompt design guidance](https://docs.aws.amazon.com/bedrock/latest/userguide/design-a-prompt.html) describes how clear instructions, output indicators, and question placement at the end of the prompt shape the system-instruction and user-turn components individually. 

 The cheapest tokens are the ones never sent. Most agents register many more tools than any single turn will invoke, so injecting the full tool catalog on every request spends context budget on schemas the model ignores. [Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-advanced-performance.html) addresses this with semantic search that returns only the tools relevant to the current user intent. 

 Retrieval-augmented context suffers from the same failure mode, passing raw top-K passages into the prompt without a relevance threshold or per-passage cap lets low-signal chunks displace higher-signal context. 

 Conversation history is the third inflation source: the [SummaryMemoryStrategy in Amazon Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/long-term-configuring-built-in-strategies.html#long-term-session-summaries-strategy) maintains a running per-session summary that replaces raw turns after the session exceeds a threshold, decoupling prompt size from session length so per-turn latency remains stable as conversations grow. 

 Static prefixes unlock large, recurring input-token savings. [Amazon Bedrock prompt caching](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html) accepts cache checkpoints in the system, tools, and messages fields on the Converse API, with cache reads charged at a reduced rate on a 5-minute default TTL, or a 1-hour TTL on Claude Opus 4.5, Haiku 4.5, and Sonnet 4.5 for longer-running or intermittent agent traffic. 

 Invariant content (system instructions, stable tool definitions, and pinned context) belongs before the checkpoint, and variable content (current user turn and session-specific retrievals) belongs after it so the cached prefix remains identical across turns. Simplified cache management for Claude models looks back approximately 20 content blocks for the longest matching prefix, so the most-reused content should sit within that range. 

 Prompts behave like code, so a change to wording, component order, or a tool description can shift quality, token count, and cache-hit rate simultaneously, while the effects remain invisible until rollout unless they are measured. [Amazon Bedrock Prompt management](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-create.html) stores prompts as versioned artifacts with variables, inference configuration, and optional prompt-caching settings, and its console variant comparison surfaces quality and token differences side by side before promotion. 

 [Prompt Optimization](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-optimize.html) generates model-specific rewrites that serve as candidate variants rather than drop-in replacements, and quality plus token-cost benchmarks on representative test sets should gate promotion of any variant. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Define the prompt component taxonomy and per-component token budget:** Decompose every prompt into a fixed set of components, system instructions, tool schemas, retrieved knowledge, conversation history, and the current user turn, and allocate a token budget to each that sums to the input-length target derived from the workload's latency and cost SLO. Apply the [Amazon Bedrock prompt design guidance](https://docs.aws.amazon.com/bedrock/latest/userguide/design-a-prompt.html) to keep the system-instruction component clear, concise, and consistent with the user query placed at the end of the prompt. 

1.  **Instrument per-component token usage on every request:** Emit token counts for each component as structured logs or CloudWatch metrics alongside the inputTokens and outputTokens returned by the [Amazon Bedrock Converse API](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html), dimensioned by agent ID and task type. Include cacheReadInputTokens and cacheWriteInputTokens from the Converse response so cache effectiveness is measured alongside component growth, and alert when any component trends outside its budget before it impacts the end-to-end SLO. 

1.  **Assemble tool schemas dynamically with just-in-time selection:** Replace full-catalog injection with task-relevant selection so the prompt carries only the tools the agent might invoke for the current turn. For agents using [Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-advanced-performance.html), enable semantic search by setting "searchType": "SEMANTIC" on the mcp protocol in the gateway's protocolConfiguration so tool retrieval narrows on user intent. Keep each tool's schema compact with clear parameter descriptions and required fields to reduce its per-invocation token weight. 

1.  **Bound conversation history with summarization and a sliding window:** Cap raw-turn retention and replace older turns with a running summary after the session exceeds a threshold expressed in turns or tokens. Configure the [SummaryMemoryStrategy in Amazon Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/long-term-configuring-built-in-strategies.html#long-term-session-summaries-strategy) with a namespaceTemplates entry such as /summaries/{actorId}/{sessionId}/ and inject the summary rather than the raw transcript into the prompt, paired with a small sliding window of recent turns to preserve near-term conversational detail. 

1.  **Filter and truncate retrieved passages before prompt assembly:** Apply a relevance threshold, a per-passage token cap, and a total retrieval budget so low-signal chunks can't displace higher-signal context. Rank passages by relevance score, drop any below the threshold, and truncate long passages to the per-passage cap before composing the retrieved-knowledge component. 

1.  **Structure prompts so they compose with prompt caching:** Order every prompt so invariant content (system instructions, stable tool definitions, pinned reference material) appears before variant content (user turn, per-request retrievals), then place [Amazon Bedrock prompt cache checkpoints](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html) in the system, tools, and messages fields at the boundary between static and dynamic content. For long-running or intermittent sessions on supported Claude models, set "ttl": "1h" on the cachePoint to extend the cache window beyond the 5-minute default, keeping the 1-hour entry ahead of any 5-minute entries in the same request. 

1.  **Version prompts and gate changes on evaluation:** Store prompts as versioned artifacts in [Amazon Bedrock Prompt management](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-create.html) with variables for dynamic inputs and inference configuration tied to the version, then use [Create version](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-version-create.html) to snapshot known-good drafts. Use the side-by-side variant comparison in the prompt builder to evaluate candidates against each other, and promote a new version only after it clears quality and token-cost baselines on a representative test set. 

1.  **Generate model-tuned rewrites with prompt optimization:** Run candidate prompts through [Amazon Bedrock Prompt Optimization](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-optimize.html) to produce model-specific rewrites, passing the target model through targetModelId when using the OptimizePrompt API. Treat the optimized output as a candidate variant rather than a drop-in replacement, and compare it against the original on the same evaluation set so token-count reductions are weighed against any quality impact before promotion. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTPERF03-BP01 Implement tiered memory management systems](agentperf03-bp01.html) 
+  [AGENTPERF03-BP03 Optimize RAG retrieval pipelines for latency and precision](agentperf03-bp03.html) 
+  [AGENTPERF03-BP04 Establish efficient agent caching and data access patterns](agentperf03-bp04.html) 
+  [AGENTPERF06-BP01 Design optimized tool integration strategies](agentperf06-bp01.html) 

 **Related documents:** 
+  [Amazon Bedrock, Prompt caching for faster model inference](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html) 
+  [Amazon Bedrock, Create a prompt using Prompt management](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-create.html) 
+  [Amazon Bedrock, Create a version of a prompt in Prompt management](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-version-create.html) 
+  [Amazon Bedrock, Optimize a prompt](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-optimize.html) 
+  [Amazon Bedrock, Design a prompt](https://docs.aws.amazon.com/bedrock/latest/userguide/design-a-prompt.html) 
+  [AgentCore Gateway, Performance optimization (refined tool schemas and semantic search)](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-advanced-performance.html) 
+  [AgentCore Memory, Long-term built-in strategies (semantic, episodic, summary, user preference)](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/long-term-configuring-built-in-strategies.html) 
+  [Foundations of agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-foundations/introduction.html) 

 **Related services:** 
+  [Amazon Bedrock](https://aws.amazon.com/bedrock/) 
+  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) 