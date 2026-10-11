

# Knowledge and Grounding
<a name="knowledge-and-grounding"></a>

AVX uses a dual grounding strategy to deliver accurate, contextual answers across every persona and channel. A Bedrock Knowledge Base provides reference-document retrieval for unstructured automotive content; AgentCore Memory provides metadata-tagged long-term memory (LTM) for structured, per-persona tabular data sourced from ADP data products. Together they ensure that every agent response is grounded in authoritative data rather than generated from the model’s training knowledge alone.

The composition and technical wiring — how AVX sessions are initialized, how cross-account Lake Formation grants authorize Athena queries, and how the KB resource policy enables cross-account Retrieve calls — is covered in [Building on CMS and ADP](building-on-cms-and-adp.md). This chapter describes the grounding strategy itself: what goes into each mechanism, how filtering provides isolation and relevance, how tenancy shapes the KB layout, how personas map to grounding surfaces, how citations build caller trust, and how to manage content without code redeployment.