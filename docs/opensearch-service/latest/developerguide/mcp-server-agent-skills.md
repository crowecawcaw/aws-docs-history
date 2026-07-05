# MCP Server and Agent Skills for Amazon OpenSearch Service

You can work with Amazon OpenSearch Service and OpenSearch Serverless directly from AI coding agents – such as
Claude Code, Kiro, Cursor, and Codex – using the Agent Toolkit for AWS. The
toolkit gives your agent two things that work together:

- **[Set up the AWS MCP Server](aws-mcp-server.md "aws-mcp-server.md")** – A
  managed Model Context Protocol server that gives your agent authenticated access
  to AWS. It runs AWS API calls on your behalf, executes scripts in a
  sandboxed environment, and lets your agent discover and load AWS skills on
  demand.
- **[amazon-opensearch-service skill](amazon-opensearch-service-skill.md "amazon-opensearch-service-skill.md")**
  – A curated package of OpenSearch instructions and reference material
  that teaches your agent how to perform OpenSearch workflows correctly:
  migrating to OpenSearch, provisioning and operating clusters, building search
  applications, and running log and trace analytics.
  Together, the skill tells the agent what to do and the AWS MCP Server gives it the
  authenticated access to do it – against managed OpenSearch Service domains and OpenSearch Serverless
  collections alike.

###### Note

The fastest way to get both is to install the `aws-data-analytics`
plugin, which bundles the AWS MCP Server configuration and the OpenSearch skill
in a single install.

## What you can do

The `amazon-opensearch-service` skill covers five capabilities.
Describe your goal in natural language and the agent routes to the right one.

| #   | Capability      | What you can ask for                                                                                                                                                       |
| --- | --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | Migration       | Move from Solr, Elasticsearch, or self-managed OpenSearch into<br>Amazon OpenSearch Service or Serverless – schema and query translation, sizing,<br>and cutover planning. |
| 2   | Operations      | Provision and manage domains and collections – lifecycle,<br>upgrades, storage tiers, fine-grained access control, and<br>monitoring.                                      |
| 3   | Search          | Build vector, semantic, hybrid, and RAG search – including<br>Amazon Bedrock connectors and k-NN engine selection.                                                         |
| 4   | Log analytics   | Search and analyze logs with Piped Processing Language (PPL),<br>OpenSearch Ingestion, anomaly detection, and OpenSearch Dashboards.                                       |
| 5   | Trace analytics | Investigate distributed traces with OpenTelemetry – span<br>queries, service maps, and Data Prepper ingestion.                                                             |

Example prompts:

```
Migrate my self-managed Elasticsearch 7.10 cluster to OpenSearch Service
Build a semantic search application for product documentation
Investigate why my service is returning 500s and correlate with recent traces
Set up an OpenSearch Serverless collection for my search application
```

## Get started

1. Install the `aws-data-analytics` plugin in your agent, or
   configure the AWS MCP Server directly. See [Set up the AWS MCP Server](aws-mcp-server.md "aws-mcp-server.md").
2. Make sure your AWS credentials are configured with permission for the
   OpenSearch operations you intend to run. See [Identity-based policies](ac.md#ac-types-identity "ac.md#ac-types-identity") for domains and [Data access control for Amazon OpenSearch Serverless](serverless-data-access.md "serverless-data-access.md") for collections.
3. Ask your agent an OpenSearch question. It loads the
   `amazon-opensearch-service` skill and runs the work for
   you.
