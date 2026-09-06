

# How Topics work
<a name="topics-how-it-works"></a>

A Topic in Quick Sight consists of four layers:

1. **Data sources.** Your normalized datasets connect to Quick Sight from supported sources. Topics support SPICE datasets and Direct Query datasets against Amazon Redshift, Athena, Amazon S3 Tables, Snowflake, and Databricks. You cannot combine SPICE and Direct Query datasets within a single Topic.

1. **Dataset enrichment.** Each dataset is independently enriched with semantic metadata that improves natural language query accuracy. Enrichment includes column descriptions, synonyms, semantic types, calculated fields, and field exclusions. You can enrich datasets directly in Quick Sight or bring metadata in using catalogs from AWS Glue (AWS Glue Data Catalog) and Databricks Unity Catalog.

1. **Multi-dataset Topic.** The Topic serves as the unified container that brings datasets together. It holds:
   + **Datasets** (up to 12). Each dataset maintains its own enrichment and connects to its own data source.
   + **Relationships.** Join keys defined between dataset pairs tell Quick Sight how tables relate. You upload a JSON file that maps columns between datasets.
   + **Custom instructions.** Persistent natural language rules that guide the AI in interpreting domain-specific terminology. These handle disambiguation, custom date logic, and business definitions.
   + **Permissions.** Owners can modify the Topic. Viewers can ask questions and use the Topic in analysis but cannot change its configuration.

1. **Consumption.** Business users interact with the Topic through multiple surfaces:
   + **Chat.** Users ask natural language questions in the Amazon Quick chat interface. The LLM-powered chat agent parses the question, identifies relevant columns across datasets, constructs SQL with appropriate joins based on your defined relationships, and returns a unified answer.
   + **Analysis sheets.** Authors build visuals using fields from multiple datasets within the Topic. Quick Sight performs runtime inner joins automatically when a visual references fields from more than one dataset.

Row-level security (RLS) is enforced at the dataset level during runtime joins. Users see only the data they are authorized to access, even when queries span multiple datasets.