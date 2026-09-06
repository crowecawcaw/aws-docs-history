

# Neptune dataplane API Exceptions
<a name="data-api-dp-errors"></a>

**Exceptions:**
+ [AccessDeniedException (structure)](#AccessDeniedException)
+ [BadRequestException (structure)](#BadRequestException)
+ [BulkLoadIdNotFoundException (structure)](#BulkLoadIdNotFoundException)
+ [CancelledByUserException (structure)](#CancelledByUserException)
+ [ClientTimeoutException (structure)](#ClientTimeoutException)
+ [ConcurrentModificationException (structure)](#ConcurrentModificationException)
+ [ConstraintViolationException (structure)](#ConstraintViolationException)
+ [ExpiredStreamException (structure)](#ExpiredStreamException)
+ [FailureByQueryException (structure)](#FailureByQueryException)
+ [IllegalArgumentException (structure)](#IllegalArgumentException)
+ [InternalFailureException (structure)](#InternalFailureException)
+ [InvalidArgumentException (structure)](#InvalidArgumentException)
+ [InvalidNumericDataException (structure)](#InvalidNumericDataException)
+ [InvalidParameterException (structure)](#InvalidParameterException)
+ [LoadUrlAccessDeniedException (structure)](#LoadUrlAccessDeniedException)
+ [MalformedQueryException (structure)](#MalformedQueryException)
+ [MemoryLimitExceededException (structure)](#MemoryLimitExceededException)
+ [MethodNotAllowedException (structure)](#MethodNotAllowedException)
+ [MissingParameterException (structure)](#MissingParameterException)
+ [MLResourceNotFoundException (structure)](#MLResourceNotFoundException)
+ [ParsingException (structure)](#ParsingException)
+ [PreconditionsFailedException (structure)](#PreconditionsFailedException)
+ [QueryLimitExceededException (structure)](#QueryLimitExceededException)
+ [QueryLimitException (structure)](#QueryLimitException)
+ [QueryTooLargeException (structure)](#QueryTooLargeException)
+ [ReadOnlyViolationException (structure)](#ReadOnlyViolationException)
+ [S3Exception (structure)](#S3Exception)
+ [ServerShutdownException (structure)](#ServerShutdownException)
+ [StatisticsNotAvailableException (structure)](#StatisticsNotAvailableException)
+ [StreamRecordsNotFoundException (structure)](#StreamRecordsNotFoundException)
+ [ThrottlingException (structure)](#ThrottlingException)
+ [TimeLimitExceededException (structure)](#TimeLimitExceededException)
+ [TooManyRequestsException (structure)](#TooManyRequestsException)
+ [UnsupportedOperationException (structure)](#UnsupportedOperationException)
+ [UnloadUrlAccessDeniedException (structure)](#UnloadUrlAccessDeniedException)

## AccessDeniedException (structure)
<a name="AccessDeniedException"></a>

Raised in case of an authentication or authorization failure.

**Fields**
+ **code** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The HTTP status code returned with the exception.
+ **detailedMessage** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  A detailed message describing the problem.
+ **requestId** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The ID of the request in question.

## BadRequestException (structure)
<a name="BadRequestException"></a>

Raised when a request is submitted that cannot be processed.

**Fields**
+ **code** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The HTTP status code returned with the exception.
+ **detailedMessage** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  A detailed message describing the problem.
+ **requestId** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The ID of the bad request.

## BulkLoadIdNotFoundException (structure)
<a name="BulkLoadIdNotFoundException"></a>

Raised when a specified bulk-load job ID cannot be found.

**Fields**
+ **code** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The HTTP status code returned with the exception.
+ **detailedMessage** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  A detailed message describing the problem.
+ **requestId** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The bulk-load job ID that could not be found.

## CancelledByUserException (structure)
<a name="CancelledByUserException"></a>

Raised when a user cancelled a request.

**Fields**
+ **code** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The HTTP status code returned with the exception.
+ **detailedMessage** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  A detailed message describing the problem.
+ **requestId** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The ID of the request in question.

## ClientTimeoutException (structure)
<a name="ClientTimeoutException"></a>

Raised when a request timed out in the client.

**Fields**
+ **code** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The HTTP status code returned with the exception.
+ **detailedMessage** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  A detailed message describing the problem.
+ **requestId** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The ID of the request in question.

## ConcurrentModificationException (structure)
<a name="ConcurrentModificationException"></a>

Raised when a request attempts to modify data that is concurrently being modified by another process.

**Fields**
+ **code** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The HTTP status code returned with the exception.
+ **detailedMessage** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  A detailed message describing the problem.
+ **requestId** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The ID of the request in question.

## ConstraintViolationException (structure)
<a name="ConstraintViolationException"></a>

Raised when a value in a request field did not satisfy required constraints.

**Fields**
+ **code** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The HTTP status code returned with the exception.
+ **detailedMessage** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  A detailed message describing the problem.
+ **requestId** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The ID of the request in question.

## ExpiredStreamException (structure)
<a name="ExpiredStreamException"></a>

Raised when a request attempts to access an stream that has expired.

**Fields**
+ **code** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The HTTP status code returned with the exception.
+ **detailedMessage** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  A detailed message describing the problem.
+ **requestId** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The ID of the request in question.

## FailureByQueryException (structure)
<a name="FailureByQueryException"></a>

Raised when a request fails.

**Fields**
+ **code** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The HTTP status code returned with the exception.
+ **detailedMessage** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  A detailed message describing the problem.
+ **requestId** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The ID of the request in question.

## IllegalArgumentException (structure)
<a name="IllegalArgumentException"></a>

Raised when an argument in a request is not supported.

**Fields**
+ **code** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The HTTP status code returned with the exception.
+ **detailedMessage** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  A detailed message describing the problem.
+ **requestId** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The ID of the request in question.

## InternalFailureException (structure)
<a name="InternalFailureException"></a>

Raised when the processing of the request failed unexpectedly.

**Fields**
+ **code** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The HTTP status code returned with the exception.
+ **detailedMessage** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  A detailed message describing the problem.
+ **requestId** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The ID of the request in question.

## InvalidArgumentException (structure)
<a name="InvalidArgumentException"></a>

Raised when an argument in a request has an invalid value.

**Fields**
+ **code** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The HTTP status code returned with the exception.
+ **detailedMessage** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  A detailed message describing the problem.
+ **requestId** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The ID of the request in question.

## InvalidNumericDataException (structure)
<a name="InvalidNumericDataException"></a>

Raised when invalid numerical data is encountered when servicing a request.

**Fields**
+ **code** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The HTTP status code returned with the exception.
+ **detailedMessage** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  A detailed message describing the problem.
+ **requestId** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The ID of the request in question.

## InvalidParameterException (structure)
<a name="InvalidParameterException"></a>

Raised when a parameter value is not valid.

**Fields**
+ **code** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The HTTP status code returned with the exception.
+ **detailedMessage** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  A detailed message describing the problem.
+ **requestId** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The ID of the request that includes an invalid parameter.

## LoadUrlAccessDeniedException (structure)
<a name="LoadUrlAccessDeniedException"></a>

Raised when access is denied to a specified load URL.

**Fields**
+ **code** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The HTTP status code returned with the exception.
+ **detailedMessage** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  A detailed message describing the problem.
+ **requestId** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The ID of the request in question.

## MalformedQueryException (structure)
<a name="MalformedQueryException"></a>

Raised when a query is submitted that is syntactically incorrect or does not pass additional validation.

**Fields**
+ **code** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The HTTP status code returned with the exception.
+ **detailedMessage** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  A detailed message describing the problem.
+ **requestId** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The ID of the malformed query request.

## MemoryLimitExceededException (structure)
<a name="MemoryLimitExceededException"></a>

Raised when a request fails because of insufficient memory resources. The request can be retried.

**Fields**
+ **code** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The HTTP status code returned with the exception.
+ **detailedMessage** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  A detailed message describing the problem.
+ **requestId** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The ID of the request that failed.

## MethodNotAllowedException (structure)
<a name="MethodNotAllowedException"></a>

Raised when the HTTP method used by a request is not supported by the endpoint being used.

**Fields**
+ **code** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The HTTP status code returned with the exception.
+ **detailedMessage** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  A detailed message describing the problem.
+ **requestId** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The ID of the request in question.

## MissingParameterException (structure)
<a name="MissingParameterException"></a>

Raised when a required parameter is missing.

**Fields**
+ **code** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The HTTP status code returned with the exception.
+ **detailedMessage** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  A detailed message describing the problem.
+ **requestId** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The ID of the request in which the parameter is missing.

## MLResourceNotFoundException (structure)
<a name="MLResourceNotFoundException"></a>

Raised when a specified machine-learning resource could not be found.

**Fields**
+ **code** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The HTTP status code returned with the exception.
+ **detailedMessage** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  A detailed message describing the problem.
+ **requestId** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The ID of the request in question.

## ParsingException (structure)
<a name="ParsingException"></a>

Raised when a parsing issue is encountered.

**Fields**
+ **code** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The HTTP status code returned with the exception.
+ **detailedMessage** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  A detailed message describing the problem.
+ **requestId** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The ID of the request in question.

## PreconditionsFailedException (structure)
<a name="PreconditionsFailedException"></a>

Raised when a precondition for processing a request is not satisfied.

**Fields**
+ **code** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The HTTP status code returned with the exception.
+ **detailedMessage** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  A detailed message describing the problem.
+ **requestId** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The ID of the request in question.

## QueryLimitExceededException (structure)
<a name="QueryLimitExceededException"></a>

Raised when the number of active queries exceeds what the server can process. The query in question can be retried when the system is less busy.

**Fields**
+ **code** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The HTTP status code returned with the exception.
+ **detailedMessage** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  A detailed message describing the problem.
+ **requestId** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The ID of the request which exceeded the limit.

## QueryLimitException (structure)
<a name="QueryLimitException"></a>

Raised when the size of a query exceeds the system limit.

**Fields**
+ **code** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The HTTP status code returned with the exception.
+ **detailedMessage** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  A detailed message describing the problem.
+ **requestId** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The ID of the request that exceeded the limit.

## QueryTooLargeException (structure)
<a name="QueryTooLargeException"></a>

Raised when the body of a query is too large.

**Fields**
+ **code** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The HTTP status code returned with the exception.
+ **detailedMessage** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  A detailed message describing the problem.
+ **requestId** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The ID of the request that is too large.

## ReadOnlyViolationException (structure)
<a name="ReadOnlyViolationException"></a>

Raised when a request attempts to write to a read-only resource.

**Fields**
+ **code** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The HTTP status code returned with the exception.
+ **detailedMessage** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  A detailed message describing the problem.
+ **requestId** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The ID of the request in which the parameter is missing.

## S3Exception (structure)
<a name="S3Exception"></a>

Raised when there is a problem accessing Amazon S3.

**Fields**
+ **code** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The HTTP status code returned with the exception.
+ **detailedMessage** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  A detailed message describing the problem.
+ **requestId** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The ID of the request in question.

## ServerShutdownException (structure)
<a name="ServerShutdownException"></a>

Raised when the server shuts down while processing a request.

**Fields**
+ **code** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The HTTP status code returned with the exception.
+ **detailedMessage** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  A detailed message describing the problem.
+ **requestId** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The ID of the request in question.

## StatisticsNotAvailableException (structure)
<a name="StatisticsNotAvailableException"></a>

Raised when statistics needed to satisfy a request are not available.

**Fields**
+ **code** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The HTTP status code returned with the exception.
+ **detailedMessage** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  A detailed message describing the problem.
+ **requestId** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The ID of the request in question.

## StreamRecordsNotFoundException (structure)
<a name="StreamRecordsNotFoundException"></a>

Raised when stream records requested by a query cannot be found.

**Fields**
+ **code** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The HTTP status code returned with the exception.
+ **detailedMessage** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  A detailed message describing the problem.
+ **requestId** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The ID of the request in question.

## ThrottlingException (structure)
<a name="ThrottlingException"></a>

Raised when the rate of requests exceeds the maximum throughput. Requests can be retried after encountering this exception.

**Fields**
+ **code** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The HTTP status code returned with the exception.
+ **detailedMessage** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  A detailed message describing the problem.
+ **requestId** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The ID of the request that could not be processed for this reason.

## TimeLimitExceededException (structure)
<a name="TimeLimitExceededException"></a>

Raised when the an operation exceeds the time limit allowed for it.

**Fields**
+ **code** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The HTTP status code returned with the exception.
+ **detailedMessage** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  A detailed message describing the problem.
+ **requestId** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The ID of the request that could not be processed for this reason.

## TooManyRequestsException (structure)
<a name="TooManyRequestsException"></a>

Raised when the number of requests being processed exceeds the limit.

**Fields**
+ **code** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The HTTP status code returned with the exception.
+ **detailedMessage** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  A detailed message describing the problem.
+ **requestId** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The ID of the request that could not be processed for this reason.

## UnsupportedOperationException (structure)
<a name="UnsupportedOperationException"></a>

Raised when a request attempts to initiate an operation that is not supported.

**Fields**
+ **code** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The HTTP status code returned with the exception.
+ **detailedMessage** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  A detailed message describing the problem.
+ **requestId** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The ID of the request in question.

## UnloadUrlAccessDeniedException (structure)
<a name="UnloadUrlAccessDeniedException"></a>

Raised when access is denied to a URL that is an unload target.

**Fields**
+ **code** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The HTTP status code returned with the exception.
+ **detailedMessage** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  A detailed message describing the problem.
+ **requestId** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The ID of the request in question.