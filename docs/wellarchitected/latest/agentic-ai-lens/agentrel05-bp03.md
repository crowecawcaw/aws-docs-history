

# AGENTREL05-BP03 Ground agent cognition in real information
<a name="agentrel05-bp03"></a>

 Training data has a cutoff and an agent reasoning only from model knowledge can hallucinate about the present. Retrieval-augmented generation grounds each answer in current, domain-specific information and reduces hallucination rates as a byproduct. 

 **Desired outcome:** 
+  You have retrieval pipelines that ground agent reasoning in current, domain-specific information. 
+  You validate knowledge freshness and flag content that exceeds staleness thresholds. 
+  You handle retrieval failures gracefully, letting agents continue with model knowledge while communicating the uncertainty. 

 **Common anti-patterns:** 
+  Relying only on model training data for domain-specific knowledge, producing outputs that may be outdated or inaccurate. 
+  Running retrieval without freshness validation, causing agents to reason from stale data. 
+  Treating retrieval as a hard dependency, so retrieval failures cascade into agent failures. 

 **Benefits of establishing this best practice:** 
+  Hallucination rates drop because reasoning is grounded in retrieved factual information. 
+  Factual accuracy improves through access to current, domain-specific knowledge. 
+  Reliability holds as the operational environment evolves through knowledge base updates. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 [Amazon Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) handles the mechanics of RAG, document ingestion, chunking, embedding, and vector storage, so most of the setup is configuration rather than infrastructure. Configure data sources that reflect the agent's domain and set up automated synchronization to keep content current. S3 event notifications trigger sync operations when source documents are updated, and the Knowledge Bases direct ingestion API handles programmatic content. Chunking strategy matters. Smaller chunks produce precise factual retrieval, while larger chunks produce better contextual understanding. Reranking models re-score retrieved passages for higher-quality context. 

 A knowledge base populated at launch and never refreshed becomes a source of wrong answers over time. Track ingestion timestamps and flag content that exceeds staleness thresholds before it is served. For information that requires real-time accuracy (prices, inventory, and system status), caches are not sufficient. Implement tool functions that agents invoke to retrieve data from authoritative sources through [Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html), and treat the authoritative source as the single source of truth. 

 [Amazon Bedrock Data Automation](https://docs.aws.amazon.com/bedrock/latest/userguide/bda.html) extracts structured data from documents, forms, and tables, so agents reason over extracted content rather than raw images. Retrieved context quality assessment filters low-relevance results and deduplicates redundant passages before injection into prompts. Otherwise the context window fills with noise that drowns out the signal. Handle retrieval failures by allowing the agent to continue with model knowledge while communicating uncertainty about information currency. A transparent "I'm working from general knowledge rather than current data" beats silent reliance on training data. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Configure Amazon Bedrock Knowledge Bases with automated synchronization:** Set up [Amazon Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) with domain-appropriate data sources and sync pipelines triggered by source changes. 

1.  **Implement knowledge freshness validation:** Track ingestion timestamps and flag stale content before it is served. 

1.  **Use Knowledge Bases reranking:** Re-score retrieved passages for higher-quality context injection. 

1.  **Implement real-time data retrieval tools through AgentCore Gateway:** Use [Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) tool functions for information that requires current accuracy. 

1.  **Handle retrieval failures gracefully:** Allow agents to continue with model knowledge while communicating uncertainty about information currency. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTREL03-BP01 Design an information classification model to identify short-term and long-term memories](agentrel03-bp01.html) 
+  [AGENTREL05-BP01 Design modular, fault-tolerant agentic reasoning components](agentrel05-bp01.html) 
+  [AGENTREL05-BP02 Facilitate reliable adaptation through evaluation-driven improvement cycles](agentrel05-bp02.html) 

 **Related documents:** 
+  [Amazon Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) 
+  [Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) 
+  [Amazon Bedrock Data Automation](https://docs.aws.amazon.com/bedrock/latest/userguide/bda.html) 

 **Related videos:** 
+  [AWS re:Invent 2024 - Advanced agentic RAG Systems: Deep dive with Bedrock (AIM425)](https://www.youtube.com/watch?v=bu2cD1pCFTs) 

 **Related examples:** 
+  [GitHub: awslabs/amazon-bedrock-agent-samples - Knowledge Base integration](https://github.com/awslabs/amazon-bedrock-agent-samples/tree/main/examples/agents/agent_with_knowledge_base_integration) 

 **Related services:** 
+  [Amazon Bedrock](https://aws.amazon.com/bedrock/) 
+  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) 