# Run queries with execution parameters in the Athena console

When you run a parameterized query that has execution parameters (question marks)
in the Athena console, you are prompted for the values in the order in which the
question marks occur in the query.

###### To run a query that has execution parameters

1. Enter a query with question mark placeholders in the Athena editor, as in
   the following example.

```
SELECT * FROM "my_database"."my_table"
WHERE year = ? and month= ? and day= ?
```

2. Choose **Run.**
3. In the **Enter parameters** dialog box, enter a value in
   order for each of the question marks in the query.

![Enter values for the query parameters in order](images/querying-with-prepared-statements-1.png) 4. When you are finished entering the parameters, choose
**Run**. The editor shows the query results for the
parameter values that you entered.
At this point, you can do one of the following:

- Enter different parameter values for the same query, and then choose
  **Run again**.
- To clear all of the values that you entered at once, choose
  **Clear**.
- To edit the query directly (for example, to add or remove question marks),
  close the **Enter parameters** dialog box first.
- To save the parameterized query for later use, choose
  **Save** or **Save as**, and then give
  the query a name. For more information about using saved queries, see [Use saved queries](saved-queries.md "saved-queries.md").
  As a convenience, the **Enter parameters** dialog box remembers
  the values that you entered previously for the query as long as you use the same tab
  in the query editor.
