# Automatic instance recovery

###### Important

This section describes how to proactively configure recovery mechanisms on an EC2
instance. These recovery mechanisms are designed to restore instance availability when AWS
detects an underlying hardware or software issue that causes a system status check to fail.
If you are currently experiencing problems accessing your instance, see [Troubleshoot EC2 instances](ec2-instance-troubleshoot.md "ec2-instance-troubleshoot.md").

If AWS detects that an instance is unavailable due to an underlying hardware or software
issue, there are two mechanisms that can automatically restore instance
availability—[simplified automatic
recovery](instance-configuration-recovery.md "instance-configuration-recovery.md") and [Amazon CloudWatch action based recovery](cloudwatch-recovery.md "cloudwatch-recovery.md").
Restoring instance availability is also known as _instance
recovery_.

During the instance recovery process, AWS will attempt to move your instance from the host
with the underlying hardware or software issue to a different host. If successful, the instance
recovery process will appear to the instance as an unplanned reboot. You can [verify if instance recovery
occurred](verify-if-automatic-recovery-occurred.md "verify-if-automatic-recovery-occurred.md").

If the recovery process is unsuccessful, the instance might continue running on the host
with the underlying hardware or software issue. In this case, manual intervention is required.
If the instance becomes unreachable or the system status check continues to fail, we recommend
that you manually [stop and start](Stop_Start.md "Stop_Start.md") the instance. When you start
an instance, it is typically migrated to a new underlying host computer. However, unlike
automatic instance recovery, where the instance retains its public IPv4 address, a restarted
instance receives a new public IPv4 address unless it has an Elastic IP address.

To benefit from the automatic recovery mechanisms, they must be configured in advance on an
instance before a system status check fails. By default, simplified automatic recovery is
enabled during instance launch. You can optionally configure Amazon CloudWatch action based recovery
after launch. Having one of these mechanisms configured makes your instance more
resilient.

Simplified automatic recovery and Amazon CloudWatch action based recovery are only available on
supported instances. For more information, see [Requirements for enabling
simplified automatic recovery](instance-configuration-recovery.md#requirements-for-simplified-automatic-recovery "instance-configuration-recovery.md#requirements-for-simplified-automatic-recovery") and [Requirements for
enabling CloudWatch action based recovery](cloudwatch-recovery.md#requirements-for-cloudwatch-action-based-recovery "cloudwatch-recovery.md#requirements-for-cloudwatch-action-based-recovery").

###### Warning

When AWS recovers your instance due to an underlying hardware or software issue, be
aware of the following consequences: data stored in volatile memory (RAM) will be lost and the
operating system’s uptime will start over from zero. Furthermore, with CloudWatch action based
recovery, data on instance store volumes will also be lost. To help protect against data loss,
we recommend that you regularly create backups of valuable data. For more information about
backup and recovery best practices for EC2 instances, see [Best practices for Amazon EC2](ec2-best-practices.md "ec2-best-practices.md").

Automatic instance recovery mechanisms are designed for _individual
instances_. For guidance on building a resilient _system_, see [Build a resilient system](#instance-recovery-build-a-resilient-system "#instance-recovery-build-a-resilient-system").

###### Topics

- [Key concepts of automatic
  instance recovery](#ec2-automatic-instance-recovery-key-concepts "#ec2-automatic-instance-recovery-key-concepts")
- [Differences between simplified automatic recovery and CloudWatch
  action based recovery](#differences "#differences")
- [Build a resilient system](#instance-recovery-build-a-resilient-system "#instance-recovery-build-a-resilient-system")
- [Verify if automatic instance recovery
  occurred](verify-if-automatic-recovery-occurred.md "verify-if-automatic-recovery-occurred.md")
- [Configure simplified automatic recovery on
  an Amazon EC2 instance](instance-configuration-recovery.md "instance-configuration-recovery.md")
- [Configure CloudWatch action based recovery on an EC2 instance](cloudwatch-recovery.md "cloudwatch-recovery.md")

## Key concepts of automatic

instance recovery

Automatic instance recovery is an Amazon EC2 feature that automatically restores instance
availability when underlying hardware or software failures occur, enhancing the resilience and
reliability of your EC2 instances.

The following are key concepts of automatic instance recovery:

**Configuration options**

Two mechanisms can be configured to support automatic instance recovery:

- [Simplified automatic
  recovery](instance-configuration-recovery.md "instance-configuration-recovery.md"): Enabled by default on supported instances.
- [CloudWatch action based recovery](cloudwatch-recovery.md "cloudwatch-recovery.md"): Requires
  manual configuration on supported instances.

**System status checks**

System status checks automatically monitor the AWS infrastructure on which your
EC2 instance runs.

- If a system status check fails, AWS initiates automatic instance recovery,
  which attempts to migrate the affected instance to different hardware.
- A failed system status check indicates a problem with the host's hardware or
  software, and not a problem with the instance itself. Automatic instance recovery
  can recover an instance that fails a system status check. However, automatic
  instance recovery does not operate if only the instance status check fails.
- For the differences between instance and system status checks, see [Types of status checks](monitoring-system-instance-status-check.md#types-of-instance-status-checks "monitoring-system-instance-status-check.md#types-of-instance-status-checks").

**Examples of underlying hardware or software problems**

Hardware or software issues that can cause a system status check to fail include
loss of network connectivity, loss of system power, software issues on the physical
host, and hardware issues on the physical host that impact network reachability.

**Characteristics of recovered instances**

A recovered instance is identical to the original instance, except for the elements
that are lost.

Preserved elements:

- Instance ID
- Public, private, and Elastic IP addresses
- Instance metadata
- Placement group
- Attached EBS volumes
- Availability Zone

Lost elements:

- Data stored in volatile memory (RAM)
- Data stored on instance store volumes (applicable to CloudWatch action based recovery
  only)
- Operating system uptime resets to zero

**Monitoring system status checks with CloudWatch**

The [StatusCheckFailed_System](viewing_metrics_with_cloudwatch.md#status-check-metrics "viewing_metrics_with_cloudwatch.md#status-check-metrics") metric in
CloudWatch indicates whether a system status check passed or failed.

Metric values:

- **0** – The system status check passed.
- **1** – The system status check failed.

**Events in Health Dashboard**

During automatic instance recovery attempts, AWS sends events to your Health Dashboard based
on the configured recovery mechanism and its outcome:

- Simplified automatic recovery
  - Success event: `AWS_EC2_SIMPLIFIED_AUTO_RECOVERY_SUCCESS`
  - Failure event: `AWS_EC2_SIMPLIFIED_AUTO_RECOVERY_FAILURE`

- CloudWatch action based recovery
  - Success event: `AWS_EC2_INSTANCE_AUTO_RECOVERY_SUCCESS`
  - Failure event: `AWS_EC2_INSTANCE_AUTO_RECOVERY_FAILURE`

## Differences between simplified automatic recovery and CloudWatch

action based recovery

The following table compares the key differences between simplified automatic recovery and
CloudWatch action based recovery.

| Comparison point                          | Simplified automatic recovery                                            | CloudWatch action based recovery                                                                                    |
| ----------------------------------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------- |
| Configuration                             | Enabled by default on supported instances                                | Requires manual configuration of CloudWatch alarms and actions                                                      |
| Flexibility                               | Fixed recovery behavior managed by AWS                                   | Customizable actions and conditions                                                                                 |
| Notification                              | Basic notifications through Health Dashboard                             | Customizable notifications through SNS                                                                              |
| Metal instance size                       | Excluded                                                                 | Included                                                                                                            |
| Instance store volumes attached at launch | Not supported for instances that attach instance store volumes at launch | Supported on selected instance types. Note that data on instance store volumes is<br>lost during instance recovery. |
| Recovery time                             | Standard recovery attempt                                                | Faster recovery attempts than simplified automatic recovery                                                         |
| Host problem resolves during migration    | Migration might be canceled and the instance stays on the original host  | Migration continues to a new host                                                                                   |
| Cost                                      | No additional cost                                                       | Might incur CloudWatch charges                                                                                      |

## Build a resilient system

While simplified automatic recovery and CloudWatch action based recovery are effective for
maintaining individual instance availability, AWS recommends implementing a
high-availability architecture that allows failover of traffic to healthy instances.

To achieve this, consider using AWS services such as Elastic Load Balancing (which distributes
incoming traffic across multiple EC2 instances) and Amazon EC2 Auto Scaling (which automatically adjusts the
number of instances based on demand and health).

For more information about building a resilient, fault-tolerant system with EC2 instances,
see the following resources:

- [Back to Basics: Designing for
  Failure with EC2](https://www.youtube.com/watch?v=5Hq5YxOrKYs "https://www.youtube.com/watch?v=5Hq5YxOrKYs") on the _AWS YouTube
  channel_
- [Disaster Recovery (DR) Architecture on AWS, Part I: Strategies for Recovery in the
  Cloud](https://aws.amazon.com/blogs/architecture/disaster-recovery-dr-architecture-on-aws-part-i-strategies-for-recovery-in-the-cloud/ "https://aws.amazon.com/blogs/architecture/disaster-recovery-dr-architecture-on-aws-part-i-strategies-for-recovery-in-the-cloud/") on the _AWS Architecture Blog_
  site
- [Application Load
  Balancers User Guide](../../../elasticloadbalancing/latest/application/introduction.md "../../../elasticloadbalancing/latest/application/introduction.md")
- [Amazon EC2 Auto Scaling User
  Guide](../../../autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.md "../../../autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.md")
- [REL11-BP02 Fail over to healthy resources](../../../wellarchitected/latest/reliability-pillar/rel_withstand_component_failures_failover2good.md "../../../wellarchitected/latest/reliability-pillar/rel_withstand_component_failures_failover2good.md") in the _Reliability Pillar AWS Well-Architected Framework_
