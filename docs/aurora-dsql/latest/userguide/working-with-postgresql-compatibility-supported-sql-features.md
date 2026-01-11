# Supported SQL

for Aurora DSQL

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
| `FOR UPDATE`                      |                                  |

## Data Definition Language (DDL)

Aurora DSQL supports the following PostgreSQL DDL commands.

| Command  | Primary Clause         | Supported Clauses                                                                                                                                                                                                                                                                                       |
| -------- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CREATE` | `TABLE`                | For information about the supported syntax of the `CREATE TABLE`<br>command, see [CREATE TABLE](create-table-syntax-support.md "create-table-syntax-support.md").                                                                                                                                       |
| `ALTER`  | `TABLE`                | For information about the supported syntax of the `ALTER TABLE`<br>command, see [ALTER TABLE](alter-table-syntax-support.md "alter-table-syntax-support.md").                                                                                                                                           |
| `DROP`   | `TABLE`                |                                                                                                                                                                                                                                                                                                         |
| `CREATE` | `[UNIQUE] INDEX ASYNC` | You can use this command with the following parameters: `ON`,<br>`NULLS FIRST`, `NULLS LAST`.<br>For information about the supported syntax of the `CREATE INDEX<br>ASYNC` command, see [Asynchronous indexes in Aurora DSQL](working-with-create-index-async.md "working-with-create-index-async.md"). |
| `DROP`   | `INDEX`                |                                                                                                                                                                                                                                                                                                         |
| `CREATE` | `VIEW`                 | For more information about the supported syntax of the `CREATE<br>VIEW` command, see [CREATE VIEW](create-view.md "create-view.md").                                                                                                                                                                    |
| `ALTER`  | `VIEW`                 | For information about the supported syntax of the `ALTER VIEW`<br>command, see [ALTER VIEW](alter-view-syntax-support.md "alter-view-syntax-support.md").                                                                                                                                               |
| `DROP`   | `VIEW`                 | For information about the supported syntax of the `DROP VIEW`<br>command, see [DROP VIEW](drop-view-overview.md "drop-view-overview.md").                                                                                                                                                               |
| `CREATE` | `ROLE`, `WITH`         |                                                                                                                                                                                                                                                                                                         |
| `CREATE` | `FUNCTION`             | `LANGUAGE SQL`                                                                                                                                                                                                                                                                                          |
| `CREATE` | `DOMAIN`               |                                                                                                                                                                                                                                                                                                         |

## Data Manipulation Language (DML)

Aurora DSQL supports the following PostgreSQL DML commands.

| Command  | Primary clause | Supported clauses                |
| -------- | -------------- | -------------------------------- |
| `INSERT` | `INTO`         | `VALUES``SELECT`                 |
| `UPDATE` | `SET`          | `WHERE (SELECT)`<br>`FROM, WITH` |
| `DELETE` | `FROM`         | `USING`, `WHERE`                 |

## Data Control Language (DCL)

Aurora DSQL supports the following PostgreSQL DCL commands.

| Command  | Supported clauses                      |
| -------- | -------------------------------------- |
| `GRANT`  | `ON`, `TO`                             |
| `REVOKE` | `ON`, `FROM`, `CASCADE`,<br>`RESTRICT` |

## Transaction Control Language (TCL)

Aurora DSQL supports the following PostgreSQL TCL commands.

| Command  | Supported clauses |
| -------- | ----------------- | ------------------------------ | ------------- |
| `COMMIT` |                   |
| `BEGIN`  | [`WORK`           | `TRANSACTION`]<br>[`READ ONLY` | `READ WRITE`] |

## Utility commands

Aurora DSQL supports the following PostgreSQL utility commands:

- `EXPLAIN`
- `ANALYZE` (relation name only)
