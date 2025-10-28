# Job run states

When you submit a job run to an Amazon EMR Serverless job queue, the job run enters the
`SUBMITTED` state. A job state's passes from `SUBMITTED` through
`RUNNING` until it reaches `FAILED`, `SUCCESS`, or
`CANCELLING`.

Job runs can have the following states:

| State          | Description                                                                                                                                                                                                                                                                                            |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Submitted**  | The initial job state when you submit a job run to EMR Serverless. The job waits to be scheduled for the application. EMR Serverless begins to prioritize and schedule the job run.                                                                                                                    |
| **Queued**     | The job run waits in this state when application level job run concurrency is fully occupied. For more information about queuing and concurrency, refer to [Job concurrency and queuing for an EMR Serverless application](applications-concurrency-queuing.md "applications-concurrency-queuing.md"). |
| **Pending**    | The scheduler is evaluating the job run to prioritize and schedule the run for the application.                                                                                                                                                                                                        |
| **Scheduled**  | EMR Serverless has scheduled the job run for the application, and is allocating resources to execute the job.                                                                                                                                                                                          |
| **Running**    | EMR Serverless has allocated the resources that the job initially needs, and the job is running in the application. In Spark applications, this means that the Spark driver process is in the `running` state.                                                                                         |
| **Failed**     | EMR Serverless failed to submit the job run to the application, or it completed unsuccessfully. Refer to `StateDetails` for additional information about this job failure.                                                                                                                             |
| **Success**    | The job run has completed successfully.                                                                                                                                                                                                                                                                |
| **Cancelling** | The `CancelJobRun` API has requested job run cancellation, or the job run has timed out. EMR Serverless is trying to cancel the job in the application and release the resources.                                                                                                                      |
| **Cancelled**  | The job run was cancelled successfully, and the resources that it used have been released.                                                                                                                                                                                                             |
