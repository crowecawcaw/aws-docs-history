# Agentic migration with AI tools

AI coding agents can accelerate your migration to Aurora DSQL by analyzing schemas, transforming code, and executing DDL migrations with built-in safety checks.

## Using Kiro for migration

Coding agents such as [Kiro](https://kiro.dev/ "https://kiro.dev/") can help you analyze and migrate your PostgreSQL code to Aurora DSQL:

- **Schema analysis:** Upload your existing schema files and ask Kiro to identify potential compatibility issues and suggest alternatives
- **Code transformation:** Provide your application code and ask Kiro to help refactor trigger logic, replace sequences with UUIDs, or modify transaction patterns
- **Migration planning:** Ask Kiro to create a step-by-step migration plan based on your specific application architecture
- **DDL migrations:** Execute schema modifications using the table recreation pattern with built-in safety checks and user verification

**Example prompts:**

```
"Analyze this PostgreSQL schema for DSQL compatibility and suggest alternatives for any unsupported features"

"Help me refactor this trigger function into application-level logic for DSQL migration"

"Create a migration checklist for moving my Django application from PostgreSQL to DSQL"

"Drop the legacy_status column from the orders table"

"Change the price column from VARCHAR to DECIMAL in the products table"
```

## DDL migration with table recreation

When using AI agents with the Aurora DSQL MCP server, certain ALTER TABLE operations use a _table recreation pattern_ that safely migrates your data. The agent handles the complexity while keeping you informed at each step.

The following operations use the table recreation pattern:

| Operation                        | Approach                                  |
| -------------------------------- | ----------------------------------------- |
| `DROP COLUMN`                    | Exclude column from new table             |
| `ALTER COLUMN TYPE`              | Cast data type during migration           |
| `ALTER COLUMN SET/DROP NOT NULL` | Change constraint in new table definition |
| `ALTER COLUMN SET/DROP DEFAULT`  | Define default in new table definition    |
| `ADD/DROP CONSTRAINT`            | Include or remove constraint in new table |
| `MODIFY PRIMARY KEY`             | Define new PK with uniqueness validation  |
| Split/Merge columns              | Use SPLIT_PART, SUBSTRING, or CONCAT      |

The following ALTER TABLE operations are supported directly without table recreation:

- `ALTER TABLE ... RENAME COLUMN` – Rename a column
- `ALTER TABLE ... RENAME TO` – Rename a table
- `ALTER TABLE ... ADD COLUMN` – Add a new column

**Safety features:** When executing DDL migrations, AI agents present the migration plan, verify data compatibility, confirm row counts, and request explicit approval before any destructive operations like DROP TABLE.

**Batched migrations:** For tables exceeding 3,000 rows, the agent automatically batches the migration in increments of 500-1,000 rows to stay within transaction limits.

## Aurora DSQL MCP server

The Aurora DSQL Model Context Protocol (MCP) server allows AI assistants to connect directly to your Aurora DSQL cluster and search Aurora DSQL documentation. This enables the AI to:

- Analyze your existing schema and suggest migration changes
- Execute DDL migrations with the table recreation pattern
- Test queries and verify compatibility during migration
- Provide accurate, up-to-date guidance based on the latest Aurora DSQL documentation

To use the Aurora DSQL MCP server with AI assistants, see
the setup instructions for the [Aurora DSQL MCP server](SECTION_aurora-dsql-mcp-server.md "SECTION_aurora-dsql-mcp-server.md").
