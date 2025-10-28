# Neptune dataplane API Exceptions

**Exceptions:**

- [AccessDeniedException (structure)](#AccessDeniedException "#AccessDeniedException")
- [BadRequestException (structure)](#BadRequestException "#BadRequestException")
- [BulkLoadIdNotFoundException (structure)](#BulkLoadIdNotFoundException "#BulkLoadIdNotFoundException")
- [CancelledByUserException (structure)](#CancelledByUserException "#CancelledByUserException")
- [ClientTimeoutException (structure)](#ClientTimeoutException "#ClientTimeoutException")
- [ConcurrentModificationException (structure)](#ConcurrentModificationException "#ConcurrentModificationException")
- [ConstraintViolationException (structure)](#ConstraintViolationException "#ConstraintViolationException")
- [ExpiredStreamException (structure)](#ExpiredStreamException "#ExpiredStreamException")
- [FailureByQueryException (structure)](#FailureByQueryException "#FailureByQueryException")
- [IllegalArgumentException (structure)](#IllegalArgumentException "#IllegalArgumentException")
- [InternalFailureException (structure)](#InternalFailureException "#InternalFailureException")
- [InvalidArgumentException (structure)](#InvalidArgumentException "#InvalidArgumentException")
- [InvalidNumericDataException (structure)](#InvalidNumericDataException "#InvalidNumericDataException")
- [InvalidParameterException (structure)](#InvalidParameterException "#InvalidParameterException")
- [LoadUrlAccessDeniedException (structure)](#LoadUrlAccessDeniedException "#LoadUrlAccessDeniedException")
- [MalformedQueryException (structure)](#MalformedQueryException "#MalformedQueryException")
- [MemoryLimitExceededException (structure)](#MemoryLimitExceededException "#MemoryLimitExceededException")
- [MethodNotAllowedException (structure)](#MethodNotAllowedException "#MethodNotAllowedException")
- [MissingParameterException (structure)](#MissingParameterException "#MissingParameterException")
- [MLResourceNotFoundException (structure)](#MLResourceNotFoundException "#MLResourceNotFoundException")
- [ParsingException (structure)](#ParsingException "#ParsingException")
- [PreconditionsFailedException (structure)](#PreconditionsFailedException "#PreconditionsFailedException")
- [QueryLimitExceededException (structure)](#QueryLimitExceededException "#QueryLimitExceededException")
- [QueryLimitException (structure)](#QueryLimitException "#QueryLimitException")
- [QueryTooLargeException (structure)](#QueryTooLargeException "#QueryTooLargeException")
- [ReadOnlyViolationException (structure)](#ReadOnlyViolationException "#ReadOnlyViolationException")
- [S3Exception (structure)](#S3Exception "#S3Exception")
- [ServerShutdownException (structure)](#ServerShutdownException "#ServerShutdownException")
- [StatisticsNotAvailableException (structure)](#StatisticsNotAvailableException "#StatisticsNotAvailableException")
- [StreamRecordsNotFoundException (structure)](#StreamRecordsNotFoundException "#StreamRecordsNotFoundException")
- [ThrottlingException (structure)](#ThrottlingException "#ThrottlingException")
- [TimeLimitExceededException (structure)](#TimeLimitExceededException "#TimeLimitExceededException")
- [TooManyRequestsException (structure)](#TooManyRequestsException "#TooManyRequestsException")
- [UnsupportedOperationException (structure)](#UnsupportedOperationException "#UnsupportedOperationException")
- [UnloadUrlAccessDeniedException (structure)](#UnloadUrlAccessDeniedException "#UnloadUrlAccessDeniedException")

## AccessDeniedException (structure)

Raised in case of an authentication or authorization failure.

###### Fields

- **code** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The HTTP status code returned with the exception.

- **detailedMessage** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

A detailed message describing the problem.

- **requestId** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The ID of the request in question.

## BadRequestException (structure)

Raised when a request is submitted that cannot be processed.

###### Fields

- **code** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The HTTP status code returned with the exception.

- **detailedMessage** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

A detailed message describing the problem.

- **requestId** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The ID of the bad request.

## BulkLoadIdNotFoundException (structure)

Raised when a specified bulk-load job ID cannot be found.

###### Fields

- **code** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The HTTP status code returned with the exception.

- **detailedMessage** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

A detailed message describing the problem.

- **requestId** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The bulk-load job ID that could not be found.

## CancelledByUserException (structure)

Raised when a user cancelled a request.

###### Fields

- **code** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The HTTP status code returned with the exception.

- **detailedMessage** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

A detailed message describing the problem.

- **requestId** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The ID of the request in question.

## ClientTimeoutException (structure)

Raised when a request timed out in the client.

###### Fields

- **code** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The HTTP status code returned with the exception.

- **detailedMessage** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

A detailed message describing the problem.

- **requestId** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The ID of the request in question.

## ConcurrentModificationException (structure)

Raised when a request attempts to modify data that is concurrently being
modified by another process.

###### Fields

- **code** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The HTTP status code returned with the exception.

- **detailedMessage** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

A detailed message describing the problem.

- **requestId** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The ID of the request in question.

## ConstraintViolationException (structure)

Raised when a value in a request field did not satisfy required constraints.

###### Fields

- **code** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The HTTP status code returned with the exception.

- **detailedMessage** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

A detailed message describing the problem.

- **requestId** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The ID of the request in question.

## ExpiredStreamException (structure)

Raised when a request attempts to access an stream that has expired.

###### Fields

- **code** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The HTTP status code returned with the exception.

- **detailedMessage** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

A detailed message describing the problem.

- **requestId** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The ID of the request in question.

## FailureByQueryException (structure)

Raised when a request fails.

###### Fields

- **code** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The HTTP status code returned with the exception.

- **detailedMessage** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

A detailed message describing the problem.

- **requestId** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The ID of the request in question.

## IllegalArgumentException (structure)

Raised when an argument in a request is not supported.

###### Fields

- **code** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The HTTP status code returned with the exception.

- **detailedMessage** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

A detailed message describing the problem.

- **requestId** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The ID of the request in question.

## InternalFailureException (structure)

Raised when the processing of the request failed unexpectedly.

###### Fields

- **code** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The HTTP status code returned with the exception.

- **detailedMessage** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

A detailed message describing the problem.

- **requestId** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The ID of the request in question.

## InvalidArgumentException (structure)

Raised when an argument in a request has an invalid value.

###### Fields

- **code** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The HTTP status code returned with the exception.

- **detailedMessage** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

A detailed message describing the problem.

- **requestId** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The ID of the request in question.

## InvalidNumericDataException (structure)

Raised when invalid numerical data is encountered when servicing a request.

###### Fields

- **code** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The HTTP status code returned with the exception.

- **detailedMessage** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

A detailed message describing the problem.

- **requestId** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The ID of the request in question.

## InvalidParameterException (structure)

Raised when a parameter value is not valid.

###### Fields

- **code** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The HTTP status code returned with the exception.

- **detailedMessage** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

A detailed message describing the problem.

- **requestId** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The ID of the request that includes an invalid parameter.

## LoadUrlAccessDeniedException (structure)

Raised when access is denied to a specified load URL.

###### Fields

- **code** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The HTTP status code returned with the exception.

- **detailedMessage** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

A detailed message describing the problem.

- **requestId** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The ID of the request in question.

## MalformedQueryException (structure)

Raised when a query is submitted that is syntactically incorrect or does
not pass additional validation.

###### Fields

- **code** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The HTTP status code returned with the exception.

- **detailedMessage** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

A detailed message describing the problem.

- **requestId** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The ID of the malformed query request.

## MemoryLimitExceededException (structure)

Raised when a request fails because of insufficient memory resources.
The request can be retried.

###### Fields

- **code** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The HTTP status code returned with the exception.

- **detailedMessage** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

A detailed message describing the problem.

- **requestId** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The ID of the request that failed.

## MethodNotAllowedException (structure)

Raised when the HTTP method used by a request is not supported by the endpoint
being used.

###### Fields

- **code** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The HTTP status code returned with the exception.

- **detailedMessage** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

A detailed message describing the problem.

- **requestId** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The ID of the request in question.

## MissingParameterException (structure)

Raised when a required parameter is missing.

###### Fields

- **code** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The HTTP status code returned with the exception.

- **detailedMessage** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

A detailed message describing the problem.

- **requestId** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The ID of the request in which the parameter is missing.

## MLResourceNotFoundException (structure)

Raised when a specified machine-learning resource could not be found.

###### Fields

- **code** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The HTTP status code returned with the exception.

- **detailedMessage** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

A detailed message describing the problem.

- **requestId** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The ID of the request in question.

## ParsingException (structure)

Raised when a parsing issue is encountered.

###### Fields

- **code** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The HTTP status code returned with the exception.

- **detailedMessage** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

A detailed message describing the problem.

- **requestId** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The ID of the request in question.

## PreconditionsFailedException (structure)

Raised when a precondition for processing a request is not satisfied.

###### Fields

- **code** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The HTTP status code returned with the exception.

- **detailedMessage** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

A detailed message describing the problem.

- **requestId** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The ID of the request in question.

## QueryLimitExceededException (structure)

Raised when the number of active queries exceeds what the server can process.
The query in question can be retried when the system is less busy.

###### Fields

- **code** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The HTTP status code returned with the exception.

- **detailedMessage** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

A detailed message describing the problem.

- **requestId** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The ID of the request which exceeded the limit.

## QueryLimitException (structure)

Raised when the size of a query exceeds the system limit.

###### Fields

- **code** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The HTTP status code returned with the exception.

- **detailedMessage** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

A detailed message describing the problem.

- **requestId** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The ID of the request that exceeded the limit.

## QueryTooLargeException (structure)

Raised when the body of a query is too large.

###### Fields

- **code** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The HTTP status code returned with the exception.

- **detailedMessage** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

A detailed message describing the problem.

- **requestId** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The ID of the request that is too large.

## ReadOnlyViolationException (structure)

Raised when a request attempts to write to a read-only resource.

###### Fields

- **code** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The HTTP status code returned with the exception.

- **detailedMessage** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

A detailed message describing the problem.

- **requestId** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The ID of the request in which the parameter is missing.

## S3Exception (structure)

Raised when there is a problem accessing Amazon S3.

###### Fields

- **code** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The HTTP status code returned with the exception.

- **detailedMessage** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

A detailed message describing the problem.

- **requestId** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The ID of the request in question.

## ServerShutdownException (structure)

Raised when the server shuts down while processing a request.

###### Fields

- **code** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The HTTP status code returned with the exception.

- **detailedMessage** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

A detailed message describing the problem.

- **requestId** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The ID of the request in question.

## StatisticsNotAvailableException (structure)

Raised when statistics needed to satisfy a request are not available.

###### Fields

- **code** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The HTTP status code returned with the exception.

- **detailedMessage** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

A detailed message describing the problem.

- **requestId** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The ID of the request in question.

## StreamRecordsNotFoundException (structure)

Raised when stream records requested by a query cannot be found.

###### Fields

- **code** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The HTTP status code returned with the exception.

- **detailedMessage** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

A detailed message describing the problem.

- **requestId** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The ID of the request in question.

## ThrottlingException (structure)

Raised when the rate of requests exceeds the maximum throughput. Requests
can be retried after encountering this exception.

###### Fields

- **code** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The HTTP status code returned with the exception.

- **detailedMessage** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

A detailed message describing the problem.

- **requestId** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The ID of the request that could not be processed for this reason.

## TimeLimitExceededException (structure)

Raised when the an operation exceeds the time limit allowed for it.

###### Fields

- **code** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The HTTP status code returned with the exception.

- **detailedMessage** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

A detailed message describing the problem.

- **requestId** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The ID of the request that could not be processed for this reason.

## TooManyRequestsException (structure)

Raised when the number of requests being processed exceeds the limit.

###### Fields

- **code** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The HTTP status code returned with the exception.

- **detailedMessage** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

A detailed message describing the problem.

- **requestId** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The ID of the request that could not be processed for this reason.

## UnsupportedOperationException (structure)

Raised when a request attempts to initiate an operation that is not supported.

###### Fields

- **code** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The HTTP status code returned with the exception.

- **detailedMessage** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

A detailed message describing the problem.

- **requestId** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The ID of the request in question.

## UnloadUrlAccessDeniedException (structure)

Raised when access is denied to a URL that is an unload target.

###### Fields

- **code** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The HTTP status code returned with the exception.

- **detailedMessage** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

A detailed message describing the problem.

- **requestId** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The ID of the request in question.
