# AI agent integrations for Amazon OpenSearch Service

The OpenSearch community maintains two open source projects that let AI agents
work directly with Amazon OpenSearch Service:

- **[OpenSearch Agent Skills](opensearch-agent-skills.md "opensearch-agent-skills.md")**
  – A collection of task-focused instruction sets that teach AI coding
  agents how to perform common OpenSearch workflows, such as building a search
  application, investigating distributed traces, or deploying a cluster to AWS.
  Skills work with any agent that supports the Agent Skills standard, including
  Claude Code, Cursor, and Kiro, and require no running server.
- **[OpenSearch MCP server](opensearch-mcp-server.md "opensearch-mcp-server.md")**
  – A Model Context Protocol (MCP) server that exposes OpenSearch APIs
  as callable tools, enabling AI assistants and agent frameworks to search
  indexes, inspect cluster state, and run diagnostics against live OpenSearch Service domains
  and OpenSearch Serverless collections. It integrates with coding IDEs, Claude Desktop, the
  Kiro CLI, and agent frameworks such as Strands Agents and LangGraph.
  Both integrations work with managed OpenSearch Service domains and OpenSearch Serverless collections.
