

# Overview of semantic caching
<a name="semantic-caching-overview"></a>

Unlike traditional caches that rely on exact string matches, a semantic cache retrieves data based on semantic similarity. A semantic cache uses vector embeddings produced by models like Amazon Titan Text Embeddings to capture semantic meaning in a high-dimensional vector space.

In generative AI applications, a semantic cache stores vector representations of queries and their corresponding responses. The system compares the vector embedding of each new query against cached vectors of prior queries to determine if a similar query has been answered before. If the cache contains a similar query above a configured similarity threshold, the system returns the previously generated response instead of invoking the LLM. Otherwise, the system invokes the LLM to generate a response and caches the query embedding and response together for future reuse.

## Why semantic, not exact match?
<a name="semantic-caching-why-semantic"></a>

Consider an IT help chatbot where thousands of users ask the same question. The following queries are different strings but carry the same meaning:
+ "How do I install the VPN app on my laptop?"
+ "Can you guide me through setting up the company VPN?"
+ "Steps to get VPN working on my computer"

An exact-match cache treats each query as unique and invokes the LLM three times. A semantic cache recognizes these queries as semantically equivalent and returns the cached response for all three, invoking the LLM only once.

## Key benefits
<a name="semantic-caching-benefits"></a>

Semantic caching provides the following benefits for generative AI and agentic AI applications:
+ **Reduced costs** – Reusing answers for similar questions reduces the number of LLM calls and overall inference spend. In benchmarks, semantic caching reduced LLM inference cost by up to 86%.
+ **Lower latency** – Serving answers from the cache provides faster responses than running LLM inference. Cache hits return responses in milliseconds rather than seconds, achieving up to 88% latency reduction.
+ **Improved scalability** – Reducing LLM calls for similar or repeated queries enables you to serve more requests within the same model throughput limits without increasing capacity.
+ **Improved consistency** – Using the same cached response for semantically similar requests helps deliver a consistent answer for the same underlying question.

## Where semantic caching is effective
<a name="semantic-caching-effective-use-cases"></a>

Semantic caching is particularly effective for the following types of applications:


| Application type | Description | Example | 
| --- | --- | --- | 
| RAG-based assistants and copilots | Many queries are duplicate requests from different users against a shared knowledge base | IT help chatbot, product FAQ bot, documentation assistant | 
| Agentic AI applications | Agents break tasks into multiple small steps that may repeatedly look up similar information | Compliance agent reusing policy lookups, research agent reusing prior findings | 
| Multimodal applications | Matching similar audio segments, images, or video queries | Automated phone systems reusing guidance for repeated requests like store hours | 