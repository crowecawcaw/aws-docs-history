# Oracle to Aurora PostgreSQL migration quick tips

This section provides migration tips that can help save time as you transition from Oracle to Aurora PostgreSQL. They address many of the challenges faced by administrators new to Aurora PostgreSQL. Some of these tips describe functional differences in similar features between Oracle and Aurora PostgreSQL.

## Management

- In Aurora PostgreSQL terminology, _Database Snapshot_ is equivalent to Oracle RMAN backup.
- Partitioning in Aurora PostgreSQL is called `INHERITS` tables and act completely different in terms of management.
- Unlike Oracle statistics, Aurora PostgreSQL doesn’t collect detailed key value distribution; it relies on selectivity only. When troubleshooting execution, be aware that parameter values are insignificant to plan choices.
- Many missing features such as sending emails can be achieved with quick implementations of Amazon services (such as Lambda).
- Parameters and backups are managed by Amazon RDS. It is very useful in terms of checking parameter’s value against its default and comparing them to another parameter group.
- You can implement high availability in few clicks to create replicas.
- With Database Links, there are two options. The `db_link` extension is similar to Oracle and the `postgres_fdw` extension for using Foreign Data Wrapper.

## SQL

- Triggers work differently in Aurora PostgreSQL. The syntax for inserted and deleted for each row is `NEW` and `OLD`.
- Aurora PostgreSQL doesn’t support many cursors status checks. When you declare cursors in Aurora PostgreSQL, create an explicit `HANDLER` object.
- To run a stored procedure or function, use `SELECT` instead of `EXECUTE`.
- To run a string as a query, use Aurora PostgreSQL Prepared Statements instead of `EXECUTE (<String>)` syntax.
- In Aurora PostgreSQL, terminate `IF` blocks with `END IF` and the `WHILE..LOOP` loops with `END LOOP`.
- Unlike Oracle, in Aurora PostgreSQL auto commit is `ON`. Make sure to turn it off to make the database behavior more similar to Oracle.
- Aurora PostgreSQL doesn’t use special data types for `UNICODE` data. All string types may use any character set and any relevant collation.
- You can define collations at the server, database, and column level, similar to Oracle. You can’t define collations at the table level.
- Oracle `DELETE <Table Name>` syntax, which allows omitting the `FROM` keyword, is not valid in Aurora PostgreSQL. Add the `FROM` keyword to all delete statements.
- Aurora PostgreSQL `SERIAL` column property is similar to `IDENTITY` in Oracle.
- Error handling in Aurora PostgreSQL has less features, but for special requirements, you can log or send alerts by inserting into tables or catching errors.
- Aurora PostgreSQL doesn’t support the `MERGE` statement. Use the `REPLACE` statement and the `INSERT…​ ON DUPLICATE KEY UPDATE` statement as alternatives.
- You can concatenate strings in Aurora PostgreSQL using the `||` operator, as in Oracle.
- Aurora PostgreSQL is much stricter than Oracle in terms of statement terminators. Make sure that you always use a semicolon at the end of statements.
- There is no `CREATE PROCEDURE` syntax; only `CREATE FUNCTION`. You can create a function that returns void.
- Keep in mind that the window functions `GREATEST` and `LEAST` might get different results than the results that might being returned in Oracle from using these functions.
- PostgreSQL doesn’t support `SAVEPOINT` and `ROLLBACK TO SAVEPOINT` inside of functions.
- Aurora PostgreSQL doesn’t support `BFILE`, `ROWID`, and `UROWID` data types, try to use other data types.
- Aurora PostgreSQL keeps temporary tables only for the session level and only the session that created the table can query the temporary table.
- PostgreSQL doesn’t support unused or virtual columns, there is no workaround for replacing unused columns, for using similar functionality to the virtual columns, you can combine views and functions.
- PostgreSQL doesn’t support automatic or incremental `REFRESH` for materialized views, use triggers instead.
- Explore AWS to locate which features can be replaced with Amazon’s services, this can help you maintain your database and decrease costs.
- The architecture in PostgreSQL allows you to have multiple databases in a single instance, which is important for consolidation projects.
- Beware of control characters when copying and pasting a script to Aurora PostgreSQL clients. Aurora PostgreSQL is much more sensitive to control characters than Oracle and they result in frustrating syntax errors that are hard to find.
