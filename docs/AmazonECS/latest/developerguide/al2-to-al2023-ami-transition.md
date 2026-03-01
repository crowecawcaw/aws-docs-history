# Migrating from an Amazon Linux 2 to an Amazon Linux 2023 Amazon ECS-optimized AMI

Following [Amazon Linux](https://aws.amazon.com/amazon-linux-2/faqs "https://aws.amazon.com/amazon-linux-2/faqs"),
Amazon ECS ends standard support for Amazon Linux 2 Amazon ECS-optimized AMIs effective June 30, 2026.
After this date, the Amazon ECS agent version is pinned and new Amazon Linux 2 Amazon ECS-optimized AMIs
are only published when the source Amazon Linux 2 AMI is updated. Complete End of Life (EOL) occurs
on June 30, 2026, after which no more Amazon ECS-optimized Amazon Linux 2 AMIs are published,
even if the source AMI is updated.

Amazon Linux 2023 provides a secure-by-default approach with preconfigured security policies, SELinux
in permissive mode, IMDSv2-only mode enabled by default, optimized boot times, and improved
package management for enhanced security and performance.

There is a high degree of compatibility between the Amazon Linux 2 and Amazon Linux 2023 Amazon ECS-optimized
AMIs, and most customers will experience minimal-to-zero changes in their workloads between
the two operating systems.

For more information, see [Comparing Amazon Linux 2 and _Amazon Linux 2023_](../../../linux/al2023/ug/compare-with-al2.md "../../../linux/al2023/ug/compare-with-al2.md") in the _Amazon Linux 2023 User
Guide_ and the [AL2023 FAQs](https://aws.amazon.com/linux/amazon-linux-2023/faqs "https://aws.amazon.com/linux/amazon-linux-2023/faqs").

## Compatibility considerations

### Package management and OS updates

Unlike previous versions of Amazon Linux, Amazon ECS-optimized Amazon Linux 2023 AMIs are locked to a specific
version of the Amazon Linux repository. This insulates users from inadvertently
updating packages that might bring in unwanted or breaking changes. For more
information, see [Managing repositories and
OS updates in Amazon Linux 2023](../../../linux/al2023/ug/managing-repos-os-updates.md "../../../linux/al2023/ug/managing-repos-os-updates.md") in the _Amazon Linux 2023
User Guide_.

### Linux kernel versions

Amazon Linux 2 AMIs are based on Linux kernels 4.14 and 5.10, while Amazon Linux 2023 uses Linux
kernel 6.1 and 6.12. For more information, see [Comparing Amazon Linux 2 and
Amazon Linux 2023 kernels](../../../linux/al2023/ug/compare-with-al2-kernel.md "../../../linux/al2023/ug/compare-with-al2-kernel.md") in the _Amazon Linux 2023 User
Guide_.

### Package availability changes

The following are notable package changes in Amazon Linux 2023:

- Some source binary packages in Amazon Linux 2 are no longer available in Amazon Linux 2023.
  For more information, see [Packages removed from
  Amazon Linux 2023](../../../linux/al2023/release-notes/removed.md "../../../linux/al2023/release-notes/removed.md") in the _Amazon Linux 2023 Release
  Notes_.
- Changes in how Amazon Linux supports different versions of packages. The
  `amazon-linux-extras` system used in Amazon Linux 2 does not exist in
  Amazon Linux 2023. All packages are simply available in the "core" repository.
- Extra packages for Enterprise Linux (EPEL) are not supported in Amazon Linux 2023.
  For more information, see [EPEL compatibility in
  Amazon Linux 2023](../../../linux/al2023/ug/epel.md "../../../linux/al2023/ug/epel.md") in the _Amazon Linux 2023 User
  Guide_.
- 32-bit applications are not supported in Amazon Linux 2023. For more information,
  see [Deprecated features from Amazon Linux 2](../../../linux/al2023/ug/deprecated-al2.md#deprecated-32bit-rpms "../../../linux/al2023/ug/deprecated-al2.md#deprecated-32bit-rpms") in the _Amazon Linux 2023 User Guide_.

### Control Groups (cgroups) changes

A Control Group (cgroup) is a Linux kernel feature to hierarchically organize
processes and distribute system resources between them. Control Groups are used
extensively to implement a container runtime, and by `systemd`.

The Amazon ECS agent, Docker, and containerd all support both cgroupv1 and cgroupv2.
Amazon ECS agent and the container runtime manage cgroups for you, so Amazon ECS customers do
not need to make any changes for this underlying cgroup upgrade.

For further details on cgroupv2, see [Control groups v2 in Amazon Linux 2023](../../../linux/al2023/ug/cgroupv2.md "../../../linux/al2023/ug/cgroupv2.md") in
the _Amazon Linux 2023 User Guide_.

### Instance Metadata Service (IMDS) changes

Amazon Linux 2023 requires Instance Metadata Service version 2 (IMDSv2) by default. IMDSv2 has several benefits that help improve
security posture. It uses a session-oriented authentication method that requires the
creation of a secret token in a simple HTTP PUT request to start the session. A
session's token can be valid for anywhere between 1 second and 6 hours.

For more information on how to transition from IMDSv1 to IMDSv2, see [Transition to using Instance Metadata Service Version 2](../../../AWSEC2/latest/UserGuide/instance-metadata-transition-to-version-2.md "../../../AWSEC2/latest/UserGuide/instance-metadata-transition-to-version-2.md") in the
_Amazon EC2 User Guide_.

If you would like to use IMDSv1, you can still do so by manually overriding the
settings using instance metadata option launch properties.

### Memory swappiness changes

Per-container memory swappiness is not supported on Amazon Linux 2023 and cgroups v2. For
more information, see [Managing container swap memory space on Amazon ECS](container-swap.md "container-swap.md").

### FIPS validation changes

Amazon Linux 2 is certified under FIPS 140-2 and Amazon Linux 2023 is certified under FIPS
140-3.

To enable FIPS mode on Amazon Linux 2023, install the necessary packages on your Amazon EC2
instance and follow the configuration steps using the instructions in [Enable FIPS Mode on
Amazon Linux 2023](../../../linux/al2023/ug/fips-mode.md "../../../linux/al2023/ug/fips-mode.md") in the _Amazon Linux 2023 User
Guide_.

### Accelerated instance support

The Amazon ECS-optimized Amazon Linux 2023 AMIs support both Neuron and GPU accelerated instance types. For more
information, see [Amazon ECS-optimized Linux AMIs](ecs-optimized_AMI.md "ecs-optimized_AMI.md").

## Building custom AMIs

While we recommend moving to officially supported and published Amazon ECS-optimized AMIs
for Amazon Linux 2023, you can continue to build custom Amazon Linux 2 Amazon ECS-optimized AMIs using the
open-source build scripts that are used to build the Linux variants of the
Amazon ECS-optimized AMI. For more information, see [Amazon ECS-optimized Linux AMI build script](ecs-ami-build-scripts.md "ecs-ami-build-scripts.md").

## Migration strategies

We recommend creating and implementing a migration plan that includes thorough
application testing. The following sections outline different migration strategies based
on how you manage your Amazon ECS infrastructure.

### Migrating with Amazon ECS capacity providers

1. Create a new capacity provider with a new launch template. This should
   reference an Auto Scaling group with a launch template similar to your
   existing one, but instead of the Amazon Linux 2 Amazon ECS-optimized AMI, it should
   specify one of the Amazon Linux 2023 variants. Add this new capacity provider to your
   existing Amazon ECS cluster.
2. Update your cluster's default capacity provider strategy to include both
   the existing Amazon Linux 2 capacity provider and the new Amazon Linux 2023 capacity provider.
   Start with a higher weight on the Amazon Linux 2 provider and a lower weight on the
   Amazon Linux 2023 provider (for example, Amazon Linux 2: weight 80, Amazon Linux 2023: weight 20). This
   causes Amazon ECS to begin provisioning Amazon Linux 2023 instances as new tasks are
   scheduled. Verify that the instances register correctly and that tasks are
   able to run successfully on the new instances.
3. Gradually adjust the capacity provider weights in your cluster's default
   strategy, increasing the weight for the Amazon Linux 2023 provider while decreasing
   the Amazon Linux 2 provider weight over time (for example, 60/40, then 40/60, then
   20/80). You can also update individual service capacity provider strategies
   to prioritize Amazon Linux 2023 instances. Monitor task placement to ensure they're
   successfully running on Amazon Linux 2023 instances.
4. Optionally drain Amazon Linux 2 container instances to accelerate task migration.
   If you have sufficient Amazon Linux 2023 replacement capacity, you can manually drain
   your Amazon Linux 2 container instances through the Amazon ECS console or AWS CLI to speed
   up the transition of your tasks from Amazon Linux 2 to Amazon Linux 2023. After the migration
   is complete, remove the Amazon Linux 2 capacity provider from your cluster and delete
   the associated Auto Scaling group.

### Migrating with an Amazon EC2 Auto Scaling group

1. Create a new Amazon EC2 Auto Scaling group with a new launch template. This
   should be similar to your existing launch template, but instead of the Amazon Linux 2
   Amazon ECS-optimized AMI, it should specify one of the Amazon Linux 2023 variants. This new
   Auto Scaling group can launch instances to your existing cluster.
2. Scale up the Auto Scaling group so that you begin to have Amazon Linux 2023
   instances registering to your cluster. Verify that the instances register
   correctly and that tasks are able to run successfully on the new
   instances.
3. After your tasks have been verified to work on Amazon Linux 2023, scale up the
   Amazon Linux 2023 Auto Scaling group while gradually scaling down the Amazon Linux 2 Auto Scaling group, until you have completely replaced all Amazon Linux 2
   instances.
4. If you have sufficient Amazon Linux 2023 replacement capacity, you might want to
   explicitly drain the container instances to speed up the transition
   of your tasks from Amazon Linux 2 to Amazon Linux 2023. For more information, see [Draining Amazon ECS container instances](container-instance-draining.md "container-instance-draining.md").

### Migrating with manually managed instances

1. Manually launch (or adjust scripts that launch) new Amazon EC2 instances using
   the Amazon ECS-optimized Amazon Linux 2023 AMI instead of Amazon Linux 2. Ensure these instances use the same
   security groups, subnets, IAM roles, and cluster configuration as your
   existing Amazon Linux 2 instances. The instances should automatically register to
   your existing Amazon ECS cluster upon launch.
2. Verify the new Amazon Linux 2023 instances are successfully registering to your
   Amazon ECS cluster and are in an `ACTIVE` state. Test that tasks can
   be scheduled and run properly on these new instances by either waiting for
   natural task placement or manually stopping/starting some tasks to trigger
   rescheduling.
3. Gradually replace your Amazon Linux 2 instances by launching additional Amazon Linux 2023
   instances as needed, then manually draining and terminating the Amazon Linux 2
   instances one by one. You can drain instances through the Amazon ECS console by
   setting the instance to `DRAINING` status, which will stop placing new tasks
   on it and allow existing tasks to finish or be rescheduled elsewhere.
