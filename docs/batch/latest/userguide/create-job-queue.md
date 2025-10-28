# Create a job queue

Before you can submit jobs in AWS Batch, you must create a job queue. When you create a job
queue, you associate one or more compute environments to the queue and assign an order of
preference.

You also set priority to the job queue that determines the order that the AWS Batch
scheduler places jobs. This means that, if a compute environment is associated with more than one
job queue, the job queue with a higher priority is given preference.

###### Topics

- [Create an Amazon EC2 job queue](create-job-queue-ec2.md "create-job-queue-ec2.md")
- [Create a Fargate job queue](create-job-queue-fargate.md "create-job-queue-fargate.md")
- [Create an Amazon EKS job queue](create-job-queue-eks.md "create-job-queue-eks.md")
- [Create a SageMaker Training job queue in AWS Batch](create-sagemaker-job-queue.md "create-sagemaker-job-queue.md")
- [Job queue template](job-queue-template.md "job-queue-template.md")
