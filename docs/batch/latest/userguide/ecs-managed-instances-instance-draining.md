

# Instance draining and task interruptions
<a name="ecs-managed-instances-instance-draining"></a>

Amazon ECS Managed Instances initiates draining at day 14 from instance launch. When Amazon ECS drains an instance that is running a job, the job's task fails with the stop reason `Task stopped during instance draining`. Configure a [retry strategy](job_retries.md) on the job or job definition to rerun the job. For more information about instance draining, see [Draining Amazon ECS container instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/container-instance-draining.html) in the *Amazon Elastic Container Service Developer Guide*.