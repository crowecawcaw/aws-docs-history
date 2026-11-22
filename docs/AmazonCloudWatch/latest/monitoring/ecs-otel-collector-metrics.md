

# Metrics and attributes

For each running task, the receiver emits about 28 task-level metrics (`ecs.task.*`). It also emits about 26 container-level metrics (`container.*`) for each running container. The following table lists commonly used metrics.


| Metric | Unit | Description | 
| --- | --- | --- | 
| ecs.task.cpu.utilized, ecs.task.cpu.reserved | CPU units (1024 = 1 vCPU) | Task CPU used and reserved | 
| ecs.task.memory.utilized, ecs.task.memory.reserved | MiB | Task memory used and reserved | 
| ecs.task.network.rate.rx, ecs.task.network.rate.tx | Bytes/second | Task network throughput | 
| ecs.task.storage.read\_bytes, ecs.task.storage.write\_bytes | Bytes, cumulative | Task storage I/O. Use rate() in queries. | 
| container.cpu.utilized, container.cpu.reserved | CPU units | Container CPU used and reserved | 
| container.memory.utilized, container.memory.reserved | MiB | Container memory used and reserved | 
| container.memory.usage, container.memory.usage.limit | Bytes | Container memory usage and hard limit | 
| container.network.rate.rx, container.network.rate.tx | Bytes/second | Network throughput of the container's network interface | 

In PromQL, resource attributes appear with the `@resource.` prefix. With the configuration in step 2, each series has the following attributes.


| Attribute | Present on | 
| --- | --- | 
| aws.ecs.cluster.name | Task and container metrics | 
| aws.ecs.service.name | Task and container metrics. Empty for tasks that aren't part of a service. | 
| aws.ecs.task.family, aws.ecs.task.revision | Task and container metrics | 
| aws.ecs.task.id | Task and container metrics | 
| aws.ecs.task.launch\_type | Task and container metrics. The value is EC2, FARGATE, or MANAGED\_INSTANCES. | 
| aws.ecs.launchtype | Task and container metrics. The value is ec2 or fargate. Not set for Amazon ECS Managed Instances. | 
| cloud.availability\_zone | Task and container metrics | 
| container.name, container.image.name, container.image.tag | Container metrics | 