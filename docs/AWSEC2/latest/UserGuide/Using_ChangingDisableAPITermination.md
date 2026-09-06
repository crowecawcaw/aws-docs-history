

# Change instance termination protection
<a name="Using_ChangingDisableAPITermination"></a>

To prevent your instance from being accidentally terminated using the Amazon EC2 API, whether you call `TerminateInstances` directly or using another interface such as the Amazon EC2 console, enable *termination protection* for the instance. The `DisableApiTermination` attribute controls whether the instance can be terminated. By default, termination protection is disabled for your instance. You can set the value of this attribute when you launch an instance, or while the instance is running or stopped.

The `DisableApiTermination` attribute doesn't prevent you from terminating an instance by initiating shutdown from the instance (for example, by using an operating system command for system shutdown) when the `InstanceInitiatedShutdownBehavior` attribute is set to `terminate`. For more information, see [Change instance initiated shutdown behavior](Using_ChangingInstanceInitiatedShutdownBehavior.md).

**Considerations**
+ Enabling termination protection does not prevent AWS from terminating the instance when there is a [scheduled event](monitoring-instances-status-check_sched.md) to terminate the instance.
+ Enabling termination protection does not prevent Amazon EC2 Auto Scaling from terminating an instance when the instance is unhealthy or during scale-in events. You can control whether an Auto Scaling group can terminate a particular instance when scaling using [instance scale-in protection](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-instance-protection.html). You can control whether an Auto Scaling group can terminate unhealthy instances by [suspending the ReplaceUnhealthy scaling process](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-suspend-resume-processes.html).
+ You can't enable termination protection for Spot Instances.

------
#### [ Console ]

**To enable termination protection for an instance at launch**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. On the dashboard, choose **Launch instance**.

1. Expand **Advanced details**. For **Termination protection**, select **Enable**.

1. When you are finishing specifying the details for your instance, choose **Launch instance**.

**To change termination protection for an instance**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, select **Instances**.

1. Select the instance.

1. Choose **Actions**, **Instance settings**, **Change termination protection**.

1. For **Termination protection** select or clear **Enable**.

1. Choose **Save**.

------
#### [ AWS CLI ]

**To enable termination protection for an instance**  
Use the [modify-instance-attribute](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-instance-attribute.html) command.

```
aws ec2 modify-instance-attribute \
    --instance-id {{i-1234567890abcdef0}} \
    --disable-api-termination
```

**To disable termination protection for an instance**  
Use the [modify-instance-attribute](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-instance-attribute.html) command.

```
aws ec2 modify-instance-attribute \
    --instance-id {{i-1234567890abcdef0}} \
    --no-disable-api-termination
```

------
#### [ PowerShell ]

**To enable termination protection for an instance**  
Use the [Edit-EC2InstanceAttribute](https://docs.aws.amazon.com/powershell/latest/reference/items/Edit-EC2InstanceAttribute.html) cmdlet.

```
Edit-EC2InstanceAttribute `
    -InstanceId {{i-1234567890abcdef0}} `
    -DisableApiTermination $true
```

**To disable termination protection for an instance**  
Use the [Edit-EC2InstanceAttribute](https://docs.aws.amazon.com/powershell/latest/reference/items/Edit-EC2InstanceAttribute.html) cmdlet.

```
Edit-EC2InstanceAttribute `
    -InstanceId {{i-1234567890abcdef0}} `
    -DisableApiTermination $false
```

------

## Terminate multiple instances with termination protection
<a name="terminate-multiple"></a>

If you terminate multiple instances across multiple Availability Zones in the same request, and one or more of the specified instances are enabled for termination protection, the request fails with the following results:
+ The specified instances that are in the same Availability Zone as the protected instance are not terminated.
+ The specified instances that are in different Availability Zones, where no other specified instances are protected, are successfully terminated.

**Example**  
Suppose that you have the following four instances across two Availability Zones.


<table>
<thead>
  <tr><th>Instance </th><th>Availability Zone</th><th>Terminate protection</th></tr>
</thead>
<tbody>
  <tr><td><b>Instance 1</b></td><td rowspan="2">AZ A</td><td><code>Disabled</code></td></tr>
  <tr><td><b>Instance 2</b></td><td><code>Disabled</code></td></tr>
  <tr><td><b>Instance 3</b></td><td rowspan="2">AZ B</td><td><code>Enabled</code></td></tr>
  <tr><td><b>Instance 4</b></td><td><code>Disabled</code></td></tr>
</tbody>
</table>


If you attempt to terminate all of these instances in the same request, the request reports failure with the following results:
+ **Instance 1** and **Instance 2** are successfully terminated because neither instance is enabled for termination protection.
+ **Instance 3** and **Instance 4** fail to terminate because **Instance 3** is enabled for termination protection.