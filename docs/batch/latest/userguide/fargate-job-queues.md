# Job queues on Fargate

AWS Batch job queues on AWS Fargate are essentially unchanged. The only restriction is that the compute environments
that are listed in `computeEnvironmentOrder` must all be Fargate compute environments
(`FARGATE` or `FARGATE_SPOT`). EC2 and Fargate compute environments can't be mixed.
