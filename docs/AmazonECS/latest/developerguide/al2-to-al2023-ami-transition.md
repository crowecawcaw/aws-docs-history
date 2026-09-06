

# Migrating from an Amazon Linux 2 to an Amazon Linux 2023 Amazon ECS-optimized AMI
<a name="al2-to-al2023-ami-transition"></a>

Following [Amazon Linux](https://aws.amazon.com/amazon-linux-2/faqs), Amazon ECS ends standard support for Amazon Linux 2 Amazon ECS-optimized AMIs effective June 30, 2026. After this date, the Amazon ECS agent version is pinned and new Amazon Linux 2 Amazon ECS-optimized AMIs are only published when the source Amazon Linux 2 AMI is updated. Complete End of Life (EOL) occurs on June 30, 2026, after which no more Amazon ECS-optimized Amazon Linux 2 AMIs are published, even if the source AMI is updated.

Amazon Linux 2023 provides a secure-by-default approach with preconfigured security policies, SELinux in permissive mode, IMDSv2-only mode enabled by default, optimized boot times, and improved package management for enhanced security and performance.

There is a high degree of compatibility between the Amazon Linux 2 and Amazon Linux 2023 Amazon ECS-optimized AMIs, and most customers will experience minimal-to-zero changes in their workloads between the two operating systems.

For more information, see [Comparing Amazon Linux 2 and *Amazon Linux 2023*](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html) in the *Amazon Linux 2023 User Guide* and the [AL2023 FAQs](https://aws.amazon.com/linux/amazon-linux-2023/faqs).

## Compatibility considerations
<a name="al2-to-al2023-ami-transition-compatibility"></a>

### Package management and OS updates
<a name="al2-to-al2023-ami-transition-compatibility-package-management"></a>

Unlike previous versions of Amazon Linux, Amazon ECS-optimized Amazon Linux 2023 AMIs are locked to a specific version of the Amazon Linux repository. This insulates users from inadvertently updating packages that might bring in unwanted or breaking changes. For more information, see [Managing repositories and OS updates in Amazon Linux 2023](https://docs.aws.amazon.com/linux/al2023/ug/managing-repos-os-updates.html) in the *Amazon Linux 2023 User Guide*.

### Linux kernel versions
<a name="al2-to-al2023-ami-transition-compatibility-kernel"></a>

Amazon Linux 2 AMIs are based on Linux kernels 4.14 and 5.10, while Amazon Linux 2023 uses Linux kernel 6.1 and 6.12. For more information, see [Comparing Amazon Linux 2 and Amazon Linux 2023 kernels](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2-kernel.html) in the *Amazon Linux 2023 User Guide*.

### Package availability changes
<a name="al2-to-al2023-ami-transition-compatibility-packages"></a>

The following are notable package changes in Amazon Linux 2023:
+ Some source binary packages in Amazon Linux 2 are no longer available in Amazon Linux 2023. For more information, see [Packages removed from Amazon Linux 2023](https://docs.aws.amazon.com/linux/al2023/release-notes/removed.html) in the *Amazon Linux 2023 Release Notes*.
+ Changes in how Amazon Linux supports different versions of packages. The `amazon-linux-extras` system used in Amazon Linux 2 does not exist in Amazon Linux 2023. All packages are simply available in the "core" repository.
+ Extra packages for Enterprise Linux (EPEL) are not supported in Amazon Linux 2023. For more information, see [EPEL compatibility in Amazon Linux 2023](https://docs.aws.amazon.com/linux/al2023/ug/epel.html) in the *Amazon Linux 2023 User Guide*.
+ 32-bit applications are not supported in Amazon Linux 2023. For more information, see [Deprecated features from Amazon Linux 2](https://docs.aws.amazon.com/linux/al2023/ug/deprecated-al2.html#deprecated-32bit-rpms) in the *Amazon Linux 2023 User Guide*.

### Control Groups (cgroups) changes
<a name="al2-to-al2023-ami-transition-compatibility-cgroups"></a>

A Control Group (cgroup) is a Linux kernel feature to hierarchically organize processes and distribute system resources between them. Control Groups are used extensively to implement a container runtime, and by `systemd`.

Amazon Linux 2023 uses cgroupv2 by default, while Amazon Linux 2 used cgroupv1. The Amazon ECS agent, Docker, and containerd all support both cgroupv1 and cgroupv2. For further details on cgroupv2, see [Control groups v2 in Amazon Linux 2023](https://docs.aws.amazon.com/linux/al2023/ug/cgroupv2.html) in the *Amazon Linux 2023 User Guide*.

#### Memory usage reporting
<a name="al2-to-al2023-ami-transition-cgroups-reporting"></a>

cgroupv2 changes how container memory usage is calculated. In cgroupv1 (Amazon Linux 2), container memory utilization as reported by the container runtime typically excludes page cache. In cgroupv2 (Amazon Linux 2023), page cache is included in the reported memory usage. The same workload may report higher memory utilization on Amazon Linux 2023 compared to Amazon Linux 2, even when actual application memory consumption has not changed.

We recommend benchmarking memory usage on Amazon Linux 2023 instances before migrating production workloads, and adjusting task and container memory limits if needed. You can use [Container Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-metrics-ECS.html) to compare memory utilization between Amazon Linux 2 and Amazon Linux 2023.

#### Task memory limit visibility
<a name="al2-to-al2023-ami-transition-cgroups-memory-visibility"></a>

When you set memory at the task level without setting a container-level memory limit, Amazon ECS applies the limit to the task's cgroup. This acts as the effective memory limit for all the containers belonging to the task. On cgroupv1 (Amazon Linux 2), child cgroups could read the effective memory limit at their own level. They did not need to traverse the cgroup hierarchy. On cgroupv2 (Amazon Linux 2023), the effective limit is not visible to the container. Additionally, Docker runs containers in a private cgroup namespace by default, which prevents them from traversing up the cgroup hierarchy to discover the parent's limit.

Any process inside the container that reads cgroup memory limits to determine available memory will see the full host memory rather than the task-level limit. For example, the Java Virtual Machine (JVM) is known to be affected by this issue. It uses cgroup limits to automatically size the heap. When it cannot detect the true limit, it over-allocates memory, which increases the risk of out-of-memory (OOM) kills. Other runtimes or frameworks that read cgroup limits for resource decisions may be similarly affected.

This occurs when task-level memory is set but container-level `memory` is not set in the task definition.

To resolve this issue, choose one of the following workarounds:

**Set container-level memory limits (recommended)**

Explicitly set the `memory` parameter at the container level in your task definition, equal to the task-level memory value. This approach is safe, reliable, and requires no infrastructure changes.

**Enable agent-level task memory limit propagation**

Set the `ECS_PROPAGATE_TASK_MEMORY_LIMIT_CGROUPV2` environment variable to `true` on the Amazon ECS agent. When enabled and on cgroupv2, the agent automatically sets each container's memory limit to the task-level value if the container does not already have an explicit container-level memory limit. This makes the task memory limit visible inside the container without requiring task definition changes.

You can set this in the Amazon ECS agent configuration file (`/etc/ecs/ecs.config`) on your Amazon EC2 instances:

```
ECS_PROPAGATE_TASK_MEMORY_LIMIT_CGROUPV2=true
```

This option requires Amazon ECS agent version 1.104.0 or later. It only applies on Linux instances using cgroupv2. It is not supported on Windows.

### Instance Metadata Service (IMDS) changes
<a name="al2-to-al2023-ami-transition-compatibility-imds"></a>

Amazon Linux 2023 requires Instance Metadata Service version 2 (IMDSv2) by default. IMDSv2 has several benefits that help improve security posture. It uses a session-oriented authentication method that requires the creation of a secret token in a simple HTTP PUT request to start the session. A session's token can be valid for anywhere between 1 second and 6 hours.

For more information on how to transition from IMDSv1 to IMDSv2, see [Transition to using Instance Metadata Service Version 2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-metadata-transition-to-version-2.html) in the *Amazon EC2 User Guide*.

If you would like to use IMDSv1, you can still do so by manually overriding the settings using instance metadata option launch properties.

### Memory swappiness changes
<a name="al2-to-al2023-ami-transition-compatibility-memory-swappiness"></a>

Per-container memory swappiness is not supported on Amazon Linux 2023 and cgroups v2. For more information, see [Managing container swap memory space on Amazon ECS](container-swap.md).

### FIPS validation changes
<a name="al2-to-al2023-ami-transition-compatibility-fips"></a>

Amazon Linux 2 is certified under FIPS 140-2 and Amazon Linux 2023 is certified under FIPS 140-3.

To enable FIPS mode on Amazon Linux 2023, install the necessary packages on your Amazon EC2 instance and follow the configuration steps using the instructions in [Enable FIPS Mode on Amazon Linux 2023](https://docs.aws.amazon.com/linux/al2023/ug/fips-mode.html) in the *Amazon Linux 2023 User Guide*.

### Accelerated instance support
<a name="al2-to-al2023-ami-transition-compatibility-accelerated"></a>

The Amazon ECS-optimized Amazon Linux 2023 AMIs support both Neuron and GPU accelerated instance types. For more information, see [Amazon ECS-optimized Linux AMIs](ecs-optimized_AMI.md).

## Building custom AMIs
<a name="al2-to-al2023-ami-transition-custom-ami"></a>

While we recommend moving to officially supported and published Amazon ECS-optimized AMIs for Amazon Linux 2023, you can continue to build custom Amazon Linux 2 Amazon ECS-optimized AMIs using the open-source build scripts that are used to build the Linux variants of the Amazon ECS-optimized AMI. For more information, see [Amazon ECS-optimized Linux AMI build script](ecs-ami-build-scripts.md).

## Migration strategies
<a name="al2-to-al2023-ami-transition-migration"></a>

We recommend creating and implementing a migration plan that includes thorough application testing. The following sections outline different migration strategies based on how you manage your Amazon ECS infrastructure.

### Migrating with Amazon ECS capacity providers
<a name="al2-to-al2023-ami-transition-migration-capacity-providers"></a>

1. Create a new capacity provider with a new launch template. This should reference an Auto Scaling group with a launch template similar to your existing one, but instead of the Amazon Linux 2 Amazon ECS-optimized AMI, it should specify one of the Amazon Linux 2023 variants. Add this new capacity provider to your existing Amazon ECS cluster.

1. Update your cluster's default capacity provider strategy to include both the existing Amazon Linux 2 capacity provider and the new Amazon Linux 2023 capacity provider. Start with a higher weight on the Amazon Linux 2 provider and a lower weight on the Amazon Linux 2023 provider (for example, Amazon Linux 2: weight 80, Amazon Linux 2023: weight 20). This causes Amazon ECS to begin provisioning Amazon Linux 2023 instances as new tasks are scheduled. Verify that the instances register correctly and that tasks are able to run successfully on the new instances.

1. Gradually adjust the capacity provider weights in your cluster's default strategy, increasing the weight for the Amazon Linux 2023 provider while decreasing the Amazon Linux 2 provider weight over time (for example, 60/40, then 40/60, then 20/80). You can also update individual service capacity provider strategies to prioritize Amazon Linux 2023 instances. Monitor task placement to ensure they're successfully running on Amazon Linux 2023 instances.

1. Optionally drain Amazon Linux 2 container instances to accelerate task migration. If you have sufficient Amazon Linux 2023 replacement capacity, you can manually drain your Amazon Linux 2 container instances through the Amazon ECS console or AWS CLI to speed up the transition of your tasks from Amazon Linux 2 to Amazon Linux 2023. After the migration is complete, remove the Amazon Linux 2 capacity provider from your cluster and delete the associated Auto Scaling group.

### Migrating with an Amazon EC2 Auto Scaling group
<a name="al2-to-al2023-ami-transition-migration-asg"></a>

1. Create a new Amazon EC2 Auto Scaling group with a new launch template. This should be similar to your existing launch template, but instead of the Amazon Linux 2 Amazon ECS-optimized AMI, it should specify one of the Amazon Linux 2023 variants. This new Auto Scaling group can launch instances to your existing cluster.

1. Scale up the Auto Scaling group so that you begin to have Amazon Linux 2023 instances registering to your cluster. Verify that the instances register correctly and that tasks are able to run successfully on the new instances.

1. After your tasks have been verified to work on Amazon Linux 2023, scale up the Amazon Linux 2023 Auto Scaling group while gradually scaling down the Amazon Linux 2 Auto Scaling group, until you have completely replaced all Amazon Linux 2 instances.

1. If you have sufficient Amazon Linux 2023 replacement capacity, you might want to explicitly drain the container instances to speed up the transition of your tasks from Amazon Linux 2 to Amazon Linux 2023. For more information, see [Draining Amazon ECS container instances](container-instance-draining.md).

### Migrating with manually managed instances
<a name="al2-to-al2023-ami-transition-migration-manual"></a>

1. Manually launch (or adjust scripts that launch) new Amazon EC2 instances using the Amazon ECS-optimized Amazon Linux 2023 AMI instead of Amazon Linux 2. Ensure these instances use the same security groups, subnets, IAM roles, and cluster configuration as your existing Amazon Linux 2 instances. The instances should automatically register to your existing Amazon ECS cluster upon launch.

1. Verify the new Amazon Linux 2023 instances are successfully registering to your Amazon ECS cluster and are in an `ACTIVE` state. Test that tasks can be scheduled and run properly on these new instances by either waiting for natural task placement or manually stopping/starting some tasks to trigger rescheduling.

1. Gradually replace your Amazon Linux 2 instances by launching additional Amazon Linux 2023 instances as needed, then manually draining and terminating the Amazon Linux 2 instances one by one. You can drain instances through the Amazon ECS console by setting the instance to `DRAINING` status, which will stop placing new tasks on it and allow existing tasks to finish or be rescheduled elsewhere.