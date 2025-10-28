# Using job retry policies

In Amazon EMR on EKS versions 6.9.0 and later, you can set a retry policy for your job runs. Retry
policies cause a job driver pod to be restarted automatically if it fails or is deleted. This
makes long-running Spark streaming jobs more resilient to failures.

## Setting a retry policy for a job

To configure a retry policy, you provide a `RetryPolicyConfiguration` field
using the [StartJobRun](../../../emr-on-eks/latest/APIReference/API_StartJobRun.md "../../../emr-on-eks/latest/APIReference/API_StartJobRun.md") API. An
example `retryPolicyConfiguration` is shown here:

```
aws emr-containers start-job-run \
--virtual-cluster-id cluster_id \
--name sample-job-name \
--execution-role-arn execution-role-arn \
--release-label emr-6.9.0-latest \
--job-driver '{
  "sparkSubmitJobDriver": {
    "entryPoint": "local:///usr/lib/spark/examples/src/main/python/pi.py",
    "entryPointArguments": [ "2" ],
    "sparkSubmitParameters": "--conf spark.executor.instances=2 --conf spark.executor.memory=2G --conf spark.executor.cores=2 --conf spark.driver.cores=1"
  }
}' \
--retry-policy-configuration '{
    "maxAttempts": 5
  }' \
--configuration-overrides '{
  "monitoringConfiguration": {
    "cloudWatchMonitoringConfiguration": {
      "logGroupName": "my_log_group_name",
      "logStreamNamePrefix": "my_log_stream_prefix"
    },
    "s3MonitoringConfiguration": {
       "logUri": "s3://amzn-s3-demo-logging-bucket"
    }
  }
}'
```

###### Note

`retryPolicyConfiguration` is only available from AWS CLI 1.27.68 version
onwards. To update the AWS CLI to the latest version, see [Installing or updating the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md")

Configure the `maxAttempts` field with the maximum number of times you want
the job driver pod to be restarted if it fails or is deleted. The execution interval between
two job driver retry attempts is an exponential retry interval of (10 seconds, 20 seconds,
40 seconds ...) which is capped at 6 minutes, as described in the [Kubernetes documentation](https://kubernetes.io/docs/concepts/workloads/controllers/job/#pod-backoff-failure-policy "https://kubernetes.io/docs/concepts/workloads/controllers/job/#pod-backoff-failure-policy").

###### Note

Every additional job driver execution will be billed as another job run, and will be
subject to [Amazon EMR on EKS
pricing](https://aws.amazon.com/emr/pricing/#Amazon_EMR_on_Amazon_EKS "https://aws.amazon.com/emr/pricing/#Amazon_EMR_on_Amazon_EKS").

### Retry policy configuration values

- **Default retry policy for a job:**
  `StartJobRun` includes a retry policy set to 1 maximum attempt by default.
  You can configure the retry policy as desired.

###### Note

If `maxAttempts` of the `retryPolicyConfiguration` is set
to 1, it means that no retries will be done to bring up the driver pod on
failure.

- **Disabling retry policy for a job:** To disable a
  retry policy, set the max attempts value in retryPolicyConfiguration to 1.

```
"retryPolicyConfiguration": {
    "maxAttempts": 1
}
```

- **Set maxAttempts for a job within the valid range:**
  `StartJobRun` call will fail if the `maxAttempts` value is
  outside the valid range. The valid `maxAttempts` range is from 1 to
  2,147,483,647 (32-bit integer), the range supported for Kubernetes'
  `backOffLimit` configuration setting. For more information, see [Pod backoff failure policy](https://kubernetes.io/docs/concepts/workloads/controllers/job/#pod-backoff-failure-policy "https://kubernetes.io/docs/concepts/workloads/controllers/job/#pod-backoff-failure-policy") in the Kubernetes documentation. If the
  `maxAttempts` value is invalid, the following error message is
  returned:

```
{
 "message": "Retry policy configuration's parameter value of maxAttempts is invalid"
}
```

## Retrieving a retry policy status for a job

You can view the status of the retry attempts for a job with the [`ListJobRuns`](../../../emr-on-eks/latest/APIReference/API_ListJobRuns.md "../../../emr-on-eks/latest/APIReference/API_ListJobRuns.md") and [`DescribeJobRun`](../../../emr-on-eks/latest/APIReference/API_DescribeJobRun.md "../../../emr-on-eks/latest/APIReference/API_DescribeJobRun.md") APIs. Once you request a job with an enabled retry
policy configuration, the `ListJobRun` and `DescribeJobRun` responses
will contain the status of the retry policy in the `RetryPolicyExecution` field.
In addition, the `DescribeJobRun` response will contain the
`RetryPolicyConfiguration` that was input in the `StartJobRun`
request for the job.

**Sample responses**

ListJobRuns response

```
{
  "jobRuns": [
    ...
    ...
    "retryPolicyExecution" : {
      "currentAttemptCount": 2
    }
    ...
    ...
  ]
}
```

DescribeJobRun response

```
{
  ...
  ...
  "retryPolicyConfiguration": {
    "maxAttempts": 5
   },
   "retryPolicyExecution" : {
    "currentAttemptCount": 2
  },
  ...
  ...
}
```

These fields will not be visible when retry policy is disabled in the job, as described
below in [Retry policy configuration values](#retry-config "#retry-config").

## Monitoring a job with a retry policy

When you enable a retry policy, a CloudWatch event is generated for every job driver that is
created. To subscribe to these events, set up a CloudWatch event rule using the following
command:

```
aws events put-rule \
--name cwe-test \
--event-pattern '{"detail-type": ["EMR Job Run New Driver Attempt"]}'
```

The event will return information on the `newDriverPodName`,
`newDriverCreatedAt` timestamp, `previousDriverFailureMessage`, and
`currentAttemptCount` of the job drivers. These events will not be created if
the retry policy is disabled.

For more information on how to monitor your job with CloudWatch events, see [Monitor jobs with Amazon CloudWatch Events](monitoring.md#monitoring-cloudwatch-events "monitoring.md#monitoring-cloudwatch-events").

## Finding logs for drivers and executors

Driver pod names follow the format `spark-<job
 id>-driver-<random-suffix>`. The same `random-suffix` is added
to the executor pod names that the driver spawns. When you use this
`random-suffix`, you can find logs for a driver and its associated executors.
The `random-suffix` is only present if the [retry
policy is enabled](#retry-config "#retry-config") for the job; otherwise, the `random-suffix` is
absent.

For more information on how to configure jobs with monitoring configuration for logging,
see [Run a Spark application](getting-started.md#getting-started-run-spark-app "getting-started.md#getting-started-run-spark-app").
