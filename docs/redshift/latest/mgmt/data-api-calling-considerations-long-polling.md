Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# Reduce API calls with long polling

By default, Data API operations return an immediate response. If the operation is against an in-progress statement,
you must poll repeatedly until the statement reaches a terminal state. With long polling, set `WaitTimeSeconds` to a value between 1 and 30.
The API will delay returning a synchronous response until the statement finishes, or `WaitTimeSeconds` is reached,
whichever comes sooner.

Long polling is supported on [DescribeStatement](data-api-calling-cli-describe-statement.md "data-api-calling-cli-describe-statement.md"),
[ExecuteStatement](pass-sql-statements.md#data-api-calling-cli-execute-statement "pass-sql-statements.md#data-api-calling-cli-execute-statement"),
[BatchExecuteStatement](pass-sql-statements.md#data-api-calling-cli-batch-execute-statement "pass-sql-statements.md#data-api-calling-cli-batch-execute-statement"),
[GetStatementResult](data-api-calling-cli-get-statement-result.md "data-api-calling-cli-get-statement-result.md"), and
[GetStatementResultV2](data-api-calling-cli-get-statement-result.md "data-api-calling-cli-get-statement-result.md").

When an operation uses `WaitTimeSeconds` to submit a new statement or wait on an existing one:

- If the statement **completes** within
  the wait time, the response includes the terminal status or result
  data, depending on the operation.
- If the statement is **still running**
  when the wait time expires, the response returns the current
  in-progress status.
- If the statement **already completed**
  before the long-poll request is made, the API returns immediately
  with the terminal status.
- If `WaitTimeSeconds` is **omitted**,
  the default asynchronous behavior is preserved.

## Common use cases

The following are examples of when long polling may be useful:

- **Submit a short query and wait for
  completion** — Use
  `ExecuteStatement` with
  `WaitTimeSeconds`. When the query finishes or the
  wait time expires, the response returns the statement `Status`,
  `RedshiftPid`, and `HasResultSet`. To
  get full statement metadata, call `DescribeStatement`.
  If `HasResultSet` is `true`, call
  `GetStatementResult` to fetch results.
- **Long poll for status** — Use
  `ExecuteStatement` to submit the query, then call
  `DescribeStatement` with
  `WaitTimeSeconds`. When the query finishes,
  `DescribeStatement` returns full statement metadata
  including status, duration, and error details.
- **Long poll for result** — Use `ExecuteStatement`
  to submit the query, then call `GetStatementResult`
  with `WaitTimeSeconds`. When the query finishes, result
  data is returned directly. If the query is still running when the
  wait time expires, a `ResourceNotFoundException` is
  returned indicating no results are available yet.
- **Submit multiple queries and wait for the
  entire batch to complete** — Use
  `BatchExecuteStatement` with
  `WaitTimeSeconds`. The call holds open until all
  sub-statements complete and returns the batch parent ID and overall
  status.
- **Submit multiple queries and long poll status for a
  sub-statement** — Use
  `DescribeStatement` or
  `GetStatementResult` with the sub-statement ID and
  `WaitTimeSeconds`. Returns as soon as that
  sub-statement finishes, without waiting for the rest of the batch.
