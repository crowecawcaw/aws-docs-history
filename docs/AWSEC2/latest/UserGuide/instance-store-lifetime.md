# Data persistence for Amazon EC2 instance store volumes

Instance store volumes are attached only at instance launch. You can't attach instance
store volumes after launch. You can’t detach an instance store volume from one instance and
attach it to a different instance.

An instance store volume exists only during the lifetime of the instance to which it is
attached. You can’t configure an instance store volume to persist beyond the lifetime of its
associated instance.

The data on an instance store volume persists even if the instance is rebooted. However,
the data does not persist if the instance is stopped, hibernated, or terminated. When the
instance is stopped, hibernated, or terminated, every block of the instance store volume is
cryptographically erased.

Therefore, do not rely on instance store volumes for valuable, long-term data. If you
need to retain the data stored on an instance store volume beyond the lifetime of the instance,
you need to manually copy that data to more persistent storage, such as an Amazon EBS volume, an
Amazon S3 bucket, or an Amazon EFS file system.

There are some events that can result in your data not persisting throughout the
lifetime of the instance. The following table indicates whether data on instance store
volumes is persisted during specific events, for both virtualized and bare metal
instances.

| Event                                                                                                                                           | What happens to your data?                                       |
| ----------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **User-initiated instance lifecycle events**                                                                                                    |
| [The instance is rebooted](ec2-instance-reboot.md "ec2-instance-reboot.md")                                                                     | The data persists                                                |
| [The instance is stopped](Stop_Start.md "Stop_Start.md")                                                                                        | The data does not persist                                        |
| [The instance is hibernated](Hibernate.md "Hibernate.md")                                                                                       | The data does not persist                                        |
| [The instance is terminated](terminating-instances.md "terminating-instances.md")                                                               | The data does not persist                                        |
| [The instance type is changed](ec2-instance-resize.md "ec2-instance-resize.md")                                                                 | The data does not persist \*                                     |
| [An EBS-backed AMI is created from the instance](creating-an-ami-ebs.md "creating-an-ami-ebs.md")                                               | The data does not persist in the created AMI \*\*                |
| [An Amazon S3-backed AMI is created from the instance](creating-an-ami-instance-store.md "creating-an-ami-instance-store.md") (Linux instances) | The data persists in the AMI bundle uploaded to Amazon S3 \*\*\* |
| **User-initiated OS events**                                                                                                                    |
| A shutdown is initiated                                                                                                                         | The data does not persist †                                      |
| A restart is initiated                                                                                                                          | The data persists                                                |
| **AWS scheduled events**                                                                                                                        |
| [Instance stop](schedevents_actions_retire.md "schedevents_actions_retire.md")                                                                  | The data does not persist                                        |
| [Instance reboot](schedevents_actions_reboot.md "schedevents_actions_reboot.md")                                                                | The data persists                                                |
| [System reboot](schedevents_actions_reboot.md "schedevents_actions_reboot.md")                                                                  | The data persists                                                |
| [Instance retirement](schedevents_actions_retire.md "schedevents_actions_retire.md")                                                            | The data does not persist                                        |
| **Unplanned events**                                                                                                                            |
| [Simplified automatic recovery](instance-configuration-recovery.md "instance-configuration-recovery.md")                                        | The data does not persist                                        |
| [CloudWatch action based recovery](cloudwatch-recovery.md "cloudwatch-recovery.md")                                                             | The data does not persist                                        |
| The underlying disk fails                                                                                                                       | The data on the failed disk does not persist                     |
| Power failure                                                                                                                                   | The data persists upon reboot                                    | \* If the new instance type supports instance store, the instance gets the number of instance store volumes supported by the new instance type, but the data does not transfer to the new instance. If the new instance type does not support instance store, the instance does not get the instance store volumes. \*\* The data is not included in the EBS-backed AMI, and it is not included on instance store volumes attached to instances launched from that AMI. \*\*\* The data is included in the AMI bundle that is uploaded to Amazon S3. When you launch an instance from that AMI, the instance gets the instance store volumes bundled in the AMI with the data they contained at the time the AMI was created. † Termination protection and stop protection do not protect instances against instance stops or terminations as a result of shutdowns initiated through the operating system on the instance. Data stored on instance store volumes does not persist in both instance stop and termination events. |
