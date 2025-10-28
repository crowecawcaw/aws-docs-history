# SQL syntax for

prepared statements

You can use the `PREPARE`, `EXECUTE` and `DEALLOCATE
 PREPARE` SQL statements to run parameterized queries in the Athena console
query editor.

- To specify parameters where you would normally use literal values, use
  question marks in the `PREPARE` statement.
- To replace the parameters with values when you run the query, use the
  `USING` clause in the `EXECUTE` statement.
- To remove a prepared statement from the prepared statements in a
  workgroup, use the `DEALLOCATE PREPARE` statement.
  The following sections provide additional detail about each of these
  statements.

###### Topics

- [PREPARE](querying-with-prepared-statements-prepare.md "querying-with-prepared-statements-prepare.md")
- [EXECUTE](querying-with-prepared-statements-execute.md "querying-with-prepared-statements-execute.md")
- [DEALLOCATE PREPARE](querying-with-prepared-statements-deallocate-prepare.md "querying-with-prepared-statements-deallocate-prepare.md")
