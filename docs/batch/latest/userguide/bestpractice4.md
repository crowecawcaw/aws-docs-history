# Choose the right compute environment resource

AWS Fargate requires less initial setup and configuration than Amazon EC2 and is likely easier
to use, particularly if it's your first time. With Fargate, you don't need to manage servers,
handle capacity planning, or isolate container workloads for security.

If you have the following requirements, we recommend you use Fargate instances:

- Your jobs must start quickly, specifically less than 30 seconds.
- The requirements of your jobs are 16 vCPUs or less, no GPUs, and 120 GiB of memory or
  less.
  For more information, see [When to use Fargate](when-to-use-fargate.md "when-to-use-fargate.md").

If you have the following requirements, we recommend that you use Amazon EC2 instances:

- You require increased control over the instance selection or require using specific
  instance types.
- Your jobs require resources that AWS Fargate can’t provide, such as GPUs, more memory, a
  custom AMI, or the Amazon Elastic Fabric Adapter.
- You require a high level of throughput or concurrency.
- You need to customize your AMI, Amazon EC2 Launch Template, or access to special Linux
  parameters.
  With Amazon EC2, you can more finely tune your workload to your specific requirements and run at
  scale if needed.
