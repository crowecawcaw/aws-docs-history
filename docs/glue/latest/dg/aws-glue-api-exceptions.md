# Exceptions

This section describes AWS Glue exceptions that you can use
to find the source of problems and fix them. For more information on HTTP error
codes and strings for exceptions related to machine learning, see [AWS Glue machine learning exceptions](exceptions-machine-learning.md "exceptions-machine-learning.md").

## AccessDeniedException structure

Access to a resource was denied.

###### Fields

- `Message` – UTF-8 string.

A message describing the problem.

## AlreadyExistsException structure

A resource to be created or added already exists.

###### Fields

- `Message` – UTF-8 string.

A message describing the problem.

## ConcurrentModificationException structure

Two processes are trying to modify a resource simultaneously.

###### Fields

- `Message` – UTF-8 string.

A message describing the problem.

## ConcurrentRunsExceededException structure

Too many jobs are being run concurrently.

###### Fields

- `Message` – UTF-8 string.

A message describing the problem.

## CrawlerNotRunningException structure

The specified crawler is not running.

###### Fields

- `Message` – UTF-8 string.

A message describing the problem.

## CrawlerRunningException structure

The operation cannot be performed because the crawler is already running.

###### Fields

- `Message` – UTF-8 string.

A message describing the problem.

## CrawlerStoppingException structure

The specified crawler is stopping.

###### Fields

- `Message` – UTF-8 string.

A message describing the problem.

## EntityNotFoundException structure

A specified entity does not exist

###### Fields

- `Message` – UTF-8 string.

A message describing the problem.

- `FromFederationSource` – Boolean.

Indicates whether or not the exception relates to a federated source.

## FederationSourceException structure

A federation source failed.

###### Fields

- `FederationSourceErrorCode` – UTF-8 string (valid values: `AccessDeniedException` | `EntityNotFoundException` | `InvalidCredentialsException` | `InvalidInputException` | `InvalidResponseException` | `OperationTimeoutException` | `OperationNotSupportedException` | `InternalServiceException` | `PartialFailureException` | `ThrottlingException`).

The error code of the problem.

- `Message` – UTF-8 string.

The message describing the problem.

## FederationSourceRetryableException structure

A federation source failed, but the operation may be retried.

###### Fields

- `Message` – UTF-8 string.

A message describing the problem.

## GlueEncryptionException structure

An encryption operation failed.

###### Fields

- `Message` – UTF-8 string.

The message describing the problem.

## IdempotentParameterMismatchException structure

The same unique identifier was associated with two different records.

###### Fields

- `Message` – UTF-8 string.

A message describing the problem.

## IllegalWorkflowStateException structure

The workflow is in an invalid state to perform a requested operation.

###### Fields

- `Message` – UTF-8 string.

A message describing the problem.

## InternalServiceException structure

An internal service error occurred.

###### Fields

- `Message` – UTF-8 string.

A message describing the problem.

## InvalidExecutionEngineException structure

An unknown or invalid execution engine was specified.

###### Fields

- `message` – UTF-8 string.

A message describing the problem.

## InvalidInputException structure

The input provided was not valid.

###### Fields

- `Message` – UTF-8 string.

A message describing the problem.

- `FromFederationSource` – Boolean.

Indicates whether or not the exception relates to a federated source.

## InvalidStateException structure

An error that indicates your data is in an invalid state.

###### Fields

- `Message` – UTF-8 string.

A message describing the problem.

## InvalidTaskStatusTransitionException structure

Proper transition from one task to the next failed.

###### Fields

- `message` – UTF-8 string.

A message describing the problem.

## JobDefinitionErrorException structure

A job definition is not valid.

###### Fields

- `message` – UTF-8 string.

A message describing the problem.

## JobRunInTerminalStateException structure

The terminal state of a job run signals a failure.

###### Fields

- `message` – UTF-8 string.

A message describing the problem.

## JobRunInvalidStateTransitionException structure

A job run encountered an invalid transition from source state to target
state.

###### Fields

- `jobRunId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of the job run in question.

- `message` – UTF-8 string.

A message describing the problem.

- `sourceState` – UTF-8 string (valid values: `STARTING` | `RUNNING` | `STOPPING` | `STOPPED` | `SUCCEEDED` | `FAILED` | `TIMEOUT` | `ERROR` | `WAITING` | `EXPIRED`).

The source state.

- `targetState` – UTF-8 string (valid values: `STARTING` | `RUNNING` | `STOPPING` | `STOPPED` | `SUCCEEDED` | `FAILED` | `TIMEOUT` | `ERROR` | `WAITING` | `EXPIRED`).

The target state.

## JobRunNotInTerminalStateException structure

A job run is not in a terminal state.

###### Fields

- `message` – UTF-8 string.

A message describing the problem.

## LateRunnerException structure

A job runner is late.

###### Fields

- `Message` – UTF-8 string.

A message describing the problem.

## NoScheduleException structure

There is no applicable schedule.

###### Fields

- `Message` – UTF-8 string.

A message describing the problem.

## OperationTimeoutException structure

The operation timed out.

###### Fields

- `Message` – UTF-8 string.

A message describing the problem.

## ResourceNotReadyException structure

A resource was not ready for a transaction.

###### Fields

- `Message` – UTF-8 string.

A message describing the problem.

## ResourceNumberLimitExceededException structure

A resource numerical limit was exceeded.

###### Fields

- `Message` – UTF-8 string.

A message describing the problem.

## SchedulerNotRunningException structure

The specified scheduler is not running.

###### Fields

- `Message` – UTF-8 string.

A message describing the problem.

## SchedulerRunningException structure

The specified scheduler is already running.

###### Fields

- `Message` – UTF-8 string.

A message describing the problem.

## SchedulerTransitioningException structure

The specified scheduler is transitioning.

###### Fields

- `Message` – UTF-8 string.

A message describing the problem.

## UnrecognizedRunnerException structure

The job runner was not recognized.

###### Fields

- `Message` – UTF-8 string.

A message describing the problem.

## ValidationException structure

A value could not be validated.

###### Fields

- `Message` – UTF-8 string.

A message describing the problem.

## VersionMismatchException structure

There was a version conflict.

###### Fields

- `message` – UTF-8 string.

A message describing the problem.
