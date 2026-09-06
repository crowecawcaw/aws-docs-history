# Supported SQL for Aurora DSQL

Aurora DSQL supports a wide range of core PostgreSQL SQL features. In the following sections, you
can learn about general PostgreSQL expression support. This list is not exhaustive.

## `SELECT` command

Aurora DSQL supports the following clauses of the `SELECT` command.

| Primary clause                    | Supported clauses                |
| --------------------------------- | -------------------------------- |
| `FROM`                            |                                  |
| `GROUP BY`                        | `ALL`, `DISTINCT`                |
| `ORDER BY`                        | `ASC`, `DESC`, `NULLS`           |
| `LIMIT`                           |                                  |
| `DISTINCT`                        |                                  |
| `HAVING`                          |                                  |
| `USING`                           |                                  |
| `WITH` (common table expressions) |                                  |
| `INNER JOIN`                      | `ON`                             |
| `OUTER JOIN`                      | `LEFT`, `RIGHT`, `FULL`,<br>`ON` |
| `CROSS JOIN`                      | `ON`                             |
| `UNION`                           | `ALL`                            |
| `INTERSECT`                       | `ALL`                            |
| `EXCEPT`                          | `ALL`                            |
| `OVER`                            | `RANK ()`, `PARTITION BY`        |
| `FOR { UPDATE                     | KEY SHARE }`                     | Transaction limits apply. For more information, see [Cluster quotas and database limits in Amazon Aurora DSQL](CHAP_quotas.md "CHAP_quotas.md"). To understand how this impacts concurrent transactions,<br>see [Concurrency control in Aurora DSQL](working-with-concurrency-control.md "working-with-concurrency-control.md"). |

## Data Definition Language (DDL)

Aurora DSQL supports the following PostgreSQL DDL commands.

| Command      | Primary Clause          | Supported Clauses                                                                                                                                                                                                                                          |
| ------------ | ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CREATE`     | `TABLE`                 | For information about the supported syntax of the `CREATE TABLE`<br>command, see [CREATE TABLE](create-table-syntax-support.md "create-table-syntax-support.md").                                                                                          |
| `ALTER`      | `TABLE`                 | For information about the supported syntax of the `ALTER TABLE`<br>command, see [ALTER TABLE](alter-table-syntax-support.md "alter-table-syntax-support.md").                                                                                              |
| `DROP`       | `TABLE`                 |                                                                                                                                                                                                                                                            |
| `CREATE`     | `[UNIQUE] INDEX ASYNC`  | Index keys can be column names or expressions. You can also use<br>`INCLUDE`, `NULLS FIRST`, `NULLS LAST`, and<br>`NULLS [NOT] DISTINCT`.<br>See [CREATE INDEX](create-index-syntax-support.md "create-index-syntax-support.md") for the supported syntax. |
| `DROP`       | `INDEX`                 |                                                                                                                                                                                                                                                            |
| `CREATE`     | `STATISTICS`            | For information about the supported syntax of the `CREATE<br>STATISTICS` command, see [CREATE STATISTICS](create-statistics-syntax-support.md "create-statistics-syntax-support.md").                                                                      |
| `ALTER`      | `STATISTICS`            | For information about the supported syntax of the `ALTER<br>STATISTICS` command, see [ALTER STATISTICS](alter-statistics-syntax-support.md "alter-statistics-syntax-support.md").                                                                          |
| `DROP`       | `STATISTICS`            | For information about the supported syntax of the `DROP<br>STATISTICS` command, see [DROP STATISTICS](drop-statistics-syntax-support.md "drop-statistics-syntax-support.md").                                                                              |
| `CREATE`     | `VIEW`                  | For more information about the supported syntax of the `CREATE<br>VIEW` command, see [CREATE VIEW](create-view.md "create-view.md").                                                                                                                       |
| `ALTER`      | `VIEW`                  | For information about the supported syntax of the `ALTER VIEW`<br>command, see [ALTER VIEW](alter-view-syntax-support.md "alter-view-syntax-support.md").                                                                                                  |
| `DROP`       | `VIEW`                  | For information about the supported syntax of the `DROP VIEW`<br>command, see [DROP VIEW](drop-view-overview.md "drop-view-overview.md").                                                                                                                  |
| `CREATE`     | `SEQUENCE`              | For information about the supported syntax of the `CREATE<br>SEQUENCE` command, see [CREATE SEQUENCE](create-sequence-syntax-support.md "create-sequence-syntax-support.md").                                                                              |
| `ALTER`      | `SEQUENCE`              | For information about the supported syntax of the `ALTER<br>SEQUENCE` command, see [ALTER SEQUENCE](alter-sequence-syntax-support.md "alter-sequence-syntax-support.md").                                                                                  |
| `DROP`       | `SEQUENCE`              | For information about the supported syntax of the `DROP<br>SEQUENCE` command, see [DROP SEQUENCE](drop-sequence-syntax-support.md "drop-sequence-syntax-support.md").                                                                                      |
| `CREATE`     | `ROLE`, `WITH`          |                                                                                                                                                                                                                                                            |
| `CREATE`     | `FUNCTION`              | `LANGUAGE SQL`                                                                                                                                                                                                                                             |
| `CREATE`     | `DOMAIN`                |                                                                                                                                                                                                                                                            |
| `CREATE`     | `SCHEMA`                | You can nest `CREATE SEQUENCE` and `GRANT` statements<br>in the `CREATE SCHEMA` command.                                                                                                                                                                   |
| `ALTER`      | `USER`, `ROLE`, `GROUP` | `RENAME TO`                                                                                                                                                                                                                                                |
| `ALTER`      | `ROUTINE`               | `SET SCHEMA`, `OWNER TO`,<br>`RENAME TO`                                                                                                                                                                                                                   |
| `COMMENT ON` | `ROUTINE`               | None                                                                                                                                                                                                                                                       |
| `DROP`       | `ROUTINE`               | None                                                                                                                                                                                                                                                       |

## Data Manipulation Language (DML)

Aurora DSQL supports the following PostgreSQL DML commands.

| Command  | Primary clause | Supported clauses                       |
| -------- | -------------- | --------------------------------------- |
| `INSERT` | `INTO`         | `VALUES`<br>`SELECT`<br>`[ON CONFLICT]` |
| `UPDATE` | `SET`          | `WHERE (SELECT)`<br>`FROM, WITH`        |
| `DELETE` | `FROM`         | `USING`, `WHERE`                        |

## Data Control Language (DCL)

Aurora DSQL supports the following PostgreSQL DCL commands.

| Command                    | Supported clauses                                                                        |
| -------------------------- | ---------------------------------------------------------------------------------------- |
| `GRANT`                    | `ON`, `TO`<br>Supported object types include `ROUTINE`.                                  |
| `REVOKE`                   | `ON`, `FROM`, `CASCADE`,<br>`RESTRICT`<br>Supported object types include `ROUTINE`.      |
| `ALTER DEFAULT PRIVILEGES` | Configure default privileges for `TABLE`, `SEQUENCE`,<br>`FUNCTION`, and `TYPE` objects. |

## Transaction Control Language (TCL)

Aurora DSQL supports the following PostgreSQL TCL commands.

| Command             | Supported clauses                                    | Alias                                                                  |
| ------------------- | ---------------------------------------------------- | ---------------------------------------------------------------------- |
| `COMMIT`            | [`WORK`                                              | `TRANSACTION`]<br>[`AND NO CHAIN`]                                     | `END`        |
| `BEGIN`             | [`WORK`                                              | `TRANSACTION`]<br>[`ISOLATION LEVEL REPEATABLE READ`]<br>[`READ WRITE` | `READ ONLY`] |     |
| `START TRANSACTION` | [`ISOLATION LEVEL REPEATABLE READ`]<br>[`READ WRITE` | `READ ONLY`]                                                           |              |
| `ROLLBACK`          | [`WORK`                                              | `TRANSACTION`]<br>[`AND NO CHAIN`]                                     | `ABORT`      |
| `SET CONSTRAINTS`   | {`ALL`                                               | ``name` [, ...]`}<br>{`DEFERRED`                                       | `IMMEDIATE`} |     |

## Utility commands

Aurora DSQL supports the following PostgreSQL utility commands:

- `EXPLAIN`
- `ANALYZE` (relation name only)
