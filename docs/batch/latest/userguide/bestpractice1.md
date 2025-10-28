# When to use AWS Batch

AWS Batch runs jobs at scale and at low cost, and provides queuing services and cost-optimized
scaling. However, not every workload is suitable to be run using AWS Batch.

- Short jobs – If a job runs for only a few seconds, the overhead to
  schedule the batch job might take longer than the runtime of the job itself. As a workaround,
  binpack your tasks together before you submit them in AWS Batch. Then, configure your AWS Batch jobs to
  iterate over the tasks. For example, stage the individual task arguments into an Amazon DynamoDB table or as a file in an
  Amazon S3 bucket. Consider grouping tasks so the jobs run 3-5 minutes each. After you binpack the jobs,
  loop through your task groups within your AWS Batch job.
- Jobs that must be run immediately – AWS Batch can process
  jobs quickly. However, AWS Batch is a scheduler and optimizes for cost performance, job priority,
  and throughput. AWS Batch might require time to process your requests. If you need a response in
  under a few seconds, then a service-based approach using Amazon ECS or Amazon EKS is more
  suitable.
