# Migrating from PostgreSQL to Aurora DSQL

Aurora DSQL is designed to be [PostgreSQL
compatible](working-with-postgresql-compatibility.md "working-with-postgresql-compatibility.md"), supporting core relational features such as ACID transactions, secondary indexes, joins, and standard DML operations. Most existing PostgreSQL applications can migrate to Aurora DSQL with minimal changes.

This section provides practical guidance for migrating your application to Aurora DSQL, including framework compatibility, migration patterns, and architectural considerations.

##

Framework and ORM compatibility

Aurora DSQL uses the standard PostgreSQL wire protocol, ensuring
compatibility with PostgreSQL drivers and frameworks. Most
popular ORMs work with Aurora DSQL with minimal or no changes.
See [Aurora DSQL adapters and dialects](aws-sdks.md#aurora-dsql-adapters "aws-sdks.md#aurora-dsql-adapters") for
reference implementations and available ORM integrations.

## Common migration patterns

When migrating from PostgreSQL to Aurora DSQL, some features work differently
or have alternative syntax. This section provides guidance on common
migration scenarios.

### DDL operation alternatives

Aurora DSQL provides modern alternatives to traditional PostgreSQL DDL operations:

**Index creation**

Use `CREATE INDEX ASYNC` instead of `CREATE INDEX` for non-blocking index creation.

**Benefit:** Zero-downtime index creation on large tables.

**Data removal**

Use `DELETE FROM table_name` instead of `TRUNCATE`.

**Alternative:** For complete table recreation, use `DROP TABLE` followed by `CREATE TABLE`.

**System configuration**

Aurora DSQL doesn't support `ALTER SYSTEM` commands because the system is fully managed. Configuration is handled automatically based on workload patterns.

**Benefit:** No need for database tuning or parameter management.

### Schema design patterns

Adapt these common PostgreSQL patterns for Aurora DSQL compatibility:

**Sequences for keys**

Use UUIDs or composite keys instead of auto-incrementing
sequences. Auto-incrementing sequences lead to a high amount
of conflicts in a distributed system as multiple writers are
trying to update the same data. UUIDs provide the same
function but require no coordination.

**Example:** `id UUID PRIMARY KEY DEFAULT gen_random_uuid()`

**Referential integrity patterns**

Aurora DSQL supports table relationships and `JOIN` operations but doesn't yet enforce foreign key constraints. This design choice aligns with modern distributed database patterns where application-layer validation provides more flexibility and avoids performance bottlenecks from cascading operations.

**Pattern:** Implement referential integrity checks in your application layer using consistent naming conventions, validation logic, and transaction boundaries. Many high-scale applications prefer this approach for better control over error handling and performance.

**Temporary data handling**

Use CTEs, subqueries, or regular tables with cleanup logic instead of temporary tables.

**Alternative:** Create tables with session-specific names and clean them up in your application.

## Understanding architectural differences

Aurora DSQL's distributed, serverless architecture intentionally differs from traditional PostgreSQL in several areas. These differences enable Aurora DSQL's key benefits of simplicity and scale.

### Simplified database model

**Single database per cluster**

Aurora DSQL provides one built-in database named `postgres` per cluster.

**Migration tip:** If your application uses multiple databases, create separate Aurora DSQL clusters for logical separation, or use schemas within a single cluster.

**No temporary tables**

Temporary tables are not yet supported in Aurora DSQL. Common table
expressions (CTEs) and subqueries can be
used as an alternative for complex queries.

**Alternative:** Use CTEs with `WITH`
clauses for temporary result sets, or regular tables with unique
naming for session-specific data.

**Automatic storage management**

Aurora DSQL eliminates tablespaces and manual storage management. Storage automatically scales and optimizes based on your data patterns.

**Benefit:** No need to monitor disk space, plan storage allocation, or manage tablespace configurations.

### Modern application patterns

Aurora DSQL encourages modern application development patterns that improve maintainability and performance:

**Application-level logic instead of database triggers**

Aurora DSQL doesn't support triggers.

**Migration strategy:** Move trigger logic to application code, use event-driven architectures with AWS services like EventBridge, or implement audit trails using application logging.

**SQL functions for data processing**

Aurora DSQL supports SQL-based functions but not procedural languages like PL/pgSQL.

**Alternative:** Use SQL functions for data transformations, or move complex logic to your application layer or AWS Lambda functions.

**Optimistic concurrency control instead of pessimistic locking**

Aurora DSQL uses optimistic concurrency control (OCC), a lock-free approach that differs from traditional database locking mechanisms. Instead of acquiring locks that block other transactions, Aurora DSQL allows transactions to proceed without blocking and detects conflicts at commit time. This eliminates deadlocks and prevents slow transactions from blocking other operations.

**Key difference:** When conflicts occur, Aurora DSQL returns a serialization error rather than making transactions wait for locks. This requires applications to implement retry logic, similar to handling lock timeouts in traditional databases, but conflicts are resolved immediately rather than causing blocking waits.

**Design pattern:** Implement idempotent transaction logic with retry mechanisms. Design schemas to minimize contention by using random primary keys and spreading updates across your key range. For details, see [Concurrency control in Aurora DSQL](working-with-concurrency-control.md "working-with-concurrency-control.md").

**Relationships and referential integrity**

Aurora DSQL supports foreign key relationships between tables,
including
`JOIN`
operations, but foreign key constraints are not yet supported. While
enforcing referential integrity can be valuable, cascading
operations (like cascading deletes) can create unexpected performance
issues—for example, deleting an order with 1,000 line items
becomes a 1,001-row transaction. Many customers avoid foreign
key constraints for this reason.

**Design pattern:** Implement referential integrity checks in your application layer, use eventual consistency patterns, or leverage AWS services for data validation.

### Operational simplifications

Aurora DSQL eliminates many traditional database maintenance tasks, reducing operational overhead:

**No manual maintenance required**

Aurora DSQL doesn't require `VACUUM`, `TRUNCATE`, or `ALTER SYSTEM` commands. The system automatically manages storage optimization, statistics collection, and performance tuning.

**Benefit:** Eliminates the need for database maintenance windows, vacuum scheduling, and system parameter tuning.

**Automatic partitioning and scaling**

Aurora DSQL automatically partitions and distributes your data based on access patterns. Manual partitioning and sequences are not needed.

**Migration tip:** Remove manual partitioning logic and let Aurora DSQL handle data distribution. Use UUIDs or application-generated IDs instead of sequences.

## AI-assisted migration

You can leverage AI tools to help migrate your codebase to Aurora DSQL:

### Using Kiro for migration assistance

Coding agents such as [Kiro](https://kiro.dev/ "https://kiro.dev/") can help you analyze and migrate your PostgreSQL code to Aurora DSQL:

- **Schema analysis:** Upload your existing schema files and ask Kiro to identify potential compatibility issues and suggest alternatives
- **Code transformation:** Provide your application code and ask Kiro to help refactor trigger logic, replace sequences with UUIDs, or modify transaction patterns
- **Migration planning:** Ask Kiro to create a step-by-step migration plan based on your specific application architecture

**Example Kiro prompts:**

```
"Analyze this PostgreSQL schema for DSQL compatibility and suggest alternatives for any unsupported features"

"Help me refactor this trigger function into application-level logic for DSQL migration"

"Create a migration checklist for moving my Django application from PostgreSQL to DSQL"
```

### Aurora DSQL MCP server

The Aurora DSQL Model Context Protocol (MCP) server allows AI assistants like Claude to connect directly to your Aurora DSQL cluster and search Aurora DSQL documentation. This enables the AI to:

- Analyze your existing schema and suggest migration changes
- Test queries and verify compatibility during migration
- Provide accurate, up-to-date guidance based on the latest Aurora DSQL documentation

To use the Aurora DSQL MCP server with Claude or other AI assistants, see
the setup instructions for the [Aurora DSQL MCP server](SECTION_aurora-dsql-mcp-server.md "SECTION_aurora-dsql-mcp-server.md").

## Aurora DSQL

considerations for PostgreSQL compatibility

Aurora DSQL has feature support differences from self-managed PostgreSQL that enable its distributed architecture, serverless operation, and automatic scaling. Most applications work within these differences without modification.

For general considerations, see [Considerations for working with Amazon Aurora DSQL](considerations.md "considerations.md"). For quotas and limits, see [Cluster quotas and database limits in Amazon Aurora DSQL](CHAP_quotas.md "CHAP_quotas.md").

- Aurora DSQL uses a single built-in database named `postgres`. You can't
  create additional databases or rename or drop the `postgres`
  database.
- The `postgres` database uses UTF-8 character encoding. You can't change
  the server encoding.
- The database uses the `C` collation only.
- Aurora DSQL uses `UTC` as the system timezone. Postgres stores all timezone-aware
  dates and times internally in UTC. You can set the `TimeZone` configuration parameter
  to convert how it is displayed to the client and serve as the default for client input that
  the server will use to convert to UTC internally.
- The transaction isolation level is fixed at PostgreSQL `Repeatable
Read`.
- Transactions have the following constraints:
  - A transaction can't mix DDL and DML operations
  - A transaction can include only 1 DDL statement
  - A transaction can modify up to 3,000 rows, regardless of the number of
    secondary indexes
  - The 3,000-row limit applies to all DML statements (`INSERT`,
    `UPDATE`, `DELETE`)

- Database connections time out after 1 hour.
- Aurora DSQL doesn't currently let you run `GRANT [permission] ON DATABASE`.
  If you attempt to run that statement, Aurora DSQL returns the error message `ERROR:
unsupported object type in GRANT`.
- Aurora DSQL doesn't let non-admin user roles to run the `CREATE SCHEMA`
  command. You can't run the `GRANT [permission] on DATABASE` command and
  grant `CREATE` permissions on the database. If a non-admin user role tries
  to create a schema, Aurora DSQL returns with the error message `ERROR: permission
denied for database postgres`.
- Non-admin users can't create objects in the public schema. Only admin users can
  create objects in the public schema. The admin user role has permissions to grant
  read, write, and modify access to these objects to non-admin users, but it cannot
  grant `CREATE` permissions to the public schema itself. Non-admin users
  must use different, user-created schemas for object creation.

## Need help with migration?

If you encounter features that are critical for your migration but not currently supported in Aurora DSQL, see [Providing feedback on Amazon Aurora DSQL](providing-feedback.md "providing-feedback.md") for information on how to share feedback with AWS.
