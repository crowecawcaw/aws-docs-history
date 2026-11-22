

# Running EMR Serverless jobs on spare capacity with Flex

EMR Serverless Flex is an execution option that runs Spark batch job runs on spare compute capacity at a discounted rate. When you enable Flex for a job run, EMR Serverless runs the Spark executors on spare capacity and the Spark driver on a Standard worker. EMR Serverless selects the capacity, handles reclamation of spare capacity, and retries affected tasks on your behalf. You add one parameter when you submit the job run. You don't configure instance fleets or Spark decommissioning settings. For pricing information, refer to the [Amazon EMR Pricing](https://aws.amazon.com/emr/pricing/) page.

Because spare capacity can be reclaimed, Flex job runs can take longer to start and complete than job runs on Standard, the default execution option. Use Flex for fault-tolerant workloads where cost matters more than predictable execution time, such as nightly batch ETL, backfills, one-time data loads, recurring reports, and development, test, or pre-production runs. Keep workloads with strict completion deadlines on Standard.

Flex supports Spark batch job runs on both the x86\_64 and arm64 architectures. You can run Flex and Standard job runs on the same application.

**Default behavior**

Flex is turned off by default. Job runs use Standard unless you explicitly enable Flex for the job run.

## Enabling Flex
<a name="jobs-flex-execution-enable"></a>

You enable Flex per job run with the `flexExecution` parameter of the `StartJobRun` API. Specify the parameter each time that you submit a job run. You don't need to change how you create your application.

The following AWS CLI command starts a Flex job run:

```bash
aws emr-serverless start-job-run \
    --application-id {{application-id}} \
    --execution-role-arn {{execution-role-arn}} \
    --flex-execution '{
        "enabled": true
    }' \
    --job-driver '{
        "sparkSubmit": {
            "entryPoint": "s3://{{amzn-s3-demo-bucket}}/scripts/my-job.py"
        }
    }'
```

In EMR Studio, select **Enable Flex execution** when you submit a job run.

To confirm whether a job run used Flex, check the `flexExecution` field that `GetJobRun`, `ListJobRuns`, and `ListJobRunAttempts` return.

## Built-in resiliency features
<a name="jobs-flex-execution-resiliency"></a>

Spare capacity can be reclaimed when it's needed elsewhere, which interrupts the affected Flex workers. Flex includes the following built-in resiliency features to reduce the impact of these interruptions. EMR Serverless applies them to every Flex job run, so you don't need to configure instance fleets, Availability Zones, or Spark decommissioning settings.
+ Availability Zone selection – EMR Serverless evaluates spare capacity across the Availability Zones in the AWS Region and places workers where the most spare capacity is available. This reduces the chance that a single reclamation event affects a large share of your executors.
+ Instance diversification – EMR Serverless spreads executors across multiple instance families and generations, so that reclamation of one instance type doesn't affect all workers at once.
+ Driver protection – The Spark driver runs on a Standard worker that isn't subject to spare capacity reclamation. The driver holds the job state, so protecting it prevents an interruption from failing the job run. Only executors run on Flex workers.
+ Graceful decommissioning – A Flex worker receives a reclamation notice two minutes before it's reclaimed. EMR Serverless then stops scheduling new tasks on that worker, excludes it from future task assignments, and migrates shuffle and cache data off the worker.
+ Automatic task retry – Spark retries the affected tasks on healthy Flex workers within the same job run. The job run continues without manual intervention.
+ Shuffle offload (optional) – If you use [Using serverless storage for Amazon EMR Serverless](jobs-serverless-storage.md), retried tasks read stored shuffle output instead of recomputing upstream stages.

Interruptions can still increase the time that a job run takes to complete, especially for shuffle-heavy jobs that must recompute upstream stages.

## Understanding Flex billing
<a name="jobs-flex-execution-billing"></a>
+ Flex workers are billed at a discounted rate for vCPU-hours and memory GB-hours compared to Standard workers. The discount is fixed and doesn't change with supply and demand.
+ The Spark driver runs on a Standard worker and is billed at the Standard rate. Storage is billed at the standard rate.
+ Each worker is billed for the time that it was part of the job run, in per-second increments with a one-minute minimum. You aren't billed for a Flex worker after it's reclaimed.
+ Flex usage appears as separate line items on your bill and in AWS Cost Explorer. Flex also works with [Enabling Job Level Cost Allocation](jobs-job-level-cost-allocation.md).

For rates, refer to the [Amazon EMR Pricing](https://aws.amazon.com/emr/pricing/) page.

## Recommended best practices for Flex
<a name="jobs-flex-execution-best-practices"></a>
+ Avoid the top of the hour – Spare capacity is less available when many jobs start at the same time at the top of the hour. Shift job start times by a few minutes, for example to 9:20 instead of 9:00, to improve the chance of a fast start.
+ Run outside business hours – Spare capacity is most available when overall compute demand is lower, such as in the evening in the AWS Region or on weekends.
+ Use serverless storage – With [Using serverless storage for Amazon EMR Serverless](jobs-serverless-storage.md), shuffle data is written to remote storage instead of local disk. When tasks from a reclaimed worker are retried, they read the stored shuffle output instead of recomputing upstream stages. This reduces the runtime impact of reclamation on shuffle-heavy jobs.
+ Plan a fallback to Standard – In the rare case that a Flex job run fails, Flex doesn't automatically fall back to Standard. If your jobs are idempotent, configure your orchestrator, such as Amazon Managed Workflows for Apache Airflow or AWS Step Functions (using the AWS SDK service integration), to catch a failed Flex job run and resubmit it without Flex.

## Considerations and limitations
<a name="jobs-flex-execution-considerations"></a>
+ Flex supports only Spark batch job runs. Hive job runs, Spark Structured Streaming job runs, and interactive sessions, such as Livy and Spark Connect, aren't supported.
+ Flex is configured per job run. You can't set it as an application-level default.
+ Flex job runs can take longer to start when spare capacity isn't immediately available. If no executor joins the driver within 20 minutes of the job run start, the job run fails.
+ In the rare case that a Flex job run fails, EMR Serverless doesn't automatically fall back to Standard. To rerun the job, resubmit it with or without Flex. For more information, refer to [Recommended best practices for Flex](#jobs-flex-execution-best-practices).
+ Flex workers count against a separate service quota, **Max concurrent Flex vCPUs per account**. This quota is independent of the **Max concurrent vCPUs per account** quota for Standard. For the default value, refer to [Service quotas](endpoints-quotas.md#quotas). If starting a Flex job run would exceed the **Max concurrent Flex vCPUs per account** quota, the job run fails with a service quota error. To run more Flex job runs concurrently, wait for running Flex job runs to finish, or request a quota increase through Service Quotas.
+ The availability of spare capacity varies over time and by AWS Region. Flex doesn't guarantee that capacity is available when you submit a job run.
+ Flex is available in all AWS Regions where EMR Serverless is available, including AWS GovCloud (US) Regions, except the China Regions.
+ Flex executors don't support workers with 1 or 2 vCPUs. If a Flex job run requests executors of these sizes, `StartJobRun` rejects the request. This limit doesn't apply to the driver, which runs on a Standard worker.
+ Flex executors don't use pre-initialized capacity. If your application has pre-initialized capacity, the driver of a Flex job run can use it, because the driver runs on a Standard worker. For more information, refer to [Pre-initialized capacity for working with an application in EMR Serverless](pre-init-capacity.md).
+ The application's maximum capacity (`maximumCapacity`) is a single setting that applies to the combined capacity of Standard and Flex workers. Flex doesn't have a separate maximum capacity setting. When you set the maximum capacity for an application that runs both Flex and Standard job runs, account for both. For more information, refer to [Maximum capacity](app-behavior.md#max-capacity).
+ The `totalResourceUtilization` and `billedResourceUtilization` values for a job run combine the usage of Standard and Flex workers. These values report resource usage, not cost, and don't separate Flex usage from Standard usage.
+ The AWS Step Functions optimized integration for EMR Serverless doesn't support Flex. To submit Flex job runs from a Step Functions state machine, use the AWS SDK service integration to call the `StartJobRun` API (`arn:aws:states:::aws-sdk:emrserverless:startJobRun`) with the `flexExecution` parameter.
+ Flex job runs are reported in separate CloudWatch job-level metrics, and Flex executors are reported with the `FlexCapacity` capacity allocation type. For more information, refer to [Monitoring EMR Serverless applications and jobs](app-job-metrics.md).