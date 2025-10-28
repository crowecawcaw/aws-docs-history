# Service jobs in AWS Batch

AWS Batch service jobs enable you to submit requests to AWS services through AWS Batch job
queues. Currently, AWS Batch supports SageMaker Training jobs as service jobs. Unlike containerized
jobs where AWS Batch manages the underlying container execution, service jobs allow AWS Batch to
provide job scheduling and queuing capabilities while the target AWS service (such as
SageMaker AI) handles the actual job execution.

AWS Batch for SageMaker Training jobs allows data scientists to submit training jobs with
priorities to configurable queues, ensuring workloads run without intervention as soon as
resources are available. This capability addresses common challenges such as resource
coordination, preventing accidental overspending, meeting budget constraints, optimizing
costs with reserved instances, and eliminating the need for manual coordination between team
members.

Service jobs differ from containerized jobs in several key ways:

- **Job submission**: Service jobs must be submitted
  using the [SubmitServiceJob](../APIReference/API_SubmitServiceJob.md "../APIReference/API_SubmitServiceJob.md") API. Service jobs cannot be submitted through the
  AWS Batch console.
- **Job execution**: AWS Batch schedules and queues
  service jobs, but the target AWS service runs the actual job workload.
- **Resource identifiers**: Service jobs use ARNs that
  contain "service-job" instead of "job" to distinguish them from containerized
  jobs.
  To get started with AWS Batch service jobs for SageMaker Training, see [Getting started with AWS Batch on SageMaker AI](getting-started-sagemaker.md "getting-started-sagemaker.md").

###### Topics

- [Service job payloads in AWS Batch](service-job-payload.md "service-job-payload.md")
- [Submit a service job in AWS Batch](service-job-submit.md "service-job-submit.md")
- [Mapping AWS Batch service job status to SageMaker AI
  status](service-job-status.md "service-job-status.md")
- [Service job retry strategies in AWS Batch](service-job-retries.md "service-job-retries.md")
- [Monitor service jobs in an AWS Batch queue](monitor-sagemaker-job-queue.md "monitor-sagemaker-job-queue.md")
