# Schedule your containers on Amazon ECS

Amazon Elastic Container Service (Amazon ECS) is a shared state, optimistic concurrency system that provides flexible
scheduling capabilities for your containerized workloads. The Amazon ECS schedulers use the same
cluster state information as the Amazon ECS API to make appropriate placement decisions.

Amazon ECS provides a service scheduler for long-running tasks and applications. It also
provides the ability to run standalone tasks or scheduled tasks for batch jobs or single run
tasks. You can specify the task placement strategies and constraints for running tasks that
best meet your needs. For example, you can specify whether tasks run across multiple
Availability Zones or within a single Availability Zone. And, optionally, you can integrate
tasks with your own custom or third-party schedulers.

| Option          | When to use                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | More information                                                                                                                                       |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Service         | The \*service scheduler<br>• is suitable for long running<br>stateless services and applications. The service scheduler optionally also<br>makes sure that tasks are registered against an ELB load balancer. You can<br>update your services that are maintained by the service scheduler. This<br>might include deploying a new task definition or changing the number of<br>desired tasks that are running. By default, the service scheduler spreads<br>tasks across multiple Availability Zones. However, you can use task<br>placement strategies and constraints to customize task placement decisions. | [Amazon ECS services](ecs_services.md "ecs_services.md")                                                                                               |
| Standalone task | A standalone task is suitable for processes such as batch jobs that<br>perform work and then stop. For example, you can have a process call<br>`RunTask` when work comes into a queue. The task pulls work from the<br>queue, performs the work, and then exits. Using `RunTask`, you can allow the<br>default task placement strategy to distribute tasks randomly across your cluster. This<br>minimizes the chances that a single instance gets a disproportionate number of tasks.                                                                                                                         | [Amazon ECS standalone tasks](standalone-tasks.md "standalone-tasks.md")                                                                               |
| Scheduled tasks | A scheduled task is suitable when you have tasks to run at set intervals in your cluster, you can use EventBridge Scheduler to create<br>a schedule. You can run tasks for a backup operation or a log scan. The EventBridge Scheduler schedule<br>that you create can run one or more tasks in your cluster at specified times. Your<br>scheduled event can be set to a specific interval (run every<br>`N` minutes, hours, or days). Otherwise, for more<br>complicated scheduling, you can use a `cron` expression.                                                                                         | [Using Amazon EventBridge Scheduler to schedule Amazon ECS tasks](tasks-scheduled-eventbridge-scheduler.md "tasks-scheduled-eventbridge-scheduler.md") |

## Compute options

With Amazon ECS, you can specify the infrastructure your tasks or services run on. You can
use a capacity provider strategy, or a launch type.

For Fargate, the capacity providers are Fargate and Fargate Spot. For EC2, the capacity provider is the Auto Scaling group with the registered container instances.

The capacity provider strategy distributes your tasks across the capacity providers associated with your cluster.

Only capacity providers that are both already associated with a cluster and have an
`ACTIVE` or `UPDATING` status can be used in a capacity
provider strategy. You can associate a capacity provider with a cluster when you create
a cluster.

In a capacity provider strategy, the optional _base_ value
designates how many tasks, at a minimum, run on a specified capacity provider. Only one
capacity provider in a capacity provider strategy can have a base defined.

The _weight_ value determines the relative percentage of the total
number of launched tasks that use the specified capacity provider. Consider the
following example. You have a strategy that contains two capacity providers, and both
have a weight of `1`. When the base percentage is reached, the tasks are
split evenly across the two capacity providers. Using that same logic, suppose that you
specify a weight of `1` for _capacityProviderA_ and a
weight of `4` for _capacityProviderB_. Then, for every one
task that's run using _capacityProviderA_, there are four tasks that
use _capacityProviderB_.

The compute option launches your tasks directly
on either Fargate or on the Amazon EC2 instances that you have manually registered to your
clusters.
