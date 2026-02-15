# An EC2 instance in AWS PCS is terminated and replaced after reboot

###### Problem overview

After an EC2 instance in a compute node group is rebooted, AWS PCS automatically terminates and replaces
the instance.

###### Why this happens

AWS PCS doesn't support instance reboots. If an EC2 instance is rebooted, AWS PCS considers the instance
unhealthy and replaces it. If AWS PCS continuously terminates
and replaces your instances, it might be because something reboots your instances after they launch.
Some examples include reboots by automation on the EC2 instance (such as an automatic reboot after patching),
automation external to the EC2 instance (such as a network management application), another AWS service (such as AWS Systems Manager),
or a manual reboot by a person.

###### What to do

You can check your `slurmctld` or `slurmd` logs to see if your instance was rebooted.
For more information, see
[Scheduler logs in AWS PCS](monitoring_scheduler-logs.md "monitoring_scheduler-logs.md")
and [Monitoring AWS PCS instances using
Amazon CloudWatch](monitoring-cloudwatch_instances.md "monitoring-cloudwatch_instances.md").
The following example `slurmctld` log entry indicates that the instance rebooted:

###### Example

```
[2024-09-12T06:42:50.393+00:00] validate_node_specs: Node Login-1 unexpectedly rebooted boot_time=1726123354 last response=1726123285
```

###### Rebooting because of patching

A reboot is often required after you apply patches. Don't apply patches directly to an EC2 instance that is part of a
AWS PCS compute node group.
If you must patch your EC2 instances, you should apply your patches to an updated Amazon Machine Image (AMI)
and update your compute node groups to use the updated AMI. New EC2 instances that AWS PCS launches for those compute node groups
will use the updated (patched) AMI. For more information, see [Custom Amazon Machine Images (AMIs) for
AWS PCS](working-with_ami_custom.md "working-with_ami_custom.md").
