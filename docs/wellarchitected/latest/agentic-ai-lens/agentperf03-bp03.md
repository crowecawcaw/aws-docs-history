

# AGENTPERF03-BP03 Optimize RAG retrieval pipelines for latency and precision
<a name="agentperf03-bp03"></a>

 Retrieval-augmented generation gives agents access to knowledge beyond the model's training data, but every reasoning iteration that queries a retrieval pipeline pays its latency and inherits the quality of its results. A well-tuned RAG pipeline returns high-relevance passages within a small latency budget. Without this discipline, retrieval either dominates per-iteration latency or returns noisy context that degrades reasoning quality. 

 **Desired outcome:** 
+  You have a chunking strategy matched to the structure and query shape of each source corpus, with chunk size and boundaries tuned against retrieval precision rather than defaulted to a single fixed size. 
+  You have retrieval latency tracked per stage (embedding, search, and re-ranking) with explicit budgets so retrieval can't silently consume time allocated to reasoning or tool calls. 
+  You have hybrid retrieval and re-ranking used where the corpus and query mix justify their added latency, rather than stacked by default. 
+  You have query reformulation ahead of every retrieval, so recall holds when agent phrasing diverges from corpus vocabulary. 
+  You have retrieval precision and relevance continually evaluated against a representative query set so quality regressions are caught before they reach production behavior. 

 **Common anti-patterns:** 
+  Using a single fixed chunk size across all document types, forcing structured content (tables, code, lists) through the same boundaries as flowing prose and splitting related information across chunks. 
+  Passing raw top-K retrieval results to the LLM without re-ranking or relevance filtering, letting low-signal passages displace high-signal context in the agent's prompt. 
+  Embedding the agent's raw query without reformulation, missing relevant documents that use different terminology than the query phrasing. 
+  Running every retrieval through pure dense similarity search when the corpus contains exact identifiers, code, or numeric values that keyword search recovers more reliably. 
+  Choosing an embedding model once and never revisiting it, missing precision gains from newer models or domain-tuned alternatives. 
+  Treating retrieval latency as a single metric rather than attributing it across embedding, search, and re-ranking stages, so performance regressions can't be localized. 

 **Benefits of establishing this best practice:** 
+  Stage-level attribution and index tuning keep embedding, search, and re-ranking within a predictable per-retrieval budget. 
+  Matching chunking strategy to document structure, hybrid retrieval where warranted, and re-ranking before context delivery keeps noise out of the prompt. 
+  High-precision first retrievals reduce the number of reasoning iterations that retry retrieval with reformulated queries. 
+  Continuous evaluation against a representative query set detects relevance drift before it reaches production. 
+  Tighter, more relevant retrievals consume less of the context window, leaving more budget for reasoning. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 At ingest, four decisions fix what any future retrieval can see before a single query runs: parsing, chunking, embedding, and the choice of [vector store](https://docs.aws.amazon.com/prescriptive-guidance/latest/choosing-an-aws-vector-database-for-rag-use-cases/introduction.html). Query-time stages can filter and reorder what ingest produced, but they can't recover information ingest discarded. This asymmetry is the architectural reason RAG pipelines can't be tuned as a single knob. Errors that are built in at ingest require re-ingesting the whole corpus to fix. Query-time misconfigurations can be patched without touching storage. When designers treat RAG as an unknown, they inherit both sides of that commitment without seeing where it was made. 

 Chunking is an ingest-time commitment with no cheap fix. Fixed-size chunks fragment tables and mix unrelated passages when topics shift mid-chunk. Hierarchical chunking preserves nested-document relationships but roughly doubles the index footprint because parent chunks are indexed alongside their children. Semantic chunking breaks on meaning rather than token count and can disagree with domain experts about where a topic actually shifts. [Advanced parsing](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-advanced-parsing.html) recovers figures and tables from PDFs before chunking runs but adds a foundation-model invocation per document. Getting any of these wrong isn't a query-time tuning problem, requiring a full re-embedding of the corpus to fix. 

 Three query-time stages each convert latency into precision, and the embedding model used at ingest sets the floor for all three. 
+  Hybrid retrieval adds BM25 scoring alongside vector similarity, recovering exact-match queries but doubling first-stage work. 
+  Re-ranking runs a second, heavier model over a broad top-k to earn back prompt tokens, spending milliseconds per passage. 
+  Query reformulation expands a single query into several, trading fan-out latency for recall when agent phrasing misses corpus terminology. 

 Stacking these stages doesn't give additive precision gains: rerank over hybrid often matches rerank over dense-only, and reformulation paired with re-ranking can overlap in what each fixes. Layering all three yields a precision return that flattens before the last layer contributes, and a latency cost that doesn't. 

 Between one deploy and the next, corpora grow, embedding models update, re-rankers retrain, and agent query patterns shift. Each change can move retrieval quality in either direction with no in-band signal. Drift is only detectable against a representative query set labeled with expected passages. 

 Recall@k and nDCG@k quantify whether the right passages were returned, and the RAG triad (context relevance, answer relevance, groundedness) extends the measurement to whether retrieved context actually supported the answer. The eval set is also the joint between corpus owners, who update documents, and pipeline owners, who tune stages. Without shared evaluation, teams can ship regressions that other teams aren't aware of. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Inventory source corpora and query patterns:** For each knowledge corpus the agent will query, record document type (prose, hierarchical document, PDF with figures, structured tables, code), typical query shape (conceptual intent vs. exact identifier), expected query volume, and precision/latency budget. This inventory drives every downstream choice (chunking strategy, embedding model, index configuration, and re-ranker placement). Without it, the pipeline is tuned by guess against an imagined average. 

1.  **Choose a chunking and parsing strategy per corpus:** For flowing prose, use semantic chunking to break on meaning. For nested documents, use hierarchical chunking to preserve parent-child context. For PDFs and multimodal content with figures or tables, enable [advanced parsing](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-advanced-parsing.html) via a foundation model or Amazon Bedrock Data Automation before chunking. Configure the strategy in the [Knowledge Base chunking configuration](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-chunking.html) per data source rather than defaulting every source to fixed-size chunks. 

1.  **Select an embedding model and dimensionality:** Pick an embedding model that covers the modalities, languages, and domain of the corpora and whose cost and latency fit the per-retrieval budget. [Amazon Titan Text Embeddings V2](https://docs.aws.amazon.com/bedrock/latest/userguide/titan-embedding-models.html) exposes configurable output dimensions so text-corpus index size, recall, and query latency can be balanced against each other, and [Amazon Nova Multimodal Embeddings](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-amazon-amazon-nova-multimodal-embeddings.html) produces a single embedding space across text, images, video, and audio for corpora that contain mixed modalities. Re-evaluate the choice when new models are released, because embedding quality improvements translate directly into retrieval precision. 

1.  **Configure the index for the retrieval pattern:** For corpora with both conceptual and exact-match queries, enable hybrid search rather than relying on pure dense similarity. With Amazon Bedrock Knowledge Bases backed by Amazon OpenSearch Service Serverless, set [overrideSearchType: HYBRID](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html) on the Retrieve request to combine vector and raw-text scoring in a single call. For direct OpenSearch workloads, configure [neural and hybrid search](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-configure-neural-search.html) explicitly. Apply metadata filters on the retrieve request to narrow the search space by document source, freshness, or scope before vector similarity runs, and tune [vector index parameters](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/vector-search.html) against retrieval precision on a representative query set so the index favors recall or latency according to the workload's budget. 

1.  **Add re-ranking before context delivery:** Run first-stage retrieval at a wider top-K than the prompt context budget allows, then pass the results through [Amazon Bedrock Rerank](https://docs.aws.amazon.com/bedrock/latest/userguide/rerank.html) to produce a higher-precision subset. The re-ranker compensates for vector-search noise and lets the LLM receive fewer but higher-relevance passages, which both tightens prompt quality and reduces input tokens. Configure the re-ranker on the Knowledge Base retrieve request rather than orchestrating it client-side so the hop stays inside the retrieval path. 

1.  **Enable query reformulation:** Transform agent-generated queries before they hit the index so retrieval doesn't fail on terminology mismatches with the source corpus. Knowledge Bases supports [query reformulation and decomposition](https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-knowledge-bases-now-supports-advanced-parsing-chunking-and-query-reformulation-giving-greater-control-of-accuracy-in-rag-based-applications/) through the Retrieve API, expanding a broad question into focused sub-queries executed against the index. Prefer the managed reformulation path over a bespoke preprocessing step so it stays colocate with the retrieval hop and benefits from future improvements to the feature. 

1.  **Instrument per-stage retrieval latency and relevance:** Emit distinct metrics for embedding latency, search latency, re-ranker latency, top-k size, and the relevance score distribution of returned passages, dimensioned by data source and query class. Per-stage attribution makes it possible to localize regressions. A rising re-ranker latency with a stable search latency points at a different root cause than the reverse. Set per-stage budgets that sum to the pipeline's end-to-end latency target so any single stage exceeding its budget alerts before end-to-end performance is affected. 

1.  **Evaluate the pipeline on a representative query set on a defined cadence:** Maintain a fixed evaluation set that spans the corpora and query shapes in the inventory, and run it against the pipeline on every significant change (new data source, chunking change, embedding or re-ranker upgrade, index parameter tuning), following the approach in [Evaluate and improve performance of Amazon Bedrock Knowledge Bases](https://aws.amazon.com/blogs/machine-learning/evaluate-and-improve-performance-of-amazon-bedrock-knowledge-bases/). Track Recall@k, nDCG@k, and RAG triad scores per change so quality regressions are caught before rollout, and refresh the evaluation set as real query patterns drift. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTPERF03-BP01 Implement tiered memory management systems](agentperf03-bp01.html) 
+  [AGENTPERF03-BP02 Optimize context window utilization and prompt management](agentperf03-bp02.html) 
+  [AGENTPERF03-BP04 Establish efficient agent caching and data access patterns](agentperf03-bp04.html) 
+  [AGENTPERF03-BP05 Implement agentic retrieval patterns for dynamic, agent-driven knowledge access](agentperf03-bp05.html) 

 **Related documents:** 
+  [Amazon Bedrock Knowledge Bases, How content chunking works](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-chunking.html) 
+  [Amazon Bedrock Knowledge Bases, Parsing options for your data source](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-advanced-parsing.html) 
+  [Amazon Bedrock Knowledge Bases, Query configurations](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html) 
+  [Amazon Bedrock, Improve the relevance of query responses with a re-ranker model](https://docs.aws.amazon.com/bedrock/latest/userguide/rerank.html) 
+  [Amazon Titan Text Embeddings models](https://docs.aws.amazon.com/bedrock/latest/userguide/titan-embedding-models.html) 
+  [Amazon Nova Multimodal Embeddings](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-amazon-amazon-nova-multimodal-embeddings.html) 
+  [Amazon OpenSearch Service, Vector search](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/vector-search.html) 
+  [Amazon OpenSearch Service Serverless, Configure Neural Search and Hybrid Search](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-configure-neural-search.html) 
+  [Blog: Amazon Bedrock Knowledge Bases, advanced parsing, chunking, and query reformulation](https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-knowledge-bases-now-supports-advanced-parsing-chunking-and-query-reformulation-giving-greater-control-of-accuracy-in-rag-based-applications/) 
+  [Blog: Evaluate and improve performance of Amazon Bedrock Knowledge Bases](https://aws.amazon.com/blogs/machine-learning/evaluate-and-improve-performance-of-amazon-bedrock-knowledge-bases/) 
+  [Choosing an AWS vector database for RAG use cases](https://docs.aws.amazon.com/prescriptive-guidance/latest/choosing-an-aws-vector-database-for-rag-use-cases/introduction.html) 

 **Related videos:** 
+  [AWS re:Invent 2025 - Advanced agentic RAG Systems: Deep dive with Amazon Bedrock (AIM425)](https://www.youtube.com/watch?v=bu2cD1pCFTs) 

 **Related examples:** 
+  [GitHub: Amazon Bedrock samples, Knowledge Bases and RAG](https://github.com/aws-samples/amazon-bedrock-samples) 

 **Related tools:** 
+  [Amazon Bedrock Knowledge Bases](https://aws.amazon.com/bedrock/knowledge-bases/) 
+  [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 