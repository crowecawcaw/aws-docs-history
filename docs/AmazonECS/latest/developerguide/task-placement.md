# How Amazon ECS places tasks on container instances

You can use task placement to configure Amazon ECS to place your tasks on container instances
that meet certain criteria, for example an Availability Zone or instance type.

The following are task placement components:

- Task placement strategy - The algorithm for selecting container instances for task
  placement or tasks for termination. For example, Amazon ECS can select container
  instances at random, or it can select container instances such that tasks are
  distributed evenly across a group of instances.
- Task group - A group of related tasks, for example database tasks.
- Task placement constraint - These are rules that must be met in order to place a
  task on a container instance. If the constraint is not met, the task is not placed
  and remains in the `PENDING` state. For example, you can use a constraint
  to place tasks only on a particular instance type.
  Amazon ECS has different algorithms for the different capacity options.

## Amazon ECS Managed Instances

For tasks that run on Amazon ECS Managed Instances, Amazon ECS must determine where to place the
task, and — when scaling down task count — which tasks to terminate. Amazon ECS makes this
determination based on the instance requirements specified in the capacity provider
launch template, requirements specified in the task definition such as CPU and memory,
and task placement constraints.

###### Note

Amazon ECS Managed Instances does not support task placement strategies. Amazon ECS will try its
best to spread tasks across accessible Availability Zones.

When Amazon ECS places tasks, it uses the following process to select container
instances:

1. Identify the container instances that satisfy the CPU, GPU, memory, and port
   requirements in the task definition.
2. Identify the container instances that satisfy the task placement constraints.
3. Identify the container instances that satisfy the instance requirements specified in the capacity provider launch template.
4. Select the container instances for task placement.

## EC2

For tasks that use the EC2 launch type, Amazon ECS must
determine where to place the task based on the requirements specified in the task
definition, such as CPU and memory. Similarly, when you scale down the task count, Amazon ECS
must determine which tasks to terminate. You can apply task placement strategies and
constraints to customize how Amazon ECS places and terminates tasks.

The default task placement strategies depend on whether you run tasks manually (standalone tasks) or within a service. For tasks running as part of an Amazon ECS service, the task placement strategy is `spread` using the `attribute:ecs.availability-zone`. There isn't a default task placement constraint for tasks not in services. For more
information, see [Schedule your containers on Amazon ECS](scheduling_tasks.md "scheduling_tasks.md").

###### Note

Task placement strategies are a best effort. Amazon ECS still attempts to place tasks
even when the most optimal placement option is unavailable. However, task placement
constraints are binding, and they can prevent task placement.

You can use task placement strategies and constraints together. For example, you can
use a task placement strategy and a task placement constraint to distribute tasks across
Availability Zones and bin pack tasks based on memory within each Availability Zone, but
only for G2 instances.

When Amazon ECS places tasks, it uses the following process to select container
instances:

1. Identify the container instances that satisfy the CPU, GPU, memory, and port
   requirements in the task definition.
2. Identify the container instances that satisfy the task placement
   constraints.
3. Identify the container instances that satisfy the task placement
   strategies.
4. Select the container instances for task placement.

## Fargate

Task placement strategies and constraints aren't supported for tasks using the
Fargate. Fargate will try its best to spread
tasks across accessible Availability Zones. If the capacity provider includes both
Fargate and Fargate Spot, the spread behavior is independent for each
capacity provider.
