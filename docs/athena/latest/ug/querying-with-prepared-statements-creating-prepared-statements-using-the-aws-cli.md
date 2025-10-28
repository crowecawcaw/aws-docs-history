# Create prepared statements using the AWS CLI

To use the AWS CLI to create a prepared statement, you can use one of the
following `athena` commands:

- Use the `create-prepared-statement` command and provide a
  query statement that has execution parameters.
- Use the `start-query-execution` command and provide a query
  string that uses the `PREPARE` syntax.

## Use create-prepared-statement

In a `create-prepared-statement` command, define the query text
in the `query-statement` argument, as in the following
example.

```
aws athena create-prepared-statement
--statement-name PreparedStatement1
--query-statement "SELECT * FROM table WHERE x = ?"
--work-group athena-engine-v2
```

## Use start-query-execution and the PREPARE syntax

Use the `start-query-execution` command. Put the
`PREPARE` statement in the `query-string`
argument, as in the following example:

```
aws athena start-query-execution
--query-string "PREPARE PreparedStatement1 FROM SELECT * FROM table WHERE x = ?"
--query-execution-context '{"Database": "default"}'
--result-configuration '{"OutputLocation": "s3://amzn-s3-demo-bucket/..."}'
```
