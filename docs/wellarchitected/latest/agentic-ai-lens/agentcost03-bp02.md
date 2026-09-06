

# AGENTCOST03-BP02 Cost optimize through intelligent compression and pruning of context windows
<a name="agentcost03-bp02"></a>

 In long-running agent sessions, raw conversation history can silently drive costs up, as every turn gets paid for again on every subsequent invocation. Compression, selective retrieval, and pruning keep context proportional to what the agent needs for the current decision rather than growing with session length. 

 **Desired outcome:** 
+  You compress older conversation turns into summaries so historical context doesn't multiply per-invocation token cost. 
+  You retrieve only the top-K most relevant memory items per reasoning step. 
+  You prune duplicates, superseded reasoning, and irrelevant tool results before each invocation. 
+  You monitor context window utilization and alert on sessions approaching overflow. 

 **Common anti-patterns:** 
+  Including full conversation history in every invocation regardless of task relevance, causing linear token cost growth with session length. 
+  Allowing raw interaction history to accumulate without compression, so context windows are dominated by historical turns with diminishing value. 
+  Deploying agents without context utilization monitoring, missing sessions that approach overflow thresholds and trigger costly re-invocation errors. 
+  Retrieving excessive RAG chunks or oversized chunk lengths when smaller, targeted retrievals would maintain reasoning quality at lower cost. 
+  Failing to prune duplicate or superseded information, paying tokens on content that doesn't contribute to the current reasoning task. 

 **Benefits of establishing this best practice:** 
+  History compression helps prevent linear token cost growth in long-running sessions, making persistent assistants economically viable. 
+  Selective retrieval includes only high-value context relevant to the current task, reducing token waste from marginally relevant data. 
+  Context window monitoring helps prevent overflow errors that trigger costly re-invocation with truncated context. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 [Amazon Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) separates short-term and long-term memory, which is the architectural pattern behind rolling summarization. Short-term memory holds raw recent turns, and long-term memory automatically extracts and consolidates key insights across sessions. For agents on AgentCore Runtime, this dual-tier behavior implements rolling summarization without custom code, and it is the difference between a persistent assistant whose token cost is bounded and one whose cost grows linearly with conversation age. 

 Selective retrieval helps handle the problem of conversation history cost. AgentCore Memory's RetrieveMemoryRecords operation performs semantic search with relevance scoring and metadata filtering, so you can pre-filter by recency or topic before the similarity search runs. Configure top-K between three and five items per reasoning step. 

 Context pruning assists with retrieval by removing duplicates between summaries and recent turns before each invocation, dropping superseded reasoning steps, and stripping irrelevant tool results. The goal is a target context utilization of 60 to 80% of the model's window, which leaves enough headroom for responses while still benefiting from available context. 

 RAG chunk sizing also helps solve this problem. When retrieving from [Amazon Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html), chunk sizes of 256 to 512 tokens balance retrieval precision against context bloat, and limiting retrieved chunks to the minimum needed helps prevent marginally relevant data from crowding out the current task. The verification that compression isn't silently hurting quality is a correlation check: pair context utilization with task success rate in CloudWatch Logs Insights and track whether aggressive pruning correlates with success-rate degradation. 

 [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) exposes token usage metrics that feed CloudWatch dashboards and alarms. Alarms on sessions consistently above 80% utilization flag the candidates for tighter summarization, correlating those same metrics with task success rates confirms whether the compression is paying off in cost without paying in quality. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Adopt managed rolling summarization:** Integrate [Amazon Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) for managed compression, or implement custom rolling summarization that compresses the oldest N turns after every N turns. 

1.  **Configure relevance-scored retrieval:** Use AgentCore Memory's RetrieveMemoryRecords with relevance thresholds and metadata filtering, retrieving only the top-K most relevant items per reasoning step. 

1.  **Prune context before each invocation:** Remove duplicates, superseded reasoning steps, and irrelevant tool results before each model call so the context window reflects what the current decision needs. 

1.  **Tune RAG chunk size:** Optimize [Amazon Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) chunk sizes to 256 to 512 tokens, limit retrieved chunks to the minimum needed, and add re-ranking to maximize relevance. 

1.  **Alarm on context utilization:** Build Amazon CloudWatch dashboards for context window utilization and set alarms for sessions exceeding 80% utilization. 

1.  **Correlate utilization with task success:** Use CloudWatch Logs Insights to correlate context utilization with task success rates, validating that compression strategies reduce cost without degrading reasoning quality. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTCOST02-BP02 Cost optimize token consumption through efficient prompt engineering](agentcost02-bp02.html) 
+  [AGENTCOST02-BP03 Use intelligent caching to reduce redundant model invocations](agentcost02-bp03.html) 
+  [AGENTCOST03-BP01 Design cost-effective retrieval systems with tiered memory](agentcost03-bp01.html) 
+  [AGENTCOST03-BP03 Implement cost-optimized state persistence and lifecycle management](agentcost03-bp03.html) 

 **Related documents:** 
+  [Amazon Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) 
+  [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) 
+  [Economics for agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-economics/index.html) 

 **Related videos:** 
+  [AWS 2025 - AgentCore Deep Dive: Memory](https://www.youtube.com/watch?v=-N4v6-kJgwA) 
+  [AWS 2025 - AgentCore Observability: Monitor and Debug with OpenTelemetry](https://www.youtube.com/watch?v=wWQgawUPr1k) 

 **Related examples:** 
+  [GitHub: awslabs/amazon-bedrock-agentcore-samples - Memory tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/04-AgentCore-memory) 

 **Related services:** 
+  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 