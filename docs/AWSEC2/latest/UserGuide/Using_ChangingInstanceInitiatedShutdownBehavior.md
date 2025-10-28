# Change instance

initiated shutdown behavior

###### Warning

**Terminating an instance is permanent and irreversible.**

After you terminate an instance, you can no longer connect to it, and it can't be recovered.
All attached Amazon EBS volumes that are configured to be deleted on termination are also permanently
deleted and can't be recovered. All data stored on instance store volumes is permanently lost.
For more information, see [How instance termination
works](how-ec2-instance-termination-works.md "how-ec2-instance-termination-works.md").

Before you terminate an instance, ensure that you have backed up all data that you need to
retain after the termination to persistent storage.

By default, when you initiate a shutdown from an Amazon EBS backed instance (using a
command such as **shutdown** or **poweroff**), the
instance stops. You can change this behavior so that the instance terminates instead by
changing the `InstanceInitiatedShutdownBehavior` attribute for the instance.
You can change this attribute while the instance is running or stopped.

The **halt** command doesn't initiate a shutdown. If used, the instance
doesn't terminate; instead, it places the CPU into `HLT` and the instance
continues to run.

###### Note

The `InstanceInitiatedShutdownBehavior` attribute only applies when you
perform a shutdown from the operating system of the instance itself. It doesn't
apply when you stop an instance using the `StopInstances` API or the
Amazon EC2 console.

Console

###### To change the instance initiated shutdown behavior

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose
   **Instances**.
3. Select the instance.
4. Choose **Actions**, **Instance
   settings**, **Change shutdown
   behavior**.

**Shutdown behavior** displays the current
behavior. 5. To change the behavior, for **Shutdown
behavior**, choose **Stop** or
**Terminate**. 6. Choose **Save**.

AWS CLI

###### To change the instance initiated shutdown behavior

Use the [modify-instance-attribute](../../../cli/latest/reference/ec2/modify-instance-attribute.md "../../../cli/latest/reference/ec2/modify-instance-attribute.md") command.

```
aws ec2 modify-instance-attribute \
    --instance-id `i-1234567890abcdef0` \
    --instance-initiated-shutdown-behavior terminate
```

PowerShell

###### To change the instance initiated shutdown behavior

Use the [Edit-EC2InstanceAttribute](../../../powershell/latest/reference/items/Edit-EC2InstanceAttribute.md "../../../powershell/latest/reference/items/Edit-EC2InstanceAttribute.md") cmdlet.

```
Edit-EC2InstanceAttribute `
    -InstanceId `i-1234567890abcdef0` `
    -InstanceInitiatedShutdownBehavior terminate
```
