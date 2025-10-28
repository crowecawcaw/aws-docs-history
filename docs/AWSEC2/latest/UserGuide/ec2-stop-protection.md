# Enable stop protection for your EC2

instances

To prevent an instance from being accidentally stopped, you can enable stop protection
for the instance. Stop protection also protects your instance from accidental
termination.

The `DisableApiStop` attribute of the Amazon EC2 [`ModifyInstanceAttribute`](../APIReference/API_ModifyInstanceAttribute.md "../APIReference/API_ModifyInstanceAttribute.md") API controls whether the instance
can be stopped by using the Amazon EC2 console, the AWS CLI, or the Amazon EC2 API. You can set the
value of this attribute when you launch the instance, while the instance is running, or
while the instance is stopped.

###### Considerations

- Enabling stop protection does not prevent you from accidentally stopping an
  instance by initiating a shutdown from the instance using an operating system
  command such as **shutdown** or
  **poweroff**.
- Enabling stop protection does not prevent AWS from stopping the instance
  when there is a [scheduled event](monitoring-instances-status-check_sched.md "monitoring-instances-status-check_sched.md") to stop the instance.
- Enabling stop protection does not prevent Amazon EC2 Auto Scaling from terminating an
  instance when the instance is unhealthy or during scale-in events. You can
  control whether an Auto Scaling group can terminate a particular instance when
  scaling in by using [instance scale-in protection](../../../autoscaling/ec2/userguide/ec2-auto-scaling-instance-protection.md "../../../autoscaling/ec2/userguide/ec2-auto-scaling-instance-protection.md").
- Stop protection not only prevents your instance from being accidentally
  stopped, but also from accidental termination when using the console, AWS CLI, or
  API. However, it does not automatically set the
  `DisableApiTermination` attribute. Note that when the
  `DisableApiStop` attribute is set to `false`, the
  `DisableApiTermination` attribute setting determines whether the
  instance can be terminated using the console, AWS CLI, or API. For more
  information see [Terminate Amazon EC2 instances](terminating-instances.md "terminating-instances.md").
- You can't enable stop protection for an instance with an instance store root
  volume.
- You can't enable stop protection for Spot Instances.
- The Amazon EC2 API follows an eventual consistency model when you enable or disable
  stop protection. This means that the result of running commands to set the stop
  protection attribute might not be immediately visible to all subsequent commands
  you run. For more information, see [Eventual
  consistency](../../../ec2/latest/devguide/eventual-consistency.md "../../../ec2/latest/devguide/eventual-consistency.md") in the _Amazon EC2 Developer
  Guide_.

###### Stop protection tasks

- [Enable stop protection for an
  instance at launch](#enable-stop-protection-at-launch "#enable-stop-protection-at-launch")
- [Enable stop
  protection for a running or stopped instance](#enable-stop-protection-on-running-or-stopped-instance "#enable-stop-protection-on-running-or-stopped-instance")
- [Disable
  stop protection for a running or stopped instance](#disable-stop-protection-on-running-or-stopped-instance "#disable-stop-protection-on-running-or-stopped-instance")

## Enable stop protection for an

instance at launch

You can enable stop protection for an instance when launching the instance.

Console

###### To enable stop protection for an instance at launch

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the dashboard, choose **Launch
   instance**.
3. Configure your instance in the [new launch instance
   wizard](ec2-launch-instance-wizard.md "ec2-launch-instance-wizard.md").
4. In the wizard, enable stop protection by choosing
   **Enable** for **Stop
   protection** under **Advanced
   details**.

AWS CLI

###### To enable stop protection for an instance at launch

Use the [run-instances](../../../cli/latest/reference/ec2/run-instances.md "../../../cli/latest/reference/ec2/run-instances.md") command to launch the instance. Add the
following parameter.

```
--disable-api-stop
```

PowerShell

###### To enable stop protection for an instance at launch

Use the [New-EC2Instance](../../../powershell/latest/reference/items/New-EC2Instance.md "../../../powershell/latest/reference/items/New-EC2Instance.md") cmdlet to launch the instance. Add the
following parameter.

```
-DisableApiStop $true
```

## Enable stop

protection for a running or stopped instance

You can enable stop protection for an instance while the instance is running or
stopped.

Console

###### To enable stop protection for an instance

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the left navigation pane, choose
   **Instances**.
3. Select the instance, and then choose
   **Actions**>**Instance
   settings**>**Change stop
   protection**.
4. Select the **Enable** checkbox, and then
   choose **Save**.

AWS CLI

###### To enable stop protection for an instance

Use the [modify-instance-attribute](../../../cli/latest/reference/ec2/modify-instance-attribute.md "../../../cli/latest/reference/ec2/modify-instance-attribute.md") command.

```
aws ec2 modify-instance-attribute \
    --instance-id `i-1234567890abcdef0` \
    --disable-api-stop
```

PowerShell

###### To enable stop protection for an instance

Use the [Edit-EC2InstanceAttribute](../../../powershell/latest/reference/items/Edit-EC2InstanceAttribute.md "../../../powershell/latest/reference/items/Edit-EC2InstanceAttribute.md") cmdlet.

```
Edit-EC2InstanceAttribute `
    -InstanceId `i-1234567890abcdef0` `
    -DisableApiStop $true
```

## Disable

stop protection for a running or stopped instance

You can disable stop protection for a running or stopped instance using one of the
following methods.

Console

###### To disable stop protection for a running or stopped

instance

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the left navigation pane, choose
   **Instances**.
3. Select the instance, and then choose
   **Actions**, **Instance
   settings**, **Change stop
   protection**.
4. Clear the **Enable** checkbox, and then
   choose **Save**.

AWS CLI

###### To disable stop protection for a running or stopped

instance

Use the [modify-instance-attribute](../../../cli/latest/reference/ec2/modify-instance-attribute.md "../../../cli/latest/reference/ec2/modify-instance-attribute.md") command.

```
aws ec2 modify-instance-attribute \
    --instance-id `i-1234567890abcdef0` \
    --no-disable-api-stop
```

PowerShell

###### To disable stop protection for an instance

Use the [Edit-EC2InstanceAttribute](../../../powershell/latest/reference/items/Edit-EC2InstanceAttribute.md "../../../powershell/latest/reference/items/Edit-EC2InstanceAttribute.md") cmdlet.

```
Edit-EC2InstanceAttribute `
    -InstanceId `i-1234567890abcdef0` `
    -DisableApiStop $false
```
