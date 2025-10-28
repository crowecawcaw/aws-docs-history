# Service job retry strategies in AWS Batch

Service job retry strategies allow AWS Batch to automatically retry failed service jobs under
specific conditions.

Service jobs may require multiple attempts for several reasons:

- **Temporary service issues**: Internal service errors,
  throttling, or temporary outages can cause jobs to fail during submission or
  execution.
- **Training initialization failures**: Issues during job
  startup, such as image pulling problems or initialization errors, may be resolved on
  retry.
  By configuring appropriate retry strategies, you can improve job success rates and reduce
  the need for manual intervention, especially for long-running training workloads.

###### Note

Service jobs automatically retry certain types of failures, such as insufficient capacity
errors, without consuming your configured retry attempts. Your retry strategy primarily
handles other types of failures such as algorithm errors or service issues.

## Configuring retry strategies

Service job retry strategies are configured using [ServiceJobRetryStrategy](../APIReference/API_ServiceJobRetryStrategy.md "../APIReference/API_ServiceJobRetryStrategy.md"), which supports both simple retry counts and conditional
retry logic.

### Retry configuration

The simplest retry strategy specifies the number of retry attempts that should be made
if a service job fails:

```
{
  "retryStrategy": {
    "attempts": 3
  }
}
```

This configuration allows the service job to be retried up to 3 times if it
fails.

###### Important

The `attempts` value represents the total number of times the job can be
placed in the `RUNNABLE` state, including the initial attempt. A value of 3
means the job will be attempted once initially, then retried up to 2 additional times if
it fails.

### Retry configuration with

evaluateOnExit

You can use the `evaluateOnExit` parameter to specify conditions under which
jobs should be retried or allowed to fail. This is useful for when different types of
failures require different handling.

The `evaluateOnExit` array can contain up to 5 retry strategies, each
specifying an action (`RETRY` or `EXIT`) and conditions based on
status reasons:

```
{
  "retryStrategy": {
    "attempts": 5,
    "evaluateOnExit": [
      {
        "action": "RETRY",
        "onStatusReason": "Received status from SageMaker: InternalServerError*"
      },
      {
        "action": "EXIT",
        "onStatusReason": "Received status from SageMaker: ValidationException*"
      },
      {
        "action": "EXIT",
        "onStatusReason": "*"
      }
    ]
  }
}
```

This configuration:

- Retries jobs that fail due to SageMaker AI internal server errors
- Immediately fails jobs that encounter validation exceptions (client errors that
  won't be resolved by retry)
- Includes a catch-all rule to exit for any other failure types

#### Status reason pattern matching

The `onStatusReason` parameter supports pattern matching with up to 512
characters. Patterns can use wildcards (\*) and match against status reasons returned by
SageMaker AI.

For service jobs, status messages from SageMaker AI are prefixed with "Received status from
SageMaker: " to distinguish them from AWS Batch-generated messages. Common patterns
include:

- `Received status from SageMaker: InternalServerError*` - Match internal
  service errors
- `Received status from SageMaker: ValidationException*` - Match client
  validation errors
- `Received status from SageMaker: ResourceLimitExceeded*` - Match
  resource limit errors
- `*CapacityError*` - Match capacity-related failures

###### Tip

Use specific pattern matching to handle different error types appropriately. For
example, retry internal server errors but immediately fail on validation errors that
indicate problems with job parameters.
