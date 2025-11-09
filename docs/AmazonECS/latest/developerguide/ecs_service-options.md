# Amazon ECS service deployment controllers and strategies

Before you deploy your service, determine the options for deploying it, and the features
the service uses.

## Scheduling strategy

There are two service scheduler
strategies available:

- `REPLICA`—The replica scheduling strategy places and
  maintains the desired number of tasks across your cluster. By default, the
  service scheduler spreads tasks across Availability Zones. You can use task
  placement strategies and constraints to customize task placement decisions. For
  more information, see [Replica scheduling strategy](#service_scheduler_replica "#service_scheduler_replica").
- `DAEMON`—The daemon scheduling strategy deploys exactly one
  task on each active container instance that meets all of the task placement
  constraints that you specify in your cluster. When using this strategy, there is no need to
  specify a desired number of tasks, a task placement strategy, or use Service
  Auto Scaling policies. For more information, see [Daemon scheduling strategy](#service_scheduler_daemon "#service_scheduler_daemon").

###### Note

Fargate tasks do not support the `DAEMON`
scheduling strategy.

### Replica scheduling strategy

The _replica_ scheduling strategy places and maintains the
desired number of tasks in your cluster.

For a service that runs tasks on Fargate, when the service scheduler
launches new tasks or stops running tasks, the service scheduler uses a best attempt
to maintain a balance across Availability Zones. You don't need to specify task
placement strategies or constraints.

When you create a service that runs tasks on EC2 instances, you can
optionally specify task placement strategies and constraints to customize task
placement decisions. If no task placement strategies or constraints are specified,
then by default the service scheduler spreads the tasks across Availability Zones.
The service scheduler uses the following logic:

- Determines which of the container instances in your cluster can support
  your service's task definition (for example, required CPU, memory, ports,
  and container instance attributes).
- Determines which container instances satisfy any placement constraints
  that are defined for the service.
- When you have a replica service that depends on a daemon service (for
  example, a daemon log router task that needs to be running before tasks can
  use logging), create a task placement constraint that ensures that the
  daemon service tasks get placed on the EC2 instance prior to the replica
  service tasks. For more information, see [Example Amazon ECS task placement constraints](constraint-examples.md "constraint-examples.md").
- When there's a defined placement strategy, use that strategy to select an
  instance from the remaining candidates.
- When there's no defined placement strategy, use the following logic to
  balance tasks across the Availability Zones in your cluster:
  - Sorts the valid container instances. Gives priority to instances
    that have the fewest number of running tasks for this service in
    their respective Availability Zone. For example, if zone A has one
    running service task and zones B and C each have zero, valid
    container instances in either zone B or C are considered optimal for
    placement.
  - Places the new service task on a valid container instance in an
    optimal Availability Zone based on the previous steps. Favors
    container instances with the fewest number of running tasks for this
    service.

We recommend that you use the service rebalancing feature when you use the
`REPLICA` strategy because it helps ensure high availability for your
service.

### Daemon scheduling strategy

The _daemon_ scheduling strategy deploys exactly one task on
each active container instance that meets all of the task placement constraints
specified in your cluster. The service scheduler evaluates the task placement
constraints for running tasks, and stops tasks that don't meet the placement
constraints. When you use this strategy, you don't need to specify a desired number
of tasks, a task placement strategy, or use Service Auto Scaling policies.

Amazon ECS reserves container instance compute resources including CPU, memory, and
network interfaces for the daemon tasks. When you launch a daemon service on a
cluster with other replica services, Amazon ECS prioritizes the daemon task. This means
that the daemon task is the first task to launch on the instances and the last task
to stop after all replica tasks are stopped. This strategy ensures that resources
aren't used by pending replica tasks and are available for the daemon tasks.

The daemon service scheduler doesn't place any tasks on instances that have a
`DRAINING` status. If a container instance transitions to a
`DRAINING` status, the daemon tasks on it are stopped. The service
scheduler also monitors when new container instances are added to your cluster and
adds the daemon tasks to them.

When you specify a deployment configuration, the value for the
`maximumPercent` parameter must be `100` (specified as a
percentage), which is the default value used if not set. The default value for the
`minimumHealthyPercent` parameter is `0` (specified as a
percentage).

You must restart the service when you change the placement constraints for the
daemon service. Amazon ECS dynamically updates the resources that are reserved on
qualifying instances for the daemon task. For existing instances, the scheduler
tries to place the task on the instance.

A new deployment starts when there is a change to the task size or container
resource reservation in the task definition. A new deployment also starts when
updating a service or setting a different revision of the task definition. Amazon ECS
picks up the updated CPU and memory reservations for the daemon, and then blocks
that capacity for the daemon task.

If there are insufficient resources for either of the above cases, the following
happens:

- The task placement fails.
- A CloudWatch event is generated.
- Amazon ECS continues to try and schedule the task on the instance by waiting
  for resources to become available.
- Amazon ECS frees up any reserved instances that no longer meet the placement
  constraint criteria and stops the corresponding daemon tasks.

The daemon scheduling strategy can be used in the following cases:

- Running application containers
- Running support containers for logging, monitoring and tracing
  tasks

Tasks using Fargate or the `CODE_DEPLOY`
or `EXTERNAL` deployment controller types don't support the daemon
scheduling strategy.

When the service scheduler stops running tasks, it attempts to maintain balance
across the Availability Zones in your cluster. The scheduler uses the following
logic:

- If a placement strategy is defined, use that strategy to select which
  tasks to terminate. For example, if a service has an Availability Zone
  spread strategy defined, a task is selected that leaves the remaining tasks
  with the best spread.
- If no placement strategy is defined, use the following logic to maintain
  balance across the Availability Zones in your cluster:
  - Sort the valid container instances. Give priority to instances
    that have the largest number of running tasks for this service in
    their respective Availability Zone. For example, if zone A has one
    running service task and zones B and C each have two running service
    task, container instances in either zone B or C are considered
    optimal for termination.
  - Stop the task on a container instance in an optimal Availability
    Zone based on the previous steps. Favoring container instances with
    the largest number of running tasks for this service.

## Deployment controllers

The deployment controller is the mechanism that determines how tasks are deployed for
your service. The valid options are:

- ECS

When you create a service which uses the `ECS` deployment controller, you can choose between the following deployment strategies:

    + `ROLLING`: When you create a service which uses the *rolling update*
     (`ROLLING`) deployment strategy, the Amazon ECS service scheduler replaces the
     currently running tasks with new tasks. The number of tasks that Amazon ECS adds or
     removes from the service during a rolling update is controlled by the service
     deployment configuration.


    Rolling update deployments are best suited for the following scenarios:




    	- Gradual service updates: You need to
    	 update your service incrementally without taking the entire service
    	 offline at once.
    	- Limited resource requirements: You
    	 want to avoid the additional resource costs of running two complete
    	 environments simultaneously (as required by blue/green
    	 deployments).
    	- Acceptable deployment time: Your
    	 application can tolerate a longer deployment process, as rolling updates
    	 replace tasks one by one.
    	- No need for instant roll back: Your
    	 service can tolerate a rollback process that takes minutes rather than
    	 seconds.
    	- Simple deployment process: You prefer
    	 a straightforward deployment approach without the complexity of managing
    	 multiple environments, target groups, and listeners.
    	- No load balancer requirement: Your
    	 service doesn't use or require a load balancer, Application Load Balancer, Network Load Balancer, or Service Connect (which are required
    	 for blue/green deployments).
    	- Stateful applications: Your
    	 application maintains state that makes it difficult to run two parallel
    	 environments.
    	- Cost sensitivity: You want to
    	 minimize deployment costs by not running duplicate environments during
    	 deployment.
    Rolling updates are the default deployment strategy for services and provide a
     balance between deployment safety and resource efficiency for many common
     application scenarios.
    + `BLUE_GREEN`: A *blue/green* deployment strategy (`BLUE_GREEN`) is a release methodology that reduces downtime and
     risk by running two identical production environments called blue and green.
     With Amazon ECS blue/green deployments, you can validate new service revisions before
     directing production traffic to them. This approach provides a safer way to
     deploy changes with the ability to quickly roll back if needed.


    Amazon ECS blue/green deployments are best suited for the following scenarios:




    	- Service validation: When you need to
    	 validate new service revisions before directing production traffic to
    	 them
    	- Zero downtime: When your service
    	 requires zero-downtime deployments
    	- Instant roll back: When you
    	 need the ability to quickly roll back if issues are detected
    	- Load balancer requirement: When your
    	 service uses Application Load Balancer, Network Load Balancer, or Service Connect
    + `LINEAR`: A *linear* deployment strategy (`LINEAR`) gradually shifts traffic from the current production environment to a new environment in equal percentage increments over a specified time period. With Amazon ECS linear deployments, you can control the pace of traffic shifting and validate new service revisions with increasing amounts of production traffic.


    Amazon ECS linear deployments are best suited for the following scenarios:




    	- Gradual validation: When you want to gradually validate your new service version with increasing traffic
    	- Performance monitoring: When you need time to monitor metrics and performance during the deployment
    	- Risk minimization: When you want to minimize risk by exposing the new version to production traffic incrementally
    	- Load balancer requirement: When your service uses Application Load Balancer, Network Load Balancer, or Service Connect
    + `CANARY`: A *canary* deployment strategy (`CANARY`) shifts a small percentage of traffic to the new service revision first, then shifts the remaining traffic all at once after a specified time period. This allows you to test the new version with a subset of users before full deployment.


    Amazon ECS canary deployments are best suited for the following scenarios:




    	- Feature testing: When you want to test new features with a small subset of users before full rollout
    	- Production validation: When you need to validate performance and functionality with real production traffic
    	- Blast radius control: When you want to minimize blast radius if issues are discovered in the new version
    	- Load balancer requirement: When your service uses Application Load Balancer, Network Load Balancer, or Service Connect

- External

Use a third-party deployment controller.

- Blue/green deployment (powered by AWS CodeDeploy)

CodeDeploy installs an updated version of the application as a new replacement task
set and reroutes production traffic from the original application task set to
the replacement task set. The original task set is terminated after a successful
deployment. Use this deployment controller to verify a new deployment of a service
before sending production traffic to it.

## Deployment terminology

The following terms are used throughout the Amazon ECS deployment documentation:

Blue-green deployment

A deployment strategy that creates a new environment (green) alongside the existing environment (blue), then switches traffic from blue to green after validation.

Canary deployment

A deployment strategy that routes a small percentage of traffic to a new version while maintaining the majority on the stable version for validation.

Linear deployment

A deployment strategy that gradually shifts traffic from the old version to the new version in equal increments over time.

Rolling deployment

A deployment strategy that replaces instances of the old version with instances of the new version one at a time.

Task set

A collection of tasks that run the same task definition within a service during a deployment.

Target group

A logical grouping of targets that receive traffic from a load balancer during deployments.

Deployment controller

The method used to deploy new versions of your service, such as Amazon ECS, CodeDeploy, or external controllers.

Rollback

The process of reverting to a previous version of your application when issues are detected during deployment.
