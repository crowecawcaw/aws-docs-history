# Monitoring EMR Serverless applications and

jobs

With Amazon CloudWatch metrics for EMR Serverless, you can
receive 1-minute CloudWatch metrics and access CloudWatch dashboards to access near-real-time
operations and performance of your EMR Serverless applications.

EMR Serverless sends metrics to CloudWatch every minute.
EMR Serverless emits these metrics
at the application level as well as the job, worker-type, and capacity-allocation-type levels.

To get started, use the EMR Serverless CloudWatch dashboard template
provided in the [EMR Serverless GitHub repository](https://github.com/aws-samples/emr-serverless-samples/tree/main/cloudformation/emr-serverless-cloudwatch-dashboard/ "https://github.com/aws-samples/emr-serverless-samples/tree/main/cloudformation/emr-serverless-cloudwatch-dashboard/") and deploy it.

###### Note

[EMR Serverless interactive
workloads](interactive-workloads.md "interactive-workloads.md") have only application-level monitoring enabled, and have a
new worker type dimension, `Spark_Kernel`. To monitor and debug your
interactive workloads, access the logs and Apache Spark UI from [within your EMR Studio Workspace](../ManagementGuide/emr-studio-debug.md#emr-studio-debug-serverless "../ManagementGuide/emr-studio-debug.md#emr-studio-debug-serverless").

## Monitoring metrics

###### Important

We are restructuring our metrics display to add `ApplicationName` and `JobName` as dimensions. For release 7.10 and later, the older
metrics will no longer be updated. For EMR releases below 7.10, the older metrics are still available.

**Current dimensions**

The table below describes the EMR Serverless dimensions available within the `AWS/EMR Serverless` namespace.

| Dimensions for EMR Serverless metrics | Dimension                                                                                                                                                                                  | Description |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| `ApplicationId`                       | Filters for all metrics of an EMR Serverless application using the application ID.                                                                                                         |
| `ApplicationName`                     | Filters for all metrics of an EMR Serverless application using the name. If the name isn't provided, or contains non-ASCII<br>characters, it is published as **[Unspecified]**.            |
| `JobId`                               | Filters for all metrics of an EMR Serverless the job run ID.                                                                                                                               |
| `JobName`                             | Filters for all metrics of an EMR Serverless job run using the name. If the name isn't provided, or contains non-ASCII<br>characters, it is published as **[Unspecified]**.                |
| `WorkerType`                          | Filters for all metrics of a given worker type. For example, you can filter for<br>`SPARK_DRIVER` and `SPARK_EXECUTORS` for Spark jobs.                                                    |
| `CapacityAllocationType`              | Filters for all metrics of a given capacity allocation type. For example, you can filter for `PreInitCapacity` for pre-initialized capacity<br>and `OnDemandCapacity` for everything else. |

## Application-level monitoring

You can monitor capacity usage at the EMR Serverless application level with
Amazon CloudWatch metrics. You can also set up a single display to monitor application capacity usage in a CloudWatch dashboard.

| EMR Serverless application metrics | Metric                                                    | Description    | Unit                                                                          | Dimension |
| ---------------------------------- | --------------------------------------------------------- | -------------- | ----------------------------------------------------------------------------- | --------- |
| `MaxCPUAllowed`                    | The maximum CPU allowed for the application.              | vCPU           | `ApplicationId`, `ApplicationName`                                            |
| `MaxMemoryAllowed`                 | The maximum memory in GB allowed for the<br>application.  | Gigabytes (GB) | `ApplicationId`, `ApplicationName`                                            |
| `MaxStorageAllowed`                | The maximum storage in GB allowed for the<br>application. | Gigabytes (GB) | `ApplicationId`, `ApplicationName`                                            |
| `CPUAllocated`                     | The total numbers of vCPUs allocated.                     | vCPU           | `ApplicationId`, `ApplicationName`, `WorkerType`,<br>`CapacityAllocationType` |
| `IdleWorkerCount`                  | The number of total workers idle.                         | Count          | `ApplicationId`, `ApplicationName`, `WorkerType`,<br>`CapacityAllocationType` |
| `MemoryAllocated`                  | The total memory in GB allocated.                         | Gigabytes (GB) | `ApplicationId`, `ApplicationName`, `WorkerType`,<br>`CapacityAllocationType` |
| `PendingCreationWorkerCount`       | The number of total workers pending creation.             | Count          | `ApplicationId`, `ApplicationName`, `WorkerType`,<br>`CapacityAllocationType` |
| `RunningWorkerCount`               | The number of total workers in use by the<br>application. | Count          | `ApplicationId`, `ApplicationName`, `WorkerType`,<br>`CapacityAllocationType` |
| `StorageAllocated`                 | The total disk storage in GB allocated.                   | Gigabytes (GB) | `ApplicationId`, `ApplicationName`, `WorkerType`,<br>`CapacityAllocationType` |
| `TotalWorkerCount`                 | The number of total workers available.                    | Count          | `ApplicationId`, `ApplicationName`, `WorkerType`,<br>`CapacityAllocationType` |

## Job-level monitoring

Amazon EMR Serverless sends the following job-level metrics to
Amazon CloudWatch every one minute. You can access the metric values for
aggregate job runs by job run state. The unit for each of the metrics is
_count_.

| EMR Serverless job-level metrics | Metric                                       | Description                        | Dimension |
| -------------------------------- | -------------------------------------------- | ---------------------------------- | --------- |
| `SubmittedJobs`                  | The number of jobs in a Submitted state.     | `ApplicationId`, `ApplicationName` |
| `PendingJobs`                    | The number of jobs in a Pending state.       | `ApplicationId`, `ApplicationName` |
| `ScheduledJobs`                  | The number of jobs in a Scheduled state.     | `ApplicationId`, `ApplicationName` |
| `RunningJobs`                    | The number of jobs in a Running state.       | `ApplicationId`, `ApplicationName` |
| `SuccessJobs`                    | The number of jobs in a Success state.       | `ApplicationId`, `ApplicationName` |
| `FailedJobs`                     | The number of jobs in a Failed state.        | `ApplicationId`, `ApplicationName` |
| `CancellingJobs`                 | The number of jobs in a Cancelling<br>state. | `ApplicationId`, `ApplicationName` |
| `CancelledJobs`                  | The number of jobs in a Cancelled state.     | `ApplicationId`, `ApplicationName` |

You can monitor engine-specific metrics for running and completed
EMR Serverless jobs with engine-specific application UIs. When you access the UI
for a running job, the live application UI displays with real-time updates. When
you access the UI for a completed job, the persistent app UI displays.

**Running jobs**

For your running EMR Serverless jobs, access a real-time interface that
provides engine-specific metrics. You can use either the Apache Spark UI or the
Hive Tez UI to monitor and debug your jobs. To access these UIs, use the
EMR Studio console or request a secure URL endpoint with the
AWS Command Line Interface.

**Completed jobs**

For your completed EMR Serverless jobs, use the Spark History Server
or the Persistent Hive Tez UI to access jobs details, stages, tasks, and metrics
for Spark or Hive jobs runs. To access these UIs, use the EMR Studio
console, or request a secure URL endpoint with the AWS Command Line Interface.

## Job worker-level monitoring

Amazon EMR Serverless sends the following job worker level metrics that are available in the `AWS/EMRServerless` namespace and `Job Worker Metrics` metric group to Amazon CloudWatch.
EMR Serverless collects data points from individual workers during job runs at the job level, worker-type, and the capacity-allocation-type level. You can use
`ApplicationId` as a dimension to monitor multiple jobs that belong to the same application.

| EMR Serverless job worker-level metrics | Metric                                                                       | Description    | Unit                                                                                               | Dimension |
| --------------------------------------- | ---------------------------------------------------------------------------- | -------------- | -------------------------------------------------------------------------------------------------- | --------- |
| `WorkerCpuAllocated`                    | The total numbers of vCPU cores allocated for workers in a job run.          | vCPU           | `JobId`, `JobName`, `ApplicationId`, `ApplicationName`, `WorkerType`, and `CapacityAllocationType` |
| `WorkerCpuUsed`                         | The total numbers of vCPU cores utilized by workers in a job run.            | vCPU           | `JobId`, `JobName`, `ApplicationId`, `ApplicationName`, `WorkerType`, and `CapacityAllocationType` |
| `WorkerMemoryAllocated`                 | The total memory in GB allocated for workers in a job run.                   | Gigabytes (GB) | `JobId`, `JobName`, `ApplicationId`, `ApplicationName`, `WorkerType`, and `CapacityAllocationType` |
| `WorkerMemoryUsed`                      | The total memory in GB utilized by workers in a job run.                     | Gigabytes (GB) | `JobId`, `JobName`, `ApplicationId`, `ApplicationName`, `WorkerType`, and `CapacityAllocationType` |
| `WorkerEphemeralStorageAllocated`       | The number of bytes of ephemeral storage allocated for workers in a job run. | Gigabytes (GB) | `JobId`, `JobName`, `ApplicationId`, `ApplicationName`, `WorkerType`, and `CapacityAllocationType` |
| `WorkerEphemeralStorageUsed`            | The number of bytes of ephemeral storage used by workers in a job run.       | Gigabytes (GB) | `JobId`, `JobName`, `ApplicationId`, `ApplicationName`, `WorkerType`, and `CapacityAllocationType` |
| `WorkerStorageReadBytes`                | The number of bytes read from storage by workers in a job run.               | Bytes          | `JobId`, `JobName`, `ApplicationId`, `ApplicationName`, `WorkerType`, and `CapacityAllocationType` |
| `WorkerStorageWriteBytes`               | The number of bytes written to storage from workers in a job run.            | Bytes          | `JobId`, `JobName`, `ApplicationId`, `ApplicationName`, `WorkerType`, and `CapacityAllocationType` |

The steps below describe how to access the various types of metrics.

Console

###### To access your application UI with the console

1. Navigate to your EMR Serverless application on the
   EMR Studio with the instructions in [Getting started from the console](getting-started.md#gs-console "getting-started.md#gs-console").
2. To access engine-specific application UIs and logs for a
   running job:
   1. Choose a job with a `RUNNING`
      status.
   2. Select the job on the **Application
      details** page, or navigate to the
      **Job details** page for your
      job.
   3. Under the **Display UI** dropdown
      menu, choose either **Spark UI** or
      **Hive Tez UI** to navigate to
      the application UI for your job type.
   4. To access Spark engine logs, navigate to the
      **Executors** tab in the Spark
      UI, and choose the **Logs** link
      for the driver. To access Hive engine logs, choose the
      **Logs** link for the appropriate
      DAG in the Hive Tez UI.

3. To access engine-specific application UIs and logs for a
   completed job:
   1. Choose a job with a `SUCCESS`
      status.
   2. Select the job on your application's
      **Application details** page or
      navigate to the job's **Job
      details** page.
   3. Under the **Display UI** dropdown
      menu, choose either **Spark History
      Server** or **Persistent Hive Tez
      UI** to navigate to the application UI
      for your job type.
   4. To access Spark engine logs, navigate to the
      **Executors** tab in the Spark
      UI, and choose the **Logs** link
      for the driver. To access Hive engine logs, choose the
      **Logs** link for the appropriate
      DAG in the Hive Tez UI.

AWS CLI

###### To access your application UI with the AWS CLI

- To generate a URL that use to access your
  application UI for running and completed jobs, call the
  `GetDashboardForJobRun` API.

```
aws emr-serverless get-dashboard-for-job-run /
--application-id `<application-id>` /
--job-run-id `<job-id>`
```

The URL that you generate is valid for one hour.
