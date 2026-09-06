

# Migration quick tips
<a name="chap-sql-server-aurora-pg.tips"></a>

This section provides migration tips that can help save time as you transition from Microsoft SQL Server to Aurora PostgreSQL. They address many of the challenges faced by administrators new to Aurora PostgreSQL. Some of these tips describe functional differences in similar features between SQL Server and Aurora PostgreSQL.

## Management
<a name="chap-sql-server-aurora-pg.tips.management"></a>
+ The equivalent of SQL Server’s `CREATE DATABASE…​ AS SNAPSHOT OF…​` resembles Aurora PostgreSQL database cloning. However, unlike SQL Server snapshots, which are read-only, you can update Aurora PostgreSQL cloned databases.
+ In Aurora PostgreSQL terminology, *Database Snapshot* is equivalent to SQL Server `BACKUP DATABASE…​ WITH COPY_ONLY`.
+ Partitioning in Aurora PostgreSQL is called `INHERITS` tables and act completely different in terms of management.
+ Unlike SQL Server’s statistics, Aurora PostgreSQL doesn’t collect detailed key value distribution; it relies on selectivity only. When troubleshooting run issues, be aware that parameter values are insignificant to plan choices.
+ You can achieve many missing features, such as sending emails, with quick implementations of Amazon services such as Lambda.
+ Parameters and backups are managed by Amazon RDS. It is very useful in terms of checking parameter’s value against its default and comparing them to another parameter group.
+ You can implement high availability in few clicks to create replicas.
+ With Database Links, the `db_link` extension is similar to SQL Server.

## SQL
<a name="chap-sql-server-aurora-pg.tips.sql"></a>
+ Triggers work differently in Aurora PostgreSQL. You can run triggers for each row. The syntax for inserted and deleted for each row is `new` and `old`.
+  Aurora PostgreSQL doesn’t support `@@FETCH_STATUS` system parameter for cursors. When you declare cursors in Aurora PostgreSQL, create an explicit `HANDLER` object.
+ To run a stored procedure or function, use `SELECT` instead of `EXECUTE`.
+ To run a string as a query, use Aurora PostgreSQL Prepared Statements instead of `EXECUTE (<String>)` syntax.
+ In Aurora PostgreSQL, terminate `IF` blocks with `END IF` and the `WHILE..LOOP` loops with `END LOOP`.
+ In Aurora PostgreSQL, use `START TRANSACTION` to open a transaction instead of `BEGIN TRANSACTION`. Use `COMMIT` and `ROLLBACK` without the `TRANSACTION` keyword.
+  Aurora PostgreSQL doesn’t use special data types for `UNICODE` data. All string types may use any character set and any relevant collation.
+ You can define collations at the server, database, and column level, similar to SQL Server. You can’t define collations at the table level.
+  Aurora PostgreSQL doesn’t support `DELETE <Table Name>` syntax, where you drop the `FROM` keyword. Add the `FROM` keyword to all `DELETE` statements.
+ In Aurora PostgreSQL, you can use multiple rows with `NULL` for a `UNIQUE` constraint. In SQL Server, you can only use one. Aurora PostgreSQL follows the behavior specified in the ANSI standard.
+  Aurora PostgreSQL `SERIAL` column property is similar to `IDENTITY` in SQL Server. However, there is a major difference in the way sequences are maintained. SQL Server caches a set of values in memory and records the last allocation on disk. When the service restarts, some values may be lost, but the sequence continues from where it left off. In Aurora PostgreSQL, each time you restart the service, the seed value to `SERIAL` is reset to one increment interval larger than the largest existing value. Sequence position isn’t maintained across service restarts.
+ Parameter names in Aurora PostgreSQL don’t require a preceding `@`. You can declare local variables such as `SET schema.test = value` and get the value by running the `SELECT current_setting('username.test');` query.
+ Local parameter scope isn’t limited to the run scope. You can define or set a parameter in one statement, run it, and then query it in the following batch.
+ Error handling in Aurora PostgreSQL has less features, but for special requirements, you can log or send alerts by inserting into tables or catching errors.
+  Aurora PostgreSQL doesn’t support the `MERGE` statement. Use the `REPLACE` statement and the `INSERT…​ ON DUPLICATE KEY UPDATE` statement as alternatives.
+ In Aurora PostgreSQL, you can’t concatenate strings with the `+` operator. Use the `CONCAT` function instead. For example, `CONCAT('A', 'B')`.
+  Amazon Aurora PostgreSQL-Compatible Edition (Aurora PostgreSQL) doesn’t support aliasing in the select list using the `String Alias = Expression`. Aurora PostgreSQL treats it as a logical predicate, returns `0` or `FALSE`, and will alias the column with the full expression. Use the `AS` syntax instead. Also note that this syntax has been deprecated as of SQL Server 2008 R2.
+  Aurora PostgreSQL has a large set of string functions that is much more diverse than SQL Server. Some of the more useful string functions are:
  +  `TRIM` isn’t limited to full trim or spaces. The syntax is `TRIM([{BOTH | LEADING | TRAILING} [<remove string>] FROM] <source string>))`.
  +  `LENGTH` in PostgreSQL is equivalent to `DATALENGTH` in T-SQL. `CHAR_LENGTH` is the equivalent of T-SQL `LENGTH`.
  +  `SUBSTRING_INDEX` returns a substring from a string before the specified number of occurrences of the delimiter.
  +  `FIELD` returns the index position of the first argument in the subsequent arguments.
  +  `POSITION` returns the index position of the first argument within the second argument.
  +  `REGEXP_MATCHES` provides support for regular expressions.
  + For more information, see [String Functions and Operators](https://www.postgresql.org/docs/13/functions-string.html).
+ The Aurora PostgreSQL `CAST` function is for casting between collation and not other data types. Use `CONVERT` for casting data types.
+  Aurora PostgreSQL is much stricter than SQL Server in terms of statement terminators. Make sure that you always use a semicolon at the end of statements.
+ In Aurora PostgreSQL, you can’t use the `CREATE PROCEDURE` syntax. You can use only the `CREATE FUNCTION` syntax. You can create a function that returns void.
+ Beware of control characters when copying and pasting a script to Aurora PostgreSQL clients. Aurora PostgreSQL is much more sensitive to control characters than SQL Server and they result in frustrating syntax errors that are hard to find.