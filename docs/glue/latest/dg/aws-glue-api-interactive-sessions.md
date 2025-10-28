# Interactive sessions API

The interactive sessions API describes the AWS Glue API related
to using AWS Glue interactive sessions to build and test extract,
transform, and load (ETL) scripts for data integration.

## Data types

- [Session structure](#aws-glue-api-interactive-sessions-Session "#aws-glue-api-interactive-sessions-Session")
- [SessionCommand structure](#aws-glue-api-interactive-sessions-SessionCommand "#aws-glue-api-interactive-sessions-SessionCommand")
- [Statement structure](#aws-glue-api-interactive-sessions-Statement "#aws-glue-api-interactive-sessions-Statement")
- [StatementOutput structure](#aws-glue-api-interactive-sessions-StatementOutput "#aws-glue-api-interactive-sessions-StatementOutput")
- [StatementOutputData structure](#aws-glue-api-interactive-sessions-StatementOutputData "#aws-glue-api-interactive-sessions-StatementOutputData")
- [ConnectionsList structure](#aws-glue-api-interactive-sessions-ConnectionsList "#aws-glue-api-interactive-sessions-ConnectionsList")

## Session structure

The period in which a remote Spark runtime environment is running.

###### Fields

- `Id` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of the session.

- `CreatedOn` – Timestamp.

The time and date when the session was created.

- `Status` – UTF-8 string (valid values: `PROVISIONING` | `READY` | `FAILED` | `TIMEOUT` | `STOPPING` | `STOPPED`).

The session status.

- `ErrorMessage` – Description string, not more than 2048 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

The error message displayed during the session.

- `Description` – Description string, not more than 2048 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

The description of the session.

- `Role` – UTF-8 string, not less than 20 or more than 2048 bytes long, matching the [Custom string pattern #30](aws-glue-api-common.md#regex_30 "aws-glue-api-common.md#regex_30").

The name or Amazon Resource Name (ARN) of the IAM role associated with the
Session.

- `Command` – A [SessionCommand](#aws-glue-api-interactive-sessions-SessionCommand "#aws-glue-api-interactive-sessions-SessionCommand") object.

The command object.See SessionCommand.

- `DefaultArguments` – A map array of key-value pairs, not more than 75 pairs.

Each key is a UTF-8 string, not less than 1 or more than 128 bytes long, matching the [Custom string pattern #31](aws-glue-api-common.md#regex_31 "aws-glue-api-common.md#regex_31").

Each value is a UTF-8 string, not more than 4096 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

A map array of key-value pairs. Max is 75 pairs.

- `Connections` – A [ConnectionsList](#aws-glue-api-interactive-sessions-ConnectionsList "#aws-glue-api-interactive-sessions-ConnectionsList") object.

The number of connections used for the session.

- `Progress` – Number (double).

The code execution progress of the session.

- `MaxCapacity` – Number (double).

The number of AWS Glue data processing units (DPUs) that can
be allocated when the job runs. A DPU is a relative measure of processing power
that consists of 4 vCPUs of compute capacity and 16 GB memory.

- `SecurityConfiguration` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the SecurityConfiguration structure to be used with the session.

- `GlueVersion` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Custom string pattern #48](aws-glue-api-common.md#regex_48 "aws-glue-api-common.md#regex_48").

The AWS Glue version determines the versions of Apache Spark
and Python that AWS Glue supports. The GlueVersion must be greater
than 2.0.

- `DataAccessId` – UTF-8 string, not less than 1 or more than 36 bytes long.

The data access ID of the session.

- `PartitionId` – UTF-8 string, not less than 1 or more than 36 bytes long.

The partition ID of the sesion.

- `NumberOfWorkers` – Number (integer).

The number of workers of a defined `WorkerType` to use for
the session.

- `WorkerType` – UTF-8 string (valid values: `Standard=""` | `G.1X=""` | `G.2X=""` | `G.025X=""` | `G.4X=""` | `G.8X=""` | `Z.2X=""`).

The type of predefined worker that is allocated when a session runs. Accepts
a value of `G.1X`, `G.2X`, `G.4X`, or `G.8X`
for Spark sessions. Accepts the value `Z.2X` for Ray sessions.

- `CompletedOn` – Timestamp.

The date and time that this session is completed.

- `ExecutionTime` – Number (double).

The total time the session ran for.

- `DPUSeconds` – Number (double).

The DPUs consumed by the session (formula: ExecutionTime \* MaxCapacity).

- `IdleTimeout` – Number (integer).

The number of minutes when idle before the session times out.

- `ProfileName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of an AWS Glue usage profile associated with the session.

## SessionCommand structure

The `SessionCommand` that runs the job.

###### Fields

- `Name` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Specifies the name of the SessionCommand. Can be 'glueetl' or 'gluestreaming'.

- `PythonVersion` – UTF-8 string, matching the [Custom string pattern #49](aws-glue-api-common.md#regex_49 "aws-glue-api-common.md#regex_49").

Specifies the Python version. The Python version indicates the version
supported for jobs of type Spark.

## Statement structure

The statement or request for a particular action to occur in a session.

###### Fields

- `Id` – Number (integer).

The ID of the statement.

- `Code` – UTF-8 string.

The execution code of the statement.

- `State` – UTF-8 string (valid values: `WAITING` | `RUNNING` | `AVAILABLE` | `CANCELLING` | `CANCELLED` | `ERROR`).

The state while request is actioned.

- `Output` – A [StatementOutput](#aws-glue-api-interactive-sessions-StatementOutput "#aws-glue-api-interactive-sessions-StatementOutput") object.

The output in JSON.

- `Progress` – Number (double).

The code execution progress.

- `StartedOn` – Number (long).

The unix time and date that the job definition was started.

- `CompletedOn` – Number (long).

The unix time and date that the job definition was completed.

## StatementOutput structure

The code execution output in JSON format.

###### Fields

- `Data` – A [StatementOutputData](#aws-glue-api-interactive-sessions-StatementOutputData "#aws-glue-api-interactive-sessions-StatementOutputData") object.

The code execution output.

- `ExecutionCount` – Number (integer).

The execution count of the output.

- `Status` – UTF-8 string (valid values: `WAITING` | `RUNNING` | `AVAILABLE` | `CANCELLING` | `CANCELLED` | `ERROR`).

The status of the code execution output.

- `ErrorName` – UTF-8 string.

The name of the error in the output.

- `ErrorValue` – UTF-8 string.

The error value of the output.

- `Traceback` – An array of UTF-8 strings.

The traceback of the output.

## StatementOutputData structure

The code execution output in JSON format.

###### Fields

- `TextPlain` – UTF-8 string.

The code execution output in text format.

## ConnectionsList structure

Specifies the connections used by a job.

###### Fields

- `Connections` – An array of UTF-8 strings, not more than 1000 strings.

A list of connections used by the job.

## Operations

- [CreateSession action (Python: create_session)](#aws-glue-api-interactive-sessions-CreateSession "#aws-glue-api-interactive-sessions-CreateSession")
- [StopSession action (Python: stop_session)](#aws-glue-api-interactive-sessions-StopSession "#aws-glue-api-interactive-sessions-StopSession")
- [DeleteSession action (Python: delete_session)](#aws-glue-api-interactive-sessions-DeleteSession "#aws-glue-api-interactive-sessions-DeleteSession")
- [GetSession action (Python: get_session)](#aws-glue-api-interactive-sessions-GetSession "#aws-glue-api-interactive-sessions-GetSession")
- [ListSessions action (Python: list_sessions)](#aws-glue-api-interactive-sessions-ListSessions "#aws-glue-api-interactive-sessions-ListSessions")
- [RunStatement action (Python: run_statement)](#aws-glue-api-interactive-sessions-RunStatement "#aws-glue-api-interactive-sessions-RunStatement")
- [CancelStatement action (Python: cancel_statement)](#aws-glue-api-interactive-sessions-CancelStatement "#aws-glue-api-interactive-sessions-CancelStatement")
- [GetStatement action (Python: get_statement)](#aws-glue-api-interactive-sessions-GetStatement "#aws-glue-api-interactive-sessions-GetStatement")
- [ListStatements action (Python: list_statements)](#aws-glue-api-interactive-sessions-ListStatements "#aws-glue-api-interactive-sessions-ListStatements")
- [GetGlueIdentityCenterConfiguration action (Python: get_glue_identity_center_configuration)](#aws-glue-api-interactive-sessions-GetGlueIdentityCenterConfiguration "#aws-glue-api-interactive-sessions-GetGlueIdentityCenterConfiguration")
- [UpdateGlueIdentityCenterConfiguration action (Python: update_glue_identity_center_configuration)](#aws-glue-api-interactive-sessions-UpdateGlueIdentityCenterConfiguration "#aws-glue-api-interactive-sessions-UpdateGlueIdentityCenterConfiguration")
- [CreateGlueIdentityCenterConfiguration action (Python: create_glue_identity_center_configuration)](#aws-glue-api-interactive-sessions-CreateGlueIdentityCenterConfiguration "#aws-glue-api-interactive-sessions-CreateGlueIdentityCenterConfiguration")
- [DeleteGlueIdentityCenterConfiguration action (Python: delete_glue_identity_center_configuration)](#aws-glue-api-interactive-sessions-DeleteGlueIdentityCenterConfiguration "#aws-glue-api-interactive-sessions-DeleteGlueIdentityCenterConfiguration")

## CreateSession action (Python: create_session)

Creates a new session.

###### Request

Request to create a new session.

- `Id` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of the session request.

- `Description` – Description string, not more than 2048 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

The description of the session.

- `Role` – _Required:_ UTF-8 string, not less than 20 or more than 2048 bytes long, matching the [Custom string pattern #30](aws-glue-api-common.md#regex_30 "aws-glue-api-common.md#regex_30").

The IAM Role ARN

- `Command` – _Required:_ A [SessionCommand](#aws-glue-api-interactive-sessions-SessionCommand "#aws-glue-api-interactive-sessions-SessionCommand") object.

The `SessionCommand` that runs the job.

- `Timeout` – Number (integer), at least 1.

The number of minutes before session times out. Default for Spark ETL jobs
is 48 hours (2880 minutes). Consult the documentation for other job types.

- `IdleTimeout` – Number (integer), at least 1.

The number of minutes when idle before session times out. Default for Spark
ETL jobs is value of Timeout. Consult the documentation for other job types.

- `DefaultArguments` – A map array of key-value pairs, not more than 75 pairs.

Each key is a UTF-8 string, not less than 1 or more than 128 bytes long, matching the [Custom string pattern #31](aws-glue-api-common.md#regex_31 "aws-glue-api-common.md#regex_31").

Each value is a UTF-8 string, not more than 4096 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

A map array of key-value pairs. Max is 75 pairs.

- `Connections` – A [ConnectionsList](#aws-glue-api-interactive-sessions-ConnectionsList "#aws-glue-api-interactive-sessions-ConnectionsList") object.

The number of connections to use for the session.

- `MaxCapacity` – Number (double).

The number of AWS Glue data processing units (DPUs) that can
be allocated when the job runs. A DPU is a relative measure of processing power
that consists of 4 vCPUs of compute capacity and 16 GB memory.

- `NumberOfWorkers` – Number (integer).

The number of workers of a defined `WorkerType` to use for
the session.

- `WorkerType` – UTF-8 string (valid values: `Standard=""` | `G.1X=""` | `G.2X=""` | `G.025X=""` | `G.4X=""` | `G.8X=""` | `Z.2X=""`).

The type of predefined worker that is allocated when a job runs. Accepts
a value of G.1X, G.2X, G.4X, or G.8X for Spark jobs. Accepts the value Z.2X for Ray
notebooks.

    + For the `G.1X` worker type, each worker maps to 1 DPU (4 vCPUs,
     16 GB of memory) with 94GB disk, and provides 1 executor per worker. We recommend
     this worker type for workloads such as data transforms, joins, and queries, to
     offers a scalable and cost effective way to run most jobs.
    + For the `G.2X` worker type, each worker maps to 2 DPU (8 vCPUs,
     32 GB of memory) with 138GB disk, and provides 1 executor per worker. We recommend
     this worker type for workloads such as data transforms, joins, and queries, to
     offers a scalable and cost effective way to run most jobs.
    + For the `G.4X` worker type, each worker maps to 4 DPU (16 vCPUs,
     64 GB of memory) with 256GB disk, and provides 1 executor per worker. We recommend
     this worker type for jobs whose workloads contain your most demanding transforms,
     aggregations, joins, and queries. This worker type is available only for AWS Glue version 3.0 or later Spark ETL jobs in the following AWS Regions: US East (Ohio), US East (N. Virginia), US West (Oregon), Asia Pacific
     (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo), Canada (Central),
     Europe (Frankfurt), Europe (Ireland), and Europe (Stockholm).
    + For the `G.8X` worker type, each worker maps to 8 DPU (32 vCPUs,
     128 GB of memory) with 512GB disk, and provides 1 executor per worker. We recommend
     this worker type for jobs whose workloads contain your most demanding transforms,
     aggregations, joins, and queries. This worker type is available only for AWS Glue version 3.0 or later Spark ETL jobs, in the same AWS
     Regions as supported for the `G.4X` worker type.
    + For the `Z.2X` worker type, each worker maps to 2 M-DPU (8vCPUs,
     64 GB of memory) with 128 GB disk, and provides up to 8 Ray workers based on the autoscaler.

- `SecurityConfiguration` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the SecurityConfiguration structure to be used with the session

- `GlueVersion` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Custom string pattern #48](aws-glue-api-common.md#regex_48 "aws-glue-api-common.md#regex_48").

The AWS Glue version determines the versions of Apache Spark
and Python that AWS Glue supports. The GlueVersion must be greater
than 2.0.

- `DataAccessId` – UTF-8 string, not less than 1 or more than 36 bytes long.

The data access ID of the session.

- `PartitionId` – UTF-8 string, not less than 1 or more than 36 bytes long.

The partition ID of the session.

- `Tags` – A map array of key-value pairs, not more than 50 pairs.

Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

Each value is a UTF-8 string, not more than 256 bytes long.

The map of key value pairs (tags) belonging to the session.

- `RequestOrigin` – UTF-8 string, not less than 1 or more than 128 bytes long, matching the [Custom string pattern #31](aws-glue-api-common.md#regex_31 "aws-glue-api-common.md#regex_31").

The origin of the request.

- `ProfileName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of an AWS Glue usage profile associated with the session.

###### Response

- `Session` – A [Session](#aws-glue-api-interactive-sessions-Session "#aws-glue-api-interactive-sessions-Session") object.

Returns the session object in the response.

###### Errors

- `AccessDeniedException`
- `IdempotentParameterMismatchException`
- `InternalServiceException`
- `OperationTimeoutException`
- `InvalidInputException`
- `ValidationException`
- `AlreadyExistsException`
- `ResourceNumberLimitExceededException`

## StopSession action (Python: stop_session)

Stops the session.

###### Request

- `Id` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of the session to be stopped.

- `RequestOrigin` – UTF-8 string, not less than 1 or more than 128 bytes long, matching the [Custom string pattern #31](aws-glue-api-common.md#regex_31 "aws-glue-api-common.md#regex_31").

The origin of the request.

###### Response

- `Id` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Returns the Id of the stopped session.

###### Errors

- `AccessDeniedException`
- `InternalServiceException`
- `OperationTimeoutException`
- `InvalidInputException`
- `IllegalSessionStateException`
- `ConcurrentModificationException`

## DeleteSession action (Python: delete_session)

Deletes the session.

###### Request

- `Id` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of the session to be deleted.

- `RequestOrigin` – UTF-8 string, not less than 1 or more than 128 bytes long, matching the [Custom string pattern #31](aws-glue-api-common.md#regex_31 "aws-glue-api-common.md#regex_31").

The name of the origin of the delete session request.

###### Response

- `Id` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Returns the ID of the deleted session.

###### Errors

- `AccessDeniedException`
- `InternalServiceException`
- `OperationTimeoutException`
- `InvalidInputException`
- `IllegalSessionStateException`
- `ConcurrentModificationException`

## GetSession action (Python: get_session)

Retrieves the session.

###### Request

- `Id` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of the session.

- `RequestOrigin` – UTF-8 string, not less than 1 or more than 128 bytes long, matching the [Custom string pattern #31](aws-glue-api-common.md#regex_31 "aws-glue-api-common.md#regex_31").

The origin of the request.

###### Response

- `Session` – A [Session](#aws-glue-api-interactive-sessions-Session "#aws-glue-api-interactive-sessions-Session") object.

The session object is returned in the response.

###### Errors

- `AccessDeniedException`
- `EntityNotFoundException`
- `InternalServiceException`
- `OperationTimeoutException`
- `InvalidInputException`

## ListSessions action (Python: list_sessions)

Retrieve a list of sessions.

###### Request

- `NextToken` – UTF-8 string, not more than 400000 bytes long.

The token for the next set of results, or null if there are no more result.

- `MaxResults` – Number (integer), not less than 1 or more than 1000.

The maximum number of results.

- `Tags` – A map array of key-value pairs, not more than 50 pairs.

Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

Each value is a UTF-8 string, not more than 256 bytes long.

Tags belonging to the session.

- `RequestOrigin` – UTF-8 string, not less than 1 or more than 128 bytes long, matching the [Custom string pattern #31](aws-glue-api-common.md#regex_31 "aws-glue-api-common.md#regex_31").

The origin of the request.

###### Response

- `Ids` – An array of UTF-8 strings.

Returns the ID of the session.

- `Sessions` – An array of [Session](#aws-glue-api-interactive-sessions-Session "#aws-glue-api-interactive-sessions-Session") objects.

Returns the session object.

- `NextToken` – UTF-8 string, not more than 400000 bytes long.

The token for the next set of results, or null if there are no more result.

###### Errors

- `AccessDeniedException`
- `InvalidInputException`
- `InternalServiceException`
- `OperationTimeoutException`

## RunStatement action (Python: run_statement)

Executes the statement.

###### Request

- `SessionId` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The Session Id of the statement to be run.

- `Code` – _Required:_ UTF-8 string, not more than 68000 bytes long.

The statement code to be run.

- `RequestOrigin` – UTF-8 string, not less than 1 or more than 128 bytes long, matching the [Custom string pattern #31](aws-glue-api-common.md#regex_31 "aws-glue-api-common.md#regex_31").

The origin of the request.

###### Response

- `Id` – Number (integer).

Returns the Id of the statement that was run.

###### Errors

- `EntityNotFoundException`
- `AccessDeniedException`
- `InternalServiceException`
- `OperationTimeoutException`
- `InvalidInputException`
- `ValidationException`
- `ResourceNumberLimitExceededException`
- `IllegalSessionStateException`

## CancelStatement action (Python: cancel_statement)

Cancels the statement.

###### Request

- `SessionId` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The Session ID of the statement to be cancelled.

- `Id` – _Required:_ Number (integer).

The ID of the statement to be cancelled.

- `RequestOrigin` – UTF-8 string, not less than 1 or more than 128 bytes long, matching the [Custom string pattern #31](aws-glue-api-common.md#regex_31 "aws-glue-api-common.md#regex_31").

The origin of the request to cancel the statement.

###### Response

- _No Response parameters._

###### Errors

- `AccessDeniedException`
- `EntityNotFoundException`
- `InternalServiceException`
- `OperationTimeoutException`
- `InvalidInputException`
- `IllegalSessionStateException`

## GetStatement action (Python: get_statement)

Retrieves the statement.

###### Request

- `SessionId` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The Session ID of the statement.

- `Id` – _Required:_ Number (integer).

The Id of the statement.

- `RequestOrigin` – UTF-8 string, not less than 1 or more than 128 bytes long, matching the [Custom string pattern #31](aws-glue-api-common.md#regex_31 "aws-glue-api-common.md#regex_31").

The origin of the request.

###### Response

- `Statement` – A [Statement](#aws-glue-api-interactive-sessions-Statement "#aws-glue-api-interactive-sessions-Statement") object.

Returns the statement.

###### Errors

- `AccessDeniedException`
- `EntityNotFoundException`
- `InternalServiceException`
- `OperationTimeoutException`
- `InvalidInputException`
- `IllegalSessionStateException`

## ListStatements action (Python: list_statements)

Lists statements for the session.

###### Request

- `SessionId` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The Session ID of the statements.

- `RequestOrigin` – UTF-8 string, not less than 1 or more than 128 bytes long, matching the [Custom string pattern #31](aws-glue-api-common.md#regex_31 "aws-glue-api-common.md#regex_31").

The origin of the request to list statements.

- `NextToken` – UTF-8 string, not more than 400000 bytes long.

A continuation token, if this is a continuation call.

###### Response

- `Statements` – An array of [Statement](#aws-glue-api-interactive-sessions-Statement "#aws-glue-api-interactive-sessions-Statement") objects.

Returns the list of statements.

- `NextToken` – UTF-8 string, not more than 400000 bytes long.

A continuation token, if not all statements have yet been returned.

###### Errors

- `AccessDeniedException`
- `EntityNotFoundException`
- `InternalServiceException`
- `OperationTimeoutException`
- `InvalidInputException`
- `IllegalSessionStateException`

## GetGlueIdentityCenterConfiguration action (Python: get_glue_identity_center_configuration)

Retrieves the current AWS Glue Identity Center configuration
details, including the associated Identity Center instance and application
information.

###### Request

- _No Request parameters._

###### Response

Response containing the AWS Glue Identity Center configuration
details.

- `ApplicationArn` – UTF-8 string, not less than 10 or more than 1224 bytes long.

The Amazon Resource Name (ARN) of the Identity Center application associated
with the AWS Glue configuration.

- `InstanceArn` – UTF-8 string, not less than 10 or more than 1224 bytes long.

The Amazon Resource Name (ARN) of the Identity Center instance associated
with the AWS Glue configuration.

- `Scopes` – An array of UTF-8 strings.

A list of Identity Center scopes that define the permissions and access
levels for the AWS Glue configuration.

###### Errors

- `InvalidInputException`
- `EntityNotFoundException`
- `InternalServiceException`
- `OperationTimeoutException`
- `AccessDeniedException`
- `ConcurrentModificationException`

## UpdateGlueIdentityCenterConfiguration action (Python: update_glue_identity_center_configuration)

Updates the existing AWS Glue Identity Center configuration,
allowing modification of scopes and permissions for the integration.

###### Request

Request to update an existing AWS Glue Identity Center configuration.

- `Scopes` – An array of UTF-8 strings, not less than 1 or more than 50 strings.

A list of Identity Center scopes that define the updated permissions and
access levels for the AWS Glue configuration.

###### Response

- _No Response parameters._

###### Errors

- `InvalidInputException`
- `EntityNotFoundException`
- `InternalServiceException`
- `OperationTimeoutException`
- `AccessDeniedException`
- `ConcurrentModificationException`

## CreateGlueIdentityCenterConfiguration action (Python: create_glue_identity_center_configuration)

Creates a new AWS Glue Identity Center configuration to enable
integration between AWS Glue and AWS IAM Identity
Center for authentication and authorization.

###### Request

Request to create a new AWS Glue Identity Center configuration.

- `InstanceArn` – _Required:_ UTF-8 string, not less than 10 or more than 1224 bytes long.

The Amazon Resource Name (ARN) of the Identity Center instance to be associated
with the AWS Glue configuration.

- `Scopes` – An array of UTF-8 strings, not less than 1 or more than 50 strings.

A list of Identity Center scopes that define the permissions and access
levels for the AWS Glue configuration.

###### Response

Response from creating a new AWS Glue Identity Center configuration.

- `ApplicationArn` – UTF-8 string, not less than 10 or more than 1224 bytes long.

The Amazon Resource Name (ARN) of the Identity Center application that
was created for the AWS Glue configuration.

###### Errors

- `InvalidInputException`
- `AlreadyExistsException`
- `InternalServiceException`
- `OperationTimeoutException`
- `AccessDeniedException`
- `ConcurrentModificationException`

## DeleteGlueIdentityCenterConfiguration action (Python: delete_glue_identity_center_configuration)

Deletes the existing AWS Glue Identity Center configuration,
removing the integration between AWS Glue and AWS
IAM Identity Center.

###### Request

- _No Request parameters._

###### Response

- _No Response parameters._

###### Errors

- `InvalidInputException`
- `EntityNotFoundException`
- `InternalServiceException`
- `OperationTimeoutException`
- `AccessDeniedException`
- `ConcurrentModificationException`
