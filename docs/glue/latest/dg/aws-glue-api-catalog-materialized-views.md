

# Materialized view API
<a name="aws-glue-api-catalog-materialized-views"></a>

The materialized view API describes the AWS Glue data types and operations for starting, stopping, and monitoring materialized view refresh task runs.

## Data types
<a name="aws-glue-api-catalog-materialized-views-objects"></a>
+ [MaterializedViewRefreshTaskRun structure](#aws-glue-api-catalog-materialized-views-MaterializedViewRefreshTaskRun)

## MaterializedViewRefreshTaskRun structure
<a name="aws-glue-api-catalog-materialized-views-MaterializedViewRefreshTaskRun"></a>

The object that shows the details of the materialized view refresh task run.

**Fields**
+ `CustomerId` – UTF-8 string, not more than 12 bytes long.

  The AWS account ID.
+ `MaterializedViewRefreshTaskRunId` – UTF-8 string, matching the [Custom string pattern #48](aws-glue-api-common.md#regex_48).

  The identifier of the materialized view refresh task run.
+ `DatabaseName` – UTF-8 string.

  The database where the table resides.
+ `TableName` – UTF-8 string.

  The name of the materialized view.
+ `CatalogId` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  The ID of the Data Catalog where the table resides. If none is supplied, the account ID is used by default.
+ `Role` – UTF-8 string.

  The IAM role that the service assumes to run the materialized view refresh task.
+ `Status` – UTF-8 string (valid values: `STARTING` \| `RUNNING` \| `SUCCEEDED` \| `FAILED` \| `STOPPED`).

  The status of the task run.
+ `CreationTime` – Timestamp.

  The time that this task was created.
+ `LastUpdated` – Timestamp.

  The last point in time when this task was modified.
+ `StartTime` – Timestamp.

  The start time of the task.
+ `EndTime` – Timestamp.

  The end time of the task.
+ `ErrorMessage` – Description string, not more than 2048 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri).

  The error message for the job.
+ `DPUSeconds` – Number (double).

  The calculated DPU usage in seconds for all autoscaled workers.
+ `RefreshType` – UTF-8 string (valid values: `FULL` \| `INCREMENTAL`).

  The type of the refresh task run. Either FULL or INCREMENTAL.
+ `ProcessedBytes` – Number (long).

  The number of bytes the refresh task run has scanned to refresh the materialized view.

## Operations
<a name="aws-glue-api-catalog-materialized-views-actions"></a>
+ [StartMaterializedViewRefreshTaskRun action (Python: start\_materialized\_view\_refresh\_task\_run)](#aws-glue-api-catalog-materialized-views-StartMaterializedViewRefreshTaskRun)
+ [StopMaterializedViewRefreshTaskRun action (Python: stop\_materialized\_view\_refresh\_task\_run)](#aws-glue-api-catalog-materialized-views-StopMaterializedViewRefreshTaskRun)
+ [GetMaterializedViewRefreshTaskRun action (Python: get\_materialized\_view\_refresh\_task\_run)](#aws-glue-api-catalog-materialized-views-GetMaterializedViewRefreshTaskRun)
+ [ListMaterializedViewRefreshTaskRuns action (Python: list\_materialized\_view\_refresh\_task\_runs)](#aws-glue-api-catalog-materialized-views-ListMaterializedViewRefreshTaskRuns)

## StartMaterializedViewRefreshTaskRun action (Python: start\_materialized\_view\_refresh\_task\_run)
<a name="aws-glue-api-catalog-materialized-views-StartMaterializedViewRefreshTaskRun"></a>

Starts a materialized view refresh task run for a specified materialized view.

**Request**
+ `CatalogId` – *Required:* UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  The ID of the Data Catalog where the table reside. If none is supplied, the account ID is used by default.
+ `DatabaseName` – *Required:* UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  The name of the database where the table resides.
+ `TableName` – *Required:* UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  The name of the materialized view to run the refresh task for.
+ `FullRefresh` – Boolean.

  Specifies whether this is a full refresh of the task run.

**Response**
+ `MaterializedViewRefreshTaskRunId` – UTF-8 string, matching the [Custom string pattern #48](aws-glue-api-common.md#regex_48).

  The identifier for the materialized view refresh task run.

**Errors**
+ `AccessDeniedException`
+ `EntityNotFoundException`
+ `MaterializedViewRefreshTaskRunningException`
+ `OperationTimeoutException`
+ `ResourceNumberLimitExceededException`
+ `InvalidInputException`

## StopMaterializedViewRefreshTaskRun action (Python: stop\_materialized\_view\_refresh\_task\_run)
<a name="aws-glue-api-catalog-materialized-views-StopMaterializedViewRefreshTaskRun"></a>

Stops a materialized view refresh task run for a specified materialized view.

**Request**
+ `CatalogId` – *Required:* UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  The ID of the Data Catalog where the table reside. If none is supplied, the account ID is used by default.
+ `DatabaseName` – *Required:* UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  The name of the database where the table resides.
+ `TableName` – *Required:* UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  The name of the materialized view.

**Response**
+ *No Response parameters.*

**Errors**
+ `AccessDeniedException`
+ `MaterializedViewRefreshTaskNotRunningException`
+ `MaterializedViewRefreshTaskStoppingException`
+ `InvalidInputException`
+ `OperationTimeoutException`

## GetMaterializedViewRefreshTaskRun action (Python: get\_materialized\_view\_refresh\_task\_run)
<a name="aws-glue-api-catalog-materialized-views-GetMaterializedViewRefreshTaskRun"></a>

Get the associated metadata/information for a task run, given a task run ID.

**Request**
+ `CatalogId` – *Required:* UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  The ID of the Data Catalog where the table resides. If none is supplied, the account ID is used by default.
+ `MaterializedViewRefreshTaskRunId` – *Required:* UTF-8 string, matching the [Custom string pattern #48](aws-glue-api-common.md#regex_48).

  The identifier for the particular materialized view refresh task run.

**Response**
+ `MaterializedViewRefreshTaskRun` – A [MaterializedViewRefreshTaskRun](#aws-glue-api-catalog-materialized-views-MaterializedViewRefreshTaskRun) object.

  A MaterializedViewRefreshTaskRun object representing the details of the task run.

**Errors**
+ `AccessDeniedException`
+ `EntityNotFoundException`
+ `OperationTimeoutException`
+ `InvalidInputException`

## ListMaterializedViewRefreshTaskRuns action (Python: list\_materialized\_view\_refresh\_task\_runs)
<a name="aws-glue-api-catalog-materialized-views-ListMaterializedViewRefreshTaskRuns"></a>

List all task runs for a particular account.

**Request**
+ `CatalogId` – *Required:* UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  The ID of the Data Catalog where the table resides. If none is supplied, the account ID is used by default.
+ `DatabaseName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  The database where the table resides.
+ `TableName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  The name of the materialized view.
+ `MaxResults` – Number (integer), not less than 1 or more than 1000.

  The maximum size of the response.
+ `NextToken` – UTF-8 string.

  A continuation token, if this is a continuation call.

**Response**
+ `MaterializedViewRefreshTaskRuns` – An array of [MaterializedViewRefreshTaskRun](#aws-glue-api-catalog-materialized-views-MaterializedViewRefreshTaskRun) objects.

  The results of the ListMaterializedViewRefreshTaskRuns action. 
+ `NextToken` – UTF-8 string.

  A continuation token, if not all task run IDs have yet been returned.

**Errors**
+ `AccessDeniedException`
+ `InvalidInputException`
+ `OperationTimeoutException`

## Exceptions
<a name="aws-glue-api-catalog-materialized-views-exceptions"></a>
+ [MaterializedViewRefreshTaskRunningException structure](#aws-glue-api-catalog-materialized-views-MaterializedViewRefreshTaskRunningException)
+ [MaterializedViewRefreshTaskNotRunningException structure](#aws-glue-api-catalog-materialized-views-MaterializedViewRefreshTaskNotRunningException)
+ [MaterializedViewRefreshTaskStoppingException structure](#aws-glue-api-catalog-materialized-views-MaterializedViewRefreshTaskStoppingException)

## MaterializedViewRefreshTaskRunningException structure
<a name="aws-glue-api-catalog-materialized-views-MaterializedViewRefreshTaskRunningException"></a>

Exception thrown when a task is already in running state.

**Fields**
+ `Message` – UTF-8 string.

  A message describing the problem.

## MaterializedViewRefreshTaskNotRunningException structure
<a name="aws-glue-api-catalog-materialized-views-MaterializedViewRefreshTaskNotRunningException"></a>

Exception thrown when stopping a task that is not in running state.

**Fields**
+ `Message` – UTF-8 string.

  A message describing the problem.

## MaterializedViewRefreshTaskStoppingException structure
<a name="aws-glue-api-catalog-materialized-views-MaterializedViewRefreshTaskStoppingException"></a>

Exception thrown when a task is already in stopping state.

**Fields**
+ `Message` – UTF-8 string.

  A message describing the problem.