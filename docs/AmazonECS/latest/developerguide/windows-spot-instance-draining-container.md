# Configuring Amazon ECS Windows container instances to receive Spot Instance notices

Amazon EC2 terminates, stops, or hibernates your Spot Instance when the Spot price exceeds the
maximum price for your request or capacity is no longer available. Amazon EC2 provides a
Spot Instance interruption notice, which gives the instance a two-minute warning before it is
interrupted. If Amazon ECS Spot Instance draining is enabled on the instance, ECS receives the
Spot Instance interruption notice and places the instance in `DRAINING`
status.

###### Important

Amazon ECS monitors for the Spot Instance interruption notices that have the
`terminate` and `stop` instance-actions. If you
specified either the `hibernate` instance interruption behavior when
requesting your Spot Instances or Spot Fleet, then Amazon ECS Spot Instance draining is not supported for
those instances.

When a container instance is set to `DRAINING`, Amazon ECS prevents new
tasks from being scheduled for placement on the container instance. Service tasks on
the draining container instance that are in the `PENDING` state are
stopped immediately. If there are container instances in the cluster that are
available, replacement service tasks are started on them.

You can turn on Spot Instance draining when you launch an instance. You must set the
`ECS_ENABLE_SPOT_INSTANCE_DRAINING` parameter before you start the
container agent. Replace `my-cluster` with the name of your
cluster.

```
[Environment]::SetEnvironmentVariable("ECS_ENABLE_SPOT_INSTANCE_DRAINING", "true", "Machine")

# Initialize the agent
Initialize-ECSAgent -Cluster `my-cluster`
```

For more information, see [Launching an Amazon ECS Windows container instance](launch_window-container_instance.md "launch_window-container_instance.md").
