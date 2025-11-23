# Amazon ECS cluster capacity

You can provide capacity to an Amazon ECS cluster in several ways. For example, you can
launch Amazon EC2 instances and register them with the cluster at start-up using the Amazon ECS
container agent. However, this method can be challenging because you need to manage
scaling on your own. Therefore, we recommend that you use Amazon ECS capacity providers. Capacity providers
manage resource scaling for you. There are three kinds of capacity providers: Amazon EC2,
Fargate, and Fargate Spot. For more information about Fargate capacity providers, see
[Amazon ECS clusters for Fargate workloads](fargate-capacity-providers.md "fargate-capacity-providers.md") and for EC2 workloads, see [Amazon ECS clusters for EC2 workloads](asg-capacity-providers.md "asg-capacity-providers.md").

The Fargate and Fargate Spot capacity providers handle the lifecycle of Fargate tasks
for you. Fargate provides on-demand capacity, and Fargate Spot provides Spot capacity.
When you launch a task, Amazon ECS provisions a Fargate resource for you. This Fargate
resource comes with the memory and CPU units that directly correspond to the task-level
limits that you declared in your task definition. Each task receives its own Fargate
resource, making a 1:1 relationship between the task and compute resources.

Tasks that run on Fargate Spot are subject to interruption. Interruptions come after a
two-minute warning. These occur during periods of heavy demand. Fargate Spot works best
for interruption-tolerant workloads such as batch jobs, development or staging
environments. They're also suitable for any other scenario where high availability and
low latency isn't a requirement.

You can run Fargate Spot tasks alongside Fargate on-demand tasks. By using them
together, you receive provision “burst” capacity at a lower cost.

Amazon ECS can also manage the Amazon EC2 instance capacity for your tasks. Each Amazon EC2 capacity
provider is associated with an Amazon EC2 Auto Scaling group that you specify. When you use
the Amazon EC2 capacity provider, cluster auto scaling maintains the size of the Amazon EC2
Amazon EC2 Auto Scaling group to ensure all scheduled tasks can be placed.
