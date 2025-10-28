# Retry Policy for Pipeline Steps

Retry policies help you automatically retry your Pipelines steps after an error occurs. Any
pipeline step can encounter exceptions, and exceptions happen for various reasons. In some
cases, a retry can resolve these issues. With a retry policy for pipeline steps, you can choose
whether to retry a particular pipeline step or not.

The retry policy only supports the following pipeline steps:

- [Processing step](build-and-manage-steps-types.md#step-type-processing "build-and-manage-steps-types.md#step-type-processing")
- [Training step](build-and-manage-steps-types.md#step-type-training "build-and-manage-steps-types.md#step-type-training")
- [Tuning step](build-and-manage-steps-types.md#step-type-tuning "build-and-manage-steps-types.md#step-type-tuning")
- [AutoML step](build-and-manage-steps-types.md#step-type-automl "build-and-manage-steps-types.md#step-type-automl")
- [Create model step](build-and-manage-steps-types.md#step-type-create-model "build-and-manage-steps-types.md#step-type-create-model")
- [Register model step](build-and-manage-steps-types.md#step-type-register-model "build-and-manage-steps-types.md#step-type-register-model")
- [Transform step](build-and-manage-steps-types.md#step-type-transform "build-and-manage-steps-types.md#step-type-transform")
- [Notebook job step](build-and-manage-steps-types.md#step-type-notebook-job "build-and-manage-steps-types.md#step-type-notebook-job")

###### Note

Jobs running inside both the tuning and AutoML steps conduct retries internally and will
not retry the `SageMaker.JOB_INTERNAL_ERROR` exception type, even if a retry policy
is configured. You can program your own [Retry Strategy](../APIReference/API_RetryStrategy.md "../APIReference/API_RetryStrategy.md") using the
SageMaker API.

## Supported exception types for

the retry policy

The retry policy for pipeline steps supports the following exception types:

- `Step.SERVICE_FAULT`: These exceptions occur when an internal server error
  or transient error happens when calling downstream services. Pipelines retries on this type of
  error automatically. With a retry policy, you can override the default retry operation for
  this exception type.
- `Step.THROTTLING`: Throttling exceptions can occur while calling the
  downstream services. Pipelines retries on this type of error automatically. With a retry
  policy, you can override the default retry operation for this exception type.
- `SageMaker.JOB_INTERNAL_ERROR`: These exceptions occur when the SageMaker AI job
  returns `InternalServerError`. In this case, starting a new job may fix a
  transient issue.
- `SageMaker.CAPACITY_ERROR`: The SageMaker AI job may encounter Amazon EC2
  `InsufficientCapacityErrors`, which leads to the SageMaker AI job’s failure. You can
  retry by starting a new SageMaker AI job to avoid the issue.
- `SageMaker.RESOURCE_LIMIT`: You can exceeed the resource limit quota when
  running a SageMaker AI job. You can wait and retry running the SageMaker AI job after a short period and
  see if resources are released.

## The JSON schema for the retry

policy

The retry policy for Pipelines has the following JSON schema:

```
"RetryPolicy": {
   "ExceptionType": [String]
   "IntervalSeconds": Integer
   "BackoffRate": Double
   "MaxAttempts": Integer
   "ExpireAfterMin": Integer
}
```

- `ExceptionType`: This field requires the following exception types in a
  string array format.
  - `Step.SERVICE_FAULT`
  - `Step.THROTTLING`
  - `SageMaker.JOB_INTERNAL_ERROR`
  - `SageMaker.CAPACITY_ERROR`
  - `SageMaker.RESOURCE_LIMIT`

- `IntervalSeconds` (optional): The number of seconds before the first retry
  attempt (1 by default). `IntervalSeconds` has a maximum value of 43200 seconds
  (12 hours).
- `BackoffRate` (optional): The multiplier by which the retry interval
  increases during each attempt (2.0 by default).
- `MaxAttempts` (optional): A positive integer that represents the maximum
  number of retry attempts (5 by default). If the error recurs more times than
  `MaxAttempts` specifies, retries cease and normal error handling resumes. A
  value of 0 specifies that errors are never retried. `MaxAttempts` has a maximum
  value of 20.
- `ExpireAfterMin` (optional): A positive integer that represents the maximum
  timespan of retry. If the error recurs after `ExpireAfterMin` minutes counting
  from the step gets executed, retries cease and normal error handling resumes. A value of 0
  specifies that errors are never retried. `ExpireAfterMin` has a maximum value
  of 14,400 minutes (10 days).

###### Note

Only one of `MaxAttempts` or `ExpireAfterMin` can be given,
but not both; if both are _not_ specified, `MaxAttempts`
becomes the default. If both properties are identified within one policy, then the retry
policy generates a validation error.
