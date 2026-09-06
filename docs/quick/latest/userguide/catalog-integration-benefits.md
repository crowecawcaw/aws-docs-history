

# Benefits of data catalog integration
<a name="catalog-integration-benefits"></a>

Data catalog integration provides the following benefits:
+ **Accelerated asset curation** – Data curators (authors) use a conversational AI agent to discover tables that match their business needs, create datasets in bulk, and build multi-dataset topics in a single flow. These datasets are DirectQuery representations of your catalog assets, not copies of your data. The upstream catalog remains the source of truth. This significantly reduces the time required to deliver governed analytics to business users.
+ **Semantic inheritance** – Table and column descriptions, and primary and foreign key relationships (where available), are automatically inherited from the upstream catalog. This eliminates manual recreation of business context and ensures consistency with your catalog as the single source of truth.
+ **Focused context boundaries** – In enterprise environments with thousands of tables, the agentic experience helps authors define a curated subset of catalog assets relevant to their line of business. These curated datasets and topics provide a focused data boundary that improves the accuracy of AI-generated answers in Q&A and enables deterministic, reliable dashboards.
+ **Always-fresh data** – All datasets created through the catalog integration use DirectQuery, so data is queried at the source with no duplication or staleness.
+ **Governance inheritance** – Optionally enable identity propagation to enforce per-user data permissions defined in your upstream catalog at query time, without recreating row-level security (RLS) or column-level security (CLS) rules in Quick.
+ **Combined enterprise context** – After you establish a context boundary with datasets and topics, Quick can combine catalog data with other enterprise knowledge sources such as Slack conversations, Outlook emails, and Google Drive documents. This unified context enables AI agents to deliver more comprehensive insights across structured and unstructured data.