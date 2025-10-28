# Calling the Amazon RDS Data API with the AWS CLI

You can call RDS Data API (Data API) using the AWS CLI.

The following examples use the AWS CLI for Data API. For more information, see
[AWS CLI reference for the Data
API](../../../cli/latest/reference/rds-data/index.md "../../../cli/latest/reference/rds-data/index.md").

In each example, replace the Amazon Resource Name (ARN) for the DB cluster with the ARN for
your Aurora DB cluster. Also, replace the secret ARN with the ARN of the secret
in Secrets Manager that allows access to the DB cluster.

###### Note

The AWS CLI can format responses in JSON.

###### Topics

- [Starting a SQL transaction](#data-api.calling.cli.begin-transaction "#data-api.calling.cli.begin-transaction")
- [Running a SQL statement](#data-api.calling.cli.execute-statement "#data-api.calling.cli.execute-statement")
- [Running a batch SQL statement over an array of data](#data-api.calling.cli.batch-execute-statement "#data-api.calling.cli.batch-execute-statement")
- [Committing a SQL transaction](#data-api.calling.cli.commit-transaction "#data-api.calling.cli.commit-transaction")
- [Rolling back a SQL transaction](#data-api.calling.cli.rollback-transaction "#data-api.calling.cli.rollback-transaction")

## Starting a SQL transaction

You can start a SQL transaction using the `aws rds-data
 begin-transaction` CLI command. The call returns a transaction
identifier.

###### Important

Within Data API, a transaction times out if there are no calls that use its transaction ID
in three minutes. If a transaction times out before it's
committed, Data API rolls it back automatically.

MySQL data definition language (DDL) statements inside a transaction cause an
implicit commit. We recommend that you run each MySQL DDL statement in a separate
`execute-statement` command with the
`--continue-after-timeout` option.

In addition to the common options, specify the `--database` option,
which provides the name of the database.

For example, the following CLI command starts a SQL transaction.

For Linux, macOS, or Unix:

```
aws rds-data begin-transaction --resource-arn "`arn:aws:rds:us-east-1:123456789012:cluster:mydbcluster`" \
--database "`mydb`" --secret-arn "`arn:aws:secretsmanager:us-east-1:123456789012:secret:mysecret`"
```

For Windows:

```
aws rds-data begin-transaction --resource-arn "`arn:aws:rds:us-east-1:123456789012:cluster:mydbcluster`" ^
--database "`mydb`" --secret-arn "`arn:aws:secretsmanager:us-east-1:123456789012:secret:mysecret`"
```

The following is an example of the response.

```
{
    "transactionId": "`ABC1234567890xyz`"
}
```

## Running a SQL statement

You can run a SQL statement using the `aws rds-data execute-statement`
CLI command.

You can run the SQL statement in a transaction by specifying the transaction
identifier with the `--transaction-id` option. You can start a
transaction using the `aws rds-data begin-transaction` CLI
command. You can end and commit a transaction using the `aws rds-data
 commit-transaction` CLI command.

###### Important

If you don't specify the `--transaction-id` option, changes that
result from the call are committed automatically.

In addition to the common options, specify the following options:

- `--sql` (required) – A SQL statement to run on the DB
  cluster.
- `--transaction-id` (optional) – The identifier of a
  transaction that was started using the
  `begin-transaction` CLI command. Specify the
  transaction ID of the transaction that you want to include the SQL
  statement in.
- `--parameters` (optional) – The parameters for the SQL
  statement.
- `--include-result-metadata | --no-include-result-metadata`
  (optional) – A value that indicates whether to include
  metadata in the results. The default is
  `--no-include-result-metadata`.
- `--database` (optional) – The name of the database.

The `--database` option might not work when you run a SQL statement after running `--sql "use
 `database_name`;"` in the previous request. We recommend that you use the
`--database` option instead of running `--sql "use
 `database_name`;"` statements.

- `--continue-after-timeout | --no-continue-after-timeout`
  (optional) – A value that indicates whether to continue running
  the statement after the call exceeds the Data API timeout interval of 45 seconds. The default is
  `--no-continue-after-timeout`.

For data definition language (DDL) statements, we recommend continuing to
run the statement after the call times out to avoid errors and the possibility of
corrupted data structures.

- `--format-records-as "JSON"|"NONE"` – An optional value that specifies whether to
  format the result set as a JSON string. The default is `"NONE"`.
  For usage information about processing JSON result sets, see
  [Processing Amazon RDS Data API query results in JSON format](data-api-json.md "data-api-json.md").

The DB cluster returns a response for the call.

###### Note

The response size limit is 1 MiB. If the call returns more than 1 MiB of response data, the call is terminated.

For Aurora Serverless v1, the maximum number of requests per second is 1,000. For all other supported databases, there is no limit.

For example, the following CLI command runs a single SQL statement and
omits the metadata in the results (the default).

For Linux, macOS, or Unix:

```
aws rds-data execute-statement --resource-arn "`arn:aws:rds:us-east-1:123456789012:cluster:mydbcluster`" \
--database "`mydb`" --secret-arn "`arn:aws:secretsmanager:us-east-1:123456789012:secret:mysecret`" \
--sql "`select * from mytable`"
```

For Windows:

```
aws rds-data execute-statement --resource-arn "`arn:aws:rds:us-east-1:123456789012:cluster:mydbcluster`" ^
--database "`mydb`" --secret-arn "`arn:aws:secretsmanager:us-east-1:123456789012:secret:mysecret`" ^
--sql "`select * from mytable`"
```

The following is an example of the response.

```
{
    "numberOfRecordsUpdated": 0,
    "records": [
        [
            {
                "longValue": `1`
            },
            {
                "stringValue": "`ValueOne`"
            }
        ],
        [
            {
                "longValue": `2`
            },
            {
                "stringValue": "`ValueTwo`"
            }
        ],
        [
            {
                "longValue": `3`
            },
            {
                "stringValue": "`ValueThree`"
            }
        ]
    ]
}
```

The following CLI command runs a single SQL statement in a transaction by
specifying the `--transaction-id` option.

For Linux, macOS, or Unix:

```
aws rds-data execute-statement --resource-arn "`arn:aws:rds:us-east-1:123456789012:cluster:mydbcluster`" \
--database "`mydb`" --secret-arn "`arn:aws:secretsmanager:us-east-1:123456789012:secret:mysecret`" \
--sql "`update mytable set quantity=5 where id=201`" --transaction-id "`ABC1234567890xyz`"
```

For Windows:

```
aws rds-data execute-statement --resource-arn "`arn:aws:rds:us-east-1:123456789012:cluster:mydbcluster`" ^
--database "`mydb`" --secret-arn "`arn:aws:secretsmanager:us-east-1:123456789012:secret:mysecret`" ^
--sql "`update mytable set quantity=5 where id=201`" --transaction-id "`ABC1234567890xyz`"
```

The following is an example of the response.

```
{
    "numberOfRecordsUpdated": 1
}
```

The following CLI command runs a single SQL statement with parameters.

For Linux, macOS, or Unix:

```
aws rds-data execute-statement --resource-arn "`arn:aws:rds:us-east-1:123456789012:cluster:mydbcluster`" \
--database "`mydb`" --secret-arn "`arn:aws:secretsmanager:us-east-1:123456789012:secret:mysecret`" \
--sql "insert into `mytable` values (`:id`, `:val`)" --parameters "[{\"name\": \"`id`\", \"value\": {\"longValue\": `1`}},{\"name\": \"`val`\", \"value\": {\"stringValue\": \"`value1`\"}}]"
```

For Windows:

```
aws rds-data execute-statement --resource-arn "`arn:aws:rds:us-east-1:123456789012:cluster:mydbcluster`" ^
--database "`mydb`" --secret-arn "`arn:aws:secretsmanager:us-east-1:123456789012:secret:mysecret`" ^
--sql "insert into `mytable` values (`:id`, `:val`)" --parameters "[{\"name\": \"`id`\", \"value\": {\"longValue\": `1`}},{\"name\": \"`val`\", \"value\": {\"stringValue\": \"`value1`\"}}]"
```

The following is an example of the response.

```
{
    "numberOfRecordsUpdated": 1
}
```

The following CLI command runs a data definition language (DDL) SQL statement. The DDL statement renames column
`job` to column `role`.

###### Important

For DDL statements, we recommend continuing to run the statement after
the call times out. When a DDL statement terminates before it is finished
running, it can result in errors and possibly corrupted data structures. To
continue running a statement after a call exceeds the RDS Data API timeout interval of 45 seconds, specify the `--continue-after-timeout`
option.

For Linux, macOS, or Unix:

```
aws rds-data execute-statement --resource-arn "`arn:aws:rds:us-east-1:123456789012:cluster:mydbcluster`" \
--database "`mydb`" --secret-arn "`arn:aws:secretsmanager:us-east-1:123456789012:secret:mysecret`" \
--sql "`alter table mytable change column job role varchar(100)`" --continue-after-timeout
```

For Windows:

```
aws rds-data execute-statement --resource-arn "`arn:aws:rds:us-east-1:123456789012:cluster:mydbcluster`" ^
--database "`mydb`" --secret-arn "`arn:aws:secretsmanager:us-east-1:123456789012:secret:mysecret`" ^
--sql "`alter table mytable change column job role varchar(100)`" --continue-after-timeout
```

The following is an example of the response.

```
{
    "generatedFields": [],
    "numberOfRecordsUpdated": 0
}
```

###### Note

The `generatedFields` data isn't supported by Aurora
PostgreSQL. To get the values of generated fields, use the
`RETURNING` clause. For more information, see [Returning data from modified rows](https://www.postgresql.org/docs/10/dml-returning.html "https://www.postgresql.org/docs/10/dml-returning.html") in the PostgreSQL
documentation.

## Running a batch SQL statement over an array of data

You can run a batch SQL statement over an array of data by using the
`aws rds-data batch-execute-statement` CLI command. You can
use this command to perform a bulk import or update operation.

You can run the SQL statement in a transaction by specifying the
transaction identifier with the `--transaction-id` option. You
can start a transaction by using the `aws rds-data
 begin-transaction` CLI command. You can end and commit a
transaction by using the `aws rds-data commit-transaction` CLI
command.

###### Important

If you don't specify the `--transaction-id` option,
changes that result from the call are committed automatically.

In addition to the common options, specify the following options:

- `--sql` (required) – A SQL statement to run on
  the DB cluster.

###### Tip

For MySQL-compatible statements, don't include a semicolon at the
end of the `--sql` parameter. A trailing semicolon might cause
a syntax error.

- `--transaction-id` (optional) – The identifier
  of a transaction that was started using the
  `begin-transaction` CLI command. Specify the
  transaction ID of the transaction that you want to include the SQL
  statement in.
- `--parameter-set` (optional) – The parameter
  sets for the batch operation.
- `--database` (optional) – The name of the database.

The DB cluster returns a response to the call.

###### Note

There isn't a fixed upper limit on the number of parameter sets.
However, the maximum size of the HTTP request submitted through Data API is
4 MiB. If the request exceeds this limit, Data API returns an error and
doesn't process the request. This 4 MiB limit includes the size of the
HTTP headers and the JSON notation in the request. Thus, the number of
parameter sets that you can include depends on a combination of factors,
such as the size of the SQL statement and the size of each parameter
set.

The response size limit is 1 MiB. If the call returns more than 1 MiB of response data, the call is terminated.

For Aurora Serverless v1, the maximum number of requests per second is 1,000. For all other supported databases, there is no limit.

For example, the following CLI command runs a batch SQL statement over an
array of data with a parameter set.

For Linux, macOS, or Unix:

```
aws rds-data batch-execute-statement --resource-arn "`arn:aws:rds:us-east-1:123456789012:cluster:mydbcluster`" \
--database "`mydb`" --secret-arn "`arn:aws:secretsmanager:us-east-1:123456789012:secret:mysecret`" \
--sql "insert into `mytable` values (`:id`, `:val`)" \
--parameter-sets "[[{\"name\": \"`id`\", \"value\": {\"longValue\": `1`}},{\"name\": \"`val`\", \"value\": {\"stringValue\": \"`ValueOne`\"}}],
[{\"name\": \"`id`\", \"value\": {\"longValue\": `2`}},{\"name\": \"`val`\", \"value\": {\"stringValue\": \"`ValueTwo`\"}}],
[{\"name\": \"`id`\", \"value\": {\"longValue\": `3`}},{\"name\": \"`val`\", \"value\": {\"stringValue\": \"`ValueThree`\"}}]]"
```

For Windows:

```
aws rds-data batch-execute-statement --resource-arn "`arn:aws:rds:us-east-1:123456789012:cluster:mydbcluster`" ^
--database "`mydb`" --secret-arn "`arn:aws:secretsmanager:us-east-1:123456789012:secret:mysecret`" ^
--sql "insert into `mytable` values (`:id`, `:val`)" ^
--parameter-sets "[[{\"name\": \"`id`\", \"value\": {\"longValue\": `1`}},{\"name\": \"`val`\", \"value\": {\"stringValue\": \"`ValueOne`\"}}],
[{\"name\": \"`id`\", \"value\": {\"longValue\": `2`}},{\"name\": \"`val`\", \"value\": {\"stringValue\": \"`ValueTwo`\"}}],
[{\"name\": \"`id`\", \"value\": {\"longValue\": `3`}},{\"name\": \"`val`\", \"value\": {\"stringValue\": \"`ValueThree`\"}}]]"
```

###### Note

Don't include line breaks in the `--parameter-sets`
option.

## Committing a SQL transaction

Using the `aws rds-data commit-transaction` CLI command, you can
end a SQL transaction that you started with `aws rds-data
 begin-transaction` and commit the changes.

In addition to the common options, specify the following option:

- `--transaction-id` (required) – The identifier of a
  transaction that was started using the
  `begin-transaction` CLI command. Specify the
  transaction ID of the transaction that you want to end and
  commit.

For example, the following CLI command ends a SQL transaction and commits the
changes.

For Linux, macOS, or Unix:

```
aws rds-data commit-transaction --resource-arn "`arn:aws:rds:us-east-1:123456789012:cluster:mydbcluster`" \
--secret-arn "`arn:aws:secretsmanager:us-east-1:123456789012:secret:mysecret`" \
--transaction-id "`ABC1234567890xyz`"
```

For Windows:

```
aws rds-data commit-transaction --resource-arn "`arn:aws:rds:us-east-1:123456789012:cluster:mydbcluster`" ^
--secret-arn "`arn:aws:secretsmanager:us-east-1:123456789012:secret:mysecret`" ^
--transaction-id "`ABC1234567890xyz`"
```

The following is an example of the response.

```
{
    "transactionStatus": "Transaction Committed"
}
```

## Rolling back a SQL transaction

Using the `aws rds-data rollback-transaction` CLI command, you can
roll back a SQL transaction that you started with `aws rds-data
 begin-transaction`. Rolling back a transaction cancels its
changes.

###### Important

If the transaction ID has expired, the transaction was rolled back automatically. In this case,
an `aws rds-data rollback-transaction` command that specifies the expired transaction ID
returns an error.

In addition to the common options, specify the following option:

- `--transaction-id` (required) – The identifier of a
  transaction that was started using the
  `begin-transaction` CLI command. Specify the
  transaction ID of the transaction that you want to roll back.

For example, the following AWS CLI command rolls back a SQL transaction.

For Linux, macOS, or Unix:

```
aws rds-data rollback-transaction --resource-arn "`arn:aws:rds:us-east-1:123456789012:cluster:mydbcluster`" \
--secret-arn "`arn:aws:secretsmanager:us-east-1:123456789012:secret:mysecret`" \
--transaction-id "`ABC1234567890xyz`"
```

For Windows:

```
aws rds-data rollback-transaction --resource-arn "`arn:aws:rds:us-east-1:123456789012:cluster:mydbcluster`" ^
--secret-arn "`arn:aws:secretsmanager:us-east-1:123456789012:secret:mysecret`" ^
--transaction-id "`ABC1234567890xyz`"
```

The following is an example of the response.

```
{
    "transactionStatus": "Rollback Complete"
    }
```
