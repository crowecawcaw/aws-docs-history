# Column statistics API

The column statistics API describes AWS Glue APIs for returning
statistics on columns in a table.

## Data types

- [ColumnStatisticsTaskRun structure](#aws-glue-api-crawler-column-statistics-ColumnStatisticsTaskRun "#aws-glue-api-crawler-column-statistics-ColumnStatisticsTaskRun")
- [ColumnStatisticsTaskSettings structure](#aws-glue-api-crawler-column-statistics-ColumnStatisticsTaskSettings "#aws-glue-api-crawler-column-statistics-ColumnStatisticsTaskSettings")
- [ExecutionAttempt structure](#aws-glue-api-crawler-column-statistics-ExecutionAttempt "#aws-glue-api-crawler-column-statistics-ExecutionAttempt")

## ColumnStatisticsTaskRun structure

The object that shows the details of the column stats run.

###### Fields

- `CustomerId` – UTF-8 string, not more than 12 bytes long.

The AWS account ID.

- `ColumnStatisticsTaskRunId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The identifier for the particular column statistics task run.

- `DatabaseName` – UTF-8 string.

The database where the table resides.

- `TableName` – UTF-8 string.

The name of the table for which column statistics is generated.

- `ColumnNameList` – An array of UTF-8 strings.

A list of the column names. If none is supplied, all column names for the
table will be used by default.

- `CatalogID` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of the Data Catalog where the table resides. If none is supplied,
the AWS account ID is used by default.

- `Role` – UTF-8 string.

The IAM role that the service assumes to generate statistics.

- `SampleSize` – Number (double), not more than 100.

The percentage of rows used to generate statistics. If none is supplied,
the entire table will be used to generate stats.

- `SecurityConfiguration` – UTF-8 string, not more than 128 bytes long.

Name of the security configuration that is used to encrypt CloudWatch
logs for the column stats task run.

- `NumberOfWorkers` – Number (integer), at least 1.

The number of workers used to generate column statistics. The job is preconfigured
to autoscale up to 25 instances.

- `WorkerType` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The type of workers being used for generating stats. The default is `g.1x`.

- `ComputationType` – UTF-8 string (valid values: `FULL` | `INCREMENTAL`).

The type of column statistics computation.

- `Status` – UTF-8 string (valid values: `STARTING` | `RUNNING` | `SUCCEEDED` | `FAILED` | `STOPPED`).

The status of the task run.

- `CreationTime` – Timestamp.

The time that this task was created.

- `LastUpdated` – Timestamp.

The last point in time when this task was modified.

- `StartTime` – Timestamp.

The start time of the task.

- `EndTime` – Timestamp.

The end time of the task.

- `ErrorMessage` – Description string, not more than 2048 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

The error message for the job.

- `DPUSeconds` – Number (double), not more than None.

The calculated DPU usage in seconds for all autoscaled workers.

## ColumnStatisticsTaskSettings structure

The settings for a column statistics task.

###### Fields

- `DatabaseName` – UTF-8 string.

The name of the database where the table resides.

- `TableName` – UTF-8 string.

The name of the table for which to generate column statistics.

- `Schedule` – A [Schedule](aws-glue-api-crawler-scheduler.md#aws-glue-api-crawler-scheduler-Schedule "aws-glue-api-crawler-scheduler.md#aws-glue-api-crawler-scheduler-Schedule") object.

A schedule for running the column statistics, specified in CRON syntax.

- `ColumnNameList` – An array of UTF-8 strings.

A list of column names for which to run statistics.

- `CatalogID` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of the Data Catalog in which the database resides.

- `Role` – UTF-8 string.

The role used for running the column statistics.

- `SampleSize` – Number (double), not more than 100.

The percentage of data to sample.

- `SecurityConfiguration` – UTF-8 string, not more than 128 bytes long.

Name of the security configuration that is used to encrypt CloudWatch
logs.

- `ScheduleType` – UTF-8 string (valid values: `CRON` | `AUTO`).

The type of schedule for a column statistics task. Possible values may
be `CRON` or `AUTO`.

- `SettingSource` – UTF-8 string (valid values: `CATALOG` | `TABLE`).

The source of setting the column statistics task. Possible values may
be `CATALOG` or `TABLE`.

- `LastExecutionAttempt` – An [ExecutionAttempt](#aws-glue-api-crawler-column-statistics-ExecutionAttempt "#aws-glue-api-crawler-column-statistics-ExecutionAttempt") object.

The last `ExecutionAttempt` for the column statistics task
run.

## ExecutionAttempt structure

A run attempt for a column statistics task run.

###### Fields

- `Status` – UTF-8 string (valid values: `FAILED` | `STARTED`).

The status of the last column statistics task run.

- `ColumnStatisticsTaskRunId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

A task run ID for the last column statistics task run.

- `ExecutionTimestamp` – Timestamp.

A timestamp when the last column statistics task run occurred.

- `ErrorMessage` – Description string, not more than 2048 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

An error message associated with the last column statistics task run.

## Operations

- [StartColumnStatisticsTaskRun action (Python: start_column_statistics_task_run)](#aws-glue-api-crawler-column-statistics-StartColumnStatisticsTaskRun "#aws-glue-api-crawler-column-statistics-StartColumnStatisticsTaskRun")
- [GetColumnStatisticsTaskRun action (Python: get_column_statistics_task_run)](#aws-glue-api-crawler-column-statistics-GetColumnStatisticsTaskRun "#aws-glue-api-crawler-column-statistics-GetColumnStatisticsTaskRun")
- [GetColumnStatisticsTaskRuns action (Python: get_column_statistics_task_runs)](#aws-glue-api-crawler-column-statistics-GetColumnStatisticsTaskRuns "#aws-glue-api-crawler-column-statistics-GetColumnStatisticsTaskRuns")
- [ListColumnStatisticsTaskRuns action (Python: list_column_statistics_task_runs)](#aws-glue-api-crawler-column-statistics-ListColumnStatisticsTaskRuns "#aws-glue-api-crawler-column-statistics-ListColumnStatisticsTaskRuns")
- [StopColumnStatisticsTaskRun action (Python: stop_column_statistics_task_run)](#aws-glue-api-crawler-column-statistics-StopColumnStatisticsTaskRun "#aws-glue-api-crawler-column-statistics-StopColumnStatisticsTaskRun")
- [CreateColumnStatisticsTaskSettings action (Python: create_column_statistics_task_settings)](#aws-glue-api-crawler-column-statistics-CreateColumnStatisticsTaskSettings "#aws-glue-api-crawler-column-statistics-CreateColumnStatisticsTaskSettings")
- [UpdateColumnStatisticsTaskSettings action (Python: update_column_statistics_task_settings)](#aws-glue-api-crawler-column-statistics-UpdateColumnStatisticsTaskSettings "#aws-glue-api-crawler-column-statistics-UpdateColumnStatisticsTaskSettings")
- [GetColumnStatisticsTaskSettings action (Python: get_column_statistics_task_settings)](#aws-glue-api-crawler-column-statistics-GetColumnStatisticsTaskSettings "#aws-glue-api-crawler-column-statistics-GetColumnStatisticsTaskSettings")
- [DeleteColumnStatisticsTaskSettings action (Python: delete_column_statistics_task_settings)](#aws-glue-api-crawler-column-statistics-DeleteColumnStatisticsTaskSettings "#aws-glue-api-crawler-column-statistics-DeleteColumnStatisticsTaskSettings")
- [StartColumnStatisticsTaskRunSchedule action (Python: start_column_statistics_task_run_schedule)](#aws-glue-api-crawler-column-statistics-StartColumnStatisticsTaskRunSchedule "#aws-glue-api-crawler-column-statistics-StartColumnStatisticsTaskRunSchedule")
- [StopColumnStatisticsTaskRunSchedule action (Python: stop_column_statistics_task_run_schedule)](#aws-glue-api-crawler-column-statistics-StopColumnStatisticsTaskRunSchedule "#aws-glue-api-crawler-column-statistics-StopColumnStatisticsTaskRunSchedule")

## StartColumnStatisticsTaskRun action (Python: start_column_statistics_task_run)

Starts a column statistics task run, for a specified table and columns.

###### Request

- `DatabaseName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the database where the table resides.

- `TableName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the table to generate statistics.

- `ColumnNameList` – An array of UTF-8 strings.

A list of the column names to generate statistics. If none is supplied,
all column names for the table will be used by default.

- `Role` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The IAM role that the service assumes to generate statistics.

- `SampleSize` – Number (double), not more than 100.

The percentage of rows used to generate statistics. If none is supplied,
the entire table will be used to generate stats.

- `CatalogID` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of the Data Catalog where the table reside. If none is supplied, the
AWS account ID is used by default.

- `SecurityConfiguration` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Name of the security configuration that is used to encrypt CloudWatch
logs for the column stats task run.

###### Response

- `ColumnStatisticsTaskRunId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The identifier for the column statistics task run.

###### Errors

- `AccessDeniedException`
- `EntityNotFoundException`
- `ColumnStatisticsTaskRunningException`
- `OperationTimeoutException`
- `ResourceNumberLimitExceededException`
- `InvalidInputException`

## GetColumnStatisticsTaskRun action (Python: get_column_statistics_task_run)

Get the associated metadata/information for a task run, given a task run
ID.

###### Request

- `ColumnStatisticsTaskRunId` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The identifier for the particular column statistics task run.

###### Response

- `ColumnStatisticsTaskRun` – A [ColumnStatisticsTaskRun](#aws-glue-api-crawler-column-statistics-ColumnStatisticsTaskRun "#aws-glue-api-crawler-column-statistics-ColumnStatisticsTaskRun") object.

A `ColumnStatisticsTaskRun` object representing the details
of the column stats run.

###### Errors

- `EntityNotFoundException`
- `OperationTimeoutException`
- `InvalidInputException`

## GetColumnStatisticsTaskRuns action (Python: get_column_statistics_task_runs)

Retrieves information about all runs associated with the specified table.

###### Request

- `DatabaseName` – _Required:_ UTF-8 string.

The name of the database where the table resides.

- `TableName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the table.

- `MaxResults` – Number (integer), not less than 1 or more than 1000.

The maximum size of the response.

- `NextToken` – UTF-8 string.

A continuation token, if this is a continuation call.

###### Response

- `ColumnStatisticsTaskRuns` – An array of [ColumnStatisticsTaskRun](#aws-glue-api-crawler-column-statistics-ColumnStatisticsTaskRun "#aws-glue-api-crawler-column-statistics-ColumnStatisticsTaskRun") objects.

A list of column statistics task runs.

- `NextToken` – UTF-8 string.

A continuation token, if not all task runs have yet been returned.

###### Errors

- `OperationTimeoutException`

## ListColumnStatisticsTaskRuns action (Python: list_column_statistics_task_runs)

List all task runs for a particular account.

###### Request

- `MaxResults` – Number (integer), not less than 1 or more than 1000.

The maximum size of the response.

- `NextToken` – UTF-8 string.

A continuation token, if this is a continuation call.

###### Response

- `ColumnStatisticsTaskRunIds` – An array of UTF-8 strings, not more than 100 strings.

A list of column statistics task run IDs.

- `NextToken` – UTF-8 string.

A continuation token, if not all task run IDs have yet been returned.

###### Errors

- `OperationTimeoutException`

## StopColumnStatisticsTaskRun action (Python: stop_column_statistics_task_run)

Stops a task run for the specified table.

###### Request

- `DatabaseName` – _Required:_ UTF-8 string.

The name of the database where the table resides.

- `TableName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the table.

###### Response

- _No Response parameters._

###### Errors

- `EntityNotFoundException`
- `ColumnStatisticsTaskNotRunningException`
- `ColumnStatisticsTaskStoppingException`
- `OperationTimeoutException`

## CreateColumnStatisticsTaskSettings action (Python: create_column_statistics_task_settings)

Creates settings for a column statistics task.

###### Request

- `DatabaseName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the database where the table resides.

- `TableName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the table for which to generate column statistics.

- `Role` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The role used for running the column statistics.

- `Schedule` – UTF-8 string.

A schedule for running the column statistics, specified in CRON syntax.

- `ColumnNameList` – An array of UTF-8 strings.

A list of column names for which to run statistics.

- `SampleSize` – Number (double), not more than 100.

The percentage of data to sample.

- `CatalogID` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of the Data Catalog in which the database resides.

- `SecurityConfiguration` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Name of the security configuration that is used to encrypt CloudWatch
logs.

- `Tags` – A map array of key-value pairs, not more than 50 pairs.

Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

Each value is a UTF-8 string, not more than 256 bytes long.

A map of tags.

###### Response

- _No Response parameters._

###### Errors

- `AlreadyExistsException`
- `AccessDeniedException`
- `EntityNotFoundException`
- `InvalidInputException`
- `OperationTimeoutException`
- `ResourceNumberLimitExceededException`
- `ColumnStatisticsTaskRunningException`

## UpdateColumnStatisticsTaskSettings action (Python: update_column_statistics_task_settings)

Updates settings for a column statistics task.

###### Request

- `DatabaseName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the database where the table resides.

- `TableName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the table for which to generate column statistics.

- `Role` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The role used for running the column statistics.

- `Schedule` – UTF-8 string.

A schedule for running the column statistics, specified in CRON syntax.

- `ColumnNameList` – An array of UTF-8 strings.

A list of column names for which to run statistics.

- `SampleSize` – Number (double), not more than 100.

The percentage of data to sample.

- `CatalogID` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of the Data Catalog in which the database resides.

- `SecurityConfiguration` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Name of the security configuration that is used to encrypt CloudWatch
logs.

###### Response

- _No Response parameters._

###### Errors

- `AccessDeniedException`
- `EntityNotFoundException`
- `InvalidInputException`
- `VersionMismatchException`
- `OperationTimeoutException`

## GetColumnStatisticsTaskSettings action (Python: get_column_statistics_task_settings)

Gets settings for a column statistics task.

###### Request

- `DatabaseName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the database where the table resides.

- `TableName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the table for which to retrieve column statistics.

###### Response

- `ColumnStatisticsTaskSettings` – A [ColumnStatisticsTaskSettings](#aws-glue-api-crawler-column-statistics-ColumnStatisticsTaskSettings "#aws-glue-api-crawler-column-statistics-ColumnStatisticsTaskSettings") object.

A `ColumnStatisticsTaskSettings` object representing
the settings for the column statistics task.

###### Errors

- `EntityNotFoundException`
- `InvalidInputException`
- `OperationTimeoutException`

## DeleteColumnStatisticsTaskSettings action (Python: delete_column_statistics_task_settings)

Deletes settings for a column statistics task.

###### Request

- `DatabaseName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the database where the table resides.

- `TableName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the table for which to delete column statistics.

###### Response

- _No Response parameters._

###### Errors

- `EntityNotFoundException`
- `InvalidInputException`
- `OperationTimeoutException`

## StartColumnStatisticsTaskRunSchedule action (Python: start_column_statistics_task_run_schedule)

Starts a column statistics task run schedule.

###### Request

- `DatabaseName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the database where the table resides.

- `TableName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the table for which to start a column statistic task run schedule.

###### Response

- _No Response parameters._

###### Errors

- `AccessDeniedException`
- `EntityNotFoundException`
- `InvalidInputException`
- `OperationTimeoutException`

## StopColumnStatisticsTaskRunSchedule action (Python: stop_column_statistics_task_run_schedule)

Stops a column statistics task run schedule.

###### Request

- `DatabaseName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the database where the table resides.

- `TableName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the table for which to stop a column statistic task run schedule.

###### Response

- _No Response parameters._

###### Errors

- `EntityNotFoundException`
- `InvalidInputException`
- `OperationTimeoutException`

## Exceptions

- [ColumnStatisticsTaskRunningException structure](#aws-glue-api-crawler-column-statistics-ColumnStatisticsTaskRunningException "#aws-glue-api-crawler-column-statistics-ColumnStatisticsTaskRunningException")
- [ColumnStatisticsTaskNotRunningException structure](#aws-glue-api-crawler-column-statistics-ColumnStatisticsTaskNotRunningException "#aws-glue-api-crawler-column-statistics-ColumnStatisticsTaskNotRunningException")
- [ColumnStatisticsTaskStoppingException structure](#aws-glue-api-crawler-column-statistics-ColumnStatisticsTaskStoppingException "#aws-glue-api-crawler-column-statistics-ColumnStatisticsTaskStoppingException")
- [ColumnStatisticsTaskAutoConcurrencyLimitException structure](#aws-glue-api-crawler-column-statistics-ColumnStatisticsTaskAutoConcurrencyLimitException "#aws-glue-api-crawler-column-statistics-ColumnStatisticsTaskAutoConcurrencyLimitException")
- [InvalidCatalogSettingException structure](#aws-glue-api-crawler-column-statistics-InvalidCatalogSettingException "#aws-glue-api-crawler-column-statistics-InvalidCatalogSettingException")

## ColumnStatisticsTaskRunningException structure

An exception thrown when you try to start another job while running a column
stats generation job.

###### Fields

- `Message` – UTF-8 string.

A message describing the problem.

## ColumnStatisticsTaskNotRunningException structure

An exception thrown when you try to stop a task run when there is no task running.

###### Fields

- `Message` – UTF-8 string.

A message describing the problem.

## ColumnStatisticsTaskStoppingException structure

An exception thrown when you try to stop a task run.

###### Fields

- `Message` – UTF-8 string.

A message describing the problem.

## ColumnStatisticsTaskAutoConcurrencyLimitException structure

An exception thrown when you have already reached the limit of concurrent
auto statistics jobs.

###### Fields

- `Message` – UTF-8 string.

A message describing the problem.

## InvalidCatalogSettingException structure

An exception thrown when there is a problem with the catalog settings.

###### Fields

- `Message` – UTF-8 string.

A message describing the problem.
