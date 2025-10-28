# Status checks for Amazon EC2

instances

With instance status monitoring, you can quickly determine whether Amazon EC2 has detected
any problems that might prevent your instances from running applications. Amazon EC2 performs
automated checks on every running EC2 instance to identify hardware and software issues.
You can view the results of these status checks to identify specific and detectable
problems. The event status data augments the information that Amazon EC2 already provides
about the state of each instance (such as `pending`, `running`,
`stopping`) and the utilization metrics that Amazon CloudWatch monitors (CPU
utilization, network traffic, and disk activity).

Status checks are performed every minute, returning a pass or a fail status. If all
checks pass, the overall status of the instance is **OK**. If one or
more checks fail, the overall status is **impaired**. Status checks are
built into Amazon EC2, so they cannot be disabled or deleted.

When a status check fails, the corresponding CloudWatch metric for status checks is
incremented. For more information, see [Status check metrics](viewing_metrics_with_cloudwatch.md#status-check-metrics "viewing_metrics_with_cloudwatch.md#status-check-metrics"). You can use these metrics to create CloudWatch
alarms that are triggered based on the result of the status checks. For example, you can
create an alarm to warn you if status checks fail on a specific instance. For more
information, see [Create CloudWatch alarms for Amazon EC2
instances that fail status checks](creating_status_check_alarms.md "creating_status_check_alarms.md").

You can also create an Amazon CloudWatch alarm that monitors an Amazon EC2 instance and
automatically recovers the instance if it becomes impaired due to an underlying issue.
For more information, see [Automatic instance recovery](ec2-instance-recover.md "ec2-instance-recover.md").

###### Contents

- [Types of status checks](#types-of-instance-status-checks "#types-of-instance-status-checks")
- [View status checks for Amazon EC2 instances](viewing_status.md "viewing_status.md")
- [Create CloudWatch alarms for Amazon EC2
  instances that fail status checks](creating_status_check_alarms.md "creating_status_check_alarms.md")

## Types of status checks

There are three types of status checks.

- [System status checks](#system-status-checks "#system-status-checks")
- [Instance status checks](#instance-status-checks "#instance-status-checks")
- [Attached EBS status checks](#attached-ebs-status-checks "#attached-ebs-status-checks")

### System status checks

System status checks monitor the AWS systems on which your instance runs.
These checks detect underlying problems with your instance that require AWS
involvement to repair. When a system status check fails, you can choose to wait
for AWS to fix the issue, or you can resolve it yourself. For instances backed
by Amazon EBS, you can stop and start the instance yourself, which in most cases
results in the instance being migrated to a new host. For instances backed by
instance store (supported only for Linux instances), you can terminate and
replace the instance. Note that instance store volumes are ephemeral and all
data is lost when the instance is stopped.

The following are examples of problems that can cause system status checks to
fail:

- Loss of network connectivity
- Loss of system power
- Software issues on the physical host
- Hardware issues on the physical host that impact network
  reachability

If a system status check fails, we increment the [StatusCheckFailed_System](viewing_metrics_with_cloudwatch.md#status-check-metrics "viewing_metrics_with_cloudwatch.md#status-check-metrics")
metric.

###### Bare metal instances

If you perform a restart from the operating system on a bare metal
instance, the system status check might temporarily return a fail status.
When the instance becomes available, the system status check should return a
pass status.

### Instance status checks

Instance status checks monitor the software and network connectivity of your
individual instance. Amazon EC2 checks the health of the instance by sending an
address resolution protocol (ARP) request to the network interface (NIC). These
checks detect problems that require your involvement to repair. When an instance
status check fails, you typically must address the problem yourself (for
example, by rebooting the instance or by making instance configuration
changes).

###### Note

Recent Linux distributions that use `systemd-networkd` for
network configuration might report on health checks differently from earlier
distributions. During the boot process, this type of network can start
earlier and potentially finish before other startup tasks that can also
affect instance health. Status checks that depend on network availability
can report a healthy status before other tasks complete.

The following are examples of problems that can cause instance status checks
to fail:

- Failed system status checks
- Incorrect networking or startup configuration
- Exhausted memory
- Corrupted file system
- Incompatible kernel
- During a reboot, an instance status check reports a failure until the
  instance becomes available again.

If an instance status check fails, we increment the [StatusCheckFailed_Instance](viewing_metrics_with_cloudwatch.md#status-check-metrics "viewing_metrics_with_cloudwatch.md#status-check-metrics")
metric.

###### Bare metal instances

If you perform a restart from the operating system on a bare metal
instance, the instance status check might temporarily return a fail status.
When the instance becomes available, the instance status check should return
a pass status.

### Attached EBS status checks

Attached EBS status checks monitor if the Amazon EBS volumes attached to an
instance are reachable and able to complete I/O operations. The
`StatusCheckFailed_AttachedEBS` metric is a binary value that
indicates impairment if one or more of the EBS volumes attached to the instance
are unable to complete I/O operations. These status checks detect underlying
issues with the compute or Amazon EBS infrastructure. When the attached EBS status
check metric fails, you can either wait for AWS to resolve the issue, or you
can take actions, such as replacing the affected volumes or stopping and
restarting the instance.

The following are examples of issues that can cause attached EBS status checks
to fail:

- Hardware or software issues on the storage subsystems underlying the
  EBS volumes
- Hardware issues on the physical host that impact reachability of the
  EBS volumes
- Connectivity issues between the instance and EBS volumes

You can use the `StatusCheckFailed_AttachedEBS` metric to help
improve the resilience of your workload. You can use this metric to create
Amazon CloudWatch alarms that are triggered based on the result of the status check. For
example, you could fail over to a secondary instance or Availability Zone when
you detect a prolonged impact. Alternatively, you can monitor the I/O
performance of each attached volume using EBS CloudWatch metrics to detect and
replace the impaired volume. If your workload is not driving I/O to any EBS
volumes attached to your instance, and the EBS status check indicates an
impairment, you can stop and start the instance to move it to a new host. This
can resolve underlying host issues that are impacting the reachability of the
EBS volumes. For more information, see [Amazon CloudWatch metrics for
Amazon EBS](../../../ebs/latest/userguide/using_cloudwatch_ebs.md "../../../ebs/latest/userguide/using_cloudwatch_ebs.md").

You can also configure your Amazon EC2 Auto Scaling groups to detect attached EBS status
check failures, and then replace the affected instance with a new one. For more
information, see [Monitor and replace Auto Scaling instances with impaired Amazon EBS volumes](../../../autoscaling/ec2/userguide/monitor-and-replace-instances-with-impaired-ebs-volumes.md "../../../autoscaling/ec2/userguide/monitor-and-replace-instances-with-impaired-ebs-volumes.md") in
the _Amazon EC2 Auto Scaling User Guide_.

###### Note

The attached EBS status check metric is available only for Nitro
instances.
