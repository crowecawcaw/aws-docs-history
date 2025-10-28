# Specify job configurations by using the

AWS IoT Jobs API

You can use the [CreateJob](../apireference/API_CreateJob.md "../apireference/API_CreateJob.md") or
the [CreateJobTemplate](../apireference/API_CreateJobTemplate.md "../apireference/API_CreateJobTemplate.md")
API to specify the different job configurations. The following sections describe how
to add these configurations. After you've added the configurations, you can use
[JobExecutionSummary](../apireference/API_JobExecutionSummary.md "../apireference/API_JobExecutionSummary.md") and [JobExecutionSummaryForJob](../apireference/API_JobExecutionSummaryForJob.md "../apireference/API_JobExecutionSummaryForJob.md") to view their status.

For more information about the different configurations and how they work, see
[How job configurations work](jobs-configurations-details.md "jobs-configurations-details.md").

## Rollout configuration

You can specify a constant rollout rate or an exponential rollout rate for
your rollout configuration.

- ###### Set a constant rollout rate

To set a constant rollout rate, use the [`JobExecutionsRolloutConfig`](../apireference/API_JobExecutionsRolloutConfig.md "../apireference/API_JobExecutionsRolloutConfig.md") object to
add the `maximumPerMinute` parameter to the
`CreateJob` request. This parameter specifies the
upper limit of the rate at which job executions can occur. This
value is optional and ranges from 1 to 1000. If you don't set the
value, it uses 1000 as the default value.

```
    "jobExecutionsRolloutConfig": {
        "maximumPerMinute": 1000
    }
```

- ###### Set an exponential rollout rate

To set a variable job rollout rate, use the [`JobExecutionsRolloutConfig`](../apireference/API_JobExecutionsRolloutConfig.md "../apireference/API_JobExecutionsRolloutConfig.md") object. You
can configure the
`ExponentialRolloutRate`property when you
run the `CreateJob` API operation. The following example
sets an exponential rollout rate by using the
`exponentialRate` parameter. For more information
about the parameters, see [`ExponentialRolloutRate`](../apireference/API_ExponentialRolloutRate.md "../apireference/API_ExponentialRolloutRate.md").

```
{
...
  "jobExecutionsRolloutConfig": {
    "exponentialRate": {
      "baseRatePerMinute": 50,
      "incrementFactor": 2,
      "rateIncreaseCriteria": {
        "numberOfNotifiedThings": 1000,
        "numberOfSucceededThings": 1000
      },
      "maximumPerMinute": 1000
    }
  }
...
}
```

Where the parameter:

**baseRatePerMinute**

Specifies the rate at which the jobs are executed until the
`numberOfNotifiedThings` or
`numberOfSucceededThings` threshold has been
met.

**incrementFactor**

Specifies the exponential factor by which the rollout rate
increases after the `numberOfNotifiedThings` or
`numberOfSucceededThings` threshold has been
met.

**rateIncreaseCriteria**

Specifies either the `numberOfNotifiedThings` or
`numberOfSucceededThings` threshold.

## Abort configuration

To add this configuration by using the API, specify the [`AbortConfig`](../apireference/API_AbortConfig.md "../apireference/API_AbortConfig.md")
parameter when you run the [`CreateJob`](../apireference/API_CreateJob.md "../apireference/API_CreateJob.md"), or the [`CreateJobTemplate`](../apireference/API_CreateJobTemplate.md "../apireference/API_CreateJobTemplate.md") API operation. The following example
shows an abort configuration for a job rollout that was experiencing multiple
failed executions, as specified with the `CreateJob` API
operation.

###### Note

Deleting a job execution affects the computation value of the total
completed execution. When a job aborts, the service creates an automated
`comment` and `reasonCode` to differentiate a
user-driven cancellation from a job abort cancellation.

```
   "abortConfig": {
      "criteriaList": [
         {
            "action": "CANCEL",
            "failureType": "FAILED",
            "minNumberOfExecutedThings": 100,
            "thresholdPercentage": 20
         },
         {
            "action": "CANCEL",
            "failureType": "TIMED_OUT",
            "minNumberOfExecutedThings": 200,
            "thresholdPercentage": 50
         }
      ]
    }
```

Where the parameter:

**action**

Specifies the action to take when the abort criteria has been met.
This parameter is required, and `CANCEL` is the only
valid value.

**failureType**

Specifies which failure types should initiate a job abort. Valid
values are `FAILED`, `REJECTED`,
`TIMED_OUT`, and `ALL`.

**minNumberOfExecutedThings**

Specifies the number of completed job executions that must occur
before the job abort criteria has been met. In this example, AWS IoT
doesn't check to see if a job abort should occur until at least 100
devices have completed job executions.

**thresholdPercentage**

Specifies the total number of things for which jobs are executed
that can initiate a job abort. In this example, AWS IoT checks
sequentially and initiates a job abort if the threshold percentage
is met. If at least 20% of the complete executions failed after 100
executions are complete, it cancels the job rollout. If this
criteria isn't met, AWS IoT then checks if at least 50% of completed
executions timed out after 200 executions are complete. If this is
the case, it cancels the job rollout.

## Scheduling configuration

To add this configuration by using the API, specify the optional [`SchedulingConfig`](../apireference/API_SchedulingConfig.md "../apireference/API_SchedulingConfig.md") when you run the [`CreateJob`](../apireference/API_CreateJob.md "../apireference/API_CreateJob.md"), or the
[`CreateJobTemplate`](../apireference/API_CreateJobTemplate.md "../apireference/API_CreateJobTemplate.md") API operation.

```
    "SchedulingConfig": {
      "endBehavior": string
      "endTime": string
      "maintenanceWindows": string
      "startTime": string
   }
```

Where the parameter:

**startTime**

Specifies the date and time when the job will start.

**endTime**

Specifies the date and time when the job will end.

**maintenanceWindows**Specifies if an optional maintenance window was selected for the scheduled job to rollout the
job document to all devices in the target group. The string format
for `maintenanceWindow` is YYYY/MM/DD for the date and
hh:mm for the time.

**endBehavior**

Specifies the job behavior for a scheduled job upon reaching the
`endTime`.

###### Note

The optional `SchedulingConfig` for a job is viewable in the
[`DescribeJob`](../apireference/API_DescribeJob.md "../apireference/API_DescribeJob.md") and [`DescribeJobTemplate`](../apireference/API_DescribeJobTemplate.md "../apireference/API_DescribeJobTemplate.md") APIs.

## Timeout configuration

To add this configuration by using the API, specify the [`TimeoutConfig`](../apireference/API_TimeoutConfig.md "../apireference/API_TimeoutConfig.md")
parameter when you run the [`CreateJob`](../apireference/API_CreateJob.md "../apireference/API_CreateJob.md"), or the [`CreateJobTemplate`](../apireference/API_CreateJobTemplate.md "../apireference/API_CreateJobTemplate.md") API operation.

To use the timeout configuration

1. To set the in-progress timer when you're creating a job or job
   template, set a value for the `inProgressTimeoutInMinutes`
   property of the optional [TimeoutConfig](../apireference/API_TimeoutConfig.md "../apireference/API_TimeoutConfig.md") object.

```
    "timeoutConfig": {
      "inProgressTimeoutInMinutes": number
   }
```

2. To specify a step timer for a job execution, set a value for
   `stepTimeoutInMinutes` when you call [UpdateJobExecution](../apireference/API_iot-jobs-data_UpdateJobExecution.md "../apireference/API_iot-jobs-data_UpdateJobExecution.md"). The step timer applies only to the job
   execution that you update. You can set a new value for this timer each
   time you update a job execution.

###### Note

`UpdateJobExecution` can discard a step timer that's
already been created by creating a new step timer with a value of
-1.

```
{
   ...
    "statusDetails": {
      "string" : "string"
   },
   "stepTimeoutInMinutes": number
}
```

3. To create a new step timer, you can also call the [StartNextPendingJobExecution](../apireference/API_iot-jobs-data_StartNextPendingJobExecution.md "../apireference/API_iot-jobs-data_StartNextPendingJobExecution.md") API operation.

## Retry configuration

###### Note

When you're creating a job, consider the appropriate number of retries to
use for your configuration. To avoid incurring excess costs because of
potential retry failures, add an abort configuration. After a job has been
created, the number of retries can't be updated. You can only set the number
of retries to 0 by using the [UpdateJob](../apireference/API_UpdateJob.md "../apireference/API_UpdateJob.md") API operation.

To add this configuration by using the API, specify the [`jobExecutionsRetryConfig`](../apireference/API_jobExecutionsRetryConfig.md "../apireference/API_jobExecutionsRetryConfig.md") parameter when you run
the [`CreateJob`](../apireference/API_CreateJob.md "../apireference/API_CreateJob.md"),
or the [`CreateJobTemplate`](../apireference/API_CreateJobTemplate.md "../apireference/API_CreateJobTemplate.md") API operation.

```
{
...
  "jobExecutionsRetryConfig": {
      "criteriaList": [
         {
            "failureType": "string",
            "numberOfRetries": number
         }
      ]
  }
...
}
```

Where **criteriaList** is an array specifying the
list of criteria that determines the number of retries permitted for each
failure type for a job.
