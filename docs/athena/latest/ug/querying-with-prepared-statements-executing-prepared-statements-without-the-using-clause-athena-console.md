# Run interactive prepared statements in the Athena console

If you run an existing prepared statement with the syntax `EXECUTE`
`prepared_statement` in the query editor, Athena opens the
**Enter parameters** dialog box so that you can enter the
values that would normally go in the `USING` clause of the `EXECUTE
 ... USING` statement.

###### To run a prepared statement using the **Enter parameters** dialog box

1. In the query editor, instead of using the syntax `EXECUTE
 prepared_statement USING`
   `value1``,`
   `value2`
   `...`, use the syntax `EXECUTE`
   `prepared_statement`.
2. Choose **Run**. The **Enter parameters**
   dialog box appears.

![Entering parameter values for a prepared statement in the Athena console.](images/querying-with-prepared-statements-2.png) 3. Enter the values in order in the **Execution parameters**
dialog box. Because the original text of the query is not visible, you must
remember the meaning of each positional parameter or have the prepared
statement available for reference. 4. Choose **Run**.
