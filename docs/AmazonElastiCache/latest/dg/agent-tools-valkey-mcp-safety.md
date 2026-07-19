# Guardrails and tracking usage

The Valkey MCP server uses a risk-tiered execution model that separates read, write, and administrative operations. The read tier is always available and provides the lowest-risk level of access. The write tier allows agents to modify data while continuing to block destructive operations such as `FLUSHALL`. The admin tier covers high-impact operations and is disabled by default. Enabling it requires both a server-level setting and explicit confirmation for each call.

For production exploration, you can also run the server with `--readonly` to restrict agents to read-only operations.

## Track agent activity

The Valkey MCP server writes a structured log of every tool call to `valkey-mcp-server.log` in your MCP client's working directory, showing the operation, parameters, and result. Open this file to see what your agent is doing against your datastore in real time.
