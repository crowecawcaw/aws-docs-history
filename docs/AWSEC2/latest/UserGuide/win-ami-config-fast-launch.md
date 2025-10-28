# Use EC2 Fast Launch for your

Windows instances

When you configure a Windows Server AMI for EC2 Fast Launch, Amazon EC2 creates
a set of pre-provisioned snapshots to use for faster launching, as follows.

1. Amazon EC2 launches a set of temporary t3 instances, based on your settings.
2. As each temporary instance completes the standard launch steps, Amazon EC2 creates a
   pre-provisioned snapshot of the instance. It stores the snapshot in your Amazon S3 bucket.
3. When the snapshot is ready, Amazon EC2 terminates the associated t3 instance to
   keep resource costs as low as possible.
4. The next time Amazon EC2 launches an instance from the EC2 Fast Launch enabled AMI,
   it uses one of the snapshots to significantly reduce the time it takes to launch.
   Amazon EC2 automatically replenishes the snapshots you have on hand as it uses them to
   launch instances from the EC2 Fast Launch enabled AMI.

Any account that has access to an AMI with EC2 Fast Launch enabled can benefit from
reduced launch times. When the AMI owner grants access for you to launch instances,
the pre-provisioned snapshots come from the AMI owner’s account.

If an AMI that supports EC2 Fast Launch is shared with you, you can enable or disable
faster launching on the shared AMI yourself. If you enable a shared AMI for EC2 Fast Launch,
Amazon EC2 creates the pre-provisioned snapshots directly in your account. If you deplete the snapshots
in your account, you can still use snapshots from the AMI owner's account.

###### Note

EC2 Fast Launch deletes pre-provisioned snapshots as soon as they're consumed by
a launch to minimize storage costs and prevent reuse. However, if the deleted snapshots
match a retention rule, Recycle Bin automatically retains them. We recommend that you
review the scope of your Recycle Bin retention rules so that this doesn't happen. For
more information, see [Recycle Bin](../../../ebs/latest/userguide/recycle-bin.md "../../../ebs/latest/userguide/recycle-bin.md")
in the _Amazon EBS User Guide_.

This feature is not the same as [EBS fast snapshot restore](../../../ebs/latest/userguide/ebs-fast-snapshot-restore.md "../../../ebs/latest/userguide/ebs-fast-snapshot-restore.md").
You must explicitly enable EBS fast snapshot restore on a per-snapshot basis, and it has its
own associated costs.

The following video demonstrates how to configure your Windows AMI for faster launching with a
quick overview of the related key terms and their definitions: [Launching EC2 Windows instances up to 65% faster on AWS](https://www.youtube.com/watch?v=qTWlmhf9I9I "https://www.youtube.com/watch?v=qTWlmhf9I9I").

###### Resource costs

There is no service charge to configure Windows AMIs for EC2 Fast Launch. However,
standard pricing applies for any underlying AWS resources that Amazon EC2 uses. To learn
more about associated resource costs and how to manage them, see
[Manage costs for EC2 Fast Launch underlying resources](win-fast-launch-manage-costs.md "win-fast-launch-manage-costs.md").

###### Contents

- [Key terms](#win-fast-launch-key-terms "#win-fast-launch-key-terms")
- [EC2 Fast Launch prerequisites for Windows](win-start-fast-launch-prereqs.md "win-start-fast-launch-prereqs.md")
- [Configure EC2 Fast Launch settings for your
  Amazon EC2 Windows Server AMI](win-fast-launch-configure.md "win-fast-launch-configure.md")
- [View AMIs with EC2 Fast Launch enabled](win-view-fast-launch.md "win-view-fast-launch.md")
- [Manage costs for EC2 Fast Launch underlying resources](win-fast-launch-manage-costs.md "win-fast-launch-manage-costs.md")
- [Monitor EC2 Fast Launch](win-fast-launch-monitor.md "win-fast-launch-monitor.md")
- [Service-linked role for
  EC2 Fast Launch](slr-windows-fast-launch.md "slr-windows-fast-launch.md")
- [Troubleshoot Windows EC2 Fast Launch](win-fast-launch-troubleshoot.md "win-fast-launch-troubleshoot.md")

## Key terms

The EC2 Fast Launch feature uses the following key terms:

**Pre-provisioned snapshot**

A snapshot of an instance that was launched from a Windows AMI
with EC2 Fast Launch enabled, and that has completed the following
Windows launch steps, rebooting as required.

- Sysprep specialize
- Windows Out of Box Experience (OOBE)

When these steps are complete, EC2 Fast Launch stops the instance, and
creates a snapshot that is later used for faster launching from the AMI,
based on your configuration.

**Launch frequency**

Controls the number of pre-provisioned snapshots that Amazon EC2 can launch
within the specified timeframe. When you enable EC2 Fast Launch for your
AMI, Amazon EC2 creates the initial set of pre-provisioned snapshots in the
background. For example, if the launch frequency is set to five launches
per hour, which is the default, then EC2 Fast Launch creates an initial
set of five pre-provisioned snapshots.

When Amazon EC2 launches an instance from an AMI with EC2 Fast Launch enabled,
it uses one of the pre-provisioned snapshots to reduce the launch time. As
snapshots are used, they are automatically replenished, up to the number
specified by the launch frequency.

If you expect a spike in the number of instances that are launched from your
AMI – during a special event, for example – you can increase the
launch frequency in advance to cover the additional instances that you'll need.
When your launch rate returns to normal, you can adjust the frequency back down.

When you experience a higher number of launches than anticipated, you might use
up all the pre-provisioned snapshots that you have available. This doesn't cause
any launches to fail. However, it can result in some instances going through the
standard launch process, until snapshots can be replenished.

**Target resource count**

The number of pre-provisioned snapshots to keep on hand for an
Amazon EC2 Windows Server AMI with EC2 Fast Launch enabled.

**Max parallel launches**

Controls how many instances Amazon EC2 can launch at the same time to create the
pre-provisioned snapshots for EC2 Fast Launch. If your target resource count
is higher than the maximum parallel launches that you've configured, then Amazon EC2
launches the number of instances specified by **Max parallel
launches** to start creating the snapshots. As those instances
complete the process, Amazon EC2 takes the snapshot and stops the instance. Then it
continues to launch more instances until the total number of snapshots
available has reached the target resource count. The value for
**Max parallel launches** must be 6 or greater.
