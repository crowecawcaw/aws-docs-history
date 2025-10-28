# Triggers

The Triggers API describes the data types and API related to creating,
updating, or deleting, and starting and stopping job triggers in AWS Glue.

## Data types

- [Trigger structure](#aws-glue-api-jobs-trigger-Trigger "#aws-glue-api-jobs-trigger-Trigger")
- [TriggerUpdate structure](#aws-glue-api-jobs-trigger-TriggerUpdate "#aws-glue-api-jobs-trigger-TriggerUpdate")
- [Predicate structure](#aws-glue-api-jobs-trigger-Predicate "#aws-glue-api-jobs-trigger-Predicate")
- [Condition structure](#aws-glue-api-jobs-trigger-Condition "#aws-glue-api-jobs-trigger-Condition")
- [Action structure](#aws-glue-api-jobs-trigger-Action "#aws-glue-api-jobs-trigger-Action")
- [EventBatchingCondition structure](#aws-glue-api-jobs-trigger-EventBatchingCondition "#aws-glue-api-jobs-trigger-EventBatchingCondition")

## Trigger structure

Information about a specific trigger.

###### Fields

- `Name` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the trigger.

- `WorkflowName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the workflow associated with the trigger.

- `Id` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Reserved for future use.

- `Type` – UTF-8 string (valid values: `SCHEDULED` | `CONDITIONAL` | `ON_DEMAND` | `EVENT`).

The type of trigger that this is.

- `State` – UTF-8 string (valid values: `CREATING` | `CREATED` | `ACTIVATING` | `ACTIVATED` | `DEACTIVATING` | `DEACTIVATED` | `DELETING` | `UPDATING`).

The current state of the trigger.

- `Description` – Description string, not more than 2048 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

A description of this trigger.

- `Schedule` – UTF-8 string.

A `cron` expression used to specify the schedule (see [Time-Based
Schedules for Jobs and Crawlers](monitor-data-warehouse-schedule.md "monitor-data-warehouse-schedule.md"). For example, to run something every
day at 12:15 UTC, you would specify: `cron(15 12 * * ? *)`.

- `Actions` – An array of [Action](#aws-glue-api-jobs-trigger-Action "#aws-glue-api-jobs-trigger-Action") objects.

The actions initiated by this trigger.

- `Predicate` – A [Predicate](#aws-glue-api-jobs-trigger-Predicate "#aws-glue-api-jobs-trigger-Predicate") object.

The predicate of this trigger, which defines when it will fire.

- `EventBatchingCondition` – An [EventBatchingCondition](#aws-glue-api-jobs-trigger-EventBatchingCondition "#aws-glue-api-jobs-trigger-EventBatchingCondition") object.

Batch condition that must be met (specified number of events received
or batch time window expired) before EventBridge event trigger fires.

## TriggerUpdate structure

A structure used to provide information used to update a trigger. This
object updates the previous trigger definition by overwriting it completely.

###### Fields

- `Name` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Reserved for future use.

- `Description` – Description string, not more than 2048 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

A description of this trigger.

- `Schedule` – UTF-8 string.

A `cron` expression used to specify the schedule (see [Time-Based
Schedules for Jobs and Crawlers](monitor-data-warehouse-schedule.md "monitor-data-warehouse-schedule.md"). For example, to run something every
day at 12:15 UTC, you would specify: `cron(15 12 * * ? *)`.

- `Actions` – An array of [Action](#aws-glue-api-jobs-trigger-Action "#aws-glue-api-jobs-trigger-Action") objects.

The actions initiated by this trigger.

- `Predicate` – A [Predicate](#aws-glue-api-jobs-trigger-Predicate "#aws-glue-api-jobs-trigger-Predicate") object.

The predicate of this trigger, which defines when it will fire.

- `EventBatchingCondition` – An [EventBatchingCondition](#aws-glue-api-jobs-trigger-EventBatchingCondition "#aws-glue-api-jobs-trigger-EventBatchingCondition") object.

Batch condition that must be met (specified number of events received
or batch time window expired) before EventBridge event trigger fires.

## Predicate structure

Defines the predicate of the trigger, which determines when it fires.

###### Fields

- `Logical` – UTF-8 string (valid values: `AND` | `ANY`).

An optional field if only one condition is listed. If multiple conditions
are listed, then this field is required.

- `Conditions` – An array of [Condition](#aws-glue-api-jobs-trigger-Condition "#aws-glue-api-jobs-trigger-Condition") objects, not more than 500 structures.

A list of the conditions that determine when the trigger will fire.

## Condition structure

Defines a condition under which a trigger fires.

###### Fields

- `LogicalOperator` – UTF-8 string (valid values: `EQUALS`).

A logical operator.

- `JobName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the job whose `JobRuns` this condition applies
to, and on which this trigger waits.

- `State` – UTF-8 string (valid values: `STARTING` | `RUNNING` | `STOPPING` | `STOPPED` | `SUCCEEDED` | `FAILED` | `TIMEOUT` | `ERROR` | `WAITING` | `EXPIRED`).

The condition state. Currently, the only job states that a trigger can
listen for are `SUCCEEDED`, `STOPPED`, `FAILED`,
and `TIMEOUT`. The only crawler states that a trigger can listen
for are `SUCCEEDED`, `FAILED`, and `CANCELLED`.

- `CrawlerName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the crawler to which this condition applies.

- `CrawlState` – UTF-8 string (valid values: `RUNNING` | `CANCELLING` | `CANCELLED` | `SUCCEEDED` | `FAILED` | `ERROR`).

The state of the crawler to which this condition applies.

## Action structure

Defines an action to be initiated by a trigger.

###### Fields

- `JobName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of a job to be run.

- `Arguments` – A map array of key-value pairs.

Each key is a UTF-8 string.

Each value is a UTF-8 string.

The job arguments used when this trigger fires. For this job run, they replace
the default arguments set in the job definition itself.

You can specify arguments here that your own job-execution script consumes,
as well as arguments that AWS Glue itself consumes.

For information about how to specify and consume your own Job arguments,
see the [Calling
AWS Glue APIs in Python](aws-glue-programming-python-calling.md "aws-glue-programming-python-calling.md") topic in the developer guide.

For information about the key-value pairs that AWS Glue consumes
to set up your job, see the [Special
Parameters Used by AWS Glue](aws-glue-programming-etl-glue-arguments.md "aws-glue-programming-etl-glue-arguments.md") topic in the developer guide.

- `Timeout` – Number (integer), at least 1.

The `JobRun` timeout in minutes. This is the maximum time
that a job run can consume resources before it is terminated and enters `TIMEOUT`
status. This overrides the timeout value set in the parent job.

Jobs must have timeout values less than 7 days or 10080 minutes. Otherwise,
the jobs will throw an exception.

When the value is left blank, the timeout is defaulted to 2880 minutes.

Any existing AWS Glue jobs that had a timeout value greater
than 7 days will be defaulted to 7 days. For instance if you have specified a timeout
of 20 days for a batch job, it will be stopped on the 7th day.

For streaming jobs, if you have set up a maintenance window, it will be restarted
during the maintenance window after 7 days.

- `SecurityConfiguration` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the `SecurityConfiguration` structure to be
used with this action.

- `NotificationProperty` – A [NotificationProperty](aws-glue-api-jobs-runs.md#aws-glue-api-jobs-runs-NotificationProperty "aws-glue-api-jobs-runs.md#aws-glue-api-jobs-runs-NotificationProperty") object.

Specifies configuration properties of a job run notification.

- `CrawlerName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the crawler to be used with this action.

## EventBatchingCondition structure

Batch condition that must be met (specified number of events received
or batch time window expired) before EventBridge event trigger fires.

###### Fields

- `BatchSize` – _Required:_ Number (integer), not less than 1 or more than 100.

Number of events that must be received from Amazon EventBridge before
EventBridge event trigger fires.

- `BatchWindow` – Number (integer), not less than 1 or more than 900.

Window of time in seconds after which EventBridge event trigger fires.
Window starts when first event is received.

## Operations

- [CreateTrigger action (Python: create_trigger)](#aws-glue-api-jobs-trigger-CreateTrigger "#aws-glue-api-jobs-trigger-CreateTrigger")
- [StartTrigger action (Python: start_trigger)](#aws-glue-api-jobs-trigger-StartTrigger "#aws-glue-api-jobs-trigger-StartTrigger")
- [GetTrigger action (Python: get_trigger)](#aws-glue-api-jobs-trigger-GetTrigger "#aws-glue-api-jobs-trigger-GetTrigger")
- [GetTriggers action (Python: get_triggers)](#aws-glue-api-jobs-trigger-GetTriggers "#aws-glue-api-jobs-trigger-GetTriggers")
- [UpdateTrigger action (Python: update_trigger)](#aws-glue-api-jobs-trigger-UpdateTrigger "#aws-glue-api-jobs-trigger-UpdateTrigger")
- [StopTrigger action (Python: stop_trigger)](#aws-glue-api-jobs-trigger-StopTrigger "#aws-glue-api-jobs-trigger-StopTrigger")
- [DeleteTrigger action (Python: delete_trigger)](#aws-glue-api-jobs-trigger-DeleteTrigger "#aws-glue-api-jobs-trigger-DeleteTrigger")
- [ListTriggers action (Python: list_triggers)](#aws-glue-api-jobs-trigger-ListTriggers "#aws-glue-api-jobs-trigger-ListTriggers")
- [BatchGetTriggers action (Python: batch_get_triggers)](#aws-glue-api-jobs-trigger-BatchGetTriggers "#aws-glue-api-jobs-trigger-BatchGetTriggers")

## CreateTrigger action (Python: create_trigger)

Creates a new trigger.

Job arguments may be logged. Do not pass plaintext secrets as arguments.
Retrieve secrets from a AWS Glue Connection, AWS
Secrets Manager or other secret management mechanism if you intend to keep them
within the Job.

###### Request

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the trigger.

- `WorkflowName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the workflow associated with the trigger.

- `Type` – _Required:_ UTF-8 string (valid values: `SCHEDULED` | `CONDITIONAL` | `ON_DEMAND` | `EVENT`).

The type of the new trigger.

- `Schedule` – UTF-8 string.

A `cron` expression used to specify the schedule (see [Time-Based
Schedules for Jobs and Crawlers](monitor-data-warehouse-schedule.md "monitor-data-warehouse-schedule.md"). For example, to run something every
day at 12:15 UTC, you would specify: `cron(15 12 * * ? *)`.

This field is required when the trigger type is SCHEDULED.

- `Predicate` – A [Predicate](#aws-glue-api-jobs-trigger-Predicate "#aws-glue-api-jobs-trigger-Predicate") object.

A predicate to specify when the new trigger should fire.

This field is required when the trigger type is `CONDITIONAL`.

- `Actions` – _Required:_ An array of [Action](#aws-glue-api-jobs-trigger-Action "#aws-glue-api-jobs-trigger-Action") objects.

The actions initiated by this trigger when it fires.

- `Description` – Description string, not more than 2048 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

A description of the new trigger.

- `StartOnCreation` – Boolean.

Set to `true` to start `SCHEDULED` and `CONDITIONAL`
triggers when created. True is not supported for `ON_DEMAND` triggers.

- `Tags` – A map array of key-value pairs, not more than 50 pairs.

Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

Each value is a UTF-8 string, not more than 256 bytes long.

The tags to use with this trigger. You may use tags to limit access to the
trigger. For more information about tags in AWS Glue, see [AWS Tags in AWS Glue](monitor-tags.md "monitor-tags.md") in the developer guide.

- `EventBatchingCondition` – An [EventBatchingCondition](#aws-glue-api-jobs-trigger-EventBatchingCondition "#aws-glue-api-jobs-trigger-EventBatchingCondition") object.

Batch condition that must be met (specified number of events received
or batch time window expired) before EventBridge event trigger fires.

###### Response

- `Name` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the trigger.

###### Errors

- `AlreadyExistsException`
- `EntityNotFoundException`
- `InvalidInputException`
- `IdempotentParameterMismatchException`
- `InternalServiceException`
- `OperationTimeoutException`
- `ResourceNumberLimitExceededException`
- `ConcurrentModificationException`

## StartTrigger action (Python: start_trigger)

Starts an existing trigger. See [Triggering
Jobs](trigger-job.md "trigger-job.md") for information about how different types of trigger are started.

###### Request

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the trigger to start.

###### Response

- `Name` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the trigger that was started.

###### Errors

- `InvalidInputException`
- `InternalServiceException`
- `EntityNotFoundException`
- `OperationTimeoutException`
- `ResourceNumberLimitExceededException`
- `ConcurrentRunsExceededException`

## GetTrigger action (Python: get_trigger)

Retrieves the definition of a trigger.

###### Request

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the trigger to retrieve.

###### Response

- `Trigger` – A [Trigger](#aws-glue-api-jobs-trigger-Trigger "#aws-glue-api-jobs-trigger-Trigger") object.

The requested trigger definition.

###### Errors

- `EntityNotFoundException`
- `InvalidInputException`
- `InternalServiceException`
- `OperationTimeoutException`

## GetTriggers action (Python: get_triggers)

Gets all the triggers associated with a job.

###### Request

- `NextToken` – UTF-8 string.

A continuation token, if this is a continuation call.

- `DependentJobName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the job to retrieve triggers for. The trigger that can start
this job is returned, and if there is no such trigger, all triggers are returned.

- `MaxResults` – Number (integer), not less than 1 or more than 200.

The maximum size of the response.

###### Response

- `Triggers` – An array of [Trigger](#aws-glue-api-jobs-trigger-Trigger "#aws-glue-api-jobs-trigger-Trigger") objects.

A list of triggers for the specified job.

- `NextToken` – UTF-8 string.

A continuation token, if not all the requested triggers have yet been returned.

###### Errors

- `EntityNotFoundException`
- `InvalidInputException`
- `InternalServiceException`
- `OperationTimeoutException`

## UpdateTrigger action (Python: update_trigger)

Updates a trigger definition.

Job arguments may be logged. Do not pass plaintext secrets as arguments.
Retrieve secrets from a AWS Glue Connection, AWS
Secrets Manager or other secret management mechanism if you intend to keep them
within the Job.

###### Request

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the trigger to update.

- `TriggerUpdate` – _Required:_ A [TriggerUpdate](#aws-glue-api-jobs-trigger-TriggerUpdate "#aws-glue-api-jobs-trigger-TriggerUpdate") object.

The new values with which to update the trigger.

###### Response

- `Trigger` – A [Trigger](#aws-glue-api-jobs-trigger-Trigger "#aws-glue-api-jobs-trigger-Trigger") object.

The resulting trigger definition.

###### Errors

- `InvalidInputException`
- `InternalServiceException`
- `EntityNotFoundException`
- `OperationTimeoutException`
- `ConcurrentModificationException`

## StopTrigger action (Python: stop_trigger)

Stops a specified trigger.

###### Request

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the trigger to stop.

###### Response

- `Name` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the trigger that was stopped.

###### Errors

- `InvalidInputException`
- `InternalServiceException`
- `EntityNotFoundException`
- `OperationTimeoutException`
- `ConcurrentModificationException`

## DeleteTrigger action (Python: delete_trigger)

Deletes a specified trigger. If the trigger is not found, no exception
is thrown.

###### Request

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the trigger to delete.

###### Response

- `Name` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the trigger that was deleted.

###### Errors

- `InvalidInputException`
- `InternalServiceException`
- `OperationTimeoutException`
- `ConcurrentModificationException`

## ListTriggers action (Python: list_triggers)

Retrieves the names of all trigger resources in this AWS account, or the resources with the specified tag. This operation allows you
to see which resources are available in your account, and their names.

This operation takes the optional `Tags` field, which you
can use as a filter on the response so that tagged resources can be retrieved as
a group. If you choose to use tags filtering, only resources with the tag are retrieved.

###### Request

- `NextToken` – UTF-8 string.

A continuation token, if this is a continuation request.

- `DependentJobName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the job for which to retrieve triggers. The trigger that can
start this job is returned. If there is no such trigger, all triggers are returned.

- `MaxResults` – Number (integer), not less than 1 or more than 200.

The maximum size of a list to return.

- `Tags` – A map array of key-value pairs, not more than 50 pairs.

Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

Each value is a UTF-8 string, not more than 256 bytes long.

Specifies to return only these tagged resources.

###### Response

- `TriggerNames` – An array of UTF-8 strings.

The names of all triggers in the account, or the triggers with the specified
tags.

- `NextToken` – UTF-8 string.

A continuation token, if the returned list does not contain the last metric
available.

###### Errors

- `EntityNotFoundException`
- `InvalidInputException`
- `InternalServiceException`
- `OperationTimeoutException`

## BatchGetTriggers action (Python: batch_get_triggers)

Returns a list of resource metadata for a given list of trigger names. After
calling the `ListTriggers` operation, you can call this operation
to access the data to which you have been granted permissions. This operation
supports all IAM permissions, including permission conditions that uses tags.

###### Request

- `TriggerNames` – _Required:_ An array of UTF-8 strings.

A list of trigger names, which may be the names returned from the `ListTriggers`
operation.

###### Response

- `Triggers` – An array of [Trigger](#aws-glue-api-jobs-trigger-Trigger "#aws-glue-api-jobs-trigger-Trigger") objects.

A list of trigger definitions.

- `TriggersNotFound` – An array of UTF-8 strings.

A list of names of triggers not found.

###### Errors

- `InternalServiceException`
- `OperationTimeoutException`
- `InvalidInputException`
