

# Amazon RDS Data API operations reference
<a name="data-api-operations"></a>

The Amazon RDS Data API provides the following operations to perform SQL statements.



|  Data API operation  |  AWS CLI command  |  Description  | 
| --- | --- | --- | 
| [`ExecuteStatement`](https://docs.aws.amazon.com/rdsdataservice/latest/APIReference/API_ExecuteStatement.html) | [`aws rds-data execute-statement`](https://docs.aws.amazon.com/cli/latest/reference/rds-data/execute-statement.html) | Runs a SQL statement on a database. | 
| [`BatchExecuteStatement`](https://docs.aws.amazon.com/rdsdataservice/latest/APIReference/API_BatchExecuteStatement.html) | [`aws rds-data batch-execute-statement`](https://docs.aws.amazon.com/cli/latest/reference/rds-data/batch-execute-statement.html) | Runs a batch SQL statement over an array of data for bulk update and insert operations. You can run a data manipulation language (DML) statement with an array of parameter sets. A batch SQL statement can provide a significant performance improvement over individual insert and update statements. | 

You can use either operation to run individual SQL statements or to run transactions. For transactions, Data API provides the following operations.



|  Data API operation  |  AWS CLI command  |  Description  | 
| --- | --- | --- | 
| [`BeginTransaction`](https://docs.aws.amazon.com/rdsdataservice/latest/APIReference/API_BeginTransaction.html) | [`aws rds-data begin-transaction`](https://docs.aws.amazon.com/cli/latest/reference/rds-data/begin-transaction.html) | Starts a SQL transaction. | 
| [`CommitTransaction`](https://docs.aws.amazon.com/rdsdataservice/latest/APIReference/API_CommitTransaction.html) | [`aws rds-data commit-transaction`](https://docs.aws.amazon.com/cli/latest/reference/rds-data/commit-transaction.html) | Ends a SQL transaction and commits the changes. | 
| [`RollbackTransaction`](https://docs.aws.amazon.com/rdsdataservice/latest/APIReference/API_RollbackTransaction.html) | [`aws rds-data rollback-transaction`](https://docs.aws.amazon.com/cli/latest/reference/rds-data/rollback-transaction.html) | Performs a rollback of a transaction. | 

The operations for performing SQL statements and supporting transactions have the following common Data API parameters and AWS CLI options. Some operations support other parameters or options.



|  Data API operation parameter  |  AWS CLI command option  |  Required  |  Description  | 
| --- | --- | --- | --- | 
| `resourceArn` | `--resource-arn` | Yes | The Amazon Resource Name (ARN) of the Aurora DB cluster. The cluster must be in the same AWS account as the IAM role or user that invokes the Data API. To access a cluster in a different account, assume a role in that account. | 
| `secretArn` | `--secret-arn` | Yes | The name or ARN of the secret that enables access to the DB cluster. | 

RDS Data API supports the following data types for Aurora MySQL:
+ `TINYINT(1)`, `BOOLEAN`, `BOOL`
+ `TINYINT`
+ `SMALLINT` [`SIGNED` \| `UNSIGNED`]
+ `MEDIUMINT` [`SIGNED` \| `UNSIGNED`]
+ `INT` [`SIGNED` \| `UNSIGNED`]
+ `BIGINT` [`SIGNED` \| `UNSIGNED`]
+ `FLOAT`
+ `DOUBLE`
+ `VARCHAR`, `CHAR`, `TEXT`, `ENUM`
+ `VARBINARY`, `BINARY`, `BLOB`
+ `DATE`, `TIME`, `DATETIME`, `TIMESTAMP`
+ `DECIMAL`
+ `JSON`
+ `BIT`, `BIT(N)` 

RDS Data API supports following Aurora PostgreSQL scalar types:
+ `BOOL`
+ `BYTEA`
+ `DATE`
+ `CIDR`
+ `DECIMAL`, `NUMERIC`
+ `ENUM`
+ `FLOAT8`, `DOUBLE PRECISION`
+ `INET`
+ `INT`, `INT4`, `SERIAL`
+ `INT2`, `SMALLINT`, `SMALLSERIAL`
+ `INT8`, `BIGINT`, `BIGSERIAL`
+ `JSONB`, `JSON`
+ `REAL`, `FLOAT`
+ `TEXT`, `CHAR(N)`, `VARCHAR`, `NAME`
+ `TIME`
+ `TIMESTAMP`
+ `UUID`
+ `VECTOR`

RDS Data API supports the following Aurora PostgreSQL array types:
+ `BOOL[]`, `BIT[]`
+ `DATE[]`
+ `DECIMAL[]`, `NUMERIC[]`
+ `FLOAT8[]`, `DOUBLE PRECISION[]`
+ `INT[]`, `INT4[]`
+ `INT2[]`
+ `INT8[]`, `BIGINT[]`
+ `JSON[]`
+ `REAL[]`, `FLOAT[]`
+ `TEXT[]`, `CHAR(N)[]`, `VARCHAR[]`, `NAME[]`
+ `TIME[]`
+ `TIMESTAMP[]`
+ `UUID[]`

You can use parameters in Data API calls to `ExecuteStatement` and `BatchExecuteStatement`, and when you run the AWS CLI commands `execute-statement` and `batch-execute-statement`. To use a parameter, you specify a name-value pair in the `SqlParameter` data type. You specify the value with the `Field` data type. The following table maps Java Database Connectivity (JDBC) data types to the data types that you specify in Data API calls.



|  JDBC data type  |  Data API data type  | 
| --- | --- | 
| `INTEGER, TINYINT, SMALLINT, BIGINT` | `LONG` (or `STRING`) | 
| `FLOAT, REAL, DOUBLE` | `DOUBLE` | 
| `DECIMAL` | `STRING` | 
| `BOOLEAN, BIT` | `BOOLEAN` | 
| `BLOB, BINARY, LONGVARBINARY, VARBINARY` | `BLOB` | 
| `CLOB` | `STRING` | 
| Other types (including types related to date and time) | `STRING` | 

**Note**  
 You can specify the `LONG` or `STRING` data type in your Data API call for `LONG` values returned by the database. We recommend that you do so to avoid losing precision for extremely large numbers, which can happen when you work with JavaScript. 

Certain types, such as `DECIMAL` and `TIME`, require a hint so that Data API passes `String` values to the database as the correct type. To use a hint, include values for `typeHint` in the `SqlParameter` data type. The possible values for `typeHint` are the following:
+ `DATE` – The corresponding `String` parameter value is sent as an object of `DATE` type to the database. The accepted format is `YYYY-MM-DD`.
+ `DECIMAL` – The corresponding `String` parameter value is sent as an object of `DECIMAL` type to the database.
+ `JSON` – The corresponding `String` parameter value is sent as an object of `JSON` type to the database.
+ `TIME` – The corresponding `String` parameter value is sent as an object of `TIME` type to the database. The accepted format is `HH:MM:SS[.FFF]`.
+ `TIMESTAMP` – The corresponding `String` parameter value is sent as an object of `TIMESTAMP` type to the database. The accepted format is `YYYY-MM-DD HH:MM:SS[.FFF]`.
+  `UUID` – The corresponding `String` parameter value is sent as an object of `UUID` type to the database. 
**Note**  
Currently, Data API doesn't support arrays of Universal Unique Identifiers (UUIDs).

**Note**  
 For Amazon Aurora PostgreSQL, Data API always returns the Aurora PostgreSQL data type `TIMESTAMPTZ` in UTC time zone.