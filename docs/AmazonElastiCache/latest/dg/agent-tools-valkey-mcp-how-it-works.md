# How Valkey MCP Server works

The Valkey MCP server gives your agent a set of structured tools for working with the configured Valkey datastore. When you make a request, the agent selects the appropriate tool, provides the required parameters, and receives the result directly from Valkey. The server handles command construction and validation, so the agent does not need to generate client code or manually format Valkey commands.

The Valkey MCP server provides the following capability areas:

| Capability area             | Purpose                                                                                                                                                         |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Valkey operations**       | Read and modify strings, hashes, lists, sets, sorted sets, streams, and other Valkey data structures.                                                           |
| **JSON operations**         | Store, retrieve, and update JSON documents and arrays using structured paths.                                                                                   |
| **Search and AI workloads** | Create search indexes, add documents, run text, semantic, vector, and hybrid searches, and aggregate results.                                                   |
| **Operational safeguards**  | Separates read, write, and administrative operations. Destructive administrative commands are disabled by default, and the server can be run in read-only mode. |

The server uses structured JSON inputs and translates them into the appropriate Valkey operations. This reduces command-formatting errors and gives the agent a consistent interface across common data, search, and operational tasks.

## Full Valkey access through a compact tool surface

The Valkey MCP server gives agents access to the full Valkey command set through three structured tools:

1. `valkey_read` handles read-only operations such as `GET`, `HGETALL`, `SCAN`, and `INFO`.
2. `valkey_write` supports mutations such as `SET`, `HSET`, `DEL`, and `LPUSH`.
3. `valkey_admin` covers configuration and high-impact operations.

This keeps the tool surface simple for agents while supporting Valkey capabilities like strings, hashes, lists, sorted sets, streams, pub/sub, bitmaps, HyperLogLog, and others.

## Simplified AI, search, and analytics workflows

The Valkey MCP server provides four purpose-built tools for vector, semantic, text, and hybrid search, along with aggregations. Agents can query your data without constructing low-level commands, giving developers a direct path from a natural-language request to a working Valkey search or AI workflow.

1. `manage_index` lets agents create, drop, inspect, or list search indexes.
2. `add_documents` ingests documents into a search index and automatically creates the index if it does not exist. It also supports optional embedding generation for semantic search, using open-source embedding packages by default and configurable providers such as Amazon Bedrock, OpenAI, or Ollama.
3. `search` provides a unified interface for semantic, text, hybrid, and find-similar searches. It automatically detects the search mode from the parameters provided.
4. `aggregate` provides a structured pipeline builder for `FT.AGGREGATE`, with support for `GROUPBY`, `SORTBY`, `APPLY`, `FILTER`, and `LIMIT` stages.

When debugging, the `search` and `aggregate` tools let agents inspect the actual contents of your datastore. Agents can review indexed data, sample matching documents, and validate search and aggregation results directly in the conversation.
