# Show table information after creation

After you have created a table in Athena, its name displays in the
**Tables** list on the left in the Athena console. To show
information about the table and manage it, choose the vertical three dots next to the
table name in the Athena console.

- Preview table – Shows the first 10 rows
  of all columns by running the `SELECT * FROM
"`database_name`"."`table_name`"
LIMIT 10` statement in the Athena query editor.
- Generate table DDL – Generates a DDL
  statement that you can use to re-create the table by running the `SHOW CREATE TABLE`
  `table_name` statement in the Athena query
  editor.
- Load partitions – Runs the `MSCK REPAIR TABLE
`table_name`` statement in the Athena query
  editor. This option is available only if the table has partitions.
- Insert into editor – Inserts the name of
  the table into the query editor at the current editing location.
- Delete table – Displays a confirmation
  dialog box asking if you want to delete the table. If you agree, runs the
  `DROP TABLE
`table_name`` statement in the Athena query
  editor.
- Table properties – Shows the table name,
  database name, time created, and whether the table has encrypted data.
