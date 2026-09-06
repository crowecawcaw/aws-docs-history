

# Troubleshoot Amazon EC2 instance termination issues
<a name="TroubleshootingInstancesShuttingDown"></a>

Shutting down or deleting your instance is known as instance termination. The following information can help you troubleshoot issues when you terminate your instance.

You are not billed for any instance usage while an instance is not in the `running` state. In other words, when you terminate an instance, you stop incurring charges for that instance as soon as its state changes to `shutting-down`.

## Instance terminates immediately
<a name="instance-terminates-immediately"></a>

Several issues can cause your instance to terminate immediately on start-up. See [Instance terminates immediately](troubleshooting-launch.md#troubleshooting-launch-internal) for more information.

## Delayed instance termination
<a name="instance-stuck-terminating"></a>

If your instance remains in the `shutting-down` state longer than a few minutes, it might be because:
+ The instance is running shutdown scripts.
+ There's a problem with the underlying host computer.

After several hours in the `shutting-down` state, Amazon EC2 treats the instance as stuck and forcibly terminates it.

To resolve a stuck instance yourself:

1. **Force terminate the instance**

   Use the Amazon EC2 console or the AWS CLI to force terminate the instance. For the steps, see [Force terminate an instance](#force-terminate-ec2-instance).

   The instance will first attempt a graceful shutdown, which includes flushing file system caches and metadata (although you can optionally bypass the graceful shutdown). If the graceful shutdown fails to complete within the timeout period, the instance shuts down forcibly without flushing the file system caches and metadata.

1. **If force terminate fails**

   If, after several hours, the instance has not terminated and it appears stuck terminating, do the following:

   1. Post a request for help on [AWS re:Post](https://repost.aws/). To help expedite a resolution, include the instance ID, and describe the steps that you've already taken.

   1. Alternatively, if you have a support plan, create a technical support case in the [Support Center](https://console.aws.amazon.com/support/home#/).

### Force terminate an instance
<a name="force-terminate-ec2-instance"></a>

If it appears that your instance is stuck terminating, you can force your instance to terminate. If, after several hours, the instance has not terminated, post a request for help to [AWS re:Post](https://repost.aws/). To help expedite a resolution, include the instance ID and describe the steps that you've already taken. Alternatively, if you have a support plan, create a technical support case in the [Support Center](https://console.aws.amazon.com/support/home#/).

------
#### [ Console ]

**To force terminate an instance**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Instances** and select the stuck instance.

1. Choose **Instance state**, **Force terminate instance**.

   Note that **Force terminate instance** is only available in the console if your instance is in the `stopping` state. If your instance is in another state (except `shutting-down` and `terminated`) you can use the AWS CLI to force terminate your instance.

1. (Optional) To bypass the graceful OS shutdown during the force terminate, select the **Skip OS shutdown** checkbox.

1. Choose **Force terminate**.

------
#### [ AWS CLI ]

**To force terminate an instance**  
Use the [terminate-instances](https://docs.aws.amazon.com/cli/latest/reference/ec2/terminate-instances.html) command with the `--force` option.

```
aws ec2 terminate-instances \
    --instance-ids {{i-1234567890abcdef0}} \
    --force
```

To bypass the graceful OS shutdown during force terminate, include the `--skip-os-shutdown` option.

```
aws ec2 terminate-instances \
    --instance-ids {{i-1234567890abcdef0}} \
    --force \
    --skip-os-shutdown
```

------
#### [ PowerShell ]

**To force terminate an instance**  
Use the [Remove-EC2Instance](https://docs.aws.amazon.com/powershell/latest/reference/items/Remove-EC2Instance.html) cmdlet and set `-Enforce` to `true`.

```
Remove-EC2Instance `
    -InstanceId {{i-1234567890abcdef0}} `
    -Enforce $true
```

To bypass the graceful OS shutdown during force terminate, include `-SkipOsShutdown $true`.

```
Remove-EC2Instance `
    -InstanceId {{i-1234567890abcdef0}} `
    -Enforce $true `
    -SkipOsShutdown $true
```

------

## Terminated instance still displayed
<a name="terminated-instance-still-displaying"></a>

After you terminate an instance, it remains visible for a short while before being deleted. The state shows as `terminated`. If the entry is not deleted after several hours, contact Support.

## Error: The instance may not be terminated. Modify its 'disableApiTermination' instance attribute
<a name="termination-protection-enabled"></a>

If you try to terminate an instance and get the `The instance {{i-1234567890abcdef0}} may not be terminated. Modify its 'disableApiTermination' instance attribute` error message, it indicates that the instance has been enabled for termination protection. Termination protection prevents the instance from being accidentally terminated.

You must disable termination protection before you can terminate the instance.

For more information, see [Change instance termination protection](Using_ChangingDisableAPITermination.md).

## Instances automatically launched or terminated
<a name="automatic-instance-create-or-delete"></a>

Generally, the following behaviors mean that you've used Amazon EC2 Auto Scaling, EC2 Fleet, or Spot Fleet to scale your computing resources automatically based on criteria that you've defined:
+ You terminate an instance and a new instance launches automatically.
+ You launch an instance and one of your instances terminates automatically.
+ You stop an instance and it terminates and a new instance launches automatically.

To stop automatic scaling, find the Auto Scaling group or the fleet that is launching the instances and either set its capacity to 0 or delete it.