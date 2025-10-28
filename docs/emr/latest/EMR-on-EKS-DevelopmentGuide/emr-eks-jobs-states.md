# Job run states

When you submit a job run to an Amazon EMR on EKS job queue, the job run enters the
`PENDING` state. It then passes through the following states until it succeeds
(exits with code `0`) or fails (exits with a non-zero code).

Job runs can have the following states:

- `PENDING` ‐ The initial job state when the job run is submitted to
  Amazon EMR on EKS. The job is waiting to be submitted to the virtual cluster, and Amazon EMR on EKS is
  working on submitting this job.
- `SUBMITTED` ‐ A job run that has been successfully submitted to the
  virtual cluster. The cluster scheduler then tries to run this job on the cluster.
- `RUNNING` ‐ A job run that is running in the virtual cluster. In
  Spark applications, this means that the Spark driver process is in the
  `running` state.
- `FAILED` ‐ A job run that failed to be submitted to the virtual
  cluster or that completed unsuccessfully. Look at StateDetails and FailureReason to find
  additional information about this job failure.
- `COMPLETED` ‐ A job run that has completed successfully.
- `CANCEL_PENDING` ‐ A job run has been requested for cancellation.
  Amazon EMR on EKS is trying to cancel the job on the virtual cluster.
- `CANCELLED` ‐ A job run that was cancelled successfully.
