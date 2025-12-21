# Control the instances Amazon ECS terminates

###### Important

You must turn on Auto Scaling _instance scale-in protection_ on the
Auto Scaling group to use the managed termination protection feature of cluster auto scaling.

Managed termination protection allows cluster auto scaling to control which instances are terminated.
When you used managed termination protection, Amazon ECS only terminates EC2 instances that
don't have any running Amazon ECS tasks. Tasks that are run by a service that uses the
`DAEMON` scheduling strategy are ignored and an instance can be
terminated by cluster auto scaling even when the instance is running these tasks. This is because all
of the instances in the cluster are running these tasks.

Amazon ECS first turns on the _instance scale-in protection_ option for
the EC2 instances in the Auto Scaling group. Then, Amazon ECS places the tasks on the instances. When all
non-daemon tasks are stopped on an instance, Amazon ECS initiates the scale-in process and
turns off scale-in protection for the EC2 instance. The Auto Scaling group can then terminate the
instance.

Auto Scaling _instance scale-in protection_ controls which EC2 instances
can be terminated by Auto Scaling. Instances with the scale-in feature turned on can't be
terminated during the scale-in process. For more information about Auto Scaling instance
scale-in protection, see [Using
instance scale-in protection](../../../autoscaling/ec2/userguide/ec2-auto-scaling-instance-protection.md "../../../autoscaling/ec2/userguide/ec2-auto-scaling-instance-protection.md") in the _Amazon EC2 Auto Scaling User
Guide_.

You can set the `targetCapacity` percentage so that you have spare
capacity. This helps future tasks launch more quickly because the Auto Scaling group does not have to
launch more instances. Amazon ECS uses the target capacity value to manage the CloudWatch metric
that the service creates. Amazon ECS manages the CloudWatch metric. The Auto Scaling group is treated as a
steady state so that no scaling action is required. The values can be from 0-100%. For
example, to configure Amazon ECS to keep 10% free capacity on top of that used by Amazon ECS
tasks, set the target capacity value to 90%. Consider the following when setting the
`targetCapacity` value on a capacity provider.

- A `targetCapacity` value of less than 100% represents the amount of
  free capacity (Amazon EC2 instances) that need to be present in the cluster. Free
  capacity means that there are no running tasks.
- Placement constraints such as Availability Zones, without additional
  `binpack` forces Amazon ECS to eventually run one task for each
  instance, which might not be the desired behavior.
  You must turn on Auto Scaling instance scale-in protection on the Auto Scaling group to use managed
  termination protection. If you don't turn on scale-in protection, then turning on
  managed termination protection can lead to undesirable behavior. For example, you may
  have instances stuck in draining state. For more information, see [Using
  instance scale-in protection](../../../autoscaling/ec2/userguide/ec2-auto-scaling-instance-protection.md "../../../autoscaling/ec2/userguide/ec2-auto-scaling-instance-protection.md") in the _Amazon EC2 Auto Scaling User
  Guide_.

When you use termination protection with a capacity provider, don't perform any manual
actions, like detaching the instance, on the Auto Scaling group associated with the capacity
provider. Manual actions can break the scale-in operation of the capacity provider. If
you detach an instance from the Auto Scaling group, you need to also [deregister
the detached instance](deregister_container_instance.md "deregister_container_instance.md") from the Amazon ECS cluster.
