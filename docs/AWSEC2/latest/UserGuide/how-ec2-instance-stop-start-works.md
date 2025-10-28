# How EC2 instance stop and start

works

When you stop an Amazon EC2 instance, changes are registered at the operating system (OS)
level of the instance, some resources are lost, and some resources persist. When you
start an instance, changes are registered at the instance level.

###### Topics

- [What happens when you stop an instance](#what-happens-stop "#what-happens-stop")
- [What happens when you start an instance](#what-happens-start "#what-happens-start")
- [Test application response to stop and
  start](#test-stop-start-instance "#test-stop-start-instance")
- [Costs related to instance stop and
  start](#ec2-stop-start-costs "#ec2-stop-start-costs")

## What happens when you stop an instance

The following describes what typically happens when you stop an instance using the
default stop method. Note that some aspects might vary depending on which [stop method](instance-stop-methods.md "instance-stop-methods.md") you use.

###### Changes registered at the OS level

- The API request sends a button press event to the guest.
- Various system services are stopped as a result of the button press event.
  Graceful OS shutdown is triggered by the ACPI shutdown button press event
  from the hypervisor.
- ACPI shutdown is initiated.
- The instance shuts down when the graceful OS shutdown process exits. There
  is no configurable OS shutdown time.
- If the instance OS does not cleanly shut down within a few minutes, a hard
  shutdown is performed.
- The instance stops running.
- The instance state changes to `stopping` and then
  `stopped`.
- [Auto Scaling] If your instance is in an Auto Scaling group, when the instance is in any
  Amazon EC2 state other than `running`, or if its status for the status
  checks becomes `impaired`, Amazon EC2 Auto Scaling considers the instance to be
  unhealthy and replaces it. For more information, see [Health checks for
  instances in an Auto Scaling group](../../../autoscaling/ec2/userguide/ec2-auto-scaling-health-checks.md "../../../autoscaling/ec2/userguide/ec2-auto-scaling-health-checks.md") in the
  _Amazon EC2 Auto Scaling User Guide_.
- [Windows instances] When you stop and start a Windows instance, the launch
  agent performs tasks on the instance, such as changing the drive letters for
  any attached Amazon EBS volumes. For more information about these defaults and
  how you can change them, see [Use the EC2Launch v2 agent to perform tasks during EC2 Windows
  instance launch](ec2launch-v2.md "ec2launch-v2.md").

###### Resources lost

- Data stored on the RAM.
- Data stored on the instance store volumes.
- The public IPv4 address that Amazon EC2 automatically assigned to the instance
  upon launch or start. To retain a public IPv4 address that never changes,
  you can associate an [Elastic IP
  address](elastic-ip-addresses-eip.md "elastic-ip-addresses-eip.md") with your instance.

###### Resources that persist

- Any attached Amazon EBS root and data volumes.
- Data stored on the Amazon EBS volumes.
- Any attached [network interfaces](using-eni.md "using-eni.md").

A network interface includes the following resources, which also
persist:

    + Private IPv4 addresses.
    + IPv6 addresses.
    + Elastic IP addresses associated with the instance. Note that when
     the instance is stopped, you are [charged
     for the associated Elastic IP addresses](elastic-ip-addresses-eip.md#eip-pricing "elastic-ip-addresses-eip.md#eip-pricing").

The following diagram illustrates what persists and what is lost when an EC2
instance is stopped. The diagram is divided into three parts: the first part,
labeled **Running EC2 instance**, shows the instance in the
`running` state with its resources. The second part, labeled
**Stopped EC2 instance**, shows the instance in the
`stopped` state with the resources that persist. The third part,
labeled **Lost**, shows the resources that are lost when the
instance is stopped.

![The public IPv4 address, RAM, and instance storage data are lost when an instance is stopped.](images/stop-instance.png)

For information about what happens when you stop a Mac instance,
see [Stop or terminate your Amazon EC2 Mac instance](mac-instance-stop.md "mac-instance-stop.md").

## What happens when you start an instance

- In most cases, the instance is migrated to a new underlying host computer
  (though in some cases, such as when an instance is allocated to a host in a
  [Dedicated Host](dedicated-hosts-understanding.md "dedicated-hosts-understanding.md")
  configuration, it remains on the current host).
- The associated EBS volumes and network interfaces are reattached to the
  instance.
- Amazon EC2 assigns a new public IPv4 address to the instance if the instance is
  configured to receive a public IPv4 address, unless it has a secondary
  network interface or a secondary private IPv4 address that is associated
  with an Elastic IP address.

## Test application response to stop and

start

You can use AWS Fault Injection Service to test how your application responds when your instance
is stopped and started. For more information, see the [AWS Fault Injection Service User
Guide](../../../fis/latest/userguide/what-is.md "../../../fis/latest/userguide/what-is.md").

## Costs related to instance stop and

start

The following costs are associated with stopping and starting an instance.

**Stopping** – As soon as the state of an
instance changes to `shutting-down` or `terminated`, charges
are no longer incurred for the instance. You are not charged for usage or data
transfer fees for a stopped instance. Charges are incurred to store Amazon EBS storage
volumes.

**Starting** – Each time you start a stopped
instance, you are charged for a minimum of one minute of usage. After one minute,
you are charged for only the seconds you use. For example, if you run an instance
for 20 seconds and then stop it, you are charged for a minute of usage. If you run
an instance for 3 minutes and 40 seconds, you are charged for 3 minutes and 40
seconds of usage.
