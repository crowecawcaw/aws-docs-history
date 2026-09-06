# Instance draining and task interruptions

Amazon ECS Managed Instances initiates draining at day 14 from instance launch. When Amazon ECS
drains an instance that is running a job, the job's task fails with the stop reason `Task
 stopped during instance draining`. Configure a [retry
strategy](job_retries.md "job_retries.md") on the job or job definition to rerun the job. For more information about instance draining, see [Draining Amazon ECS container
instances](../../../AmazonECS/latest/developerguide/container-instance-draining.md "../../../AmazonECS/latest/developerguide/container-instance-draining.md") in the _Amazon Elastic Container Service Developer Guide_.
