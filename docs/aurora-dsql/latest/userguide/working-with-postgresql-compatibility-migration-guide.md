# Migrating from PostgreSQL to Aurora DSQL

Aurora DSQL is designed to be [PostgreSQL
compatible](working-with-postgresql-compatibility.md "working-with-postgresql-compatibility.md"), supporting core relational features such as ACID transactions, secondary indexes, joins, and standard DML operations. Most existing PostgreSQL applications can migrate to Aurora DSQL with minimal changes.

This section provides practical guidance for migrating your application to Aurora DSQL, including framework compatibility, migration patterns, and architectural considerations.

## Framework and ORM compatibility

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

Aurora DSQL is fully managed, so configuration is handled automatically based on workload patterns. Use the AWS Management Console or API to manage cluster settings.

**Benefit:** No need for database tuning or parameter management.

### Schema design patterns

Adapt these common PostgreSQL patterns for Aurora DSQL compatibility:

**Referential integrity patterns**

Aurora DSQL supports table relationships and `JOIN` operations. For referential integrity, implement validation in your application layer. This design aligns with modern distributed database patterns where application-layer validation provides more flexibility and avoids performance bottlenecks from cascading operations.

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

For temporary data handling, you SHOULD use common table expressions (CTEs) and subqueries, which provide flexible alternatives for complex queries.

**Alternative:** Use CTEs with `WITH`
clauses for temporary result sets, or regular tables with unique
naming for session-specific data.

**Automatic storage management**

Aurora DSQL eliminates tablespaces and manual storage management. Storage automatically scales and optimizes based on your data patterns.

**Benefit:** No need to monitor disk space, plan storage allocation, or manage tablespace configurations.

### Modern application patterns

Aurora DSQL encourages modern application development patterns that improve maintainability and performance:

**Application-level logic instead of database triggers**

For trigger-like functionality, implement event-driven logic in your application layer.

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
operations. For referential integrity, implement validation in your application layer. While
enforcing referential integrity can be valuable, cascading
operations (like cascading deletes) can create unexpected performance
issues—for example, deleting an order with 1,000 line items
becomes a 1,001-row transaction. Many customers avoid foreign
key constraints for this reason.

**Design pattern:** Implement referential integrity checks in your application layer, use eventual consistency patterns, or leverage AWS services for data validation.

### Operational simplifications

Aurora DSQL eliminates many traditional database maintenance tasks, reducing operational overhead:

**No manual maintenance required**

Aurora DSQL automatically manages storage optimization, statistics collection, and performance tuning. Traditional maintenance commands like `VACUUM` are handled by the system.

**Benefit:** Eliminates the need for database maintenance windows, vacuum scheduling, and system parameter tuning.

**Automatic partitioning and scaling**

Aurora DSQL automatically partitions and distributes your data based on access patterns. Use UUIDs or application-generated IDs for optimal distribution.

**Migration tip:** Remove manual partitioning logic and let Aurora DSQL handle data distribution. Use UUIDs or application-generated IDs for optimal distribution. If your application requires sequential identifiers, see [Sequences and identity columns](sequences-identity-columns.md "sequences-identity-columns.md").

## Aurora DSQL considerations for PostgreSQL compatibility

Aurora DSQL has feature support differences from self-managed PostgreSQL that enable its distributed architecture, serverless operation, and automatic scaling. Most applications work within these differences without modification.

For general considerations, see [Considerations for working with Amazon Aurora DSQL](considerations.md "considerations.md"). For quotas and limits, see [Cluster quotas and database limits in Amazon Aurora DSQL](CHAP_quotas.md "CHAP_quotas.md").

- Aurora DSQL uses a single built-in database named `postgres` per cluster. For logical separation, create separate Aurora DSQL clusters or use schemas within a single cluster.
- The `postgres` database uses UTF-8 character encoding, which provides broad international character support.
- The database uses the `C` collation only.
- Aurora DSQL uses `UTC` as the system timezone. Postgres stores all timezone-aware
  dates and times internally in UTC. You can set the `TimeZone` configuration parameter
  to convert how it is displayed to the client and serve as the default for client input that
  the server will use to convert to UTC internally.
- The transaction isolation level is fixed at PostgreSQL `Repeatable
Read`.
- Transactions have the following constraints:
  - DDL and DML operations require separate transactions
  - A transaction can include only 1 DDL statement
  - A transaction can modify up to 3,000 rows, regardless of the number of
    secondary indexes
  - The 3,000-row limit applies to all DML statements (`INSERT`,
    `UPDATE`, `DELETE`)

- Database connections time out after 1 hour.
- Aurora DSQL manages permissions through schema-level grants. Admin users create schemas using `CREATE SCHEMA` and grant access using `GRANT USAGE ON SCHEMA`. Admin users manage objects in the public schema, while non-admin users create objects in user-created schemas for clear ownership boundaries. For more information, see [Authorizing database roles to use SQL in your database](using-database-and-iam-roles.md#using-database-and-iam-roles-custom-database-roles-sql "using-database-and-iam-roles.md#using-database-and-iam-roles-custom-database-roles-sql").

## Need help with migration?

If you encounter features that are critical for your migration but not currently supported in Aurora DSQL, see [Providing feedback on Amazon Aurora DSQL](providing-feedback.md "providing-feedback.md") for information on how to share feedback with AWS.
