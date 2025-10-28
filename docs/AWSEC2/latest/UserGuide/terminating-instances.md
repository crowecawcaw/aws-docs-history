# Terminate Amazon EC2 instances

###### Warning

**Terminating an instance is permanent and irreversible.**

After you terminate an instance, you can no longer connect to it, and it can't be recovered.
All attached Amazon EBS volumes that are configured to be deleted on termination are also permanently
deleted and can't be recovered. All data stored on instance store volumes is permanently lost.
For more information, see [How instance termination
works](how-ec2-instance-termination-works.md "how-ec2-instance-termination-works.md").

Before you terminate an instance, ensure that you have backed up all data that you need to
retain after the termination to persistent storage.

You can delete your instance when you no longer need it. This is referred to as
_terminating_ your instance. As soon as the state of an instance
changes to `shutting-down` or `terminated`, you stop incurring charges
for that instance.

You can't connect to or start an instance after you've terminated it. However, you can
launch new instances using the same AMI.

If you'd rather stop or hibernate your instance, see [Stop and start Amazon EC2 instances](Stop_Start.md "Stop_Start.md") or [Hibernate your Amazon EC2 instance](Hibernate.md "Hibernate.md").
For more information, see [Differences between instance states](ec2-instance-lifecycle.md#lifecycle-differences "ec2-instance-lifecycle.md#lifecycle-differences").

###### Contents

- [How instance termination
  works](how-ec2-instance-termination-works.md "how-ec2-instance-termination-works.md")
- [Methods for terminating an instance](instance-terminate-methods.md "instance-terminate-methods.md")
- [Terminate an instance with a graceful OS
  shutdown](#terminating-instances-console "#terminating-instances-console")
- [Terminate an instance and
  bypass the graceful OS shutdown](#terminating-instances-bypass-graceful-os-shutdown "#terminating-instances-bypass-graceful-os-shutdown")
- [Troubleshoot instance
  termination](#troubleshoot-instance-terminate "#troubleshoot-instance-terminate")
- [Change instance termination
  protection](Using_ChangingDisableAPITermination.md "Using_ChangingDisableAPITermination.md")
- [Change instance
  initiated shutdown behavior](Using_ChangingInstanceInitiatedShutdownBehavior.md "Using_ChangingInstanceInitiatedShutdownBehavior.md")
- [Preserve data when an instance is
  terminated](preserving-volumes-on-termination.md "preserving-volumes-on-termination.md")

## Terminate an instance with a graceful OS

shutdown

You can terminate an instance using the default terminate method, which includes an attempt
at a graceful OS shutdown. For more information, see [Methods for terminating an instance](instance-terminate-methods.md "instance-terminate-methods.md").

Console

###### To terminate an instance using the default terminate method

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose
   **Instances**.
3. Select the instance, and choose **Instance
   state**, **Terminate (delete)
   instance**.
4. Choose **Terminate (delete)** when prompted for
   confirmation.
5. After you terminate an instance, it remains visible for a short
   while, with a state of `terminated`.

If termination fails or if a terminated instance is visible for
more than a few hours, see [Terminated instance still displayed](TroubleshootingInstancesShuttingDown.md#terminated-instance-still-displaying "TroubleshootingInstancesShuttingDown.md#terminated-instance-still-displaying").

AWS CLI

###### To terminate an instance using the default terminate method

Use the [terminate-instances](../../../cli/latest/reference/ec2/terminate-instances.md "../../../cli/latest/reference/ec2/terminate-instances.md") command.

```
aws ec2 terminate-instances --instance-ids `i-1234567890abcdef0`
```

PowerShell

###### To terminate an instance using the default terminate method

Use the [Remove-EC2Instance](../../../powershell/latest/reference/items/Remove-EC2Instance.md "../../../powershell/latest/reference/items/Remove-EC2Instance.md") cmdlet.

```
Remove-EC2Instance -InstanceId `i-1234567890abcdef0`
```

## Terminate an instance and

bypass the graceful OS shutdown

You can bypass the graceful OS shutdown when terminating an instance. For more information,
see [Methods for terminating an instance](instance-terminate-methods.md "instance-terminate-methods.md").

Console

###### To terminate an instance and bypass the graceful OS shutdown

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose
   **Instances**.
3. Select the instance, and choose **Instance
   state**, **Terminate (delete)
   instance**.
4. Under **Skip OS shutdown**, select the **Skip OS
   shutdown** checkbox. If you don't see this option in
   the console, it's not yet available in the console in the current
   Region. You can, however, access this feature using the AWS CLI or
   SDK, or try another Region in the console.
5. Choose **Terminate (delete)**.
6. After you terminate an instance, it remains visible for a short
   while, with a state of `terminated`.

If termination fails or if a terminated instance is visible for
more than a few hours, see [Terminated instance still displayed](TroubleshootingInstancesShuttingDown.md#terminated-instance-still-displaying "TroubleshootingInstancesShuttingDown.md#terminated-instance-still-displaying").

AWS CLI

###### To terminate an instance and bypass the graceful OS shutdown

Use the [terminate-instances](../../../cli/latest/reference/ec2/terminate-instances.md "../../../cli/latest/reference/ec2/terminate-instances.md") command with
`--skip-os-shutdown`..

```
aws ec2 terminate-instances \
    --instance-ids `i-1234567890abcdef0` \
    --skip-os-shutdown
```

PowerShell

###### To terminate an instance and bypass the graceful OS shutdown

Use the [Remove-EC2Instance](../../../powershell/latest/reference/items/Remove-EC2Instance.md "../../../powershell/latest/reference/items/Remove-EC2Instance.md") cmdlet with `-SkipOsShutdown
 $true`..

```
Remove-EC2Instance `
    -InstanceId `i-1234567890abcdef0` `
    -SkipOsShutdown $true
```

## Troubleshoot instance

termination

The requester must have permission to call `ec2:TerminateInstances`. For
more information, see [Example policies to work
with instances](ExamplePolicies_EC2.md#iam-example-instances "ExamplePolicies_EC2.md#iam-example-instances").

If you terminate your instance and another instance starts, most likely you have
configured automatic scaling through a feature like EC2 Fleet or Amazon EC2 Auto Scaling. For more
information, see [Instances automatically launched or terminated](TroubleshootingInstancesShuttingDown.md#automatic-instance-create-or-delete "TroubleshootingInstancesShuttingDown.md#automatic-instance-create-or-delete").

###### Note

You can't terminate an instance if termination protection is turned
on. For more information, see [Change instance termination protection](Using_ChangingDisableAPITermination.md "Using_ChangingDisableAPITermination.md").

If your instance is in the `shutting-down` state for longer than usual, you can
attempt to force terminate it. If it remains in the `shutting-down` state, it
should be cleaned up (terminated) by automated processes within the Amazon EC2 service. For
more information, see [Delayed instance termination](TroubleshootingInstancesShuttingDown.md#instance-stuck-terminating "TroubleshootingInstancesShuttingDown.md#instance-stuck-terminating").
