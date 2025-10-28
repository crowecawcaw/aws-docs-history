# Draining Amazon ECS container instances

There might be times when you need to remove a container instance from your cluster, for
example, to perform system updates or to scale down the cluster
capacity. Amazon ECS provides the ability to transition a container instance to a
`DRAINING` status. This is referred to as _container instance
draining_. When a container instance is set to `DRAINING`, Amazon ECS
prevents new tasks from being scheduled for placement on the container instance.

## Draining behavior for services

Any tasks that are part of a service that are in a `PENDING` state are
stopped immediately. If there is available container instance capacity in the cluster,
the service scheduler will start replacement tasks. If there isn't enough container
instance capacity, a service event message will be sent indicating the issue.

Tasks that are part of a service on the container instance that are in a
`RUNNING` state are transitioned to a `STOPPED` state. The
service scheduler attempts to replace the tasks according to the service's deployment
type and deployment configuration parameters, `minimumHealthyPercent` and
`maximumPercent`. For more information, see [Amazon ECS services](ecs_services.md "ecs_services.md") and [Amazon ECS service definition parameters](service_definition_parameters.md "service_definition_parameters.md").

- If `minimumHealthyPercent` is below 100%, the scheduler can ignore
  `desiredCount` temporarily during task replacement. For example,
  `desiredCount` is four tasks, a minimum of 50% allows the
  scheduler to stop two existing tasks before starting two new tasks. If the
  minimum is 100%, the service scheduler can't remove existing tasks until the
  replacement tasks are considered healthy. If tasks for services that do not use
  a load balancer are in the `RUNNING` state, they are considered
  healthy. Tasks for services that use a load balancer are considered healthy if
  they are in the `RUNNING` state and the container instance they are
  hosted on is reported as healthy by the load balancer.

###### Important

If you use Spot Instances and `minimumHealthyPercent` is greater than or
equal to 100%, then the service will not have enough time to replace the
task before the Spot Instance terminates.

- The `maximumPercent` parameter represents an upper limit on the
  number of running tasks during task replacement, which allows you to define the
  replacement batch size. For example, if `desiredCount` of four tasks,
  a maximum of 200% starts four new tasks before stopping the four tasks to be
  drained (provided that the cluster resources required to do this are available).
  If the maximum is 100%, then replacement tasks can't start until the draining
  tasks have stopped.

###### Important

If both `minimumHealthyPercent` and `maximumPercent`
are 100%, then the service can't remove existing tasks, and also cannot
start replacement tasks. This prevents successful container instance
draining and prevents making new deployments.

## Draining behavior for standalone

tasks

Any standalone tasks in the `PENDING` or `RUNNING` state are
unaffected; you must wait for them to stop on their own or stop them manually. The
container instance will remain in `DRAINING` status.

## Draining behavior for Amazon ECS Managed Instances

Amazon ECS Managed Instances termination processes ensure graceful workload transitions while
optimizing costs and maintaining system health. The termination system provides three
distinct decision paths for instance termination, each with different timing
characteristics and customer impact profiles.

Customer-initiated termination

Provides direct control over instance removal when you need to remove
container instances from service immediately. You run
`deregister-container-instance` with the
`force` request parameter set to true, This means that
immediate termination is required despite any running workloads.

System-initiated idle termination

Implements cost optimization through intelligent idle detection that identifies instances no longer serving workloads. The Elastic Workload Service (EWS) implements sophisticated idle detection algorithms that monitor instance utilization and initiate termination for instances that remain idle for configurable periods.

Infrastructure refresh termination

Implements proactive infrastructure management through Node Manager's natural decay policy, where instances are periodically refreshed to ensure they run on the latest platform versions and maintain security posture. Node Manager implements time-to-live (TTL) policies that initiate graceful termination for instances that have reached their maximum operational lifetime.

The termination system implements a two-phase approach that balances workload continuity against infrastructure management requirements.

###### Phase 1: Graceful completion period

During this phase, the system implements graceful draining strategies that prioritize workload continuity. Service tasks are gracefully drained through normal Amazon ECS scheduling processes. Standalone tasks continue running because they might complete naturally. The system monitors for all tasks to reach stopped state through natural completion processes.

###### Phase 2: Hard deadline enforcement

When graceful completion does not achieve termination objectives within acceptable timeframes, the system implements hard deadline enforcement. The hard deadline is typically set to draining initiation time plus seven days, providing substantial time for graceful completion while maintaining operational requirements. The enforcement includes automatic force deregistration procedures and immediate termination of all remaining tasks regardless of the completion status.

A container instance has completed draining when all tasks running on the instance
transition to a `STOPPED` state. The container instance remains in a
`DRAINING` state until it is activated again or deleted. You can verify the
state of the tasks on the container instance by using the [ListTasks](../APIReference/API_ListTasks.md "../APIReference/API_ListTasks.md") operation with the
`containerInstance` parameter to get a list of tasks on the instance followed
by a [DescribeTasks](../APIReference/API_DescribeTasks.md "../APIReference/API_DescribeTasks.md") operation with
the Amazon Resource Name (ARN) or ID of each task to verify the task state.

When you are ready for the container instance to start hosting tasks again, you change the
state of the container instance from `DRAINING` to `ACTIVE`. The Amazon ECS
service scheduler then considers the container instance for task placement again.

## Procedure

The following steps can be used to set a container instance to draining using the new
AWS Management Console.

You can also use the [UpdateContainerInstancesState](../APIReference/API_UpdateContainerInstancesState.md "../APIReference/API_UpdateContainerInstancesState.md") API action or the [update-container-instances-state](../../../cli/latest/reference/ecs/update-container-instances-state.md "../../../cli/latest/reference/ecs/update-container-instances-state.md") command to change the status of a
container instance to `DRAINING`.

###### AWS Management Console

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. In the navigation pane, choose **Clusters**.
3. On the **Clusters** page, choose a cluster that hosts your
   instances.
4. On the **Cluster : `name`** page,
   choose the **Infrastructure** tab. Then, under
   **Container instances** select the check box for each
   container instance you want to drain.
5. Choose **Actions**, **Drain**.
