# Update Amazon ECS service parameters

After you create a service, there are times when you might need to update the service
parameters, for example, the number of tasks.

When the service scheduler launches new tasks, it determines task placement in your
cluster with the following logic.

- Determine which of the container instances in your cluster can support your
  service's task definition. For example, they have the required CPU, memory, ports,
  and container instance attributes.
- By default, the service scheduler attempts to balance tasks across Availability
  Zones in this manner even though you can choose a different placement
  strategy.

      + Sort the valid container instances by the fewest number of running tasks
       for this service in the same Availability Zone as the instance. For example,
       if zone A has one running service task and zones B and C each have zero,
       valid container instances in either zone B or C are considered optimal for
       placement.
      + Place the new service task on a valid container instance in an optimal
       Availability Zone (based on the previous steps), favoring container
       instances with the fewest number of running tasks for this service.

  When the service scheduler stops running tasks, it attempts to maintain balance across the
  Availability Zones in your cluster using the following logic:

- Sort the container instances by the largest number of running tasks for this
  service in the same Availability Zone as the instance. For example, if zone A has
  one running service task and zones B and C each have two, container instances in
  either zone B or C are considered optimal for termination.
- Stop the task on a container instance in an optimal Availability Zone (based on
  the previous steps), favoring container instances with the largest number of running
  tasks for this service.
  Use the list to determine if you can change the service parameter.

**Availability Zone rebalancing**

Indicates whether to use Availability Zone rebalancing for the service.

You can change this parameter for rolling deployments.

**Capacity provider strategy**

The details of a capacity provider strategy. You can set a capacity provider
when you create a cluster, run a task, or update a service.

When you use Fargate, the capacity providers are `FARGATE` or
`FARGATE_SPOT`.

When you use Amazon EC2, the capacity providers are Auto Scaling groups.

You can change capacity providers for rolling deployments and blue/green
deployments.

The following list provides the valid transitions:

- Update the Fargate to an Auto Scaling group capacity
  provider.
- Update the EC2 to a Fargate capacity provider.
- Update the Fargate capacity provider to an Auto Scaling group capacity
  provider.
- Update the Amazon EC2 capacity provider to a Fargate capacity provider.
- Update the Auto Scaling group or Fargate capacity provider back to the
  launch type. When you use the CLI, or API, you pass an empty list in the
  `capacityProviderStrategy` parameter.

**Cluster**

You can't change the cluster name.

**Deployment configuration**

The deployment configuration includes the CloudWatch alarms, and circuit breaker
used to detect failures and the required configuration.

The deployment circuit breaker determines whether a service deployment will
fail if the service can't reach a steady state. If you use the deployment
circuit breaker, a service deployment will transition to a failed state and stop
launching new tasks. If you use the rollback option, when a service deployment
fails, the service is rolled back to the last deployment that completed
successfully.

When you update a service that uses Amazon ECS circuit breaker, Amazon ECS creates a
service deployment and a service revision. These resources allow you to view
detailed information about the service history. For more information, see [View service history using Amazon ECS service
deployments](service-deployment.md "service-deployment.md").

The service scheduler uses the minimum healthy percent and maximum percent
parameters (in the deployment configuration for the service) to determine the
deployment strategy.

If a service uses the rolling update (`ECS`) deployment type, the
**minimum healthy percent** represents a lower
limit on the number of tasks in a service that must remain in the
`RUNNING` state during a deployment, as a percentage of the
desired number of tasks (rounded up to the nearest integer). The parameter also
applies while any container instances are in the `DRAINING` state if
the service contains tasks using EC2. Use this
parameter to deploy without using additional cluster capacity. For example, if
your service has a desired number of four tasks and a minimum healthy percent of
50 percent, the scheduler may stop two existing tasks to free up cluster
capacity before starting two new tasks. The service considers tasks healthy for
services that do not use a load balancer if they are in the `RUNNING`
state. The service considers tasks healthy for services that do use a load
balancer if they are in the `RUNNING` state and they are reported as
healthy by the load balancer. The default value for minimum healthy percent is
100 percent.

If a service uses the rolling update (`ECS`) deployment type, the
**maximum percent** parameter represents an
upper limit on the number of tasks in a service that are allowed in the
`PENDING`, `RUNNING`, or `STOPPING` state
during a deployment, as a percentage of the desired number of tasks (rounded
down to the nearest integer). The parameter also applies while any container
instances are in the `DRAINING` state if the service contains tasks
using EC2. Use this parameter to define the
deployment batch size. For example, if your service has a desired number of four
tasks and a maximum percent value of 200 percent, the scheduler may start four
new tasks before stopping the four older tasks. This is provided that the
cluster resources required to do this are available. The default value for the
maximum percent is 200 percent.

When the service scheduler replaces a task during an update, the service first
removes the task from the load balancer (if used) and waits for the connections
to drain. Then, the equivalent of **docker stop** is issued to
the containers running in the task. This results in a `SIGTERM`
signal and a 30-second timeout, after which `SIGKILL` is sent and the
containers are forcibly stopped. If the container handles the
`SIGTERM` signal gracefully and exits within 30 seconds from
receiving it, no `SIGKILL` signal is sent. The service scheduler
starts and stops tasks as defined by your minimum healthy percent and maximum
percent settings.

The service scheduler also replaces tasks determined to be unhealthy after a container health check or a load balancer target group health check fails. This replacement depends on the `maximumPercent` and `desiredCount` service definition parameters.
If a task is marked unhealthy, the service scheduler will first start a replacement task. Then, the following happens.

- If the replacement task has a health status of `HEALTHY`, the service scheduler stops the unhealthy task
- If the replacement task has a health status of `UNHEALTHY`, the scheduler will stop either the unhealthy replacement task or the existing unhealthy task to get the total task count to equal `desiredCount`.

If the `maximumPercent` parameter limits the scheduler from starting a replacement task first, the scheduler will stop an unhealthy task one at a time at random to free up capacity, and then start a replacement task.
The start and stop process continues until all unhealthy tasks are replaced with healthy tasks. Once all unhealthy tasks have been replaced and only healthy tasks are running, if the total task count exceeds the `desiredCount`, healthy tasks are stopped at random until the total task count equals `desiredCount`. For more information about `maximumPercent` and `desiredCount`, see [Service definition parameters](service_definition_parameters.md "service_definition_parameters.md").

**Deployment controller**

The deployment controller to use for the service. There are three deployment
controller types available:

- `ECS`
- `EXTERNAL`
- `CODE_DEPLOY`

When you update a service, you can update the deployment controller it uses.
The following list provides the valid transitions:

- Update from CodeDeploy blue/green deployments (`CODE_DEPLOY`) to
  ECS rolling or blue/green deployments (`ECS`).
- Update from CodeDeploy blue/green deployments (`CODE_DEPLOY`) to
  external deployments (`EXTERNAL`).
- Update from ECS rolling or blue/green deployments (`ECS`)
  to external deployments (`EXTERNAL`).
- Update from external deployments (`EXTERNAL`) to ECS
  rolling or blue/green deployments (`ECS`).

Consider the following when you update a service's deployment
controller:

- You can't update the deployment controller of a service from the
  `ECS` deployment controller to any of the other
  controllers if it uses VPC Lattice or Amazon ECS Service Connect.
- You can't update the deployment controller of a service during an
  ongoing service deployment.
- You can't update the deployment controller of a service to
  `CODE_DEPLOY` if there are no load balancers on the
  service.
- You can't update the deployment controller of a service from
  `ECS` to any of the other controllers if the
  `deploymentConfiguration` includes alarms, a deployment
  circuit breaker, or a `BLUE_GREEN` deployment strategy. For
  more information, see [Amazon ECS service deployment controllers and strategies](ecs_service-options.md "ecs_service-options.md").
- The value you specify for `versionConsistency` in the
  container definition won't be used by Amazon ECS if you update the deployment
  controller of the service from `ECS` to any of the other
  controllers.
- If you update a service's deployment controller from `ECS`
  to any of the other controllers, the `UpdateService` and
  `DescribeService` API responses will still return
  `deployments` instead of `taskSets`. For more
  information about `UpdateService` and
  `CreateService`, see [UpdateService](../APIReference/API_Service.md "../APIReference/API_Service.md") and [CreateService](../APIReference/API_Service.md "../APIReference/API_Service.md") in the _Amazon ECS API
  Reference_.
- If a service uses a rolling update deployment strategy, updating the
  deployment controller from `ECS` to any of the other
  controllers will change how the `maximumPercent` value in the
  `deploymentConfiguration` is used. Instead of just being
  used as a cap on total tasks in a rolling update deployment,
  `maximumPercent` is used for replacing unhealthy tasks.
  For more information on how the scheduler replaces unhealthy tasks, see
  [Amazon ECS services](ecs_services.md "ecs_services.md").
- If you update a service's deployment controller from `ECS`
  to any of the other deployment controllers, any
  `advancedConfiguration` that you specify with your load
  balancer configuration will be ignored. For more information, see [LoadBalancer](../APIReference/API_LoadBalancer.md "../APIReference/API_LoadBalancer.md") and [AdvancedConfiguration](../APIReference/API_AdvancedConfiguration.md "../APIReference/API_AdvancedConfiguration.md") in the _Amazon ECS API
  reference_.

When updating the deployment controller for a service using CloudFormation,
consider the following depending on the type of migration you're
performing.

- If you have a CloudFormation
  template that contains the `EXTERNAL` deployment controller
  information as well as `TaskSet` and
  `PrimaryTaskSet` resources, and you remove the task set
  resources from the template when updating from `EXTERNAL` to
  `ECS`, the `DescribeTaskSet` and
  `DeleteTaskSet` API calls will return a 400 error after
  the deployment controller is updated to `ECS`. This results
  in a CloudFormation delete failure on the task set resources, even though
  the CloudFormation stack transitions to `UPDATE_COMPLETE` status.
  For more information, see [Resource removed from stack but not deleted](../../../AWSCloudFormation/latest/UserGuide/troubleshooting.md#troubleshooting-errors-resource-removed-not-deleted "../../../AWSCloudFormation/latest/UserGuide/troubleshooting.md#troubleshooting-errors-resource-removed-not-deleted") in the
  AWS CloudFormation User Guide. To fix this issue, delete the task sets directly
  using the Amazon ECS `DeleteTaskSet` API. For more information
  about how to delete a task set, see [DeleteTaskSet](../APIReference/API_DeleteTaskSet.md "../APIReference/API_DeleteTaskSet.md") in the _Amazon Elastic Container Service_
  _API Reference_.
- If you're migrating from `CODE_DEPLOY` to `ECS`
  with a new task definition and CloudFormation performs a rollback operation,
  the Amazon ECS `UpdateService` request fails with the following
  error:

```
Resource handler returned message: "Invalid request provided: Unable to update
task definition on services with a CODE_DEPLOY deployment controller. Use AWS
CodeDeploy to trigger a new deployment. (Service: Ecs, Status Code: 400,
Request ID: 0abda1e2-f7b3-4e96-b6e9-c8bc585181ac) (SDK Attempt Count: 1)"
(RequestToken: ba8767eb-c99e-efed-6ec8-25011d9473f0, HandlerErrorCode: InvalidRequest)
```

- After a successful migration from `ECS` to `EXTERNAL` deployment controller, you need to manually remove the `ACTIVE` task
  set, because Amazon ECS no longer manages the deployment. For information about
  how to delete a task set, see [DeleteTaskSet](../APIReference/API_DeleteTaskSet.md "../APIReference/API_DeleteTaskSet.md") in the Amazon Elastic Container Service _API
  Reference_.

**Desired task count**

The number of instantiations of the task to place and keep running in your
service.

If you want to temporarily stop your service, set this value to 0. Then, when
you are ready to start the service, update the service with the original
value.

You can change this parameter for rolling deployments, and blue/green
deployments.

**Enable managed tags**

Determines whether to turn on Amazon ECS managed tags for the tasks in the
service.

Only tasks launched after the update will reflect the update. To update the
tags on all tasks, use the force deployment option.

You can change this parameter for rolling deployments, and blue/green
deployments.

**Enable ECS Exec**

Determines whether Amazon ECS Exec is used.

If you do not want to override the value that was set when the service was
created, you can set this to null when performing this action.

You can change this parameter for rolling deployments.

**Health check grace period**

The period of time, in seconds, that the Amazon ECS service scheduler ignores
unhealthy Elastic Load Balancing, VPC Lattice, and container health checks after a task has first
started. If you don't specify a health check grace period value, the default
value of `0` is used. If you don't use any of the health checks, then
`healthCheckGracePeriodSeconds` is unused.

If your service's tasks take a while to start and respond to health checks,
you can specify a health check grace period of up to 2,147,483,647 seconds
(about 69 years). During that time, the Amazon ECS service scheduler ignores health
check status. This grace period can prevent the service scheduler from marking
tasks as unhealthy and stopping them before they have time to come up.

You can change this parameter for rolling deployments and blue/green
deployments.

**Load balancers**

You must use a service-linked role when you update a load balancer.

A list of Elastic Load Balancing load balancer objects. It contains the load balancer name, the
container name, and the container port to access from the load balancer. The
container name is as it appears in a container definition.

Amazon ECS does not automatically update the security groups associated with Elastic Load Balancing
load balancers or Amazon ECS container instances.

When you add, update, or remove a load balancer configuration, Amazon ECS starts
new tasks with the updated Elastic Load Balancing configuration, and then stops the old tasks
when the new tasks are running.

For services that use rolling updates, you can add, update, or remove Elastic Load Balancing
target groups. You can update from a single target group to multiple target
groups and from multiple target groups to a single target group.

For services that use blue/green deployments, you can update Elastic Load Balancing target
groups by using `CreateDeployment` through CodeDeploy. Note that multiple
target groups are not supported for blue/green deployments. For more information
see [Register multiple target groups with a service](register-multiple-targetgroups.md "register-multiple-targetgroups.md").

For services that use the external deployment controller, you can add, update,
or remove load balancers by using [CreateTaskSet](../APIReference/API_CreateTaskSet.md "../APIReference/API_CreateTaskSet.md"). Note that multiple target groups are not supported
for external deployments. For more information see [Register multiple target groups with a service](register-multiple-targetgroups.md "register-multiple-targetgroups.md").

Pass an empty list to remove load balancers.

You can change this parameter for rolling deployments.

**Network configuration**

The service network configuration.

You can change this parameter for rolling deployments.

**Placement constraints**

An array of task placement constraint objects to update the service to use. If
no value is specified, the existing placement constraints for the service will
remain unchanged. If this value is specified, it will override any existing
placement constraints defined for the service. To remove all existing placement
constraints, specify an empty array.

You can specify a maximum of 10 constraints for each task. This limit includes
constraints in the task definition and those specified at runtime.

You can change this parameter for rolling deployments, and blue/green
deployments.

**Placement strategy**

The task placement strategy objects to update the service to use. If no value
is specified, the existing placement strategy for the service will remain
unchanged. If this value is specified, it will override the existing placement
strategy defined for the service. To remove an existing placement strategy,
specify an empty object.

You can change this parameter for rolling deployments, and blue/green
deployments.

**Platform version**

The Fargate platform version your service runs on.

A service using a Linux platform version cannot be updated to use a Windows
platform version and vice versa.

You can change this parameter for rolling deployments.

**Propagate tags**

Determines whether to propagate the tags from the task definition or the
service to the task. If no value is specified, the tags aren't
propagated.

Only tasks launched after the update will reflect the update. To update the
tags on all tasks, set `forceNewDeployment` to `true`, so
that Amazon ECS starts new tasks with the updated tags.

You can change this parameter for rolling deployments, and blue/green
deployments.

**Service Connect configuration**

The configuration for Amazon ECS Service Connect. This parameter determines how
the service connects to other services within your application.

You can change this parameter for rolling deployments.

**Service registries**

You must use a service-linked role when you update the service
registries.

The details for the service discovery registries to assign to this service.
For more information, see [Service
Discovery](service-discovery.md "service-discovery.md").

When you add, update, or remove the service registries configuration, Amazon ECS
starts new tasks with the updated service registries configuration, and then
stops the old tasks when the new tasks are running.

Pass an empty list to remove the service registries.

You can change this parameter for rolling deployments.

**Task definition**

The task definition and revision to use for the service.

If you change the ports used by containers in a task definition, you might
need to update the security groups for the container instances to work with the
updated ports.

If you update the task definition for the service, the container name and
container port that are specified in the load balancer configuration must remain
in the task definition.

The container image pull behavior differs for the compute options. For more
information, see one of the following:

- [Architect for AWS Fargate for Amazon ECS](AWS_Fargate.md "AWS_Fargate.md")
- [Architect for EC2 capacity for Amazon ECS](launch-type-ec2.md "launch-type-ec2.md")
- [External (Amazon ECS Anywhere) for Amazon ECS](launch-type-external.md "launch-type-external.md")

You can change this parameter for rolling deployments.

**Volume configuration**

The details of the volume that was `configuredAtLaunch`. When
`configuredAtLaunch` is set to `true` in the task
definition, this service parameter configures one Amazon EBS volume for each task in
the service to be created and attached during deployment. You can configure the
size, volumeType, IOPS, throughput, snapshot and encryption in [ServiceManagedEBSVolumeConfiguration](../APIReference/API_ServiceManagedEBSVolumeConfiguration.md "../APIReference/API_ServiceManagedEBSVolumeConfiguration.md"). The `name` of the
volume must match the `name` from the task definition. If set to
null, no new deployment is triggered. Otherwise, if this configuration differs
from the existing one, it triggers a new deployment.

You can change this parameter for rolling deployments.

**VPC Lattice configuration**

The VPC Lattice configuration for your service. This defines how your service
integrates with VPC Lattice for service-to-service communication.

You can change this parameter for rolling deployments.

## AWS CDK considerations

The AWS CDK doesn't track resource states. It doesn't know whether you are creating or
updating a service. Customers should use the escape hatch to access the ecs
`Service` L1 construct directly.

For information about escape hatches, see [Customize constructs from
the AWS Construct Library](../../../cdk/v2/guide/cfn-layer.md#develop-customize-escape "../../../cdk/v2/guide/cfn-layer.md#develop-customize-escape") in the _AWS Cloud Development Kit (AWS CDK) v2
Developer Guide_.

To migrate your existing service to the `ecs.Service` construct, do the
following:

1. Use the escape hatch to access the `Service` L1 construct.
2. Manually set the following properties in the `Service` L1
   construct.

If your service uses Amazon EC2 capacity:

    * `daemon?`
    * `placementConstraints?`
    * `placementStrategies?`
    * If you use the `awsvpc` network mode, you need to set the
     `vpcSubnets?` and the `securityGroups?`
     constructs.

If your service uses Fargate:

    * `FargatePlatformVersion`
    * The `vpcSubnets?` and the `securityGroups?`
     constructs.

3. Set the `launchType` as follows:

```
const cfnEcsService = service.node.findChild('Service') as ecs.CfnService;
cfnEcsService.launchType = "FARGATE";
```

To migrate from a launch type to a capacity provider, do the following:

1. Use the escape hatch to access the `Service` L1 construct.
2. Add the `capacityProviderStrategies?` construct.
3. Deploy the service.
