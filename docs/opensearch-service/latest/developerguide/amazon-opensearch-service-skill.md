# amazon-opensearch-service skill

`amazon-opensearch-service` is a skill in the Agent Toolkit for AWS that
brings Amazon OpenSearch Service expertise directly into your AI coding agent. A skill is a curated
package of instructions, scripts, and reference material that helps an agent complete a
task correctly – encapsulating domain knowledge and best practices the model would
not otherwise have. The agent loads the skill only when your request is about OpenSearch,
so it adds capability without slowing the agent down on unrelated work.

The skill works with managed OpenSearch Service domains and OpenSearch Serverless collections.

## Capabilities

The skill routes each request to one of five capabilities.

### Migration

Plan a migration from Solr, Elasticsearch, or self-managed OpenSearch into
Amazon OpenSearch Service or Serverless. The skill assesses compatibility, translates schemas and
queries, recommends instance class, count, and shard math, and outlines a cutover
approach.

```
Assess my Solr 8 catalog for migration to OpenSearch Service
```

###### Note

The skill plans the migration; it does not move data. Use Migration
Assistant for Amazon OpenSearch Service for historical backfill and live cutover.

### Operations

Provision and manage domains and collections – lifecycle, version
upgrades, storage tiers (including UltraWarm and OR1), fine-grained access
control, and monitoring.

```
Provision a production OpenSearch Service domain with three Availability Zones
```

### Search

Build keyword (BM25), vector, semantic, hybrid, and RAG search. The skill
helps with index configuration, k-NN engine selection (FAISS HNSW vs. Lucene),
and Amazon Bedrock connectors for embeddings, and includes query DSL examples.

```
Build a hybrid search application with OpenSearch and Bedrock embeddings
```

### Log analytics

Search and analyze logs with Piped Processing Language (PPL), set up
OpenSearch Ingestion pipelines, detect anomalies, and build OpenSearch Dashboards.

```
Investigate why my service is returning 500s and correlate with recent traces
```

### Trace analytics

Investigate distributed traces with OpenTelemetry – identify slow and
error spans, build service maps, and ingest spans with Data Prepper.

```
Which service is causing the p99 latency regression in the checkout flow?
```

## How the agent gets the skill

The skill is delivered through the Agent Toolkit for AWS. You have two
options:

- **Install the `aws-data-analytics` plugin
  (recommended).** The plugin bundles the AWS MCP Server
  configuration and the OpenSearch skill in a single install.
- **Discover it at runtime through the AWS MCP
  Server.** With the AWS MCP Server configured, your agent finds
  the skill on demand using the server's `search_documentation`
  tool and loads it with `retrieve_skill` – no local install
  required.

## Using the skill with and without the AWS MCP Server

The skill is designed to run with the [Set up the AWS MCP Server](aws-mcp-server.md "aws-mcp-server.md"), which
provides authenticated API access, sandboxed script execution, and enterprise
controls. Where the AWS MCP Server is available, the agent uses its
`call_aws` tool to run OpenSearch operations.

The skill also works without the AWS MCP Server. Every operation in the skill
runs with the standard AWS CLI alone (for example,
`aws opensearch describe-domain` or
`aws opensearchserverless create-collection`). The skill includes
instructions that work with both approaches.

## Prerequisites

- An AI coding agent that supports the Agent Toolkit for AWS (such as
  Claude Code or Codex).
- AWS credentials configured with permission for the OpenSearch
  operations you intend to run. For domains, see [Identity-based policies](ac.md#ac-types-identity "ac.md#ac-types-identity"). For Serverless, see [Data access control for Amazon OpenSearch Serverless](serverless-data-access.md "serverless-data-access.md").
- For the recommended setup, the [Set up the AWS MCP Server](aws-mcp-server.md "aws-mcp-server.md").

## Security considerations

When the agent runs OpenSearch operations, it acts with the credentials you
provide. Anything those credentials are authorized to do, the agent can trigger on
your behalf.

- Use least-privilege credentials scoped to the indexes and actions the
  agent needs. Avoid reusing administrator credentials.
- Separate development and production. Point the agent at non-production
  resources for exploration, and require explicit confirmation before
  production changes.
- Review resources the agent creates before committing to long-lived
  infrastructure. The Operations and Migration capabilities can provision
  domains, collections, IAM roles, and networking resources.
- Review tool output. MCP tool responses are returned to the language model
  as context. Avoid running operations against indexes that contain sensitive
  data you do not want exposed to your model provider.
