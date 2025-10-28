# Using Kernel Live Patching on Amazon Linux 2 managed

nodes

Kernel Live Patching for Amazon Linux 2 allows you to apply security vulnerability and critical bug
patches to a running Linux kernel without reboots or disruptions to running
applications. This allows you to benefit from improved service and application
availability, while keeping your infrastructure secure and up to date. Kernel Live Patching is
supported on Amazon EC2 instances, AWS IoT Greengrass core devices, and [on-premises
virtual machines](../../../AWSEC2/latest/UserGuide/amazon-linux-2-virtual-machine.md "../../../AWSEC2/latest/UserGuide/amazon-linux-2-virtual-machine.md") running Amazon Linux 2.

For general information about Kernel Live Patching, see [Kernel Live Patching on AL2](../../../linux/al2/ug/al2-live-patching.md "../../../linux/al2/ug/al2-live-patching.md") in the
_Amazon Linux 2 User Guide_.

After you turn on Kernel Live Patching on an Amazon Linux 2 managed node, you can use Patch Manager, a tool in
AWS Systems Manager, to apply kernel live patches to the managed node. Using Patch Manager is an
alternative to using existing yum workflows on the node to apply the updates.

###### Before you begin

To use Patch Manager to apply kernel live patches to your Amazon Linux 2 managed nodes, ensure
your nodes are based on the correct architecture and kernel version. For
information, see [Supported configurations and prerequisites](../../../AWSEC2/latest/UserGuide/al2-live-patching.md#al2-live-patching-prereq "../../../AWSEC2/latest/UserGuide/al2-live-patching.md#al2-live-patching-prereq") in the
_Amazon EC2 User Guide_.

###### Topics

- [Kernel Live Patching  using  Patch Manager](#about-klp "#about-klp")
- [How Kernel Live Patching using Patch Manager works](#how-klp-works "#how-klp-works")
- [Turning on Kernel Live Patching using Run Command](enable-klp.md "enable-klp.md")
- [Applying kernel live patches using Run Command](install-klp.md "install-klp.md")
- [Turning off Kernel Live Patching using Run Command](disable-klp.md "disable-klp.md")

## Kernel Live Patching  using  Patch Manager

Updating the kernel version

You don't need to reboot a managed node after applying a kernel live
patch update. However, AWS provides kernel live patches for an Amazon Linux 2
kernel version for up to three months after its release. After the
three-month period, you must update to a later kernel version to
continue to receive kernel live patches. We recommend using a
maintenance window to schedule a reboot of your node at least once every
three months to prompt the kernel version update.

Uninstalling kernel live patches

Kernel live patches can't be uninstalled using Patch Manager. Instead, you
can turn off Kernel Live Patching, which removes the RPM packages for the applied
kernel live patches. For more information, see [Turning off Kernel Live Patching using Run Command](disable-klp.md "disable-klp.md").

Kernel compliance

In some cases, installing all CVE fixes from live patches for the
current kernel version can bring that kernel into the same compliance
state that a newer kernel version would have. When that happens, the
newer version is reported as `Installed`, and the managed
node reported as `Compliant`. No installation time is
reported for newer kernel version, however.

One kernel live patch, multiple CVEs

If a kernel live patch addresses multiple CVEs, and those CVEs have
various classification and severity values, only the highest
classification and severity from among the CVEs is reported for the
patch.

The remainder of this section describes how to use Patch Manager to apply kernel live
patches to managed nodes that meet these requirements.

## How Kernel Live Patching using Patch Manager works

AWS releases two types of kernel live patches for Amazon Linux 2: security updates and
bug fixes. To apply those types of patches, you use a patch baseline document that
targets only the classifications and severities listed in the following
table.

| Classification | Severity                |
| -------------- | ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Security`     | `Critical`, `Important` |
| `Bugfix`       | `All`                   | You can create a custom patch baseline that targets only these patches, or use the predefined `AWS-AmazonLinux2DefaultPatchBaseline` patch baseline. In other words, you can use `AWS-AmazonLinux2DefaultPatchBaseline` with Amazon Linux 2 managed nodes on which Kernel Live Patching is turned on, and kernel live updates will be applied. ###### Note The `AWS-AmazonLinux2DefaultPatchBaseline` configuration specifies a 7-day waiting period after a patch is released or last updated before it's installed automatically. If you don't want to wait 7 days for kernel live patches to be auto-approved, you can create and use a custom patch baseline. In your patch baseline, you can specify no auto-approval waiting period, or specify a shorter or longer one. For more information, see [Working with custom patch baselines](patch-manager-manage-patch-baselines.md "patch-manager-manage-patch-baselines.md"). We recommend the following strategy to patch your managed nodes with kernel live updates: 1. Turn on Kernel Live Patching on your Amazon Linux 2 managed nodes. 2. Use Run Command, a tool in AWS Systems Manager, to run a `Scan` operation on your managed nodes using the predefined `AWS-AmazonLinux2DefaultPatchBaseline` or a custom patch baseline that also targets only `Security` updates with severity classified as `Critical` and `Important`, and the `Bugfix` severity of `All`. 3. Use Compliance, a tool in AWS Systems Manager, to review whether non-compliance for patching is reported for any of the managed nodes that were scanned. If so, view the node compliance details to determine whether any kernel live patches are missing from the managed node. 4. To install missing kernel live patches, use Run Command with the same patch baseline you specified before, but this time run an `Install` operation instead of a `Scan` operation. Because kernel live patches are installed without the need to reboot, you can choose the `NoReboot` reboot option for this operation. ###### Note You can still reboot the managed node if required for other types of patches installed on it, or if you want to update to a newer kernel. In these cases, choose the `RebootIfNeeded` reboot option instead. 5. Return to Compliance to verify that the kernel live patches were installed. |
