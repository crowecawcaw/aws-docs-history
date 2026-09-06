

# Service job retry strategies in AWS Batch
<a name="service-job-retries"></a>

Service job retry strategies allow AWS Batch to automatically retry failed service jobs under specific conditions.

Service jobs may require multiple attempts for several reasons:
+ **Temporary service issues**: Internal service errors, throttling, or temporary outages can cause jobs to fail during submission or execution.
+ **Training initialization failures**: Issues during job startup, such as image pulling problems or initialization errors, may be resolved on retry.

By configuring appropriate retry strategies, you can improve job success rates and reduce the need for manual intervention, especially for long-running training workloads.

**Note**  
When a SageMaker Training job fails due to insufficient capacity, AWS Batch retries the job automatically until capacity becomes available. The most recent SageMaker Training job that failed due to insufficient capacity will be retained, and earlier SageMaker Training jobs that failed due to insufficient capacity will be deleted on a best-effort basis.  
These capacity-based retries don't consume your configured retry attempts. Your retry strategy primarily handles other types of failures such as algorithm errors or service issues that occur after a job enters `STARTING`.

## Configuring retry strategies
<a name="configuring-service-job-retries"></a>

Service job retry strategies are configured using [ServiceJobRetryStrategy](https://docs.aws.amazon.com/batch/latest/APIReference/API_ServiceJobRetryStrategy.html), which supports both simple retry counts and conditional retry logic.

### Retry configuration
<a name="basic-retry-configuration"></a>

The simplest retry strategy specifies the number of retry attempts that should be made if a service job fails:

```
{
  "retryStrategy": {
    "attempts": 3
  }
}
```

This configuration allows the service job to be retried up to 3 times if it fails.

**Important**  
The `attempts` value represents the total number of times the job can be placed in the `RUNNABLE` state, including the initial attempt. A value of 3 means the job will be attempted once initially, then retried up to 2 additional times if it fails.

### Retry configuration with evaluateOnExit
<a name="advanced-retry-configuration"></a>

You can use the `evaluateOnExit` parameter to specify conditions under which jobs should be retried or allowed to fail. This is useful for when different types of failures require different handling.

The `evaluateOnExit` array can contain up to 5 retry strategies, each specifying an action (`RETRY` or `EXIT`) and conditions based on status reasons:

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
+ Retries jobs that fail due to SageMaker AI internal server errors
+ Immediately fails jobs that encounter validation exceptions (client errors that won't be resolved by retry)
+ Includes a catch-all rule to exit for any other failure types

#### Status reason pattern matching
<a name="status-reason-patterns"></a>

The `onStatusReason` parameter supports pattern matching with up to 512 characters. Patterns can use wildcards (\*) and match against status reasons returned by SageMaker AI.

For service jobs, status messages from SageMaker AI are prefixed with "Received status from SageMaker: " to distinguish them from AWS Batch-generated messages. Common patterns include:
+ `Received status from SageMaker: InternalServerError*` - Match internal service errors
+ `Received status from SageMaker: ValidationException*` - Match client validation errors
+ `Received status from SageMaker: ResourceLimitExceeded*` - Match resource limit errors
+ `*CapacityError*` - Match capacity-related failures

**Tip**  
Use specific pattern matching to handle different error types appropriately. For example, retry internal server errors but immediately fail on validation errors that indicate problems with job parameters.