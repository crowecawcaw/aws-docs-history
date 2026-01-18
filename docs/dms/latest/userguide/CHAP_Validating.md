# AWS DMS data validation

###### Topics

- [Replication task statistics](#CHAP_Validating.TaskStatistics "#CHAP_Validating.TaskStatistics")
- [Replication task statistics with Amazon CloudWatch](#CHAP_Validating.TaskStatistics.CloudWatch "#CHAP_Validating.TaskStatistics.CloudWatch")
- [Revalidating tables during a task](#CHAP_Validating.Revalidating "#CHAP_Validating.Revalidating")
- [Using JSON editor to modify validation rules](#CHAP_Validating.JSONEditor "#CHAP_Validating.JSONEditor")
- [Validation only tasks](#CHAP_Validating.ValidationOnly "#CHAP_Validating.ValidationOnly")
- [Troubleshooting](#CHAP_Validating.Troubleshooting "#CHAP_Validating.Troubleshooting")
- [Redshift Validation Performance](#CHAP_Validating.Redshift "#CHAP_Validating.Redshift")
- [Enhanced data validation for AWS Database Migration Service](#CHAP_Validating_Enhanced "#CHAP_Validating_Enhanced")
- [Limitations](#CHAP_Validating.Limitations "#CHAP_Validating.Limitations")
- [Amazon S3 target data validation](CHAP_Validating_S3.md "CHAP_Validating_S3.md")
- [AWS DMS data resync](CHAP_Validating.md "CHAP_Validating.md")
  AWS DMS provides support for data validation to ensure that your data was migrated
  accurately from the source to the target. If enabled, validation begins immediately
  after a full load is performed for a table. Validation compares the incremental
  changes for a CDC-enabled task as they occur.

During data validation, AWS DMS compares each row in the source with its corresponding
row at the target, verifies the rows contain the same data, and reports any mismatches.
To accomplish this AWS DMS issues appropriate queries to retrieve the data. Note that these
queries will consume additional resources at the source and target as well as additional
network resources.

For a CDC only task with validation enabled, all pre-existing data in a table is validated before starting validation of new data.

Data validation works with the following source databases wherever AWS DMS supports
them as source endpoints:

- Oracle
- PostgreSQL-compatible database (PostgreSQL, Aurora PostgreSQL, or Aurora Serverless for PostgreSQL)
- MySQL-compatible database (MySQL, MariaDB, Aurora MySQL, or Aurora Serverless for MySQL)
- Microsoft SQL Server
- IBM Db2 LUW
  Data validation works with the following target databases wherever AWS DMS supports
  them as target endpoints:

- Oracle
- PostgreSQL-compatible database (PostgreSQL, Aurora PostgreSQL, or Aurora Serverless for PostgreSQL)
- MySQL-compatible database (MySQL, MariaDB, Aurora MySQL, or Aurora Serverless for MySQL)
- Microsoft SQL Server
- IBM Db2 LUW
- Amazon Redshift
- Amazon S3. For information about validating Amazon S3 target data, see [Amazon S3 target data validation](CHAP_Validating_S3.md "CHAP_Validating_S3.md").
  For more information about the supported endpoints, see [Working with AWS DMS endpoints](CHAP_Endpoints.md "CHAP_Endpoints.md").

Data validation requires additional time, beyond the amount required for the
migration itself. The extra time required depends on how much data was
migrated.

For more information about these settings, see [Data
validation task settings](CHAP_Tasks.CustomizingTasks.TaskSettings.md "CHAP_Tasks.CustomizingTasks.TaskSettings.md").

For an example of `ValidationSettings` task settings in a JSON file, see [Task settings example](CHAP_Tasks.CustomizingTasks.md#CHAP_Tasks.CustomizingTasks.TaskSettings.Example "CHAP_Tasks.CustomizingTasks.md#CHAP_Tasks.CustomizingTasks.TaskSettings.Example").

## Replication task statistics

When data validation is enabled, AWS DMS provides the following statistics at
the table level:

- ValidationState—The
  validation state of the table. The parameter can have the following
  values:
  - Not enabled—Validation is not enabled for the table in
    the migration task.
  - Pending records—Some records in the table are waiting for
    validation.
  - Mismatched records—Some records in the table don't match
    between the source and target. A mismatch might occur for a number of
    reasons; For more information, check the
    `awsdms_control.awsdms_validation_failures_v1` table on the target
    endpoint.
  - Suspended records—Some records in the table can't be
    validated.
  - No primary key—The table can't be validated because it
    had no primary key.
  - Table error—The table wasn't validated because it was in
    an error state and some data wasn't migrated.
  - Validated—All rows in the table are validated. If the
    table is updated, the status can change from Validated.
  - Error—The table can't be validated because of an
    unexpected error.
  - Pending validation—The table is waiting validation.
  - Preparing table—Preparing the table enabled in the migration task for validation.
  - Pending revalidation—All rows in the table are pending validation after the table was updated.

- ValidationPending—The number of
  records that have been migrated to the target, but that haven't yet been
  validated.
- ValidationSuspended—The number of
  records that AWS DMS can't compare. For example, if a record at the source is
  constantly being updated, AWS DMS can't compare the source and the target.
- ValidationFailed—The number of
  records that didn't pass the data validation phase.

For an example of `ValidationSettings` task settings in a JSON file, see [Task settings example](CHAP_Tasks.CustomizingTasks.md#CHAP_Tasks.CustomizingTasks.TaskSettings.Example "CHAP_Tasks.CustomizingTasks.md#CHAP_Tasks.CustomizingTasks.TaskSettings.Example").

You can view the data validation information using the console, the AWS CLI,
or the AWS DMS API.

- On the console, you can choose to validate a task when you create or modify the task. To view
  the data validation report using the console, choose the task on the
  **Tasks** page and choose the **Table
  statistics** tab in the details section.
- Using the CLI, set the `EnableValidation` parameter to `true`
  when creating or modifying a task to begin data validation. The
  following example creates a task and enables data validation.

```
create-replication-task
  --replication-task-settings '{"ValidationSettings":{"EnableValidation":true}}'
  --replication-instance-arn arn:aws:dms:us-east-1:5731014:
     rep:36KWVMB7Q
  --source-endpoint-arn arn:aws:dms:us-east-1:5731014:
     endpoint:CSZAEFQURFYMM
  --target-endpoint-arn arn:aws:dms:us-east-1:5731014:
     endpoint:CGPP7MF6WT4JQ
  --migration-type full-load-and-cdc
  --table-mappings '{"rules": [{"rule-type": "selection", "rule-id": "1",
     "rule-name": "1", "object-locator": {"schema-name": "data_types", "table-name": "%"},
     "rule-action": "include"}]}'
```

Use the `describe-table-statistics` command to receive
the data validation report in JSON format. The following command
shows the data validation report.

```
aws dms  describe-table-statistics --replication-task-arn arn:aws:dms:us-east-1:5731014:
rep:36KWVMB7Q
```

The report would be similar to the following.

```
{
    "ReplicationTaskArn": "arn:aws:dms:us-west-2:5731014:task:VFPFTYKK2RYSI",
    "TableStatistics": [
        {
            "ValidationPendingRecords": 2,
            "Inserts": 25,
            "ValidationState": "Pending records",
            "ValidationSuspendedRecords": 0,
            "LastUpdateTime": 1510181065.349,
            "FullLoadErrorRows": 0,
            "FullLoadCondtnlChkFailedRows": 0,
            "Ddls": 0,
            "TableName": "t_binary",
            "ValidationFailedRecords": 0,
            "Updates": 0,
            "FullLoadRows": 10,
            "TableState": "Table completed",
            "SchemaName": "d_types_s_sqlserver",
            "Deletes": 0
        }
}

```

- Using the AWS DMS API, create a task using the **CreateReplicationTask**
  action and set the `EnableValidation` parameter to
  **true** to validate the data migrated by the
  task. Use the **DescribeTableStatistics** action to
  receive the data validation report in JSON format.

## Replication task statistics with Amazon CloudWatch

When Amazon CloudWatch is enabled, AWS DMS provides the following replication task
statistics:

- ValidationSucceededRecordCount— Number of
  rows that AWS DMS validated, per minute.
- ValidationAttemptedRecordCount— Number of
  rows that validation was attempted, per minute.
- ValidationFailedOverallCount— Number of
  rows where validation failed.
- ValidationSuspendedOverallCount— Number of
  rows where validation was suspended.
- ValidationPendingOverallCount— Number of
  rows where the validation is still pending.
- ValidationBulkQuerySourceLatency— AWS DMS
  can do data validation in bulk, especially in certain scenarios during a
  full-load or on-going replication when there are many changes. This metric
  indicates the latency required to read a bulk set of data from the source
  endpoint.
- ValidationBulkQueryTargetLatency— AWS DMS
  can do data validation in bulk, especially in certain scenarios during a
  full-load or on-going replication when there are many changes. This metric
  indicates the latency required to read a bulk set of data on the target
  endpoint.
- ValidationItemQuerySourceLatency— During
  on-going replication, data validation can identify on-going changes and validate
  those changes. This metric indicates the latency in reading those changes from
  the source. Validation can run more queries than required, based on number of
  changes, if there are errors during validation.
- ValidationItemQueryTargetLatency— During
  on-going replication, data validation can identify on-going changes and validate
  the changes row by row. This metric gives us the latency in reading those
  changes from the target. Validation may run more queries than required, based on
  number of changes, if there are errors during validation.

To collect data validation information from CloudWatch enabled statistics,
select **Enable CloudWatch logs** when you create or modify a task using the console.
Then, to view the data validation information and ensure that your data was migrated
accurately from source to target, do the following.

1. Choose the task on the **Database migration tasks** page.
2. Choose the **CloudWatch metrics** tab.
3. Select **Validation** from the drop down menu.

## Revalidating tables during a task

While a task is running, you can request AWS DMS to perform data validation.

### AWS Management Console

1. Sign in to the AWS Management Console and open the AWS DMS console at [https://console.aws.amazon.com/dms/v2/](https://console.aws.amazon.com/dms/v2/ "https://console.aws.amazon.com/dms/v2/").

If you're signed in as an AWS Identity and Access Management (IAM) user, make sure that you
have the appropriate permissions to access AWS DMS. the permissions required,
see [IAM permissions needed to use
AWS DMS](security-iam.md#CHAP_Security.IAMPermissions "security-iam.md#CHAP_Security.IAMPermissions"). 2. Choose **Tasks** from the navigation pane. 3. Choose the running task that has the table you want to revalidate. 4. Choose the **Table Statistics** tab. 5. Choose the table you want to revalidate (you can choose up to 10 tables at one time). If the task is no longer running, you
can't revalidate the table(s). 6. Choose **Revalidate**.

## Using JSON editor to modify validation rules

To add a validation rule to a task using the JSON editor from the AWS DMS Console, do
the following:

1. Select **Database migration tasks**.
2. Select your task from the list of migration tasks.
3. If your task is running, select **Stop** from the **Actions** drop down menu.
4. Once the task has stopped, to modify your task, select **Modify** from the **Actions** drop down menu.
5. In the **Table mappings** section, select **JSON editor** and add your
   validation rule to your table mappings.

For example, you can add the following validation rule to run a replace function on the source. In this case, if the
validation rule encounters a null byte, it validates it as a space.

```
{
	"rule-type": "validation",
	"rule-id": "1",
	"rule-name": "1",
	"rule-target": "column",
	"object-locator": {
		"schema-name": "Test-Schema",
		"table-name": "Test-Table",
		"column-name": "Test-Column"
	},
	"rule-action": "override-validation-function",
	"source-function": "REPLACE(${column-name}, chr(0), chr(32))",
	"target-function": "${column-name}"
}

```

###### Note

`override-validation-function` does not take effect if the column is a
part of the primary key.

## Validation only tasks

You can create validation only tasks to preview and validate data without performing
any migration or data replication. To create a validation only task, set the
`EnableValidation` and `ValidationOnly` settings to
`true`. When enabling `ValidationOnly`, additional
requirements apply. For more information, see [Data
validation task settings](CHAP_Tasks.CustomizingTasks.TaskSettings.md "CHAP_Tasks.CustomizingTasks.TaskSettings.md").

For a full load only migration type, a validation only task
completes much faster than its CDC equivalent when many failures are reported. But
changes to the source or target endpoint are reported as failures for full load mode, a
possible disadvantage.

A CDC validation only task delays validation based on average latency, and retries failures multiple times
before reporting them. If the majority of data comparisons result in failures, a validation only task for CDC mode
is very slow, a potential drawback.

A validation only task must be set up in the same direction as the replication task,
especially for CDC. This is because a CDC Validation Only task detects which rows have
changed and need to be revalidated based on the change log on the source. If the target
is specified as the source, then it only knows about changes sent to the target by DMS
and is not guaranteed to catch replication errors.

### Full load validation only

Beginning with AWS DMS version 3.4.6 and higher, a full load validation only task quickly compares all rows
from the source and target tables in a single pass, immediately reports any failures, and then shuts down.
Validation never is suspended due to failures in this mode, it is optimized for speed. But changes to the source
or target endpoint are reported as failures.

###### Note

Beginning with AWS DMS version 3.4.6 and higher, this validation behavior also
applies to full load migration task with validation enabled.

### CDC validation only

A CDC validation only task validates all existing rows between the source and
target tables on a fresh start. In addition, a CDC validation only task runs
continuously, re-validates ongoing replication changes, limits the number of
failures reported each pass, and retries mismatched rows before failing them. It is
optimized to prevent false positives.

Validation for a table (or the entire task) is suspended if the`FailureMaxCount` or `TableFailureMaxCount` thresholds are
breached. This also applies for a CDC or Full Load+CDC migration task with
validation enabled. And a CDC task with validation enabled delays re-validation for
each changed row based on average source and target latency.

But a CDC _validation only task_ doesn't
migrate data and has no latency. It sets `ValidationQueryCdcDelaySeconds`
to 180 by default. And you can increase the amount to account for high latency
environments and help prevent false positives.

### Validation only use cases

Use cases for splitting the data validation portion of a migration or replication task into a
separate _validation only task_ includes, but is not limited to, the following:

- _Control exactly when validation occurs_ — Validation queries add
  an additional load to both source and target endpoints. So, migrating or replicating data in one task first,
  then validating the results in another task can be beneficial.
- _Reduce load on the replication instance_ —
  Splitting data validation to run on its own instance can be
  advantageous.
- _Quickly obtain how many rows don't match at a given moment in time_ —
  For example, just before or during a maintenance window production cut–over to a target endpoint, you can create a Full Load
  validation only task to get an answer to your question.
- _When validation failures are expected for a migration task with
  a CDC component_ — For example, if migrating
  Oracle `varchar2` to PostgreSQL `jsonb`, CDC validation keeps
  retrying these failed rows and limits the number of failures reported each
  time. But, you can create a Full Load validation only task and obtain a
  quicker answer.
- _You've developed a data repair script/utility that reads
  the validation failure table_ — (See also, [Troubleshooting](#CHAP_Validating.Troubleshooting "#CHAP_Validating.Troubleshooting")). A Full Load
  validation only task quickly reports failures for the data repair script to
  act upon.

For an example of `ValidationSettings` task settings in a JSON file, see [Task settings example](CHAP_Tasks.CustomizingTasks.md#CHAP_Tasks.CustomizingTasks.TaskSettings.Example "CHAP_Tasks.CustomizingTasks.md#CHAP_Tasks.CustomizingTasks.TaskSettings.Example")).

## Troubleshooting

During validation, AWS DMS creates a new table at the target endpoint:
`awsdms_control.awsdms_validation_failures_v1`. If any record enters the
_ValidationSuspended_ or the
_ValidationFailed_ state, AWS DMS writes diagnostic
information to `awsdms_control.awsdms_validation_failures_v1`. You can query this table
to help troubleshoot validation errors.

For information about changing the default schema the table is created in on the target, see
[Control table task settings](CHAP_Tasks.CustomizingTasks.TaskSettings.md "CHAP_Tasks.CustomizingTasks.TaskSettings.md").

Following is a description of the `awsdms_control.awsdms_validation_failures_v1`
table:

| Column name    | Data type                | Description                                                                                                                 |
| -------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------------------- |
| `TASK_NAME`    | `VARCHAR(128) NOT NULL`  | AWS DMS task identifier.                                                                                                    |
| `TABLE_OWNER`  | `VARCHAR(128) NOT NULL`  | Schema (owner) of the table.                                                                                                |
| `TABLE_NAME`   | `VARCHAR(128) NOT NULL`  | Table name.                                                                                                                 |
| `FAILURE_TIME` | `DATETIME(3) NOT NULL`   | Time when the failure occurred.                                                                                             |
| `KEY_TYPE`     | `VARCHAR(128) NOT NULL`  | Reserved for future use (value is always 'Row')                                                                             |
| `KEY`          | `TEXT NOT NULL`          | This is the primary key for row record type.                                                                                |
| `FAILURE_TYPE` | `VARCHAR(128) NOT NULL`  | Severity of validation error. Can be either<br>`RECORD_DIFF`, `MISSING_SOURCE`,<br>`MISSING_TARGET`, or<br>`TABLE_WARNING`. |
| `DETAILS`      | `VARCHAR(8000) NOT NULL` | JSON formatted string of all source/target column values<br>which do not match for the given key.                           |

The following is a sample query for a MySQL target that will show you all the failures for a task by querying the
`awsdms_control.awsdms_validation_failures_v1` table. Note that the schema name and
query syntax will vary across target engine versions. The task name should be the
external resource ID of the task. The external resource ID of the task is the last value
in the task ARN. For example, for a task with an ARN value of
arn:aws:dms:us-west-2:5599:task: VFPFKH4FJR3FTYKK2RYSI, the external resource ID of the
task would be VFPFKH4FJR3FTYKK2RYSI.

```

select * from awsdms_validation_failures_v1 where TASK_NAME = 'VFPFKH4FJR3FTYKK2RYSI'

TASK_NAME       VFPFKH4FJR3FTYKK2RYSI
TABLE_OWNER     DB2PERF
TABLE_NAME      PERFTEST
FAILURE_TIME    2020-06-11 21:58:44
KEY_TYPE        Row
KEY             {"key":  ["3451491"]}
FAILURE_TYPE    RECORD_DIFF
DETAILS         [[{'MYREAL': '+1.10106036e-01'}, {'MYREAL': '+1.10106044e-01'}],]


```

You can look at the `DETAILS` field to determine which columns
don’t match. Since you have the primary key of the failed record, you can query the
source and target endpoints to see what part of the record does not match.

### `awsdms_validation_failures_v2` control table

During validation, in AWS DMS version 3.6.1 and above, DMS creates a new table at
the PostgreSQL target endpoint: `awsdms_validation_failures_v2`. This
tables consists of failures for all the DMS tasks that have data validation enabled.
When the `awsdms_validation_failures_v2` table is created, you should not
drop or truncate the table as it can cause errors for any tasks with validation and
resync enabled. `awsdms_validation_failures_v2` table has an
auto-increment primary key feature. This table consists of new columns to support
the Data resync feature. They are:

`**RESYNC\_RESULT**`

**Values**: `SUCCESS` or
`FAILURE`.

**`RESYNC_TIME`**

Timestamp with millisecond precision. Default value is
`NULL` if Data resync is not attempted for this
failure.

**`RESYNC_ACTION`**

**Values**: `UPSERT` or
`DELETE`.

`**RESYNC\_ID**`

Primary key column with auto-increment enabled.

In the `awsdms_validation_failures_v2` table, an index is added to the
`TASK_NAME`, `TABLE_OWNER`, `TABLE_NAME`,
`FAILURE_TYPE`, and `FAILURE_TIME` columns to efficiently
read failures for any given table in your target database. Below is an example
create statement to create an `awsdms_validation_failures_v2`
table:

```
CREATE TABLE public.awsdms_validation_failures_v2 (
    "RESYNC_ID" int8 GENERATED BY DEFAULT AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE) NOT NULL,
    "TASK_NAME" varchar(128) NOT NULL,
    "TABLE_OWNER" varchar(128) NOT NULL,
    "TABLE_NAME" varchar(128) NOT NULL,
    "FAILURE_TIME" timestamp NOT NULL,
    "KEY_TYPE" varchar(128) NOT NULL,
    "KEY" varchar(7800) NOT NULL,
    "FAILURE_TYPE" varchar(128) NOT NULL,
    "DETAILS" varchar(7000) NOT NULL,
    "RESYNC_RESULT" varchar(128) NULL,
    "RESYNC_TIME" timestamp NULL,
    "RESYNC_ACTION" varchar(128) NULL,
    CONSTRAINT awsdms_validation_failures_v2_pkey PRIMARY KEY ("RESYNC_ID")
);
```

## Redshift Validation Performance

Amazon Redshift differs from relational databases in several ways, including columnar storage,
MPP, data compression, and other factors. These differences give Redshift a different
performance profile from relational databases.

During the full-load replication phase, validation uses range queries, with the data
size governed by the `PartitionSize` setting.
These range-based queries select all the records from the source table.

For ongoing
replication, queries switch between range-based and individual-record fetches. The query type is
determined dynamically based on multiple factors, such as the following:

- Query volume
- Types of DML queries on the source table
- Task latency
- Total number of records
- Validation settings such as `PartitionSize`
  You may see additional load on your Amazon Redshift cluster due to validation queries.
  As the above factors vary across use cases, you must review your validation query performance and
  tune your cluster and table accordingly. Some options to mitigate performance isses include the following:

- Reduce the `PartitionSize` and `ThreadCount` settings to help reduce the
  workload during full-load validation. Note that this will slow down data validation.
- While Redshift doesn’t enforce primary keys, AWS DMS relies on primary keys to uniquely identify
  records on the target for data validation. If possible, set the primary key to mirror the sort key so that
  full load validation queries execute more quickly.

## Enhanced data validation for AWS Database Migration Service

AWS Database Migration Service has enhanced data validation performance for database migrations, enabling
customers to validate large datasets with significantly faster processing times. This
enhanced data validation is now available in version 3.5.4 of the replication engine for
both full load and full load with CDC migration tasks. Currently, this enhancement
supports migration paths from Oracle to PostgreSQL, SQL Server to PostgreSQL, Oracle to
Oracle, and SQL Server to SQL Server, with additional migration paths planned for future
releases.

### Prerequisites

- _Oracle:_ grant the `EXECUTE` permission on `SYS.DBMS_CRYPTO` to the user account that accesses the Oracle endpoint:

```
GRANT EXECUTE ON SYS.DBMS_CRYPTO TO dms_endpoint_user;
```

- Install the `pgcrypto` extension on the PostgreSQL database:

For self-managed PostgreSQL instances, you need to install the `contrib` module libraries and create the extension:

    + Install the `contrib` module libraries. For example, on an Amazon EC2 instance with Amazon Linux and PostgreSQL 15:



    ```
    sudo dnf install postgresql15-contrib
    ```
    + Create the `pgcrypto` extension:



    ```
    CREATE EXTENSION IF NOT EXISTS pgcrypto;
    ```

- For Amazon RDS for PostgreSQL instances, configure the SSL mode for the AWS DMS endpoint:
  - By default, Amazon RDS forces an SSL connection. When you create a AWS DMS endpoint for a Amazon RDS for PostgreSQL instance, use the "SSL mode" option = "required".
  - If you want to use the "SSL mode" option = "none", set the `rds.force_ssl` parameter to 0 in the RDS Parameter Group.

- For PostgreSQL 12 and 13, create the `BIT_XOR` aggregate:

```
CREATE OR REPLACE AGGREGATE BIT_XOR(IN v bit) (SFUNC = bitxor, STYPE = bit);
```

### Enhanced data validation

limitations

This enhanced data validation feature has the following limitations:

- Database endpoint requirements: This improvement is enabled only for database endpoints that meet the following criteria:
  - Use AWS Secrets Manager to store credentials.
  - For Microsoft SQL Server, Kerberos authentication is also supported.

- Database version support:
  - PostgreSQL 12 and higher
  - Oracle 12.1 and higher
  - For Microsoft SQL Server versions lower than 2019, validation of NCHAR and NVARCHAR data types is not supported.

## Limitations

- Data validation requires that the table has a primary key or unique
  index.
  - Primary key columns cannot be of type `CLOB`, `BLOB`,
    `BINARY`, or `BYTE`.
  - For primary key columns of type `VARCHAR` or
    `CHAR`, the length must be less than 1024. You must specify the length
    in the datatype. You can't use unbounded data types as a primary key for data validation.
  - An Oracle key created with the `NOVALIDATE` clause is _not_
    considered a primary key or unique index.
  - For an Oracle table with no primary key and only a unique key,
    the columns with the unique constraint must also have a `NOT NULL` constraint.

- Validation of NULL PK/UK values aren't supported.
- If the collation of the primary key column in the target PostgreSQL
  instance isn't set to "C", the sort order of the primary key is different
  compared to the sort order in Oracle. If the sort order is different between
  PostgreSQL and Oracle, data validation fails to validate the records.
- Data validation generates additional queries against the source and
  target databases. You must ensure that both databases have enough resources to
  handle this additional load. This is especially true for Redshift targets.
  For more information, see [Redshift Validation Performance](#CHAP_Validating.Redshift "#CHAP_Validating.Redshift") following.
- Data validation isn't supported when consolidating several databases into one.
- For a source or target Oracle endpoint, AWS DMS uses
  `DBMS_CRYPTO`. If you use data validation on Oracle endpoint you
  must grant the execute permission on `dbms_crypto` to the user
  account used to access the Oracle endpoint. You can do this by running the
  following statement

```
grant execute on sys.dbms_crypto to `dms_endpoint_user`;
```

- If the target database is modified outside of AWS DMS during validation,
  then discrepancies might not be reported accurately. This result can occur if
  one of your applications writes data to the target table, while AWS DMS is
  performing validation on that same table.
- If one or more rows are being continuously modified during
  validation, then AWS DMS can't validate those rows.
- If AWS DMS detects more than 10,000 failed or suspended records, it
  stops the validation. Before you proceed further, resolve any underlying problems
  with the data.
- AWS DMS doesn't support data validation of views.
- AWS DMS doesn't support data validation when character substitution task settings are used.
- AWS DMS doesn't support validating the Oracle LONG type.
- AWS DMS doesn't support validating the Oracle Spatial type during heterogeneous migration.
- Data validation ignores those columns in tables for which data masking transformations exists in table mapping.
- Data validation skips an entire table if there is a data masking transformation rule for its PK/UK column. The validation state will show as No primary key for such tables.
- Data validation does not work with Amazon Aurora PostgreSQL Limitless. When
  attempting to validate tables in a Limitless Database, the validation state
  displays "No primary key" for these tables.

For limitations when using S3 target validation, see [Limitations for using S3 target
validation](CHAP_Validating_S3.md#CHAP_Validating_S3_limitations "CHAP_Validating_S3.md#CHAP_Validating_S3_limitations").
