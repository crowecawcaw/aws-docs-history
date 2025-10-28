# Job definitions

AWS Batch job definitions specify how jobs are to be run. While each job must reference a job definition, many of
the parameters that are specified in the job definition can be overridden at runtime.

Some of the attributes specified in a job definition include:

- Which Docker image to use with the container in your job.
- How many vCPUs and how much memory to use with the container.
- The command the container should run when it is started.
- What (if any) environment variables should be passed to the container when it starts.
- Any data volumes that should be used with the container.
- What (if any) IAM role your job should use for AWS permissions.

###### Contents

- [Create a single-node job definition](create-job-definition.md "create-job-definition.md")
- [Create a multi-node parallel job definition](create-multi-node-job-def.md "create-multi-node-job-def.md")
- [Job definition template that uses ContainerProperties](job-definition-template.md "job-definition-template.md")
- [Create job definitions using EcsProperties](multi-container-jobs.md "multi-container-jobs.md")
- [Use the awslogs log driver](using_awslogs.md "using_awslogs.md")
- [Specify sensitive data](specifying-sensitive-data.md "specifying-sensitive-data.md")
- [Private registry authentication for jobs](private-registry.md "private-registry.md")
- [Amazon EFS volumes](efs-volumes.md "efs-volumes.md")
- [Job definition examples](example-job-definitions.md "example-job-definitions.md")
