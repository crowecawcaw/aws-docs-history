# Mapping AWS Batch service job status to SageMaker AI

status

When you submit jobs to a SageMaker job queue using [SubmitServiceJob](../APIReference/API_SubmitServiceJob.md "../APIReference/API_SubmitServiceJob.md"),
AWS Batch manages the job lifecycle and maps AWS Batch [job states](job_states.md "job_states.md") to equivalent SageMaker Training
job states. Service jobs, such as SageMaker Training jobs, follow a different state lifecycle
than traditional container jobs. While service jobs share most states with container jobs,
they introduce the `SCHEDULED` state and exhibit different retry behaviors,
particularly for handling insufficient capacity errors from the target service.

The following table shows the AWS Batch job state and the corresponding SageMaker
Status/SecondaryStatus:

| Batch Status | SageMaker AI Primary Status | SageMaker AI Secondary Status | Description                                                                                                                                                                                                                            |
| ------------ | --------------------------- | ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `SUBMITTED`  | N/A                         | N/A                           | Job submitted to queue, waiting for scheduler evaluation.                                                                                                                                                                              |
| `RUNNABLE`   | N/A                         | N/A                           | Job is queued and ready for scheduling. Jobs in this state are started as soon as sufficient resources are available in the service environment. Jobs can remain in this state indefinitely when sufficient resources are unavailable. |
| `SCHEDULED`  | `InProgress`                | `Pending`                     | Service job successfully submitted to SageMaker AI                                                                                                                                                                                     |
| `STARTING`   | `InProgress`                | `Downloading`                 | SageMaker Training job downloading data and images. Training job capacity has been acquired and job initialization begins.                                                                                                             |
| `RUNNING`    | `InProgress`                | `Training`                    | SageMaker Training job executing algorithm                                                                                                                                                                                             |
| `RUNNING`    | `InProgress`                | `Uploading`                   | SageMaker Training job uploading output artifacts after training completion                                                                                                                                                            |
| `SUCCEEDED`  | `Completed`                 | `Completed`                   | SageMaker Training job completed successfully. Output artifacts finished uploading.                                                                                                                                                    |
| `FAILED`     | `Failed`                    | `Failed`                      | SageMaker Training job encountered an unrecoverable error.                                                                                                                                                                             |
| `FAILED`     | `Stopped`                   | `Stopped`                     | SageMaker Training job was manually stopped using `StopTrainingJob`.                                                                                                                                                                   |
