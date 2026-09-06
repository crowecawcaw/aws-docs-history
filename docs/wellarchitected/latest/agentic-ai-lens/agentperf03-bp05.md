

# AGENTPERF03-BP05 Implement agentic retrieval patterns for dynamic, agent-driven knowledge access
<a name="agentperf03-bp05"></a>

 Complex questions often require information from multiple sources, iterative refinement, or real-time data that a single retrieval pass can't provide. In agentic retrieval the agent actively controls the retrieval process as part of its reasoning loop, deciding when to retrieve, what to retrieve, which retrieval tool to use, and whether the retrieved context is sufficient before proceeding. Each iteration adds embedding generation, vector search, re-ranking, and context injection overhead, so the retrieval loop needs explicit termination conditions. 

 **Desired outcome:** 
+  You have agents retrieving the right information in the minimum number of iterations required. 
+  You have simple questions answered with a single retrieval and complex questions handled through structured multi-hop retrieval with explicit termination conditions. 
+  You have the agent selecting the most appropriate retrieval tool for each query type. 
+  You have retrieval iteration counts, per-iteration latency, and sufficiency rates tracked and optimized. 

 **Common anti-patterns:** 
+  Treating all retrieval as a single-shot preprocessing step, forcing the agent to work with whatever context was retrieved on the first attempt regardless of sufficiency. 
+  Allowing agents to retrieve iteratively without retrieval budgets or termination conditions, producing unbounded retrieval loops that consume tokens and latency without converging. 
+  Routing all retrieval through a single pipeline regardless of query type, missing opportunities to use faster or more appropriate retrieval tools for different information needs. 

 **Benefits of establishing this best practice:** 
+  Parallel sub-query execution and retrieval-tool routing reduce end-to-end latency by selecting the fastest appropriate source. 
+  Explicit budgets that cap iterations and total tokens keep retrieval costs under control. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Design retrieval as a set of agent tools rather than a monolithic pipeline. Distinct retrieval tools for different knowledge access patterns let the agent route to the right source: 
+  A semantic search tool backed by [Amazon Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) for conceptual questions 
+  A structured query tool for exact lookups by identifier 
+  A real-time data tool for information requiring current values 
+  A web search tool for questions beyond the organization's knowledge base 
+  A document processing tool backed by [Amazon Bedrock Data Automation](https://docs.aws.amazon.com/bedrock/latest/userguide/bda.html) for extracting structured data from images, forms, and tables 

 [Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) exposes retrieval tools as MCP-compatible endpoints, and registering each tool with clear descriptions, what question types it handles, what data sources it accesses, and its expected latency guides the agent's tool selection. 

 Retrieval sufficiency evaluation is a lightweight assessment after each retrieval iteration, typically run by a smaller, faster model. The evaluator judges whether the retrieved context is sufficient, identifies gaps, and formulates refined queries. A maximum retrieval iteration limit (typically 2-3 iterations) helps prevent unbounded loops. If the agent has not retrieved sufficient context within the budget, it proceeds with the best available context and communicates uncertainty. 

 For complex questions requiring multiple sources, query decomposition breaks the question into focused sub-queries and runs independent sub-queries concurrently. Per-task retrieval performance budgets, derived from the task's overall latency SLO, keep the iterative pattern inside the workload's target. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Implement distinct retrieval tools for different knowledge access patterns:** Register a semantic search tool, a structured-query tool, a real-time data tool, a web search tool, and a document processing tool through [Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) with clear descriptions that guide the agent's tool selection. 

1.  **Implement retrieval sufficiency evaluation as a lightweight post-retrieval assessment:** Use a small, fast model to judge whether retrieved context is sufficient, identify gaps, and formulate refined queries for the next iteration. 

1.  **Configure maximum retrieval iteration limits with graceful fallback to best-available context:** Cap iterations at 2-3 for most tasks, and when the budget is exhausted proceed with the best context obtained and communicate uncertainty rather than looping without bounds. 

1.  **Implement query decomposition for complex questions, running independent sub-queries concurrently:** Break multi-source questions into focused sub-queries and fan them out in parallel so sub-query latency doesn't accumulate serially. 

1.  **Define per-task retrieval performance budgets based on the overall latency SLO:** Allocate an explicit portion of the task's latency SLO to retrieval so the iterative pattern can't silently consume the budget reserved for inference or downstream tool calls. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTPERF03-BP03 Optimize RAG retrieval pipelines for latency and precision](agentperf03-bp03.html) 
+  [AGENTPERF03-BP02 Optimize context window utilization and prompt management](agentperf03-bp02.html) 
+  [AGENTPERF02-BP01 Design efficient reasoning pipelines](agentperf02-bp01.html) 
+  [AGENTREL05-BP03 Ground agent cognition in real information](agentrel05-bp03.html) 
+  [AGENTCOST03-BP02 Cost optimize through intelligent compression and pruning of context windows](agentcost03-bp02.html) 

 **Related documents:** 
+  [Amazon Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) 
+  [Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) 
+  [Amazon Bedrock Data Automation](https://docs.aws.amazon.com/bedrock/latest/userguide/bda.html) 
+  [Agentic AI patterns and workflows on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/introduction.html) 
+  [Blog: Building intelligent search with Amazon Bedrock and Amazon OpenSearch Service for hybrid RAG solutions](https://aws.amazon.com/blogs/machine-learning/building-intelligent-search-with-amazon-bedrock-and-amazon-opensearch-for-hybrid-rag-solutions/) 

 **Related examples:** 
+  [GitHub: Advanced RAG using Bedrock and SageMaker AI](https://github.com/aws-samples/sample-advanced-rag-using-bedrock-and-sagemaker) 

 **Related services:** 
+  [Amazon Bedrock Knowledge Bases](https://aws.amazon.com/bedrock/knowledge-bases/) 
+  [Amazon Bedrock AgentCore Gateway](https://aws.amazon.com/bedrock/agentcore/) 
+  [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 