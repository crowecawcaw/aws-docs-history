# Terminate service jobs

Use the [`TerminateServiceJob`](../APIReference/API_TerminateServiceJob.md "../APIReference/API_TerminateServiceJob.md") operation to stop a running service job.

Terminate a specific service job:

```
aws batch terminate-service-job \
  --job-id `a4d6c728-8ee8-4c65-8e2a-9a5e8f4b7c3d` \
  --reason "Job terminated by user request"
```

When you terminate a service job, AWS Batch stops the job and notifies the target service.
For SageMaker Training jobs, this will stop the training job in SageMaker AI as well.
