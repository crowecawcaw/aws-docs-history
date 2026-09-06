

# When to use data catalog integration
<a name="catalog-integration-when-to-use"></a>

Data catalog integration is designed for the following scenarios:
+ **Large-scale catalogs that require a focused context boundary** – In enterprise environments with thousands of tables, exposing the entire catalog to end users can introduce noise and reduce answer accuracy in AI-powered Q&A. The agentic experience enables authors to define a curated subset of assets relevant to their line of business. These assets are represented as datasets and topics in Quick, providing a focused boundary for deterministic dashboards and more accurate AI-generated answers.
+ **Catalog as the authoritative source of truth** – Datasets created through the agentic experience are DirectQuery projections of upstream catalog assets. The catalog remains the single source of truth for metadata and definitions. Semantic sync keeps definitions current. Quick also supports additional transformations on these assets when needed.
+ **Combined enterprise context** – By building curated representations (datasets and topics) in Quick, Quick can combine catalog data with other enterprise knowledge sources. This unified context enables AI agents to deliver comprehensive insights across structured and unstructured data.