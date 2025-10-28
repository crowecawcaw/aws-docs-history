# Checklist to run at scale

Before you run a large workload on 50 thousand or more vCPUs, consider the following
checklist.

###### Note

If you plan to run a large workload on a million or more vCPUs or need guidance running at
large scale, contact your AWS team.

- Check your Amazon EC2 quotas – Check your Amazon EC2 quotas (also
  known as limits) in the Service Quotas panel of the AWS Management Console. If necessary, request a quota increase for
  your peak number of Amazon EC2 instances. Remember that Amazon EC2 Spot and Amazon On-Demand instances
  have separate quotas. For more information, see [Getting started with Service
  Quotas](../../../servicequotas/latest/userguide/getting-started.md "../../../servicequotas/latest/userguide/getting-started.md").
- Verify your Amazon Elastic Block Store quota for each Region – Each
  instance uses a GP2 or GP3 volume for the operating system. By default, the quota for each
  AWS Region is 300 TiB. However, each instance uses counts as part of this quota. So, make
  sure to factor this in when you verify your Amazon Elastic Block Store quota for each Region. If your quota is
  reached, you can’t create more instances. For more information, see [Amazon Elastic Block Store endpoints and
  quotas](../../../general/latest/gr/ebs-service.md "../../../general/latest/gr/ebs-service.md")
- Use Amazon S3 for storage – Amazon S3 provides high throughput and
  helps to eliminate the guesswork on how much storage to provision based on the number of jobs
  and instances in each Availability Zone. For more information, see [Best practices design patterns:
  optimizing Amazon S3 performance](../../../AmazonS3/latest/userguide/optimizing-performance.md "../../../AmazonS3/latest/userguide/optimizing-performance.md").
- Scale gradually to identify bottlenecks early – For a job
  that runs on a million or more vCPUs, start lower and gradually increase so that you can
  identify bottlenecks early. For example, start by running on 50 thousand vCPUs. Then, increase
  the count to 200 thousand vCPUs, and then 500 thousand vCPUs, and so on. In other words,
  continue to gradually increase the vCPU count until you reach the desired number of
  vCPUs.
- Monitor to identify potential issues early – To avoid
  potential breaks and issues when running at scale, make sure to monitor both your application
  and architecture. Breaks might occur even when scaling from 1 thousand to 5 thousand vCPUs. You
  can use Amazon CloudWatch Logs to review log data or use CloudWatch Embedded Metrics using a client library. For
  more information, see [CloudWatch Logs agent reference](../../../AmazonCloudWatch/latest/logs/AgentReference.md "../../../AmazonCloudWatch/latest/logs/AgentReference.md") and
  [`aws-embedded-metrics`](https://github.com/awslabs/aws-embedded-metrics-python "https://github.com/awslabs/aws-embedded-metrics-python")
