# Change instance termination

protection

To prevent your instance from being accidentally terminated using the Amazon EC2 API,
whether you call `TerminateInstances` directly or using another interface
such as the Amazon EC2 console, enable _termination protection_ for the
instance. The `DisableApiTermination` attribute controls whether the instance
can be terminated. By default, termination protection is disabled for your instance. You
can set the value of this attribute when you launch an instance, or while the instance
is running or stopped.

The `DisableApiTermination` attribute doesn't prevent you from terminating
an instance by initiating shutdown from the instance (for example, by using an operating
system command for system shutdown) when the
`InstanceInitiatedShutdownBehavior` attribute is set to
`terminate`. For more information, see [Change instance
initiated shutdown behavior](Using_ChangingInstanceInitiatedShutdownBehavior.md "Using_ChangingInstanceInitiatedShutdownBehavior.md").

###### Considerations

- Enabling termination protection does not prevent AWS from terminating the
  instance when there is a [scheduled event](monitoring-instances-status-check_sched.md "monitoring-instances-status-check_sched.md") to terminate the instance.
- Enabling termination protection does not prevent Amazon EC2 Auto Scaling from terminating an
  instance when the instance is unhealthy or during scale-in events. You can
  control whether an Auto Scaling group can terminate a particular instance when scaling
  using [instance
  scale-in protection](../../../autoscaling/ec2/userguide/ec2-auto-scaling-instance-protection.md "../../../autoscaling/ec2/userguide/ec2-auto-scaling-instance-protection.md"). You can control whether an Auto Scaling group can
  terminate unhealthy instances by [suspending the
  ReplaceUnhealthy scaling process](../../../autoscaling/ec2/userguide/as-suspend-resume-processes.md "../../../autoscaling/ec2/userguide/as-suspend-resume-processes.md").
- You can't enable termination protection for Spot Instances.

Console

###### To enable termination protection for an instance at launch

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the dashboard, choose **Launch
   instance**.
3. Expand **Advanced details**. For
   **Termination protection**, select
   **Enable**.
4. When you are finishing specifying the details for your instance,
   choose **Launch instance**.

###### To change termination protection for an instance

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, select
   **Instances**.
3. Select the instance.
4. Choose **Actions**, **Instance
   settings**, **Change termination
   protection**.
5. For **Termination protection** select or clear
   **Enable**.
6. Choose **Save**.

AWS CLI

###### To enable termination protection for an instance

Use the [modify-instance-attribute](../../../cli/latest/reference/ec2/modify-instance-attribute.md "../../../cli/latest/reference/ec2/modify-instance-attribute.md") command.

```
aws ec2 modify-instance-attribute \
    --instance-id `i-1234567890abcdef0` \
    --disable-api-termination
```

###### To disable termination protection for an instance

Use the [modify-instance-attribute](../../../cli/latest/reference/ec2/modify-instance-attribute.md "../../../cli/latest/reference/ec2/modify-instance-attribute.md") command.

```
aws ec2 modify-instance-attribute \
    --instance-id `i-1234567890abcdef0` \
    --no-disable-api-termination
```

PowerShell

###### To enable termination protection for an instance

Use the [Edit-EC2InstanceAttribute](../../../powershell/latest/reference/items/Edit-EC2InstanceAttribute.md "../../../powershell/latest/reference/items/Edit-EC2InstanceAttribute.md") cmdlet.

```
Edit-EC2InstanceAttribute `
    -InstanceId `i-1234567890abcdef0` `
    -DisableApiTermination $true
```

###### To disable termination protection for an instance

Use the [Edit-EC2InstanceAttribute](../../../powershell/latest/reference/items/Edit-EC2InstanceAttribute.md "../../../powershell/latest/reference/items/Edit-EC2InstanceAttribute.md") cmdlet.

```
Edit-EC2InstanceAttribute `
    -InstanceId `i-1234567890abcdef0` `
    -DisableApiTermination $false
```

## Terminate multiple instances with termination

protection

If you terminate multiple instances across multiple Availability Zones in the same
request, and one or more of the specified instances are enabled for termination
protection, the request fails with the following results:

- The specified instances that are in the same Availability Zone as the
  protected instance are not terminated.
- The specified instances that are in different Availability Zones, where no
  other specified instances are protected, are successfully terminated.

###### Example

Suppose that you have the following four instances across two Availability
Zones.

| Instance       | Availability Zone | Terminate protection                                                                                                                                                                                                                                                                                                                                                                        |
| -------------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Instance 1** | AZ A              | `Disabled`                                                                                                                                                                                                                                                                                                                                                                                  |
| **Instance 2** | `Disabled`        |
| **Instance 3** | AZ B              | `Enabled`                                                                                                                                                                                                                                                                                                                                                                                   |
| **Instance 4** | `Disabled`        | If you attempt to terminate all of these instances in the same request, the request reports failure with the following results: <br>• **Instance 1** and **Instance 2** are successfully terminated because neither instance is enabled for termination protection. <br>• **Instance 3** and **Instance 4** fail to terminate because **Instance 3** is enabled for termination protection. |
