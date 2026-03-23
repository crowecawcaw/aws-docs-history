# Oracle to [.shared]`AURMySQL` migration quick tips

This section provides migration tips that can help save time as you transition from Oracle to Amazon Aurora MySQL-Compatible Edition (Aurora MySQL). These tips address many of the challenges faced by administrators new to Aurora MySQL. Some of these tips describe functional differences in similar features between Oracle and Aurora MySQL.

## Management

- In Aurora MySQL, _database snapshot_ is equivalent to RMAN backup in Oracle.
- Partitioning in Aurora MySQL doesn’t provide many of the Oracle features such as Partition Advisor, Preference Partitioning, Virtual Column-Based Partitioning, and Automatic List Partitioning.
- Unlike Oracle statistics, Aurora MySQL doesn’t collect detailed key value distribution in tables. Aurora MySQL only collects statistics on indexes.
- You can use Amazon services, such as Lambda, to replicate functionality of features not provided by MySQL, such as email.
- Amazon RDS manages parameters and backups. It is very useful for checking a parameter’s value against its default and comparing them to another parameter group.
- With just a few clicks, you can create replicas to implement high availability.
- Aurora MySQL doesn’t have an equivalent to database links. Aurora MySQL can only query across databases within the same instance.

## SQL

- Aurora MySQL doesn’t support statement-level triggers or triggers on system events.
- Aurora MySQL doesn’t support many cursor status checks. When you declare cursors in Aurora MySQL, make sure that you create an explicit `HANDLER` object.
- To run a stored procedure or function, use `CALL` instead of `EXECUTE`.
- To run a string as a query, use Aurora MySQL Prepared Statements instead of `EXECUTE(<String>)`.
- In Aurora MySQL, make sure that you terminate the `IF` blocks with `END IF`. Also, make sure that you terminate the `WHILE..LOOP` loops with `END LOOP`.
- Unlike Oracle, Aurora MySQL auto-commit default is set to `ON`. Be sure to set it to `OFF` to enable the database behavior similar to Oracle.
- Similar to Oracle, you can define collations at the server, database, and column level. You can’t define collations at the table level in Aurora MySQL.
- In Oracle, the `DELETE <Table Name>` syntax enables you to omit the `FROM` keyword. This syntax is not valid in Aurora MySQL. Add the `FROM` keyword to all `DELETE` statements.
- In Aurora MySQL, the `AUTO_INCREMENT` column property is similar to `IDENTITY` in Oracle.
- Error handling in Aurora MySQL has less features than Oracle. For special requirements, you can log or send alerts by inserting into tables or catching errors.
- Aurora MySQL doesn’t support the `MERGE` statement. Use the `REPLACE` statement and the `INSERT…​ON DUPLICATE KEY UPDATE` statement as alternatives.
- Unlike Oracle, you can’t concatenate strings in Aurora MySQL using the `||` operator.
- Aurora MySQL is much stricter than Oracle for statement terminators. Make sure that you use semicolons at the end of statements.
- Aurora MySQL doesn’t support the `BFILE`, `ROWID`, and `UROWID` data types.
- In MySQL, temporary tables are retained only for the session and only the session that created a temporary table can query it.
- MySQL doesn’t support unused or virtual columns and there is no workaround for replacing unused columns to achieve functionality similar to virtual columns. You can combine views and functions.
- MySQL doesn’t support materialized views. Use views or summary tables instead.
- Explore AWS to locate features that can be replaced with Amazon services. They can help you maintain your database and decrease costs.
- In MySQL, you can create multiple databases in a single instance. This approach can be useful for consolidation projects.
- Beware of control characters when copying and pasting a script to Aurora MySQL clients. Aurora MySQL is much more sensitive to control characters than Oracle and can result in frustrating syntax errors that are hard to find.
