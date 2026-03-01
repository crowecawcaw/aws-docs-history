# Use parameterized queries

You can use Athena parameterized queries to re-run the same query with different parameter
values at execution time and help prevent SQL injection attacks. In Athena, parameterized
queries can take the form of execution parameters in any DML query or SQL prepared
statements.

- Queries with execution parameters can be done in a single step and are not
  workgroup specific. You place question marks in any DML query for the values that
  you want to parameterize. When you run the query, you declare the execution
  parameter values sequentially. The declaration of parameters and the assigning of
  values for the parameters can be done in the same query, but in a decoupled fashion.
  Unlike prepared statements, you can select the workgroup when you submit a query
  with execution parameters.
- Prepared statements require two separate SQL statements: `PREPARE` and
  `EXECUTE`. First, you define the parameters in the
  `PREPARE` statement. Then, you run an `EXECUTE` statement
  that supplies the values for the parameters that you defined. Prepared statements
  are workgroup specific; you cannot run them outside the context of the workgroup to
  which they belong.

## Considerations and limitations

- Parameterized queries are supported in Athena engine version 2 and later versions. For
  information about Athena engine versions, see [Athena engine versioning](engine-versions.md "engine-versions.md").
- Currently, parameterized queries are supported only for `SELECT`,
  `INSERT INTO`, `CTAS`, and `UNLOAD`
  statements.
- In parameterized queries, parameters are positional and are denoted by
  `?`. Parameters are assigned values by their order in the query.
  Named parameters are not supported.
- Currently, `?` parameters can be placed only in the
  `WHERE` clause. Syntax like `SELECT ? FROM table` is
  not supported.
- Question mark parameters cannot be placed in double or single quotes (that is,
  `'?'` and `"?"` are not valid syntax).
- For SQL execution parameters to be treated as strings, they must be enclosed
  in single quotes rather than double quotes.
- If necessary, you can use the `CAST` function when you enter a
  value for a parameterized term. For example, if you have a column of the
  `date` type that you have parameterized in a query and you want
  to query for the date `2014-07-05`, entering `CAST('2014-07-05'
AS DATE)` for the parameter value will return the result.
- Prepared statements are workgroup specific, and prepared statement names must
  be unique within the workgroup.
- IAM permissions for prepared statements are required. For more information,
  see [Configure access to prepared statements](security-iam-athena-prepared-statements.md "security-iam-athena-prepared-statements.md").
- Queries with execution parameters in the Athena console are limited to a
  maximum of 25 question marks.

###### Topics

- [Use execution parameters](querying-with-prepared-statements-querying-using-execution-parameters.md "querying-with-prepared-statements-querying-using-execution-parameters.md")
- [Use prepared statements](querying-with-prepared-statements-querying.md "querying-with-prepared-statements-querying.md")
- [Additional resources](querying-with-prepared-statements-additional-resources.md "querying-with-prepared-statements-additional-resources.md")
