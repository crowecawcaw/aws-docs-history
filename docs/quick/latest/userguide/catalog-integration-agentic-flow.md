

# The agentic catalog experience
<a name="catalog-integration-agentic-flow"></a>

After you connect to a supported catalog, data curators (authors) can choose **Explore data** on the data source to launch the agentic experience. The AI agent guides you through the following steps in a conversational flow:

1. **Discover** – Describe your use case in natural language. The agent uses catalog metadata, including table and column descriptions, data quality scores, and lineage, to recommend the most relevant tables. For example: *"I am a supply chain analyst looking to enable Q&A for my logistics managers. They need to track carrier on-time delivery performance and shipping costs across distribution centers."*

1. **Create** – After you verify the recommended assets, create all relevant datasets in bulk within the same conversational flow. These datasets are DirectQuery representations of your catalog assets — the upstream catalog remains the source of truth. We recommend that you create datasets only for your intended use cases to maintain a focused context boundary.

1. **Relationships and topics** – Once datasets are created, the agent inherits relationships from the upstream catalog (where available) and can recommend additional inferred relationships. The agent then creates a multi-dataset topic that spans your selected assets.

1. **Semantic inheritance** – Table and column descriptions are automatically inherited from the upstream catalog onto the created datasets. This metadata provides the business context that AI agents in Quick need to generate accurate, grounded answers for your end users.

**Important**  
The agentic experience is AI-powered. Authors should review all agent recommendations, including discovered tables, inferred relationships, and inherited descriptions, before proceeding.