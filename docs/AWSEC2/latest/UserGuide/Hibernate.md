# Hibernate your Amazon EC2 instance

When you hibernate an instance, Amazon EC2 signals the operating system to perform hibernation
(suspend-to-disk). Hibernation saves the contents from the instance memory (RAM) to your
Amazon Elastic Block Store (Amazon EBS) root volume. Amazon EC2 persists the instance's EBS root volume and any
attached EBS data volumes. When your instance is started:

- The EBS root volume is restored to its previous state
- The RAM contents are reloaded
- The processes that were previously running on the instance are resumed
- Previously attached data volumes are reattached and the instance retains its
  instance ID
  You can hibernate an instance only if it's [enabled
  for hibernation](enabling-hibernation.md "enabling-hibernation.md") and it meets the [hibernation prerequisites](hibernating-prerequisites.md "hibernating-prerequisites.md").

If an instance or application takes a long time to bootstrap and build a memory footprint
in order to become fully productive, you can use hibernation to pre-warm the instance. To
pre-warm the instance, you:

1. Launch it with hibernation enabled.
2. Bring it to a desired state.
3. Hibernate it so that it's ready to be resumed to the desired state whenever
   needed.
   You're not charged for instance usage for a hibernated instance when it is in the
   `stopped` state or for data transfer when the contents of the RAM are
   transferred to the EBS root volume. You are charged for storage of any EBS volumes,
   including storage for the RAM contents.

If you no longer need an instance, you can terminate it at any time, including when it is
in a `stopped` (hibernated) state. For more information, see [Terminate Amazon EC2 instances](terminating-instances.md "terminating-instances.md").

###### Contents

- [How it works](instance-hibernate-overview.md "instance-hibernate-overview.md")
- [Prerequisites](hibernating-prerequisites.md "hibernating-prerequisites.md")
- [Configure a Linux AMI to support
  hibernation](hibernation-enabled-AMI.md "hibernation-enabled-AMI.md")
- [Enable instance
  hibernation](enabling-hibernation.md "enabling-hibernation.md")
- [Disable KASLR on an instance (Ubuntu
  only)](hibernation-disable-kaslr.md "hibernation-disable-kaslr.md")
- [Hibernate an instance](hibernating-instances.md "hibernating-instances.md")
- [Start a hibernated
  instance](hibernating-resuming.md "hibernating-resuming.md")
- [Troubleshoot](troubleshoot-instance-hibernate.md "troubleshoot-instance-hibernate.md")
